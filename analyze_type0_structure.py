#!/usr/bin/env python3
"""
Analyse approfondie de la structure Type 0 dans biblio.vnd
Parcourt manuellement tous les séparateurs 01 00 00 00
"""
import struct
import sys

def parse_biblio_deep(filename):
    """Parse tous les records de biblio.vnd en détail"""

    with open(filename, 'rb') as f:
        data = f.read()

    print("="*80)
    print(f"ANALYSE APPROFONDIE: {filename}")
    print("="*80)
    print(f"Taille fichier: {len(data):,} bytes ({len(data)/1024:.1f} KB)")
    print()

    # Cherche signature VNFILE
    vnfile_pos = data.find(b'VNFILE')
    if vnfile_pos == -1:
        print("✗ Signature VNFILE non trouvée")
        return

    print(f"✓ Signature VNFILE @ 0x{vnfile_pos:04X}")

    # Cherche tous les séparateurs 01 00 00 00
    separators = []
    pos = 0
    while pos < len(data) - 4:
        if struct.unpack('<I', data[pos:pos+4])[0] == 1:
            # Vérifie que c'est un vrai séparateur (suivi de length/type raisonnables)
            if pos + 12 <= len(data):
                length = struct.unpack('<I', data[pos+4:pos+8])[0]
                type_id = struct.unpack('<I', data[pos+8:pos+12])[0]
                # Filtre: length < 100000 et type < 200
                if length < 100000 and type_id < 200:
                    separators.append({'pos': pos, 'length': length, 'type': type_id})
        pos += 1

    print(f"✓ Trouvé {len(separators)} séparateurs potentiels")
    print()

    # Groupe par type
    by_type = {}
    for sep in separators:
        t = sep['type']
        if t not in by_type:
            by_type[t] = []
        by_type[t].append(sep)

    print("DISTRIBUTION PAR TYPE:")
    print("-" * 80)
    for t in sorted(by_type.keys()):
        count = len(by_type[t])
        print(f"  Type {t:3d} (0x{t:02X}): {count:4d} records")
    print()

    # Analyse des premiers records de chaque type
    print("ÉCHANTILLONS PAR TYPE (3 premiers de chaque):")
    print("=" * 80)

    for t in sorted(by_type.keys())[:10]:  # Top 10 types
        records = by_type[t][:3]  # 3 premiers
        print(f"\n--- Type {t} ({len(by_type[t])} total) ---")

        for i, rec in enumerate(records):
            pos = rec['pos']
            length = rec['length']

            # Lit les données
            data_start = pos + 12
            data_end = min(data_start + length, len(data))
            rec_data = data[data_start:data_end]

            # Affiche
            print(f"\n  Record #{i+1} @ 0x{pos:04X}:")
            print(f"    Length: {length} bytes")

            # Hex preview (32 premiers bytes)
            hex_preview = ' '.join(f'{b:02x}' for b in rec_data[:32])
            print(f"    Data (hex): {hex_preview}")

            # ASCII preview
            ascii_preview = ''.join(chr(b) if 32 <= b < 127 else '.' for b in rec_data[:64])
            if ascii_preview:
                print(f"    Data (ascii): {ascii_preview[:60]}")

    # Cherche Type 0 spécifiquement
    if 0 in by_type:
        print("\n" + "=" * 80)
        print(f"ANALYSE TYPE 0 (SCENES) - {len(by_type[0])} records")
        print("=" * 80)

        for i, rec in enumerate(by_type[0][:5]):  # 5 premiers Type 0
            pos = rec['pos']
            length = rec['length']

            print(f"\nType 0 Record #{i+1} @ 0x{pos:04X}:")
            print(f"  LENGTH field: {length} bytes")

            # Cherche le prochain séparateur pour la vraie longueur
            next_sep_pos = None
            for sep in separators:
                if sep['pos'] > pos:
                    next_sep_pos = sep['pos']
                    break

            if next_sep_pos:
                real_length = next_sep_pos - (pos + 12)
                print(f"  Real length (to next separator): {real_length} bytes")
                print(f"  ⚠ Diff: {abs(real_length - length)} bytes")

            # Preview data
            data_start = pos + 12
            preview_size = min(200, len(data) - data_start)
            preview_data = data[data_start:data_start+preview_size]

            # Cherche strings ASCII
            strings = []
            current_string = []
            for b in preview_data:
                if 32 <= b < 127:
                    current_string.append(chr(b))
                else:
                    if len(current_string) >= 3:
                        strings.append(''.join(current_string))
                    current_string = []

            if strings:
                print(f"  Strings trouvées: {', '.join(strings[:5])}")

if __name__ == '__main__':
    filename = 'Vnd-vnp/biblio.vnd' if len(sys.argv) < 2 else sys.argv[1]
    parse_biblio_deep(filename)
