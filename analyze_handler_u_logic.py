#!/usr/bin/env python3
"""
Analyse du Handler 'u' (opcode 21) - Logic if/then
Adresse handler: 0x00431A7C
Fonction appelée: 0x00428373 (probablement)
"""

import struct
import sys

try:
    from capstone import *
    HAS_CAPSTONE = True
except ImportError:
    HAS_CAPSTONE = False

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

def analyze_function(data, sections, va, name):
    """Analyze a function with capstone"""
    print("="*80)
    print(f"ANALYSE: {name}")
    print(f"Adresse: 0x{va:08X}")
    print("="*80)
    print()

    offset = va_to_file_offset(va, sections)
    if not offset:
        print("✗ Adresse invalide")
        return

    print(f"File offset: 0x{offset:08X}\n")

    code = data[offset:offset+2000]

    if not HAS_CAPSTONE:
        print("⚠ Capstone non disponible")
        return

    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    print("Assembly:")
    print("-"*80)

    function_calls = []
    comparisons = []
    jumps = []
    var_refs = []

    for i, insn in enumerate(md.disasm(code, va)):
        print(f"{insn.address:08x}:  {insn.mnemonic:8s} {insn.op_str}")

        # Track function calls
        if insn.mnemonic == 'call':
            if '0x' in insn.op_str:
                try:
                    target = int(insn.op_str.replace('call ', '').strip(), 16)
                    function_calls.append((insn.address, target))
                except:
                    pass
            elif 'dword ptr' in insn.op_str:
                function_calls.append((insn.address, 'virtual'))

        # Track comparisons (for if/then logic)
        if insn.mnemonic in ['cmp', 'test']:
            comparisons.append((insn.address, insn.op_str))

        # Track jumps (conditional branches)
        if insn.mnemonic.startswith('j'):
            jumps.append((insn.address, insn.mnemonic, insn.op_str))

        # Track variable table references
        if '0x44ecce' in insn.op_str.lower():
            var_refs.append((insn.address, insn.mnemonic, insn.op_str))

        if insn.mnemonic == 'ret':
            print(f"\n✓ Fin de fonction @ 0x{insn.address:08X}")
            break

        if i > 400:
            print("\n⚠ Limité à 400 instructions")
            break

    # Analysis
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print()
    print(f"Function calls: {len(function_calls)}")
    print(f"Comparisons: {len(comparisons)}")
    print(f"Conditional jumps: {len(jumps)}")
    print(f"Variable table refs: {len(var_refs)}")
    print()

    if function_calls:
        print("Function Calls:")
        for addr, target in function_calls[:15]:
            if target == 'virtual':
                print(f"  0x{addr:08X} → virtual call")
            else:
                print(f"  0x{addr:08X} → 0x{target:08X}")
        if len(function_calls) > 15:
            print(f"  ... and {len(function_calls) - 15} more")
        print()

    if comparisons:
        print("Comparisons (if logic):")
        for addr, op_str in comparisons[:10]:
            print(f"  0x{addr:08X}: {op_str}")
        if len(comparisons) > 10:
            print(f"  ... and {len(comparisons) - 10} more")
        print()

    if var_refs:
        print("Variable Table References (0x44ECCE):")
        for addr, mnemonic, op_str in var_refs:
            print(f"  0x{addr:08X}: {mnemonic} {op_str}")
        print()

def main():
    binary = "DOCS/europeo.exe"

    with open(binary, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    print("="*80)
    print("HANDLER 'u' (OPCODE 21) - LOGIC IF/THEN")
    print("="*80)
    print()
    print("Selon la doc VND:")
    print("  - Opcode 'u' = index 21")
    print("  - Fonction: sub_431721 (dans la doc)")
    print("  - Rôle: Évaluation conditions if/then/else")
    print("  - Format: if VARIABLE OPERATOR VALUE then COMMAND")
    print()
    print("Depuis ma première analyse:")
    print("  - Handler wrapper @ 0x00431A7C")
    print("  - Appelle probablement: 0x00428373")
    print()

    # Analyze the wrapper first
    print("\n" + "="*80)
    print("1. WRAPPER @ 0x00431A7C (extrait du dispatcher)")
    print("="*80)
    print()
    print("Code extrait de l'analyse précédente:")
    print("-"*80)
    print("""00431a7c:  test     esi, esi
00431a7e:  je       0x4321b6
00431a84:  mov      eax, esi
00431a86:  add      eax, 0x1c           ; param +0x1c
00431a89:  push     eax
00431a8a:  mov      edx, esi
00431a8c:  add      edx, 0xc            ; param +0xc
00431a8f:  push     edx
00431a90:  push     dword ptr [esi + 8] ; param +0x8
00431a93:  mov      ecx, esi
00431a95:  add      ecx, 4              ; param +0x4
00431a98:  push     ecx
00431a99:  add      esi, 0x20           ; param +0x20
00431a9c:  push     esi
00431a9d:  push     ebx                 ; context
00431a9e:  call     0x428373            ; ← LOGIC FUNCTION
""")

    print("\nParamètres passés (6 total):")
    print("  1. ebx = contexte")
    print("  2. esi+0x20 = ??")
    print("  3. esi+0x4 = ??")
    print("  4. esi+0x8 = ??")
    print("  5. esi+0xc = ??")
    print("  6. esi+0x1c = ??")
    print()

    # Analyze the real logic function
    logic_func_va = 0x00428373
    analyze_function(data, sections, logic_func_va, "sub_428373 - Logic Function (réelle)")

    # Also analyze the one from doc
    print("\n\n")
    doc_logic_va = 0x00431721
    analyze_function(data, sections, doc_logic_va, "sub_431721 - Logic Function (doc VND)")

if __name__ == "__main__":
    main()
