#!/usr/bin/env python3
"""
Mapper Records → Opcodes
Analyse les records VND et identifie quels opcodes sont utilisés par chaque type
"""
import struct
import re
from collections import defaultdict, Counter

def find_vnfile_signature(data):
    """Trouve la signature VNFILE"""
    return data.find(b'VNFILE')

def find_first_separator(data, start=0x80):
    """Trouve le premier séparateur de record (01 00 00 00 = 1)"""
    for i in range(start, len(data) - 12):
        separator = struct.unpack('<I', data[i:i+4])[0]
        if separator == 1:
            # Vérifie que c'est suivi d'une longueur et type raisonnables
            length = struct.unpack('<I', data[i+4:i+8])[0]
            type_id = struct.unpack('<I', data[i+8:i+12])[0]
            if length < 100000 and type_id < 50:
                return i
    return None

def extract_opcodes_from_data(data):
    """Extrait les opcodes (nombre+lettre) d'un bloc de données"""
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

        # Check que ce n'est pas du texte (ex: "bibliobis.avi 1")
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

def parse_records_with_opcodes(vnd_file):
    """Parse les records et extrait les opcodes de chaque record"""

    with open(vnd_file, 'rb') as f:
        data = f.read()

    print("="*80)
    print(f"MAPPING RECORDS → OPCODES: {vnd_file}")
    print("="*80)
    print()

    # Trouve le début des records
    sig_pos = find_vnfile_signature(data)
    if sig_pos == -1:
        print("✗ Signature VNFILE non trouvée")
        return

    print(f"✓ Signature VNFILE @ 0x{sig_pos:04X}")

    record_start = find_first_separator(data)
    if not record_start:
        print("✗ Aucun record trouvé")
        return

    print(f"✓ Premier record @ 0x{record_start:04X}")
    print()

    # Parse tous les records
    records = []
    offset = record_start
    record_num = 0

    print("PARSING RECORDS...")
    print("-" * 80)

    while offset < len(data) - 12 and record_num < 500:
        # Lit le séparateur
        separator = struct.unpack('<I', data[offset:offset+4])[0]

        if separator != 1:
            print(f"✓ Fin des records @ 0x{offset:04X}")
            break

        # Lit length et type
        length = struct.unpack('<I', data[offset+4:offset+8])[0]
        type_id = struct.unpack('<I', data[offset+8:offset+12])[0]

        if length > 100000:
            print(f"⚠ Longueur invalide {length} @ 0x{offset:04X}")
            break

        # Lit les données du record
        record_data_start = offset + 12

        # Pour Type 0, la longueur ne représente pas la taille totale
        # On doit chercher le prochain séparateur
        if type_id == 0:
            # Cherche le prochain record
            next_sep_pos = offset + 12
            found_next = False

            for i in range(offset + 12, min(offset + 10000, len(data) - 4)):
                test_sep = struct.unpack('<I', data[i:i+4])[0]
                if test_sep == 1:
                    # Vérifie que c'est vraiment un record
                    if i + 8 <= len(data):
                        test_len = struct.unpack('<I', data[i+4:i+8])[0]
                        if 0 <= test_len < 100000:
                            next_sep_pos = i
                            found_next = True
                            break

            if found_next:
                actual_length = next_sep_pos - record_data_start
            else:
                actual_length = min(length, 5000)
        else:
            actual_length = length

        record_data = data[record_data_start:record_data_start + actual_length]

        # Extrait les opcodes de ce record
        opcodes = extract_opcodes_from_data(record_data)

        records.append({
            'number': record_num,
            'offset': offset,
            'type': type_id,
            'length_field': length,
            'actual_length': actual_length,
            'opcodes': opcodes,
            'data_preview': record_data[:100] if len(record_data) > 0 else b''
        })

        # Affiche résumé
        opcode_str = ', '.join([op['full'] for op in opcodes[:10]])
        if len(opcodes) > 10:
            opcode_str += f" ... ({len(opcodes)} total)"

        print(f"Record {record_num:3d}  @ 0x{offset:06X}  Type={type_id:2d}  Len={actual_length:5d}  Opcodes: {opcode_str}")

        # Avance au prochain record
        if type_id == 0:
            offset = next_sep_pos if found_next else offset + 12 + actual_length
        else:
            offset += 12 + length

        record_num += 1

    print()
    print(f"✓ Parsé {len(records)} records")
    print()

    # Analyse par type de record
    print("="*80)
    print("ANALYSE PAR TYPE DE RECORD")
    print("="*80)
    print()

    records_by_type = defaultdict(list)
    for rec in records:
        records_by_type[rec['type']].append(rec)

    for record_type in sorted(records_by_type.keys()):
        recs = records_by_type[record_type]
        print(f"TYPE {record_type:2d}: {len(recs)} records")
        print("-" * 80)

        # Compte les opcodes utilisés
        all_opcodes = []
        for rec in recs:
            all_opcodes.extend([op['opcode'] for op in rec['opcodes']])

        opcode_counts = Counter(all_opcodes)

        if opcode_counts:
            print(f"  Opcodes utilisés ({len(all_opcodes)} total):")
            for opcode, count in opcode_counts.most_common(10):
                index = ord(opcode) - ord('a') + 1
                print(f"    '{opcode}' (idx {index:2d}): {count:3d} fois")
        else:
            print("  Aucun opcode trouvé")

        # Exemples de records
        print(f"\n  Exemples:")
        for rec in recs[:3]:
            preview = rec['data_preview'][:60].decode('latin-1', errors='replace')
            preview = preview.replace('\n', '\\n').replace('\r', '\\r').replace('\x00', '.')
            print(f"    Record {rec['number']} @ 0x{rec['offset']:06X}: {preview}...")

        print()

    # Résumé global
    print("="*80)
    print("RÉSUMÉ GLOBAL")
    print("="*80)
    print()

    all_opcodes_global = []
    for rec in records:
        all_opcodes_global.extend([op['opcode'] for op in rec['opcodes']])

    opcode_counts_global = Counter(all_opcodes_global)

    print(f"Total opcodes trouvés: {len(all_opcodes_global)}")
    print()
    print("TOP 20 OPCODES:")
    print("-" * 80)
    for opcode, count in opcode_counts_global.most_common(20):
        index = ord(opcode) - ord('a') + 1

        # Nom selon OPCODES_SYSTEM_COMPLETE.md
        names = {
            6: 'Navigation/scene',
            8: 'Tooltip',
            9: 'Images',
            10: 'Bitmaps',
            11: 'Audio WAV',
            12: 'Music MIDI',
            21: 'Logic if/then'
        }
        name = names.get(index, '?')

        print(f"  '{opcode}' (idx {index:2d} - {name:20s}): {count:4d} fois")

    return records, records_by_type

def main():
    import sys

    if len(sys.argv) < 2:
        vnd_file = "couleurs1.vnd"
    else:
        vnd_file = sys.argv[1]

    parse_records_with_opcodes(vnd_file)

if __name__ == '__main__':
    main()
