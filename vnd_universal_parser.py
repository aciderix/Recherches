#!/usr/bin/env python3
"""
VND Universal Parser - Gère les structures variables entre scènes
Basé sur les découvertes:
- Scène 1: 6 slots standard (tous avec params) → InitScript → Config → Hotspots
- Scène 2: 5 slots + 1 slot sans param + 3 bytes padding + BMP string → InitScript → Config → Hotspots
"""
import struct
import sys

class VNDUniversalParser:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.offset = 0

    def read_u32(self):
        if self.offset + 4 > len(self.data):
            raise EOFError(f"Cannot read u32 at 0x{self.offset:08X}")
        val = struct.unpack('<I', self.data[self.offset:self.offset+4])[0]
        self.offset += 4
        return val

    def peek_u32(self):
        """Lit sans avancer"""
        if self.offset + 4 > len(self.data):
            return None
        return struct.unpack('<I', self.data[self.offset:self.offset+4])[0]

    def read_string(self):
        length = self.read_u32()
        if length == 0:
            return ""
        if self.offset + length > len(self.data):
            raise EOFError(f"Cannot read string of length {length}")
        string = self.data[self.offset:self.offset+length].decode('latin-1', errors='replace')
        self.offset += length
        return string

    def is_likely_string_pascal(self, offset):
        """Détecte si c'est probablement une String Pascal valide"""
        if offset + 4 > len(self.data):
            return False

        length = struct.unpack('<I', self.data[offset:offset+4])[0]

        # Length raisonnable (0-1000)
        if not (0 <= length < 1000):
            return False

        if length == 0:
            return True  # String vide est valide

        # Vérifie les caractères
        if offset + 4 + length > len(self.data):
            return False

        sample = self.data[offset+4:min(offset+4+20, offset+4+length)]
        if not sample:
            return True

        ascii_count = sum(1 for b in sample if 32 <= b < 127 or b in [0, 9, 10, 13])
        return ascii_count / len(sample) > 0.7

    def skip_to_scenes(self):
        """Trouve le début des scènes"""
        # Hardcodé pour couleurs1.vnd
        self.offset = 0x1164
        print(f"✓ Début scènes @ 0x{self.offset:08X}")

    def parse_scene_files_adaptive(self, scene_num):
        """Parse les fichiers de fond avec détection adaptative"""
        print(f"\n  [FICHIERS DE FOND]")
        files = []

        # Parse les 6 premiers slots normalement
        for slot in range(1, 7):
            slot_start = self.offset
            filename = self.read_string()

            # Après le filename, vérifie s'il y a un param
            # Si les 4 prochains bytes forment un nombre raisonnable (< 1000), c'est un param
            # Sinon, c'est peut-être une String Pascal

            peek_val = self.peek_u32()

            if slot < 6:
                # Slots 1-5 ont toujours des params
                param = self.read_u32()
                files.append({'slot': slot, 'filename': filename, 'param': param})

                if filename:
                    print(f"    Slot {slot} @ 0x{slot_start:08X}: '{filename}' param={param}")
                else:
                    print(f"    Slot {slot} @ 0x{slot_start:08X}: (vide) param={param}")
            else:
                # Slot 6: détection adaptative
                # Si peek_val est raisonnable (< 1000), c'est un param
                # Sinon, pas de param

                if peek_val is not None and peek_val < 1000:
                    param = self.read_u32()
                    files.append({'slot': slot, 'filename': filename, 'param': param})
                    print(f"    Slot {slot} @ 0x{slot_start:08X}: (vide) param={param}")
                else:
                    # Pas de param pour Slot 6
                    files.append({'slot': slot, 'filename': filename, 'param': None})
                    print(f"    Slot {slot} @ 0x{slot_start:08X}: (vide) SANS param")

        return files

    def skip_padding(self):
        """Saute les bytes de padding (0x00) jusqu'à trouver une structure valide"""
        start_offset = self.offset
        padding_count = 0

        while self.offset < len(self.data) and padding_count < 4:
            # Vérifie si c'est une String Pascal valide
            if self.is_likely_string_pascal(self.offset):
                if padding_count > 0:
                    print(f"    ⚠️  Sauté {padding_count} bytes de padding @ 0x{start_offset:08X}")
                return

            # Sinon, avance d'1 byte
            if self.data[self.offset] == 0:
                self.offset += 1
                padding_count += 1
            else:
                break

    def parse_extra_file(self):
        """Parse un fichier supplémentaire après les 6 slots (cas Scène 2)"""
        # Saute le padding éventuel
        self.skip_padding()

        # Vérifie si c'est une String Pascal avec un VRAI filename (non vide)
        if self.is_likely_string_pascal(self.offset):
            # Peek à la length
            length = self.peek_u32()

            # Si la string est non-vide (length > 0) et raisonnable (< 100)
            # alors c'est probablement un fichier supplémentaire
            if length > 0 and length < 100:
                file_start = self.offset
                filename = self.read_string()
                param = self.read_u32()

                print(f"\n  [FICHIER SUPPLÉMENTAIRE]")
                print(f"    @ 0x{file_start:08X}: '{filename}' param={param}")
                return {'filename': filename, 'param': param}

        return None

    def parse_init_script(self):
        """Parse InitScript"""
        print(f"\n  [INIT SCRIPT] @ 0x{self.offset:08X}")
        flag = self.read_u32()
        count = self.read_u32()
        print(f"    Flag={flag}, Count={count}")

        if 0 <= count < 100:
            for i in range(count):
                cmd_id = self.read_u32()
                cmd_sub = self.read_u32()
                cmd_param = self.read_string()
                if cmd_param and len(cmd_param) < 100:
                    print(f"      Cmd {cmd_id}.{cmd_sub}: '{cmd_param}'")
        else:
            print(f"    ⚠️  Count invalide")

    def parse_config(self):
        """Parse Config"""
        print(f"\n  [CONFIG] @ 0x{self.offset:08X}")
        flag = self.read_u32()
        ints = [self.read_u32() for _ in range(7)]
        print(f"    Flag={flag}, Ints={ints}")

    def parse_hotspots(self):
        """Parse Hotspots"""
        print(f"\n  [HOTSPOTS] @ 0x{self.offset:08X}")
        obj_count = self.read_u32()
        print(f"    Count={obj_count}")

        if 0 <= obj_count < 50:
            for obj_idx in range(obj_count):
                if obj_idx < 3:  # Affiche seulement les 3 premiers
                    print(f"\n    Hotspot #{obj_idx+1}:")

                cmd_count = self.read_u32()

                for cmd_idx in range(cmd_count):
                    cmd_id = self.read_u32()
                    cmd_sub = self.read_u32()
                    cmd_param = self.read_string()

                cursor_id = self.read_u32()
                point_count = self.read_u32()

                if obj_idx < 3:
                    print(f"      {cmd_count} commandes, cursor={cursor_id}, {point_count} points")

                self.offset += point_count * 8  # Skip points (x,y coords)
                extra = self.read_u32()

            if obj_count > 3:
                print(f"\n    ... et {obj_count - 3} autres hotspots")

    def parse_scene(self, scene_num):
        """Parse une scène complète"""
        scene_start = self.offset
        print(f"\n{'═'*80}")
        print(f"SCÈNE #{scene_num} @ 0x{scene_start:08X}")
        print(f"{'═'*80}")

        try:
            # 1. Fichiers de fond (6 slots)
            files = self.parse_scene_files_adaptive(scene_num)

            # 2. Fichier supplémentaire éventuel (cas Scène 2)
            extra_file = self.parse_extra_file()

            # 3. InitScript
            self.parse_init_script()

            # 4. Config
            self.parse_config()

            # 5. Hotspots
            self.parse_hotspots()

            print(f"\n  ✓ Scène #{scene_num} terminée @ 0x{self.offset:08X}")
            return True

        except Exception as e:
            print(f"\n  ❌ Erreur: {e}")
            import traceback
            traceback.print_exc()
            return False

    def parse(self, max_scenes=5):
        """Parse le fichier VND"""
        print("="*80)
        print("VND UNIVERSAL PARSER - Structure Variable")
        print(f"Fichier: {self.filepath}")
        print("="*80)

        self.skip_to_scenes()

        for scene_num in range(1, max_scenes + 1):
            if not self.parse_scene(scene_num):
                break

        print(f"\n{'='*80}")
        print(f"Position finale: 0x{self.offset:08X}")
        print("="*80)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_universal_parser.py <file.vnd> [max_scenes]")
        sys.exit(1)

    max_scenes = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    parser = VNDUniversalParser(sys.argv[1])
    parser.parse(max_scenes)

if __name__ == '__main__':
    main()
