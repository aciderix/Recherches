#!/usr/bin/env python3
"""
Analyse rapide des handlers média: 'h', 'i', 'j', 'k', 'l'
"""
from capstone import *
import struct

EXE_FILE = "DOCS/europeo.exe"
BASE_ADDR = 0x00400000

# Handlers selon extract_opcode_table.py
HANDLERS = {
    'h': {'addr': 0x00431B70, 'name': 'Tooltip', 'doc_func': '0x426D33'},
    'i': {'addr': 0x004321B6, 'name': 'Images', 'doc_func': '0x42703A'},
    'j': {'addr': 0x00432201, 'name': 'Bitmaps', 'doc_func': '0x4275F6'},
    'k': {'addr': 0x0043224C, 'name': 'Audio WAV', 'doc_func': '0x427B56'},
    'l': {'addr': 0x00432297, 'name': 'Music MIDI', 'doc_func': '0x427C42'},
}

def va_to_file_offset(va, sections):
    """Convert VA to file offset"""
    va_no_base = va - BASE_ADDR if va >= BASE_ADDR else va
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

def analyze_handler(data, sections, opcode, info):
    """Analyse un handler"""
    print("="*80)
    print(f"HANDLER '{opcode}' - {info['name']}")
    print(f"Adresse: 0x{info['addr']:08X}")
    print(f"Fonction documentée: sub_{info['doc_func'][2:]}")
    print("="*80)

    offset = va_to_file_offset(info['addr'], sections)
    if not offset:
        print("✗ Adresse invalide\n")
        return

    code = data[offset:offset+300]

    # Désassemble
    md = Cs(CS_ARCH_X86, CS_MODE_32)

    calls_found = []
    for i, insn in enumerate(md.disasm(code, info['addr'])):
        if i >= 50:  # Limite à 50 instructions
            break

        if insn.mnemonic == 'call':
            calls_found.append({
                'addr': insn.address,
                'target': insn.op_str
            })

    print(f"✓ Trouvé {len(calls_found)} appels de fonction")

    if calls_found:
        print("\nAPPELS:")
        for call in calls_found[:8]:
            # Check si c'est la fonction documentée
            is_doc = info['doc_func'].lower() in call['target'].lower()
            marker = " ← DOCUMENTED FUNCTION" if is_doc else ""
            print(f"  @ 0x{call['addr']:08X}  →  {call['target']}{marker}")

    print()

def main():
    print("="*80)
    print("ANALYSE DES HANDLERS MÉDIA")
    print("="*80)
    print()

    # Lit le fichier EXE
    with open(EXE_FILE, 'rb') as f:
        data = f.read()

    # Parse les sections PE
    sections = parse_pe_sections(data)

    # Analyse chaque handler
    for opcode in ['h', 'i', 'j', 'k', 'l']:
        analyze_handler(data, sections, opcode, HANDLERS[opcode])

if __name__ == '__main__':
    main()
