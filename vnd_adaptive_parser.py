#!/usr/bin/env python3
"""
VND Adaptive Parser - Détecte dynamiquement la structure variable
"""
import struct
import sys

class VNDAdaptiveParser:
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
        """Lit sans avancer l'offset"""
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

    def is_likely_string_length(self, val):
        """Détermine si une valeur est probablement une longueur de string"""
        # Une longueur raisonnable est entre 1 et 1000
        # Et le contenu suivant doit être des caractères ASCII
        if not (0 < val < 1000):
            return False

        # Vérifie que les premiers caractères sont ASCII imprimables
        if self.offset + val > len(self.data):
            return False

        sample = self.data[self.offset:min(self.offset+20, self.offset+val)]
        ascii_count = sum(1 for b in sample if 32 <= b < 127 or b in [0])
        return ascii_count / len(sample) > 0.7

    def skip_header(self):
        """Trouve le début des scènes"""
        # Pour l'instant, utilise un offset fixe validé manuellement
        # TODO: Détecter automatiquement en cherchant la fin de la table de variables
        self.offset = 0x1164
        print(f"✓ Début scènes @ 0x{self.offset:08X}")

    def parse_scene(self, scene_num):
        """Parse une scène de manière adaptative"""
        scene_start = self.offset
        print(f"\n{'═'*80}")
        print(f"SCÈNE #{scene_num} @ 0x{scene_start:08X}")
        print(f"{'═'*80}")

        try:
            # Phase 1: Parse exactement 6 slots
            print(f"\n  [6 FICHIERS/SLOTS]")

            for slot_num in range(1, 7):
                slot_offset = self.offset

                # Lit une string
                filename = self.read_string()

                # Lit le param (toujours Int32)
                param = self.read_u32()

                repr_fn = repr(filename) if filename else "(vide)"
                print(f"    Slot {slot_num} @ 0x{slot_offset:08X}: {repr_fn:<30} param={param}")

            # Phase 2: InitScript
            print(f"\n  [INIT SCRIPT] @ 0x{self.offset:08X}")
            flag = self.read_u32()
            count = self.read_u32()
            print(f"    Flag={flag}, Count={count}")

            if 0 <= count < 100:
                for i in range(count):
                    cmd_id = self.read_u32()
                    cmd_sub = self.read_u32()
                    cmd_param = self.read_string()
                    if len(cmd_param) < 100:
                        print(f"      Cmd {cmd_id}.{cmd_sub}: '{cmd_param}'")
            else:
                print(f"    ⚠️ Count invalide, skip")

            # Phase 3: Config
            print(f"\n  [CONFIG] @ 0x{self.offset:08X}")
            flag = self.read_u32()
            ints = [self.read_u32() for _ in range(7)]
            print(f"    Flag={flag}, Ints={ints}")

            # Phase 4: Hotspots
            print(f"\n  [HOTSPOTS] @ 0x{self.offset:08X}")
            obj_count = self.read_u32()
            print(f"    Count={obj_count}")

            if 0 <= obj_count < 50:
                for obj_idx in range(obj_count):  # Parse TOUS les hotspots
                    cmd_count = self.read_u32()

                    # N'affiche que les 3 premiers pour ne pas surcharger
                    if obj_idx < 3:
                        print(f"\n    Hotspot #{obj_idx+1}: {cmd_count} commandes")

                    for cmd_idx in range(cmd_count):
                        cmd_id = self.read_u32()
                        cmd_sub = self.read_u32()
                        cmd_param = self.read_string()

                    cursor_id = self.read_u32()
                    point_count = self.read_u32()

                    if obj_idx < 3:
                        print(f"      Géométrie: cursor={cursor_id}, {point_count} points")

                    self.offset += point_count * 8  # Skip points
                    extra = self.read_u32()

                if obj_count > 3:
                    print(f"    ... et {obj_count - 3} autres hotspots")

            print(f"\n  Fin scène #{scene_num} @ 0x{self.offset:08X}")
            return True

        except Exception as e:
            print(f"\n❌ Erreur: {e}")
            import traceback
            traceback.print_exc()
            return False

    def parse(self, max_scenes=3):
        print("="*80)
        print(f"VND ADAPTIVE PARSER")
        print(f"Fichier: {self.filepath}")
        print("="*80)

        self.skip_header()

        for scene_num in range(1, max_scenes + 1):
            if not self.parse_scene(scene_num):
                break

        print(f"\n{'='*80}")
        print(f"Position finale: 0x{self.offset:08X}")
        print("="*80)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_adaptive_parser.py <file.vnd> [max_scenes]")
        sys.exit(1)

    max_scenes = int(sys.argv[2]) if len(sys.argv) > 2 else 3

    parser = VNDAdaptiveParser(sys.argv[1])
    parser.parse(max_scenes)

if __name__ == '__main__':
    main()
