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

def read_exe_section(filename, rva, size):
    """Lit une section du fichier EXE"""
    # Offset dans le fichier = RVA - 0x1000 + 0x400 (header PE)
    file_offset = rva - 0x1000 + 0x400
    with open(filename, 'rb') as f:
        f.seek(file_offset)
        return f.read(size)

def analyze_handler_i():
    """Analyse le handler 'i' @ 0x004321B6"""

    print("="*80)
    print("ANALYSE HANDLER 'i' (Index 9) @ 0x004321B6 - Images")
    print("="*80)
    print()

    # Lit 500 bytes à partir de l'adresse du handler
    rva = HANDLER_I_ADDR - BASE_ADDR
    code = read_exe_section(EXE_FILE, rva, 500)

    print(f"Handler @ 0x{HANDLER_I_ADDR:08X} (RVA: 0x{rva:08X})")
    print()

    # Désassemble avec capstone
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    print("DÉSASSEMBLAGE:")
    print("-" * 80)

    calls_found = []
    jumps_found = []
    params_access = []

    for i, insn in enumerate(md.disasm(code, HANDLER_I_ADDR)):
        if i > 100:  # Limite à 100 instructions
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

    print()

if __name__ == '__main__':
    analyze_handler_i()
