#!/usr/bin/env python3
"""
Parse manuel byte-par-byte de Scène 2 pour comprendre la vraie structure
"""
import struct

data = open('Vnd-vnp/couleurs1.vnd', 'rb').read()

def show_bytes(offset, count, label=""):
    """Affiche les bytes à un offset donné"""
    bytes_str = ' '.join([f'{data[offset+i]:02X}' for i in range(count)])
    ascii_str = ''.join([chr(data[offset+i]) if 32 <= data[offset+i] < 127 else '.' for i in range(count)])
    if label:
        print(f"  {label}")
    print(f"    @ 0x{offset:08X}: {bytes_str}  |  {ascii_str}")

def read_u32_at(offset):
    """Lit un u32 à un offset donné SANS déplacer le curseur"""
    return struct.unpack('<I', data[offset:offset+4])[0]

def read_string_at(offset):
    """Lit une string Pascal à un offset donné et retourne (string, next_offset)"""
    length = read_u32_at(offset)
    if length == 0:
        return "", offset + 4
    string = data[offset+4:offset+4+length].decode('latin-1', errors='replace')
    return string, offset + 4 + length

print("="*80)
print("PARSE MANUEL SCÈNE 2 - Byte par byte")
print("="*80)

# Scène 2 commence à 0x1A31
offset = 0x1A31

print(f"\n[SLOT 1] @ 0x{offset:08X}")
show_bytes(offset, 4, "Length:")
length = read_u32_at(offset)
print(f"    → Length = {length}")
offset += 4

show_bytes(offset, length, f"String ({length} chars):")
string = data[offset:offset+length].decode('latin-1')
print(f"    → String = '{string}'")
offset += length

show_bytes(offset, 4, "Param:")
param = read_u32_at(offset)
print(f"    → Param = {param}")
offset += 4

print(f"\n[SLOT 2] @ 0x{offset:08X}")
show_bytes(offset, 8)
string, offset = read_string_at(offset)
param = read_u32_at(offset)
print(f"  → String = '{string}', Param = {param}")
offset += 4

print(f"\n[SLOT 3] @ 0x{offset:08X}")
show_bytes(offset, 12)
string, offset = read_string_at(offset)
param = read_u32_at(offset)
print(f"  → String = '{string}' (len={len(string)}), Param = {param}")
offset += 4

print(f"\n[SLOT 4] @ 0x{offset:08X}")
show_bytes(offset, 8)
string, offset = read_string_at(offset)
param = read_u32_at(offset)
print(f"  → String = '{string}', Param = {param}")
offset += 4

print(f"\n[SLOT 5] @ 0x{offset:08X}")
show_bytes(offset, 8)
string, offset = read_string_at(offset)
param = read_u32_at(offset)
print(f"  → String = '{string}', Param = {param}")
offset += 4

print(f"\n[SLOT 6] @ 0x{offset:08X}")
print("  Affichage des 64 prochains bytes:")
for i in range(4):
    show_bytes(offset + i*16, 16)

# Slot 6 string
show_bytes(offset, 4, "\n  Length de Slot 6:")
length = read_u32_at(offset)
print(f"    → Length = {length}")
offset += 4

print(f"\n  Après Slot 6 length, offset = 0x{offset:08X}")
print("  Question: Y a-t-il un param ou pas?")

print("\n  OPTION A: Slot 6 a un param")
show_bytes(offset, 4, "    Param potentiel:")
param_a = read_u32_at(offset)
print(f"      → Param = {param_a} (0x{param_a:08X})")

print("\n  OPTION B: Slot 6 n'a PAS de param, c'est le début de la prochaine string")
show_bytes(offset, 4, "    Length potentielle:")
length_b = read_u32_at(offset)
print(f"      → Length = {length_b} (0x{length_b:08X})")

string_b = ""
if length_b > 0 and length_b < 100:
    show_bytes(offset+4, min(length_b, 40), "    String potentielle:")
    string_b = data[offset+4:offset+4+length_b].decode('latin-1', errors='replace')
    print(f"      → String = '{string_b}'")
    print(f"\n  ✓ OPTION B semble correcte! C'est une string valide.")
else:
    print(f"\n  ✗ Length invalide pour OPTION B")

print("\n" + "="*80)
print("HYPOTHÈSE FINALE")
print("="*80)

if string_b:
    print(f"\nScène 2 a une structure:")
    print(f"  - Slot 1-5: (String + Param) × 5")
    print(f"  - Slot 6: String seulement, PAS de param")
    print(f"  - Puis une 7ème string: '{string_b}'")

print(f"\nCette 7ème string est probablement:")
print(f"  - Soit un fichier de fond supplémentaire (slot 7)")
print(f"  - Soit le début d'une structure différente")

if string_b:
    # Continuons après cette string
    offset_after_bmp = offset + 4 + length_b
    show_bytes(offset_after_bmp, 4, f"\nAprès '{string_b}':")
    param_bmp = read_u32_at(offset_after_bmp)
    print(f"  → Param/Value = {param_bmp} (0x{param_bmp:08X})")

    print(f"\nSi c'est un fichier de fond: param={param_bmp}")
    print(f"Si c'est autre chose: cette valeur a une autre signification")

    # Essayons de continuer - est-ce InitScript après?
    offset_after_param = offset_after_bmp + 4
    print(f"\n" + "="*80)
    print(f"APRÈS LE BMP @ 0x{offset_after_param:08X}")
    print("="*80)

    print("\nTest InitScript:")
    flag = read_u32_at(offset_after_param)
    count = read_u32_at(offset_after_param + 4)
    print(f"  Flag={flag}, Count={count}")

    if 0 <= count < 50:
        print(f"  ✓ C'est probablement InitScript!")
    else:
        print(f"  ✗ Pas InitScript")
else:
    print("\nIMPOSSIBLE de parser - structure inconnue!")
