#!/usr/bin/env python3
"""
Correlate TYPEINFO addresses with LoadFromINI functions
Try to identify which LoadFromINI function belongs to which TVN structure
"""

import struct
import re

# Known TYPEINFO addresses from VTABLES_FROM_TYPEINFO.md
TYPEINFO_ADDRESSES = {
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

# Already identified LoadFromINI functions
KNOWN_LOADFROMINI = {
    'TVNScene': 0x00412324,
    'TVNTextObject': [0x0041F028, 0x0041F790, 0x0041F121, 0x0041F179, 0x0041F1CF,
                      0x0041F231, 0x0041F2BA, 0x0041FC53, 0x004200CF],
    'TVNImageObject': [0x00419750, 0x0041A04F],
    'TVNHotspot': 0x00435863,
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


def read_string(data, offset, max_len=64):
    """Read a null-terminated string"""
    if offset < 0 or offset >= len(data):
        return None
    result = []
    for i in range(max_len):
        if offset + i >= len(data):
            break
        byte = data[offset + i]
        if byte == 0:
            break
        if 32 <= byte <= 126:
            result.append(chr(byte))
        else:
            break
    return ''.join(result) if len(result) >= 3 else None


def read_rtti_borland(data, sections, typeinfo_va):
    """Read Borland RTTI structure"""
    offset = va_to_file_offset(typeinfo_va, sections)
    if offset is None:
        return None

    # Borland RTTI offsets (discovered previously)
    type_id = read_dword(data, offset + 0x00)
    parent_or_flags = read_dword(data, offset + 0x04)
    destructor = read_dword(data, offset + 0x08)
    name = read_string(data, offset + 0x0C)

    return {
        'typeinfo_va': typeinfo_va,
        'type_id': type_id,
        'parent': parent_or_flags,
        'destructor': destructor,
        'name': name
    }


def scan_for_vtable_refs_in_function(data, sections, func_va, typeinfo_va):
    """
    Scan a function to see if it references vtables near the TYPEINFO
    This would indicate the function belongs to that structure
    """
    offset = va_to_file_offset(func_va, sections)
    if offset is None:
        return False

    # Read up to 2000 bytes of function
    func_bytes = data[offset:offset + 0x800]

    # Look for references to addresses near TYPEINFO (vtables are usually nearby)
    typeinfo_zone_start = typeinfo_va - 0x1000
    typeinfo_zone_end = typeinfo_va + 0x1000

    # Scan for DWORD values in the function that point to this zone
    for i in range(0, len(func_bytes) - 4, 1):
        dword = struct.unpack('<I', func_bytes[i:i+4])[0]
        if typeinfo_zone_start <= dword <= typeinfo_zone_end:
            return True

    return False


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: correlate_typeinfo_loadfromini.py <europeo.exe>")
        sys.exit(1)

    binary_path = sys.argv[1]

    print("="*80)
    print("CORRELATE TYPEINFO WITH LOADFROMINI FUNCTIONS")
    print("="*80)
    print()

    # Load binary
    with open(binary_path, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    # Parse all TYPEINFO addresses
    print("Reading RTTI structures...\n")

    rtti_data = {}
    for struct_name, typeinfo_va in sorted(TYPEINFO_ADDRESSES.items()):
        rtti = read_rtti_borland(data, sections, typeinfo_va)
        if rtti:
            rtti_data[struct_name] = rtti
            print(f"{struct_name:20s} @ 0x{typeinfo_va:08X}")
            print(f"  Name: {rtti['name']}")
            print(f"  Destructor: 0x{rtti['destructor']:08X}")
            print()

    # Now try to correlate with known LoadFromINI
    print("="*80)
    print("CORRELATION WITH KNOWN LOADFROMINI")
    print("="*80)
    print()

    for struct_name, loadfromini in KNOWN_LOADFROMINI.items():
        if struct_name in rtti_data:
            rtti = rtti_data[struct_name]
            if isinstance(loadfromini, list):
                print(f"{struct_name}:")
                print(f"  TYPEINFO: 0x{rtti['typeinfo_va']:08X}")
                print(f"  Destructor: 0x{rtti['destructor']:08X}")
                print(f"  LoadFromINI functions: {len(loadfromini)}")
                for addr in loadfromini:
                    print(f"    - 0x{addr:08X}")
            else:
                print(f"{struct_name}:")
                print(f"  TYPEINFO: 0x{rtti['typeinfo_va']:08X}")
                print(f"  Destructor: 0x{rtti['destructor']:08X}")
                print(f"  LoadFromINI: 0x{loadfromini:08X}")
            print()

    # Try to find LoadFromINI for unknown structures
    print("="*80)
    print("SEARCHING FOR LOADFROMINI OF OTHER STRUCTURES")
    print("="*80)
    print()

    # Parse LOADFROMINI_CANDIDATES.md to get all 180 addresses
    loadfromini_addrs = []
    try:
        with open("LOADFROMINI_CANDIDATES.md", 'r') as f:
            content = f.read()
            pattern = r'## #\d+: Function @ (0x[0-9A-F]+)'
            for match in re.finditer(pattern, content):
                addr = int(match.group(1), 16)
                loadfromini_addrs.append(addr)
    except:
        print("Could not read LOADFROMINI_CANDIDATES.md")
        return

    print(f"Loaded {len(loadfromini_addrs)} LoadFromINI candidate addresses\n")

    # For each unknown structure, try to find its LoadFromINI
    for struct_name, typeinfo_va in sorted(TYPEINFO_ADDRESSES.items()):
        if struct_name in KNOWN_LOADFROMINI:
            continue  # Skip already known

        print(f"Searching for {struct_name}...")

        # Scan each LoadFromINI candidate
        matches = []
        for func_va in loadfromini_addrs:
            if scan_for_vtable_refs_in_function(data, sections, func_va, typeinfo_va):
                matches.append(func_va)

        if matches:
            print(f"  ✓ Found {len(matches)} potential LoadFromINI:")
            for addr in matches[:5]:  # Top 5
                print(f"    - 0x{addr:08X}")
        else:
            print(f"  ✗ No matches found")
        print()


if __name__ == "__main__":
    main()
