#!/usr/bin/env python3
"""
VND DECOMPILER - Décompilateur complet de fichiers VND
Extrait et affiche le contenu en pseudocode lisible
"""
import struct
import sys
import re
from collections import defaultdict

class VNDDecompiler:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'rb') as f:
            self.data = f.read()
        self.file_size = len(self.data)
        self.vnfile_pos = None
        self.variables = []
        self.records = []

    def find_vnfile_signature(self):
        """Trouve la signature VNFILE"""
        self.vnfile_pos = self.data.find(b'VNFILE')
        return self.vnfile_pos != -1

    def parse_header(self):
        """Parse le header VNFILE"""
        if not self.vnfile_pos:
            return None

        # Lit quelques infos basiques
        header_data = self.data[self.vnfile_pos:self.vnfile_pos+200]

        return {
            'signature': 'VNFILE',
            'position': self.vnfile_pos
        }

    def parse_variables(self):
        """Parse la table de variables"""
        # Cherche dans les premiers 5000 bytes
        pos = 0
        search_end = min(5000, self.file_size)

        while pos < search_end - 12:
            try:
                length = struct.unpack('<I', self.data[pos:pos+4])[0]

                # Filtre pour nom de variable
                if 3 <= length <= 30:
                    name_data = self.data[pos+4:pos+4+length]

                    # Vérifie ASCII
                    try:
                        name = name_data.decode('ascii')
                        if name.replace('_', '').replace('-', '').isalnum():
                            # Vérifie null terminator
                            if pos + 4 + length < self.file_size:
                                if self.data[pos + 4 + length] == 0:
                                    # Lit valeur
                                    if pos + 4 + length + 5 <= self.file_size:
                                        value = struct.unpack('<I', self.data[pos+4+length+1:pos+4+length+5])[0]

                                        self.variables.append({
                                            'name': name,
                                            'value': value,
                                            'offset': pos
                                        })

                                        pos += 4 + length + 1 + 4
                                        continue
                    except:
                        pass
            except:
                pass

            pos += 1

    def find_all_separators(self):
        """Trouve tous les séparateurs de records"""
        separators = []
        pos = 0

        while pos < self.file_size - 12:
            if struct.unpack('<I', self.data[pos:pos+4])[0] == 1:
                length = struct.unpack('<I', self.data[pos+4:pos+8])[0]
                type_id = struct.unpack('<I', self.data[pos+8:pos+12])[0]

                if length < 100000 and type_id < 200:
                    separators.append({
                        'pos': pos,
                        'length_field': length,
                        'type': type_id
                    })
            pos += 1

        return separators

    def parse_records(self):
        """Parse tous les records"""
        separators = self.find_all_separators()

        for i, sep in enumerate(separators):
            pos = sep['pos']
            type_id = sep['type']
            length_field = sep['length_field']

            # Calcule vraie longueur
            if i + 1 < len(separators):
                real_length = separators[i + 1]['pos'] - (pos + 12)
            else:
                real_length = self.file_size - (pos + 12)

            real_length = min(real_length, 50000)

            # Lit données
            data_start = pos + 12
            data_end = data_start + real_length
            if data_end > self.file_size:
                data_end = self.file_size
            record_data = self.data[data_start:data_end]

            # Décode le contenu
            decoded = self.decode_record(record_data, type_id)

            self.records.append({
                'index': i,
                'type': type_id,
                'length': real_length,
                'decoded': decoded,
                'raw': record_data
            })

    def decode_record(self, data, type_id):
        """Décode le contenu d'un record"""
        try:
            # Essaie de décoder en ASCII
            text = data.decode('ascii', errors='ignore')

            # Nettoie
            text = ''.join(c if c.isprintable() or c in '\n\r\t' else '.' for c in text)

            # Détecte patterns connus
            patterns = {
                'if_then': r'(\w+)\s*([<>=!]+)\s*(\d+)\s+then\s+(.+)',
                'runprj': r'runprj\s+([\w\.\\/]+)\s+(\d+)([a-z])',
                'playwav': r'playwav\s+([\w\.\\/]+)',
                'playavi': r'playavi\s+([\w\.\\/]+)',
                'addbmp': r'addbmp\s+(\w+)\s+([\w\.\\/]+)',
                'scene': r'scene\s+(\d+)([a-z]?)',
                'set_var': r'set_var\s+(\w+)\s+(-?\d+)',
                'inc_var': r'inc_var\s+(\w+)\s+(\d+)',
                'dec_var': r'dec_var\s+(\w+)\s+(\d+)',
            }

            detected_patterns = []
            for pattern_name, pattern_re in patterns.items():
                matches = re.finditer(pattern_re, text)
                for match in matches:
                    detected_patterns.append({
                        'type': pattern_name,
                        'match': match.group(0),
                        'groups': match.groups()
                    })

            return {
                'text': text[:200],  # Limite à 200 chars
                'patterns': detected_patterns
            }

        except:
            return {
                'text': f'<binary data: {len(data)} bytes>',
                'patterns': []
            }

    def decompile_to_pseudocode(self):
        """Génère le pseudocode du fichier VND"""
        output = []

        output.append("=" * 80)
        output.append(f"VND DECOMPILED: {self.filename}")
        output.append("=" * 80)
        output.append("")

        # Header
        if self.vnfile_pos is not None:
            output.append("HEADER:")
            output.append(f"  Signature: VNFILE @ 0x{self.vnfile_pos:04X}")
            output.append("")

        # Variables
        if self.variables:
            output.append(f"VARIABLES ({len(self.variables)}):")
            for var in self.variables[:30]:
                output.append(f"  {var['name']:20} = {var['value']}")
            if len(self.variables) > 30:
                output.append(f"  ... et {len(self.variables) - 30} autres")
            output.append("")

        # Records par type
        by_type = defaultdict(list)
        for rec in self.records:
            by_type[rec['type']].append(rec)

        output.append(f"RECORDS ({len(self.records)} total, {len(by_type)} types):")
        output.append("")

        # Affiche quelques records de chaque type
        for type_id in sorted(by_type.keys())[:15]:
            records = by_type[type_id]
            output.append(f"--- Type {type_id} ({len(records)} records) ---")

            for rec in records[:3]:
                decoded = rec['decoded']

                # Affiche patterns détectés
                if decoded['patterns']:
                    for pattern in decoded['patterns'][:2]:
                        output.append(f"  [{pattern['type']}] {pattern['match']}")
                else:
                    # Affiche texte brut
                    text = decoded['text'][:80]
                    if text.strip():
                        output.append(f"  {text}")

            if len(records) > 3:
                output.append(f"  ... et {len(records) - 3} autres records")
            output.append("")

        # Statistiques
        output.append("=" * 80)
        output.append("STATISTIQUES:")
        output.append("=" * 80)

        total_patterns = sum(len(rec['decoded']['patterns']) for rec in self.records)
        output.append(f"Total records: {len(self.records)}")
        output.append(f"Types uniques: {len(by_type)}")
        output.append(f"Variables: {len(self.variables)}")
        output.append(f"Patterns détectés: {total_patterns}")

        # Top types
        sorted_types = sorted(by_type.items(), key=lambda x: len(x[1]), reverse=True)[:10]
        output.append("")
        output.append("Top 10 types:")
        for type_id, records in sorted_types:
            pct = len(records) * 100.0 / len(self.records)
            output.append(f"  Type {type_id:3d}: {len(records):4d} records ({pct:5.1f}%)")

        return "\n".join(output)

    def save_decompiled(self, output_file=None):
        """Sauvegarde le pseudocode décompilé"""
        if output_file is None:
            output_file = self.filename.replace('.vnd', '_decompiled.txt')

        pseudocode = self.decompile_to_pseudocode()

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(pseudocode)

        return output_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_decompiler.py <file.vnd> [output.txt]")
        sys.exit(1)

    filename = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Décompilation de {filename}...")
    print()

    decompiler = VNDDecompiler(filename)

    # Parse
    decompiler.find_vnfile_signature()
    decompiler.parse_header()
    decompiler.parse_variables()
    decompiler.parse_records()

    # Génère pseudocode
    pseudocode = decompiler.decompile_to_pseudocode()

    # Affiche
    print(pseudocode)

    # Sauvegarde
    if output_file or '--save' in sys.argv:
        saved_file = decompiler.save_decompiled(output_file)
        print()
        print(f"Pseudocode sauvegardé: {saved_file}")

if __name__ == '__main__':
    main()
