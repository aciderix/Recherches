#!/usr/bin/env python3
"""
VND Decompiler V3 - Ordre Séquentiel
Affiche les records dans l'ORDRE DU FICHIER (comme le moteur les lit)
Montre la hiérarchie naturelle et le flux d'exécution
"""
import struct
import sys
import re
from typing import List, Tuple, Optional

class VndDecompilerV3:
    """Décompilateur qui respecte l'ordre séquentiel du fichier"""

    # Types connus
    TYPE_SCENE = 0
    TYPE_CONDITION = 1
    TYPE_HOTSPOT = 2
    TYPE_HOTSPOT_TEXT = 38
    TYPE_FONT = 39
    TYPE_POLYGON = 105

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.text_content = self.data.decode('latin-1', errors='replace')
        self.current_scene_id = 0
        self.polygons_map = self._find_all_polygons()

    def _find_all_polygons(self):
        """Trouve tous les polygones dans le fichier (signature 0x69)"""
        polygons = {}
        pos = 0

        while pos < len(self.data) - 8:
            # Cherche signature 0x69 00 00 00
            if self.data[pos:pos+4] == b'\x69\x00\x00\x00':
                count = struct.unpack('<I', self.data[pos+4:pos+8])[0]

                if 3 <= count <= 50:
                    points = []
                    valid = True

                    for i in range(count):
                        pt_offset = pos + 8 + i * 8
                        if pt_offset + 8 > len(self.data):
                            valid = False
                            break

                        x = struct.unpack('<i', self.data[pt_offset:pt_offset+4])[0]
                        y = struct.unpack('<i', self.data[pt_offset+4:pt_offset+8])[0]

                        if not (-200 <= x <= 2000 and -200 <= y <= 2000):
                            valid = False
                            break

                        points.append((x, y))

                    if valid and points:
                        xs = [p[0] for p in points]
                        ys = [p[1] for p in points]
                        bbox = (min(xs), min(ys), max(xs), max(ys))

                        polygons[pos] = {
                            'offset': pos,
                            'count': count,
                            'points': points,
                            'bbox': bbox
                        }

            pos += 1

        return polygons

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
                        'length_field': length,
                        'type': type_id
                    })
            pos += 1

        return separators

    def extract_strings(self, data, min_len=3):
        """Extrait strings ASCII significatives"""
        strings = []
        current = []

        for byte in data:
            if 32 <= byte <= 126 or byte in [9, 10, 13]:
                current.append(chr(byte))
            else:
                if len(current) >= min_len:
                    s = ''.join(current).strip()
                    if s and not s.replace('.', '').replace(' ', '') == '':
                        strings.append(s)
                current = []

        if len(current) >= min_len:
            s = ''.join(current).strip()
            if s:
                strings.append(s)

        return strings

    def parse_polygon(self, data, offset) -> Optional[dict]:
        """Parse un polygone Type 105"""
        if offset + 8 > len(data):
            return None

        record_type = struct.unpack('<I', data[offset:offset+4])[0]
        if record_type != self.TYPE_POLYGON:
            return None

        count = struct.unpack('<I', data[offset+4:offset+8])[0]

        if not (3 <= count <= 50):
            return None

        points = []
        for i in range(count):
            pt_offset = offset + 8 + i * 8
            if pt_offset + 8 > len(data):
                return None

            x = struct.unpack('<i', data[pt_offset:pt_offset+4])[0]
            y = struct.unpack('<i', data[pt_offset+4:pt_offset+8])[0]

            if not (-200 <= x <= 2000 and -200 <= y <= 2000):
                return None

            points.append((x, y))

        if points:
            xs = [p[0] for p in points]
            ys = [p[1] for p in points]
            bbox = (min(xs), min(ys), max(xs), max(ys))

            return {
                'points': points,
                'count': count,
                'bbox': bbox
            }

        return None

    def detect_patterns(self, text):
        """Détecte patterns connus dans le texte"""
        patterns = []

        patterns_config = {
            'if_then': r'(\w+)\s*([<>=!]+)\s*(-?\d+)\s+then\s+(.+)',
            'runprj': r'runprj\s+([\w\.\\/]+)\s+(\d+)([a-z]?)',
            'playwav': r'playwav\s+([\w\.\\/]+)',
            'playavi': r'playavi\s+([\w\.\\/]+)',
            'addbmp': r'addbmp\s+(\w+)',
            'scene': r'scene\s+(\d+)([a-z]?)',
            'set_var': r'set_var\s+(\w+)\s+(-?\d+)',
            'inc_var': r'inc_var\s+(\w+)\s+(\d+)',
            'dec_var': r'dec_var\s+(\w+)\s+(\d+)',
        }

        for pattern_name, pattern_re in patterns_config.items():
            matches = re.finditer(pattern_re, text, re.IGNORECASE)
            for match in matches:
                patterns.append({
                    'type': pattern_name,
                    'match': match.group(0).strip()
                })

        return patterns

    def decode_record(self, data, type_id, offset, next_offset):
        """Décode un record selon son type"""
        length = next_offset - offset if next_offset else len(data) - offset
        record_data = data[offset:offset+length]

        result = {
            'type': type_id,
            'offset': offset,
            'length': length,
            'content': []
        }

        # Type 0: Scène (métadonnées)
        if type_id == self.TYPE_SCENE:
            self.current_scene_id += 1
            strings = self.extract_strings(record_data, min_len=3)

            # Cherche images, audio, DLL
            images = [s for s in strings if '.bmp' in s.lower()]
            audio = [s for s in strings if '.wav' in s.lower()]
            videos = [s for s in strings if '.avi' in s.lower()]
            dlls = [s for s in strings if '.dll' in s.lower()]
            variables = [s for s in strings if s.isupper() and len(s) >= 3 and s.isalpha()]
            fonts = [s for s in strings if 'Comic sans' in s or '#' in s]

            result['scene_id'] = self.current_scene_id
            result['images'] = images[:5]
            result['audio'] = audio[:3]
            result['videos'] = videos[:3]
            result['dlls'] = dlls
            result['variables'] = variables[:10]
            result['fonts'] = fonts[:2]

        # Type 1: Conditions (peut contenir polygones!)
        elif type_id == 1:
            strings = self.extract_strings(record_data, min_len=3)
            full_text = ' '.join(strings)
            patterns = self.detect_patterns(full_text)
            result['patterns'] = patterns
            result['strings'] = strings[:5]

            # Cherche polygones DANS ce record
            polygons_in_record = []
            for poly_offset, poly in self.polygons_map.items():
                if offset <= poly_offset < offset + length:
                    polygons_in_record.append(poly)

            if polygons_in_record:
                result['polygons'] = polygons_in_record

        # Type 2: Hotspot (peut contenir opcode + coordonnées)
        elif type_id == 2:
            strings = self.extract_strings(record_data, min_len=2)
            # Premier string = souvent opcode
            if strings:
                result['opcode'] = strings[0]
                result['text'] = strings[1] if len(strings) > 1 else None

        # Type 38: Hotspot text (X Y 125 365 layer text)
        elif type_id == 38:
            text = self.text_content[offset:offset+length]
            match = re.search(r'(\d{1,3})\s+(\d{1,3})\s+125\s+365\s+(\d+)\s+([^\x00\r\n]+)', text)
            if match:
                result['text_x'] = int(match.group(1))
                result['text_y'] = int(match.group(2))
                result['layer'] = int(match.group(3))
                result['text'] = match.group(4).strip()

        # Type 105: Polygone
        elif type_id == 105:
            # Cherche dans les données brutes
            poly_offset = 0
            # Scan pour trouver le vrai offset du polygone
            for i in range(max(0, offset - 100), min(len(data), offset + 100)):
                poly = self.parse_polygon(data, i)
                if poly:
                    result['polygon'] = poly
                    break

        # Autres types: extraction patterns + strings
        else:
            strings = self.extract_strings(record_data, min_len=3)
            full_text = ' '.join(strings)
            patterns = self.detect_patterns(full_text)

            if patterns:
                result['patterns'] = patterns
            if strings:
                result['strings'] = strings[:5]

        return result

    def parse_sequential(self):
        """Parse le fichier dans l'ordre séquentiel"""
        print("=" * 80)
        print(f"VND DECOMPILER V3 - ORDRE SÉQUENTIEL")
        print(f"Fichier: {self.filepath}")
        print("=" * 80)
        print()

        # Trouve tous les separators
        separators = self.find_all_separators()

        print(f"Total records: {len(separators)}")
        print(f"Total polygones: {len(self.polygons_map)}")
        print()
        print("=" * 80)
        print("RECORDS DANS L'ORDRE DU FICHIER")
        print("=" * 80)
        print()

        # Parse chaque record dans l'ordre
        indent_level = 0
        last_type = None
        last_pos = 0

        for i, sep in enumerate(separators):
            offset = sep['pos'] + 12  # Skip header
            next_pos = separators[i + 1]['pos'] if i + 1 < len(separators) else len(self.data)
            type_id = sep['type']

            # Décode le record
            decoded = self.decode_record(self.data, type_id, offset, next_pos)

            # Gestion indentation (Type 0 = nouvelle scène, reset indent)
            if type_id == self.TYPE_SCENE:
                indent_level = 0
                if i > 0:
                    print()  # Ligne vide avant nouvelle scène
            elif last_type == self.TYPE_SCENE:
                indent_level = 1  # Records après Type 0 sont enfants

            indent = "  " * indent_level

            # Vérifie s'il y a des polygones entre last_pos et ce record
            for poly_offset, poly in sorted(self.polygons_map.items()):
                if last_pos < poly_offset < sep['pos']:
                    bbox = poly['bbox']
                    print(f"{indent}  [Polygone @ 0x{poly_offset:08X}] {poly['count']} points")
                    print(f"{indent}    Points: {poly['points'][:3]}...")
                    print(f"{indent}    BBox: ({bbox[0]},{bbox[1]}) → ({bbox[2]},{bbox[3]})")

            # Affiche selon le type
            if type_id == self.TYPE_SCENE:
                scene_id = decoded.get('scene_id', '?')
                print(f"\n{'─' * 80}")
                print(f"SCÈNE #{scene_id} @ 0x{sep['pos']:08X} (Type 0)")
                print(f"{'─' * 80}")

                if decoded.get('images'):
                    print(f"{indent}🖼️  Images: {', '.join(decoded['images'])}")
                if decoded.get('audio'):
                    print(f"{indent}🔊 Audio: {', '.join(decoded['audio'])}")
                if decoded.get('videos'):
                    print(f"{indent}🎬 Vidéos: {', '.join(decoded['videos'])}")
                if decoded.get('dlls'):
                    print(f"{indent}📦 DLL: {', '.join(decoded['dlls'])}")
                if decoded.get('variables'):
                    vars_str = ', '.join(decoded['variables'][:5])
                    remaining = len(decoded['variables']) - 5
                    if remaining > 0:
                        vars_str += f" ... +{remaining}"
                    print(f"{indent}📊 Variables: {vars_str}")

            elif type_id == 1:
                print(f"{indent}[Type 1 @ 0x{sep['pos']:08X}] Condition/Logic")
                for pattern in decoded.get('patterns', [])[:3]:
                    print(f"{indent}  → [{pattern['type']}] {pattern['match']}")

                # Affiche polygones intégrés
                for poly in decoded.get('polygons', []):
                    bbox = poly['bbox']
                    print(f"{indent}  ✓ Polygone: {poly['count']} points @ 0x{poly['offset']:08X}")
                    print(f"{indent}    Points: {poly['points'][:3]}...")
                    print(f"{indent}    BBox: ({bbox[0]},{bbox[1]}) → ({bbox[2]},{bbox[3]})")

            elif type_id == 2:
                opcode = decoded.get('opcode', '?')
                text = decoded.get('text', '')
                print(f"{indent}[Type 2 @ 0x{sep['pos']:08X}] Hotspot: {opcode}")
                if text:
                    print(f"{indent}  Text: {text}")

            elif type_id == 38:
                text = decoded.get('text', '?')
                x = decoded.get('text_x', 0)
                y = decoded.get('text_y', 0)
                print(f"{indent}[Type 38 @ 0x{sep['pos']:08X}] Hotspot Text")
                print(f"{indent}  \"{text}\" @ ({x}, {y})")

            elif type_id == 105:
                poly = decoded.get('polygon')
                if poly:
                    bbox = poly['bbox']
                    print(f"{indent}[Type 105 @ 0x{sep['pos']:08X}] Polygone ({poly['count']} points)")
                    print(f"{indent}  Points: {poly['points'][:3]}...")
                    print(f"{indent}  BBox: ({bbox[0]},{bbox[1]}) → ({bbox[2]},{bbox[3]})")
                else:
                    print(f"{indent}[Type 105 @ 0x{sep['pos']:08X}] Polygone (parse failed)")

            else:
                # Autres types
                patterns = decoded.get('patterns', [])
                strings = decoded.get('strings', [])

                if patterns:
                    print(f"{indent}[Type {type_id} @ 0x{sep['pos']:08X}]")
                    for pattern in patterns[:2]:
                        print(f"{indent}  → [{pattern['type']}] {pattern['match']}")
                elif strings:
                    print(f"{indent}[Type {type_id} @ 0x{sep['pos']:08X}] {strings[0][:50]}")

            last_type = type_id
            last_pos = next_pos

        # Affiche polygones restants après le dernier record
        for poly_offset, poly in sorted(self.polygons_map.items()):
            if poly_offset > last_pos:
                bbox = poly['bbox']
                print(f"  [Polygone @ 0x{poly_offset:08X}] {poly['count']} points")
                print(f"    Points: {poly['points'][:3]}...")
                print(f"    BBox: ({bbox[0]},{bbox[1]}) → ({bbox[2]},{bbox[3]})")

        print()
        print("=" * 80)
        print("FIN DU FICHIER")
        print("=" * 80)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_decompiler_v3.py <file.vnd>")
        print("\nDécompile le VND dans l'ordre SÉQUENTIEL (comme le moteur le lit)")
        sys.exit(1)

    decompiler = VndDecompilerV3(sys.argv[1])
    decompiler.parse_sequential()

if __name__ == '__main__':
    main()
