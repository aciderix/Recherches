#!/usr/bin/env python3
"""
Dump de la table de variables @ 0x44ECCE
Adresse utilisée par handlers p, q, r (16-18)
"""
import struct

EXE_FILE = "DOCS/europeo.exe"
VAR_TABLE_VA = 0x0044ECCE
BASE_ADDR = 0x00400000

def va_to_file_offset(va, sections):
    """Convert VA to file offset"""
    va_no_base = va - BASE_ADDR if va >= BASE_ADDR else va
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

def dump_variable_table(data, offset, size=2000):
    """Dump et analyse la table de variables"""
    print(f"\n{'='*80}")
    print(f"DUMP TABLE VARIABLES @ 0x{VAR_TABLE_VA:08X}")
    print(f"{'='*80}")
    print(f"File offset: 0x{offset:08X}")
    print()

    # Lit les données
    var_data = data[offset:offset+size]

    # Affiche hex dump
    print("HEX DUMP (premiers 256 bytes):")
    print("-" * 80)
    for i in range(0, min(256, len(var_data)), 16):
        # Offset
        hex_str = f"{offset + i:08x}:  "

        # Hex bytes
        hex_bytes = ' '.join(f'{b:02x}' for b in var_data[i:i+16])
        hex_str += f"{hex_bytes:48}  "

        # ASCII
        ascii_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in var_data[i:i+16])
        hex_str += ascii_str

        print(hex_str)

    # Cherche des strings
    print(f"\n{'='*80}")
    print("ANALYSE DES STRINGS")
    print(f"{'='*80}")

    strings = []
    current = []
    current_offset = 0

    for i, b in enumerate(var_data[:800]):
        if 32 <= b < 127:
            if not current:
                current_offset = offset + i
            current.append(chr(b))
        else:
            if len(current) >= 3:
                strings.append({
                    'offset': current_offset,
                    'text': ''.join(current)
                })
            current = []

    print(f"\nTrouvé {len(strings)} strings (>= 3 chars):")
    print("-" * 80)

    for s in strings[:50]:
        print(f"  @ 0x{s['offset']:08X}: \"{s['text']}\"")

    # Cherche des patterns de variables (comme dans les VND files)
    print(f"\n{'='*80}")
    print("RECHERCHE PATTERNS VARIABLES")
    print(f"{'='*80}")
    print("\nPattern VND: [LENGTH:4][NAME:ASCII][00][VALUE:4]")
    print("-" * 80)

    variables = []
    pos = 0
    while pos < len(var_data) - 12:
        # Lit length potentiel
        length = struct.unpack('<I', var_data[pos:pos+4])[0]

        # Filtre raisonnable pour nom de variable (3-20 chars)
        if 3 <= length <= 20:
            # Lit le nom
            name_data = var_data[pos+4:pos+4+length]

            # Vérifie que c'est ASCII
            try:
                name = name_data.decode('ascii')
                # Vérifie que c'est alphanumérique
                if name.replace('_', '').replace('-', '').isalnum():
                    # Vérifie null terminator
                    if pos + 4 + length < len(var_data):
                        null_byte = var_data[pos + 4 + length]
                        if null_byte == 0:
                            # Lit la valeur
                            if pos + 4 + length + 5 <= len(var_data):
                                value = struct.unpack('<I', var_data[pos+4+length+1:pos+4+length+5])[0]

                                variables.append({
                                    'offset': offset + pos,
                                    'name': name,
                                    'value': value
                                })

                                pos += 4 + length + 1 + 4
                                continue
            except:
                pass

        pos += 1

    if variables:
        print(f"\nTrouvé {len(variables)} variables potentielles:")
        print("-" * 80)
        for v in variables[:30]:
            print(f"  @ 0x{v['offset']:08X}: {v['name']:20} = {v['value']}")
    else:
        print("\n⚠ Aucune variable au format VND trouvée")
        print("La table peut avoir un format différent (C struct, array, etc.)")

def main():
    print("="*80)
    print("DUMP TABLE VARIABLES")
    print("="*80)
    print()
    print(f"Adresse VA: 0x{VAR_TABLE_VA:08X}")
    print("Référencée par handlers: 'p' (16), 'q' (17), 'r' (18)")
    print()

    # Lit le fichier EXE
    with open(EXE_FILE, 'rb') as f:
        data = f.read()

    # Parse les sections PE
    sections = parse_pe_sections(data)

    print("SECTIONS PE:")
    print("-" * 80)
    for sec in sections:
        va_start = sec['VirtualAddress']
        va_end = va_start + sec['SizeOfRawData']
        print(f"  {sec['Name']:8} VA: 0x{va_start + BASE_ADDR:08X} - 0x{va_end + BASE_ADDR:08X}")
    print()

    # Convertit VA en offset fichier
    offset = va_to_file_offset(VAR_TABLE_VA, sections)
    if not offset:
        print("✗ Impossible de trouver l'adresse")
        return

    # Dump
    dump_variable_table(data, offset)

if __name__ == '__main__':
    main()
