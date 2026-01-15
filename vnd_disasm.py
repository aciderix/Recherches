#!/usr/bin/env python3
"""
VND Disassembler - Context-aware parser
Basé sur l'analyse manuelle corrigée

Gère les structures variables de la Zone 4 (données de scène)
"""

import struct
import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional


class VNDDisassembler:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.pos = 0

        # Zones identifiées
        self.header_end = 0x0086
        self.variables_end = 0x1154
        self.scene_data_start = 0x115C

        # Résultats
        self.header = {}
        self.variables = []
        self.scene_entries = []

    def read_u32(self, pos=None):
        """Lire uint32 little-endian"""
        if pos is None:
            pos = self.pos
        val = struct.unpack('<I', self.data[pos:pos+4])[0]
        return val

    def read_u16(self, pos=None):
        """Lire uint16 little-endian"""
        if pos is None:
            pos = self.pos
        val = struct.unpack('<H', self.data[pos:pos+2])[0]
        return val

    def read_string_length_prefixed(self, pos):
        """Lire string avec longueur uint32"""
        length = self.read_u32(pos)
        if length == 0 or length > 1000:
            return None, pos
        s = self.data[pos+4:pos+4+length].decode('ascii', errors='ignore')
        return s, pos + 4 + length

    def read_cstring(self, pos, max_len=500):
        """Lire string null-terminated"""
        end = self.data.find(b'\x00', pos, pos + max_len)
        if end == -1:
            return "", pos
        s = self.data[pos:end].decode('ascii', errors='ignore')
        return s, end + 1

    def find_ascii_string(self, pos, min_len=4):
        """Trouver une chaîne ASCII lisible à partir de pos"""
        s = ""
        i = pos
        while i < len(self.data) and i < pos + 200:
            b = self.data[i]
            if 32 <= b < 127:  # ASCII imprimable
                s += chr(b)
                i += 1
            elif b == 0 and len(s) >= min_len:
                # Fin de string
                return s, i + 1
            else:
                # Non-ASCII
                if len(s) >= min_len:
                    return s, i
                return None, pos

        if len(s) >= min_len:
            return s, i
        return None, pos

    def parse_header(self):
        """Parser Zone 1: Header (0x0000 - 0x0086)"""
        print("=" * 70)
        print("ZONE 1: HEADER")
        print("=" * 70)

        # Magic
        magic = self.read_u32(0x0000)
        print(f"Magic: 0x{magic:08x}")

        # Strings
        signature, _ = self.read_string_length_prefixed(0x0005)
        print(f"Signature: {signature}")

        version, _ = self.read_string_length_prefixed(0x000F)
        print(f"Version: {version}")

        region, _ = self.read_string_length_prefixed(0x001B)
        print(f"Région: {region}")

        company, _ = self.read_string_length_prefixed(0x0026)
        print(f"Éditeur: {company}")

        project_id, _ = self.read_string_length_prefixed(0x003A)
        print(f"ID Projet: {project_id}")

        # Paramètres graphiques
        width = self.read_u32(0x004E)
        height = self.read_u32(0x0052)
        bpp = self.read_u32(0x0056)
        print(f"Résolution: {width}x{height}x{bpp}")

        # DLL path
        dll_len = self.read_u32(0x006A)
        dll_path = self.data[0x006E:0x006E+dll_len].decode('ascii', errors='ignore')
        print(f"DLL: {dll_path}")

        self.header = {
            'magic': magic,
            'signature': signature,
            'version': version,
            'region': region,
            'company': company,
            'project_id': project_id,
            'width': width,
            'height': height,
            'bpp': bpp,
            'dll_path': dll_path
        }

    def parse_variables(self):
        """Parser Zone 2: Table de Variables (0x0086 - 0x1154)"""
        print("\n" + "=" * 70)
        print("ZONE 2: TABLE DE VARIABLES")
        print("=" * 70)

        pos = 0x008A  # Après le uint32 de taille
        var_num = 0

        while pos < self.variables_end:
            # Lire longueur
            length = self.read_u32(pos)

            if length == 0 or length > 100:
                break

            # Lire nom de variable
            varname = self.data[pos+4:pos+4+length].decode('ascii', errors='ignore')
            self.variables.append(varname)
            var_num += 1

            # Avancer (nom + padding de 4 bytes)
            pos += 4 + length + 4

        print(f"✓ {len(self.variables)} variables trouvées")
        print(f"\nPremières variables:")
        for i, var in enumerate(self.variables[:20]):
            print(f"  {i:3d}. {var}")
        if len(self.variables) > 20:
            print(f"  ... ({len(self.variables) - 20} autres)")

    def detect_entry_type(self, pos):
        """
        Détecter le type d'entrée de scène par analyse du contenu

        Types identifiés:
        - VIDEO: contient des chemins .avi, .bmp
        - TEXT: contient format de texte (police, couleur #RRGGBB)
        - DATA: valeurs numériques uniquement
        """
        # Lire les 200 prochains bytes
        chunk = self.data[pos:pos+200]

        # Chercher des strings
        has_avi = b'.avi' in chunk or b'.AVI' in chunk
        has_bmp = b'.bmp' in chunk or b'.BMP' in chunk
        has_wav = b'.wav' in chunk or b'.WAV' in chunk
        has_color = re.search(b'#[0-9A-Fa-f]{6}', chunk)
        has_font = b'Comic sans MS' in chunk or b'Arial' in chunk or b'Times' in chunk

        if has_avi or has_bmp or has_wav:
            return 'VIDEO'
        elif has_color or has_font:
            return 'TEXT'
        else:
            return 'DATA'

    def parse_video_entry(self, pos, entry_num):
        """Parser une entrée VIDEO/IMAGE"""
        entry = {
            'type': 'VIDEO',
            'offset': pos,
            'files': [],
            'params': []
        }

        # Lire les uint32 initiaux
        marker = self.read_u32(pos)
        pos += 4

        # Lire les paramètres (jusqu'à 10 uint32)
        for i in range(10):
            if pos + 4 > len(self.data):
                break
            val = self.read_u32(pos)

            # Si la valeur ressemble à un petit entier (< 1000), c'est un paramètre
            if val < 1000:
                entry['params'].append(val)
                pos += 4
            else:
                break

        # Chercher les chemins de fichiers
        max_search = 200
        search_end = min(pos + max_search, len(self.data))

        while pos < search_end:
            s, new_pos = self.find_ascii_string(pos, min_len=4)
            if s:
                # Vérifier si c'est un chemin de fichier
                if any(ext in s.lower() for ext in ['.avi', '.bmp', '.wav', '.jpg', '.png', '\\']):
                    entry['files'].append(s)
                    pos = new_pos
                else:
                    pos = new_pos
            else:
                pos += 1

        return entry, pos

    def parse_text_entry(self, pos, entry_num):
        """Parser une entrée TEXT (dialogue, narration)"""
        entry = {
            'type': 'TEXT',
            'offset': pos,
            'font': None,
            'font_size': None,
            'color': None,
            'position': None,
            'text': None,
            'background': None
        }

        # Lire le marqueur
        marker = self.read_u32(pos)
        pos += 4

        # Lire les premiers paramètres
        val1 = self.read_u32(pos)
        val2 = self.read_u32(pos + 4)
        entry['length_param'] = val1
        entry['font_size'] = val2
        pos += 8

        # Chercher strings dans les 400 prochains bytes
        max_search = 400
        search_end = min(pos + max_search, len(self.data))

        strings_found = []
        while pos < search_end:
            s, new_pos = self.find_ascii_string(pos, min_len=3)
            if s:
                strings_found.append(s)
                pos = new_pos

                # Analyser le contenu
                if '.avi' in s.lower() or '.bmp' in s.lower():
                    entry['background'] = s
                elif re.search(r'#[0-9A-Fa-f]{6}', s):
                    # Format texte: "18 0 #000000 Comic sans MS"
                    parts = s.split()
                    if len(parts) >= 3:
                        entry['color'] = next((p for p in parts if '#' in p), None)
                        entry['font'] = ' '.join(parts[3:]) if len(parts) > 3 else None
                elif re.match(r'\d+\s+\d+\s+\d+\s+\d+', s):
                    # Position: "57 60 125 365 0 Text..."
                    parts = s.split(None, 5)
                    if len(parts) >= 4:
                        entry['position'] = {
                            'x': int(parts[0]),
                            'y': int(parts[1]),
                            'width': int(parts[2]),
                            'height': int(parts[3])
                        }
                        if len(parts) > 5:
                            entry['text'] = parts[5]
            else:
                pos += 1

        return entry, pos

    def parse_data_entry(self, pos, entry_num):
        """Parser une entrée DATA (valeurs numériques)"""
        entry = {
            'type': 'DATA',
            'offset': pos,
            'values': []
        }

        # Lire le marqueur
        marker = self.read_u32(pos)
        pos += 4

        # Lire jusqu'à 20 uint32
        for i in range(20):
            if pos + 4 > len(self.data):
                break

            val = self.read_u32(pos)
            entry['values'].append(val)
            pos += 4

            # Arrêter si on trouve le prochain marqueur 01 00 00 00
            if pos + 4 <= len(self.data) and self.read_u32(pos) == 1:
                break

        return entry, pos

    def parse_scene_data(self):
        """Parser Zone 4: Données de Scène (0x115C - EOF)"""
        print("\n" + "=" * 70)
        print("ZONE 4: DONNÉES DE SCÈNE")
        print("=" * 70)

        pos = self.scene_data_start
        entry_num = 0

        print("\nEntrées de scène:\n")

        while pos < len(self.data) - 100:
            # Chercher le prochain marqueur 01 00 00 00
            marker_pos = self.data.find(b'\x01\x00\x00\x00', pos)

            if marker_pos == -1 or marker_pos >= len(self.data) - 100:
                break

            entry_num += 1
            pos = marker_pos

            # Détecter le type
            entry_type = self.detect_entry_type(pos)

            # Parser selon le type
            if entry_type == 'VIDEO':
                entry, new_pos = self.parse_video_entry(pos, entry_num)
            elif entry_type == 'TEXT':
                entry, new_pos = self.parse_text_entry(pos, entry_num)
            else:
                entry, new_pos = self.parse_data_entry(pos, entry_num)

            entry['entry_num'] = entry_num
            self.scene_entries.append(entry)

            # Afficher
            self.print_entry(entry)

            # Avancer
            pos = marker_pos + 4

            # Limiter pour test
            if entry_num >= 100:
                print(f"\n... (limité à 100 entrées pour test)")
                break

        print(f"\n✓ {len(self.scene_entries)} entrées de scène parsées")

    def print_entry(self, entry):
        """Afficher une entrée de scène"""
        num = entry['entry_num']
        offset = entry['offset']
        entry_type = entry['type']

        print(f"Entrée #{num:3d} @ 0x{offset:06x} [{entry_type}]")

        if entry_type == 'VIDEO':
            if entry['params']:
                print(f"  Paramètres: {entry['params']}")
            for f in entry['files']:
                print(f"  Fichier: {f}")

        elif entry_type == 'TEXT':
            if entry['background']:
                print(f"  Fond: {entry['background']}")
            if entry['font']:
                print(f"  Police: {entry['font']}, taille={entry['font_size']}")
            if entry['color']:
                print(f"  Couleur: {entry['color']}")
            if entry['position']:
                p = entry['position']
                print(f"  Position: ({p['x']}, {p['y']}) - {p['width']}x{p['height']}")
            if entry['text']:
                text_preview = entry['text'][:60] + "..." if len(entry['text']) > 60 else entry['text']
                print(f"  Texte: {text_preview}")

        elif entry_type == 'DATA':
            vals = entry['values'][:8]
            more = f" ... (+{len(entry['values']) - 8})" if len(entry['values']) > 8 else ""
            print(f"  Values: {vals}{more}")

        print()

    def export_resources(self, output_dir):
        """Exporter les ressources extraites"""
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)

        # Fichiers
        files_list = output_dir / "files.txt"
        with open(files_list, 'w') as f:
            f.write("LISTE DES FICHIERS RÉFÉRENCÉS\n")
            f.write("=" * 70 + "\n\n")

            for entry in self.scene_entries:
                if entry['type'] == 'VIDEO' and entry['files']:
                    f.write(f"Entrée #{entry['entry_num']}:\n")
                    for file in entry['files']:
                        f.write(f"  {file}\n")
                    f.write("\n")
                elif entry['type'] == 'TEXT' and entry.get('background'):
                    f.write(f"Entrée #{entry['entry_num']}:\n")
                    f.write(f"  {entry['background']}\n\n")

        # Textes
        texts_list = output_dir / "texts.txt"
        with open(texts_list, 'w') as f:
            f.write("LISTE DES TEXTES EXTRAITS\n")
            f.write("=" * 70 + "\n\n")

            for entry in self.scene_entries:
                if entry['type'] == 'TEXT' and entry.get('text'):
                    f.write(f"Entrée #{entry['entry_num']} @ 0x{entry['offset']:06x}\n")
                    if entry.get('font'):
                        f.write(f"Police: {entry['font']}, taille={entry['font_size']}\n")
                    if entry.get('color'):
                        f.write(f"Couleur: {entry['color']}\n")
                    if entry.get('position'):
                        p = entry['position']
                        f.write(f"Position: ({p['x']}, {p['y']}) - {p['width']}x{p['height']}\n")
                    f.write(f"Texte: {entry['text']}\n")
                    f.write("-" * 70 + "\n\n")

        # Variables
        vars_list = output_dir / "variables.txt"
        with open(vars_list, 'w') as f:
            f.write("LISTE DES VARIABLES DU JEU\n")
            f.write("=" * 70 + "\n\n")

            for i, var in enumerate(self.variables):
                f.write(f"{i:3d}. {var}\n")

        print(f"\n✓ Ressources exportées vers {output_dir}/")

    def run(self):
        """Exécuter le désassemblage complet"""
        print("╔" + "═" * 68 + "╗")
        print("║" + " " * 20 + "VND DISASSEMBLER" + " " * 32 + "║")
        print("╚" + "═" * 68 + "╝\n")

        print(f"Fichier: {self.filepath.name}")
        print(f"Taille: {len(self.data):,} bytes\n")

        # Parser chaque zone
        self.parse_header()
        self.parse_variables()
        self.parse_scene_data()

        # Statistiques
        print("\n" + "=" * 70)
        print("STATISTIQUES")
        print("=" * 70)

        video_count = sum(1 for e in self.scene_entries if e['type'] == 'VIDEO')
        text_count = sum(1 for e in self.scene_entries if e['type'] == 'TEXT')
        data_count = sum(1 for e in self.scene_entries if e['type'] == 'DATA')

        print(f"Variables: {len(self.variables)}")
        print(f"Entrées de scène: {len(self.scene_entries)}")
        print(f"  - VIDEO: {video_count}")
        print(f"  - TEXT: {text_count}")
        print(f"  - DATA: {data_count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: vnd_disasm.py <fichier.vnd> [output_dir]")
        sys.exit(1)

    filepath = sys.argv[1]
    disasm = VNDDisassembler(filepath)
    disasm.run()

    # Export
    output_dir = sys.argv[2] if len(sys.argv) > 2 else Path(filepath).stem + "_resources"
    disasm.export_resources(output_dir)


if __name__ == "__main__":
    main()
