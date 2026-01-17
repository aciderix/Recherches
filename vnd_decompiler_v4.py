#!/usr/bin/env python3
"""
VND Decompiler V4 - Structure Hiérarchique
Parse et affiche le VND avec une structure lisible:
- Scènes avec nom, musique, fond
- Hotspots regroupés avec toutes leurs données
- Conditions séparées (pas concaténées)
"""
import struct
import sys
import re
from typing import List, Dict, Optional, Tuple

class VndDecompilerV4:
    """Décompilateur qui regroupe les données en structure hiérarchique"""

    # Types connus
    TYPE_SCENE = 0
    TYPE_CONDITION = 1
    TYPE_HOTSPOT = 2

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
                        'type': type_id,
                        'data_offset': pos + 12
                    })
            pos += 1

        return separators

    def extract_text_at(self, offset, length):
        """Extrait le texte à un offset donné, filtré des caractères binaires"""
        if offset + length > len(self.text_content):
            length = len(self.text_content) - offset
        text = self.text_content[offset:offset+length]

        # Filtre les caractères binaires tout en gardant les caractères imprimables
        filtered = []
        for char in text:
            # Garde: lettres, chiffres, ponctuation, espaces, accents
            if (32 <= ord(char) <= 126) or char in ['\n', '\r', '\t']:
                filtered.append(char)
            elif 128 <= ord(char) <= 255:
                # Garde les accents français communs
                if char in 'àâäéèêëïîôùûüÿçœæÀÂÄÉÈÊËÏÎÔÙÛÜŸÇŒÆ':
                    filtered.append(char)
                else:
                    filtered.append(' ')
            else:
                # Remplace les autres par un espace
                filtered.append(' ')

        return ''.join(filtered)

    def parse_conditions_separately(self, text):
        """Parse les conditions et les sépare proprement"""
        conditions = []

        # Patterns pour différents types de conditions
        patterns = [
            (r'(\w+)\s*([<>=!]+)\s*(-?\d+)\s+then\s+([^;\n]+)', 'if_then'),
            (r'runprj\s+([\w\.\\/]+)\s+(\d+)([a-z]?)', 'runprj'),
            (r'playwav\s+([\w\.\\/]+)(?:\s+(\d+))?([a-z]?)', 'playwav'),
            (r'playavi\s+([\w\.\\/]+)(?:\s+(\d+))?(?:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+))?', 'playavi'),
            (r'addbmp\s+(\w+)\s+([\w\.\\/]+)\s+(\d+)\s+(\d+)\s+(\d+)', 'addbmp'),
            (r'delbmp\s+(\w+)', 'delbmp'),
            (r'scene\s+(\d+)([a-z]?)', 'scene'),
            (r'set_var\s+(\w+)\s+(-?\d+)', 'set_var'),
            (r'inc_var\s+(\w+)\s+(\d+)', 'inc_var'),
            (r'dec_var\s+(\w+)\s+(\d+)', 'dec_var'),
            (r'playtext\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.+)', 'playtext'),
            (r'closewav', 'closewav'),
            (r'rundll\s+([\w\.]+)', 'rundll'),
        ]

        for pattern, name in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                conditions.append({
                    'type': name,
                    'text': match.group(0).strip(),
                    'start': match.start(),
                    'end': match.end()
                })

        # Trie par position
        conditions.sort(key=lambda x: x['start'])
        return conditions

    def parse_font_spec(self, text):
        """Parse une spécification de police: 18 0 #ffffff Comic sans MS"""
        match = re.search(r'(\d+)\s+(\d+)\s+(#[0-9a-fA-F]{6})\s+(Comic\s+sans\s+MS)', text, re.IGNORECASE)
        if match:
            return {
                'size': int(match.group(1)),
                'style': int(match.group(2)),
                'color': match.group(3),
                'font': match.group(4).strip()
            }
        return None

    def parse_text_coords(self, text):
        """Parse coordonnées de texte: X Y 125 365 layer TEXT"""
        matches = list(re.finditer(r'(\d+)\s+(\d+)\s+125\s+365\s+(\d+)\s+([^\n]+)', text))
        return [{
            'x': int(m.group(1)),
            'y': int(m.group(2)),
            'layer': int(m.group(3)),
            'text': m.group(4).strip()
        } for m in matches]

    def group_into_hotspots(self, records):
        """Regroupe les records en hotspots logiques"""
        hotspots = []
        current_hotspot = None
        current_font = None

        for rec in records:
            rec_type = rec['type']
            offset = rec['data_offset']
            next_offset = rec.get('next_offset', len(self.data))
            length = next_offset - offset
            text = self.extract_text_at(offset, min(length, 5000))

            # Type 0 = nouvelle scène (pas un hotspot)
            if rec_type == 0:
                if current_hotspot:
                    hotspots.append(current_hotspot)
                    current_hotspot = None
                continue

            # Détecte spécification de police (début de nouveau hotspot ou section)
            font = self.parse_font_spec(text)
            if font:
                # Si on a déjà un hotspot avec une police différente, on crée une nouvelle section
                if current_hotspot and current_font:
                    # Nouvelle section dans le même hotspot
                    current_hotspot['sections'].append({
                        'font': font,
                        'texts': [],
                        'conditions': [],
                        'actions': []
                    })
                    current_font = font
                else:
                    # Nouveau hotspot
                    if current_hotspot:
                        hotspots.append(current_hotspot)
                    current_hotspot = {
                        'start_offset': offset,
                        'sections': [{
                            'font': font,
                            'texts': [],
                            'conditions': [],
                            'actions': []
                        }],
                        'polygon': None,
                        'terminator': None
                    }
                    current_font = font

            # Parse le contenu
            if current_hotspot:
                section = current_hotspot['sections'][-1]

                # Cherche coordonnées de texte
                text_coords = self.parse_text_coords(text)
                section['texts'].extend(text_coords)

                # Cherche conditions/actions
                conditions = self.parse_conditions_separately(text)
                for cond in conditions:
                    if cond['type'] in ['if_then', 'set_var', 'inc_var', 'dec_var']:
                        section['conditions'].append(cond)
                    else:
                        section['actions'].append(cond)

                # Cherche polygone dans ce record
                for poly_offset, poly in self.polygons_map.items():
                    if offset <= poly_offset < next_offset:
                        current_hotspot['polygon'] = poly

                # Cherche terminateur (lettre seule à la fin)
                terminator = re.search(r'([a-z])\s*$', text)
                if terminator:
                    current_hotspot['terminator'] = terminator.group(1)

        if current_hotspot:
            hotspots.append(current_hotspot)

        return hotspots

    def parse_and_display(self):
        """Parse le fichier et affiche la structure"""
        print("=" * 80)
        print(f"VND DECOMPILER V4 - STRUCTURE HIÉRARCHIQUE")
        print(f"Fichier: {self.filepath}")
        print("=" * 80)
        print()

        # Trouve tous les separators
        separators = self.find_all_separators()

        # Ajoute next_offset à chaque separator
        for i in range(len(separators) - 1):
            separators[i]['next_offset'] = separators[i + 1]['pos']
        if separators:
            separators[-1]['next_offset'] = len(self.data)

        print(f"Total records: {len(separators)}")
        print(f"Total polygones: {len(self.polygons_map)}")
        print()

        # Parse scènes et hotspots
        scene_num = 0
        hotspot_num = 0
        i = 0

        while i < len(separators):
            sep = separators[i]
            rec_type = sep['type']
            offset = sep['data_offset']
            next_offset = sep.get('next_offset', len(self.data))
            length = next_offset - offset
            text = self.extract_text_at(offset, min(length, 5000))

            # Type 0 = Scène
            if rec_type == 0:
                scene_num += 1
                hotspot_num = 0

                print("\n" + "─" * 80)
                print(f"SCÈNE #{scene_num} @ 0x{sep['pos']:08X}")
                print("─" * 80)

                # Scan les 5 prochains records pour collecter les infos de scène
                scene_text = text
                for j in range(1, min(6, len(separators) - i)):
                    next_sep = separators[i + j]
                    next_off = next_sep['data_offset']
                    next_len = min(2000, next_sep.get('next_offset', len(self.data)) - next_off)
                    scene_text += ' ' + self.extract_text_at(next_off, next_len)

                # Cherche nom de scène (première ligne significative)
                lines = text.split('\n')
                scene_name = None
                for line in lines[:10]:
                    line = line.strip()
                    if line and not line.endswith('.bmp') and not line.endswith('.wav') and not line.endswith('.dll') and not line.endswith('.avi'):
                        if 3 < len(line) < 50 and not re.match(r'^\d+', line) and not re.search(r'then|playtext|addbmp', line):
                            scene_name = line
                            break

                if scene_name:
                    print(f"Nom: {scene_name}")

                # Cherche fichiers dans scene_text
                audio_files = list(set(re.findall(r'[\w\\/-]+\.wav', scene_text, re.IGNORECASE)))
                image_files = list(set(re.findall(r'[\w\\/-]+\.bmp', scene_text, re.IGNORECASE)))

                # Filtre les fichiers rollover
                image_files = [f for f in image_files if 'rollover' not in f.lower()]

                if audio_files:
                    print(f"🔊 Audio: {audio_files[0]}")
                if image_files:
                    print(f"🖼️  Fond: {image_files[0]}")
                print()

            # Autres types = potentiellement hotspot
            else:
                # Détecte si c'est un début de hotspot (contient une font spec)
                font = self.parse_font_spec(text)
                if font:
                    hotspot_num += 1
                    print(f"\n[HOTSPOT #{hotspot_num}]")
                    print(f"{font['size']} {font['style']} {font['color']} {font['font']}")

                # Affiche les coordonnées de texte
                text_coords = self.parse_text_coords(text)
                seen_coords = set()
                for tc in text_coords:
                    clean_text = tc['text'].replace('&', '').strip()
                    # Nettoie davantage (enlève codes binaires résiduels)
                    clean_text = re.sub(r'\s{3,}', ' ', clean_text)  # Multiple espaces
                    clean_text = re.sub(r'^\d+\s+\d+\s+#[0-9a-fA-F]+', '', clean_text).strip()  # Codes de police

                    # Ignore si c'est juste des codes ou déjà vu
                    coord_key = (tc['x'], tc['y'], clean_text)
                    if len(clean_text) > 2 and not re.match(r'^[\d\s#]+$', clean_text) and coord_key not in seen_coords:
                        print(f"{tc['x']} {tc['y']} 125 365 {tc['layer']} {clean_text}")
                        seen_coords.add(coord_key)

                # Affiche les vidéos
                video_matches = re.findall(r'([\w\\/-]+\.avi)\s+(\d+)', text, re.IGNORECASE)
                seen_videos = set()
                for vm in video_matches:
                    if vm[0] not in seen_videos:
                        print(f"{vm[0]} {vm[1]}")
                        seen_videos.add(vm[0])

                # Affiche les conditions séparément
                conditions = self.parse_conditions_separately(text)
                printed_conditions = set()
                for cond in conditions:
                    # Évite les doublons
                    clean_cond = cond['text'].strip()
                    if clean_cond not in printed_conditions and len(clean_cond) > 5:
                        print(f"{clean_cond}")
                        printed_conditions.add(clean_cond)

                # Cherche polygone
                for poly_offset, poly in self.polygons_map.items():
                    if offset <= poly_offset < next_offset:
                        bbox = poly['bbox']
                        print(f"[Polygone {poly['count']} points]")

                # Cherche terminateur
                terminator_matches = re.findall(r'\b([a-z])\s*$', text[:500])
                if terminator_matches and len(terminator_matches[-1]) == 1:
                    print(f"{terminator_matches[-1]}")

            i += 1

        print("=" * 80)
        print("FIN DU FICHIER")
        print("=" * 80)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_decompiler_v4.py <file.vnd>")
        print("\nDécompile le VND avec une structure hiérarchique lisible")
        sys.exit(1)

    decompiler = VndDecompilerV4(sys.argv[1])
    decompiler.parse_and_display()

if __name__ == '__main__':
    main()
