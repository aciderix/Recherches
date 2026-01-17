#!/usr/bin/env python3
"""
Test simple pour comprendre la structure exacte au début d'une scène
"""
import struct

data = open('Vnd-vnp/couleurs1.vnd', 'rb').read()

def read_u32(offset):
    return struct.unpack('<I', data[offset:offset+4])[0]

def read_string(offset):
    length = read_u32(offset)
    if length == 0:
        return offset + 4, ""
    string = data[offset+4:offset+4+length].decode('latin-1')
    return offset + 4 + length, string

print("="*70)
print("SCÈNE 1 @ 0x1164")
print("="*70)

offset = 0x1164

# Test: Y a-t-il un nom de scène?
print(f"\n0x{offset:08X}: ", end="")
next_offset, name = read_string(offset)
if name:
    print(f"NOM SCÈNE = '{name}'")
else:
    print(f"Pas de nom de scène (length=0)")
offset = next_offset

# Slot 1
print(f"0x{offset:08X}: ", end="")
next_offset, filename = read_string(offset)
offset = next_offset
param = read_u32(offset)
offset += 4
print(f"Slot 1: '{filename}' (param={param})")

# Slot 2
print(f"0x{offset:08X}: ", end="")
next_offset, filename = read_string(offset)
offset = next_offset
param = read_u32(offset)
offset += 4
print(f"Slot 2: '{filename}' (param={param})")

print("\n" + "="*70)
print("SCÈNE 2 @ 0x1A31")
print("="*70)

offset = 0x1A31

# Test: Y a-t-il un nom de scène?
print(f"\n0x{offset:08X}: ", end="")
next_offset, name = read_string(offset)
if name:
    print(f"NOM SCÈNE = '{name}'")
else:
    print(f"Pas de nom de scène (length=0)")
offset = next_offset

# Slot 1
print(f"0x{offset:08X}: ", end="")
next_offset, filename = read_string(offset)
offset = next_offset
param = read_u32(offset)
offset += 4
print(f"Slot 1: '{filename}' (param={param})")

# Slot 2
print(f"0x{offset:08X}: ", end="")
next_offset, filename = read_string(offset)
offset = next_offset
param = read_u32(offset)
offset += 4
print(f"Slot 2: '{filename}' (param={param})")

# Slot 3
print(f"0x{offset:08X}: ", end="")
next_offset, filename = read_string(offset)
offset = next_offset
param = read_u32(offset)
offset += 4
print(f"Slot 3: '{filename}' (param={param})")

# Slot 4
print(f"0x{offset:08X}: ", end="")
next_offset, filename = read_string(offset)
offset = next_offset
param = read_u32(offset)
offset += 4
print(f"Slot 4: '{filename}' (param={param})")
