#!/usr/bin/env python3
"""
VND Decompiler V5 - Parsing Binaire Correct par Type
Parse chaque type de record selon sa structure binaire documentée.
"""
import struct
import sys
import re
from typing import List, Dict, Optional, Tuple

class VndDecompilerV5:
    """Décompilateur qui parse correctement les données binaires par type"""

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.text_content = self.data.decode('latin-1', errors='replace')

    def find_all_separators(self):
        """Trouve tous les séparateurs dans l'ordre"""
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

    def extract_text_clean(self, data, max_len=None):
        """Extrait texte ASCII/Latin-1 propre depuis des bytes"""
        if max_len:
            data = data[:max_len]

        text = data.decode('latin-1', errors='replace')
        # Garde uniquement caractères imprimables + accents
        result = []
        for char in text:
            if (32 <= ord(char) <= 126) or char in '\n\r\t' or char in 'àâäéèêëïîôùûüÿçœæÀÂÄÉÈÊËÏÎÔÙÛÜŸÇŒÆ':
                result.append(char)
            elif ord(char) == 0:  # Null terminator
                break
            else:
                result.append(' ')

        return ''.join(result).strip()

    def parse_type_0(self, data, length):
        """Type 0: Métadonnées et Scène (DLL, variables, BMP)"""
        text = self.extract_text_clean(data, length)

        # Cherche fichiers
        bmps = re.findall(r'[\w\\/-]+\.bmp', text, re.IGNORECASE)
        dlls = re.findall(r'[\w\\/-]+\.dll', text, re.IGNORECASE)
        wavs = re.findall(r'[\w\\/-]+\.wav', text, re.IGNORECASE)
        variables = re.findall(r'\b([A-Z]{3,20})\b', text)

        return {
            'text': text,
            'bmps': bmps,
            'dlls': dlls,
            'wavs': wavs,
            'variables': variables[:10]  # Limite
        }

    def parse_type_1(self, data, length):
        """Type 1: Action/Destination (souvent court avec opcode)"""
        text = self.extract_text_clean(data, min(length, 200))

        # Cherche patterns d'action
        patterns = []

        # Scene change: "3i" = scene 3
        scene_match = re.search(r'(\d+)([a-z])', text)
        if scene_match:
            patterns.append({
                'type': 'scene',
                'value': scene_match.group(1),
                'opcode': scene_match.group(2)
            })

        # Conditions
        cond_matches = re.findall(r'(\w+)\s*([<>=!]+)\s*(-?\d+)\s+then\s+([^\n]+)', text)
        for match in cond_matches:
            patterns.append({
                'type': 'condition',
                'var': match[0],
                'op': match[1],
                'val': match[2],
                'action': match[3].strip()
            })

        return {
            'text': text,
            'patterns': patterns
        }

    def parse_type_2(self, data, length):
        """Type 2: Hotspot Rectangulaire (binaire: X1 Y1 X2 Y2)"""
        # Essaye de lire coordonnées binaires
        if length >= 16:
            try:
                x1 = struct.unpack('<i', data[0:4])[0]
                y1 = struct.unpack('<i', data[4:8])[0]
                x2 = struct.unpack('<i', data[8:12])[0]
                y2 = struct.unpack('<i', data[12:16])[0]

                # Validation (coordonnées dans 640x480)
                if -100 <= x1 <= 700 and -100 <= y1 <= 500 and -100 <= x2 <= 700 and -100 <= y2 <= 500:
                    return {
                        'rect': (x1, y1, x2, y2),
                        'text': self.extract_text_clean(data[16:], length - 16) if length > 16 else ''
                    }
            except:
                pass

        # Sinon texte
        return {'text': self.extract_text_clean(data, length)}

    def parse_type_38(self, data, length):
        """Type 38: Texte de Hotspot (format: X Y W H layer text)"""
        text = self.extract_text_clean(data, length)

        # Parse "X Y 125 365 layer text"
        match = re.search(r'(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.+)', text)
        if match:
            return {
                'x': int(match.group(1)),
                'y': int(match.group(2)),
                'w': int(match.group(3)),
                'h': int(match.group(4)),
                'layer': int(match.group(5)),
                'text': match.group(6).strip()
            }

        return {'raw_text': text}

    def parse_type_105(self, data, length):
        """Type 105: Polygone (binaire: count + points x,y)"""
        if length < 8:
            return None

        try:
            count = struct.unpack('<I', data[0:4])[0]

            if not (3 <= count <= 50) or length < 4 + count * 8:
                return None

            points = []
            for i in range(count):
                offset = 4 + i * 8
                x = struct.unpack('<i', data[offset:offset+4])[0]
                y = struct.unpack('<i', data[offset+4:offset+8])[0]

                # Validation
                if not (-200 <= x <= 2000 and -200 <= y <= 2000):
                    return None

                points.append((x, y))

            # Calcule bounding box
            xs = [p[0] for p in points]
            ys = [p[1] for p in points]

            return {
                'count': count,
                'points': points,
                'bbox': (min(xs), min(ys), max(xs), max(ys))
            }
        except:
            return None

    def parse_type_font(self, data, length):
        """Types 7, 26, 39: Police (format: SIZE STYLE #COLOR FONT)"""
        text = self.extract_text_clean(data, length)

        match = re.search(r'(\d+)\s+(\d+)\s+(#[0-9a-fA-F]{6})\s+(Comic\s+sans\s+MS|[\w\s]+)', text, re.IGNORECASE)
        if match:
            return {
                'size': int(match.group(1)),
                'style': int(match.group(2)),
                'color': match.group(3),
                'font': match.group(4).strip(),
                'raw': text
            }

        return {'raw_text': text}

    def parse_record(self, rec):
        """Parse un record selon son type"""
        offset = rec['data_offset']
        length = rec['length']
        type_id = rec['type']
        data = self.data[offset:offset+length]

        if type_id == 0:
            return self.parse_type_0(data, length)
        elif type_id == 1:
            return self.parse_type_1(data, length)
        elif type_id == 2:
            return self.parse_type_2(data, length)
        elif type_id == 38:
            return self.parse_type_38(data, length)
        elif type_id == 105:
            return self.parse_type_105(data, length)
        elif type_id in [7, 26, 39]:
            return self.parse_type_font(data, length)
        else:
            # Autres types: texte générique + patterns
            text = self.extract_text_clean(data, min(length, 500))

            # Cherche fichiers multimédias
            avis = re.findall(r'([\w\\/-]+\.avi)\s+(\d+)', text, re.IGNORECASE)
            wavs = re.findall(r'([\w\\/-]+\.wav)', text, re.IGNORECASE)

            # Cherche commandes
            commands = []
            for cmd in ['runprj', 'playwav', 'playavi', 'addbmp', 'delbmp', 'set_var', 'inc_var', 'dec_var', 'playtext', 'scene', 'closewav', 'rundll']:
                matches = re.findall(rf'{cmd}\s+([^\n]+)', text, re.IGNORECASE)
                for m in matches:
                    commands.append(f"{cmd} {m.strip()}")

            return {
                'text': text,
                'avis': avis,
                'wavs': wavs,
                'commands': commands[:10]
            }

    def decompile(self):
        """Décompile le fichier VND"""
        print("=" * 80)
        print(f"VND DECOMPILER V5 - PARSING BINAIRE PAR TYPE")
        print(f"Fichier: {self.filepath}")
        print("=" * 80)
        print()

        separators = self.find_all_separators()
        print(f"Total records: {len(separators)}")
        print()

        scene_num = 0
        hotspot_num = 0

        for i, rec in enumerate(separators):
            type_id = rec['type']
            parsed = self.parse_record(rec)

            # Type 0 = Nouvelle scène
            if type_id == 0:
                scene_num += 1
                hotspot_num = 0

                print("\n" + "─" * 80)
                print(f"SCÈNE #{scene_num} @ 0x{rec['pos']:08X}")
                print("─" * 80)

                if parsed.get('bmps'):
                    print(f"🖼️  Fond: {parsed['bmps'][0]}")
                if parsed.get('wavs'):
                    print(f"🔊 Audio: {parsed['wavs'][0]}")
                if parsed.get('dlls'):
                    print(f"📦 DLL: {parsed['dlls'][0]}")
                if parsed.get('variables'):
                    print(f"📊 Variables: {', '.join(parsed['variables'][:5])}")
                print()

            # Type 38 = Début de hotspot (texte)
            elif type_id == 38:
                hotspot_num += 1
                print(f"\n[HOTSPOT #{hotspot_num}]")

                if 'x' in parsed:
                    print(f"  Texte: \"{parsed['text']}\" @ ({parsed['x']}, {parsed['y']})")
                else:
                    print(f"  {parsed.get('raw_text', '')}")

            # Type 105 = Polygone
            elif type_id == 105:
                if parsed:
                    bbox = parsed['bbox']
                    print(f"  Polygone: {parsed['count']} points - BBox ({bbox[0]},{bbox[1]})-({bbox[2]},{bbox[3]})")
                    # Affiche premiers points
                    pts_str = ', '.join([f"({p[0]},{p[1]})" for p in parsed['points'][:3]])
                    if len(parsed['points']) > 3:
                        pts_str += ", ..."
                    print(f"    Points: {pts_str}")

            # Type 2 = Rectangle ou texte
            elif type_id == 2:
                if 'rect' in parsed:
                    r = parsed['rect']
                    print(f"  Rectangle: ({r[0]},{r[1]})-({r[2]},{r[3]})")
                    if parsed['text']:
                        print(f"  {parsed['text']}")
                else:
                    if parsed.get('text'):
                        print(f"  {parsed['text']}")

            # Types 7, 26, 39 = Police
            elif type_id in [7, 26, 39]:
                if 'size' in parsed:
                    print(f"  Police: {parsed['size']}pt {parsed['font']} {parsed['color']}")

            # Type 1 = Action/Destination
            elif type_id == 1:
                for p in parsed.get('patterns', []):
                    if p['type'] == 'scene':
                        print(f"  → Scène {p['value']} (opcode: {p['opcode']})")
                    elif p['type'] == 'condition':
                        print(f"  Condition: {p['var']} {p['op']} {p['val']} then {p['action']}")

                if parsed.get('text') and not parsed.get('patterns'):
                    # Affiche texte court
                    txt = parsed['text'][:100]
                    if txt.strip():
                        print(f"  {txt}")

            # Autres types
            else:
                # Affiche vidéos
                for avi, loop in parsed.get('avis', []):
                    print(f"  🎬 {avi} (loop: {loop})")

                # Affiche audio
                for wav in parsed.get('wavs', []):
                    print(f"  🔊 {wav}")

                # Affiche commandes
                for cmd in parsed.get('commands', []):
                    print(f"  {cmd}")

        print("\n" + "=" * 80)
        print("FIN DU FICHIER")
        print("=" * 80)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_decompiler_v5.py <file.vnd>")
        print("\nDécompile le VND avec parsing binaire correct par type")
        sys.exit(1)

    decompiler = VndDecompilerV5(sys.argv[1])
    decompiler.decompile()

if __name__ == '__main__':
    main()
