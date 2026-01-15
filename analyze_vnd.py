#!/usr/bin/env python3
"""
Analyseur de fichier VND - Suivant la checklist méthodologique
"""

import struct
import sys
from pathlib import Path

class VNDAnalyzer:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.pos = 0
        self.findings = []

    def log(self, message, level=0):
        indent = "  " * level
        print(f"{indent}{message}")
        self.findings.append((level, message))

    def read_u32(self, offset=None):
        """Lire uint32 little-endian"""
        if offset is None:
            offset = self.pos
        return struct.unpack('<I', self.data[offset:offset+4])[0]

    def read_bytes(self, length, offset=None):
        """Lire N bytes"""
        if offset is None:
            offset = self.pos
        return self.data[offset:offset+length]

    def hex_dump(self, offset, length=16):
        """Dump hex d'une zone"""
        data = self.data[offset:offset+length]
        hex_str = ' '.join(f'{b:02x}' for b in data)
        ascii_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in data)
        return f"{hex_str:48s} {ascii_str}"

    def analyze_step1_file_start(self):
        """1️⃣ Identifier le début du fichier"""
        self.log("=" * 60)
        self.log("1️⃣ DÉBUT DU FICHIER")
        self.log("=" * 60)

        self.log(f"✓ Fichier: {self.filepath}")
        self.log(f"✓ Taille: {len(self.data):,} bytes ({len(self.data)/1024:.1f} KB)")
        self.log(f"✓ Offset 0x0000:")

        # Afficher premiers 128 octets
        for i in range(0, min(128, len(self.data)), 16):
            self.log(f"0x{i:04x}: {self.hex_dump(i)}", 1)

        # Rechercher signatures ASCII
        self.log("\n✓ Chaînes ASCII visibles dans les 256 premiers octets:")
        visible_strings = []
        current = ""
        for i in range(min(256, len(self.data))):
            b = self.data[i]
            if 32 <= b < 127:
                current += chr(b)
            else:
                if len(current) >= 4:
                    visible_strings.append((i-len(current), current))
                current = ""

        for offset, s in visible_strings:
            self.log(f"0x{offset:04x}: '{s}'", 1)

        return visible_strings

    def analyze_step2_signature(self, strings):
        """2️⃣ Identifier la signature du format"""
        self.log("\n" + "=" * 60)
        self.log("2️⃣ SIGNATURE DU FORMAT")
        self.log("=" * 60)

        # Chercher "VNFILE"
        vnfile_found = False
        for offset, s in strings:
            if 'VNFILE' in s or 'VNF' in s:
                self.log(f"✓ Signature trouvée: '{s}' à offset 0x{offset:04x}")
                vnfile_found = True

                # Regarder avant pour trouver la longueur
                if offset >= 4:
                    before = self.data[offset-4:offset]
                    len_before = struct.unpack('<I', before)[0]
                    if len_before == len(s):
                        self.log(f"  → Précédé d'un uint32 = {len_before} (longueur!)", 1)
                        return offset - 4

        if not vnfile_found:
            self.log("✗ Signature 'VNFILE' non trouvée")

        return None

    def analyze_step3_endianness(self):
        """3️⃣ Déterminer l'endianness"""
        self.log("\n" + "=" * 60)
        self.log("3️⃣ ENDIANNESS")
        self.log("=" * 60)

        # Chercher des valeurs connues (dimensions écran)
        candidates = []
        for i in range(0, min(200, len(self.data)-4), 4):
            val_le = struct.unpack('<I', self.data[i:i+4])[0]
            val_be = struct.unpack('>I', self.data[i:i+4])[0]

            # Dimensions d'écran typiques
            if 320 <= val_le <= 3840 and i+4 < len(self.data):
                next_le = struct.unpack('<I', self.data[i+4:i+8])[0]
                if 200 <= next_le <= 2160:
                    candidates.append(('little', i, val_le, next_le))

            if 320 <= val_be <= 3840 and i+4 < len(self.data):
                next_be = struct.unpack('>I', self.data[i+4:i+8])[0]
                if 200 <= next_be <= 2160:
                    candidates.append(('big', i, val_be, next_be))

        if candidates:
            self.log("✓ Valeurs plausibles de dimensions trouvées:")
            for endian, offset, w, h in candidates:
                self.log(f"0x{offset:04x}: {w}x{h} ({endian}-endian)", 1)
                if endian == 'little' and w in [640, 800, 1024] and h in [480, 600, 768]:
                    self.log(f"  → Très probable! Résolution standard", 2)
                    return 'little', offset

        self.log("✓ Test par défaut: little-endian (standard Windows/Intel)")
        return 'little', None

    def analyze_step4_strings(self, sig_offset):
        """4️⃣ Identifier les chaînes de caractères"""
        self.log("\n" + "=" * 60)
        self.log("4️⃣ CHAÎNES DE CARACTÈRES")
        self.log("=" * 60)

        if sig_offset is None:
            self.log("✗ Pas de point de départ (signature non trouvée)")
            sig_offset = 0x05  # Fallback

        self.log(f"✓ Parsing depuis 0x{sig_offset:04x}")
        self.log(f"✓ Modèle testé: [uint32 length][ASCII string]")

        pos = sig_offset
        strings = []

        for i in range(20):  # Max 20 strings
            if pos + 4 > len(self.data):
                break

            length = self.read_u32(pos)

            # Vérifier si c'est une longueur plausible
            if length == 0 or length > 1000:
                self.log(f"\n0x{pos:04x}: {length} ← Fin des strings (valeur implausible)")
                break

            pos += 4
            string_data = self.read_bytes(length, pos)

            # Tenter décodage
            try:
                string = string_data.decode('ascii')
                self.log(f"0x{pos-4:04x}: len={length:3d} | '{string}'", 1)
                strings.append((pos-4, length, string))
                pos += length

                # Chercher padding/null
                padding = 0
                while pos < len(self.data) and self.data[pos] == 0:
                    padding += 1
                    pos += 1

                if padding > 0:
                    self.log(f"  + {padding} bytes null padding", 2)

            except UnicodeDecodeError:
                self.log(f"0x{pos-4:04x}: len={length:3d} | [données binaires] {string_data.hex()[:40]}", 1)
                break

        self.log(f"\n✓ {len(strings)} chaînes trouvées")
        self.log(f"✓ Fin de la zone strings: 0x{pos:04x}")

        return strings, pos

    def analyze_step6_params(self, pos):
        """6️⃣ Identifier les paramètres globaux"""
        self.log("\n" + "=" * 60)
        self.log("6️⃣ PARAMÈTRES GLOBAUX")
        self.log("=" * 60)

        self.log(f"✓ Analyse depuis 0x{pos:04x}")

        # Lire 20 valeurs uint32
        params = []
        for i in range(20):
            if pos + 4 > len(self.data):
                break
            val = self.read_u32(pos)
            params.append((pos, val))

            # Interpréter les valeurs connues
            interpretation = ""
            if 320 <= val <= 3840:
                interpretation = "largeur?"
            elif 200 <= val <= 2160:
                interpretation = "hauteur?"
            elif val in [1, 2, 4, 8, 16, 24, 32]:
                interpretation = "bits/flags?"
            elif val == 0:
                interpretation = "null/padding"

            self.log(f"0x{pos:04x}: {val:10d} = 0x{val:08x}  {interpretation}", 1)
            pos += 4

        return params, pos

    def analyze_step10_patterns(self, pos):
        """🔟 Rechercher patterns répétés"""
        self.log("\n" + "=" * 60)
        self.log("🔟 PATTERNS RÉPÉTÉS")
        self.log("=" * 60)

        # Chercher séquences répétées
        self.log(f"✓ Scan depuis 0x{pos:04x}")

        # Pattern commun: 01 00 00 00 (marqueur de bloc)
        pattern = b'\x01\x00\x00\x00'
        occurrences = []

        search_pos = pos
        while search_pos < len(self.data):
            idx = self.data.find(pattern, search_pos)
            if idx == -1:
                break
            occurrences.append(idx)
            search_pos = idx + 1

        if occurrences:
            self.log(f"✓ Pattern 01 00 00 00 trouvé {len(occurrences)} fois:")
            for i, offset in enumerate(occurrences[:10]):  # Max 10
                self.log(f"  {i+1}. 0x{offset:04x}", 1)
                # Afficher contexte
                ctx = self.data[offset:offset+20]
                self.log(f"     {ctx.hex()}", 2)

        return occurrences

    def run_full_analysis(self):
        """Exécuter analyse complète selon checklist"""
        self.log("╔" + "═" * 58 + "╗")
        self.log("║" + " " * 10 + "ANALYSE FICHIER VND - CHECKLIST" + " " * 16 + "║")
        self.log("╚" + "═" * 58 + "╝")
        self.log("")

        # 1. Début du fichier
        strings = self.analyze_step1_file_start()

        # 2. Signature
        sig_offset = self.analyze_step2_signature(strings)

        # 3. Endianness
        endian, dim_offset = self.analyze_step3_endianness()

        # 4. Chaînes
        parsed_strings, end_strings = self.analyze_step4_strings(sig_offset)

        # 6. Paramètres
        params, end_params = self.analyze_step6_params(end_strings)

        # 10. Patterns
        patterns = self.analyze_step10_patterns(end_params)

        # Résumé
        self.log("\n" + "=" * 60)
        self.log("📊 RÉSUMÉ")
        self.log("=" * 60)
        self.log(f"✓ Taille fichier: {len(self.data):,} bytes")
        self.log(f"✓ Signature: {'VNFILE trouvée' if sig_offset else 'Non trouvée'}")
        self.log(f"✓ Endianness: {endian}")
        self.log(f"✓ Strings trouvées: {len(parsed_strings)}")
        self.log(f"✓ Zone header: 0x0000 - 0x{end_strings:04x}")
        self.log(f"✓ Zone params: 0x{end_strings:04x} - 0x{end_params:04x}")
        self.log(f"✓ Patterns répétés: {len(patterns)} occurrences")

        return {
            'strings': parsed_strings,
            'params': params,
            'patterns': patterns,
            'endian': endian
        }

def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_vnd.py <fichier.vnd>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not Path(filepath).exists():
        print(f"Erreur: fichier '{filepath}' introuvable")
        sys.exit(1)

    analyzer = VNDAnalyzer(filepath)
    results = analyzer.run_full_analysis()

    # Sauvegarder rapport
    report_path = Path(filepath).with_suffix('.analysis.txt')
    with open(report_path, 'w') as f:
        for level, msg in analyzer.findings:
            f.write("  " * level + msg + "\n")

    print(f"\n✓ Rapport sauvegardé: {report_path}")

if __name__ == "__main__":
    main()
