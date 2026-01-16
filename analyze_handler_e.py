#!/usr/bin/env python3
"""
Analyse du Handler 'e' (Index 5) @ 0x004318EE
35 occurrences trouvées dans holl.vnd et autres fichiers
Pattern: "runprj couleurs1.vnp 54e"
"""
from capstone import *
import struct

EXE_FILE = "DOCS/europeo.exe"
HANDLER_E_ADDR = 0x004318EE
BASE_ADDR = 0x00400000

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

def main():
    print("="*80)
    print("ANALYSE HANDLER 'e' (Index 5) @ 0x004318EE")
    print("="*80)
    print()

    # Lit le fichier EXE
    with open(EXE_FILE, 'rb') as f:
        data = f.read()

    # Parse les sections PE
    sections = parse_pe_sections(data)

    # Convertit VA en offset fichier
    offset = va_to_file_offset(HANDLER_E_ADDR, sections)
    if not offset:
        print("✗ Impossible de trouver l'adresse")
        return

    print(f"Handler @ 0x{HANDLER_E_ADDR:08X}")
    print(f"File offset: 0x{offset:08X}")
    print()

    # Lit 300 bytes
    code = data[offset:offset+300]

    # Désassemble avec capstone
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    print("DÉSASSEMBLAGE (50 premières instructions):")
    print("-" * 80)

    calls_found = []
    jumps_found = []

    for i, insn in enumerate(md.disasm(code, HANDLER_E_ADDR)):
        if i >= 50:
            break

        print(f"{insn.address:08x}:  {insn.mnemonic:8} {insn.op_str:30}")

        if insn.mnemonic == 'call':
            calls_found.append({'addr': insn.address, 'target': insn.op_str})

        if insn.mnemonic.startswith('j'):
            jumps_found.append({'addr': insn.address, 'type': insn.mnemonic, 'target': insn.op_str})

    print()
    print("="*80)
    print("ANALYSE:")
    print("="*80)
    print()

    print(f"✓ Trouvé {len(calls_found)} appels de fonction")
    print(f"✓ Trouvé {len(jumps_found)} sauts")
    print()

    if calls_found:
        print("APPELS DE FONCTION:")
        print("-" * 80)
        for call in calls_found[:10]:
            print(f"  @ 0x{call['addr']:08X}  →  {call['target']}")
        print()

    # Comparaison avec handlers connus
    print("COMPARAISON AVEC HANDLERS CONNUS:")
    print("-" * 80)
    print("Handler 'f' (navigation) appelle: 0x4268F8")
    print("Handler 'g' (tooltip variant) appelle: 0x427D34, 0x427FAE, 0x4280EA")
    print("Handler 'h' (tooltip) appelle: 0x427FAE, 0x4280EA")
    print()
    print("Recherche de correspondances...")

    known_funcs = ['0x4268f8', '0x427d34', '0x427fae', '0x4280ea']
    for call in calls_found:
        target = call['target'].lower()
        if any(func in target for func in known_funcs):
            print(f"  ✓ MATCH: {call['target']} (connu)")
    print()

if __name__ == '__main__':
    main()
