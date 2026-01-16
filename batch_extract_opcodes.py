#!/usr/bin/env python3
"""
Extraction batch des opcodes de tous les fichiers VND
Compare les patterns entre fichiers
"""
import os
import re
from collections import Counter, defaultdict

def extract_opcodes_from_file(filepath):
    """Extrait les opcodes (nombre+lettre) d'un fichier VND"""
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
    except:
        return []

    # Convertit en string latin-1
    try:
        text = data.decode('latin-1')
    except:
        return []

    # Cherche pattern nombre+lettre
    opcodes = []
    pattern = r'(\d+)([a-z])'

    for match in re.finditer(pattern, text):
        number = match.group(1)
        opcode = match.group(2)
        offset = match.start()

        # Vérifie que ce n'est pas du texte
        next_char_idx = match.end()
        if next_char_idx < len(text):
            next_char = text[next_char_idx]
            if next_char.isalpha():  # Probablement du texte
                continue

        opcode_index = ord(opcode) - ord('a') + 1
        opcodes.append({
            'offset': offset,
            'number': number,
            'opcode': opcode,
            'index': opcode_index,
            'full': f"{number}{opcode}"
        })

    return opcodes

def main():
    print("="*80)
    print("EXTRACTION BATCH OPCODES - 19 FICHIERS VND")
    print("="*80)
    print()

    vnd_dir = "Vnd-vnp"
    vnd_files = sorted([f for f in os.listdir(vnd_dir) if f.endswith('.vnd')])

    all_opcodes = []
    file_stats = []

    # Analyse chaque fichier
    for vnd_file in vnd_files:
        filepath = os.path.join(vnd_dir, vnd_file)
        opcodes = extract_opcodes_from_file(filepath)

        opcode_counts = Counter([op['opcode'] for op in opcodes])

        file_stats.append({
            'file': vnd_file,
            'total': len(opcodes),
            'opcodes': opcode_counts,
            'unique': len(opcode_counts)
        })

        all_opcodes.extend(opcodes)

        # Affiche résumé
        top3 = opcode_counts.most_common(3)
        top3_str = ', '.join([f"'{op}': {cnt}" for op, cnt in top3]) if top3 else 'none'
        print(f"{vnd_file:20s}  {len(opcodes):4d} opcodes  {len(opcode_counts):2d} unique  "
              f"Top: {top3_str}")

    print()
    print("="*80)
    print("ANALYSE GLOBALE")
    print("="*80)
    print()

    # Compte tous les opcodes
    global_opcodes = Counter([op['opcode'] for op in all_opcodes])

    print(f"Total opcodes extraits: {len(all_opcodes)}")
    print(f"Opcodes uniques: {len(global_opcodes)}")
    print()

    print("TOP 20 OPCODES (tous fichiers):")
    print("-" * 80)

    # Noms des opcodes connus
    opcode_names = {
        1: 'Unknown-a',
        2: 'Unknown-b',
        3: 'Unknown-c',
        4: 'DIRECT suffix',
        5: 'Unknown-e',
        6: 'Navigation',
        7: 'Unknown-g',
        8: 'Tooltip',
        9: 'Images/INDEX',
        10: 'Bitmaps',
        11: 'Audio WAV',
        12: 'MIDI Music',
        13: 'Unknown-m',
        14: 'Unknown-n',
        15: 'Unknown-o',
        16: 'Unknown-p',
        17: 'Unknown-q',
        18: 'Unknown-r',
        19: 'Unknown-s',
        20: 'Unknown-t',
        21: 'Logic if/then',
    }

    for opcode, count in global_opcodes.most_common(20):
        index = ord(opcode) - ord('a') + 1
        name = opcode_names.get(index, f'Unknown-{opcode}')
        pct = count * 100.0 / len(all_opcodes)
        print(f"  '{opcode}' (idx {index:2d} - {name:20s}): {count:5d} ({pct:5.1f}%)")

    print()

    # Nouveaux opcodes (pas vus dans couleurs1.vnd)
    couleurs1_opcodes = set([op['opcode'] for op in all_opcodes if 'couleurs1' in
                              [f['file'] for f in file_stats if f['total'] > 0]])

    # Récupère les opcodes de couleurs1
    couleurs1_stats = [f for f in file_stats if f['file'] == 'couleurs1.vnd'][0]
    known_opcodes = set(couleurs1_stats['opcodes'].keys())

    all_found_opcodes = set(global_opcodes.keys())
    new_opcodes = all_found_opcodes - known_opcodes

    if new_opcodes:
        print("NOUVEAUX OPCODES (non vus dans couleurs1.vnd):")
        print("-" * 80)
        for opcode in sorted(new_opcodes):
            index = ord(opcode) - ord('a') + 1
            count = global_opcodes[opcode]
            name = opcode_names.get(index, f'Unknown-{opcode}')
            print(f"  '{opcode}' (idx {index:2d} - {name:20s}): {count:5d} occurrences")
        print()

    # Fichiers avec le plus d'opcodes
    print("TOP 5 FICHIERS (nombre d'opcodes):")
    print("-" * 80)
    for stat in sorted(file_stats, key=lambda x: x['total'], reverse=True)[:5]:
        print(f"  {stat['file']:20s}  {stat['total']:4d} opcodes  {stat['unique']:2d} unique")

    print()

if __name__ == '__main__':
    main()
