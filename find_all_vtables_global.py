#!/usr/bin/env python3
"""
Global vtable scanner - finds ALL potential vtables in the entire binary
Then tries to match them to missing structures
"""

import struct
import sys


def read_dword(data, offset):
    """Read DWORD at offset"""
    if offset < 0 or offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def is_valid_code_pointer(addr):
    """Check if address is valid code"""
    return 0x00401000 <= addr <= 0x00500000


def check_vtable_at_offset(data, file_offset):
    """Check if a file offset looks like a valid vtable"""
    methods = []

    for offset in range(0, 0x100, 4):  # Check up to 64 methods
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


def parse_pe_sections(data):
    """Parse PE sections from binary"""
    # DOS header
    if data[0:2] != b'MZ':
        print("ERROR: Not a valid PE file")
        return []

    # Get PE header offset
    pe_offset = struct.unpack('<I', data[0x3C:0x40])[0]

    # Check PE signature
    if data[pe_offset:pe_offset+4] != b'PE\x00\x00':
        print("ERROR: Not a valid PE file")
        return []

    # COFF header
    coff_offset = pe_offset + 4
    num_sections = struct.unpack('<H', data[coff_offset+2:coff_offset+4])[0]
    size_of_optional = struct.unpack('<H', data[coff_offset+16:coff_offset+18])[0]

    # Section table
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


def file_offset_to_va(offset, sections):
    """Convert file offset to virtual address"""
    for section in sections:
        file_start = section['PointerToRawData']
        file_end = file_start + section['SizeOfRawData']

        if file_start <= offset < file_end:
            offset_in_section = offset - file_start
            return section['VirtualAddress'] + offset_in_section + 0x00400000

    return None


def scan_all_vtables(data, sections):
    """Scan entire DATA section for all vtables"""
    print("Scanning entire DATA section for vtables...")
    print("This may take a few minutes...\n")

    all_vtables = []

    # Only scan DATA section (vtables are in data, not code)
    for section in sections:
        if section['Name'] not in ['DATA', '.data', '.rdata']:
            continue

        print(f"Scanning section: {section['Name']}")
        print(f"  Range: 0x{section['PointerToRawData']:X} - 0x{section['PointerToRawData'] + section['SizeOfRawData']:X}")

        start_offset = section['PointerToRawData']
        end_offset = start_offset + section['SizeOfRawData']

        # Scan every 4-byte aligned address
        for offset in range(start_offset, end_offset, 4):
            methods = check_vtable_at_offset(data, offset)

            if methods:
                va = file_offset_to_va(offset, sections)
                if va:
                    all_vtables.append({
                        'file_offset': offset,
                        'va': va,
                        'methods': methods,
                        'section': section['Name']
                    })

                    if len(all_vtables) % 10 == 0:
                        print(f"  Found {len(all_vtables)} vtables so far...")

    print(f"\n✓ Scan complete! Found {len(all_vtables)} potential vtables\n")
    return all_vtables


def find_string_in_binary(data, search_str):
    """Find all occurrences of a string"""
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


def associate_vtables_with_structures(data, sections, all_vtables):
    """Try to associate vtables with structures based on TYPEINFO/string proximity"""

    STRUCTURES = {
        "TVNFileNameParms": {"typeinfo": 0x0040F3CE, "string": 0x0040F3DA},
        "TVNEventCommand": {"typeinfo": 0x0040F51E, "string": 0x0040F52A},
        "TVNVariable": {"typeinfo": 0x004067B8, "string": 0x00406804},
        "TVNToolBar": {"typeinfo": 0x00435901, "string": 0x0043590D},
        "TVNWindow": {"typeinfo": 0x00435921, "string": 0x0043592D},
        "TVNApplication": {"typeinfo": 0x00438A7A, "string": 0x00438A86},
        "TVNAviMedia": {"typeinfo": 0x00435953, "string": 0x0043595F},
        "TVNWaveMedia": {"typeinfo": 0x0041C51D, "string": 0x0041C529},
        "TVNMidiMedia": {"typeinfo": 0x0041C590, "string": 0x0041C59C},
        "TVNCDAMedia": {"typeinfo": 0x00435939, "string": 0x00435945},
        "TVNBitmap": {"typeinfo": 0x0041E5FC, "string": 0x0041E608},
        "TVNGdiObject": {"typeinfo": 0x0041E673, "string": 0x0041E67F},
        "TVNHtmlText": {"typeinfo": 0x004231F0, "string": 0x004231FC},
        "TVNBmpImg": {"typeinfo": 0x004358CF, "string": 0x004358DB},
    }

    results = {}

    for struct_name, addrs in STRUCTURES.items():
        print(f"\nAnalyzing {struct_name}:")
        print(f"  TYPEINFO: 0x{addrs['typeinfo']:08X}")

        # Find vtables within increasing distance ranges
        candidates = []

        for max_distance in [500, 1000, 2000, 5000, 10000, 50000]:
            for vtable in all_vtables:
                # Calculate distance from TYPEINFO
                distance = abs(vtable['va'] - addrs['typeinfo'])

                if distance <= max_distance:
                    candidates.append({
                        'vtable': vtable,
                        'distance': distance
                    })

            if candidates:
                break

        # Sort by distance
        candidates.sort(key=lambda x: x['distance'])

        if candidates:
            # Show top 5 closest
            print(f"  ✓ Found {len(candidates)} candidate(s) within {max_distance} bytes:")
            for i, cand in enumerate(candidates[:5]):
                vt = cand['vtable']
                dist = cand['distance']
                print(f"    #{i+1}: 0x{vt['va']:08X} - {len(vt['methods'])} methods - {dist} bytes away")

            results[struct_name] = candidates[:5]  # Keep top 5
        else:
            print(f"  ❌ No candidates found (even within 50KB)")
            results[struct_name] = []

    return results


def save_results(all_vtables, associations):
    """Save results to markdown"""
    output_file = "ALL_VTABLES_GLOBAL_SCAN.md"

    with open(output_file, 'w') as f:
        f.write("# Global Vtable Scan Results\n\n")
        f.write("Complete scan of DATA section for all potential vtables.\n\n")
        f.write("**Strategy**: Scan every 4-byte aligned address in DATA section\n")
        f.write("**Validation**: Must have 2+ consecutive valid code pointers\n\n")
        f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")
        f.write(f"**Total vtables found**: {len(all_vtables)}\n\n")

        # Show all vtables
        f.write("## All Vtables Found\n\n")
        f.write("| VA | File Offset | Methods | Section |\n")
        f.write("|----|-------------|---------|----------|\n")

        for vt in all_vtables:
            f.write(f"| 0x{vt['va']:08X} | 0x{vt['file_offset']:X} | {len(vt['methods']):2d} | {vt['section']} |\n")

        f.write("\n---\n\n")

        # Associations
        f.write("## Structure Associations\n\n")

        for struct_name, candidates in associations.items():
            f.write(f"### {struct_name}\n\n")

            if candidates:
                f.write(f"**Top candidates**: {len(candidates)}\n\n")

                for i, cand in enumerate(candidates):
                    vt = cand['vtable']
                    dist = cand['distance']

                    f.write(f"#### Candidate #{i+1}\n\n")
                    f.write(f"- **Vtable VA**: 0x{vt['va']:08X}\n")
                    f.write(f"- **File Offset**: 0x{vt['file_offset']:X}\n")
                    f.write(f"- **Methods**: {len(vt['methods'])}\n")
                    f.write(f"- **Distance from TYPEINFO**: {dist} bytes\n")
                    f.write(f"- **Section**: {vt['section']}\n\n")

                    f.write("**Method Pointers**:\n\n")
                    for j, method in enumerate(vt['methods']):
                        f.write(f"- [{j}] 0x{method:08X}\n")
                    f.write("\n")
            else:
                f.write("**Candidates**: ❌ None found\n\n")

            f.write("---\n\n")

        # Code suggestions
        f.write("## Suggested Vtable Addresses\n\n")
        f.write("Based on closest match to TYPEINFO:\n\n")
        f.write("```python\n")

        for struct_name, candidates in associations.items():
            if candidates:
                best = candidates[0]['vtable']
                f.write(f'    "{struct_name}": 0x{best["va"]:08X},  # {len(best["methods"])} methods, {candidates[0]["distance"]} bytes from TYPEINFO\n')
            else:
                f.write(f'    "{struct_name}": None,  # No candidates found\n')

        f.write("```\n\n")

    print(f"\n✓ Results saved to {output_file}")


def main():
    if len(sys.argv) < 2:
        print("Usage: find_all_vtables_global.py <europeo.exe>")
        sys.exit(1)

    binary_path = sys.argv[1]

    print("="*100)
    print("GLOBAL VTABLE SCANNER")
    print("="*100)
    print()
    print(f"Binary: {binary_path}")
    print("Strategy: Scan entire DATA section for all vtables")
    print()

    # Read binary
    with open(binary_path, 'rb') as f:
        data = f.read()

    print(f"Binary loaded: {len(data)} bytes")

    # Parse PE sections
    sections = parse_pe_sections(data)
    if not sections:
        print("ERROR: Could not parse PE sections")
        sys.exit(1)

    print(f"PE sections: {len(sections)}\n")

    # Scan for all vtables
    all_vtables = scan_all_vtables(data, sections)

    # Associate with structures
    print("\n" + "="*100)
    print("ASSOCIATING VTABLES WITH STRUCTURES")
    print("="*100)

    associations = associate_vtables_with_structures(data, sections, all_vtables)

    # Save results
    print("\n" + "="*100)
    print("SAVING RESULTS")
    print("="*100)

    save_results(all_vtables, associations)

    print("\n✓ Done! Check ALL_VTABLES_GLOBAL_SCAN.md")


if __name__ == "__main__":
    main()
