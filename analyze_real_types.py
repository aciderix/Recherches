#!/usr/bin/env python3
"""
Analyse des types réels dans couleurs1.vnd
Sans présupposés sur la structure
"""

import struct
import sys
import re
from collections import defaultdict


def read_u32(data, pos):
    if pos + 4 > len(data):
        return None, pos
    return struct.unpack('<I', data[pos:pos+4])[0], pos + 4


def is_ascii(data, ratio=0.7):
    if len(data) == 0:
        return False
    ascii_count = sum(1 for b in data if 32 <= b < 127 or b in [9, 10, 13, 0])
    return ascii_count / len(data) >= ratio


def analyze_type_patterns(filepath):
    """Analyser les patterns réels des types"""

    with open(filepath, 'rb') as f:
        data = f.read()

    # Grouper par type
    type_data = defaultdict(list)

    pos = 0x115C
    while pos < len(data) - 12:
        marker_pos = data.find(b'\x01\x00\x00\x00', pos)
        if marker_pos == -1 or marker_pos >= len(data) - 12:
            break

        pos = marker_pos
        separator, pos = read_u32(data, pos)
        if separator != 1:
            pos = marker_pos + 1
            continue

        length, pos = read_u32(data, pos)
        if length is None or length > 100000 or length == 0:
            pos = marker_pos + 1
            continue

        rtype, pos = read_u32(data, pos)
        if rtype is None:
            pos = marker_pos + 1
            continue

        payload_end = pos + length
        if payload_end > len(data):
            pos = marker_pos + 1
            continue

        payload = data[pos:payload_end]

        # Vérifier cohérence
        next_marker = data.find(b'\x01\x00\x00\x00', payload_end)
        if next_marker != -1 and next_marker < payload_end + 100:
            type_data[rtype].append({
                'offset': marker_pos,
                'length': length,
                'payload': payload
            })
            pos = payload_end
        else:
            pos = marker_pos + 1

    # Analyser chaque type
    print("=" * 80)
    print("ANALYSE DES TYPES RÉELS - couleurs1.vnd")
    print("=" * 80)
    print()

    # Trier par nombre d'occurrences
    sorted_types = sorted(type_data.items(), key=lambda x: len(x[1]), reverse=True)

    for rtype, records in sorted_types[:20]:  # Top 20
        count = len(records)
        print(f"\n{'='*80}")
        print(f"TYPE {rtype:6d} (0x{rtype:08x}) - {count} occurrence(s)")
        print(f"{'='*80}")

        # Analyser le contenu
        lengths = [r['length'] for r in records]
        min_len = min(lengths)
        max_len = max(lengths)
        avg_len = sum(lengths) // len(lengths)

        print(f"Longueurs: min={min_len}, max={max_len}, moy={avg_len}")

        # Vérifier si c'est du texte ASCII
        ascii_count = sum(1 for r in records if is_ascii(r['payload']))
        is_text_type = ascii_count / count > 0.8

        print(f"Type: {'TEXTE ASCII' if is_text_type else 'BINAIRE'}")

        # Montrer exemples
        print("\nExemples:")
        for i, rec in enumerate(records[:3]):
            payload = rec['payload']
            print(f"\n  Exemple {i+1} @ 0x{rec['offset']:06x} (len={rec['length']})")

            if is_ascii(payload):
                text = payload.decode('ascii', errors='ignore').strip('\x00')
                print(f"    ASCII: '{text}'")

                # Détecter patterns
                if 'then' in text:
                    print(f"    → Pattern: CONDITION (contient 'then')")
                if '=' in text and 'then' in text:
                    print(f"    → Pattern: SCRIPT (var = val then action)")
                if any(cmd in text for cmd in ['playavi', 'playwav', 'addbmp', 'runprj']):
                    print(f"    → Pattern: COMMANDE MÉDIA")
                if re.search(r'#[0-9A-Fa-f]{6}', text):
                    print(f"    → Pattern: COULEUR")
                if re.search(r'\d+\s+\d+\s+\d+\s+\d+', text):
                    print(f"    → Pattern: COORDONNÉES")
            else:
                # Analyse binaire
                print(f"    HEX: {payload[:32].hex()}")

                if rec['length'] == 16:
                    # Peut-être un rectangle
                    try:
                        x1, y1, x2, y2 = struct.unpack('<IIII', payload)
                        if all(0 <= v < 10000 for v in [x1, y1, x2, y2]):
                            print(f"    → Pattern: Peut-être RECTANGLE ({x1},{y1})-({x2},{y2})")
                    except:
                        pass

                if rec['length'] >= 4:
                    # Peut-être un count suivi de données
                    try:
                        first_u32 = struct.unpack('<I', payload[:4])[0]
                        if 2 <= first_u32 <= 100:
                            expected_len = 4 + (first_u32 * 8)
                            if rec['length'] == expected_len:
                                print(f"    → Pattern: Peut-être POLYGONE ({first_u32} points)")
                    except:
                        pass

                # Statistiques
                if rec['length'] > 100:
                    unique_vals = len(set(payload))
                    print(f"    → {unique_vals} valeurs uniques sur {rec['length']} bytes")

    # Résumé des patterns trouvés
    print("\n" + "=" * 80)
    print("PATTERNS IDENTIFIÉS")
    print("=" * 80)
    print()

    # Scripts conditionnels (avec "then")
    script_types = []
    for rtype, records in type_data.items():
        if any('then' in r['payload'].decode('ascii', errors='ignore') for r in records[:3]):
            script_types.append((rtype, len(records)))

    if script_types:
        print("Types contenant des SCRIPTS (avec 'then'):")
        for rtype, count in sorted(script_types, key=lambda x: x[1], reverse=True)[:10]:
            print(f"  Type {rtype:3d} (0x{rtype:02x}): {count:3d} occurrences")

    print()

    # Gros blocs binaires
    large_types = [(rtype, len(records)) for rtype, records in type_data.items()
                   if records and records[0]['length'] > 1000]

    if large_types:
        print("Types avec GROS BLOCS (>1000 bytes):")
        for rtype, count in sorted(large_types):
            example = type_data[rtype][0]
            print(f"  Type {rtype:6d} (0x{rtype:04x}): {count} occurrence(s), taille={example['length']} bytes")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: analyze_real_types.py <fichier.vnd>")
        sys.exit(1)

    analyze_type_patterns(sys.argv[1])
