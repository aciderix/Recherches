#!/usr/bin/env python3
"""
Analyse critique: Les slots vides ont-ils un param Int32 ou non?
Compare Scene 1 Slot 5/6 (vides) avec Scene 2 Slot 6 (vide)
"""
import struct

data = open('Vnd-vnp/couleurs1.vnd', 'rb').read()

def read_u32(offset):
    return struct.unpack('<I', data[offset:offset+4])[0], offset + 4

def read_string(offset):
    length, offset = read_u32(offset)
    if length == 0:
        return "", offset
    string = data[offset:offset+length].decode('latin-1', errors='replace')
    return string, offset + length

def hexdump(offset, size):
    """Affiche hexdump à un offset donné"""
    for i in range(0, size, 16):
        addr = offset + i
        hex_part = ' '.join([f'{data[addr+j]:02X}' for j in range(min(16, size-i))])
        ascii_part = ''.join([chr(data[addr+j]) if 32 <= data[addr+j] < 127 else '.' for j in range(min(16, size-i))])
        print(f"  0x{addr:08X}  {hex_part:<48}  {ascii_part}")

print("="*80)
print("ANALYSE SCÈNE 1 - Slots 5 et 6 (tous deux vides)")
print("="*80)

offset = 0x1164

# Parse Slots 1-4 pour arriver aux slots vides
print("\nParsing Slots 1-4 (pour arriver aux slots vides):")
for slot in range(1, 5):
    slot_start = offset
    filename, offset = read_string(offset)
    param, offset = read_u32(offset)
    if filename:
        print(f"  Slot {slot} @ 0x{slot_start:08X}: '{filename}' param={param}")
    else:
        print(f"  Slot {slot} @ 0x{slot_start:08X}: (vide) param={param}")

print(f"\nAvant Slot 5: offset = 0x{offset:08X}")
print("Hexdump des 32 prochains octets:")
hexdump(offset, 32)

# Slot 5 (vide)
print("\n" + "-"*80)
print("SLOT 5 (VIDE):")
print("-"*80)
slot5_start = offset
length, offset = read_u32(offset)
print(f"  @ 0x{slot5_start:08X}: String Length = {length}")

if length == 0:
    print(f"  String vide détectée")
    print(f"  Offset actuel (après length): 0x{offset:08X}")

    # Lisons les 4 prochains octets
    next_4_bytes, temp_offset = read_u32(offset)
    print(f"  Prochains 4 octets @ 0x{offset:08X}: {next_4_bytes} (0x{next_4_bytes:08X})")

    # Est-ce un param raisonnable (0 ou petit nombre)?
    if next_4_bytes == 0 or next_4_bytes < 10:
        print(f"  ✓ Semble être un param (valeur={next_4_bytes})")
        offset = temp_offset
    else:
        print(f"  ✗ NE semble PAS être un param (trop grand ou étrange)")
        print(f"  Peut-être que c'est le début de Slot 6?")

# Slot 6 (vide aussi)
print("\n" + "-"*80)
print("SLOT 6 (VIDE):")
print("-"*80)
slot6_start = offset
length, offset = read_u32(offset)
print(f"  @ 0x{slot6_start:08X}: String Length = {length}")

if length == 0:
    print(f"  String vide détectée")
    print(f"  Offset actuel (après length): 0x{offset:08X}")

    # Lisons les 4 prochains octets
    next_4_bytes, temp_offset = read_u32(offset)
    print(f"  Prochains 4 octets @ 0x{offset:08X}: {next_4_bytes} (0x{next_4_bytes:08X})")

    # Vérifie si c'est InitScript flag
    # InitScript devrait commencer par Flag + Count
    print(f"\n  Hypothèse 1: Ces 4 octets sont le param de Slot 6")
    print(f"    → Param = {next_4_bytes}")
    print(f"    → InitScript devrait commencer @ 0x{temp_offset:08X}")

    print(f"\n  Hypothèse 2: Ces 4 octets sont InitScript Flag")
    print(f"    → InitScript Flag = {next_4_bytes}")
    print(f"    → InitScript commencerait @ 0x{offset:08X}")

# Vérifie où devrait être InitScript
print("\n" + "="*80)
print("VÉRIFICATION: Où est InitScript?")
print("="*80)

# On sait que Scene 1 parse correctement avec vnd_adaptive_parser
# et que InitScript @ 0x11AE avec Flag=0, Count=0
expected_initscript = 0x11AE
print(f"\nSelon vnd_adaptive_parser.py qui marche:")
print(f"  InitScript est @ 0x{expected_initscript:08X}")
print(f"\n  Flag @ 0x{expected_initscript:08X}: {read_u32(expected_initscript)[0]}")
print(f"  Count @ 0x{expected_initscript+4:08X}: {read_u32(expected_initscript+4)[0]}")

print(f"\nOffset actuel après Slot 6 string: 0x{offset:08X}")
print(f"Différence avec InitScript attendu: 0x{expected_initscript - offset:08X} octets")

if expected_initscript - offset == 4:
    print(f"\n✓ CONCLUSION: Il y a exactement 4 octets de différence")
    print(f"  → Slot 6 (vide) a bien un param Int32!")
    param_value = read_u32(offset)[0]
    print(f"  → Param de Slot 6 = {param_value}")
elif expected_initscript == offset:
    print(f"\n✓ CONCLUSION: Pas de différence")
    print(f"  → Slot 6 (vide) N'A PAS de param Int32!")
    print(f"  → InitScript commence directement")

print("\n" + "="*80)
print("ANALYSE SCÈNE 2 - Slot 6 (vide)")
print("="*80)

# Scene 2 commence à 0x1A31
offset = 0x1A31

# Parse Slots 1-5
print("\nParsing Slots 1-5:")
for slot in range(1, 6):
    slot_start = offset
    filename, offset = read_string(offset)
    param, offset = read_u32(offset)
    if filename:
        print(f"  Slot {slot} @ 0x{slot_start:08X}: '{filename}' param={param}")
    else:
        print(f"  Slot {slot} @ 0x{slot_start:08X}: (vide) param={param}")

# Slot 6
print("\n" + "-"*80)
print("SLOT 6 (VIDE):")
print("-"*80)
slot6_start = offset
print(f"@ 0x{slot6_start:08X}:")
hexdump(offset, 40)

length, offset = read_u32(offset)
print(f"\n  String Length @ 0x{slot6_start:08X}: {length}")

if length == 0:
    print(f"  String vide")
    print(f"\n  Prochains 4 octets @ 0x{offset:08X}:")
    next_4_bytes, temp_offset = read_u32(offset)
    print(f"    Valeur: {next_4_bytes} (0x{next_4_bytes:08X})")

    # C'est 0x1B000000 = 452984832
    if next_4_bytes == 0x1B:
        print(f"\n  ✓ C'est 0x1B = 27 decimal")
        print(f"  → Ceci est la LENGTH de 'euroland\\bureaubanquier.bmp' (27 caractères)!")
        print(f"\n  DONC: Slot 6 (vide) N'A PAS de param!")
        print(f"  → La string suivante commence directement @ 0x{offset:08X}")

        # Vérifie
        bmp_filename, _ = read_string(offset)
        print(f"\n  Vérification - String suivante: '{bmp_filename}'")

print("\n" + "="*80)
print("CONCLUSION FINALE")
print("="*80)
print("\nScène 1: Slots vides (5 et 6) ont des params")
print("Scène 2: Slot 6 (vide) N'A PAS de param")
print("\n⚠️  LA STRUCTURE VARIE ENTRE LES SCÈNES!")
print("\nPossibilités:")
print("  1. Scène 1 a toujours 6 × (String + Int32)")
print("  2. Scène 2 a une structure différente (peut-être 1 String + 5 Strings sans params?)")
print("  3. Ou bien Scène 2 a un nombre différent de slots?")
