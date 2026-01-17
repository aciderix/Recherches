#!/usr/bin/env python3
"""
Vérifie si Scène 2 a vraiment 0 hotspots ou si le count est mal lu
"""
import struct

data = open('Vnd-vnp/couleurs1.vnd', 'rb').read()

# Scène 2 Hotspots devrait être à 0x1AC1
offset = 0x1AC1

print("="*80)
print("VÉRIFICATION HOTSPOTS SCÈNE 2 @ 0x1AC1")
print("="*80)

# Affiche les 100 prochains bytes
print("\nHexdump:")
for i in range(0, 100, 16):
    addr = offset + i
    hex_part = ' '.join([f'{data[addr+j]:02X}' for j in range(min(16, 100-i))])
    ascii_part = ''.join([chr(data[addr+j]) if 32 <= data[addr+j] < 127 else '.' for j in range(min(16, 100-i))])
    print(f"  0x{addr:08X}  {hex_part:<48}  {ascii_part}")

# Lit le count
obj_count = struct.unpack('<I', data[offset:offset+4])[0]
print(f"\nObjCount @ 0x{offset:08X}: {obj_count}")

if obj_count == 0:
    print(f"  → Aucun hotspot selon le count")
    print(f"  → Scène 2 devrait se terminer @ 0x{offset+4:08X}")

    print(f"\nMais regardons ce qu'il y a après 0x{offset+4:08X}:")

    # Essayons de lire comme si c'était une Scène 3
    next_offset = offset + 4
    print(f"\nTest: Est-ce le début de Scène 3?")

    # Slot 1
    length = struct.unpack('<I', data[next_offset:next_offset+4])[0]
    print(f"  Slot 1 length @ 0x{next_offset:08X}: {length}")

    if length == 0:
        print(f"    → String vide")
        next_offset += 4
        param = struct.unpack('<I', data[next_offset:next_offset+4])[0]
        print(f"    → Param: {param}")
        next_offset += 4
    elif 0 < length < 100:
        print(f"    → String de {length} caractères")
        string = data[next_offset+4:next_offset+4+length].decode('latin-1', errors='replace')
        print(f"    → String: '{string}'")
        next_offset += 4 + length
        param = struct.unpack('<I', data[next_offset:next_offset+4])[0]
        print(f"    → Param: {param}")
    else:
        print(f"    → Length invalide! Pas le début d'une scène")

else:
    print(f"  → {obj_count} hotspots")
    print(f"  → Parser devrait continuer")

# Cherchons où Scène 2 se termine vraiment
print(f"\n{'='*80}")
print("RECHERCHE: Où est le vrai début de Scène 3?")
print("="*80)

# On sait que Scène 3 devrait avoir "euroland\banque.bmp" selon l'utilisateur
bmp3 = b'euroland\\banque.bmp'
pos = data.find(bmp3, 0x1AC0)

if pos != -1:
    print(f"\nTrouvé 'euroland\\banque.bmp' @ 0x{pos:08X}")

    # La length devrait être 4 bytes avant
    length_pos = pos - 4
    length = struct.unpack('<I', data[length_pos:length_pos+4])[0]
    print(f"  Length @ 0x{length_pos:08X}: {length} (attendu: {len(bmp3)})")

    if length == len(bmp3):
        print(f"    ✓ Correct!")
        print(f"\n  Donc Scène 3 commence probablement @ 0x{length_pos:08X}")

        # Reculons pour trouver les 5 premiers slots
        print(f"\n  En reculant pour trouver Slot 1 de Scène 3...")

        # Si c'est comme les autres scènes, il y a 6 slots avant le BMP
        # Essayons de trouver où commence Slot 1

        # Hypothèse: le BMP est dans un des 6 slots
        # Cherchons 100 bytes avant
        search_start = length_pos - 100

        print(f"\n  Hexdump de 0x{search_start:08X} à 0x{pos+20:08X}:")
        for i in range(0, 150, 16):
            addr = search_start + i
            hex_part = ' '.join([f'{data[addr+j]:02X}' for j in range(16)])
            ascii_part = ''.join([chr(data[addr+j]) if 32 <= data[addr+j] < 127 else '.' for j in range(16)])
            print(f"  0x{addr:08X}  {hex_part:<48}  {ascii_part}")
