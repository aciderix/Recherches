#!/usr/bin/env python3
"""
Analyse complète de tous les types de records
Statistiques sur tous les 19 fichiers VND
"""
import struct
import os
from collections import defaultdict

VND_FOLDER = "Vnd-vnp"

def find_all_separators(data):
    """Trouve TOUS les séparateurs 01 00 00 00"""
    separators = []
    pos = 0
    while pos < len(data) - 12:
        if struct.unpack('<I', data[pos:pos+4])[0] == 1:
            # Vérifie length et type
            length = struct.unpack('<I', data[pos+4:pos+8])[0]
            type_id = struct.unpack('<I', data[pos+8:pos+12])[0]

            # Filtre raisonnable
            if length < 100000 and type_id < 200:
                separators.append({
                    'pos': pos,
                    'length_field': length,
                    'type': type_id
                })
        pos += 1

    return separators

def extract_sample_data(data, pos, max_len=100):
    """Extrait un échantillon de données"""
    data_start = pos + 12
    data_end = min(data_start + max_len, len(data))
    sample = data[data_start:data_end]

    # Convertit en ASCII lisible
    ascii_str = ''
    for b in sample:
        if 32 <= b < 127:
            ascii_str += chr(b)
        else:
            ascii_str += '.'

    return ascii_str[:80]

def analyze_vnd_file(filepath):
    """Analyse un fichier VND"""
    with open(filepath, 'rb') as f:
        data = f.read()

    separators = find_all_separators(data)

    # Groupe par type
    by_type = defaultdict(list)
    for sep in separators:
        t = sep['type']
        by_type[t].append(sep)

    return {
        'filename': os.path.basename(filepath),
        'total_records': len(separators),
        'by_type': dict(by_type),
        'data': data
    }

def main():
    print("="*80)
    print("ANALYSE COMPLÈTE DES TYPES DE RECORDS")
    print("="*80)
    print()

    # Analyse tous les fichiers VND
    all_results = []
    vnd_files = [f for f in os.listdir(VND_FOLDER) if f.endswith('.vnd')]

    print(f"Analyse de {len(vnd_files)} fichiers VND...")
    print()

    for filename in sorted(vnd_files):
        filepath = os.path.join(VND_FOLDER, filename)
        result = analyze_vnd_file(filepath)
        all_results.append(result)

    # Statistiques globales par type
    global_by_type = defaultdict(int)
    type_samples = defaultdict(list)

    for result in all_results:
        for type_id, records in result['by_type'].items():
            global_by_type[type_id] += len(records)

            # Garde un échantillon
            if len(type_samples[type_id]) < 3:
                for rec in records[:1]:
                    sample = extract_sample_data(result['data'], rec['pos'])
                    type_samples[type_id].append({
                        'file': result['filename'],
                        'sample': sample
                    })

    # Affiche statistiques globales
    print("="*80)
    print("STATISTIQUES GLOBALES PAR TYPE")
    print("="*80)
    print()
    print(f"{'Type':>5} | {'Count':>6} | {'%':>6} | Échantillon")
    print("-" * 80)

    total = sum(global_by_type.values())

    for type_id in sorted(global_by_type.keys()):
        count = global_by_type[type_id]
        pct = count * 100.0 / total
        sample = type_samples[type_id][0]['sample'][:40] if type_samples[type_id] else ''

        print(f"{type_id:5d} | {count:6d} | {pct:5.1f}% | {sample}")

    print("-" * 80)
    print(f"{'TOTAL':>5} | {total:6d} | 100.0%")
    print()

    # Top 20 types les plus utilisés
    print("="*80)
    print("TOP 20 TYPES LES PLUS UTILISÉS")
    print("="*80)
    print()

    sorted_types = sorted(global_by_type.items(), key=lambda x: x[1], reverse=True)[:20]

    for i, (type_id, count) in enumerate(sorted_types, 1):
        pct = count * 100.0 / total
        print(f"{i:2d}. Type {type_id:3d} (0x{type_id:02X}): {count:5d} records ({pct:5.1f}%)")

        # Affiche échantillons
        if type_samples[type_id]:
            for j, sample_info in enumerate(type_samples[type_id][:2]):
                print(f"    Sample {j+1} ({sample_info['file']}): {sample_info['sample'][:60]}")
        print()

    # Types rares (1-5 occurrences)
    print("="*80)
    print("TYPES RARES (≤ 5 occurrences)")
    print("="*80)
    print()

    rare_types = [(t, c) for t, c in sorted(global_by_type.items()) if c <= 5]

    if rare_types:
        for type_id, count in rare_types:
            sample_info = type_samples[type_id][0] if type_samples[type_id] else None
            if sample_info:
                print(f"Type {type_id:3d}: {count} occ. - {sample_info['file']}: {sample_info['sample'][:50]}")
    else:
        print("Aucun type rare détecté")

    print()

    # Résumé par fichier
    print("="*80)
    print("RÉSUMÉ PAR FICHIER")
    print("="*80)
    print()

    for result in all_results:
        unique_types = len(result['by_type'])
        print(f"{result['filename']:20} - {result['total_records']:4d} records, {unique_types:2d} types uniques")

if __name__ == '__main__':
    main()
