#!/usr/bin/env python3
"""
VND Decompiler V4 - Structure basée sur Type 0 Records
Les Type 0 records sont les délimiteurs:
- Type 0 avec BMP = nouvelle scène
- Type 0 sans BMP = nouveau hotspot dans la scène courante
"""
import struct
import sys
import re
from typing import List, Dict, Optional

class VndDecompilerV4:
    """Décompilateur qui utilise les Type 0 records comme délimiteurs structurels"""

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.text_content = self.data.decode('latin-1', errors='replace')
        self.polygons_map = self.find_all_polygons()

    def find_all_separators(self):
        """Trouve tous les séparateurs 01 00 00 00 dans le fichier"""
        separators = []
        pos = 0

        while pos < len(self.data) - 12:
            if struct.unpack('<I', self.data[pos:pos+4])[0] == 1:
                length = struct.unpack('<I', self.data[pos+4:pos+8])[0]
                type_id = struct.unpack('<I', self.data[pos+8:pos+12])[0]

                # Filtre valeurs invalides
                if length < 100000 and type_id < 200:
                    separators.append({
                        'pos': pos,
                        'length': length,
                        'type': type_id,
                        'data_offset': pos + 12
                    })
            pos += 1

        return separators

    def find_all_polygons(self):
        """Trouve tous les polygones (Type 105) avec leurs coordonnées"""
        polygons = {}
        pos = 0

        while pos < len(self.data) - 16:
            # Cherche signature 0x69 (105) avec séparateur
            if (pos >= 12 and
                struct.unpack('<I', self.data[pos-12:pos-8])[0] == 1 and
                struct.unpack('<I', self.data[pos-4:pos])[0] == 105):

                try:
                    count = struct.unpack('<I', self.data[pos:pos+4])[0]

                    # Validation
                    if 3 <= count <= 50 and pos + 4 + count * 8 <= len(self.data):
                        points = []
                        valid = True

                        for i in range(count):
                            offset = pos + 4 + i * 8
                            x = struct.unpack('<i', self.data[offset:offset+4])[0]
                            y = struct.unpack('<i', self.data[offset+4:offset+8])[0]

                            if not (-200 <= x <= 2000 and -200 <= y <= 2000):
                                valid = False
                                break

                            points.append((x, y))

                        if valid and len(points) == count:
                            xs = [p[0] for p in points]
                            ys = [p[1] for p in points]

                            polygons[pos] = {
                                'count': count,
                                'points': points,
                                'bbox': (min(xs), min(ys), max(xs), max(ys))
                            }
                except:
                    pass

            pos += 1

        return polygons

    def extract_text_at(self, offset, max_length):
        """Extrait texte lisible depuis un offset jusqu'au prochain séparateur"""
        if offset >= len(self.data):
            return ""

        # Lit les données brutes
        end_pos = min(offset + max_length, len(self.data))
        chunk = self.data[offset:end_pos]

        # Décode en Latin-1
        text = chunk.decode('latin-1', errors='replace')

        # Filtre les caractères binaires mais continue (ne s'arrête pas)
        filtered = []
        binary_count = 0
        max_consec_binary = 30  # Stop après 30 caractères binaires consécutifs

        for i, char in enumerate(text):
            ord_val = ord(char)

            # Caractères imprimables ASCII
            if (32 <= ord_val <= 126) or char in ['\n', '\r', '\t']:
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

            # Binaire
            else:
                binary_count += 1
                if binary_count <= max_consec_binary:
                    if len(filtered) > 0 and filtered[-1] != ' ':
                        filtered.append(' ')
                elif binary_count == max_consec_binary + 1:
                    # Stop après 30 caractères binaires
                    break

        return ''.join(filtered).strip()

    def parse_font_spec(self, text):
        """Parse une spécification de police: SIZE STYLE #COLOR FONT"""
        match = re.search(r'(\d{2})\s+(\d+)\s+(#[0-9a-fA-F]{6})\s+(Comic\s+sans\s+MS|\w[\w\s]+)', text, re.IGNORECASE)
        if match:
            return {
                'size': match.group(1),
                'style': match.group(2),
                'color': match.group(3),
                'font': match.group(4).strip()
            }
        return None

    def parse_text_coords(self, text):
        """Parse les coordonnées de texte: X Y W H layer text"""
        coords = []
        # Pattern: X Y 125 365 layer text
        for match in re.finditer(r'(\d+)\s+(\d+)\s+125\s+365\s+(\d+)\s+([^\n]+)', text):
            coords.append({
                'x': match.group(1),
                'y': match.group(2),
                'layer': match.group(3),
                'text': match.group(4).strip()
            })
        return coords

    def parse_conditions_separately(self, text):
        """Parse les conditions if...then séparément"""
        conditions = []

        # Pattern: var op val then action
        pattern = r'(\w+)\s*([<>=!]+)\s*(-?\d+)\s+then\s+([^\n]+)'
        for match in re.finditer(pattern, text, re.IGNORECASE):
            full_text = f"{match.group(1)} {match.group(2)} {match.group(3)} then {match.group(4).strip()}"
            conditions.append({
                'var': match.group(1),
                'op': match.group(2),
                'val': match.group(3),
                'action': match.group(4).strip(),
                'text': full_text
            })

        # Pattern: commandes simples (runprj, inc_var, dec_var, etc.)
        cmd_pattern = r'\b(runprj|inc_var|dec_var|set_var|playavi|playwav|addbmp|delbmp)\s+([^\n]+)'
        for match in re.finditer(cmd_pattern, text, re.IGNORECASE):
            conditions.append({
                'text': f"{match.group(1)} {match.group(2).strip()}"
            })

        return conditions

    def parse_and_display(self):
        """Parse et affiche le contenu du VND avec structure basée sur Type 0"""
        print("=" * 80)
        print(f"VND DÉCOMPILATEUR V4 - STRUCTURE PAR TYPE 0 RECORDS")
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

        # Filtre les Type 0 records (délimiteurs)
        type0_records = [s for s in separators if s['type'] == 0]

        print(f"Total records: {len(separators)}")
        print(f"Total polygones: {len(self.polygons_map)}")
        print(f"Total Type 0 records (délimiteurs): {len(type0_records)}")
        print()

        scene_num = 0
        hotspot_num = 0
        in_scene = False

        # Parse chaque Type 0 record
        for type0_idx, type0_rec in enumerate(type0_records):
            offset = type0_rec['data_offset']
            next_offset = type0_rec['next_offset']
            length = next_offset - offset

            # Extrait texte de ce Type 0
            text = self.extract_text_at(offset, min(length, 1000))

            # Cherche BMP (= nouvelle scène)
            bmp_match = re.search(r'(euroland\\[\w]+\.bmp)', text, re.IGNORECASE)

            if bmp_match and 'rollover' not in bmp_match.group(1).lower():
                # === NOUVELLE SCÈNE ===
                scene_num += 1
                hotspot_num = 0
                in_scene = True

                print("\n" + "═" * 80)
                print(f"SCÈNE #{scene_num} @ 0x{type0_rec['pos']:08X}")
                print("═" * 80)

                # Cherche WAV
                wav_match = re.search(r'([\w\\/-]+\.wav)', text, re.IGNORECASE)
                if wav_match:
                    print(f"{wav_match.group(1)}")

                # Affiche BMP
                print(f"{bmp_match.group(1)}")
                print()

            elif in_scene:
                # === Type 0 SANS BMP = délimiteur de hotspot ===
                # Ignore les Type 0 vides (length=36, data=0)
                if length < 10:
                    continue

                # Vérifie si c'est vraiment un hotspot (contient font spec ou texte)
                font = self.parse_font_spec(text)
                text_coords = self.parse_text_coords(text)

                # Nouveau hotspot si a du contenu
                if font or text_coords or re.search(r'\b\w{3,}\b', text):
                    hotspot_num += 1
                    print(f"\n[HOTSPOT #{hotspot_num}]")

                    # Affiche font
                    if font:
                        print(f"{font['size']} {font['style']} {font['color']} {font['font']}")

                    # Affiche coords texte
                    seen_coords = set()
                    for tc in text_coords:
                        clean_text = tc['text'].replace('&', '').strip()
                        clean_text = re.sub(r'\s{3,}', ' ', clean_text)
                        clean_text = re.sub(r'^\d+\s+\d+\s+#[0-9a-fA-F]+', '', clean_text).strip()

                        coord_key = (tc['x'], tc['y'], clean_text)
                        if len(clean_text) > 2 and not re.match(r'^[\d\s#]+$', clean_text) and coord_key not in seen_coords:
                            print(f"{tc['x']} {tc['y']} 125 365 {tc['layer']} {clean_text}")
                            seen_coords.add(coord_key)

            # === Affiche tous les records NON-Type0 entre ce Type 0 et le prochain ===
            # Trouve la fin de ce segment Type 0
            if type0_idx + 1 < len(type0_records):
                segment_end = type0_records[type0_idx + 1]['pos']
            else:
                segment_end = len(self.data)

            # Parse tous les records dans ce segment
            for sep in separators:
                sep_offset = sep['data_offset']
                if offset < sep_offset < segment_end and sep['type'] != 0:
                    sep_next = sep.get('next_offset', len(self.data))
                    sep_length = sep_next - sep_offset
                    sep_text = self.extract_text_at(sep_offset, min(sep_length, 5000))

                    # Affiche vidéos
                    video_matches = re.findall(r'([\w\\/-]+\.avi)\s+(\d+)', sep_text, re.IGNORECASE)
                    seen_videos = set()
                    for vm in video_matches:
                        if vm[0] not in seen_videos and 'rollover' not in vm[0].lower():
                            print(f"{vm[0]} {vm[1]}")
                            seen_videos.add(vm[0])

                    # Affiche conditions
                    conditions = self.parse_conditions_separately(sep_text)
                    printed_conditions = set()
                    for cond in conditions:
                        clean_cond = cond['text'].strip()
                        if clean_cond not in printed_conditions and len(clean_cond) > 5:
                            print(f"{clean_cond}")
                            printed_conditions.add(clean_cond)

                    # Cherche références de navigation (5i, 51j, etc.)
                    nav_refs = re.findall(r'\b(\d+)([a-z])\b', sep_text)
                    printed_navs = set()
                    for num, opcode in nav_refs:
                        nav = f"{num}{opcode}"
                        if len(num) <= 3 and nav not in printed_navs:
                            # Ignore si c'est dans une condition ou commande déjà affichée
                            if not any(nav in cond for cond in printed_conditions):
                                print(f"{nav}")
                                printed_navs.add(nav)

                    # Affiche polygones avec coordonnées
                    for poly_offset, poly in self.polygons_map.items():
                        if sep_offset <= poly_offset < sep_next:
                            bbox = poly['bbox']
                            print(f"[Polygone {poly['count']} points]")
                            pts_str = ' '.join([f"({p[0]},{p[1]})" for p in poly['points'][:4]])
                            if len(poly['points']) > 4:
                                pts_str += " ..."
                            print(f"  Points: {pts_str}")
                            print(f"  BBox: ({bbox[0]},{bbox[1]})-({bbox[2]},{bbox[3]})")

        print("\n" + "=" * 80)
        print("FIN DU FICHIER")
        print("=" * 80)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_decompiler_v4_type0.py <file.vnd>")
        print("\nDécompile le VND avec structure basée sur Type 0 records")
        sys.exit(1)

    decompiler = VndDecompilerV4(sys.argv[1])
    decompiler.parse_and_display()

if __name__ == '__main__':
    main()
