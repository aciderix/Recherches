#!/usr/bin/env python3
"""
Vérification des types de records VND
Compare ce qui est réellement dans le fichier avec la spécification fournie
"""

import struct
import sys
from collections import Counter, defaultdict
from pathlib import Path


def read_u32(data, pos):
    """Lire uint32 little-endian"""
    if pos + 4 > len(data):
        return None, pos
    return struct.unpack('<I', data[pos:pos+4])[0], pos + 4


def is_ascii_text(data, min_ratio=0.7):
    """Vérifier si les données sont du texte ASCII"""
    if len(data) == 0:
        return False
    ascii_count = sum(1 for b in data if 32 <= b < 127 or b in [9, 10, 13])
    return ascii_count / len(data) >= min_ratio


def analyze_vnd_records(filepath):
    """Analyser tous les records VND et lister les types trouvés"""

    with open(filepath, 'rb') as f:
        data = f.read()

    print("=" * 80)
    print("VÉRIFICATION DES TYPES DE RECORDS VND")
    print("=" * 80)
    print(f"\nFichier: {filepath}")
    print(f"Taille: {len(data):,} bytes\n")

    # Statistiques
    type_counts = Counter()
    type_examples = defaultdict(list)
    records_found = []

    # Parser tous les records
    pos = 0x115C  # Début des données de scène
    record_num = 0

    print("Recherche des records...\n")

    while pos < len(data) - 12:
        # Chercher le marqueur 01 00 00 00
        marker_pos = data.find(b'\x01\x00\x00\x00', pos)

        if marker_pos == -1 or marker_pos >= len(data) - 12:
            break

        pos = marker_pos

        # Lire la structure du record
        separator, pos = read_u32(data, pos)
        if separator != 1:
            pos = marker_pos + 1
            continue

        length, pos = read_u32(data, pos)
        if length is None or length > 100000 or length == 0:
            pos = marker_pos + 1
            continue

        record_type, pos = read_u32(data, pos)
        if record_type is None:
            pos = marker_pos + 1
            continue

        # Vérifier que le payload est dans les limites
        payload_start = pos
        payload_end = payload_start + length

        if payload_end > len(data):
            pos = marker_pos + 1
            continue

        payload = data[payload_start:payload_end]

        # Vérifier cohérence: le prochain record devrait être après le payload
        next_marker = data.find(b'\x01\x00\x00\x00', payload_end)
        if next_marker != -1 and next_marker < payload_end + 100:
            # Record valide
            record_num += 1
            type_counts[record_type] += 1

            # Garder quelques exemples
            if len(type_examples[record_type]) < 3:
                is_text = is_ascii_text(payload)
                preview = ""

                if is_text:
                    preview = payload.decode('ascii', errors='ignore')[:60]
                else:
                    preview = payload[:32].hex()

                type_examples[record_type].append({
                    'offset': marker_pos,
                    'length': length,
                    'is_text': is_text,
                    'preview': preview,
                    'payload': payload
                })

            records_found.append({
                'num': record_num,
                'offset': marker_pos,
                'type': record_type,
                'length': length,
                'is_text': is_ascii_text(payload)
            })

            pos = payload_end
        else:
            pos = marker_pos + 1

    # Afficher les résultats
    print(f"✓ {record_num} records trouvés\n")
    print("=" * 80)
    print("TYPES DE RECORDS IDENTIFIÉS")
    print("=" * 80)
    print()

    # Trier par nombre d'occurrences
    for record_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"Type {record_type:6d} (0x{record_type:08x}): {count:4d} occurrence(s)")

        # Afficher exemples
        for i, ex in enumerate(type_examples[record_type]):
            content_type = "ASCII" if ex['is_text'] else "binary"
            print(f"  Exemple {i+1} @ 0x{ex['offset']:06x}, len={ex['length']:5d}, {content_type}")

            if ex['is_text']:
                # Afficher le texte
                text = ex['preview'].replace('\n', '\\n').replace('\r', '\\r')
                print(f"    '{text}'")
            else:
                # Afficher hex
                print(f"    {ex['preview']}")
        print()

    # Comparer avec la spécification fournie
    print("=" * 80)
    print("COMPARAISON AVEC LA SPÉCIFICATION")
    print("=" * 80)
    print()

    spec_types = {
        6: "Navigation / scène",
        21: "Script / condition",
        38: "Texte de hotspot (tooltip)",
        39: "Police",
        2: "Hotspot RECTANGLE",
        105: "Hotspot POLYGONE",
        257: "Signature interne",
        1634296933: "Checksum"
    }

    print("Types documentés dans la spec:")
    print()
    for spec_type, description in sorted(spec_types.items()):
        if spec_type in type_counts:
            count = type_counts[spec_type]
            print(f"  ✓ Type {spec_type:6d} (0x{spec_type:08x}): {count:4d} trouvé(s) - {description}")
        else:
            print(f"  ✗ Type {spec_type:6d} (0x{spec_type:08x}):    0 trouvé(s) - {description}")

    print()
    print("Types trouvés NON documentés dans la spec:")
    print()

    undocumented = set(type_counts.keys()) - set(spec_types.keys())
    if undocumented:
        for utype in sorted(undocumented):
            count = type_counts[utype]
            print(f"  ? Type {utype:6d} (0x{utype:08x}): {count:4d} occurrence(s)")
    else:
        print("  (aucun)")

    # Analyser quelques types spécifiques en détail
    print()
    print("=" * 80)
    print("ANALYSE DÉTAILLÉE DE TYPES SPÉCIFIQUES")
    print("=" * 80)

    # Type 2 (Rectangle)
    if 2 in type_examples:
        print("\n🟥 TYPE 2 - Rectangle (devrait être 16 bytes: X1 Y1 X2 Y2)")
        for ex in type_examples[2]:
            if ex['length'] == 16:
                payload = ex['payload']
                x1, y1, x2, y2 = struct.unpack('<IIII', payload)
                print(f"  @ 0x{ex['offset']:06x}: Rectangle ({x1}, {y1}) -> ({x2}, {y2})")
            else:
                print(f"  @ 0x{ex['offset']:06x}: ⚠️ Longueur {ex['length']} != 16")

    # Type 105 (Polygone)
    if 105 in type_examples:
        print("\n🟥 TYPE 105 - Polygone (devrait être: count + points)")
        for ex in type_examples[105]:
            payload = ex['payload']
            if len(payload) >= 4:
                point_count = struct.unpack('<I', payload[0:4])[0]
                expected_length = 4 + (point_count * 8)
                print(f"  @ 0x{ex['offset']:06x}: {point_count} points, longueur={ex['length']}, attendu={expected_length}")

                if ex['length'] == expected_length and point_count <= 20:
                    # Lire les points
                    print(f"    Points:", end="")
                    for i in range(min(3, point_count)):
                        x = struct.unpack('<I', payload[4+i*8:4+i*8+4])[0]
                        y = struct.unpack('<I', payload[4+i*8+4:4+i*8+8])[0]
                        print(f" ({x},{y})", end="")
                    if point_count > 3:
                        print(f" ... (+{point_count-3})")
                    else:
                        print()
                else:
                    print(f"    ⚠️ Longueur ne correspond pas")

    # Type 21 (Script)
    if 21 in type_examples:
        print("\n🟦 TYPE 21 - Script (devrait contenir 'then' ou 'else')")
        for ex in type_examples[21]:
            text = ex['preview']
            has_then = 'then' in text.lower()
            has_else = 'else' in text.lower()
            print(f"  @ 0x{ex['offset']:06x}: then={has_then}, else={has_else}")
            print(f"    '{text}'")

    # Type 38 (Tooltip)
    if 38 in type_examples:
        print("\n🟦 TYPE 38 - Tooltip (devrait être: X Y W H layer texte)")
        for ex in type_examples[38]:
            text = ex['preview']
            print(f"  @ 0x{ex['offset']:06x}: '{text}'")

    # Type 39 (Police)
    if 39 in type_examples:
        print("\n🟦 TYPE 39 - Police (devrait être: SIZE STYLE #RRGGBB FONTNAME)")
        for ex in type_examples[39]:
            text = ex['preview']
            has_color = '#' in text
            print(f"  @ 0x{ex['offset']:06x}: couleur={has_color}")
            print(f"    '{text}'")

    return records_found, type_counts


def main():
    if len(sys.argv) < 2:
        print("Usage: verify_vnd_types.py <fichier.vnd>")
        sys.exit(1)

    filepath = sys.argv[1]
    records, types = analyze_vnd_records(filepath)

    print()
    print("=" * 80)
    print("RÉSUMÉ")
    print("=" * 80)
    print(f"\nTotal records: {len(records)}")
    print(f"Types différents: {len(types)}")


if __name__ == "__main__":
    main()
