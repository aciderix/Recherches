#!/usr/bin/env python3
"""
Complete TVN extractor using Capstone
Uses all the vtable addresses we discovered
"""

import struct
from capstone import *
import sys
import os

# All TVN structures with their vtable addresses
TVN_STRUCTURES = {
    # Parms structures (16) - share base vtable 0x0040E1E0
    "TVNProjectParms": 0x0040E1E0,
    "TVNMidiParms": 0x0040E1E0,
    "TVNDigitParms": 0x0040E1E0,
    "TVNHtmlParms": 0x0040E1E0,
    "TVNImageParms": 0x0040E1E0,
    "TVNImgObjParms": 0x0040E1E0,
    "TVNImgSeqParms": 0x0040E1E0,
    "TVNExecParms": 0x0040E1E0,
    "TVNSetVarParms": 0x0040E1E0,
    "TVNIfParms": 0x0040E1E0,
    "TVNTextParms": 0x0040E1E0,
    "TVNTextObjParms": 0x0040E1E0,
    "TVNFontParms": 0x0040E1E0,
    "TVNCommand": 0x0040E1E0,
    "TVNSceneParms": 0x0040E1E0,
    "TVNStringParms": 0x0040E1E0,

    # Specific vtables (6)
    "TVNFrame_1": 0x00435B50,
    "TVNFrame_2": 0x00435DD4,
    "TVNHotspot": 0x00413514,
    "TVNImageObject_1": 0x00429980,
    "TVNImageObject_2": 0x004299D0,
    "TVNTimer": 0x004394D4,

    # Found by automated search (3)
    "TVNImageObject": 0x0042A517,
    "TVNTextObject": 0x0042A3D0,
    "TVNScene": 0x00417B52,
}


def parse_pe_sections(data):
    """Parse PE sections"""
    pe_offset = struct.unpack('<I', data[0x3C:0x40])[0]
    coff_offset = pe_offset + 4
    num_sections = struct.unpack('<H', data[coff_offset+2:coff_offset+4])[0]
    size_of_optional = struct.unpack('<H', data[coff_offset+16:coff_offset+18])[0]
    section_offset = coff_offset + 20 + size_of_optional

    sections = []
    for i in range(num_sections):
        sec_data = data[section_offset + i*40:section_offset + (i+1)*40]
        name = sec_data[0:8].rstrip(b'\x00').decode('ascii', errors='ignore')
        virtual_size = struct.unpack('<I', sec_data[8:12])[0]
        virtual_addr = struct.unpack('<I', sec_data[12:16])[0]
        size_of_raw = struct.unpack('<I', sec_data[16:20])[0]
        ptr_to_raw = struct.unpack('<I', sec_data[20:24])[0]

        sections.append({
            'Name': name,
            'VirtualSize': virtual_size,
            'VirtualAddress': virtual_addr,
            'SizeOfRawData': size_of_raw,
            'PointerToRawData': ptr_to_raw
        })

    return sections


def va_to_file_offset(va, sections):
    """Convert VA to file offset"""
    va_no_base = va - 0x00400000 if va >= 0x00400000 else va

    for section in sections:
        virt_start = section['VirtualAddress']
        virt_end = virt_start + section['VirtualSize']

        if virt_start <= va_no_base < virt_end:
            offset_in_section = va_no_base - virt_start
            file_offset = section['PointerToRawData'] + offset_in_section

            # Make sure we're within the raw data size
            if offset_in_section < section['SizeOfRawData']:
                return file_offset

    return None


def read_dword(data, offset):
    """Read DWORD at file offset"""
    if offset < 0 or offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def read_vtable(data, sections, vtable_va):
    """Read all method pointers from a vtable"""
    vtable_offset = va_to_file_offset(vtable_va, sections)
    if vtable_offset is None:
        return None

    methods = []
    for i in range(32):  # Max 32 methods
        method_va = read_dword(data, vtable_offset + i*4)

        if method_va is None or method_va == 0:
            break

        # Valid code pointer check
        if not (0x00401000 <= method_va <= 0x00500000):
            if i == 0:
                return None  # First must be valid
            break

        methods.append(method_va)

    return methods if len(methods) >= 2 else None


def find_function_end(data, sections, start_va, max_size=0x2000):
    """Find where a function ends by looking for ret instructions"""
    start_offset = va_to_file_offset(start_va, sections)
    if start_offset is None:
        return None

    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    # Read up to max_size bytes
    code_bytes = data[start_offset:start_offset + max_size]

    last_ret = None
    for i in md.disasm(code_bytes, start_va):
        # Look for return instructions
        if i.mnemonic in ['ret', 'retn']:
            last_ret = i.address + i.size
        # Also look for unconditional jumps out
        elif i.mnemonic == 'jmp' and len(i.operands) > 0:
            if i.operands[0].type == CS_OP_IMM:
                target = i.operands[0].imm
                # If jumping far away, might be end
                if abs(target - i.address) > 0x100:
                    if last_ret:
                        return last_ret
        # If we hit padding (CC bytes), function likely ended
        elif i.mnemonic == 'int3':
            if last_ret:
                return last_ret

    return last_ret if last_ret else (start_va + 0x100)  # Default small size


def disassemble_function(data, sections, func_va):
    """Disassemble a complete function"""
    func_offset = va_to_file_offset(func_va, sections)
    if func_offset is None:
        return None

    # Find function end
    end_va = find_function_end(data, sections, func_va)
    if end_va is None:
        end_va = func_va + 0x100  # Default

    func_size = end_va - func_va
    if func_size > 0x2000:
        func_size = 0x2000

    code_bytes = data[func_offset:func_offset + func_size]

    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    instructions = []
    data_refs = []

    for i in md.disasm(code_bytes, func_va):
        instructions.append({
            'address': i.address,
            'mnemonic': i.mnemonic,
            'op_str': i.op_str,
            'bytes': i.bytes
        })

        # Extract data references
        if i.operands:
            for op in i.operands:
                if op.type == CS_OP_MEM:
                    # Memory operand might reference data
                    if hasattr(op.mem, 'disp') and op.mem.disp != 0:
                        addr = op.mem.disp
                        if 0x00400000 <= addr <= 0x00500000:
                            data_refs.append(addr)
                elif op.type == CS_OP_IMM:
                    # Immediate might be an address
                    addr = op.imm
                    if 0x00400000 <= addr <= 0x00500000:
                        data_refs.append(addr)

    return {
        'instructions': instructions,
        'data_refs': list(set(data_refs)),
        'size': func_size
    }


def extract_string_at_address(data, sections, addr):
    """Try to extract a string at an address"""
    offset = va_to_file_offset(addr, sections)
    if offset is None:
        return None

    # Try to read as ASCII string
    string_bytes = []
    for i in range(256):
        if offset + i >= len(data):
            break
        byte = data[offset + i]
        if byte == 0:
            break
        if 32 <= byte <= 126:  # Printable ASCII
            string_bytes.append(byte)
        else:
            break

    if len(string_bytes) >= 3:  # At least 3 chars
        try:
            return bytes(string_bytes).decode('ascii')
        except:
            pass

    return None


def format_assembly(func_data):
    """Format assembly instructions as markdown"""
    lines = []
    lines.append("```assembly")

    for instr in func_data['instructions']:
        addr = instr['address']
        mnem = instr['mnemonic']
        ops = instr['op_str']

        # Format nicely
        line = f"{addr:08X}  {mnem:8s} {ops}"
        lines.append(line)

    lines.append("```")
    return '\n'.join(lines)


def extract_structure(data, sections, struct_name, vtable_va):
    """Extract all info for one structure"""
    print(f"\n{'='*80}")
    print(f"EXTRACTING: {struct_name}")
    print(f"Vtable: 0x{vtable_va:08X}")
    print(f"{'='*80}")

    result = {
        'struct_name': struct_name,
        'vtable_va': vtable_va,
        'methods': []
    }

    # Read vtable
    method_vas = read_vtable(data, sections, vtable_va)
    if not method_vas:
        print(f"  ⚠️  Could not read vtable")
        return None

    print(f"  Found {len(method_vas)} method(s)")

    # Disassemble each method
    for idx, method_va in enumerate(method_vas):
        print(f"  [{idx}] Disassembling method @ 0x{method_va:08X}...")

        func_data = disassemble_function(data, sections, method_va)
        if not func_data:
            print(f"      ⚠️  Could not disassemble")
            continue

        # Extract strings from data refs
        strings = []
        for ref in func_data['data_refs']:
            string = extract_string_at_address(data, sections, ref)
            if string:
                strings.append({
                    'address': ref,
                    'value': string
                })

        result['methods'].append({
            'index': idx,
            'address': method_va,
            'name': 'destructor' if idx == 0 else f'method_{idx}',
            'assembly': func_data,
            'strings': strings
        })

        print(f"      ✓ {len(func_data['instructions'])} instructions, {len(strings)} strings")

    print(f"  ✓ Extraction complete")
    return result


def save_structure_markdown(result, output_dir):
    """Save structure to markdown file"""
    if not result:
        return

    struct_name = result['struct_name']
    filename = os.path.join(output_dir, f"{struct_name}_EXTRACTED.md")

    with open(filename, 'w') as f:
        f.write(f"# {struct_name} - Complete Extraction\n\n")
        f.write(f"**Structure**: {struct_name}\n")
        f.write(f"**Vtable Address**: 0x{result['vtable_va']:08X}\n")
        f.write(f"**Binary**: europeo.exe\n")
        f.write(f"**Tool**: Capstone Disassembler\n\n")
        f.write("---\n\n")

        # Methods summary
        f.write("## Methods Summary\n\n")
        f.write("| Index | Address | Name | Instructions |\n")
        f.write("|-------|---------|------|-------------|\n")

        for method in result['methods']:
            idx = method['index']
            addr = method['address']
            name = method['name']
            num_instr = len(method['assembly']['instructions'])
            f.write(f"| {idx:2d} | 0x{addr:08X} | `{name}` | {num_instr} |\n")

        f.write("\n---\n\n")

        # Each method detail
        for method in result['methods']:
            idx = method['index']
            addr = method['address']
            name = method['name']

            f.write(f"## Method [{idx}]: {name}\n\n")
            f.write(f"**Address**: 0x{addr:08X}\n")
            f.write(f"**Index in vtable**: {idx}\n")
            f.write(f"**Name**: `{name}`\n\n")

            # Assembly code
            f.write("### Assembly Code\n\n")
            f.write(format_assembly(method['assembly']))
            f.write("\n\n")

            # Strings found
            if method['strings']:
                f.write("### Strings Referenced\n\n")
                for s in method['strings']:
                    f.write(f"- `\"{s['value']}\"` @ 0x{s['address']:08X}\n")
                f.write("\n")

            # Data references
            if method['assembly']['data_refs']:
                f.write("### Data References\n\n")
                for ref in method['assembly']['data_refs']:
                    f.write(f"- 0x{ref:08X}\n")
                f.write("\n")

            f.write("---\n\n")

    print(f"  ✓ Saved to {filename}")


def main():
    if len(sys.argv) < 2:
        print("Usage: extract_tvn_with_capstone.py <europeo.exe>")
        sys.exit(1)

    binary_path = sys.argv[1]
    output_dir = "TVN_EXTRACTED_CAPSTONE"

    print("="*80)
    print("TVN STRUCTURE EXTRACTOR - CAPSTONE")
    print("="*80)
    print()
    print(f"Binary: {binary_path}")
    print(f"Output: {output_dir}/")
    print(f"Structures: {len(TVN_STRUCTURES)}")
    print()

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Load binary
    with open(binary_path, 'rb') as f:
        data = f.read()

    print(f"Binary loaded: {len(data)} bytes")

    # Parse PE
    sections = parse_pe_sections(data)
    print(f"PE sections: {len(sections)}")
    print()

    # Extract each structure
    results = []
    for struct_name, vtable_va in TVN_STRUCTURES.items():
        result = extract_structure(data, sections, struct_name, vtable_va)
        if result:
            save_structure_markdown(result, output_dir)
            results.append(result)

    # Summary
    print()
    print("="*80)
    print("EXTRACTION COMPLETE")
    print("="*80)
    print()
    print(f"Total structures: {len(TVN_STRUCTURES)}")
    print(f"Successfully extracted: {len(results)}")
    print(f"Output directory: {output_dir}/")
    print()
    print("✓ Done!")


if __name__ == "__main__":
    main()
