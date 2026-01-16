#!/usr/bin/env python3
"""
Extract complete vtables for all 18 TVN structures
Using TYPEINFO addresses to find vtables
"""

import struct
import sys

# All 18 structures with TYPEINFO
STRUCTURES = {
    'TVNFileNameParms': 0x0040F3CE,
    'TVNEventCommand': 0x0040F51E,
    'TVNVariable': 0x004067B8,
    'TVNScene': 0x004179AE,
    'TVNToolBar': 0x00435901,
    'TVNWindow': 0x00435921,
    'TVNApplication': 0x00438A7A,
    'TVNAviMedia': 0x00435953,
    'TVNWaveMedia': 0x0041C51D,
    'TVNMidiMedia': 0x0041C590,
    'TVNCDAMedia': 0x00435939,
    'TVNBitmap': 0x0041E5FC,
    'TVNGdiObject': 0x0041E673,
    'TVNHtmlText': 0x004231F0,
    'TVNBmpImg': 0x004358CF,
    'TVNImageObject': 0x0042A40B,
    'TVNTextObject': 0x0042A448,
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
        sections.append({
            'Name': sec_data[0:8].rstrip(b'\x00').decode('ascii', errors='ignore'),
            'VirtualSize': struct.unpack('<I', sec_data[8:12])[0],
            'VirtualAddress': struct.unpack('<I', sec_data[12:16])[0],
            'SizeOfRawData': struct.unpack('<I', sec_data[16:20])[0],
            'PointerToRawData': struct.unpack('<I', sec_data[20:24])[0]
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
            if offset_in_section < section['SizeOfRawData']:
                return section['PointerToRawData'] + offset_in_section
    return None


def read_dword(data, offset):
    """Read a DWORD at offset"""
    if offset + 4 <= len(data):
        return struct.unpack('<I', data[offset:offset+4])[0]
    return None


def is_valid_code_pointer(addr):
    """Check if address looks like code (in reasonable range)"""
    return 0x00400000 <= addr <= 0x00500000


def scan_for_vtables_near_typeinfo(data, sections, typeinfo_va, struct_name, scan_range=0x2000):
    """Scan for vtables near TYPEINFO address"""
    vtables_found = []

    # Search before and after TYPEINFO
    start_va = typeinfo_va - scan_range
    end_va = typeinfo_va + scan_range

    # Align to dword
    start_va = (start_va // 4) * 4

    current_va = start_va
    while current_va < end_va:
        offset = va_to_file_offset(current_va, sections)
        if offset is None:
            current_va += 4
            continue

        # Read potential vtable
        potential_vtable = []
        test_offset = offset

        # Try to read a sequence of valid code pointers
        for i in range(50):  # Max 50 methods
            ptr = read_dword(data, test_offset + i * 4)
            if ptr is None:
                break

            if is_valid_code_pointer(ptr):
                potential_vtable.append(ptr)
            else:
                break  # Stop at first non-code pointer

        # If we found at least 3 methods, it's probably a vtable
        if len(potential_vtable) >= 3:
            vtables_found.append({
                'va': current_va,
                'offset': offset,
                'methods': potential_vtable,
                'distance_from_typeinfo': current_va - typeinfo_va
            })

            # Skip past this vtable
            current_va += len(potential_vtable) * 4
        else:
            current_va += 4

    return vtables_found


def main():
    if len(sys.argv) < 2:
        print("Usage: extract_complete_vtables.py <europeo.exe>")
        sys.exit(1)

    binary = sys.argv[1]

    print("="*80)
    print("COMPLETE VTABLE EXTRACTION FOR 18 TVN STRUCTURES")
    print("="*80)
    print()

    # Load binary
    with open(binary, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    # Extract vtables for each structure
    all_results = []

    for struct_name, typeinfo_va in sorted(STRUCTURES.items()):
        print(f"\n{'='*80}")
        print(f"{struct_name} @ 0x{typeinfo_va:08X}")
        print(f"{'='*80}")

        # Scan for vtables
        vtables = scan_for_vtables_near_typeinfo(data, sections, typeinfo_va, struct_name)

        if vtables:
            print(f"  ✓ Found {len(vtables)} vtable(s):")
            for i, vt in enumerate(vtables):
                print(f"\n  Vtable #{i+1} @ 0x{vt['va']:08X}")
                print(f"  Distance from TYPEINFO: {vt['distance_from_typeinfo']:+d} bytes")
                print(f"  Methods: {len(vt['methods'])}")
                print(f"  Method pointers:")
                for j, method in enumerate(vt['methods'][:20]):  # First 20
                    print(f"    [{j:2d}] 0x{method:08X}")
                if len(vt['methods']) > 20:
                    print(f"    ... and {len(vt['methods']) - 20} more methods")

                all_results.append({
                    'struct': struct_name,
                    'typeinfo': typeinfo_va,
                    'vtable_va': vt['va'],
                    'method_count': len(vt['methods']),
                    'methods': vt['methods'],
                    'distance': vt['distance_from_typeinfo']
                })
        else:
            print(f"  ✗ No vtables found")

    # Generate summary report
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}\n")

    with open("COMPLETE_VTABLES.md", 'w') as f:
        f.write("# Complete Vtable Extraction for 18 TVN Structures\n\n")
        f.write(f"**Total structures**: {len(STRUCTURES)}\n")
        f.write(f"**Vtables found**: {len(all_results)}\n\n")
        f.write("---\n\n")

        # Summary table
        f.write("## Summary Table\n\n")
        f.write("| Structure | TYPEINFO | Vtable Address | Methods | Distance |\n")
        f.write("|-----------|----------|----------------|---------|----------|\n")

        for struct_name in sorted(STRUCTURES.keys()):
            typeinfo = STRUCTURES[struct_name]
            struct_vtables = [r for r in all_results if r['struct'] == struct_name]

            if struct_vtables:
                for vt in struct_vtables:
                    f.write(f"| {struct_name} | 0x{typeinfo:08X} | 0x{vt['vtable_va']:08X} | {vt['method_count']} | {vt['distance']:+d} |\n")
            else:
                f.write(f"| {struct_name} | 0x{typeinfo:08X} | ❌ Not found | - | - |\n")

        f.write("\n---\n\n")

        # Detailed results
        f.write("## Detailed Vtable Information\n\n")

        for result in all_results:
            f.write(f"### {result['struct']}\n\n")
            f.write(f"**TYPEINFO**: 0x{result['typeinfo']:08X}\n")
            f.write(f"**Vtable Address**: 0x{result['vtable_va']:08X}\n")
            f.write(f"**Method Count**: {result['method_count']}\n")
            f.write(f"**Distance from TYPEINFO**: {result['distance']:+d} bytes\n\n")

            f.write("**Method Table**:\n\n")
            f.write("| Index | Address | Notes |\n")
            f.write("|-------|---------|-------|\n")

            for i, method in enumerate(result['methods']):
                f.write(f"| {i:2d} | 0x{method:08X} |  |\n")

            f.write("\n---\n\n")

    print(f"Structure               TYPEINFO    Vtables  Methods")
    print("-" * 80)

    for struct_name in sorted(STRUCTURES.keys()):
        typeinfo = STRUCTURES[struct_name]
        struct_vtables = [r for r in all_results if r['struct'] == struct_name]

        if struct_vtables:
            total_methods = sum(v['method_count'] for v in struct_vtables)
            print(f"{struct_name:<23} 0x{typeinfo:08X}  {len(struct_vtables):2d}      {total_methods:3d}")
        else:
            print(f"{struct_name:<23} 0x{typeinfo:08X}  ✗       -")

    print(f"\n✓ Report saved to COMPLETE_VTABLES.md")
    print()


if __name__ == "__main__":
    main()
