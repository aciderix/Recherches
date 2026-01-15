#!/usr/bin/env python3
"""
Extracteur VND - Extrait tous les blocs dans des fichiers séparés
"""

import struct
import sys
from pathlib import Path

def extract_blocks(filepath):
    """Extraire tous les blocs d'un fichier VND"""

    with open(filepath, 'rb') as f:
        data = f.read()

    output_dir = Path(filepath).parent / f"{Path(filepath).stem}_blocks"
    output_dir.mkdir(exist_ok=True)

    print(f"Extraction des blocs vers: {output_dir}")
    print("=" * 70)

    # Trouver tous les séparateurs
    separator = b'\x01\x00\x00\x00'
    offsets = []
    pos = 0
    while pos < len(data):
        idx = data.find(separator, pos)
        if idx == -1:
            break
        offsets.append(idx)
        pos = idx + 1

    print(f"✓ {len(offsets)} blocs trouvés\n")

    # Extraire chaque bloc
    blocks_extracted = 0

    for i, offset in enumerate(offsets):
        if offset + 12 > len(data):
            continue

        # Lire structure
        length = struct.unpack('<I', data[offset+4:offset+8])[0]
        block_type = struct.unpack('<I', data[offset+8:offset+12])[0]

        # Vérifier taille raisonnable
        if length > 100000 or length == 0:
            continue

        payload_start = offset + 12
        payload_end = payload_start + length

        if payload_end > len(data):
            continue

        payload = data[payload_start:payload_end]

        # Détecter type de contenu
        is_text = False
        if length < 1000:
            is_text = all(32 <= b < 127 or b in [0, 9, 10, 13] for b in payload[:min(100, length)])

        # Nom de fichier
        ext = "txt" if is_text else "bin"
        filename = f"block_{i:04d}_type{block_type:04x}_len{length:06d}.{ext}"

        # Sauvegarder
        output_path = output_dir / filename
        with open(output_path, 'wb') as f:
            f.write(payload)

        # Afficher info
        content_preview = ""
        if is_text:
            try:
                text = payload.decode('ascii', errors='ignore').strip('\x00')[:50]
                content_preview = f" '{text}...'"
            except:
                pass
        else:
            content_preview = f" {payload[:16].hex()}..."

        print(f"Block {i:4d} @ 0x{offset:06x}: type=0x{block_type:04x}, len={length:6d}{content_preview}")
        print(f"  → {filename}")

        blocks_extracted += 1

        if blocks_extracted >= 100:  # Limiter pour test
            print(f"\n✓ Limite de 100 blocs atteinte (pour test)")
            break

    print(f"\n✓ {blocks_extracted} blocs extraits vers {output_dir}")

    # Créer index
    index_file = output_dir / "INDEX.txt"
    with open(index_file, 'w') as f:
        f.write("INDEX DES BLOCS EXTRAITS\n")
        f.write("=" * 70 + "\n\n")

        for i, offset in enumerate(offsets[:blocks_extracted]):
            if offset + 12 > len(data):
                continue

            length = struct.unpack('<I', data[offset+4:offset+8])[0]
            block_type = struct.unpack('<I', data[offset+8:offset+12])[0]

            if length > 100000 or length == 0:
                continue

            filename = f"block_{i:04d}_type{block_type:04x}_len{length:06d}"
            f.write(f"Bloc {i:4d}:\n")
            f.write(f"  Offset:   0x{offset:06x}\n")
            f.write(f"  Type:     0x{block_type:04x} ({block_type})\n")
            f.write(f"  Longueur: {length} bytes\n")
            f.write(f"  Fichier:  {filename}.*\n\n")

    print(f"✓ Index créé: {index_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: extract_vnd_blocks.py <fichier.vnd>")
        sys.exit(1)

    extract_blocks(sys.argv[1])

if __name__ == "__main__":
    main()
