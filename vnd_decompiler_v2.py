#!/usr/bin/env python3
"""
VND DECOMPILER V2 - Version améliorée avec meilleur filtrage
Extrait seulement les données significatives (patterns + strings lisibles)
"""
import struct
import sys
import re
from collections import defaultdict

class VNDDecompilerV2:
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

    def parse_variables(self):
        """Parse la table de variables"""
        pos = 0
        search_end = min(5000, self.file_size)

        while pos < search_end - 12:
            try:
                length = struct.unpack('<I', self.data[pos:pos+4])[0]

                if 3 <= length <= 30:
                    name_data = self.data[pos+4:pos+4+length]

                    try:
                        name = name_data.decode('ascii')
                        if name.replace('_', '').replace('-', '').isalnum():
                            if pos + 4 + length < self.file_size:
                                if self.data[pos + 4 + length] == 0:
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

    def extract_meaningful_strings(self, data, min_length=4):
        """Extrait seulement les strings significatives (>=min_length caractères consécutifs)"""
        strings = []
        current = []

        for byte in data:
            # Caractères imprimables ASCII (32-126) + espaces, tabs
            if 32 <= byte <= 126 or byte in [9, 10, 13]:
                current.append(chr(byte))
            else:
                if len(current) >= min_length:
                    s = ''.join(current).strip()
                    if s and not s.replace('.', '').replace(' ', '') == '':
                        strings.append(s)
                current = []

        # Dernière string
        if len(current) >= min_length:
            s = ''.join(current).strip()
            if s and not s.replace('.', '').replace(' ', '') == '':
                strings.append(s)

        return strings

    def detect_patterns(self, text):
        """Détecte les patterns connus dans le texte"""
        patterns_config = {
            'if_then': r'(\w+)\s*([<>=!]+)\s*(-?\d+)\s+then\s+(.+?)(?:\s|$)',
            'runprj': r'runprj\s+([\w\.\\/]+)\s+(\d+)([a-z]?)',
            'playwav': r'playwav\s+([\w\.\\/]+)(?:\s+(\d+))?',
            'playavi': r'playavi\s+([\w\.\\/]+)(?:\s+(\d+))?',
            'addbmp': r'addbmp\s+(\w+)(?:\s+([\w\.\\/]+))?',
            'scene': r'scene\s+(\d+)([a-z]?)',
            'set_var': r'set_var\s+(\w+)\s+(-?\d+)',
            'inc_var': r'inc_var\s+(\w+)\s+(\d+)',
            'dec_var': r'dec_var\s+(\w+)\s+(\d+)',
            'playtext': r'playtext\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)(?:\s+(\d+))?(?:\s+(.+))?',
            'addtext': r'addtext\s+(\w+)\s+(\d+)\s+(\d+)\s+(\d+)(?:\s+(.+))?',
            'closewav': r'closewav(?:\s|$)',
            'rundll': r'rundll\s+([\w\.\\/]+)',
        }

        detected = []
        for pattern_name, pattern_re in patterns_config.items():
            matches = re.finditer(pattern_re, text, re.IGNORECASE)
            for match in matches:
                detected.append({
                    'type': pattern_name,
                    'match': match.group(0).strip(),
                    'groups': match.groups()
                })

        return detected

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

            # Décode le contenu (version améliorée)
            decoded = self.decode_record_improved(record_data, type_id)

            self.records.append({
                'index': i,
                'type': type_id,
                'length': real_length,
                'decoded': decoded,
                'raw': record_data
            })

    def decode_record_improved(self, data, type_id):
        """Décode le contenu d'un record (version améliorée)"""
        try:
            # Extrait strings significatives
            strings = self.extract_meaningful_strings(data, min_length=3)

            # Concatène pour détecter patterns
            full_text = ' '.join(strings)

            # Détecte patterns
            patterns = self.detect_patterns(full_text)

            # Détermine quoi afficher
            display_items = []

            if patterns:
                # Si on a des patterns, affiche-les
                for p in patterns:
                    display_items.append({
                        'type': 'pattern',
                        'content': f"[{p['type']}] {p['match']}"
                    })

            # Ajoute les strings significatives non déjà couvertes par patterns
            if strings:
                # Filtre les strings qui ne sont pas déjà dans les patterns
                pattern_texts = [p['match'] for p in patterns]
                unique_strings = []

                for s in strings:
                    # Garde seulement si pas déjà dans un pattern
                    if not any(s in pt or pt in s for pt in pattern_texts):
                        # Filtre les strings trop courtes ou non significatives
                        if len(s) >= 3 and not s.replace('.', '').replace('\\', '') == '':
                            unique_strings.append(s)

                # Limite à 3 strings max
                for s in unique_strings[:3]:
                    display_items.append({
                        'type': 'string',
                        'content': s[:100]  # Limite longueur
                    })

            return {
                'items': display_items,
                'patterns': patterns,
                'strings': strings,
                'has_data': len(strings) > 0 or len(patterns) > 0
            }

        except Exception as e:
            return {
                'items': [],
                'patterns': [],
                'strings': [],
                'has_data': False,
                'error': str(e)
            }

    def decompile_to_pseudocode(self):
        """Génère le pseudocode du fichier VND (version améliorée)"""
        output = []

        output.append("=" * 80)
        output.append(f"VND DECOMPILED V2: {self.filename}")
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

        # Affiche records par type
        for type_id in sorted(by_type.keys()):
            records = by_type[type_id]

            # Compte combien ont des données significatives
            with_data = [r for r in records if r['decoded']['has_data']]

            output.append(f"--- Type {type_id} ({len(records)} records, {len(with_data)} with data) ---")

            # Affiche jusqu'à 5 records avec données
            shown = 0
            for rec in records:
                if shown >= 5:
                    break

                decoded = rec['decoded']
                if decoded['items']:
                    for item in decoded['items'][:3]:  # Max 3 items par record
                        output.append(f"  {item['content']}")
                    shown += 1

            if len(with_data) > 5:
                output.append(f"  ... et {len(with_data) - 5} autres records avec données")
            elif len(records) > len(with_data):
                output.append(f"  ... et {len(records) - len(with_data)} records vides/binaires")

            output.append("")

        # Statistiques
        output.append("=" * 80)
        output.append("STATISTIQUES:")
        output.append("=" * 80)

        total_patterns = sum(len(rec['decoded']['patterns']) for rec in self.records)
        records_with_data = sum(1 for rec in self.records if rec['decoded']['has_data'])

        output.append(f"Total records: {len(self.records)}")
        output.append(f"Records avec données: {records_with_data}")
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

        # Patterns les plus fréquents
        pattern_counts = defaultdict(int)
        for rec in self.records:
            for p in rec['decoded']['patterns']:
                pattern_counts[p['type']] += 1

        if pattern_counts:
            output.append("")
            output.append("Patterns les plus fréquents:")
            for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
                output.append(f"  {pattern:15}: {count:4d} occurrences")

        return "\n".join(output)

    def save_decompiled(self, output_file=None):
        """Sauvegarde le pseudocode décompilé"""
        if output_file is None:
            output_file = self.filename.replace('.vnd', '_decompiled_v2.txt')

        pseudocode = self.decompile_to_pseudocode()

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(pseudocode)

        return output_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_decompiler_v2.py <file.vnd> [output.txt]")
        sys.exit(1)

    filename = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Décompilation V2 de {filename}...")
    print()

    decompiler = VNDDecompilerV2(filename)

    # Parse
    decompiler.find_vnfile_signature()
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
        print(f"✓ Pseudocode sauvegardé: {saved_file}")

if __name__ == '__main__':
    main()
