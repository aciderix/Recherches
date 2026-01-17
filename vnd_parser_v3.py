#!/usr/bin/env python3
"""
VND Parser v3 - Gestion correcte des records Type 0
La vraie longueur = distance au prochain séparateur (pas le champ LENGTH)
"""
import struct
import sys
import re

class VNDParserV3:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'rb') as f:
            self.data = f.read()
        self.file_size = len(self.data)
        self.vnfile_pos = None
        self.separators = []
        self.records = []

    def find_all_separators(self):
        """Trouve TOUS les séparateurs 01 00 00 00"""
        print("Recherche des séparateurs...")
        pos = 0
        while pos < self.file_size - 12:
            if struct.unpack('<I', self.data[pos:pos+4])[0] == 1:
                # Vérifie length et type
                length = struct.unpack('<I', self.data[pos+4:pos+8])[0]
                type_id = struct.unpack('<I', self.data[pos+8:pos+12])[0]

                # Filtre raisonnable
                if length < 100000 and type_id < 200:
                    self.separators.append({
                        'pos': pos,
                        'length_field': length,
                        'type': type_id
                    })
            pos += 1

        print(f"✓ Trouvé {len(self.separators)} séparateurs")

    def parse_records(self):
        """Parse tous les records avec gestion Type 0"""
        print("\nParsing records...")

        for i, sep in enumerate(self.separators):
            pos = sep['pos']
            type_id = sep['type']
            length_field = sep['length_field']

            # Calcule vraie longueur = distance au prochain séparateur
            if i + 1 < len(self.separators):
                next_pos = self.separators[i + 1]['pos']
                real_length = next_pos - (pos + 12)
            else:
                # Dernier record
                real_length = self.file_size - (pos + 12)

            # Limite raisonnable
            real_length = min(real_length, 50000)

            # Lit les données
            data_start = pos + 12
            data_end = data_start + real_length
            if data_end > self.file_size:
                data_end = self.file_size
            record_data = self.data[data_start:data_end]

            # Stocke
            self.records.append({
                'index': i,
                'pos': pos,
                'type': type_id,
                'length_field': length_field,
                'real_length': real_length,
                'data': record_data
            })

        print(f"✓ Parsed {len(self.records)} records")

    def analyze_type0(self):
        """Analyse spéciale pour Type 0"""
        type0_records = [r for r in self.records if r['type'] == 0]

        if not type0_records:
            print("\n⚠ Aucun record Type 0 trouvé")
            return

        print(f"\n{'='*80}")
        print(f"ANALYSE TYPE 0 (SCENES) - {len(type0_records)} records")
        print(f"{'='*80}")

        for rec in type0_records[:10]:  # 10 premiers
            print(f"\nRecord #{rec['index']} @ 0x{rec['pos']:04X} (Type 0)")
            print(f"  LENGTH field: {rec['length_field']} bytes")
            print(f"  REAL length: {rec['real_length']} bytes")

            if rec['length_field'] != rec['real_length']:
                diff = abs(rec['real_length'] - rec['length_field'])
                print(f"  ⚠ DIFF: {diff} bytes ({diff*100//max(rec['real_length'],1)}%)")

            # Extrait strings ASCII
            data = rec['data']
            strings = self.extract_strings(data, min_len=4)
            if strings:
                print(f"  Strings: {', '.join(strings[:8])}")

            # Cherche opcodes (number+letter)
            opcodes = self.extract_opcodes(data)
            if opcodes:
                print(f"  Opcodes: {', '.join(opcodes[:10])}")

    def extract_strings(self, data, min_len=3):
        """Extrait strings ASCII lisibles"""
        strings = []
        current = []
        for b in data:
            if 32 <= b < 127 and b != ord('|'):
                current.append(chr(b))
            else:
                if len(current) >= min_len:
                    s = ''.join(current)
                    if not s.replace('.', '').replace('\\', '').isdigit():
                        strings.append(s)
                current = []
        return strings[:20]

    def extract_opcodes(self, data):
        """Extrait opcodes number+letter"""
        try:
            text = data.decode('ascii', errors='ignore')
            pattern = r'(\d+)([a-z])'
            matches = re.findall(pattern, text)
            return [f'{num}{op}' for num, op in matches[:20]]
        except:
            return []

    def print_summary(self):
        """Affiche résumé"""
        print(f"\n{'='*80}")
        print("RÉSUMÉ")
        print(f"{'='*80}")
        print(f"Fichier: {self.filename}")
        print(f"Taille: {self.file_size:,} bytes ({self.file_size/1024:.1f} KB)")
        print(f"Records: {len(self.records)}")
        print()

        # Par type
        by_type = {}
        for rec in self.records:
            t = rec['type']
            if t not in by_type:
                by_type[t] = []
            by_type[t].append(rec)

        print("DISTRIBUTION PAR TYPE:")
        print("-" * 80)
        for t in sorted(by_type.keys())[:20]:
            count = len(by_type[t])
            avg_real = sum(r['real_length'] for r in by_type[t]) // count
            print(f"  Type {t:3d} (0x{t:02X}): {count:4d} records (avg size: {avg_real:5d} bytes)")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_parser_v3.py <file.vnd>")
        sys.exit(1)

    filename = sys.argv[1]

    print("="*80)
    print("VND PARSER V3 - Type 0 Support")
    print("="*80)
    print()

    parser = VNDParserV3(filename)
    parser.find_all_separators()
    parser.parse_records()
    parser.print_summary()
    parser.analyze_type0()

if __name__ == '__main__':
    main()
