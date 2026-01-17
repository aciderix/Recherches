#!/usr/bin/env python3
"""
VND Decompiler V5 - Final Version
Détecte les scènes par BMP files dans TOUS les types de records (pas seulement Type 0)
"""
import struct
import sys
import re

class VndDecompilerV5:
    """Décompilateur final - cherche les BMP dans tous les records"""

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.text_content = self.data.decode('latin-1', errors='replace')

    def find_all_separators(self):
        """Trouve tous les séparateurs 01 00 00 00"""
        separators = []
        pos = 0

        while pos < len(self.data) - 12:
            if struct.unpack('<I', self.data[pos:pos+4])[0] == 1:
                length = struct.unpack('<I', self.data[pos+4:pos+8])[0]
                type_id = struct.unpack('<I', self.data[pos+8:pos+12])[0]

                if length < 100000 and type_id < 200:
                    separators.append({
                        'pos': pos,
                        'length': length,
                        'type': type_id,
                        'data_offset': pos + 12
                    })
            pos += 1

        return separators

    def extract_text_at(self, offset, max_length):
        """Extrait texte lisible"""
        if offset >= len(self.data):
            return ""

        chunk = self.data[offset:min(offset + max_length, len(self.data))]
        text = chunk.decode('latin-1', errors='replace')

        # Filtre binaire avec limite de 30 caractères consécutifs
        filtered = []
        binary_count = 0

        for char in text:
            ord_val = ord(char)
            if (32 <= ord_val <= 126) or char in ['\n', '\r', '\t'] or char in 'àâäéèêëïîôùûüÿçœæÀÂÄÉÈÊËÏÎÔÙÛÜŸÇŒÆ':
                if binary_count > 5:
                    filtered.append(' ')
                filtered.append(char)
                binary_count = 0
            else:
                binary_count += 1
                if binary_count <= 30:
                    if filtered and filtered[-1] != ' ':
                        filtered.append(' ')
                else:
                    break

        return ''.join(filtered).strip()

    def parse_and_display(self):
        """Parse avec détection BMP multi-types"""
        print("=" * 80)
        print(f"VND DÉCOMPILATEUR V5 - DÉTECTION BMP MULTI-TYPES")
        print(f"Fichier: {self.filepath}")
        print("=" * 80)
        print()

        separators = self.find_all_separators()

        # Ajoute next_offset
        for i in range(len(separators) - 1):
            separators[i]['next_offset'] = separators[i + 1]['pos']
        if separators:
            separators[-1]['next_offset'] = len(self.data)

        # Cherche TOUS les records contenant un BMP euroland
        scene_records = []
        for sep in separators:
            offset = sep['data_offset']
            next_offset = sep.get('next_offset', len(self.data))
            length = next_offset - offset

            text = self.extract_text_at(offset, min(length, 1000))

            # Cherche euroland BMP
            bmp_match = re.search(r'euroland[/\\\\]([\w]+\.bmp)', text, re.IGNORECASE)
            if bmp_match and 'rollover' not in bmp_match.group(0).lower():
                scene_records.append({
                    'pos': sep['pos'],
                    'type': sep['type'],
                    'bmp': bmp_match.group(0),
                    'text': text
                })

        print(f"Total records: {len(separators)}")
        print(f"Scènes détectées (records avec BMP): {len(scene_records)}")
        print()

        # Affiche les scènes
        for scene_num, scene_rec in enumerate(scene_records, 1):
            print("═" * 80)
            print(f"SCÈNE #{scene_num} @ 0x{scene_rec['pos']:08X} (Type {scene_rec['type']})")
            print("═" * 80)

            # WAV
            wav_match = re.search(r'([\w\\\\/-]+\.wav)', scene_rec['text'], re.IGNORECASE)
            if wav_match:
                print(f"🔊 {wav_match.group(1)}")

            # BMP
            print(f"🖼️  {scene_rec['bmp']}")

            # Hotspots/textes
            font_match = re.search(r'(\d{2})\s+(\d+)\s+(#[0-9a-fA-F]{6})\s+([\w\s]+)', scene_rec['text'])
            if font_match:
                print(f"📝 Police: {font_match.group(1)}pt {font_match.group(4)} {font_match.group(3)}")

            # Coordonnées texte
            coords = list(re.finditer(r'(\d+)\s+(\d+)\s+125\s+365\s+\d+\s+([^\n]+)', scene_rec['text']))
            if coords:
                print(f"📍 Hotspots:")
                for match in coords[:3]:
                    clean_text = match.group(3).strip().replace('&', '')[:40]
                    print(f"   • ({match.group(1)}, {match.group(2)}): {clean_text}")
                if len(coords) > 3:
                    print(f"   ... et {len(coords)-3} autres hotspots")

            # Conditions
            conditions = list(re.finditer(r'(\w+)\s*([<>=!]+)\s*(\d+)\s+then', scene_rec['text']))
            if conditions:
                print(f"🔀 Conditions:")
                for match in conditions[:2]:
                    print(f"   • if {match.group(1)} {match.group(2)} {match.group(3)} then...")
                if len(conditions) > 2:
                    print(f"   ... et {len(conditions)-2} autres conditions")

            # Opcodes navigation
            nav_refs = re.findall(r'\b(\d+)([a-z])\b', scene_rec['text'])
            if nav_refs:
                unique_navs = list(set([f"{num}{op}" for num, op in nav_refs if len(num) <= 3]))[:5]
                if unique_navs:
                    print(f"🧭 Navigation: {', '.join(unique_navs)}")

            print()

        print("=" * 80)
        print("FIN")
        print("=" * 80)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_decompiler_v5_final.py <file.vnd>")
        sys.exit(1)

    decompiler = VndDecompilerV5(sys.argv[1])
    decompiler.parse_and_display()

if __name__ == '__main__':
    main()
