#!/usr/bin/env python3
"""
Extracteur d'opcodes depuis fichier VND - VERSION 2
Selon la doc: les opcodes sont des lettres 'a'-'z' qui suivent IMMÉDIATEMENT des chiffres
Exemple: "54h" "5i" "123d"
"""
import sys
import re
from collections import Counter

def extract_opcodes_v2(vnd_file):
    """Extrait les opcodes qui suivent des nombres"""

    with open(vnd_file, 'rb') as f:
        data = f.read()

    # Convertit en string (on ignore les bytes non-ASCII)
    text = data.decode('latin-1')  # latin-1 pour avoir tous les bytes

    opcodes = []
    opcode_contexts = []

    # Regex: cherche nombre suivi d'une lettre minuscule
    # Pattern: [0-9]+[a-z]
    pattern = r'(\d+)([a-z])'

    for match in re.finditer(pattern, text):
        number = match.group(1)
        opcode = match.group(2)
        offset = match.start()

        # Contexte
        context_start = max(0, offset - 30)
        context_end = min(len(text), offset + 30)
        context = text[context_start:context_end]

        # Check si c'est vraiment un opcode ou juste du texte
        # Heuristique: après l'opcode, on doit avoir:
        # - un espace
        # - un chiffre (paramètre suivant)
        # - un null byte
        # - fin de string
        next_char_idx = match.end()
        if next_char_idx < len(text):
            next_char = text[next_char_idx]

            # Si le char suivant est une lettre, c'est probablement du texte (comme "bibliobis.avi 1")
            if next_char.isalpha():
                continue

        opcode_index = ord(opcode) - ord('a') + 1

        opcodes.append((offset, number, opcode, opcode_index))
        opcode_contexts.append({
            'offset': offset,
            'number': number,
            'opcode': opcode,
            'opcode_index': opcode_index,
            'context': context.replace('\x00', '\\0').replace('\n', '\\n')
        })

    return opcodes, opcode_contexts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_opcodes_from_vnd_v2.py <fichier.vnd>")
        sys.exit(1)

    vnd_file = sys.argv[1]

    print("="*80)
    print(f"EXTRACTION DES OPCODES V2: {vnd_file}")
    print("="*80)
    print()

    opcodes, contexts = extract_opcodes_v2(vnd_file)

    # Statistiques
    opcode_counts = Counter([op[2] for op in opcodes])

    print(f"✓ Trouvé {len(opcodes)} séquences nombre+lettre")
    print()

    print("TOP 20 OPCODES LES PLUS FRÉQUENTS:")
    print("-" * 80)
    for opcode, count in opcode_counts.most_common(20):
        index = ord(opcode) - ord('a') + 1
        print(f"  '{opcode}' (index {index:2d}) : {count:4d} occurrences")
    print()

    # Affiche les 100 premiers contextes
    print("PREMIERS 100 OPCODES AVEC CONTEXTE:")
    print("-" * 80)
    for ctx in contexts[:100]:
        print(f"@ 0x{ctx['offset']:06X}  {ctx['number']}{ctx['opcode']} (opcode idx {ctx['opcode_index']:2d})")
        print(f"  Context: ...{ctx['context']}...")
        print()

if __name__ == '__main__':
    main()
