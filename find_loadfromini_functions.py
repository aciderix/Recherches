#!/usr/bin/env python3
"""
Smart approach: Find LoadFromINI functions by searching for INI keyword strings
Instead of relying on RTTI, scan all functions and find those containing INI keywords
"""

import struct
from capstone import *
from capstone.x86 import *
import sys

# INI keywords to search for
INI_KEYWORDS = [
    'AREA_', 'NAME', 'BKCOLOR', 'COLOR', 'TEXTURE',
    'CURSOR', 'CAPS', 'WIDTH', 'HEIGHT', 'SIZE',
    'POSITION', 'X', 'Y', 'LEFT', 'RIGHT', 'TOP', 'BOTTOM',
    'FONT', 'TEXT', 'TITLE', 'VALUE', 'TYPE',
    'IMAGE', 'BITMAP', 'SOUND', 'MUSIC', 'VIDEO',
    'SPEED', 'DELAY', 'TIME', 'FRAME', 'INDEX',
    'SCENE', 'HOTSPOT', 'COMMAND', 'EVENT', 'ACTION',
]


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
            'VirtualSize': struct.unpack('<I', sec_data[8:12])[0],
            'VirtualAddress': struct.unpack('<I', sec_data[12:16])[0],
            'SizeOfRawData': struct.unpack('<I', sec_data[16:20])[0],
            'PointerToRawData': struct.unpack('<I', sec_data[20:24])[0]
        })
    return sections


def va_to_file_offset(va, sections):
    """Convert VA to file offset"""
    va_no_base = va - 0x00400000 if va >= 0x00400000 else va
    for section in sections:
        virt_start = section['VirtualAddress']
        virt_end = virt_start + section['VirtualSize']
        if virt_start <= va_no_base < virt_end:
            offset_in_section = va_no_base - virt_start
            if offset_in_section < section['SizeOfRawData']:
                return section['PointerToRawData'] + offset_in_section
    return None


def read_string(data, offset, max_len=64):
    if offset < 0 or offset >= len(data):
        return None
    result = []
    for i in range(max_len):
        if offset + i >= len(data):
            break
        byte = data[offset + i]
        if byte == 0:
            break
        if 32 <= byte <= 126:
            result.append(chr(byte))
        else:
            break
    return ''.join(result) if len(result) >= 3 else None


def find_all_strings_in_data(data, sections):
    """Find all strings in DATA section"""
    strings = {}  # addr -> string

    for section in sections:
        if section['Name'] not in ['DATA', '.data', '.rdata']:
            continue

        offset = section['PointerToRawData']
        end = offset + section['SizeOfRawData']

        i = offset
        while i < end:
            string = read_string(data, i)
            if string:
                va = i - offset + section['VirtualAddress'] + 0x00400000
                strings[va] = string
                i += len(string) + 1
            else:
                i += 1

    return strings


def analyze_function_for_strings(data, sections, func_va, all_strings, max_size=0x1000):
    """Analyze a function and find which strings it references"""
    offset = va_to_file_offset(func_va, sections)
    if offset is None:
        return None

    code_bytes = data[offset:offset + max_size]

    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    referenced_strings = []

    try:
        for instr in md.disasm(code_bytes, func_va):
            if instr.operands:
                for op in instr.operands:
                    addr = None
                    if op.type == X86_OP_MEM and hasattr(op.mem, 'disp'):
                        addr = op.mem.disp
                    elif op.type == X86_OP_IMM:
                        addr = op.imm

                    if addr and addr in all_strings:
                        referenced_strings.append({
                            'address': addr,
                            'string': all_strings[addr]
                        })
    except:
        pass

    return referenced_strings


def scan_code_section(data, sections):
    """Scan CODE section for functions"""
    functions = []

    for section in sections:
        if section['Name'] not in ['CODE', '.text']:
            continue

        print(f"Scanning {section['Name']} section...")

        offset = section['PointerToRawData']
        end = offset + min(section['SizeOfRawData'], 0x50000)  # Limit to first 320KB

        md = Cs(CS_ARCH_X86, CS_MODE_32)

        # Look for function prologues
        i = offset
        while i < end:
            # Check for common prologue: push ebp; mov ebp, esp (55 8B EC)
            if data[i:i+3] == b'\x55\x8B\xEC':
                va = i - offset + section['VirtualAddress'] + 0x00400000
                functions.append(va)
                i += 0x10  # Skip ahead
            else:
                i += 1

            if len(functions) % 100 == 0 and len(functions) > 0:
                print(f"  Found {len(functions)} functions so far...")

    return functions


def main():
    if len(sys.argv) < 2:
        print("Usage: find_loadfromini_functions.py <europeo.exe>")
        sys.exit(1)

    binary_path = sys.argv[1]

    print("="*80)
    print("SMART LOADFROMINI FINDER")
    print("="*80)
    print("\nStrategy: Find functions that reference INI keyword strings")
    print()

    with open(binary_path, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    # Step 1: Find all strings
    print("Step 1: Finding all strings in DATA section...")
    all_strings = find_all_strings_in_data(data, sections)
    print(f"  Found {len(all_strings)} strings total")

    # Filter to INI-related strings
    ini_strings = {addr: s for addr, s in all_strings.items()
                   if any(keyword in s.upper() for keyword in INI_KEYWORDS)}
    print(f"  Found {len(ini_strings)} INI-related strings")

    # Step 2: Find all functions
    print("\nStep 2: Finding all functions...")
    functions = scan_code_section(data, sections)
    print(f"  Found {len(functions)} function candidates")

    # Step 3: Analyze each function for INI strings
    print("\nStep 3: Analyzing functions for INI string references...")
    loadfromini_candidates = []

    for i, func_va in enumerate(functions):
        if i % 100 == 0:
            print(f"  Analyzed {i}/{len(functions)} functions...")

        strings = analyze_function_for_strings(data, sections, func_va, all_strings)
        if strings:
            # Count INI-related strings
            ini_count = sum(1 for s in strings
                           if any(keyword in s['string'].upper() for keyword in INI_KEYWORDS))

            if ini_count >= 3:  # At least 3 INI keywords
                loadfromini_candidates.append({
                    'address': func_va,
                    'ini_strings': ini_count,
                    'all_strings': len(strings),
                    'strings': [s for s in strings if any(keyword in s['string'].upper() for keyword in INI_KEYWORDS)][:10]
                })

    # Sort by number of INI strings
    loadfromini_candidates.sort(key=lambda x: x['ini_strings'], reverse=True)

    # Results
    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)
    print(f"\nFound {len(loadfromini_candidates)} functions with 3+ INI keywords\n")

    # Save to file
    with open("LOADFROMINI_CANDIDATES.md", 'w') as f:
        f.write("# LoadFromINI Function Candidates\n\n")
        f.write(f"**Total candidates**: {len(loadfromini_candidates)}\n\n")
        f.write("Functions with 3+ INI keyword string references.\n\n")
        f.write("---\n\n")

        for i, candidate in enumerate(loadfromini_candidates):  # All candidates
            if i < 50 or i % 10 == 0:  # Print first 50 or every 10th
                print(f"#{i+1}: 0x{candidate['address']:08X} - {candidate['ini_strings']} INI strings")

            f.write(f"## #{i+1}: Function @ 0x{candidate['address']:08X}\n\n")
            f.write(f"**INI Strings**: {candidate['ini_strings']}\n")
            f.write(f"**Total Strings**: {candidate['all_strings']}\n\n")
            f.write("**INI Keywords Found**:\n\n")
            for s in candidate['strings']:
                f.write(f"- `\"{s['string']}\"` @ 0x{s['address']:08X}\n")
            f.write("\n---\n\n")

    print(f"\n✓ Results saved to LOADFROMINI_CANDIDATES.md")
    print("\nTop 10 candidates:")
    for i, candidate in enumerate(loadfromini_candidates[:10]):
        print(f"  {i+1}. 0x{candidate['address']:08X} - {candidate['ini_strings']} INI keywords")


if __name__ == "__main__":
    main()
