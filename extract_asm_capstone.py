#!/usr/bin/env python3
"""
Extract assembly code using capstone disassembler
Works directly on the binary without needing IDA/Ghidra
"""

import struct
from capstone import *
from capstone.x86 import *
import os

# All TVN vtables
TVN_VTABLES = {
    "TVNCommand": 0x0040E1E0,
    "TVNFrame_1": 0x00435B50,
    "TVNFrame_2": 0x00435DD4,
    "TVNHotspot": 0x00413514,
    "TVNImageObject_1": 0x00429980,
    "TVNImageObject_2": 0x004299D0,
    "TVNTimer": 0x004394D4,
}


def read_dword(data, offset):
    """Read DWORD at offset"""
    if offset < 0 or offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def is_valid_code_pointer(addr):
    """Check if address is valid code"""
    return 0x00401000 <= addr <= 0x00500000


def extract_vtable_methods(data, vtable_va):
    """Extract method addresses from vtable"""
    file_offset = vtable_va - 0x00400000
    methods = []

    for offset in range(0, 0x40, 4):
        method_addr = read_dword(data, file_offset + offset)
        if method_addr == 0:
            break
        if not is_valid_code_pointer(method_addr):
            if offset == 0:
                break
            break
        methods.append({
            'index': offset // 4,
            'address': method_addr
        })

    return methods


def find_function_end(data, start_addr, max_size=2000):
    """
    Find function end by looking for common patterns:
    - ret instruction
    - Multiple consecutive 0xCC (int3 padding)
    - Jump to next function
    """
    file_offset = start_addr - 0x00400000

    # Initialize disassembler
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    end_offset = file_offset
    last_ret = None
    cc_count = 0

    try:
        for i in md.disasm(data[file_offset:file_offset+max_size], start_addr):
            end_offset = (i.address + i.size) - 0x00400000

            # Check for ret instruction
            if i.mnemonic == 'ret':
                last_ret = i.address + i.size
                # Continue a bit to catch any padding

            # Check for int3 padding after ret
            if last_ret and i.mnemonic == 'int3':
                cc_count += 1
                if cc_count >= 3:  # 3+ int3 = end of function
                    return last_ret
            else:
                cc_count = 0

    except Exception as e:
        pass

    # If we found a ret, use that
    if last_ret:
        return last_ret

    # Otherwise, estimate based on bytes read
    return start_addr + min(500, max_size)


def disassemble_function(data, func_addr):
    """Disassemble a function using capstone"""
    file_offset = func_addr - 0x00400000

    if file_offset < 0 or file_offset >= len(data):
        return None

    # Find function end
    func_end = find_function_end(data, func_addr)
    func_size = func_end - func_addr

    # Initialize disassembler
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True
    md.syntax = CS_OPT_SYNTAX_INTEL

    lines = []
    strings = []
    calls = []

    try:
        for i in md.disasm(data[file_offset:file_offset+func_size], func_addr):
            # Format instruction
            bytes_str = ' '.join([f'{b:02x}' for b in i.bytes])
            line = f"{i.address:08x}  {bytes_str:24s}  {i.mnemonic:8s} {i.op_str}"
            lines.append(line)

            # Extract strings and calls
            if i.mnemonic == 'call':
                # Get target address
                if i.operands and i.operands[0].type == X86_OP_IMM:
                    target = i.operands[0].imm
                    if is_valid_code_pointer(target):
                        calls.append({
                            'addr': i.address,
                            'target': target
                        })

            # Look for string references (push offset str_*)
            if i.mnemonic == 'push' or i.mnemonic == 'mov':
                if i.operands and len(i.operands) > 0:
                    for op in i.operands:
                        if op.type == X86_OP_IMM:
                            addr = op.imm
                            # Check if it's a data address
                            if 0x00400000 <= addr < 0x00500000:
                                str_offset = addr - 0x00400000
                                if str_offset < len(data):
                                    # Try to read as string
                                    string = extract_string_at(data, str_offset)
                                    if string and len(string) > 3:
                                        strings.append({
                                            'addr': i.address,
                                            'ref_addr': addr,
                                            'value': string
                                        })

    except Exception as e:
        lines.append(f"; Error disassembling: {e}")

    return {
        'lines': lines,
        'strings': strings,
        'calls': calls,
        'size': func_size
    }


def extract_string_at(data, offset, max_len=100):
    """Extract null-terminated string at offset"""
    try:
        end = offset
        while end < len(data) and end < offset + max_len:
            if data[end] == 0:
                break
            # Check if printable
            if data[end] < 32 or data[end] > 126:
                if data[end] != 0:
                    return None
            end += 1

        if end - offset < 4:  # Too short
            return None

        string = data[offset:end].decode('ascii', errors='ignore')
        # Check if it looks like a string
        if len(string) >= 3 and all(c.isprintable() or c == '\t' or c == '\n' for c in string):
            return string
    except:
        pass
    return None


def identify_important_calls(calls):
    """Identify important calls based on common addresses"""
    # These are common function addresses in Borland C++ RTL
    important_funcs = {
        0x00440090: "TProfile_related",
        0x0043BA0C: "Destructor_common",
        # Add more as we find them
    }

    important = []
    other = []

    for call in calls:
        if call['target'] in important_funcs:
            call['name'] = important_funcs[call['target']]
            important.append(call)
        else:
            call['name'] = f"sub_{call['target']:X}"
            other.append(call)

    return important, other


def extract_method_complete(data, method, method_index, output_file):
    """Extract complete assembly for one method"""

    f = output_file

    f.write(f"## Method [{method_index}]: 0x{method['address']:08X}\n\n")
    f.write(f"**Address**: 0x{method['address']:08X}\n")
    f.write(f"**Index in vtable**: {method['index']}\n\n")

    print(f"  [{method_index}] Disassembling 0x{method['address']:08X}...")

    # Disassemble
    result = disassemble_function(data, method['address'])

    if not result or not result['lines']:
        f.write("⚠️ **Could not disassemble function**\n\n")
        f.write("---\n\n")
        return

    f.write(f"**Size**: ~{result['size']} bytes\n\n")

    # Write assembly
    f.write("### Assembly Code\n\n")
    f.write("```assembly\n")
    for line in result['lines']:
        f.write(line + "\n")
    f.write("```\n\n")

    # Write strings
    if result['strings']:
        f.write("### String References\n\n")
        for s in result['strings']:
            f.write(f"- `{s['addr']:08x}` → `0x{s['ref_addr']:08x}`: \"{s['value']}\"\n")
        f.write("\n")

    # Write calls
    if result['calls']:
        important, other = identify_important_calls(result['calls'])

        f.write("### Function Calls\n\n")

        if important:
            f.write("**Important Calls**:\n\n")
            for call in important:
                f.write(f"- ⭐ `{call['addr']:08x}` → `{call['name']}` @ `0x{call['target']:08X}`\n")
            f.write("\n")

        if other:
            f.write("**Other Calls**:\n\n")
            for call in other[:20]:
                f.write(f"- `{call['addr']:08x}` → `{call['name']}`\n")
            if len(other) > 20:
                f.write(f"- ... and {len(other) - 20} more\n")
            f.write("\n")

    f.write("---\n\n")


def extract_tvn_structure(data, struct_name, vtable_va, output_dir):
    """Extract all methods for one TVN structure"""

    print(f"\n{'='*100}")
    print(f"EXTRACTING: {struct_name}")
    print(f"Vtable @ 0x{vtable_va:08X}")
    print(f"{'='*100}")

    # Extract methods
    methods = extract_vtable_methods(data, vtable_va)

    if not methods:
        print(f"  ⚠️ No methods found")
        return

    print(f"  Found {len(methods)} method(s)")

    # Create output file
    output_file = os.path.join(output_dir, f"{struct_name}_COMPLETE.md")

    with open(output_file, 'w') as f:
        # Header
        f.write(f"# {struct_name} - Complete Assembly Extraction\n\n")
        f.write(f"**Vtable Address**: 0x{vtable_va:08X}\n")
        f.write(f"**Binary**: europeo.exe\n")
        f.write(f"**Tool**: Capstone Disassembler\n")
        f.write(f"**Date**: 2026-01-16\n\n")
        f.write("---\n\n")

        # Summary
        f.write("## Methods Summary\n\n")
        f.write("| Index | Address |\n")
        f.write("|-------|----------|\n")
        for method in methods:
            f.write(f"| {method['index']:2d} | 0x{method['address']:08X} |\n")
        f.write("\n---\n\n")

        # Extract each method
        for i, method in enumerate(methods):
            extract_method_complete(data, method, i, f)

    print(f"  ✓ Saved to {struct_name}_COMPLETE.md")


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: extract_asm_capstone.py <europeo.exe> [output_dir]")
        sys.exit(1)

    binary_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "TVN_ASM_CAPSTONE"

    print("="*100)
    print("EXTRACTING ALL TVN METHODS ASSEMBLY - CAPSTONE")
    print("="*100)
    print()

    # Read binary
    with open(binary_path, 'rb') as f:
        data = f.read()

    print(f"Binary loaded: {len(data)} bytes")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}\n")

    # Extract each structure
    for struct_name, vtable_va in TVN_VTABLES.items():
        extract_tvn_structure(data, struct_name, vtable_va, output_dir)

    print("\n" + "="*100)
    print("EXTRACTION COMPLETE!")
    print("="*100)
    print(f"\nOutput directory: {output_dir}")
    print(f"Files created: {len(TVN_VTABLES)}")
    print("\nDone! ✓")


if __name__ == "__main__":
    main()
