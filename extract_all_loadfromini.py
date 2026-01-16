#!/usr/bin/env python3
"""
Extract all LoadFromINI candidates with complete assembly and DATA context
This script processes the 180 identified LoadFromINI functions
"""

import struct
import re
from capstone import *
from capstone.x86 import *
import sys
from collections import defaultdict

# INI keywords that identify specific TVN structure types
TVN_STRUCTURE_KEYWORDS = {
    'TVNScene': ['SCENE', 'AREA_', 'HOTSPOT_'],
    'TVNHotspot': ['HOTSPOT_', 'COMMAND', 'CURSOR'],
    'TVNArea': ['AREA_', 'BKCOLOR', 'TEXTURE'],
    'TVNTextObject': ['TEXT', 'FONT', 'COLOR', 'SIZE'],
    'TVNImageObject': ['IMAGE', 'BITMAP', 'POSITION'],
    'TVNSound': ['SOUND', 'MUSIC', 'VOLUME'],
    'TVNCommand': ['COMMAND', 'ACTION', 'EVENT'],
    'TVNFont': ['FONT', 'CAPS', 'HEIGHT'],
    'TVNVideo': ['VIDEO', 'FRAME', 'SPEED'],
}


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


def read_string(data, offset, max_len=128):
    """Read a null-terminated string"""
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


def find_function_end_with_padding(data, sections, start_va, max_size=0x2000):
    """
    FIX #2: Find function end by detecting padding or next function prologue
    """
    offset = va_to_file_offset(start_va, sections)
    if offset is None:
        return start_va + max_size

    last_ret_addr = start_va

    md = Cs(CS_ARCH_X86, CS_MODE_32)
    code_bytes = data[offset:offset + max_size]

    for instr in md.disasm(code_bytes, start_va):
        # Track last RET instruction
        if instr.mnemonic in ['ret', 'retn']:
            last_ret_addr = instr.address + instr.size

        # Check bytes after this instruction
        next_offset = instr.address + instr.size - start_va
        if next_offset + 3 < len(code_bytes):
            next_bytes = code_bytes[next_offset:next_offset+4]

            # Padding detection (0xCC or 0x90)
            if len(next_bytes) >= 2:
                if next_bytes[0] in [0xCC, 0x90] and next_bytes[1] in [0xCC, 0x90]:
                    return last_ret_addr

            # Next function prologue (55 8B EC = push ebp; mov ebp, esp)
            if len(next_bytes) >= 3:
                if next_bytes[0:3] == b'\x55\x8B\xEC':
                    return last_ret_addr

    return start_va + max_size


def extract_function_with_calls(data, sections, func_va, all_strings, visited=None, depth=0, max_depth=2):
    """
    FIX #3: Extract function with recursive CALL following
    """
    if visited is None:
        visited = set()

    if func_va in visited or depth > max_depth:
        return [], [], []

    visited.add(func_va)

    offset = va_to_file_offset(func_va, sections)
    if offset is None:
        return [], [], []

    # Find function end
    func_end = find_function_end_with_padding(data, sections, func_va)
    size = func_end - func_va

    code_bytes = data[offset:offset + size]

    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    instructions = []
    strings_found = []
    calls_found = []

    try:
        for instr in md.disasm(code_bytes, func_va):
            instructions.append({
                'address': instr.address,
                'mnemonic': instr.mnemonic,
                'op_str': instr.op_str,
                'bytes': instr.bytes
            })

            # Track CALL instructions
            if instr.mnemonic == 'call' and instr.operands:
                for op in instr.operands:
                    if op.type == X86_OP_IMM:
                        calls_found.append(op.imm)

            # Track string references
            if instr.operands:
                for op in instr.operands:
                    addr = None
                    if op.type == X86_OP_MEM and hasattr(op.mem, 'disp'):
                        addr = op.mem.disp
                    elif op.type == X86_OP_IMM:
                        addr = op.imm

                    if addr and addr in all_strings:
                        strings_found.append({
                            'address': addr,
                            'string': all_strings[addr],
                            'from_func': func_va
                        })
    except:
        pass

    # Recursively follow CALLs
    if depth < max_depth:
        for call_target in calls_found[:5]:  # Limit to first 5 calls
            sub_instr, sub_strings, _ = extract_function_with_calls(
                data, sections, call_target, all_strings, visited, depth + 1, max_depth
            )
            strings_found.extend(sub_strings)

    return instructions, strings_found, calls_found


def extract_data_context(data, sections, string_addr, context_size=128):
    """
    FIX #4: Extract DATA context around a string
    """
    offset = va_to_file_offset(string_addr, sections)
    if offset is None:
        return []

    context_strings = []

    # Scan ±context_size bytes
    start_offset = max(0, offset - context_size)
    end_offset = min(len(data), offset + context_size)

    i = start_offset
    while i < end_offset:
        string = read_string(data, i)
        if string and len(string) >= 3:
            va = None
            # Find VA for this offset
            for section in sections:
                sec_start = section['PointerToRawData']
                sec_end = sec_start + section['SizeOfRawData']
                if sec_start <= i < sec_end:
                    va = i - sec_start + section['VirtualAddress'] + 0x00400000
                    break

            if va:
                context_strings.append({
                    'address': va,
                    'string': string
                })
            i += len(string) + 1
        else:
            i += 1

    return context_strings


def parse_loadfromini_candidates(md_file):
    """Parse LOADFROMINI_CANDIDATES.md to get function addresses"""
    candidates = []

    with open(md_file, 'r') as f:
        content = f.read()

    # Regex to find function entries
    pattern = r'## #(\d+): Function @ (0x[0-9A-F]+)\s+\*\*INI Strings\*\*: (\d+)'

    for match in re.finditer(pattern, content, re.IGNORECASE):
        rank = int(match.group(1))
        address = int(match.group(2), 16)
        ini_count = int(match.group(3))

        candidates.append({
            'rank': rank,
            'address': address,
            'ini_count': ini_count
        })

    return candidates


def identify_tvn_structure(strings_found):
    """
    Try to identify which TVN structure this function belongs to
    based on the strings it references
    """
    string_text = ' '.join([s['string'].upper() for s in strings_found])

    scores = {}
    for struct_name, keywords in TVN_STRUCTURE_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in string_text)
        if score > 0:
            scores[struct_name] = score

    if scores:
        best_match = max(scores.items(), key=lambda x: x[1])
        return best_match[0], best_match[1]

    return 'Unknown', 0


def generate_markdown(func_data, output_file):
    """Generate markdown output for a function"""
    with open(output_file, 'w') as f:
        f.write(f"# LoadFromINI Function Analysis\n\n")
        f.write(f"**Function Address**: 0x{func_data['address']:08X}\n")
        f.write(f"**Rank**: #{func_data['rank']}\n")
        f.write(f"**INI String Count**: {func_data['ini_count']}\n")
        f.write(f"**Identified Structure**: {func_data['identified_struct']}\n")
        f.write(f"**Confidence Score**: {func_data['confidence_score']}\n\n")
        f.write("---\n\n")

        # Assembly code
        f.write("## Assembly Code\n\n")
        f.write(f"**Instructions**: {len(func_data['instructions'])}\n\n")
        f.write("```assembly\n")
        for instr in func_data['instructions'][:500]:  # Limit to 500 instructions
            f.write(f"{instr['address']:08X}  {instr['mnemonic']:8s} {instr['op_str']}\n")
        if len(func_data['instructions']) > 500:
            f.write(f"... ({len(func_data['instructions']) - 500} more instructions)\n")
        f.write("```\n\n")

        # Strings referenced
        f.write("## Strings Referenced\n\n")
        unique_strings = {}
        for s in func_data['strings']:
            unique_strings[s['address']] = s['string']

        f.write(f"**Total unique strings**: {len(unique_strings)}\n\n")
        for addr, string in sorted(unique_strings.items())[:100]:  # Limit to 100
            f.write(f"- `\"{string}\"` @ 0x{addr:08X}\n")
        if len(unique_strings) > 100:
            f.write(f"\n... and {len(unique_strings) - 100} more strings\n")
        f.write("\n")

        # DATA context for key strings
        if func_data['data_contexts']:
            f.write("## DATA Context\n\n")
            for ctx in func_data['data_contexts'][:10]:  # Limit to 10 contexts
                f.write(f"**Context around 0x{ctx['center_addr']:08X}**:\n\n")
                for s in ctx['strings'][:20]:  # Limit to 20 strings per context
                    f.write(f"- `\"{s['string']}\"` @ 0x{s['address']:08X}\n")
                f.write("\n")

        # Called functions
        if func_data['calls']:
            f.write("## Functions Called\n\n")
            for call_addr in func_data['calls'][:50]:  # Limit to 50
                f.write(f"- 0x{call_addr:08X}\n")
            if len(func_data['calls']) > 50:
                f.write(f"\n... and {len(func_data['calls']) - 50} more calls\n")

        f.write("\n---\n\n")
        f.write("*Extracted with recursive CALL following and DATA context*\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: extract_all_loadfromini.py <europeo.exe>")
        sys.exit(1)

    binary_path = sys.argv[1]
    candidates_file = "LOADFROMINI_CANDIDATES.md"

    print("="*80)
    print("COMPLETE LOADFROMINI EXTRACTION")
    print("="*80)
    print()

    # Load binary
    print("Loading binary...")
    with open(binary_path, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)
    print(f"✓ Parsed {len(sections)} sections")

    # Find all strings
    print("\nFinding all strings...")
    all_strings = find_all_strings_in_data(data, sections)
    print(f"✓ Found {len(all_strings)} strings")

    # Parse candidates
    print("\nParsing LoadFromINI candidates...")
    candidates = parse_loadfromini_candidates(candidates_file)
    print(f"✓ Found {len(candidates)} candidates")

    # Extract top 50 candidates
    print("\nExtracting top 50 candidates...")
    print()

    structure_groups = defaultdict(list)

    for i, candidate in enumerate(candidates[:50]):
        print(f"[{i+1}/50] Extracting 0x{candidate['address']:08X}...")

        # Extract function
        instructions, strings_found, calls_found = extract_function_with_calls(
            data, sections, candidate['address'], all_strings
        )

        # Identify TVN structure
        identified_struct, confidence = identify_tvn_structure(strings_found)

        # Extract DATA context for unique strings
        data_contexts = []
        unique_string_addrs = list(set([s['address'] for s in strings_found]))
        for string_addr in unique_string_addrs[:10]:  # Context for first 10 unique strings
            context = extract_data_context(data, sections, string_addr)
            if context:
                data_contexts.append({
                    'center_addr': string_addr,
                    'strings': context
                })

        func_data = {
            'rank': candidate['rank'],
            'address': candidate['address'],
            'ini_count': candidate['ini_count'],
            'instructions': instructions,
            'strings': strings_found,
            'calls': calls_found,
            'data_contexts': data_contexts,
            'identified_struct': identified_struct,
            'confidence_score': confidence
        }

        # Save to file
        output_file = f"LOADFROMINI_EXTRACTED/func_{candidate['rank']:03d}_0x{candidate['address']:08X}_{identified_struct}.md"
        generate_markdown(func_data, output_file)

        structure_groups[identified_struct].append(func_data)

        print(f"  → {identified_struct} (score: {confidence})")
        print(f"  → {len(instructions)} instructions, {len(set([s['address'] for s in strings_found]))} unique strings")

    # Generate summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print()

    for struct_name in sorted(structure_groups.keys()):
        funcs = structure_groups[struct_name]
        print(f"{struct_name}: {len(funcs)} functions")
        for func in funcs:
            print(f"  - 0x{func['address']:08X} (rank #{func['rank']})")

    print(f"\n✓ Extracted {len(candidates[:50])} functions")
    print(f"✓ Output directory: LOADFROMINI_EXTRACTED/")
    print()


if __name__ == "__main__":
    main()
