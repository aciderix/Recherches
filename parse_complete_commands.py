#!/usr/bin/env python3
"""
Parser VND - Reconstitue les commandes complètes
Les commandes sont divisées en chunks de longueur variable
"""

import struct
import sys


def read_u32(data, pos):
    if pos + 4 > len(data):
        return None, pos
    return struct.unpack('<I', data[pos:pos+4])[0], pos + 4


def parse_complete_commands(filepath):
    """Parser qui reconstitue les commandes divisées en chunks"""

    with open(filepath, 'rb') as f:
        data = f.read()

    print("=" * 80)
    print("RECONSTITUTION DES COMMANDES COMPLÈTES")
    print("=" * 80)
    print()

    pos = 0x115C  # Début des données de scène
    command_num = 0

    while pos < len(data) - 12:
        # Chercher le marqueur 01 00 00 00
        marker_pos = data.find(b'\x01\x00\x00\x00', pos)
        if marker_pos == -1 or marker_pos >= len(data) - 12:
            break

        pos = marker_pos

        # Lire le record
        separator, pos = read_u32(data, pos)
        if separator != 1:
            pos = marker_pos + 1
            continue

        length, pos = read_u32(data, pos)
        if length is None or length > 100000 or length == 0:
            pos = marker_pos + 1
            continue

        rtype, pos = read_u32(data, pos)
        if rtype is None:
            pos = marker_pos + 1
            continue

        payload_end = pos + length
        if payload_end > len(data):
            pos = marker_pos + 1
            continue

        payload = data[pos:payload_end]

        # Vérifier le prochain marqueur
        next_marker = data.find(b'\x01\x00\x00\x00', payload_end)
        if next_marker == -1 or next_marker > payload_end + 200:
            pos = marker_pos + 1
            continue

        # Extraire le texte entre ce record et le prochain
        text_between = data[payload_end:next_marker]

        # Combiner le payload avec le texte qui suit
        full_text = (payload + text_between).decode('ascii', errors='ignore').strip('\x00')

        # Si c'est une commande avec 'then', l'afficher
        if 'then' in full_text and length < 100:
            command_num += 1
            print(f"[{command_num:3d}] @ 0x{marker_pos:06x} Type {rtype:3d} (0x{rtype:02x})")
            print(f"      Chunk: {length} bytes")
            print(f"      Commande: {full_text}")
            print()

            if command_num >= 50:
                print("... (limité à 50 commandes pour affichage)")
                break

        pos = payload_end


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: parse_complete_commands.py <fichier.vnd>")
        sys.exit(1)

    parse_complete_commands(sys.argv[1])
