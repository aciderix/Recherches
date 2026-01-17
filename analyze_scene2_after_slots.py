#!/usr/bin/env python3
"""
Analyse: Que se passe-t-il après les 6 slots de Scène 2?
Est-ce que ça saute InitScript/Config ou est-ce une structure différente?
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
    for i in range(0, size, 16):
        addr = offset + i
        hex_part = ' '.join([f'{data[addr+j]:02X}' for j in range(min(16, size-i))])
        ascii_part = ''.join([chr(data[addr+j]) if 32 <= data[addr+j] < 127 else '.' for j in range(min(16, size-i))])
        print(f"  0x{addr:08X}  {hex_part:<48}  {ascii_part}")

print("="*80)
print("SCÈNE 2 - ANALYSE APRÈS LES 6 SLOTS")
print("="*80)

# On sait que Scène 2 commence à 0x1A31
offset = 0x1A31

# Parse les 6 slots SANS assumer que tous ont des params
print("\nParsing des 6 PREMIERS strings (sans assumption sur params):")
for slot in range(1, 7):
    slot_start = offset
    filename, offset = read_string(offset)

    if filename:
        print(f"  Slot {slot} @ 0x{slot_start:08X}: '{filename}'")
    else:
        print(f"  Slot {slot} @ 0x{slot_start:08X}: (vide)")

print(f"\nAprès les 6 strings, offset = 0x{offset:08X}")
print("\nHexdump des 100 prochains octets:")
hexdump(offset, 100)

# Maintenant, essayons de parser avec l'hypothèse "TOUS ont des params sauf le dernier"
print("\n" + "="*80)
print("HYPOTHÈSE 1: Les 5 premiers slots ont params, le 6e n'en a pas")
print("="*80)

offset = 0x1A31
for slot in range(1, 6):  # Slots 1-5 avec params
    filename, offset = read_string(offset)
    param, offset = read_u32(offset)
    if filename:
        print(f"  Slot {slot}: '{filename}' param={param}")
    else:
        print(f"  Slot {slot}: (vide) param={param}")

# Slot 6 SANS param
slot6_start = offset
filename, offset = read_string(offset)
print(f"  Slot 6: (vide, SANS param)")

print(f"\nAprès Slot 6: offset = 0x{offset:08X}")

# Maintenant qu'est-ce qu'il y a?
print("\n  Prochaine structure:")

# Est-ce InitScript?
print("\n  Test InitScript:")
flag, temp = read_u32(offset)
count, temp = read_u32(temp)
print(f"    Flag={flag}, Count={count}")
if 0 <= count < 50:
    print(f"    ✓ Pourrait être InitScript!")
else:
    print(f"    ✗ Pas InitScript (count invalide)")

# Ou est-ce une String Pascal?
print("\n  Test String Pascal:")
filename, temp = read_string(offset)
param, temp = read_u32(temp)
print(f"    String: '{filename}'")
print(f"    Param: {param}")
if filename:
    print(f"    ✓ C'est une String Pascal!")

# Continuons avec String Pascal
print("\n" + "="*80)
print("SI c'est une String Pascal, que suit-elle?")
print("="*80)

offset = temp
print(f"\nOffset après '{filename}' + param: 0x{offset:08X}")

# Y a-t-il InitScript maintenant?
print("\n  Test InitScript:")
flag, temp2 = read_u32(offset)
count, temp2 = read_u32(temp2)
print(f"    Flag={flag}, Count={count}")
if 0 <= count < 50:
    print(f"    ✓ Pourrait être InitScript!")
    offset = temp2

    # Parse commands
    for i in range(count):
        cmd_id, offset = read_u32(offset)
        cmd_sub, offset = read_u32(offset)
        cmd_param, offset = read_string(offset)
        if len(cmd_param) < 100:
            print(f"      Cmd {cmd_id}.{cmd_sub}: '{cmd_param}'")
else:
    print(f"    ✗ Pas InitScript")

# Config?
print(f"\n  Test Config @ 0x{offset:08X}:")
flag, temp2 = read_u32(offset)
ints = []
for i in range(7):
    val, temp2 = read_u32(temp2)
    ints.append(val)
print(f"    Flag={flag}, Ints={ints}")

# Est-ce raisonnable?
if all(i < 1000 or i > 4294967000 for i in ints):
    print(f"    ✓ Pourrait être Config!")
    offset = temp2
else:
    print(f"    ✗ Valeurs étranges")

# Hotspots?
print(f"\n  Test Hotspots @ 0x{offset:08X}:")
obj_count, temp2 = read_u32(offset)
print(f"    ObjCount={obj_count}")
if 0 <= obj_count < 50:
    print(f"    ✓ Pourrait être Hotspots! ({obj_count} objets)")
else:
    print(f"    ✗ Pas Hotspots")

print("\n" + "="*80)
print("CONCLUSION")
print("="*80)

print(f"\nStructure de Scène 2:")
print(f"  1. Slot 1: 'Le bureau du banquier' + param")
print(f"  2. Slots 2-5: (vides) + params")
print(f"  3. Slot 6: (vide) SANS param")
print(f"  4. String Pascal: '{filename}' + param")
print(f"  5. InitScript")
print(f"  6. Config")
print(f"  7. Hotspots")

print(f"\n⚠️  DIFFÉRENCE CLEF avec Scène 1:")
print(f"  Scène 1: 6 slots (tous avec params) → InitScript → Config → Hotspots")
print(f"  Scène 2: 6 slots (dernier sans param) → String BMP → InitScript → Config → Hotspots")
print(f"\nOU BIEN:")
print(f"  Scène 1: 6 fichiers de fond")
print(f"  Scène 2: 5 fichiers de fond + 1 champ vide + 1 fichier BMP supplémentaire?")
