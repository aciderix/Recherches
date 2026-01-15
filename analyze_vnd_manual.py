#!/usr/bin/env python3
"""
Analyse manuelle VND - Approche correcte
Basé sur l'observation réelle de la structure
"""

import struct
import sys

def read_u32(data, pos):
    return struct.unpack('<I', data[pos:pos+4])[0], pos+4

def read_cstring(data, pos):
    """Lire une chaîne null-terminated"""
    end = data.find(b'\x00', pos)
    if end == -1:
        return "", pos
    return data[pos:end].decode('ascii', errors='ignore'), end+1

def analyze_structure(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()

    print("=" * 70)
    print("ANALYSE MANUELLE VND - STRUCTURE RÉELLE")
    print("=" * 70)

    # Zone 1: Header
    print("\n📦 ZONE 1: HEADER (0x0000 - 0x0086)")
    print("  ├─ Magic: 0x3A010100")
    print("  ├─ Signature: VNFILE")
    print("  ├─ Version: 2.136")
    print("  ├─ Région: Europeo")
    print("  ├─ Éditeur: Sopra Multimedia")
    print("  ├─ ID: 5D51F233")
    print("  ├─ Résolution: 640x480x16")
    print("  └─ DLL: ..\\VnStudio\\vnresmod.dll")

    # Zone 2: Variables
    print("\n📋 ZONE 2: TABLE DE VARIABLES (0x0086 - 0x1154)")

    pos = 0x008A
    var_count = 0
    while pos < 0x1154:
        length, pos = read_u32(data, pos)
        if length == 0 or length > 100:
            break
        varname = data[pos:pos+length].decode('ascii')
        var_count += 1
        pos += length + 4  # +4 pour le padding

    print(f"  └─ {var_count} variables de jeu")

    # Zone 3: Données de scène
    print("\n🎬 ZONE 3: DONNÉES DE SCÈNE (0x115C - fin)")

    pos = 0x115C
    entry_num = 0

    print("\n  Entrées de scène:\n")

    while pos < min(len(data), 0x12500):
        # Chercher le prochain marqueur 01 00 00 00
        marker_pos = data.find(b'\x01\x00\x00\x00', pos)
        if marker_pos == -1 or marker_pos > len(data) - 100:
            break

        entry_num += 1
        pos = marker_pos

        # Lire l'entrée
        marker, pos = read_u32(data, pos)

        print(f"  ┌─ Entrée #{entry_num} @ 0x{marker_pos:04x}")

        # Afficher les 80 premiers bytes
        chunk = data[marker_pos:marker_pos+min(80, len(data)-marker_pos)]

        # Chercher des strings
        strings_found = []
        i = 4  # Après le marqueur
        while i < len(chunk):
            # Détecter si c'est du texte ASCII
            if 32 <= chunk[i] < 127:
                # Lire jusqu'au prochain null ou non-ASCII
                s = ""
                start = i
                while i < len(chunk) and 32 <= chunk[i] < 127:
                    s += chr(chunk[i])
                    i += 1

                if len(s) > 3:
                    strings_found.append((start, s))
            i += 1

        # Afficher les strings
        for off, s in strings_found[:5]:
            print(f"  │  +{off:02d} (0x{marker_pos+off:04x}): \"{s}\"")

        # Afficher les premiers uint32
        vals = []
        for i in range(min(8, (len(chunk)-4)//4)):
            v = struct.unpack('<I', chunk[i*4:i*4+4])[0]
            vals.append(v)

        print(f"  │  Values: {vals[:8]}")
        print(f"  └─")

        # Avancer au prochain
        pos = marker_pos + 4

        if entry_num >= 50:  # Limiter
            print(f"\n  ... (limité à 50 entrées)")
            break

    print(f"\n  Total: {entry_num} entrées de scène")

    # Statistiques finales
    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ")
    print("=" * 70)
    print(f"""
Structure du fichier VND:

1. HEADER (134 bytes)
   └─ Métadonnées du fichier

2. TABLE DE VARIABLES ({var_count} variables)
   └─ Noms des flags/variables du jeu

3. DONNÉES DE SCÈNE ({entry_num} entrées)
   └─ Commandes de scène avec:
      • Chemins de fichiers (images, audio, vidéos)
      • Paramètres d'affichage
      • Textes/dialogues
      • Logique de scène

⚠️  Format complexe avec structures imbriquées
⚠️  Pas de format bloc simple [len][type][payload]
⚠️  Structure variable selon le type d'entrée

Pour aller plus loin:
- Identifier les différents types d'entrées
- Décoder la structure exacte de chaque type
- Extraire les ressources (images, sons, textes)
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: analyze_vnd_manual.py <fichier.vnd>")
        sys.exit(1)

    analyze_structure(sys.argv[1])
