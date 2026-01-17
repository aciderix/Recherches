#!/usr/bin/env python3
"""
VND Sequential Parser - Vraie Structure
Suit la structure séquentielle révélée: 6 fichiers + InitScript + Config + Hotspots
"""
import struct
import sys

class VNDSequentialParser:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.offset = 0

    def read_u32(self):
        """Lit un unsigned int 32 bits little-endian"""
        if self.offset + 4 > len(self.data):
            raise EOFError(f"Cannot read u32 at offset 0x{self.offset:08X}")
        val = struct.unpack('<I', self.data[self.offset:self.offset+4])[0]
        self.offset += 4
        return val

    def read_i32(self):
        """Lit un signed int 32 bits little-endian"""
        if self.offset + 4 > len(self.data):
            raise EOFError(f"Cannot read i32 at offset 0x{self.offset:08X}")
        val = struct.unpack('<i', self.data[self.offset:self.offset+4])[0]
        self.offset += 4
        return val

    def read_pascal_string(self):
        """
        Lit une String Pascal VND format:
        [LENGTH:4][CHARACTERS:LENGTH]
        PAS de null terminator!
        """
        start_offset = self.offset
        length = self.read_u32()

        if length == 0:
            return ""

        if self.offset + length > len(self.data):
            raise EOFError(f"Cannot read string of length {length} at offset 0x{start_offset:08X}")

        # Lit les caractères
        string_bytes = self.data[self.offset:self.offset+length]
        self.offset += length

        try:
            return string_bytes.decode('latin-1')
        except:
            return string_bytes.decode('latin-1', errors='replace')

    def skip_header(self):
        """Saute le header VND et trouve le début des scènes"""
        # Cherche "VNFILE"
        vnfile_pos = self.data.find(b'VNFILE')
        if vnfile_pos == -1:
            print("⚠️  Signature VNFILE non trouvée")
            return

        print(f"✓ Signature VNFILE @ 0x{vnfile_pos:08X}")

        # Pour l'instant, cherche la première string Pascal après le header
        # En général les scènes commencent après la table de variables
        # Essayons de trouver le premier pattern: 00 00 00 00 00 00 00 00 (string vide) ou longueur + "music.wav"

        # Stratégie: cherche "music.wav" qui est souvent dans la scène 1
        music_pos = self.data.find(b'music.wav')
        if music_pos != -1:
            # Recule de 4 octets pour trouver la longueur
            potential_length_pos = music_pos - 4
            if potential_length_pos >= 0:
                length = struct.unpack('<I', self.data[potential_length_pos:potential_length_pos+4])[0]
                if length == 9:  # "music.wav" = 9 caractères
                    # Recule encore pour trouver le début de la paire (string vide + param)
                    # Slot 1 vide = 4 octets (length=0) + 4 octets (param)
                    scene_start = potential_length_pos - 8
                    print(f"✓ Début estimé des scènes @ 0x{scene_start:08X}")
                    self.offset = scene_start
                    return

        # Fallback: commence après la position VNFILE + 300 octets (approximation)
        self.offset = vnfile_pos + 300
        print(f"⚠️  Utilise fallback @ 0x{self.offset:08X}")

    def parse_scene_name(self):
        """Parse le nom optionnel de la scène (avant les 6 fichiers)"""
        name_offset = self.offset
        scene_name = self.read_pascal_string()

        if scene_name:
            print(f"\n  [NOM SCÈNE] @ 0x{name_offset:08X}: '{scene_name}'")

        return scene_name

    def parse_scene_files(self, scene_num):
        """Parse les 6 fichiers de fond d'une scène"""
        print(f"\n  [6 FICHIERS DE FOND]")
        files = []

        for slot in range(1, 7):
            file_offset = self.offset
            filename = self.read_pascal_string()
            param = self.read_u32()

            files.append({'slot': slot, 'filename': filename, 'param': param})

            if filename:
                print(f"    Slot {slot} @ 0x{file_offset:08X}: '{filename}' (param={param})")
            else:
                print(f"    Slot {slot} @ 0x{file_offset:08X}: (vide)")

        return files

    def parse_init_script(self):
        """Parse l'InitScript d'une scène"""
        print(f"\n  [INIT SCRIPT] @ 0x{self.offset:08X}")
        flag = self.read_u32()
        count = self.read_u32()

        print(f"    Flag: {flag}, Commands: {count}")

        # Skip commands for now (structure inconnue)
        for i in range(count):
            cmd_id = self.read_u32()
            cmd_param = self.read_pascal_string()
            print(f"      Cmd {i}: ID={cmd_id}, Param='{cmd_param[:50]}'")

    def parse_config(self):
        """Parse la Config d'une scène"""
        print(f"\n  [CONFIG] @ 0x{self.offset:08X}")
        flag = self.read_u32()
        ints = [self.read_u32() for _ in range(7)]  # 7 Ints au lieu de 5

        print(f"    Flag: {flag}, Ints: {ints}")

    def parse_hotspots(self, scene_num):
        """Parse les hotspots/objets d'une scène"""
        obj_count_offset = self.offset
        obj_count = self.read_u32()

        print(f"\n  [HOTSPOTS] @ 0x{obj_count_offset:08X}")
        print(f"    Nombre d'objets: {obj_count}")

        for obj_idx in range(obj_count):
            print(f"\n    ═══ HOTSPOT #{obj_idx+1} ═══")

            # Script de l'objet
            cmd_count_offset = self.offset
            cmd_count = self.read_u32()
            print(f"      [SCRIPT] @ 0x{cmd_count_offset:08X}: {cmd_count} commandes")

            for cmd_idx in range(cmd_count):
                cmd_id = self.read_u32()
                cmd_subtype = self.read_u32()  # Champ supplémentaire entre CmdID et String
                cmd_param = self.read_pascal_string()

                # Affiche seulement les commandes intéressantes
                if cmd_param and len(cmd_param) < 100:
                    print(f"        • Cmd {cmd_id}.{cmd_subtype}: '{cmd_param}'")

            # Géométrie de l'objet
            geom_offset = self.offset
            cursor_id = self.read_u32()
            point_count = self.read_u32()

            print(f"      [GÉOMÉTRIE] @ 0x{geom_offset:08X}: CursorID={cursor_id}, {point_count} points")

            points = []
            for p_idx in range(point_count):
                x = self.read_i32()
                y = self.read_i32()
                points.append((x, y))

            if points:
                print(f"        Points: {points[:4]}" + (" ..." if len(points) > 4 else ""))

            extra_flag = self.read_u32()
            print(f"        ExtraFlag: {extra_flag}")

    def parse_scene(self, scene_num):
        """Parse une scène complète"""
        scene_offset = self.offset
        print(f"\n{'═'*80}")
        print(f"SCÈNE #{scene_num} @ 0x{scene_offset:08X}")
        print(f"{'═'*80}")

        try:
            # Pas de champ nom - directement les 6 fichiers
            files = self.parse_scene_files(scene_num)

            # 2. InitScript
            self.parse_init_script()

            # 3. Config
            self.parse_config()

            # 4. Hotspots
            self.parse_hotspots(scene_num)

            return True

        except EOFError as e:
            print(f"\n⚠️  EOF atteint: {e}")
            return False
        except Exception as e:
            print(f"\n❌ Erreur parsing scène {scene_num}: {e}")
            import traceback
            traceback.print_exc()
            return False

    def parse(self, max_scenes=5):
        """Parse le fichier VND"""
        print("=" * 80)
        print(f"VND SEQUENTIAL PARSER - Structure Séquentielle Vraie")
        print(f"Fichier: {self.filepath}")
        print("=" * 80)

        # Skip header
        self.skip_header()

        # Parse les scènes
        scene_num = 1
        while scene_num <= max_scenes:
            if not self.parse_scene(scene_num):
                break
            scene_num += 1

        print(f"\n{'='*80}")
        print(f"Parsé {scene_num - 1} scènes")
        print(f"Position finale: 0x{self.offset:08X} / 0x{len(self.data):08X}")
        print("=" * 80)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_sequential_parser.py <file.vnd> [max_scenes]")
        sys.exit(1)

    max_scenes = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    parser = VNDSequentialParser(sys.argv[1])
    parser.parse(max_scenes)

if __name__ == '__main__':
    main()
