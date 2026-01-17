#!/usr/bin/env python3
"""
Recherche exacte: où est le champ LENGTH de "euroland\bureaubanquier.bmp"?
"""
import struct

data = open('Vnd-vnp/couleurs1.vnd', 'rb').read()

# "euroland\bureaubanquier.bmp" = 27 caractères
expected_length = 27

# En little-endian, 27 = 0x1B serait stocké comme: 1B 00 00 00
length_bytes = struct.pack('<I', 27)
print(f"27 en little-endian bytes: {' '.join([f'{b:02X}' for b in length_bytes])}")

# Cherchons ce pattern dans la zone de Scène 2
scene2_start = 0x1A31
search_start = 0x1A6F  # Après Slot 6
search_end = 0x1B00

print(f"\nRecherche de [1B 00 00 00] entre 0x{search_start:08X} et 0x{search_end:08X}:")

for offset in range(search_start, search_end):
    if data[offset:offset+4] == length_bytes:
        print(f"  Trouvé @ 0x{offset:08X}")

        # Vérifie que la string suit
        string_start = offset + 4
        string = data[string_start:string_start+27].decode('latin-1', errors='replace')
        print(f"    String suivante: '{string}'")

        if "euroland" in string:
            print(f"    ✓ C'EST LE BON OFFSET!")

            print(f"\nDonc:")
            print(f"  - Slot 6 string length @ 0x1A6F-0x1A72 (=0)")
            print(f"  - BMP string length @ 0x{offset:08X}-0x{offset+3:08X} (=27)")
            print(f"  - Écart: {offset - 0x1A73} bytes après la fin de Slot 6")

            if offset - 0x1A73 == 3:
                print(f"\n⚠️  Il y a 3 bytes de padding/gap!")
                print(f"  Bytes @ 0x1A73-0x1A75:")
                for i in range(3):
                    print(f"    0x{0x1A73+i:08X}: 0x{data[0x1A73+i]:02X}")
            elif offset - 0x1A73 == 4:
                print(f"\n  Les 4 bytes entre les deux sont le param de Slot 6:")
                param = struct.unpack('<I', data[0x1A73:0x1A77])[0]
                print(f"    Param = {param}")
