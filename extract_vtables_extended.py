#!/usr/bin/env python3
"""
Extended VTable extraction - Search ENTIRE data sections
Previous script only searched ±8KB, but Borland C++ can place vtables much further away
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
            'PointerToRawData': struct.unpack('<I', sec_data[20:24])[0],
            'Characteristics': struct.unpack('<I', sec_data[36:40])[0]
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
    """Check if address looks like code"""
    # Borland C++ Builder typical code range
    return 0x00400000 <= addr <= 0x00500000


def scan_section_for_vtables(data, sections, section_name, typeinfo_addresses):
    """Scan entire section for potential vtables"""
    # Find the target section
    target_section = None
    for sec in sections:
        if sec['Name'] == section_name:
            target_section = sec
            break

    if not target_section:
        print(f"  Section '{section_name}' not found!")
        return []

    print(f"\n  Scanning section: {section_name}")
    print(f"    VA: 0x{target_section['VirtualAddress']:08X}")
    print(f"    Size: {target_section['SizeOfRawData']} bytes ({target_section['SizeOfRawData']//1024} KB)")

    vtables_found = []
    start_offset = target_section['PointerToRawData']
    end_offset = start_offset + target_section['SizeOfRawData']
    base_va = target_section['VirtualAddress'] + 0x400000

    # Scan through section
    current_offset = start_offset
    scanned = 0

    while current_offset < end_offset - 12:  # Need at least 3 pointers
        if scanned % 10000 == 0:
            progress = (current_offset - start_offset) / (end_offset - start_offset) * 100
            print(f"\r    Progress: {progress:.1f}%", end='', flush=True)

        scanned += 1

        # Try to read a vtable at this position
        potential_vtable = []
        test_offset = current_offset

        for i in range(50):  # Max 50 methods
            ptr = read_dword(data, test_offset + i * 4)
            if ptr is None:
                break

            if is_valid_code_pointer(ptr):
                potential_vtable.append(ptr)
            else:
                break

        # If we found at least 3 consecutive code pointers, it's likely a vtable
        if len(potential_vtable) >= 3:
            current_va = base_va + (current_offset - start_offset)

            # Find nearest TYPEINFO
            nearest_typeinfo = None
            min_distance = float('inf')
            for struct_name, typeinfo_va in typeinfo_addresses.items():
                distance = abs(current_va - typeinfo_va)
                if distance < abs(min_distance):
                    min_distance = current_va - typeinfo_va
                    nearest_typeinfo = struct_name

            vtables_found.append({
                'va': current_va,
                'offset': current_offset,
                'methods': potential_vtable,
                'nearest_typeinfo': nearest_typeinfo,
                'distance': min_distance
            })

            # Skip past this vtable
            current_offset += len(potential_vtable) * 4
        else:
            current_offset += 4

    print(f"\r    Progress: 100.0% - Found {len(vtables_found)} potential vtables")

    return vtables_found


def analyze_vtable_quality(vtable):
    """Analyze vtable to determine if it's real"""
    methods = vtable['methods']

    # Check for repeated pointers (common in vtables)
    unique_methods = len(set(methods))
    repetition_ratio = unique_methods / len(methods) if len(methods) > 0 else 0

    # Check for sequential methods (adjacent addresses)
    sequential_count = 0
    for i in range(len(methods) - 1):
        if abs(methods[i+1] - methods[i]) < 1000:  # Within 1KB
            sequential_count += 1

    # Scoring
    score = 0
    confidence = "LOW"

    if len(methods) >= 4:
        score += 1
    if len(methods) <= 20:  # Too many methods is suspicious
        score += 1
    if repetition_ratio >= 0.3:  # Some repetition is normal (destructors)
        score += 1
    if sequential_count >= len(methods) // 3:  # Some sequential methods
        score += 1
    if abs(vtable['distance']) < 0x8000:  # Within 32KB of TYPEINFO
        score += 2

    if score >= 5:
        confidence = "HIGH"
    elif score >= 3:
        confidence = "MEDIUM"

    return {
        'score': score,
        'confidence': confidence,
        'unique_ratio': repetition_ratio,
        'sequential_methods': sequential_count
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: extract_vtables_extended.py <europeo.exe>")
        sys.exit(1)

    binary = sys.argv[1]

    print("="*80)
    print("EXTENDED VTABLE SEARCH - ENTIRE DATA SECTIONS")
    print("="*80)
    print()

    # Load binary
    print("Loading binary...")
    with open(binary, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    print("\nPE Sections:")
    for sec in sections:
        print(f"  {sec['Name']:8s}  VA=0x{sec['VirtualAddress']:08X}  Size={sec['SizeOfRawData']:8d}  Chars=0x{sec['Characteristics']:08X}")

    # Search in DATA and CODE sections
    all_vtables = []

    for section_name in ['DATA', '.data', '.rdata', 'CODE', '.text']:
        vtables = scan_section_for_vtables(data, sections, section_name, STRUCTURES)
        all_vtables.extend(vtables)

    print(f"\n\nTotal vtables found: {len(all_vtables)}")

    # Analyze quality
    print("\n" + "="*80)
    print("QUALITY ANALYSIS")
    print("="*80 + "\n")

    high_quality = []
    medium_quality = []

    for vt in all_vtables:
        quality = analyze_vtable_quality(vt)
        vt['quality'] = quality

        if quality['confidence'] == 'HIGH':
            high_quality.append(vt)
        elif quality['confidence'] == 'MEDIUM':
            medium_quality.append(vt)

    print(f"HIGH confidence: {len(high_quality)}")
    print(f"MEDIUM confidence: {len(medium_quality)}")
    print(f"LOW confidence: {len(all_vtables) - len(high_quality) - len(medium_quality)}")

    # Group by nearest TYPEINFO
    print("\n" + "="*80)
    print("VTABLES GROUPED BY STRUCTURE")
    print("="*80 + "\n")

    for struct_name, typeinfo_va in sorted(STRUCTURES.items()):
        # Find all vtables near this TYPEINFO
        nearby = [vt for vt in all_vtables if vt['nearest_typeinfo'] == struct_name and vt['quality']['confidence'] in ['HIGH', 'MEDIUM']]

        if nearby:
            print(f"\n{struct_name} @ 0x{typeinfo_va:08X}")
            print(f"  Found {len(nearby)} candidate vtable(s):")

            for vt in nearby:
                print(f"\n    Vtable @ 0x{vt['va']:08X}")
                print(f"      Methods: {len(vt['methods'])}")
                print(f"      Distance: {vt['distance']:+d} bytes")
                print(f"      Confidence: {vt['quality']['confidence']}")
                print(f"      Score: {vt['quality']['score']}/6")
                print(f"      First 10 methods:")
                for i, method in enumerate(vt['methods'][:10]):
                    print(f"        [{i:2d}] 0x{method:08X}")
                if len(vt['methods']) > 10:
                    print(f"        ... and {len(vt['methods']) - 10} more")
        else:
            print(f"\n{struct_name} @ 0x{typeinfo_va:08X}")
            print(f"  ✗ No HIGH/MEDIUM confidence vtables found")

    # Generate report
    print("\n\nGenerating detailed report...")
    with open("EXTENDED_VTABLES.md", 'w') as f:
        f.write("# Extended VTable Search Results\\n\\n")
        f.write(f"**Total vtables found**: {len(all_vtables)}\\n")
        f.write(f"**HIGH confidence**: {len(high_quality)}\\n")
        f.write(f"**MEDIUM confidence**: {len(medium_quality)}\\n\\n")
        f.write("---\\n\\n")

        f.write("## High-Quality Vtables\\n\\n")
        for vt in high_quality:
            f.write(f"### Vtable @ 0x{vt['va']:08X}\\n\\n")
            f.write(f"**Nearest Structure**: {vt['nearest_typeinfo']}\\n")
            f.write(f"**Distance**: {vt['distance']:+d} bytes\\n")
            f.write(f"**Methods**: {len(vt['methods'])}\\n")
            f.write(f"**Confidence**: {vt['quality']['confidence']}\\n\\n")

            f.write("**Method Table**:\\n\\n")
            f.write("| Index | Address |\\n")
            f.write("|-------|---------|\\n")
            for i, method in enumerate(vt['methods']):
                f.write(f"| {i:2d} | 0x{method:08X} |\\n")
            f.write("\\n---\\n\\n")

    print(f"✓ Report saved to EXTENDED_VTABLES.md")
    print()


if __name__ == "__main__":
    main()
