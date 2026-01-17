#!/usr/bin/env python3
"""
Vérification: Scène 2 a-t-elle InitScript/Config ou pas?
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

print("="*80)
print("HYPOTHÈSE: Scène 2 saute InitScript/Config")
print("="*80)

offset = 0x1A31
print(f"\nDébut Scène 2: 0x{offset:08X}")

# Parse les 6 slots
print("\n6 SLOTS:")
for i in range(1, 7):
    filename, offset = read_string(offset)
    param, offset = read_u32(offset)
    print(f"  Slot {i}: {repr(filename):<30} param={param}")

print(f"\nAprès les 6 slots: 0x{offset:08X}")

# Maintenant, au lieu de chercher InitScript/Config, cherchons directement un BMP
print("\nCherchons directement un fichier (.bmp, .wav, etc):")

# Lisons comme une String Pascal
filename, new_offset = read_string(offset)
if filename:
    print(f"  Trouvé: '{filename}'")
    param, new_offset = read_u32(new_offset)
    print(f"  Param: {param}")
    offset = new_offset
else:
    print("  Rien trouvé")

# Peut-être qu'après il y a InitScript/Config?
print(f"\nOffset actuel: 0x{offset:08X}")
print("\nEssayons InitScript/Config maintenant:")

flag, new_offset = read_u32(offset)
count, new_offset = read_u32(new_offset)
print(f"  Flag: {flag}, Count: {count}")

if 0 <= count < 50:
    print(f"  ✓ Semble valide! ({count} commandes)")
    offset = new_offset
else:
    print(f"  ✗ Invalide")

# Config
print(f"\nConfig @ 0x{offset:08X}:")
flag, new_offset = read_u32(offset)
ints = []
for i in range(7):
    val, new_offset = read_u32(new_offset)
    ints.append(val)
print(f"  Flag: {flag}")
print(f"  Ints: {ints}")
offset = new_offset

# Hotspots
print(f"\nHotspots @ 0x{offset:08X}:")
obj_count, new_offset = read_u32(offset)
print(f"  Count: {obj_count}")

if 0 <= obj_count < 50:
    print(f"  ✓ Semble valide! ({obj_count} hotspots)")
else:
    print(f"  ✗ Invalide")

print("\n" + "="*80)
print("CONCLUSION")
print("="*80)
print(f"\nScène 2 semble avoir la structure:")
print(f"  1. 6 slots (dont Slot 1 = 'Le bureau du banquier')")
print(f"  2. Un fichier BMP: '{filename}' avec param={param}")
print(f"  3. InitScript (flag={flag}, count={count})")
print(f"  4. Config")
print(f"  5. {obj_count} Hotspots")
