#!/usr/bin/env python3
"""
Test batch du parser VND sur tous les fichiers
Extrait statistiques et patterns de chaque fichier
"""
import os
import sys
import struct
from collections import Counter

def find_vnfile_signature(data):
    """Trouve la signature VNFILE"""
    return data.find(b'VNFILE')

def quick_analyze_vnd(filepath):
    """Analyse rapide d'un fichier VND"""
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
    except:
        return None

    size = len(data)
    sig_pos = find_vnfile_signature(data)

    if sig_pos == -1:
        return {'file': filepath, 'size': size, 'valid': False}

    # Cherche records (séparateur 01 00 00 00)
    record_count = 0
    offset = 0x80  # Après header

    while offset < len(data) - 12:
        sep = struct.unpack('<I', data[offset:offset+4])[0]
        if sep == 1:
            length = struct.unpack('<I', data[offset+4:offset+8])[0]
            type_id = struct.unpack('<I', data[offset+8:offset+12])[0]

            if length < 100000 and type_id < 200:
                record_count += 1
                # Pour Type 0, cherche prochain séparateur
                if type_id == 0:
                    # Saute empiriquement
                    offset += 12 + 200
                else:
                    offset += 12 + length
            else:
                break
        else:
            offset += 4

        if record_count > 100:  # Limite sécurité
            break

    return {
        'file': os.path.basename(filepath),
        'size': size,
        'valid': True,
        'sig_pos': sig_pos,
        'record_count': record_count
    }

def main():
    print("="*80)
    print("TEST BATCH PARSER VND - 19 FICHIERS")
    print("="*80)
    print()

    vnd_dir = "Vnd-vnp"

    # Liste tous les fichiers VND
    vnd_files = sorted([f for f in os.listdir(vnd_dir) if f.endswith('.vnd')])

    print(f"✓ Trouvé {len(vnd_files)} fichiers VND\n")

    results = []

    for vnd_file in vnd_files:
        filepath = os.path.join(vnd_dir, vnd_file)
        result = quick_analyze_vnd(filepath)

        if result:
            results.append(result)

            status = "✓" if result['valid'] else "✗"
            size_kb = result['size'] / 1024

            if result['valid']:
                print(f"{status} {result['file']:20s}  {size_kb:6.1f} KB  "
                      f"Sig @ 0x{result['sig_pos']:04X}  "
                      f"Records: {result['record_count']:3d}")
            else:
                print(f"{status} {result['file']:20s}  {size_kb:6.1f} KB  INVALID")

    print()
    print("="*80)
    print("STATISTIQUES")
    print("="*80)
    print()

    valid_files = [r for r in results if r['valid']]
    print(f"Fichiers valides: {len(valid_files)}/{len(results)}")

    if valid_files:
        sizes = [r['size'] for r in valid_files]
        records = [r['record_count'] for r in valid_files]

        print(f"Taille moyenne: {sum(sizes)/len(sizes)/1024:.1f} KB")
        print(f"Taille min/max: {min(sizes)/1024:.1f} KB / {max(sizes)/1024:.1f} KB")
        print(f"Records moyen: {sum(records)/len(records):.1f}")
        print(f"Records min/max: {min(records)} / {max(records)}")

    print()

    # Tri par taille
    print("TOP 5 PLUS GROS:")
    print("-" * 80)
    for r in sorted(valid_files, key=lambda x: x['size'], reverse=True)[:5]:
        print(f"  {r['file']:20s}  {r['size']/1024:6.1f} KB  {r['record_count']:3d} records")

    print()
    print("TOP 5 PLUS PETITS:")
    print("-" * 80)
    for r in sorted(valid_files, key=lambda x: x['size'])[:5]:
        print(f"  {r['file']:20s}  {r['size']/1024:6.1f} KB  {r['record_count']:3d} records")

if __name__ == '__main__':
    main()
