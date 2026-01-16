#!/usr/bin/env python3
"""
Analyse du répartiteur de commandes VND (sub_43177D)
Recherche la fonction dans europeo.exe et extrait son code
"""

import struct
import sys

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

def disassemble_bytes(data, offset, size):
    """Simple hexdump of bytes"""
    result = []
    for i in range(0, size, 16):
        chunk = data[offset+i:offset+i+16]
        hex_str = ' '.join(f'{b:02x}' for b in chunk)
        result.append(f"{offset+i:08x}: {hex_str}")
    return '\n'.join(result)

def main():
    binary = "DOCS/europeo.exe"

    # Adresses critiques selon la doc VND
    targets = {
        'sub_43177D (Dispatcher)': 0x0043177D,
        'sub_407FE5 (atol parser)': 0x00407FE5,
        'sub_4268F8 (scene nav)': 0x004268F8,
        'sub_42703A (images)': 0x0042703A,
        'sub_4275F6 (bitmaps)': 0x004275F6,
        'sub_427B56 (audio)': 0x00427B56,
        'sub_431721 (logic)': 0x00431721,
        'sub_41721D (load VND)': 0x0041721D,
        'sub_410AF6 (validate)': 0x00410AF6,
    }

    print("="*80)
    print("ANALYSE DU RÉPARTITEUR VND ET FONCTIONS CRITIQUES")
    print("="*80)
    print()

    # Load binary
    with open(binary, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    print("PE Sections:")
    for sec in sections:
        print(f"  {sec['Name']:8s}  VA=0x{sec['VirtualAddress']:08X}  Size={sec['SizeOfRawData']:8d}")
    print()

    # Check each target
    for name, va in targets.items():
        print("="*80)
        print(f"{name} @ 0x{va:08X}")
        print("="*80)

        offset = va_to_file_offset(va, sections)
        if offset is None:
            print(f"✗ Adresse invalide (hors sections)\n")
            continue

        print(f"File offset: 0x{offset:08X}\n")

        # Read first 256 bytes
        func_data = data[offset:offset+256]

        # Check for function prologue
        if func_data[0:2] == b'\x55\x8b' or func_data[0:1] == b'\x55':  # push ebp; mov ebp,esp
            print("✓ Function prologue detected (push ebp)")
        elif func_data[0:3] == b'\x8b\xff\x55':  # mov edi,edi; push ebp (hotpatch)
            print("✓ Function prologue detected (hotpatch)")
        else:
            print(f"⚠ No standard prologue (first bytes: {func_data[0:8].hex()})")

        print("\nFirst 128 bytes (hex):")
        print(disassemble_bytes(func_data, offset, 128))
        print()

    # Special check: Variable table
    print("="*80)
    print(f"dword_44ECCE (Variable Table) @ 0x0044ECCE")
    print("="*80)

    var_table_va = 0x0044ECCE
    var_table_offset = va_to_file_offset(var_table_va, sections)

    if var_table_offset:
        print(f"File offset: 0x{var_table_offset:08X}\n")
        print("First 256 bytes (should contain variable names):")

        var_data = data[var_table_offset:var_table_offset+256]

        # Try to find variable names
        print("\nPossible variable names (ASCII strings):")
        current_str = b""
        for i, b in enumerate(var_data[:256]):
            if 0x20 <= b <= 0x7E:  # Printable ASCII
                current_str += bytes([b])
            else:
                if len(current_str) >= 4:
                    try:
                        print(f"  Offset +{i-len(current_str):04x}: \"{current_str.decode('ascii')}\"")
                    except:
                        pass
                current_str = b""

        print("\nHexdump:")
        print(disassemble_bytes(var_data, var_table_offset, 256))
    else:
        print("✗ Adresse invalide\n")

if __name__ == "__main__":
    main()
