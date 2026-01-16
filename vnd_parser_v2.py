#!/usr/bin/env python3
"""
VND Parser V2 - Version robuste avec détection automatique
"""

import struct
import sys
from pathlib import Path

class VNDParserV2:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'rb') as f:
            self.data = f.read()
        self.offset = 0

    def read_uint32(self, offset=None):
        if offset is not None:
            return struct.unpack('<I', self.data[offset:offset+4])[0]
        value = struct.unpack('<I', self.data[self.offset:self.offset+4])[0]
        self.offset += 4
        return value

    def find_vnfile_signature(self):
        """Trouve la signature VNFILE dans le fichier"""
        vnfile = b'VNFILE'
        pos = self.data.find(vnfile)
        if pos == -1:
            return None
        print(f"✓ Signature VNFILE trouvée @ 0x{pos:04X}")
        return pos

    def find_record_start(self):
        """Trouve le premier record (séparateur 01 00 00 00)"""
        # Cherche après les 200 premiers octets (header + variables)
        search_start = 0x80
        # Cherche dans tout le fichier si nécessaire (variables peuvent être longues)
        for i in range(search_start, len(self.data) - 12):
            separator = struct.unpack('<I', self.data[i:i+4])[0]
            if separator == 1:  # 01 00 00 00 en little-endian = 1
                # Vérifier que c'est suivi d'une longueur raisonnable et un type
                length = struct.unpack('<I', self.data[i+4:i+8])[0]
                type_id = struct.unpack('<I', self.data[i+8:i+12])[0]
                # Length peut être 0 (record vide), type doit être < 50
                if length < 100000 and type_id < 50:
                    print(f"✓ Premier record trouvé @ 0x{i:04X}")
                    return i
        return None

    def parse_quick(self):
        """Parse rapide pour afficher la structure"""
        print("="*80)
        print(f"VND QUICK PARSE: {self.filename}")
        print("="*80)
        print()

        # 1. Check signature
        sig_pos = self.find_vnfile_signature()
        if sig_pos is None:
            print("✗ Pas de signature VNFILE trouvée!")
            return

        # 2. Find first record
        record_start = self.find_record_start()
        if record_start is None:
            print("✗ Aucun record trouvé!")
            return

        print()
        print(f"Structure détectée:")
        print(f"  - Signature @ 0x{sig_pos:04X}")
        print(f"  - Records start @ 0x{record_start:04X}")
        print(f"  - Header + Variables size: ~{record_start} bytes")
        print()

        # 3. Parse records
        self.offset = record_start
        self.parse_records()

        # 4. Try to find variables in header area
        self.find_variables(0, record_start)

    def find_variables(self, start, end):
        """Cherche des variables dans une zone"""
        print("="*80)
        print(f"SEARCHING FOR VARIABLES (0x{start:04X} - 0x{end:04X})")
        print("="*80)
        print()

        variables = []
        i = start

        while i < end - 20:
            # Try to detect variable pattern: [length][name][00][value]
            try:
                name_len = struct.unpack('<I', self.data[i:i+4])[0]

                if 3 <= name_len <= 20:  # Reasonable variable name length
                    name_data = self.data[i+4:i+4+name_len]

                    # Check if it's printable ASCII
                    if all(32 <= b <= 126 or b == 0 for b in name_data):
                        name = name_data.rstrip(b'\x00').decode('ascii', errors='replace')

                        # Check for null terminator
                        next_pos = i + 4 + name_len
                        if next_pos < end and self.data[next_pos] == 0:
                            next_pos += 1

                        # Try to read value
                        if next_pos + 4 <= end:
                            value = struct.unpack('<I', self.data[next_pos:next_pos+4])[0]

                            # Validate: value should be reasonable
                            if value < 1000000:
                                variables.append({
                                    'offset': i,
                                    'name': name,
                                    'value': value
                                })
                                print(f"Variable @ 0x{i:04X}: {name:15s} = {value}")

                                i = next_pos + 4
                                continue

            except:
                pass

            i += 1

        print(f"\n✓ Found {len(variables)} potential variables")
        print()
        return variables

    def parse_records(self):
        """Parse records from current offset"""
        print("="*80)
        print("PARSING RECORDS")
        print("="*80)
        print()

        print(f"Starting @ 0x{self.offset:04X}\n")

        records = []
        count = 0

        while self.offset < len(self.data) - 12 and count < 500:
            separator = self.read_uint32()

            if separator != 1:  # 01 00 00 00 en little-endian = 1
                print(f"⚠ End of records @ 0x{self.offset-4:04X}")
                break

            length = self.read_uint32()
            type_id = self.read_uint32()

            if length > 50000:
                print(f"⚠ Invalid length {length}")
                break

            # Length peut être 0 (record vide)
            data = self.data[self.offset:self.offset+length] if length > 0 else b''
            self.offset += length

            # Try to interpret as string
            data_str = ""
            try:
                if all(b == 0 or 32 <= b <= 126 or b in [9, 10, 13] for b in data[:min(80, len(data))]):
                    data_str = data.decode('ascii', errors='replace').replace('\x00', '\\x00')
                else:
                    data_str = f"<{len(data)} bytes binary>"
            except:
                data_str = f"<{len(data)} bytes>"

            print(f"Record {count:3d}  Type={type_id:3d} (0x{type_id:02X})  Len={length:5d}  Data: {data_str[:70]}")

            records.append({
                'index': count,
                'type': type_id,
                'length': length,
                'data': data
            })

            count += 1

        print(f"\n✓ Parsed {count} records")

        # Summary by type
        print("\nRECORDS BY TYPE:")
        print("-"*40)
        types = {}
        for rec in records:
            t = rec['type']
            types[t] = types.get(t, 0) + 1

        for type_id in sorted(types.keys()):
            print(f"  Type {type_id:3d} (0x{type_id:02X}): {types[type_id]:3d} records")

        return records

def main():
    if len(sys.argv) < 2:
        print("Usage: vnd_parser_v2.py <file.vnd>")
        sys.exit(1)

    vnd_file = sys.argv[1]

    if not Path(vnd_file).exists():
        print(f"✗ File not found: {vnd_file}")
        sys.exit(1)

    parser = VNDParserV2(vnd_file)
    parser.parse_quick()

if __name__ == "__main__":
    main()
