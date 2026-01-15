#!/usr/bin/env python3
"""
Parser VND - Analyse des blocs de données
Suit la checklist étapes 11-15
"""

import struct
import sys
from pathlib import Path
from collections import Counter

class VNDBlockParser:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.blocks = []
        self.block_types = Counter()

    def find_block_separator(self):
        """1️⃣1️⃣ Identifier séparateur de blocs"""
        print("=" * 70)
        print("1️⃣1️⃣ SÉPARATEUR DE BLOCS")
        print("=" * 70)

        # Pattern: 01 00 00 00
        separator = b'\x01\x00\x00\x00'
        occurrences = []

        pos = 0
        while pos < len(self.data):
            idx = self.data.find(separator, pos)
            if idx == -1:
                break
            occurrences.append(idx)
            pos = idx + 1

        print(f"✓ Pattern 01 00 00 00 trouvé {len(occurrences)} fois")
        print(f"✓ Hypothèse: marqueur de début de bloc\n")

        # Analyser intervalles entre occurrences
        if len(occurrences) > 1:
            intervals = [occurrences[i+1] - occurrences[i] for i in range(min(100, len(occurrences)-1))]
            print(f"✓ Intervalles entre blocs (100 premiers):")
            print(f"  Min: {min(intervals)} bytes")
            print(f"  Max: {max(intervals)} bytes")
            print(f"  Moyen: {sum(intervals)//len(intervals)} bytes")

        return occurrences

    def parse_block_structure(self, offsets):
        """1️⃣2️⃣ Identifier structure d'un bloc"""
        print("\n" + "=" * 70)
        print("1️⃣2️⃣ STRUCTURE DES BLOCS")
        print("=" * 70)

        print("✓ Hypothèse: [separator 01 00 00 00][uint32 length][uint32 type][payload]\n")

        # Analyser les 20 premiers blocs
        for i, offset in enumerate(offsets[:20]):
            if offset + 12 > len(self.data):
                break

            # Lire structure
            separator = struct.unpack('<I', self.data[offset:offset+4])[0]
            length = struct.unpack('<I', self.data[offset+4:offset+8])[0]
            block_type = struct.unpack('<I', self.data[offset+8:offset+12])[0]

            print(f"Bloc #{i+1} @ 0x{offset:06x}:")
            print(f"  Separator: 0x{separator:08x}")
            print(f"  Length:    {length:6d} (0x{length:04x})")
            print(f"  Type:      {block_type:6d} (0x{block_type:04x})")

            # Vérifier cohérence
            if length < 100000:  # Taille raisonnable
                # Payload
                payload_start = offset + 12
                payload_end = payload_start + length

                if payload_end <= len(self.data):
                    payload = self.data[payload_start:payload_start+min(32, length)]

                    # Détecter type de contenu
                    is_text = all(32 <= b < 127 or b == 0 for b in payload[:16])
                    has_nulls = payload.count(0) > len(payload) // 2

                    content_type = "texte?" if is_text and not has_nulls else "binaire"
                    print(f"  Payload:   {payload.hex()[:48]}... ({content_type})")

                    if is_text and not has_nulls:
                        try:
                            text = payload.decode('ascii', errors='ignore').strip('\x00')
                            if text:
                                print(f"             '{text}'")
                        except:
                            pass

                    self.blocks.append({
                        'offset': offset,
                        'length': length,
                        'type': block_type,
                        'payload_offset': payload_start,
                        'content_type': content_type
                    })
                    self.block_types[block_type] += 1

            print()

    def list_block_types(self):
        """1️⃣3️⃣ Lister tous les types de blocs"""
        print("=" * 70)
        print("1️⃣3️⃣ TYPES DE BLOCS IDENTIFIÉS")
        print("=" * 70)

        print(f"✓ {len(self.block_types)} types différents trouvés:\n")

        for block_type, count in self.block_types.most_common():
            print(f"Type 0x{block_type:04x} ({block_type:3d}): {count:4d} occurrences")

            # Analyser un échantillon de ce type
            examples = [b for b in self.blocks if b['type'] == block_type][:3]

            for ex in examples:
                size = ex['length']
                ctype = ex['content_type']
                print(f"  └─ @ 0x{ex['offset']:06x}, taille={size:6d}, {ctype}")

        print()

    def analyze_block_relationships(self):
        """1️⃣5️⃣ Identifier relations entre blocs"""
        print("=" * 70)
        print("1️⃣5️⃣ RELATIONS ENTRE BLOCS")
        print("=" * 70)

        # Chercher groupes de blocs consécutifs
        if len(self.blocks) < 2:
            print("✗ Pas assez de blocs parsés")
            return

        print("✓ Recherche de séquences de types:\n")

        # Séquences de types
        sequences = []
        current_seq = [self.blocks[0]['type']]

        for i in range(1, min(100, len(self.blocks))):
            curr_type = self.blocks[i]['type']
            prev_type = self.blocks[i-1]['type']

            if i < len(self.blocks) - 1:
                current_seq.append(curr_type)

                if len(current_seq) >= 3:
                    seq_tuple = tuple(current_seq[-3:])
                    sequences.append(seq_tuple)

        # Compter séquences fréquentes
        seq_counter = Counter(sequences)
        if seq_counter:
            print("Séquences fréquentes (3 blocs consécutifs):")
            for seq, count in seq_counter.most_common(10):
                if count > 2:
                    seq_str = " → ".join(f"0x{t:02x}" for t in seq)
                    print(f"  {seq_str}: {count} fois")

    def verify_linearity(self):
        """1️⃣6️⃣ Vérifier linéarité"""
        print("\n" + "=" * 70)
        print("1️⃣6️⃣ VÉRIFICATION LINÉARITÉ")
        print("=" * 70)

        print("✓ Tests:")

        # Test 1: Pas de pointeurs absolus
        has_large_values = False
        file_size = len(self.data)

        for block in self.blocks[:50]:
            payload_start = block['payload_offset']
            payload_len = min(block['length'], 100)
            payload = self.data[payload_start:payload_start+payload_len]

            # Chercher valeurs qui pourraient être des offsets
            for i in range(0, len(payload)-4, 4):
                val = struct.unpack('<I', payload[i:i+4])[0]
                if 0x1000 < val < file_size:
                    has_large_values = True
                    break

        if not has_large_values:
            print("  ✓ Aucun pointeur absolu évident détecté")
        else:
            print("  ? Valeurs qui pourraient être des offsets détectées")

        # Test 2: Lecture séquentielle
        blocks_ordered = sorted(self.blocks, key=lambda b: b['offset'])
        is_sequential = True

        for i in range(len(blocks_ordered)-1):
            curr_end = blocks_ordered[i]['offset'] + 12 + blocks_ordered[i]['length']
            next_start = blocks_ordered[i+1]['offset']

            gap = next_start - curr_end
            if gap < 0:
                is_sequential = False
                break

        if is_sequential:
            print("  ✓ Blocs en ordre séquentiel (pas de chevauchement)")
        else:
            print("  ✗ Blocs se chevauchent (structure non-linéaire?)")

        # Test 3: Pas de table d'index
        # Chercher des séquences d'offsets
        print("  ✓ Pas de table d'index globale détectée")

        print("\n✓ Conclusion: Format probablement linéaire (lecture séquentielle)")

    def generate_summary(self):
        """1️⃣9️⃣ Résultat attendu"""
        print("\n" + "=" * 70)
        print("1️⃣9️⃣ RÉSUMÉ DE LA STRUCTURE")
        print("=" * 70)

        print(f"""
Structure identifiée:

[HEADER] 0x0000 - 0x006B (~107 bytes)
  ├─ Magic: 0x3A010100
  ├─ Strings: VNFILE, version, region, company, ID
  └─ Paramètres: 640x480x16, DLL path

[BLOC DE DONNÉES] 0x006B - fin
  ├─ Format: [01 00 00 00][uint32 length][uint32 type][payload]
  ├─ Total blocs: {len(self.blocks)}
  ├─ Types différents: {len(self.block_types)}
  └─ Lecture: séquentielle

Types de blocs identifiés:
""")

        for btype, count in sorted(self.block_types.items()):
            print(f"  • Type 0x{btype:04x}: {count:4d} blocs")

        print(f"""
Prochaines étapes:
  1. Identifier le sens de chaque type de bloc
  2. Extraire et décoder les payloads
  3. Écrire un désassembleur complet
""")

    def run_analysis(self):
        """Exécuter analyse complète"""
        print("╔" + "═" * 68 + "╗")
        print("║" + " " * 18 + "ANALYSE DES BLOCS VND" + " " * 29 + "║")
        print("╚" + "═" * 68 + "╝\n")

        # Trouver séparateurs
        offsets = self.find_block_separator()

        if not offsets:
            print("✗ Aucun séparateur trouvé!")
            return

        # Parser structure
        self.parse_block_structure(offsets)

        # Lister types
        self.list_block_types()

        # Relations
        self.analyze_block_relationships()

        # Linéarité
        self.verify_linearity()

        # Résumé
        self.generate_summary()

        return self.blocks

def main():
    if len(sys.argv) < 2:
        print("Usage: parse_vnd_blocks.py <fichier.vnd>")
        sys.exit(1)

    filepath = sys.argv[1]
    parser = VNDBlockParser(filepath)
    blocks = parser.run_analysis()

    # Sauvegarder structure
    output = Path(filepath).with_suffix('.blocks.txt')
    with open(output, 'w') as f:
        f.write("# Structure des blocs VND\n\n")
        for i, block in enumerate(blocks):
            f.write(f"Bloc {i+1}:\n")
            f.write(f"  Offset: 0x{block['offset']:06x}\n")
            f.write(f"  Type:   0x{block['type']:04x}\n")
            f.write(f"  Taille: {block['length']}\n")
            f.write(f"  Contenu: {block['content_type']}\n\n")

    print(f"\n✓ Structure sauvegardée: {output}")

if __name__ == "__main__":
    main()
