#!/usr/bin/env python3
"""
Analyse détaillée du Handler 'f' (opcode 6) - Navigation scène
Adresse: 0x0043198B (depuis switch table)
"""

import struct
import sys

try:
    from capstone import *
    HAS_CAPSTONE = True
except ImportError:
    HAS_CAPSTONE = False
    print("⚠ Capstone not installed, using hexdump only")

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

def analyze_function(data, sections, va, name, max_size=2000):
    """Analyze a function"""
    print("="*80)
    print(f"ANALYSE: {name}")
    print(f"Adresse: 0x{va:08X}")
    print("="*80)
    print()

    offset = va_to_file_offset(va, sections)
    if not offset:
        print("✗ Adresse invalide")
        return None

    print(f"File offset: 0x{offset:08X}\n")

    code = data[offset:offset+max_size]

    # Check function prologue
    if code[0:2] == b'\x55\x8b' or code[0:1] == b'\x55':
        print("✓ Function prologue: push ebp; mov ebp, esp\n")
    elif code[0:3] == b'\x8b\xff\x55':
        print("✓ Function prologue: mov edi,edi; push ebp (hotpatch)\n")
    else:
        print(f"⚠ Non-standard prologue: {code[0:8].hex()}\n")

    if not HAS_CAPSTONE:
        print("Hexdump (first 256 bytes):")
        for i in range(0, min(256, len(code)), 16):
            chunk = code[i:i+16]
            hex_str = ' '.join(f'{b:02x}' for b in chunk)
            print(f"{va + i:08x}:  {hex_str}")
        return None

    # Disassemble with capstone
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    print("Assembly Code:")
    print("-"*80)

    instructions = []
    function_calls = []
    string_refs = []
    interesting_ops = []

    for i, insn in enumerate(md.disasm(code, va)):
        instructions.append(insn)
        print(f"{insn.address:08x}:  {insn.mnemonic:8s} {insn.op_str}")

        # Track function calls
        if insn.mnemonic == 'call':
            # Extract call target
            op_str = insn.op_str
            if op_str.startswith('0x'):
                target = int(op_str, 16)
                function_calls.append((insn.address, target))
            elif 'dword ptr' in op_str:
                function_calls.append((insn.address, 'indirect'))

        # Track string/data references
        if insn.mnemonic == 'push' and '0x' in insn.op_str:
            try:
                addr = int(insn.op_str.replace('push ', '').strip(), 16)
                if 0x00400000 <= addr <= 0x00500000:
                    string_refs.append((insn.address, addr))
            except:
                pass

        # Track interesting operations
        if insn.mnemonic in ['test', 'cmp', 'jne', 'je', 'jmp']:
            interesting_ops.append((insn.address, insn.mnemonic, insn.op_str))

        # Stop at ret
        if insn.mnemonic == 'ret':
            print(f"\n✓ Function end at 0x{insn.address:08X}")
            print(f"  Function size: {insn.address - va + 1} bytes")
            break

        # Safety limit
        if i > 300:
            print("\n⚠ Stopped after 300 instructions (limit)")
            break

    # Analysis summary
    print("\n" + "="*80)
    print("ANALYSIS SUMMARY")
    print("="*80)
    print()

    print(f"Total instructions: {len(instructions)}")
    print(f"Function calls: {len(function_calls)}")
    print(f"String/data refs: {len(string_refs)}")
    print()

    if function_calls:
        print("Function Calls:")
        print("-"*40)
        for addr, target in function_calls:
            if target == 'indirect':
                print(f"  0x{addr:08X} → indirect call (virtual?)")
            else:
                print(f"  0x{addr:08X} → 0x{target:08X}")
        print()

    if string_refs:
        print("Data/String References:")
        print("-"*40)
        for addr, ref in string_refs[:10]:  # Limit to 10
            print(f"  0x{addr:08X} → 0x{ref:08X}")
        if len(string_refs) > 10:
            print(f"  ... and {len(string_refs) - 10} more")
        print()

    return instructions

def main():
    binary = "DOCS/europeo.exe"

    # Load binary
    with open(binary, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    # Handler 'f' - Navigation (opcode 6)
    handler_f_va = 0x0043198B

    print("="*80)
    print("HANDLER 'f' (OPCODE 6) - NAVIGATION SCÈNE")
    print("="*80)
    print()
    print("Selon la doc VND:")
    print("  - Opcode 'f' = index 6")
    print("  - Fonction: sub_4268F8 (dans la doc)")
    print("  - Rôle: Transition entre scènes")
    print()
    print("Depuis la switch table:")
    print(f"  - Handler: 0x{handler_f_va:08X}")
    print()

    instructions = analyze_function(data, sections, handler_f_va, "Handler 'f' - Navigation", max_size=3000)

    if instructions:
        print("\n" + "="*80)
        print("INTERPRETATION")
        print("="*80)
        print()

        # Look for characteristic scene navigation patterns
        has_esi_check = any(i.mnemonic == 'test' and 'esi' in i.op_str for i in instructions)
        has_scene_call = any(i.mnemonic == 'call' and '42' in i.op_str for i in instructions)

        if has_esi_check:
            print("✓ Pattern détecté: test esi, esi (vérification paramètre)")
        if has_scene_call:
            print("✓ Pattern détecté: appels dans la zone 0x0042xxxx (fonctions scène)")

        print()
        print("Hypothèse:")
        print("  Ce handler est un WRAPPER qui:")
        print("  1. Vérifie si des paramètres sont fournis (esi)")
        print("  2. Appelle la vraie fonction de navigation")
        print("  3. Retourne au dispatcher")

    # Now analyze the real scene navigation function
    print("\n\n")
    scene_nav_va = 0x004268F8
    analyze_function(data, sections, scene_nav_va, "sub_4268F8 - Navigation réelle (depuis doc)", max_size=3000)

if __name__ == "__main__":
    main()
