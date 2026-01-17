#!/usr/bin/env python3
"""
Analyse la position et le contenu des records Type 0 pour comprendre leur rôle
"""
import struct
import re

filepath = 'Vnd-vnp/couleurs1.vnd'

with open(filepath, 'rb') as f:
    data = f.read()

text_content = data.decode('latin-1', errors='replace')

# Trouve tous les séparateurs
separators = []
pos = 0
while pos < len(data) - 12:
    if struct.unpack('<I', data[pos:pos+4])[0] == 1:
        length = struct.unpack('<I', data[pos+4:pos+8])[0]
        type_id = struct.unpack('<I', data[pos+8:pos+12])[0]

        if length < 100000 and type_id < 200:
            separators.append({
                'pos': pos,
                'length': length,
                'type': type_id,
                'data_offset': pos + 12
            })
    pos += 1

# Ajoute next_offset pour chaque separator
for i in range(len(separators)):
    if i + 1 < len(separators):
        separators[i]['next_offset'] = separators[i+1]['pos']
    else:
        separators[i]['next_offset'] = len(data)

# Cherche tous les BMP files
bmps = []
for match in re.finditer(r'(euroland\\[\w]+\.bmp)', text_content, re.IGNORECASE):
    if 'rollover' not in match.group(1).lower():
        bmps.append({'pos': match.start(), 'bmp': match.group(1)})

print("=" * 80)
print("ANALYSE DES RECORDS TYPE 0 et LEUR RELATION AVEC LES SCÈNES")
print("=" * 80)
print()

# Filtre les Type 0
type0_records = [s for s in separators if s['type'] == 0]

print(f"Total records Type 0: {len(type0_records)}")
print(f"Total fichiers BMP (scènes): {len(bmps)}")
print()

# Analyse chaque Type 0
for i, rec in enumerate(type0_records):
    offset = rec['data_offset']
    next_offset = rec['next_offset']
    length = next_offset - offset

    # Extrait texte jusqu'au prochain separator
    chunk = data[offset:min(offset+500, next_offset)]
    text = chunk.decode('latin-1', errors='replace')

    # Cherche BMP dans ce record
    bmp_match = re.search(r'euroland\\([\w]+\.bmp)', text, re.IGNORECASE)
    wav_match = re.search(r'([\w\\/-]+\.wav)', text, re.IGNORECASE)

    print(f"\n{'─' * 80}")
    print(f"TYPE 0 RECORD #{i+1} @ 0x{rec['pos']:08X}")
    print(f"{'─' * 80}")
    print(f"Length field: {rec['length']}")
    print(f"Real data size: {length}")

    if bmp_match:
        # Cherche quel numéro de scène c'est
        bmp_name = bmp_match.group(0)
        scene_num = None
        for idx, b in enumerate(bmps):
            if b['bmp'] == bmp_name:
                scene_num = idx + 1
                break

        print(f"🖼️  CONTIENT: {bmp_name} → SCÈNE #{scene_num}")

    if wav_match:
        print(f"🔊 AUDIO: {wav_match.group(1)}")

    # Cherche variables
    var_match = re.findall(r'\b([A-Z]{4,})\b', text[:200])
    if var_match and len(var_match) > 3:
        print(f"📊 VARIABLES: {', '.join(var_match[:5])}...")

    # Affiche premiers caractères imprimables
    clean = ''.join([c if 32 <= ord(c) <= 126 else ' ' for c in text[:100]])
    clean = re.sub(r'\s+', ' ', clean).strip()
    if clean:
        print(f"Début: {clean[:70]}...")

print("\n" + "=" * 80)
print("CONCLUSION")
print("=" * 80)
