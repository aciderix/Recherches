#!/usr/bin/env python3
"""
Standalone vtable finder that works without IDA
Searches for vtables by analyzing the binary directly
"""

import struct
import sys
import os

# Structures with missing vtables
MISSING_STRUCTURES = [
    "TVNFileNameParms",
    "TVNEventCommand",
    "TVNVariable",
    "TVNScene",
    "TVNToolBar",
    "TVNWindow",
    "TVNApplication",
    "TVNAviMedia",
    "TVNWaveMedia",
    "TVNMidiMedia",
    "TVNCDAMedia",
    "TVNBitmap",
    "TVNGdiObject",
    "TVNHtmlText",
    "TVNImageObject",
    "TVNTextObject",
    "TVNBmpImg",
]


def read_dword(data, offset):
    """Read DWORD at offset"""
    if offset < 0 or offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def is_valid_code_pointer(addr):
    """Check if address is valid code"""
    return 0x00401000 <= addr <= 0x00500000


def check_vtable_validity(data, file_offset):
    """Check if a file offset looks like a valid vtable"""
    methods = []

    for offset in range(0, 0x40, 4):  # Check up to 16 methods
        method_ptr = read_dword(data, file_offset + offset)

        if method_ptr is None or method_ptr == 0:
            break

        if not is_valid_code_pointer(method_ptr):
            if offset == 0:
                return None  # First entry must be valid
            break

        methods.append(method_ptr)

    if len(methods) >= 2:  # At least 2 methods
        return methods

    return None


def find_string_in_binary(data, search_str):
    """Find all occurrences of a string in binary data"""
    search_bytes = search_str.encode('ascii') + b'\x00'
    occurrences = []

    offset = 0
    while True:
        offset = data.find(search_bytes, offset)
        if offset == -1:
            break
        occurrences.append(offset)
        offset += 1

    return occurrences


def va_to_file_offset(va, sections):
    """Convert virtual address to file offset using PE sections"""
    for section in sections:
        virt_start = section['VirtualAddress']
        virt_end = virt_start + section['VirtualSize']

        if virt_start <= va < virt_end:
            offset_in_section = va - virt_start
            return section['PointerToRawData'] + offset_in_section

    return None


def file_offset_to_va(offset, sections):
    """Convert file offset to virtual address using PE sections"""
    for section in sections:
        file_start = section['PointerToRawData']
        file_end = file_start + section['SizeOfRawData']

        if file_start <= offset < file_end:
            offset_in_section = offset - file_start
            return section['VirtualAddress'] + offset_in_section + 0x00400000

    return None


def parse_pe_sections(data):
    """Parse PE sections from binary"""
    # DOS header
    if data[0:2] != b'MZ':
        print("ERROR: Not a valid PE file (missing MZ signature)")
        return []

    # Get PE header offset
    pe_offset = struct.unpack('<I', data[0x3C:0x40])[0]

    # Check PE signature
    if data[pe_offset:pe_offset+4] != b'PE\x00\x00':
        print("ERROR: Not a valid PE file (missing PE signature)")
        return []

    # COFF header
    coff_offset = pe_offset + 4
    num_sections = struct.unpack('<H', data[coff_offset+2:coff_offset+4])[0]
    size_of_optional = struct.unpack('<H', data[coff_offset+16:coff_offset+18])[0]

    # Section table starts after COFF header + optional header
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


def find_vtables_near_string(data, string_offset, sections, search_range=0x500):
    """Find vtables by searching near a type string"""
    candidates = []

    # Search backwards
    for offset in range(4, search_range, 4):
        check_offset = string_offset - offset
        if check_offset < 0:
            continue

        methods = check_vtable_validity(data, check_offset)
        if methods:
            va = file_offset_to_va(check_offset, sections)
            if va:
                candidates.append({
                    'file_offset': check_offset,
                    'va': va,
                    'methods': methods,
                    'distance': offset,
                    'direction': 'before'
                })

    # Search forwards
    for offset in range(4, 0x200, 4):
        check_offset = string_offset + offset
        if check_offset >= len(data):
            break

        methods = check_vtable_validity(data, check_offset)
        if methods:
            va = file_offset_to_va(check_offset, sections)
            if va:
                candidates.append({
                    'file_offset': check_offset,
                    'va': va,
                    'methods': methods,
                    'distance': offset,
                    'direction': 'after'
                })

    return candidates


def find_vtable_for_structure(data, sections, struct_name):
    """Find vtable for a structure"""
    print(f"\n{'='*100}")
    print(f"SEARCHING: {struct_name}")
    print(f"{'='*100}")

    results = {
        'struct_name': struct_name,
        'type_string_found': False,
        'vtable_candidates': []
    }

    # Step 1: Find type string patterns
    patterns = [
        f"{struct_name} *",
        f"{struct_name}*",
        struct_name
    ]

    print(f"  Step 1: Finding type string...")

    for pattern in patterns:
        occurrences = find_string_in_binary(data, pattern)
        if occurrences:
            print(f"  ✓ Found type string '{pattern}' at {len(occurrences)} location(s)")
            results['type_string_found'] = True

            # Search near each occurrence
            for string_offset in occurrences:
                string_va = file_offset_to_va(string_offset, sections)
                print(f"    String @ file offset 0x{string_offset:X} (VA: 0x{string_va:08X})")

                candidates = find_vtables_near_string(data, string_offset, sections)
                results['vtable_candidates'].extend(candidates)

            break

    if not results['type_string_found']:
        print(f"  ⚠️  Type string not found")
        return results

    # Deduplicate candidates by VA
    unique_vtables = {}
    for cand in results['vtable_candidates']:
        va = cand['va']
        if va not in unique_vtables or len(cand['methods']) > len(unique_vtables[va]['methods']):
            unique_vtables[va] = cand

    if unique_vtables:
        print(f"\n  ✅ FOUND {len(unique_vtables)} unique vtable(s):")
        for va, cand in sorted(unique_vtables.items()):
            print(f"     0x{va:08X} - {len(cand['methods'])} methods - {cand['distance']} bytes {cand['direction']} string")
    else:
        print(f"\n  ❌ No vtables found")

    results['unique_vtables'] = unique_vtables
    return results


def save_results(all_results):
    """Save results to markdown file"""
    output_file = "MISSING_VTABLES_FOUND.md"

    with open(output_file, 'w') as f:
        f.write("# Missing TVN Vtables - Search Results\n\n")
        f.write("Automated search for vtables of missing TVN structures.\n\n")
        f.write("**Tool**: Standalone Python vtable finder\n")
        f.write("**Binary**: europeo.exe\n\n")
        f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")
        f.write("| Structure | Vtables Found | Type String |\n")
        f.write("|-----------|---------------|-------------|\n")

        for result in all_results:
            name = result['struct_name']
            num_vtables = len(result.get('unique_vtables', {}))
            string_status = "✓" if result['type_string_found'] else "✗"

            f.write(f"| {name:20s} | {num_vtables:2d} | {string_status} |\n")

        f.write("\n---\n\n")

        # Detailed results
        f.write("## Detailed Results\n\n")

        for result in all_results:
            name = result['struct_name']
            f.write(f"### {name}\n\n")

            if result['type_string_found']:
                f.write(f"**Type String**: ✓ Found\n\n")
            else:
                f.write(f"**Type String**: ⚠️ Not found\n\n")

            unique_vtables = result.get('unique_vtables', {})

            if unique_vtables:
                f.write(f"**Vtables Found**: {len(unique_vtables)}\n\n")

                for va, vtable in sorted(unique_vtables.items()):
                    f.write(f"#### Vtable @ 0x{va:08X}\n\n")
                    f.write(f"- **Virtual Address**: 0x{va:08X}\n")
                    f.write(f"- **File Offset**: 0x{vtable['file_offset']:X}\n")
                    f.write(f"- **Methods**: {len(vtable['methods'])}\n")
                    f.write(f"- **Distance from string**: {vtable['distance']} bytes {vtable['direction']}\n\n")

                    f.write("**Method Pointers**:\n\n")
                    for i, method in enumerate(vtable['methods']):
                        f.write(f"- [{i}] 0x{method:08X}\n")
                    f.write("\n")
            else:
                f.write(f"**Vtables Found**: ❌ None\n\n")

            f.write("---\n\n")

        # Code to add to main script
        f.write("## Code for Main Script\n\n")
        f.write("Add these vtables to `extract_all_35_tvn_complete.py`:\n\n")
        f.write("```python\n")

        for result in all_results:
            name = result['struct_name']
            unique_vtables = result.get('unique_vtables', {})

            if unique_vtables:
                # Take the first (most likely) vtable - prefer one with more methods
                best_va = max(unique_vtables.keys(),
                            key=lambda va: len(unique_vtables[va]['methods']))
                f.write(f'    "{name}": 0x{best_va:08X},\n')
            else:
                f.write(f'    "{name}": None,  # TODO - Not found\n')

        f.write("```\n\n")

    print(f"\n✓ Results saved to {output_file}")


def main():
    if len(sys.argv) < 2:
        print("Usage: find_missing_vtables_standalone.py <europeo.exe>")
        sys.exit(1)

    binary_path = sys.argv[1]

    print("="*100)
    print("FINDING MISSING TVN VTABLES - STANDALONE")
    print("="*100)
    print()
    print(f"Binary: {binary_path}")
    print(f"Structures to search: {len(MISSING_STRUCTURES)}")
    print()

    # Read binary
    with open(binary_path, 'rb') as f:
        data = f.read()

    print(f"Binary loaded: {len(data)} bytes\n")

    # Parse PE sections
    sections = parse_pe_sections(data)
    if not sections:
        print("ERROR: Could not parse PE sections")
        sys.exit(1)

    print(f"PE sections parsed: {len(sections)} sections\n")
    for sec in sections:
        print(f"  {sec['Name']:8s} VA: 0x{sec['VirtualAddress']:08X}  "
              f"Raw: 0x{sec['PointerToRawData']:08X}  Size: 0x{sec['SizeOfRawData']:08X}")

    # Search each structure
    all_results = []

    for struct_name in MISSING_STRUCTURES:
        result = find_vtable_for_structure(data, sections, struct_name)
        all_results.append(result)

    # Save results
    print("\n" + "="*100)
    print("SEARCH COMPLETE")
    print("="*100)

    total_found = sum(len(r.get('unique_vtables', {})) for r in all_results)
    structures_found = sum(1 for r in all_results if r.get('unique_vtables'))

    print(f"\nStructures searched: {len(MISSING_STRUCTURES)}")
    print(f"Structures with vtables found: {structures_found}")
    print(f"Total vtables found: {total_found}")
    print()

    save_results(all_results)

    print("\n✓ Done! Check MISSING_VTABLES_FOUND.md for results.")


if __name__ == "__main__":
    main()
