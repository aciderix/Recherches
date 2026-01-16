#!/usr/bin/env python3
"""
Extrait la table des opcodes du dispatcher sub_43177D
"""

import struct
import sys

def va_to_file_offset(va, sections):
    """Convert VA to file offset"""
    va_no_base = va - 0x00400000 if va >= 0x00400000 else va
    for section in sections:
        virt_start = section['VirtualAddress']
        virt_end = virt_start + section['SizeOfRawData']
        if virt_start <= va_no_base < virt_end:
            offset_in_section = va_no_base - virt_start
            return section['PointerToRawData'] + offset_in_section
    return None

def parse_pe_sections(data):
    """Parse PE sections"""
    pe_offset = struct.unpack('<I', data[0x3C:0x40])[0]
    coff_offset = pe_offset + 4
    num_sections = struct.unpack('<H', data[coff_offset+2:coff_offset+4])[0]
    size_of_optional = struct.unpack('<H', data[coff_offset+16:coff_offset+18])[0]
    section_offset = coff_offset + 20 + size_of_optional

    sections = []
    for i in range(num_sections):
        sec_data = data[section_offset + i*40:section_offset + (i+1)*40]
        sections.append({
            'Name': sec_data[0:8].rstrip(b'\x00').decode('ascii', errors='ignore'),
            'VirtualAddress': struct.unpack('<I', sec_data[12:16])[0],
            'SizeOfRawData': struct.unpack('<I', sec_data[16:20])[0],
            'PointerToRawData': struct.unpack('<I', sec_data[20:24])[0]
        })
    return sections

def read_dword(data, offset):
    """Read DWORD at offset"""
    return struct.unpack('<I', data[offset:offset+4])[0]

def main():
    binary = "DOCS/europeo.exe"

    # Load binary
    with open(binary, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    # Switch table location (from disassembly):
    # 004317CE: jmp dword ptr [ecx*4 + 0x4317d5]
    switch_table_va = 0x004317D5
    num_entries = 0x2A + 1  # ecx va de 0 à 0x2A (cmp ecx, 0x2a)

    print("="*80)
    print("TABLE DES OPCODES DU DISPATCHER sub_43177D")
    print("="*80)
    print()
    print(f"Switch table @ 0x{switch_table_va:08X}")
    print(f"Number of entries: {num_entries} (0x00 - 0x{num_entries-1:02X})")
    print()

    offset = va_to_file_offset(switch_table_va, sections)
    if not offset:
        print("✗ Adresse invalide")
        return

    print(f"File offset: 0x{offset:08X}\n")

    # Known opcodes from doc
    known_opcodes = {
        'f': (6, "Navigation scène"),
        'h': (8, "Tooltip"),
        'i': (9, "Images (AVI/BMP)"),
        'j': (10, "Bitmaps (palette)"),
        'k': (11, "Audio (WAV)"),
        'u': (21, "Logic (if/then)"),
    }

    # Map letter → index
    opcode_names = {}
    for letter, (index, desc) in known_opcodes.items():
        opcode_names[index] = (letter, desc)

    # Read switch table
    print("="*80)
    print("SWITCH TABLE ENTRIES")
    print("="*80)
    print()
    print("| Index | Opcode | Handler Address | Known Function |")
    print("|-------|--------|-----------------|----------------|")

    handlers = {}
    for i in range(num_entries):
        handler_va = read_dword(data, offset + i * 4)

        # Check if valid code address
        if 0x00400000 <= handler_va <= 0x00500000:
            status = "✓"
        else:
            status = "✗ INVALID"

        # Check if we know this opcode
        if i in opcode_names:
            letter, desc = opcode_names[i]
            known = f"'{letter}' = {desc}"
        else:
            # Try to map to letter
            if 1 <= i <= 26:
                letter = chr(ord('a') + i - 1)
                known = f"'{letter}' = Unknown"
            else:
                known = f"Numeric opcode {i}"

        print(f"| {i:5d} | 0x{i:02X}   | 0x{handler_va:08X}    | {known}")

        # Store for later analysis
        if handler_va not in handlers:
            handlers[handler_va] = []
        handlers[handler_va].append((i, known))

    # Group by handler
    print("\n" + "="*80)
    print("HANDLERS GROUPÉS (Même fonction = opcodes similaires)")
    print("="*80)
    print()

    for handler_va, opcodes in sorted(handlers.items()):
        if len(opcodes) > 1:
            opcode_list = ', '.join(f"{idx} ({name})" for idx, name in opcodes)
            print(f"0x{handler_va:08X}: {opcode_list}")

    # Known handlers from disassembly
    print("\n" + "="*80)
    print("HANDLERS IDENTIFIÉS (depuis le désassemblage)")
    print("="*80)
    print()

    known_handlers = {
        0x0042703A: "Images (AVI/BMP) - Opcode 'i' (9)",
        0x00427B56: "Audio (WAV) - Opcode 'k' (11)",
        0x00427C42: "Audio alternative",
        0x004268F8: "Navigation scène - Opcode 'f' (6)",
    }

    for handler_va, desc in sorted(known_handlers.items()):
        # Find which opcodes use this handler
        if handler_va in handlers:
            opcodes = handlers[handler_va]
            opcode_str = ', '.join(str(idx) for idx, _ in opcodes)
            print(f"0x{handler_va:08X}: {desc}")
            print(f"  → Utilisé par opcodes: {opcode_str}")
        else:
            print(f"0x{handler_va:08X}: {desc}")
            print(f"  → Non trouvé dans la switch table (appelé directement?)")
        print()

    # Check for the scene navigation handler (opcode 'f' = 6)
    scene_nav_index = 6
    scene_nav_handler = read_dword(data, offset + scene_nav_index * 4)
    print("="*80)
    print(f"VÉRIFICATION: Opcode 'f' (Navigation) @ index {scene_nav_index}")
    print("="*80)
    print(f"Handler: 0x{scene_nav_handler:08X}")

    if scene_nav_handler == 0x004268F8:
        print("✓ CONFIRMÉ: Correspond à sub_4268F8 (doc VND)")
    else:
        print(f"⚠ DIFFÉRENT de sub_4268F8 (attendu selon doc)")

if __name__ == "__main__":
    main()
