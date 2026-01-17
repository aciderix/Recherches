#!/usr/bin/env python3
"""
Analyse détaillée du format des hotspots (Type 2)
Extrait coordonnées et structure
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

def parse_hotspot_type2(data):
    """Parse un hotspot Type 2"""
    # Lit jusqu'au premier null
    opcode_end = data.find(b'\x00')
    if opcode_end == -1:
        opcode = None
        coords_start = 0
    else:
        try:
            opcode = data[:opcode_end].decode('ascii')
            coords_start = opcode_end + 1
            # Skip nulls
            while coords_start < len(data) and data[coords_start] == 0:
                coords_start += 1
        except:
            opcode = None
            coords_start = 0

    # Lit les coordonnées comme suite d'entiers 32-bit little-endian
    coords = []
    pos = coords_start

    # Lit jusqu'à trouver du texte ASCII
    while pos + 4 <= len(data):
        val = struct.unpack('<I', data[pos:pos+4])[0]

        # Si on trouve un byte ASCII imprimable au début, c'est probablement du texte
        if data[pos] >= 32 and data[pos] < 127:
            break

        # Valeurs raisonnables pour coordonnées écran (0-2000)
        if val < 10000:
            coords.append(val)
            pos += 4
        else:
            pos += 1

    # Lit le texte restant
    text_data = data[pos:]
    text_end = text_data.find(b'\x00')
    if text_end != -1:
        text_data = text_data[:text_end]

    try:
        text = text_data.decode('ascii', errors='ignore').strip()
    except:
        text = None

    return {
        'opcode': opcode,
        'coordinates': coords,
        'text': text
    }

def analyze_all_hotspots(filename, max_count=10):
    """Analyse tous les hotspots Type 2"""
    with open(filename, 'rb') as f:
        data = f.read()

    separators = find_all_separators(data)

    # Filtre Type 2
    type2_records = [s for s in separators if s['type'] == 2]

    print("=" * 80)
    print(f"ANALYSE HOTSPOTS TYPE 2: {filename}")
    print("=" * 80)
    print()
    print(f"Total Type 2: {len(type2_records)}")
    print()

    for idx, sep in enumerate(type2_records[:max_count]):
        current_idx = separators.index(sep)
        next_pos = separators[current_idx + 1]['pos'] if current_idx + 1 < len(separators) else len(data)

        record_data = data[sep['pos']+12:next_pos]

        parsed = parse_hotspot_type2(record_data)

        print(f"{'─' * 80}")
        print(f"HOTSPOT #{idx + 1} @ 0x{sep['pos']:08X}")
        print(f"{'─' * 80}")

        if parsed['opcode']:
            print(f"  Opcode: {parsed['opcode']}")

        if parsed['coordinates']:
            print(f"  Coordonnées ({len(parsed['coordinates'])} valeurs):")

            # Essaie d'interpréter comme rectangle (x, y, w, h)
            if len(parsed['coordinates']) >= 4:
                coords = parsed['coordinates']
                print(f"    Première série (rectangle?):")
                print(f"      x={coords[0]}, y={coords[1]}, w={coords[2]}, h={coords[3]}")

                # Autres valeurs
                if len(coords) > 4:
                    print(f"    Autres valeurs: {coords[4:]}")

        if parsed['text']:
            print(f"  Texte: \"{parsed['text']}\"")

        print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_hotspot_format.py <file.vnd> [max_count]")
        sys.exit(1)

    filename = sys.argv[1]
    max_count = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    analyze_all_hotspots(filename, max_count)
