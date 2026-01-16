#!/usr/bin/env python3
"""
Find which Windows API is at IAT address 0x455FB4
"""

import struct
import sys

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
        virt_end = virt_start + section['SizeOfRawData']
        if virt_start <= va_no_base < virt_end:
            offset_in_section = va_no_base - virt_start
            return section['PointerToRawData'] + offset_in_section
    return None

def read_dword(data, offset):
    """Read DWORD at offset"""
    if offset + 4 <= len(data):
        return struct.unpack('<I', data[offset:offset+4])[0]
    return None

def read_string(data, offset):
    """Read null-terminated string"""
    end = data.find(b'\x00', offset)
    if end == -1:
        return None
    return data[offset:end].decode('ascii', errors='ignore')

def parse_imports(data, sections):
    """Parse import directory"""
    # Find import directory from optional header
    pe_offset = struct.unpack('<I', data[0x3C:0x40])[0]
    import_dir_rva = struct.unpack('<I', data[pe_offset + 24 + 104:pe_offset + 24 + 108])[0]

    if import_dir_rva == 0:
        return []

    import_dir_offset = va_to_file_offset(import_dir_rva + 0x400000, sections)
    if not import_dir_offset:
        return []

    imports = []
    i = 0
    while True:
        # Read IMAGE_IMPORT_DESCRIPTOR
        desc_offset = import_dir_offset + i * 20
        ilt_rva = read_dword(data, desc_offset)  # OriginalFirstThunk
        name_rva = read_dword(data, desc_offset + 12)
        iat_rva = read_dword(data, desc_offset + 16)  # FirstThunk

        if name_rva == 0:
            break

        # Get DLL name
        name_offset = va_to_file_offset(name_rva + 0x400000, sections)
        if name_offset:
            dll_name = read_string(data, name_offset)
        else:
            dll_name = "Unknown"

        # Parse import entries
        if ilt_rva:
            thunk_rva = ilt_rva
        else:
            thunk_rva = iat_rva

        thunk_offset = va_to_file_offset(thunk_rva + 0x400000, sections)
        iat_va = iat_rva + 0x400000

        j = 0
        while thunk_offset:
            entry = read_dword(data, thunk_offset + j * 4)
            if entry == 0:
                break

            # Check if import by name or ordinal
            if entry & 0x80000000:
                # Ordinal
                ordinal = entry & 0xFFFF
                func_name = f"Ordinal {ordinal}"
            else:
                # Name
                hint_name_offset = va_to_file_offset(entry + 0x400000, sections)
                if hint_name_offset:
                    func_name = read_string(data, hint_name_offset + 2)  # Skip hint
                else:
                    func_name = "Unknown"

            imports.append({
                'dll': dll_name,
                'function': func_name,
                'iat_va': iat_va + j * 4
            })

            j += 1

        i += 1

    return imports

def main():
    if len(sys.argv) < 2:
        print("Usage: find_iat_entry.py <europeo.exe>")
        sys.exit(1)

    binary = sys.argv[1]
    target_iat = 0x455FB4

    print(f"Loading {binary}...")
    with open(binary, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    print("Parsing imports...")
    imports = parse_imports(data, sections)

    print(f"\nSearching for IAT entry at 0x{target_iat:08X}...\n")

    # Find the target
    found = None
    for imp in imports:
        if imp['iat_va'] == target_iat:
            found = imp
            break

    if found:
        print("=" * 80)
        print("FOUND!")
        print("=" * 80)
        print(f"DLL: {found['dll']}")
        print(f"Function: {found['function']}")
        print(f"IAT Address: 0x{found['iat_va']:08X}")
        print()

        # Show nearby entries for context
        print("Nearby imports:")
        for imp in imports:
            if abs(imp['iat_va'] - target_iat) <= 32:
                marker = " ← TARGET" if imp['iat_va'] == target_iat else ""
                print(f"  0x{imp['iat_va']:08X}: {imp['dll']:15s} {imp['function']}{marker}")
    else:
        print(f"❌ No import found at 0x{target_iat:08X}")
        print("\nShowing first 50 imports:")
        for imp in imports[:50]:
            print(f"  0x{imp['iat_va']:08X}: {imp['dll']:15s} {imp['function']}")

    # Also list all GDI32 imports
    print("\n" + "=" * 80)
    print("ALL GDI32.DLL IMPORTS")
    print("=" * 80)
    gdi_imports = [imp for imp in imports if 'GDI32' in imp['dll'].upper()]
    for imp in gdi_imports:
        print(f"  0x{imp['iat_va']:08X}: {imp['function']}")

    print(f"\nTotal imports: {len(imports)}")
    print(f"GDI32 imports: {len(gdi_imports)}")

if __name__ == "__main__":
    main()
