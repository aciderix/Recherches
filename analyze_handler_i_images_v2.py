#!/usr/bin/env python3
"""
Analyse du Handler 'i' (Index 9) @ 0x004321B6 - Images (AVI/BMP)
Selon la doc: sub_42703A pour chargement images
"""
from capstone import *
import struct

EXE_FILE = "DOCS/europeo.exe"
HANDLER_I_ADDR = 0x004321B6  # Handler 'i' dans switch table
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

def analyze_handler_i():
    """Analyse le handler 'i' @ 0x004321B6"""

    print("="*80)
    print("ANALYSE HANDLER 'i' (Index 9) @ 0x004321B6 - Images")
    print("="*80)
    print()

    # Lit le fichier EXE
    with open(EXE_FILE, 'rb') as f:
        data = f.read()

    # Parse les sections PE
    sections = parse_pe_sections(data)

    print("Sections PE:")
    for sec in sections:
        print(f"  {sec['Name']:8} VA=0x{sec['VirtualAddress']:08X} Size=0x{sec['SizeOfRawData']:08X}")
    print()

    # Convertit VA en offset fichier
    offset = va_to_file_offset(HANDLER_I_ADDR, sections)
    if not offset:
        print("✗ Impossible de trouver l'adresse dans les sections")
        return

    print(f"Handler @ 0x{HANDLER_I_ADDR:08X}")
    print(f"File offset: 0x{offset:08X}")
    print()

    # Lit 500 bytes
    code = data[offset:offset+500]

    # Check prologue
    if code[0:2] == b'\x55\x8b':
        print("✓ Function prologue: push ebp; mov ebp, esp")
    elif code[0:3] == b'\x8b\xff\x55':
        print("✓ Function prologue: mov edi,edi; push ebp (hotpatch)")
    elif code[0:1] == b'\x83':  # sub esp, ...
        print("✓ Wrapper prologue: stack frame setup")
    else:
        print(f"⚠ Non-standard prologue: {code[0:8].hex()}")
    print()

    # Désassemble avec capstone
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    print("DÉSASSEMBLAGE (100 premières instructions):")
    print("-" * 80)

    calls_found = []
    jumps_found = []
    params_access = []

    for i, insn in enumerate(md.disasm(code, HANDLER_I_ADDR)):
        if i >= 100:  # Limite à 100 instructions
            break

        print(f"{insn.address:08x}:  {insn.mnemonic:8} {insn.op_str:30}")

        # Détecte les CALL (appels de fonction)
        if insn.mnemonic == 'call':
            calls_found.append({
                'addr': insn.address,
                'target': insn.op_str
            })

        # Détecte les JMP/JE/JNE/etc
        if insn.mnemonic.startswith('j'):
            jumps_found.append({
                'addr': insn.address,
                'type': insn.mnemonic,
                'target': insn.op_str
            })

        # Détecte les accès aux paramètres (esi, edi, ebx typiquement)
        if 'esi' in insn.op_str or 'edi' in insn.op_str or 'ebx' in insn.op_str:
            params_access.append({
                'addr': insn.address,
                'insn': f"{insn.mnemonic} {insn.op_str}"
            })

    print()
    print("="*80)
    print("ANALYSE:")
    print("="*80)
    print()

    print(f"✓ Trouvé {len(calls_found)} appels de fonction (CALL)")
    print(f"✓ Trouvé {len(jumps_found)} sauts conditionnels/inconditionnels")
    print(f"✓ Trouvé {len(params_access)} accès aux paramètres")
    print()

    if calls_found:
        print("APPELS DE FONCTION:")
        print("-" * 80)
        for call in calls_found[:10]:  # Top 10
            print(f"  @ 0x{call['addr']:08X}  →  {call['target']}")
        print()

    if jumps_found[:5]:
        print("PREMIERS SAUTS:")
        print("-" * 80)
        for jump in jumps_found[:5]:
            print(f"  @ 0x{jump['addr']:08X}  {jump['type']:8}  →  {jump['target']}")
        print()

    # Analyse spécifique: cherche le pattern typique d'un wrapper
    print("PATTERN WRAPPER:")
    print("-" * 80)

    # Le handler devrait:
    # 1. Tester si les paramètres existent (test esi/edi, je ...)
    # 2. Préparer les paramètres sur la stack
    # 3. CALL vers la vraie fonction (sub_42703A selon doc)

    print("1. Check paramètres: ", end="")
    has_param_check = any('test' in p['insn'] for p in params_access[:5])
    print("✓" if has_param_check else "✗")

    print("2. Préparation stack: ", end="")
    has_push = any('push' in p['insn'] for p in params_access[:10])
    print("✓" if has_push else "✗")

    print("3. Call sub_42703A: ", end="")
    # Cherche un call vers 0x42703A
    has_target_call = any('0x42703a' in call['target'].lower() for call in calls_found)
    print("✓" if has_target_call else "✗")

    if has_target_call:
        target_call = [c for c in calls_found if '0x42703a' in c['target'].lower()][0]
        print(f"   → Trouvé @ 0x{target_call['addr']:08X}")
    else:
        print("   ⚠ sub_42703A non trouvé, cherchons d'autres calls...")
        if calls_found:
            print(f"   Premier call: {calls_found[0]['target']} @ 0x{calls_found[0]['addr']:08X}")

    print()

if __name__ == '__main__':
    analyze_handler_i()
