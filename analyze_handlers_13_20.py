#!/usr/bin/env python3
"""
Analyse groupée des handlers 13-20 (m-t)
Désassemble et identifie les fonctions appelées
"""
from capstone import *
import struct

EXE_FILE = "DOCS/europeo.exe"
BASE_ADDR = 0x00400000

# Handlers 13-20 (m-t)
HANDLERS = {
    13: {'letter': 'm', 'addr': 0x004319CB},
    14: {'letter': 'n', 'addr': 0x00431BAB},
    15: {'letter': 'o', 'addr': 0x00431BB8},
    16: {'letter': 'p', 'addr': 0x00431BCF},
    17: {'letter': 'q', 'addr': 0x00431BEE},
    18: {'letter': 'r', 'addr': 0x00431C0D},
    19: {'letter': 's', 'addr': 0x00431C2C},
    20: {'letter': 't', 'addr': 0x00431D6A},
}

# Fonctions connues
KNOWN_FUNCTIONS = {
    0x00427B56: "Audio WAV (handler 'k')",
    0x0042703A: "Images loading (handler 'i')",
    0x004321B6: "Handler 'i' (Images)",
    0x004268F8: "Navigation (handler 'f')",
    0x00427D34: "Tooltip func (handler 'g')",
    0x00427FAE: "Tooltip func (handler 'h')",
    0x004280EA: "Tooltip func (handler 'h')",
    0x00428373: "Logic engine (handler 'u')",
    0x00426B62: "Pre-proc func A",
    0x00426D33: "Pre-proc func B",
    0x004275F6: "Pre-proc func D",
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

def analyze_handler(idx, letter, addr, data, sections):
    """Analyse un handler"""
    print(f"\n{'='*80}")
    print(f"HANDLER '{letter}' (Index {idx}) @ 0x{addr:08X}")
    print(f"{'='*80}")

    offset = va_to_file_offset(addr, sections)
    if not offset:
        print("✗ Impossible de trouver l'adresse")
        return None

    print(f"File offset: 0x{offset:08X}")

    # Lit 150 bytes
    code = data[offset:offset+150]

    # Désassemble
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    calls_found = []
    jumps_found = []
    jump_to_handler_i = False

    print("\nDÉSASSEMBLAGE (30 premières instructions):")
    print("-" * 80)

    for i, insn in enumerate(md.disasm(code, addr)):
        if i >= 30:
            break

        print(f"{insn.address:08x}:  {insn.mnemonic:8} {insn.op_str:30}")

        if insn.mnemonic == 'call':
            calls_found.append({'addr': insn.address, 'target': insn.op_str})

        if insn.mnemonic.startswith('j'):
            jumps_found.append({'addr': insn.address, 'type': insn.mnemonic, 'target': insn.op_str})
            # Détecte jump vers handler 'i'
            if '0x4321b6' in insn.op_str.lower():
                jump_to_handler_i = True

    # Analyse
    print(f"\n✓ Trouvé {len(calls_found)} appels de fonction")
    print(f"✓ Trouvé {len(jumps_found)} sauts")

    # Fonctions appelées
    direct_calls = []
    if calls_found:
        print("\nAPPELS DE FONCTION:")
        print("-" * 80)
        for call in calls_found[:10]:
            target_str = call['target']
            print(f"  @ 0x{call['addr']:08X}  →  {target_str}")

            # Parse target si c'est une adresse directe
            if target_str.startswith('0x'):
                try:
                    target_addr = int(target_str, 16)
                    direct_calls.append(target_addr)
                    if target_addr in KNOWN_FUNCTIONS:
                        print(f"      ✓ KNOWN: {KNOWN_FUNCTIONS[target_addr]}")
                except:
                    pass

    # Pattern détecté
    pattern = "Unknown"
    if jump_to_handler_i:
        pattern = "Pre-processor → handler 'i'"

    print(f"\nPATTERN DÉTECTÉ: {pattern}")

    return {
        'idx': idx,
        'letter': letter,
        'addr': addr,
        'calls': len(calls_found),
        'jumps': len(jumps_found),
        'direct_calls': direct_calls,
        'jump_to_i': jump_to_handler_i,
        'pattern': pattern
    }

def main():
    print("="*80)
    print("ANALYSE HANDLERS 13-20 (m-t)")
    print("="*80)
    print()

    # Lit le fichier EXE
    with open(EXE_FILE, 'rb') as f:
        data = f.read()

    # Parse les sections PE
    sections = parse_pe_sections(data)

    # Analyse chaque handler
    results = []
    for idx in sorted(HANDLERS.keys()):
        info = HANDLERS[idx]
        result = analyze_handler(idx, info['letter'], info['addr'], data, sections)
        if result:
            results.append(result)

    # Résumé
    print("\n" + "="*80)
    print("RÉSUMÉ DES HANDLERS 13-20")
    print("="*80)
    print()

    for r in results:
        print(f"Handler '{r['letter']}' ({r['idx']:2d}) @ 0x{r['addr']:08X}:")
        print(f"  Calls: {r['calls']}, Jumps: {r['jumps']}")
        print(f"  Pattern: {r['pattern']}")
        if r['direct_calls']:
            print(f"  Direct calls: {', '.join(f'0x{a:08X}' for a in r['direct_calls'][:3])}")
        print()

if __name__ == '__main__':
    main()
