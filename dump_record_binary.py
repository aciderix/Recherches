#!/usr/bin/env python3
"""
Dump hexadécimal + ASCII d'un record spécifique
Pour comprendre la structure binaire exacte
"""
import struct
import sys

def find_all_separators(data):
    """Trouve tous les séparateurs"""
    separators = []
    pos = 0

    while pos < len(data) - 12:
        if struct.unpack('<I', data[pos:pos+4])[0] == 1:
            length = struct.unpack('<I', data[pos+4:pos+8])[0]
            type_id = struct.unpack('<I', data[pos+8:pos+12])[0]

            if length < 100000 and type_id < 200:
                separators.append({
                    'pos': pos,
                    'length_field': length,
                    'type': type_id
                })
        pos += 1

    return separators

def hex_dump(data, offset=0, max_bytes=256):
    """Affiche hex dump formaté"""
    for i in range(0, min(max_bytes, len(data)), 16):
        # Offset
        hex_str = f"{offset + i:08x}:  "

        # Hex bytes
        hex_bytes = ' '.join(f'{b:02x}' for b in data[i:i+16])
        hex_str += f"{hex_bytes:48}  "

        # ASCII
        ascii_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in data[i:i+16])
        hex_str += ascii_str

        print(hex_str)

def dump_record(filename, type_id, index=0):
    """Dump un record spécifique"""
    with open(filename, 'rb') as f:
        data = f.read()

    separators = find_all_separators(data)

    # Filtre par type
    matching = [s for s in separators if s['type'] == type_id]

    if not matching:
        print(f"✗ Aucun record Type {type_id} trouvé")
        return

    if index >= len(matching):
        print(f"✗ Index {index} invalide (seulement {len(matching)} records Type {type_id})")
        return

    sep = matching[index]
    current_idx = separators.index(sep)
    next_pos = separators[current_idx + 1]['pos'] if current_idx + 1 < len(separators) else len(data)

    print("=" * 80)
    print(f"RECORD TYPE {type_id} (index {index}/{len(matching)-1})")
    print("=" * 80)
    print()

    print(f"Position fichier: 0x{sep['pos']:08X}")
    print(f"LENGTH field: {sep['length_field']}")

    # Calcule vraie longueur
    real_length = next_pos - (sep['pos'] + 12)
    print(f"Vraie longueur: {real_length} bytes")

    # Header (12 bytes)
    header_data = data[sep['pos']:sep['pos']+12]
    separator = struct.unpack('<I', header_data[0:4])[0]
    length = struct.unpack('<I', header_data[4:8])[0]
    type_val = struct.unpack('<I', header_data[8:12])[0]

    print(f"\nHEADER:")
    print(f"  Separator: 0x{separator:08X} ({separator})")
    print(f"  Length: {length}")
    print(f"  Type: {type_val}")

    # Données du record
    record_data = data[sep['pos']+12:next_pos]

    print(f"\nDATA ({len(record_data)} bytes):")
    print("-" * 80)

    # Hex dump
    hex_dump(record_data, offset=sep['pos']+12, max_bytes=256)

    # Tente d'interpréter les premiers bytes comme entiers
    print("\n" + "-" * 80)
    print("INTERPRÉTATION (premiers 64 bytes comme entiers 32-bit):")
    print("-" * 80)

    for i in range(0, min(64, len(record_data)), 4):
        if i + 4 <= len(record_data):
            val = struct.unpack('<I', record_data[i:i+4])[0]
            # Aussi essayer comme signed
            val_signed = struct.unpack('<i', record_data[i:i+4])[0]

            print(f"  Offset +{i:3d} (0x{i:02X}): {val:10d} (0x{val:08X}) | signed: {val_signed:10d}")

    # Strings extraites
    print("\n" + "-" * 80)
    print("STRINGS ASCII:")
    print("-" * 80)

    strings = []
    current = []
    current_offset = 0

    for i, byte in enumerate(record_data):
        if 32 <= byte <= 126 or byte in [9, 10, 13]:
            if not current:
                current_offset = i
            current.append(chr(byte))
        else:
            if len(current) >= 3:
                s = ''.join(current).strip()
                if s:
                    strings.append((current_offset, s))
            current = []

    if len(current) >= 3:
        s = ''.join(current).strip()
        if s:
            strings.append((current_offset, s))

    for offset, text in strings[:10]:
        print(f"  @ +{offset:3d}: \"{text}\"")

    if len(strings) > 10:
        print(f"  ... et {len(strings) - 10} autres strings")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 dump_record_binary.py <file.vnd> <type> [index]")
        print("\nExemple: python3 dump_record_binary.py couleurs1.vnd 2 0")
        sys.exit(1)

    filename = sys.argv[1]
    type_id = int(sys.argv[2])
    index = int(sys.argv[3]) if len(sys.argv) > 3 else 0

    dump_record(filename, type_id, index)
