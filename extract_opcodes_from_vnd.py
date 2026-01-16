#!/usr/bin/env python3
"""
Extracteur d'opcodes depuis fichier VND
Selon la doc: les opcodes sont des lettres simples 'a'-'z' qui suivent des nombres
"""
import sys
import struct
from collections import Counter

def extract_opcodes(vnd_file):
    """Extrait tous les opcodes (lettres 'a'-'z') du fichier VND"""

    with open(vnd_file, 'rb') as f:
        data = f.read()

    opcodes = []
    opcode_contexts = []

    # Cherche tous les bytes qui sont des lettres 'a'-'z' (0x61-0x7A)
    for i in range(len(data)):
        byte = data[i]

        # Check si c'est une lettre minuscule
        if 0x61 <= byte <= 0x7A:  # 'a' to 'z'
            char = chr(byte)

            # Regarde le contexte: 10 bytes avant et après
            context_start = max(0, i - 10)
            context_end = min(len(data), i + 10)
            context_before = data[context_start:i]
            context_after = data[i+1:context_end]

            # Check si le byte précédent est un chiffre ou espace
            # (indicateur qu'on a un vrai opcode)
            prev_byte = data[i-1] if i > 0 else 0
            is_likely_opcode = False

            # Heuristiques pour détecter les vrais opcodes:
            # 1. Précédé d'un chiffre ASCII ou espace
            if (0x30 <= prev_byte <= 0x39) or prev_byte == 0x20:
                is_likely_opcode = True
            # 2. Ou précédé de null bytes (fin de string C)
            elif prev_byte == 0x00:
                is_likely_opcode = True

            if is_likely_opcode:
                opcodes.append((i, char))

                # Extrait le contexte lisible
                try:
                    before_str = context_before[-10:].decode('ascii', errors='replace')
                    after_str = context_after[:10].decode('ascii', errors='replace')
                except:
                    before_str = context_before[-10:].hex()
                    after_str = context_after[:10].hex()

                opcode_contexts.append({
                    'offset': i,
                    'opcode': char,
                    'opcode_index': ord(char) - ord('a') + 1,
                    'before': before_str,
                    'after': after_str
                })

    return opcodes, opcode_contexts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_opcodes_from_vnd.py <fichier.vnd>")
        sys.exit(1)

    vnd_file = sys.argv[1]

    print("="*80)
    print(f"EXTRACTION DES OPCODES: {vnd_file}")
    print("="*80)
    print()

    opcodes, contexts = extract_opcodes(vnd_file)

    # Statistiques
    opcode_counts = Counter([op[1] for op in opcodes])

    print(f"✓ Trouvé {len(opcodes)} opcodes potentiels")
    print()

    print("TOP 20 OPCODES LES PLUS FRÉQUENTS:")
    print("-" * 80)
    for opcode, count in opcode_counts.most_common(20):
        index = ord(opcode) - ord('a') + 1
        print(f"  '{opcode}' (index {index:2d}) : {count:4d} occurrences")
    print()

    # Affiche les 50 premiers contextes
    print("PREMIERS 50 OPCODES AVEC CONTEXTE:")
    print("-" * 80)
    for ctx in contexts[:50]:
        print(f"@ 0x{ctx['offset']:06X}  '{ctx['opcode']}' (idx {ctx['opcode_index']:2d})")
        print(f"  Avant : ...{ctx['before']}")
        print(f"  Après : {ctx['after']}...")
        print()

if __name__ == '__main__':
    main()
