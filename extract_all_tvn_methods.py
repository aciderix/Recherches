#!/usr/bin/env python3
"""
Extract ALL methods from ALL TVN structures
Finds vtables, extracts method pointers, and attempts to identify method roles
"""

import struct
import subprocess
from collections import defaultdict


def read_dword(data, offset):
    """Read a DWORD (uint32) at offset"""
    if offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def read_bytes(data, offset, count):
    """Read count bytes at offset"""
    if offset + count > len(data):
        return None
    return data[offset:offset+count]


def is_valid_code_ptr(addr, data):
    """Check if address is a valid code pointer (in .text section)"""
    # For europeo.exe, code section is typically 0x00401000 - 0x00440000
    if addr < 0x00401000 or addr > 0x00450000:
        return False

    # Check if it points to valid code (common x86 opcodes at start)
    file_offset = addr - 0x00400000  # PE base is usually 0x00400000
    if file_offset < 0 or file_offset >= len(data):
        return False

    # Check for common function prologues
    first_bytes = read_bytes(data, file_offset, 4)
    if not first_bytes:
        return False

    # Common prologues: 55 (push ebp), 8B FF (mov edi,edi), 53 (push ebx), 56 (push esi)
    if first_bytes[0] in [0x55, 0x53, 0x56, 0x57, 0x8B, 0x6A, 0xFF, 0x33, 0xE8]:
        return True

    return False


def find_vtable_near_string(data, string_offset, struct_name):
    """Find vtable near a type string"""

    # Search backwards and forwards from string
    search_ranges = [
        (max(0, string_offset - 0x200), string_offset),  # Before
        (string_offset, min(len(data), string_offset + 0x200))  # After
    ]

    vtables = []

    for start, end in search_ranges:
        # Align to 4-byte boundaries
        start = (start // 4) * 4

        for offset in range(start, end, 4):
            ptr = read_dword(data, offset)
            if not ptr or not is_valid_code_ptr(ptr, data):
                continue

            # Check if this could be the start of a vtable
            # Vtables have multiple consecutive valid code pointers
            methods = []
            current_offset = offset

            for i in range(20):  # Check up to 20 method slots
                method_ptr = read_dword(data, current_offset)
                if not method_ptr:
                    break

                if is_valid_code_ptr(method_ptr, data):
                    methods.append(method_ptr)
                    current_offset += 4
                elif method_ptr == 0:
                    # NULL pointer = end of vtable or gap
                    break
                else:
                    # Not a code pointer, might be data or end of vtable
                    if len(methods) >= 3:  # Valid vtable needs at least 3 methods
                        break
                    else:
                        methods = []
                        break

            if len(methods) >= 3:
                vtables.append({
                    'offset': offset,
                    'methods': methods
                })

    return vtables


def disasm_function_start(data, addr, lines=10):
    """Disassemble first few instructions of a function"""
    file_offset = addr - 0x00400000

    if file_offset < 0 or file_offset >= len(data):
        return None

    # Extract bytes
    code_bytes = read_bytes(data, file_offset, min(50, len(data) - file_offset))
    if not code_bytes:
        return None

    # Try using objdump for disassembly
    try:
        # Write to temp file
        import tempfile
        import os

        with tempfile.NamedTemporaryFile(delete=False, suffix='.bin') as f:
            f.write(code_bytes)
            temp_path = f.name

        # Disassemble with objdump
        result = subprocess.run(
            ['objdump', '-D', '-b', 'binary', '-m', 'i386', '--adjust-vma=0x400000', temp_path],
            capture_output=True,
            text=True,
            timeout=2
        )

        os.unlink(temp_path)

        if result.returncode == 0:
            disasm_lines = result.stdout.split('\n')[7:7+lines]  # Skip header
            return '\n'.join(disasm_lines)
    except:
        pass

    # Fallback: show hex
    return code_bytes[:20].hex()


def identify_method_role(data, method_addr, method_index):
    """Try to identify the role of a method based on patterns"""

    file_offset = method_addr - 0x00400000
    if file_offset < 0 or file_offset >= len(data):
        return "Unknown"

    # Read first 50 bytes of function
    code = read_bytes(data, file_offset, 50)
    if not code:
        return "Unknown"

    # Pattern matching for common method types

    # Constructor: often has multiple string::string() calls
    if method_index == 0 and code.count(b'\xE8') >= 3:  # Multiple CALL instructions
        return "Constructor/Init"

    # Destructor: often ends with retn and has cleanup
    if b'\xC3' in code[:10]:  # RETN early
        return "Destructor/Release"

    # Load/Read methods: often have file I/O calls
    if b'GetString' in data[file_offset:file_offset+200]:
        return "Load/Parse"

    if b'GetInt' in data[file_offset:file_offset+200]:
        return "Load/Parse"

    # Execute methods: often longer and call other methods
    if len(code) > 40 and code.count(b'\xE8') >= 5:
        return "Execute/Process"

    # Virtual methods often start with mov eax, [ecx]
    if code[0:2] == b'\x8B\x01':  # mov eax, [ecx]
        return "Virtual Dispatcher"

    # Standard prologue
    if code[0] == 0x55:  # push ebp
        if code[1:3] == b'\x8B\xEC':  # mov ebp, esp
            return "Standard Method"

    return f"Method{method_index}"


def extract_all_tvn_methods(filepath):
    """Extract all methods from all TVN structures"""

    with open(filepath, 'rb') as f:
        data = f.read()

    print("=" * 100)
    print("EXTRACTING ALL TVN METHODS FROM ALL 35 STRUCTURES")
    print("=" * 100)
    print()

    # All TVN structures
    tvn_structures = {
        # Parms structures
        "TVNProjectParms": 0x0000e20e,
        "TVNMidiParms": 0x0000e22c,
        "TVNDigitParms": 0x0000e247,
        "TVNHtmlParms": 0x0000e263,
        "TVNImageParms": 0x0000e27e,
        "TVNImgObjParms": 0x0000e29a,
        "TVNImgSeqParms": 0x0000e2b7,
        "TVNExecParms": 0x0000e2d4,
        "TVNSetVarParms": 0x0000e2ef,
        "TVNIfParms": 0x0000e30c,
        "TVNTextParms": 0x0000e381,
        "TVNTextObjParms": 0x0000e39c,
        "TVNFontParms": 0x0000e3ba,
        "TVNSceneParms": 0x0000e3ee,
        "TVNFileNameParms": 0x0000e9da,

        # Class structures
        "TVNCommand": 0x0000e3d5,
        "TVNEventCommand": 0x0000eb2a,
        "TVNVariable": 0x00005e04,
        "TVNScene": 0x00016fbb,
        "TVNHotspot": 0x000135bc,
        "TVNTimer": 0x00019bdf,
        "TVNWaveMedia": 0x0001bb29,
        "TVNMidiMedia": 0x0001bb9c,
        "TVNBitmap": 0x0001dc08,
        "TVNGdiObject": 0x0001dc7f,
        "TVNHtmlText": 0x000227fc,
        "TVNImageObject": 0x00029a17,
        "TVNTextObject": 0x00029a54,
        "TVNBmpImg": 0x00034edb,
        "TVNToolBar": 0x00034f0d,
        "TVNWindow": 0x00034f2d,
        "TVNCDAMedia": 0x00034f45,
        "TVNAviMedia": 0x00034f5f,
        "TVNFrame": 0x0003603c,
        "TVNApplication": 0x00038086,
    }

    all_results = {}

    for struct_name, string_offset in sorted(tvn_structures.items(), key=lambda x: x[1]):
        print(f"\n{'='*100}")
        print(f"ANALYZING: {struct_name}")
        print(f"String offset: 0x{string_offset:08x}")
        print(f"{'='*100}")

        # Find vtables near this string
        vtables = find_vtable_near_string(data, string_offset, struct_name)

        if not vtables:
            print(f"  ⚠️  No vtable found for {struct_name}")
            all_results[struct_name] = {'vtables': [], 'methods_count': 0}
            continue

        print(f"  ✓ Found {len(vtables)} potential vtable(s)")

        struct_results = {
            'string_offset': string_offset,
            'vtables': []
        }

        for vtable_idx, vtable in enumerate(vtables):
            print(f"\n  Vtable #{vtable_idx+1} @ 0x{vtable['offset']:08x} ({len(vtable['methods'])} methods)")
            print(f"  {'-'*96}")

            vtable_info = {
                'offset': vtable['offset'],
                'methods': []
            }

            for method_idx, method_addr in enumerate(vtable['methods']):
                role = identify_method_role(data, method_addr, method_idx)

                print(f"    [{method_idx:2d}] 0x{method_addr:08x}  {role:25s}", end='')

                # Try to disassemble first instruction
                disasm = disasm_function_start(data, method_addr, lines=1)
                if disasm and '\t' in disasm:
                    first_instr = disasm.split('\t', 1)[1].split('\n')[0][:40]
                    print(f"  {first_instr}")
                else:
                    print()

                vtable_info['methods'].append({
                    'index': method_idx,
                    'address': method_addr,
                    'role': role
                })

            struct_results['vtables'].append(vtable_info)

        all_results[struct_name] = struct_results
        print()

    # Summary
    print("\n" + "=" * 100)
    print("SUMMARY - ALL TVN STRUCTURES")
    print("=" * 100)
    print()

    total_vtables = 0
    total_methods = 0

    for struct_name in sorted(tvn_structures.keys()):
        result = all_results.get(struct_name, {})
        vtables = result.get('vtables', [])
        num_vtables = len(vtables)
        num_methods = sum(len(v['methods']) for v in vtables)

        total_vtables += num_vtables
        total_methods += num_methods

        status = "✓" if num_vtables > 0 else "✗"
        print(f"  {status} {struct_name:25s}  {num_vtables} vtable(s), {num_methods:3d} methods")

    print()
    print(f"TOTAL: {total_vtables} vtables, {total_methods} methods extracted")
    print()

    return all_results


def save_results(results, output_file):
    """Save results to markdown file"""

    with open(output_file, 'w') as f:
        f.write("# All TVN Methods Extraction Results\n\n")
        f.write("Complete extraction of all vtables and methods from 35 TVN structures.\n\n")
        f.write("---\n\n")

        for struct_name, data in sorted(results.items()):
            f.write(f"## {struct_name}\n\n")

            if not data.get('vtables'):
                f.write("**No vtable found**\n\n")
                continue

            f.write(f"**String offset**: 0x{data['string_offset']:08x}\n\n")

            for vtable_idx, vtable in enumerate(data['vtables']):
                f.write(f"### Vtable #{vtable_idx+1} @ 0x{vtable['offset']:08x}\n\n")
                f.write("| Index | Address | Role |\n")
                f.write("|-------|---------|------|\n")

                for method in vtable['methods']:
                    f.write(f"| {method['index']:2d} | 0x{method['address']:08x} | {method['role']} |\n")

                f.write("\n")

            f.write("---\n\n")

    print(f"✓ Results saved to {output_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: extract_all_tvn_methods.py <europeo.exe> [output.md]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "TVN_ALL_METHODS_EXTRACTED.md"

    results = extract_all_tvn_methods(filepath)
    save_results(results, output_file)
