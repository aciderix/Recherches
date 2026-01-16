#!/usr/bin/env python3
"""
VND File Parser
===============

Parse les fichiers VND (Visual Novel Data) selon la spécification documentée:
- Header avec signature VNFILE
- Table des variables
- Records séquentiels
"""

import struct
import sys
from pathlib import Path

class VNDParser:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'rb') as f:
            self.data = f.read()
        self.offset = 0
        self.header = None
        self.variables = []
        self.records = []

    def read_uint32(self):
        """Lit un uint32 little-endian"""
        value = struct.unpack('<I', self.data[self.offset:self.offset+4])[0]
        self.offset += 4
        return value

    def read_uint16(self):
        """Lit un uint16 little-endian"""
        value = struct.unpack('<H', self.data[self.offset:self.offset+2])[0]
        self.offset += 2
        return value

    def read_bytes(self, count):
        """Lit count octets"""
        value = self.data[self.offset:self.offset+count]
        self.offset += count
        return value

    def read_string(self, length):
        """Lit une chaîne de longueur donnée (terminée par null)"""
        data = self.data[self.offset:self.offset+length]
        self.offset += length
        # Find null terminator
        try:
            null_pos = data.index(b'\x00')
            return data[:null_pos].decode('ascii', errors='replace')
        except ValueError:
            return data.decode('ascii', errors='replace')

    def parse_header(self):
        """Parse le header VND"""
        print("="*80)
        print("PARSING HEADER")
        print("="*80)
        print()

        header = {}

        # Magic number (9 bytes)
        magic = self.read_bytes(9)
        header['magic'] = magic.hex()
        print(f"Magic: {magic.hex()}")

        # Signature "VNFILE" (6 bytes)
        signature = self.read_bytes(6)
        header['signature'] = signature.decode('ascii', errors='replace')
        print(f"Signature: {header['signature']}")

        if header['signature'] != 'VNFILE':
            print("⚠ ATTENTION: Signature invalide! Attendu 'VNFILE'")

        # Version length
        version_len = self.read_uint32()
        print(f"Version length: {version_len}")

        # Version string
        if version_len > 0 and version_len < 100:  # Sanity check
            version = self.read_string(version_len)
            header['version'] = version
            print(f"Version: {version}")

        # Project name length
        project_len = self.read_uint32()
        print(f"Project name length: {project_len}")

        # Project name
        if project_len > 0 and project_len < 100:
            project = self.read_string(project_len)
            header['project'] = project
            print(f"Project: {project}")

        # Creator length
        creator_len = self.read_uint32()
        print(f"Creator length: {creator_len}")

        # Creator
        if creator_len > 0 and creator_len < 100:
            creator = self.read_string(creator_len)
            header['creator'] = creator
            print(f"Creator: {creator}")

        # Expected offset for checksum: around 0x48
        print(f"\nCurrent offset: 0x{self.offset:04X}")

        # Checksum length (should be at 0x48)
        if self.offset < 0x48:
            # Skip to 0x48
            skip = 0x48 - self.offset
            print(f"Skipping {skip} bytes to reach checksum...")
            self.offset = 0x48

        checksum_len = self.read_uint32()
        print(f"Checksum length: {checksum_len}")

        # Checksum (8 bytes as text)
        if checksum_len > 0 and checksum_len < 20:
            checksum = self.read_bytes(checksum_len)
            header['checksum'] = checksum.decode('ascii', errors='replace')
            print(f"Checksum: {header['checksum']}")

        # Padding (8 bytes of zeros)
        padding = self.read_bytes(8)

        # Screen dimensions
        width = self.read_uint32()
        height = self.read_uint32()
        color_depth = self.read_uint32()

        header['width'] = width
        header['height'] = height
        header['color_depth'] = color_depth

        print(f"\nScreen: {width}x{height} @ {color_depth}bit")

        # Flags (3 x uint32 = 12 bytes)
        flags = []
        for i in range(3):
            flag = self.read_uint32()
            flags.append(flag)
        header['flags'] = flags
        print(f"Flags: {[hex(f) for f in flags]}")

        # Reserved (4 bytes)
        reserved = self.read_uint32()

        # DLL path length
        dll_len = self.read_uint32()
        print(f"DLL path length: {dll_len}")

        # DLL path
        if dll_len > 0 and dll_len < 200:
            dll_path = self.read_string(dll_len)
            header['dll_path'] = dll_path
            print(f"DLL path: {dll_path}")

        print(f"\nHeader end offset: 0x{self.offset:04X}")
        print()

        self.header = header
        return header

    def parse_variable_table(self):
        """Parse la table des variables"""
        print("="*80)
        print("PARSING VARIABLE TABLE")
        print("="*80)
        print()

        print(f"Starting offset: 0x{self.offset:04X}\n")

        variables = []
        var_count = 0

        while var_count < 100:  # Safety limit
            # Try to read length
            if self.offset + 4 > len(self.data):
                break

            name_len = self.read_uint32()

            # End of variable table detection
            if name_len == 0 or name_len > 100 or name_len == 0x01000000:
                # Might be start of records (separator = 0x01000000)
                self.offset -= 4  # Rewind
                print(f"\nEnd of variable table at offset 0x{self.offset:04X}")
                print(f"Detected potential record separator: 0x{name_len:08X}")
                break

            # Variable name
            var_name = self.read_string(name_len)

            # Skip null terminator if present
            if self.data[self.offset:self.offset+1] == b'\x00':
                self.offset += 1

            # Variable value
            var_value = self.read_uint32()

            variables.append({
                'name': var_name,
                'value': var_value
            })

            print(f"Variable {var_count+1}: {var_name:15s} = {var_value}")
            var_count += 1

        print(f"\n✓ Parsed {var_count} variables")
        print()

        self.variables = variables
        return variables

    def parse_records(self):
        """Parse les records séquentiels"""
        print("="*80)
        print("PARSING RECORDS")
        print("="*80)
        print()

        print(f"Starting offset: 0x{self.offset:04X}\n")

        records = []
        record_count = 0

        while self.offset < len(self.data) - 12 and record_count < 1000:  # Safety
            # Separator (should be 0x01000000)
            separator = self.read_uint32()

            if separator != 0x01000000:
                print(f"⚠ Invalid separator at 0x{self.offset-4:04X}: 0x{separator:08X}")
                # Try to resync
                if separator == 0:  # End of file?
                    break
                continue

            # Length
            length = self.read_uint32()

            # Type ID
            type_id = self.read_uint32()

            # Data
            if length > 0 and length < 100000:  # Sanity check
                data = self.read_bytes(length)
            else:
                print(f"⚠ Invalid length {length} at record {record_count}")
                break

            record = {
                'index': record_count,
                'offset': self.offset - 12 - length,
                'separator': separator,
                'length': length,
                'type': type_id,
                'data': data
            }

            records.append(record)

            # Try to interpret data
            data_str = ""
            try:
                # Try as ASCII string
                if all(32 <= b <= 126 or b in [0, 9, 10, 13] for b in data[:min(50, len(data))]):
                    data_str = data.decode('ascii', errors='replace').replace('\x00', ' ')
                else:
                    data_str = f"<{len(data)} bytes binary>"
            except:
                data_str = f"<{len(data)} bytes>"

            print(f"Record {record_count:4d} @ 0x{record['offset']:06X}:  Type={type_id:3d} (0x{type_id:02X})  Len={length:5d}  Data: {data_str[:60]}")

            record_count += 1

        print(f"\n✓ Parsed {record_count} records")
        print()

        self.records = records
        return records

    def save_summary(self, output_file):
        """Sauvegarde un résumé du parsing"""
        with open(output_file, 'w') as f:
            f.write("="*80 + "\n")
            f.write(f"VND FILE ANALYSIS: {self.filename}\n")
            f.write("="*80 + "\n\n")

            # Header
            f.write("HEADER\n")
            f.write("-"*80 + "\n")
            for key, value in self.header.items():
                f.write(f"{key:15s} = {value}\n")
            f.write("\n")

            # Variables
            f.write(f"VARIABLES ({len(self.variables)})\n")
            f.write("-"*80 + "\n")
            for var in self.variables:
                f.write(f"{var['name']:15s} = {var['value']}\n")
            f.write("\n")

            # Records by type
            f.write(f"RECORDS ({len(self.records)})\n")
            f.write("-"*80 + "\n")

            # Group by type
            types = {}
            for rec in self.records:
                t = rec['type']
                if t not in types:
                    types[t] = []
                types[t].append(rec)

            for type_id in sorted(types.keys()):
                recs = types[type_id]
                f.write(f"\nType {type_id} (0x{type_id:02X}): {len(recs)} records\n")
                for rec in recs[:5]:  # First 5
                    data_preview = str(rec['data'][:40])
                    f.write(f"  Record {rec['index']:4d} @ 0x{rec['offset']:06X}  Len={rec['length']:5d}  {data_preview}\n")
                if len(recs) > 5:
                    f.write(f"  ... and {len(recs) - 5} more\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: vnd_parser.py <file.vnd>")
        print("\nExample: vnd_parser.py DOCS/europeo.vnd")
        sys.exit(1)

    vnd_file = sys.argv[1]

    if not Path(vnd_file).exists():
        print(f"✗ File not found: {vnd_file}")
        sys.exit(1)

    print("="*80)
    print(f"VND PARSER - {vnd_file}")
    print("="*80)
    print()

    parser = VNDParser(vnd_file)

    # Parse header
    parser.parse_header()

    # Parse variable table
    parser.parse_variable_table()

    # Parse records
    parser.parse_records()

    # Save summary
    output = vnd_file + ".analysis.txt"
    parser.save_summary(output)
    print(f"✓ Summary saved to: {output}")

if __name__ == "__main__":
    main()
