#!/usr/bin/env python3
"""
Analyse le gap entre Scène 2 et Scène 3
0x1AC5 (fin Scène 2) → 0x1E4B (début Scène 3 estimé)
"""
import struct

data = open('Vnd-vnp/couleurs1.vnd', 'rb').read()

def read_u32(offset):
    return struct.unpack('<I', data[offset:offset+4])[0]

def read_string(offset):
    length = read_u32(offset)
    if length == 0:
        return "", offset + 4
    string = data[offset+4:offset+4+length].decode('latin-1', errors='replace')
    return string, offset + 4 + length

print("="*80)
print("ANALYSE DU GAP ENTRE SCÈNE 2 ET SCÈNE 3")
print("="*80)

# On sait que le parser dit que Scène 2 se termine à 0x1AC5
# Mais Scène 3 commence vers 0x1E4B (avant "music.wav" à 0x1E5C)
gap_start = 0x1AC5
gap_end = 0x1E4B

print(f"\nGap: 0x{gap_start:08X} → 0x{gap_end:08X}")
print(f"Taille: 0x{gap_end - gap_start:08X} = {gap_end - gap_start} bytes")

# Cherchons des patterns dans le gap
print(f"\nRecherche de strings Pascal dans le gap:")
offset = gap_start
strings_found = []

while offset < gap_end - 4:
    length = read_u32(offset)

    # Si c'est une longueur raisonnable
    if 0 < length < 100:
        # Essayons de lire la string
        if offset + 4 + length <= len(data):
            string = data[offset+4:offset+4+length].decode('latin-1', errors='replace')

            # Si c'est principalement ASCII
            ascii_count = sum(1 for c in string if 32 <= ord(c) < 127 or c in ['\t', '\n'])
            if ascii_count / len(string) > 0.7:
                strings_found.append((offset, length, string))
                print(f"  @ 0x{offset:08X}: (len={length}) '{string}'")

    offset += 1

print(f"\nTotal: {len(strings_found)} strings trouvées")

# Analysons la structure autour des strings trouvées
if strings_found:
    print(f"\n{'='*80}")
    print(f"ANALYSE STRUCTURE AUTOUR DES STRINGS")
    print(f"{'='*80}")

    for i, (str_offset, length, string) in enumerate(strings_found[:5]):  # Premières 5
        print(f"\nString #{i+1} @ 0x{str_offset:08X}: '{string[:50]}'")

        # Regarde 12 bytes avant
        before_offset = max(gap_start, str_offset - 12)
        print(f"  12 bytes avant (@ 0x{before_offset:08X}):")
        for j in range(before_offset, str_offset, 4):
            val = read_u32(j)
            print(f"    0x{j:08X}: {val:10d} (0x{val:08X})")

        # Regarde 8 bytes après
        after_offset = str_offset + 4 + length
        print(f"  8 bytes après (@ 0x{after_offset:08X}):")
        for j in range(after_offset, min(after_offset + 8, len(data)), 4):
            val = read_u32(j)
            print(f"    0x{j:08X}: {val:10d} (0x{val:08X})")

# Cherchons des patterns de commandes (CmdID + SubType + String)
print(f"\n{'='*80}")
print(f"HYPOTHÈSE: C'est une continuation de Scène 2 (Hotspots ou autre)")
print(f"{'='*80}")

print(f"\nEssayons de parser comme des Hotspots à partir de 0x1AC5:")
offset = 0x1AC5

# Les 16 premiers bytes
print(f"\n16 premiers bytes @ 0x{offset:08X}:")
for i in range(4):
    val = read_u32(offset + i*4)
    print(f"  +{i*4:02d}: {val:10d} (0x{val:08X})")

# Peut-être que c'est InitScript/Config/Hotspots d'UNE AUTRE scène?
# Ou peut-être que c'est des données globales?

print(f"\nOu peut-être que tout le gap fait partie de Scène 2?")
print(f"Cherchons où Scène 2 se termine VRAIMENT en trouvant le pattern de début de Scène 3")

# Scène 3 devrait commencer par 6 slots, dont le 2e est "music.wav"
# Cherchons "music.wav" = 0x1E5C
# 4 bytes avant: length = 9
# Donc Slot 2 commence à 0x1E58

# Avant Slot 2, il y a Slot 1 (probablement vide)
# Si Slot 1 = string vide (4) + param (4) = 8 bytes
# Alors Slot 1 commence à 0x1E58 - 8 = 0x1E50

print(f"\n{'='*80}")
print(f"HYPOTHÈSE: Scène 3 commence à 0x1E50 (avant music.wav)")
print(f"{'='*80}")

scene3_start = 0x1E50
print(f"\nSlots de Scène 3 à partir de 0x{scene3_start:08X}:")

offset = scene3_start
for slot in range(1, 7):
    string, offset = read_string(offset)
    param = read_u32(offset)
    offset += 4

    if string:
        print(f"  Slot {slot}: '{string}' param={param}")
    else:
        print(f"  Slot {slot}: (vide) param={param}")

print(f"\nAprès les 6 slots, offset = 0x{offset:08X}")

# Donc Scène 2 se termine à 0x1E50
print(f"\nSi Scène 3 commence à 0x{scene3_start:08X},")
print(f"alors Scène 2 se termine à 0x{scene3_start:08X}")
print(f"Gap réel depuis la fin calculée (0x1AC5): 0x{scene3_start - 0x1AC5:08X} = {scene3_start - 0x1AC5} bytes")

print(f"\nCes {scene3_start - 0x1AC5} bytes (0x1AC5-0x1E50) font partie de Scène 2!")
print(f"Probablement des Hotspots non comptés ou une autre structure.")
