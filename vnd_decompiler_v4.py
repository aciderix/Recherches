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
        """Extrait le texte à un offset donné, filtre les caractères binaires mais continue"""
        if offset + length > len(self.text_content):
            length = len(self.text_content) - offset
        text = self.text_content[offset:offset+length]

        # Filtre les caractères binaires mais continue (ne s'arrête pas)
        filtered = []
        binary_count = 0
        max_consec_binary = 30  # Saute les grosses zones binaires

        for i, char in enumerate(text):
            ord_val = ord(char)

            # Caractères imprimables normaux
            if (32 <= ord_val <= 126) or char in ['\n', '\r', '\t']:
                # Si on sortait d'une zone binaire, ajoute un espace
                if binary_count > 5:
                    filtered.append(' ')
                filtered.append(char)
                binary_count = 0
            # Accents français
            elif char in 'àâäéèêëïîôùûüÿçœæÀÂÄÉÈÊËÏÎÔÙÛÜŸÇŒÆ':
                if binary_count > 5:
                    filtered.append(' ')
                filtered.append(char)
                binary_count = 0
            # Caractère binaire
            else:
                binary_count += 1
                # Saute les grosses zones binaires (ne les affiche pas)
                if binary_count <= max_consec_binary:
                    # Petites zones binaires: remplace par espace
                    if len(filtered) > 0 and filtered[-1] != ' ':
                        filtered.append(' ')

        # Nettoie les espaces multiples
        result = ''.join(filtered)
        result = re.sub(r' +', ' ', result)
        return result.strip()

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

    def find_scene_boundaries(self):
        """Trouve les limites des scènes basées sur les fichiers BMP"""
        # Cherche tous les euroland\*.bmp (sans rollover)
        scene_boundaries = []

        for match in re.finditer(r'(euroland\\[\w]+\.bmp)', self.text_content, re.IGNORECASE):
            bmp = match.group(1)
            pos = match.start()

            # Ignore fichiers rollover
            if 'rollover' in bmp.lower():
                continue

            scene_boundaries.append({
                'pos': pos,
                'bmp': bmp
            })

        return scene_boundaries

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

        # Trouve les limites des scènes (par BMP)
        scene_boundaries = self.find_scene_boundaries()

        print(f"Total records: {len(separators)}")
        print(f"Total polygones: {len(self.polygons_map)}")
        print(f"Total scènes (BMP): {len(scene_boundaries)}")
        print()

        # Parse scènes basées sur les BMP
        for scene_idx, scene_bound in enumerate(scene_boundaries):
            scene_num = scene_idx + 1
            bmp_pos = scene_bound['pos']
            bmp_file = scene_bound['bmp']

            # Trouve la fin de cette scène (début de la prochaine)
            if scene_idx + 1 < len(scene_boundaries):
                scene_end = scene_boundaries[scene_idx + 1]['pos']
            else:
                scene_end = len(self.data)

            print("\n" + "═" * 80)
            print(f"SCÈNE #{scene_num} @ 0x{bmp_pos:08X}")
            print("═" * 80)

            # Extrait le texte de la scène (200 chars avant le BMP pour le nom, WAV)
            scene_start = max(0, bmp_pos - 200)
            scene_text = self.extract_text_at(scene_start, min(5000, scene_end - scene_start))

            # Cherche nom de scène (ligne avant le BMP)
            before_bmp = self.extract_text_at(max(0, bmp_pos - 100), 100)
            lines = before_bmp.split('\n')
            scene_name = None
            for line in reversed(lines[:-1]):  # Ignore dernière ligne (le BMP lui-même)
                line = line.strip()
                if line and not line.endswith('.bmp') and not line.endswith('.wav') and not line.endswith('.dll'):
                    if 3 < len(line) < 60 and not re.search(r'then|playtext|addbmp|set_var|\d+\s+\d+\s+125', line):
                        scene_name = line
                        break

            if scene_name:
                print(f"{scene_name}")

            # Cherche fichier WAV avant ou après le BMP
            audio_match = re.search(r'([\w\\/-]+\.wav)', scene_text[:500], re.IGNORECASE)
            if audio_match:
                print(f"{audio_match.group(1)}")

            print(f"{bmp_file}")
            print()

            # Trouve tous les records dans cette scène
            hotspot_num = 0
            for sep in separators:
                offset = sep['data_offset']
                if bmp_pos <= offset < scene_end:
                    next_offset = sep.get('next_offset', len(self.data))
                    length = next_offset - offset
                    text = self.extract_text_at(offset, min(length, 5000))
                    rec_type = sep['type']

                    # Type 0 au début de scène = déjà affiché (BMP)
                    if rec_type == 0:
                        continue

                    # Autres types = potentiellement hotspot/contenu
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

                        # Cherche références de navigation/scène (comme "5i", "51j", "35")
                        nav_refs = re.findall(r'\b(\d+)([a-z])\b', text)
                        for num, opcode in nav_refs:
                            if len(num) <= 3:  # Limite aux numéros raisonnables
                                print(f"{num}{opcode}")

                        # Cherche polygone avec coordonnées
                        for poly_offset, poly in self.polygons_map.items():
                            if offset <= poly_offset < next_offset:
                                bbox = poly['bbox']
                                print(f"[Polygone {poly['count']} points]")
                                # Affiche premiers points
                                pts_str = ' '.join([f"({p[0]},{p[1]})" for p in poly['points'][:4]])
                                if len(poly['points']) > 4:
                                    pts_str += " ..."
                                print(f"  Points: {pts_str}")
                                print(f"  BBox: ({bbox[0]},{bbox[1]})-({bbox[2]},{bbox[3]})")

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
