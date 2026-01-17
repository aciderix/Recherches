#!/usr/bin/env python3
"""
Analyse complète des handlers 22-42
Détecte patterns, fonctions appelées, et handlers dupliqués
"""
from capstone import *
import struct

EXE_FILE = "DOCS/europeo.exe"
BASE_ADDR = 0x00400000

# Handlers 22-42
HANDLERS = {
    22: {'name': 'v', 'addr': 0x00431AD9},
    23: {'name': 'w', 'addr': 0x00431AF3},
    24: {'name': 'x', 'addr': 0x00431B0F},
    25: {'name': 'y', 'addr': 0x00431D84},
    26: {'name': 'z', 'addr': 0x00431D58},
    27: {'name': 'num_27', 'addr': 0x00431DE5},
    28: {'name': 'num_28', 'addr': 0x00431E11},
    29: {'name': 'num_29', 'addr': 0x00431F5A},
    30: {'name': 'num_30', 'addr': 0x0043192E},
    31: {'name': 'num_31', 'addr': 0x00431E05},
    32: {'name': 'num_32', 'addr': 0x00431FE0},
    33: {'name': 'num_33', 'addr': 0x00432005},
    34: {'name': 'num_34', 'addr': 0x004321B6},  # Handler 'i' !
    35: {'name': 'num_35', 'addr': 0x00431AAB},
    36: {'name': 'num_36', 'addr': 0x00431AD9},  # Duplicate!
    37: {'name': 'num_37', 'addr': 0x00431AF3},  # Duplicate!
    38: {'name': 'num_38', 'addr': 0x00431B0F},  # Duplicate!
    39: {'name': 'num_39', 'addr': 0x00432105},
    40: {'name': 'num_40', 'addr': 0x0043216D},
    41: {'name': 'num_41', 'addr': 0x0043194D},
    42: {'name': 'num_42', 'addr': 0x0043196C},
}

# Fonctions connues
KNOWN_FUNCTIONS = {
    0x004321B6: "Handler 'i' (Images) - HUB CENTRAL",
    0x00427B56: "Audio WAV (handler 'k')",
    0x0042703A: "Images loading",
    0x004268F8: "Navigation (handler 'f')",
    0x00428373: "Logic engine (handler 'u')",
    0x0044ECCE: "Table Variables (BSS)",
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

def quick_analyze_handler(idx, name, addr, data, sections):
    """Analyse rapide d'un handler"""

    # Handler 'i' déjà connu
    if addr == 0x004321B6:
        return {
            'idx': idx,
            'name': name,
            'addr': addr,
            'pattern': "Handler 'i' (Images) - HUB CENTRAL",
            'duplicate': False,
            'calls': 0
        }

    offset = va_to_file_offset(addr, sections)
    if not offset:
        return None

    # Lit 80 bytes
    code = data[offset:offset+80]

    # Désassemble
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    calls_found = []
    jump_to_handler_i = False

    for i, insn in enumerate(md.disasm(code, addr)):
        if i >= 25:
            break

        if insn.mnemonic == 'call':
            calls_found.append({'addr': insn.address, 'target': insn.op_str})

        if insn.mnemonic.startswith('j'):
            # Détecte jump vers handler 'i'
            if '0x4321b6' in insn.op_str.lower():
                jump_to_handler_i = True

    # Détermine pattern
    pattern = "Unknown"
    if jump_to_handler_i:
        pattern = "Pre-processor → handler 'i'"
    elif len(calls_found) == 0:
        pattern = "Direct handler (no calls)"

    return {
        'idx': idx,
        'name': name,
        'addr': addr,
        'pattern': pattern,
        'calls': len(calls_found),
        'jump_to_i': jump_to_handler_i
    }

def main():
    print("="*80)
    print("ANALYSE HANDLERS 22-42 (v-z + opcodes numériques)")
    print("="*80)
    print()

    # Lit le fichier EXE
    with open(EXE_FILE, 'rb') as f:
        data = f.read()

    # Parse les sections PE
    sections = parse_pe_sections(data)

    # Détecte duplicates
    addr_to_handlers = {}
    for idx, info in HANDLERS.items():
        addr = info['addr']
        if addr not in addr_to_handlers:
            addr_to_handlers[addr] = []
        addr_to_handlers[addr].append((idx, info['name']))

    print("DÉTECTION DUPLICATES:")
    print("-" * 80)
    duplicates = {addr: handlers for addr, handlers in addr_to_handlers.items() if len(handlers) > 1}

    if duplicates:
        for addr, handlers in sorted(duplicates.items()):
            handler_list = ', '.join(f"{name} ({idx})" for idx, name in handlers)
            print(f"  @ 0x{addr:08X}: {handler_list}")
    else:
        print("  Aucun duplicate détecté")

    print()

    # Analyse rapide de chaque handler unique
    print("ANALYSE RAPIDE PAR ADRESSE UNIQUE:")
    print("="*80)

    analyzed_addrs = set()
    results = []

    for idx in sorted(HANDLERS.keys()):
        info = HANDLERS[idx]
        addr = info['addr']

        # Skip si déjà analysé
        if addr in analyzed_addrs:
            continue
        analyzed_addrs.add(addr)

        result = quick_analyze_handler(idx, info['name'], addr, data, sections)
        if result:
            results.append(result)

            # Affiche
            handlers_at_addr = addr_to_handlers[addr]
            handler_names = ', '.join(f"{name}({i})" for i, name in handlers_at_addr)

            print(f"\nHandlers: {handler_names}")
            print(f"  @ 0x{addr:08X}")
            print(f"  Pattern: {result['pattern']}")
            print(f"  Calls: {result['calls']}")

    # Résumé par pattern
    print("\n" + "="*80)
    print("RÉSUMÉ PAR PATTERN")
    print("="*80)

    patterns = {}
    for r in results:
        p = r['pattern']
        if p not in patterns:
            patterns[p] = []
        patterns[p].append(r)

    for pattern, handlers in sorted(patterns.items()):
        print(f"\n{pattern}: {len(handlers)} handlers")
        for h in handlers:
            print(f"  - {h['name']} ({h['idx']}) @ 0x{h['addr']:08X}")

    # Stats finales
    print("\n" + "="*80)
    print("STATISTIQUES")
    print("="*80)
    print(f"Total handlers 22-42: 21")
    print(f"Adresses uniques: {len(analyzed_addrs)}")
    print(f"Duplicates: {sum(len(h)-1 for h in addr_to_handlers.values() if len(h) > 1)}")
    print(f"Pointent vers handler 'i': {sum(1 for h in addr_to_handlers.values() if h[0][0] == 34 or any(i == 34 for i, _ in h))}")

if __name__ == '__main__':
    main()
