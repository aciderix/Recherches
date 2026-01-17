#!/usr/bin/env python3
"""
Analyse de la structure hiérarchique d'une scène VND
Montre comment Type 0 organise les éléments (hotspots, images, audio)
"""
import struct
import sys
import re

def find_all_separators(data):
    """Trouve tous les séparateurs de records"""
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

def parse_coordinates(text):
    """Extrait les coordonnées numériques d'un texte"""
    # Pattern pour trouver des suites de nombres (coordonnées)
    coords = []

    # Cherche patterns comme "x y w h" ou suites de nombres
    numbers = re.findall(r'\b\d+\b', text)

    if len(numbers) >= 4:
        # Probablement des coordonnées rectangulaires
        return {
            'type': 'rectangle',
            'values': [int(n) for n in numbers[:4]],
            'all': [int(n) for n in numbers]
        }
    elif len(numbers) >= 2:
        return {
            'type': 'point/other',
            'values': [int(n) for n in numbers]
        }

    return None

def extract_strings(data, min_len=4):
    """Extrait les strings ASCII significatives"""
    strings = []
    current = []
    current_offset = 0

    for i, byte in enumerate(data):
        if 32 <= byte <= 126 or byte in [9, 10, 13]:
            if not current:
                current_offset = i
            current.append(chr(byte))
        else:
            if len(current) >= min_len:
                s = ''.join(current).strip()
                if s and not s.replace('.', '').replace(' ', '') == '':
                    strings.append({
                        'offset': current_offset,
                        'text': s
                    })
            current = []

    # Dernière string
    if len(current) >= min_len:
        s = ''.join(current).strip()
        if s:
            strings.append({
                'offset': current_offset,
                'text': s
            })

    return strings

def analyze_type_0_structure(data, separator_info, next_separator_pos):
    """Analyse détaillée d'un record Type 0"""
    pos = separator_info['pos'] + 12  # Après header
    length = next_separator_pos - pos if next_separator_pos else len(data) - pos

    record_data = data[pos:pos+length]

    # Extrait strings
    strings = extract_strings(record_data, min_len=3)

    # Cherche patterns spécifiques
    patterns = {
        'dll_files': [],
        'wav_files': [],
        'bmp_files': [],
        'avi_files': [],
        'variables': [],
        'coordinates': [],
        'fonts': []
    }

    for s in strings:
        text = s['text']

        # DLL files
        if '.dll' in text.lower():
            patterns['dll_files'].append(text)

        # WAV files
        elif '.wav' in text.lower():
            patterns['wav_files'].append(text)

        # BMP files
        elif '.bmp' in text.lower():
            patterns['bmp_files'].append(text)

        # AVI files
        elif '.avi' in text.lower():
            patterns['avi_files'].append(text)

        # Fonts
        elif 'Comic sans' in text or '#' in text:
            patterns['fonts'].append(text)

        # Variables potentielles (uppercase)
        elif text.isupper() and len(text) >= 3 and text.isalpha():
            patterns['variables'].append(text)

        # Coordonnées
        coords = parse_coordinates(text)
        if coords:
            patterns['coordinates'].append({
                'text': text,
                'coords': coords
            })

    return {
        'length': length,
        'strings': strings,
        'patterns': patterns
    }

def analyze_type_2_hotspot(data, separator_info, next_separator_pos):
    """Analyse d'un hotspot rectangulaire (Type 2)"""
    pos = separator_info['pos'] + 12
    length = next_separator_pos - pos if next_separator_pos else len(data) - pos

    record_data = data[pos:pos+length]

    # Type 2 devrait contenir: coordonnées + texte
    strings = extract_strings(record_data, min_len=2)

    # Cherche les coordonnées au début du record
    coords_data = record_data[:20]  # Premiers 20 bytes
    coords = []

    # Essaie de lire comme suite d'entiers
    for i in range(0, min(16, len(coords_data)), 4):
        if i + 4 <= len(coords_data):
            val = struct.unpack('<I', coords_data[i:i+4])[0]
            if val < 10000:  # Filtre valeurs raisonnables pour coordonnées
                coords.append(val)

    return {
        'length': length,
        'coordinates_raw': coords[:4] if len(coords) >= 4 else coords,
        'strings': strings,
        'text': strings[0]['text'] if strings else None
    }

def analyze_vnd_scene_structure(filename, max_scenes=5):
    """Analyse la structure de scènes d'un fichier VND"""
    print("=" * 80)
    print(f"ANALYSE STRUCTURE SCÈNES VND: {filename}")
    print("=" * 80)
    print()

    with open(filename, 'rb') as f:
        data = f.read()

    # Trouve tous les separators
    separators = find_all_separators(data)

    print(f"Total records: {len(separators)}")
    print()

    # Compte par type
    by_type = {}
    for sep in separators:
        t = sep['type']
        if t not in by_type:
            by_type[t] = []
        by_type[t].append(sep)

    print(f"Types uniques: {len(by_type)}")
    print()

    # Analyse les premières scènes Type 0
    type_0_records = by_type.get(0, [])

    print(f"Type 0 (SCÈNES): {len(type_0_records)} records")
    print("=" * 80)
    print()

    for idx, sep in enumerate(type_0_records[:max_scenes]):
        print(f"\n{'─' * 80}")
        print(f"SCÈNE #{idx + 1} @ offset 0x{sep['pos']:08X}")
        print(f"{'─' * 80}")

        # Trouve prochain separator
        current_idx = separators.index(sep)
        next_pos = separators[current_idx + 1]['pos'] if current_idx + 1 < len(separators) else len(data)

        # Analyse Type 0
        analysis = analyze_type_0_structure(data, sep, next_pos)

        print(f"\nLongueur réelle: {analysis['length']} bytes")
        print(f"Strings trouvées: {len(analysis['strings'])}")

        # Patterns trouvés
        patterns = analysis['patterns']

        if patterns['dll_files']:
            print(f"\n📦 DLL Files ({len(patterns['dll_files'])}):")
            for dll in patterns['dll_files']:
                print(f"  - {dll}")

        if patterns['wav_files']:
            print(f"\n🔊 Audio WAV ({len(patterns['wav_files'])}):")
            for wav in patterns['wav_files'][:5]:
                print(f"  - {wav}")
            if len(patterns['wav_files']) > 5:
                print(f"  ... et {len(patterns['wav_files']) - 5} autres")

        if patterns['bmp_files']:
            print(f"\n🖼️  Images BMP ({len(patterns['bmp_files'])}):")
            for bmp in patterns['bmp_files'][:5]:
                print(f"  - {bmp}")
            if len(patterns['bmp_files']) > 5:
                print(f"  ... et {len(patterns['bmp_files']) - 5} autres")

        if patterns['avi_files']:
            print(f"\n🎬 Vidéos AVI ({len(patterns['avi_files'])}):")
            for avi in patterns['avi_files']:
                print(f"  - {avi}")

        if patterns['variables']:
            print(f"\n📊 Variables détectées ({len(patterns['variables'])}):")
            for var in patterns['variables'][:10]:
                print(f"  - {var}")
            if len(patterns['variables']) > 10:
                print(f"  ... et {len(patterns['variables']) - 10} autres")

        if patterns['fonts']:
            print(f"\n🔤 Polices/Formatage ({len(patterns['fonts'])}):")
            for font in patterns['fonts']:
                print(f"  - {font}")

        if patterns['coordinates']:
            print(f"\n📍 Coordonnées détectées ({len(patterns['coordinates'])}):")
            for coord_info in patterns['coordinates'][:5]:
                print(f"  - {coord_info['coords']['type']}: {coord_info['coords']['values']}")
                print(f"    Context: {coord_info['text'][:60]}")

        # Affiche records suivants (probablement enfants de cette scène)
        print(f"\n📋 Records suivants (possibles enfants):")
        for i in range(current_idx + 1, min(current_idx + 6, len(separators))):
            next_sep = separators[i]
            if next_sep['type'] == 0:
                break  # Nouvelle scène Type 0
            print(f"  - Type {next_sep['type']:3d} @ 0x{next_sep['pos']:08X}")

    # Analyse quelques Type 2 (hotspots)
    print("\n" + "=" * 80)
    print("ANALYSE TYPE 2 (HOTSPOTS RECTANGULAIRES)")
    print("=" * 80)

    type_2_records = by_type.get(2, [])[:3]

    for idx, sep in enumerate(type_2_records):
        current_idx = separators.index(sep)
        next_pos = separators[current_idx + 1]['pos'] if current_idx + 1 < len(separators) else len(data)

        analysis = analyze_type_2_hotspot(data, sep, next_pos)

        print(f"\nHotspot #{idx + 1}:")
        if analysis['coordinates_raw']:
            print(f"  Coordonnées brutes: {analysis['coordinates_raw']}")
            if len(analysis['coordinates_raw']) >= 4:
                x, y, w, h = analysis['coordinates_raw'][:4]
                print(f"  Rectangle: x={x}, y={y}, w={w}, h={h}")
        if analysis['text']:
            print(f"  Texte: {analysis['text'][:60]}")

    # Cherche Type 105 (polygones)
    print("\n" + "=" * 80)
    print("RECHERCHE TYPE 105 (POLYGONES)")
    print("=" * 80)

    type_105_records = by_type.get(105, [])

    if type_105_records:
        print(f"\nTrouvé {len(type_105_records)} records Type 105")

        for idx, sep in enumerate(type_105_records[:2]):
            current_idx = separators.index(sep)
            next_pos = separators[current_idx + 1]['pos'] if current_idx + 1 < len(separators) else len(data)

            pos = sep['pos'] + 12
            length = next_pos - pos

            record_data = data[pos:pos+length]

            print(f"\nPolygone #{idx + 1}:")
            print(f"  Longueur: {length} bytes")

            # Essaie de lire comme suite de coordonnées
            coords = []
            for i in range(0, min(100, len(record_data)), 4):
                if i + 4 <= len(record_data):
                    val = struct.unpack('<I', record_data[i:i+4])[0]
                    if val < 10000:
                        coords.append(val)

            if coords:
                print(f"  Coordonnées extraites ({len(coords)} valeurs):")
                # Affiche par paires (x, y)
                pairs = [(coords[i], coords[i+1]) if i+1 < len(coords) else (coords[i],) for i in range(0, min(20, len(coords)), 2)]
                print(f"  Points: {pairs}")
    else:
        print("\n⚠️  Aucun record Type 105 trouvé dans ce fichier")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_scene_structure.py <file.vnd>")
        sys.exit(1)

    analyze_vnd_scene_structure(sys.argv[1])
