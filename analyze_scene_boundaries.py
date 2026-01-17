#!/usr/bin/env python3
"""
Analyse approfondie de la structure exacte des scènes 1 et 2
pour comprendre où ça diverge
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

def analyze_scene_1():
    print("="*80)
    print("SCÈNE 1 - ANALYSE COMPLÈTE")
    print("="*80)

    offset = 0x1164
    print(f"\nDébut: 0x{offset:08X}")

    # 6 fichiers
    print("\n6 FICHIERS:")
    for i in range(1, 7):
        start = offset
        filename, offset = read_string(offset)
        param, offset = read_u32(offset)
        repr_fn = f"'{filename}'" if filename else "(vide)"
        print(f"  Slot {i} @ 0x{start:08X}-0x{offset:08X}: {repr_fn:<30} param={param}")

    # InitScript
    print(f"\nINIT SCRIPT @ 0x{offset:08X}:")
    flag, offset = read_u32(offset)
    count, offset = read_u32(offset)
    print(f"  Flag={flag}, Count={count}")

    # Config
    print(f"\nCONFIG @ 0x{offset:08X}:")
    flag, offset = read_u32(offset)
    print(f"  Flag={flag}")
    ints = []
    for i in range(7):
        val, offset = read_u32(offset)
        ints.append(val)
    print(f"  Ints: {ints}")

    # Hotspots
    print(f"\nHOTSPOTS @ 0x{offset:08X}:")
    obj_count, offset = read_u32(offset)
    print(f"  Count={obj_count}")

    # Parse tous les hotspots
    for obj_idx in range(obj_count):
        print(f"\n  Hotspot {obj_idx+1} @ 0x{offset:08X}:")
        cmd_count, offset = read_u32(offset)
        print(f"    Commands: {cmd_count}")

        # Skip commands
        for cmd_idx in range(cmd_count):
            cmd_id, offset = read_u32(offset)
            cmd_sub, offset = read_u32(offset)
            cmd_param, offset = read_string(offset)

        # Géométrie
        cursor_id, offset = read_u32(offset)
        point_count, offset = read_u32(offset)
        print(f"    Géométrie: cursor={cursor_id}, points={point_count}")

        # Skip points
        offset += point_count * 8

        # ExtraFlag
        extra, offset = read_u32(offset)

    print(f"\nFIN SCÈNE 1: 0x{offset:08X}")
    return offset

def analyze_scene_2(start_offset):
    print("\n" + "="*80)
    print("SCÈNE 2 - ANALYSE COMPLÈTE")
    print("="*80)

    offset = start_offset
    print(f"\nDébut: 0x{offset:08X}")

    # Essayons de parser comme Scène 1
    print("\n6 FICHIERS (tentative):")
    for i in range(1, 7):
        start = offset
        try:
            filename, new_offset = read_string(offset)
            param, new_offset = read_u32(new_offset)
            repr_fn = f"'{filename}'" if filename else "(vide)"
            print(f"  Slot {i} @ 0x{start:08X}-0x{new_offset:08X}: {repr_fn:<30} param={param}")
            offset = new_offset
        except Exception as e:
            print(f"  Slot {i} @ 0x{start:08X}: ERREUR - {e}")
            break

    # InitScript
    print(f"\nINIT SCRIPT @ 0x{offset:08X}:")
    try:
        flag, new_offset = read_u32(offset)
        count, new_offset = read_u32(new_offset)
        print(f"  Flag={flag} (0x{flag:08X}), Count={count} (0x{count:08X})")

        # Si count semble invalide, regardons ce qu'il y a vraiment
        if count > 100:
            print(f"  ⚠️ Count semble invalide!")
            print(f"\n  Contenu brut:")
            for i in range(40):
                b = data[offset + i]
                if i % 16 == 0:
                    print(f"    +{i:02X}: ", end="")
                print(f"{b:02X} ", end="")
                if (i+1) % 16 == 0:
                    print(" | ", end="")
                    for j in range(i-15, i+1):
                        c = data[offset + j]
                        print(chr(c) if 32 <= c < 127 else '.', end="")
                    print()
        offset = new_offset
    except Exception as e:
        print(f"  ERREUR: {e}")

    print(f"\nPosition actuelle: 0x{offset:08X}")

# Analyse Scène 1
scene1_end = analyze_scene_1()

# Analyse Scène 2
analyze_scene_2(scene1_end)

# Maintenant cherchons où est vraiment le BMP de scène 2
print("\n" + "="*80)
print("RECHERCHE euroland\\bureaubanquier.bmp")
print("="*80)

bmp_pos = data.find(b'euroland\\bureaubanquier.bmp')
print(f"\nTrouvé à: 0x{bmp_pos:08X}")
print(f"Scène 1 se termine à: 0x{scene1_end:08X}")
print(f"Écart: 0x{bmp_pos - scene1_end:08X} octets")

# Affiche les 100 octets entre fin Scène 1 et bureaubanquier.bmp
print(f"\nContenu entre fin Scène 1 et bureaubanquier.bmp:")
between = data[scene1_end:bmp_pos+4]
for i in range(0, len(between), 16):
    offset_val = scene1_end + i
    hex_part = ' '.join([f'{b:02X}' for b in between[i:i+16]])
    ascii_part = ''.join([chr(b) if 32 <= b < 127 else '.' for b in between[i:i+16]])
    print(f"  0x{offset_val:08X}  {hex_part:<48}  {ascii_part}")
