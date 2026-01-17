#!/usr/bin/env python3
"""
VND Complete Parser - Basé sur le format découvert
Extrait scènes, hotspots, polygones, navigation
"""
import struct
import sys
import re
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

@dataclass
class Polygon:
    """Polygone cliquable"""
    points: List[Tuple[int, int]]
    offset: int = 0

    @property
    def bbox(self) -> Tuple[int, int, int, int]:
        """Bounding box (x1, y1, x2, y2)"""
        if not self.points:
            return (0, 0, 0, 0)
        xs = [p[0] for p in self.points]
        ys = [p[1] for p in self.points]
        return (min(xs), min(ys), max(xs), max(ys))

@dataclass
class Hotspot:
    """Hotspot avec texte et zone cliquable"""
    id: int
    text: str
    text_x: int  # Position d'affichage du texte
    text_y: int
    layer: int = 0
    polygon: Optional[Polygon] = None
    opcode: Optional[str] = None
    offset: int = 0

@dataclass
class Scene:
    """Scène avec fond et hotspots"""
    id: int
    background: Optional[str] = None
    audio: Optional[str] = None
    hotspots: List[Hotspot] = field(default_factory=list)
    offset: int = 0

class VndCompleteParser:
    """Parser complet pour fichiers VND"""

    # Types de records
    TYPE_SCENE = 0  # Type 0 - Scène
    TYPE_HOTSPOT_TEXT = 38  # Type 38 (0x26) - Texte hotspot
    TYPE_FONT = 39  # Type 39 (0x27) - Police
    TYPE_POLYGON = 105  # Type 105 (0x69) - Polygone

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.text_content = self.data.decode('latin-1', errors='replace')

    def find_all_separators(self):
        """Trouve tous les séparateurs de records"""
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

    def find_polygons(self) -> List[Tuple[int, Polygon]]:
        """Trouve tous les polygones (Type 105)"""
        polygons = []
        i = 0

        while i < len(self.data) - 8:
            # Cherche signature Type 105
            if i + 4 <= len(self.data):
                record_type = struct.unpack('<I', self.data[i:i+4])[0]

                if record_type == self.TYPE_POLYGON:
                    # Lit nombre de points
                    if i + 8 <= len(self.data):
                        count = struct.unpack('<I', self.data[i+4:i+8])[0]

                        if 3 <= count <= 50:  # Validation
                            points = []
                            valid = True

                            for j in range(count):
                                offset = i + 8 + j * 8
                                if offset + 8 > len(self.data):
                                    valid = False
                                    break

                                # SIGNED integers!
                                x = struct.unpack('<i', self.data[offset:offset+4])[0]
                                y = struct.unpack('<i', self.data[offset+4:offset+8])[0]

                                # Validation coordonnées écran
                                if not (-200 <= x <= 2000 and -200 <= y <= 2000):
                                    valid = False
                                    break

                                points.append((x, y))

                            if valid and points:
                                poly = Polygon(points=points, offset=i)
                                polygons.append((i, poly))
                                i += 8 + count * 8  # Skip données polygone
                                continue

            i += 1

        return polygons

    def find_hotspot_texts(self) -> List[Tuple[int, str, int, int, int]]:
        """Trouve les textes de hotspots (pattern: X Y 125 365 layer text)"""
        hotspots = []

        # Pattern: X Y 125 365 layer text
        pattern = r'(\d{1,3})\s+(\d{1,3})\s+125\s+365\s+(\d+)\s+([^\x00\r\n]{2,})'

        for match in re.finditer(pattern, self.text_content):
            offset = match.start()
            x = int(match.group(1))
            y = int(match.group(2))
            layer = int(match.group(3))
            text = match.group(4).strip()

            # Validation
            if 0 <= x <= 2000 and 0 <= y <= 2000 and len(text) > 1:
                hotspots.append((offset, text, x, y, layer))

        return hotspots

    def find_backgrounds(self) -> List[Tuple[int, str]]:
        """Trouve les images de fond"""
        backgrounds = []
        pattern = r'(?<![\\/:])(\w+\.bmp)(?!\w)'

        for match in re.finditer(pattern, self.text_content, re.IGNORECASE):
            name = match.group(1).lower()
            # Filtre rollovers
            if 'roll' not in name and 'over' not in name:
                backgrounds.append((match.start(), match.group(1)))

        return backgrounds

    def find_audio_files(self) -> List[Tuple[int, str]]:
        """Trouve les fichiers audio"""
        audio = []
        pattern = r'([\w/\\]+\.wav)'

        for match in re.finditer(pattern, self.text_content, re.IGNORECASE):
            audio.append((match.start(), match.group(1)))

        return audio

    def find_opcodes(self) -> List[Tuple[int, str]]:
        """Trouve les opcodes de navigation (ex: 39i, 13d)"""
        opcodes = []
        pattern = r'(?<!\d)(\d{1,3}[a-z])(?!\w)'

        for match in re.finditer(pattern, self.text_content):
            opcodes.append((match.start(), match.group(1)))

        return opcodes

    def parse(self):
        """Parse complet du fichier VND"""
        print("=" * 80)
        print(f"PARSING VND: {self.filepath}")
        print("=" * 80)
        print()

        # Extrait toutes les données
        separators = self.find_all_separators()
        polygons = self.find_polygons()
        hotspot_texts = self.find_hotspot_texts()
        backgrounds = self.find_backgrounds()
        audio_files = self.find_audio_files()
        opcodes = self.find_opcodes()

        print(f"Records totaux: {len(separators)}")
        print(f"Polygones (Type 105): {len(polygons)}")
        print(f"Hotspot texts: {len(hotspot_texts)}")
        print(f"Backgrounds: {len(backgrounds)}")
        print(f"Audio files: {len(audio_files)}")
        print(f"Opcodes: {len(opcodes)}")
        print()

        # Compte par type
        by_type = {}
        for sep in separators:
            t = sep['type']
            by_type[t] = by_type.get(t, 0) + 1

        print(f"Type 0 (scènes): {by_type.get(0, 0)}")
        print(f"Type 2: {by_type.get(2, 0)}")
        print(f"Type 38 (hotspot text): {by_type.get(38, 0)}")
        print(f"Type 105 (polygones): {by_type.get(105, 0)}")
        print()

        # Construit scènes
        scenes = []
        scene_id = 0

        # Utilise backgrounds comme marqueurs de scènes
        backgrounds_sorted = sorted(backgrounds, key=lambda x: x[0])

        for bg_offset, bg_name in backgrounds_sorted:
            scene_id += 1
            scene = Scene(
                id=scene_id,
                background=bg_name,
                offset=bg_offset
            )
            scenes.append(scene)

        if not scenes:
            print("⚠️  Aucune scène détectée")
            return

        print(f"Scènes construites: {len(scenes)}")
        print()

        # Associe hotspots aux scènes
        hotspot_id = 0

        for text_offset, text, x, y, layer in hotspot_texts:
            # Trouve scène parente
            scene = None
            for s in reversed(scenes):
                if s.offset < text_offset:
                    scene = s
                    break

            if not scene:
                scene = scenes[0]

            hotspot_id += 1
            hotspot = Hotspot(
                id=hotspot_id,
                text=text,
                text_x=x,
                text_y=y,
                layer=layer,
                offset=text_offset
            )

            # Cherche polygone associé (après le texte, dans limite raisonnable)
            search_limit = text_offset + 1000
            for poly_offset, polygon in polygons:
                if text_offset < poly_offset < search_limit:
                    hotspot.polygon = polygon
                    break

            # Cherche opcode associé
            for opcode_offset, opcode in opcodes:
                if text_offset - 100 < opcode_offset < search_limit:
                    hotspot.opcode = opcode
                    break

            scene.hotspots.append(hotspot)

        # Affiche résultats
        print("=" * 80)
        print("SCÈNES ET HOTSPOTS")
        print("=" * 80)
        print()

        for scene in scenes[:5]:  # Limite à 5 scènes
            print(f"{'─' * 80}")
            print(f"SCÈNE #{scene.id}: {scene.background}")
            print(f"{'─' * 80}")
            print(f"  Offset: 0x{scene.offset:08X}")
            print(f"  Hotspots: {len(scene.hotspots)}")
            print()

            for hotspot in scene.hotspots[:5]:  # Max 5 hotspots par scène
                print(f"  Hotspot #{hotspot.id}: \"{hotspot.text}\"")
                print(f"    Position texte: ({hotspot.text_x}, {hotspot.text_y}), layer={hotspot.layer}")

                if hotspot.polygon:
                    bbox = hotspot.polygon.bbox
                    print(f"    Polygone: {len(hotspot.polygon.points)} points")
                    print(f"      Points: {hotspot.polygon.points[:3]}...")
                    print(f"      BBox: ({bbox[0]}, {bbox[1]}) → ({bbox[2]}, {bbox[3]})")

                if hotspot.opcode:
                    print(f"    Opcode: {hotspot.opcode}")

                print()

            if len(scene.hotspots) > 5:
                print(f"  ... et {len(scene.hotspots) - 5} autres hotspots")
                print()

        if len(scenes) > 5:
            print(f"\n... et {len(scenes) - 5} autres scènes")

        return scenes

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vnd_complete_parser.py <file.vnd>")
        sys.exit(1)

    parser = VndCompleteParser(sys.argv[1])
    scenes = parser.parse()

if __name__ == '__main__':
    main()
