#!/usr/bin/env python3
"""
FINAL TVN Extractor with ALL expert fixes applied

Fixes:
✓ #1: RTTI vs VTable - Using correct TYPEINFO addresses
✓ #2: Function end detection with padding (0xCC, 0x90)
✓ #3: Recursive CALL following (depth 2-3)
✓ #4: DATA context extraction (±128 bytes)
✓ #5: Parent class from RTTI
✓ #6: Correct Borland RTTI offsets (discovered via analysis)

RTTI Structure (Borland C++):
+0x00: Type ID (0x04)
+0x04: Flags/Parent pointer
+0x08: Destructor function pointer
+0x0C: Class name string (inline)
"""

import struct
from capstone import *
from capstone.x86 import *
import sys
import os

# TYPEINFO addresses from CSV (verified valid)
TYPEINFO_ADDRESSES = {
    # Verified structures
    "TVNScene": 0x004179AE,
    "TVNImageObject": 0x0042A40B,
    "TVNTextObject": 0x0042A448,

    # From CSV - to verify
    "TVNProjectParms": 0x0040DCC2,
    "TVNMidiParms": 0x0040DCF6,
    "TVNDigitParms": 0x0040DD28,
    "TVNHtmlParms": 0x0040DD5A,
    "TVNImageParms": 0x0040DD8D,
    "TVNImgObjParms": 0x0040DDC2,
    "TVNImgSeqParms": 0x0040DDF7,
    "TVNExecParms": 0x0040DE2D,
    "TVNSetVarParms": 0x0040DE5F,
    "TVNIfParms": 0x0040DE94,
    "TVNTextParms": 0x0040DEC4,
    "TVNTextObjParms": 0x0040DEF8,
    "TVNFontParms": 0x0040DF2F,
    "TVNCommand": 0x0040EDC9,
    "TVNSceneParms": 0x0040EDE2,
    "TVNStringParms": 0x0040EDFF,
    "TVNFrame_1": 0x00435B50,
    "TVNFrame_2": 0x00435DD4,
    "TVNHotspot": 0x00413514,
    "TVNTimer": 0x004394D4,
}

# FIX #6: Correct Borland RTTI offsets (discovered)
RTTI_OFFSET_TYPE_ID = 0x00
RTTI_OFFSET_PARENT = 0x04
RTTI_OFFSET_DESTRUCTOR = 0x08
RTTI_OFFSET_NAME = 0x0C


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


def read_dword(data, offset):
    if offset < 0 or offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


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


def is_valid_code_pointer(addr):
    return 0x00401000 <= addr <= 0x00500000


def is_valid_data_pointer(addr):
    return 0x00400000 <= addr <= 0x00500000


def parse_rtti_borland(data, sections, typeinfo_va):
    """
    FIX #6: Parse Borland RTTI with correct offsets

    Structure:
    +0x00: Type ID (0x04)
    +0x04: Flags/Parent pointer
    +0x08: Destructor
    +0x0C: Name string (inline)
    """
    offset = va_to_file_offset(typeinfo_va, sections)
    if offset is None:
        return None

    type_id = read_dword(data, offset + RTTI_OFFSET_TYPE_ID)
    parent_or_flags = read_dword(data, offset + RTTI_OFFSET_PARENT)
    destructor = read_dword(data, offset + RTTI_OFFSET_DESTRUCTOR)
    name = read_string(data, offset + RTTI_OFFSET_NAME)

    # Validate
    if not name or 'TVN' not in name:
        return None
    if not is_valid_code_pointer(destructor):
        return None

    # Try to parse parent if it's a valid pointer
    parent_name = None
    if parent_or_flags and is_valid_data_pointer(parent_or_flags):
        parent_offset = va_to_file_offset(parent_or_flags, sections)
        if parent_offset:
            parent_name = read_string(data, parent_offset + RTTI_OFFSET_NAME)

    return {
        'typeinfo_va': typeinfo_va,
        'type_id': type_id,
        'parent_ptr': parent_or_flags,
        'parent_name': parent_name,
        'destructor': destructor,
        'name': name
    }


def find_function_end_with_padding(data, sections, start_va, max_size=0x2000):
    """
    FIX #2: Proper function end detection with padding
    """
    start_offset = va_to_file_offset(start_va, sections)
    if start_offset is None:
        return start_va + 0x100

    code_bytes = data[start_offset:start_offset + max_size]

    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    last_ret_addr = None
    instructions = list(md.disasm(code_bytes, start_va))

    for i, instr in enumerate(instructions):
        if instr.mnemonic in ['ret', 'retn']:
            last_ret_addr = instr.address + instr.size

            # Check for padding
            next_offset = va_to_file_offset(last_ret_addr, sections)
            if next_offset and next_offset + 4 < len(data):
                next_bytes = data[next_offset:next_offset+4]

                # Padding (0xCC or 0x90)
                if next_bytes[0] in [0xCC, 0x90] and next_bytes[1] in [0xCC, 0x90]:
                    return last_ret_addr

                # Next function prologue
                if next_bytes[0:3] == b'\x55\x8B\xEC':
                    return last_ret_addr

    return last_ret_addr if last_ret_addr else (start_va + 0x100)


def disassemble_with_recursion(data, sections, func_va, depth=0, max_depth=2, visited=None):
    """
    FIX #3: Recursive CALL following
    """
    if visited is None:
        visited = set()

    if func_va in visited or depth > max_depth:
        return {'instructions': [], 'strings': [], 'data_refs': [], 'called_functions': []}

    visited.add(func_va)

    func_offset = va_to_file_offset(func_va, sections)
    if func_offset is None:
        return {'instructions': [], 'strings': [], 'data_refs': [], 'called_functions': []}

    # FIX #2: Find proper end
    end_va = find_function_end_with_padding(data, sections, func_va)
    func_size = min(end_va - func_va, 0x2000)

    code_bytes = data[func_offset:func_offset + func_size]

    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True

    instructions = []
    data_refs = []
    string_refs = []
    called_functions = []

    for instr in md.disasm(code_bytes, func_va):
        instructions.append({
            'address': instr.address,
            'mnemonic': instr.mnemonic,
            'op_str': instr.op_str,
            'bytes': instr.bytes
        })

        # FIX #3: Recursive CALL
        if instr.mnemonic == 'call' and instr.operands:
            if instr.operands[0].type == X86_OP_IMM:
                target = instr.operands[0].imm
                if 0x00401000 <= target <= 0x00500000:
                    called_functions.append(target)

                    if depth < max_depth:
                        sub_result = disassemble_with_recursion(
                            data, sections, target, depth + 1, max_depth, visited
                        )
                        string_refs.extend(sub_result['strings'])
                        data_refs.extend(sub_result['data_refs'])

        # Extract data refs
        if instr.operands:
            for op in instr.operands:
                if op.type == X86_OP_MEM and hasattr(op.mem, 'disp'):
                    addr = op.mem.disp
                    if 0x00400000 <= addr <= 0x00500000:
                        data_refs.append(addr)
                        string = read_string(data, va_to_file_offset(addr, sections) or 0)
                        if string:
                            string_refs.append({'address': addr, 'value': string})
                elif op.type == X86_OP_IMM:
                    addr = op.imm
                    if 0x00400000 <= addr <= 0x00500000 and addr not in called_functions:
                        data_refs.append(addr)
                        string = read_string(data, va_to_file_offset(addr, sections) or 0)
                        if string:
                            string_refs.append({'address': addr, 'value': string})

    return {
        'instructions': instructions,
        'strings': string_refs,
        'data_refs': list(set(data_refs)),
        'called_functions': called_functions,
        'size': func_size
    }


def extract_data_context(data, sections, addr, context_size=128):
    """
    FIX #4: DATA context extraction (±128 bytes)
    """
    offset = va_to_file_offset(addr, sections)
    if offset is None:
        return None

    start = max(0, offset - context_size)
    end = min(len(data), offset + context_size)
    context_bytes = data[start:end]

    strings_in_context = []
    i = 0
    while i < len(context_bytes):
        if 32 <= context_bytes[i] <= 126:
            string = []
            j = i
            while j < len(context_bytes) and context_bytes[j] != 0:
                if 32 <= context_bytes[j] <= 126:
                    string.append(chr(context_bytes[j]))
                    j += 1
                else:
                    break

            if len(string) >= 3 and j < len(context_bytes) and context_bytes[j] == 0:
                string_addr = addr - (offset - start) + i
                strings_in_context.append({
                    'address': string_addr,
                    'value': ''.join(string)
                })
                i = j + 1
            else:
                i += 1
        else:
            i += 1

    return {
        'start_va': addr - (offset - start),
        'end_va': addr + (end - offset),
        'strings': strings_in_context
    }


def extract_structure_complete(data, sections, struct_name, typeinfo_va):
    """Complete extraction with ALL fixes"""
    print(f"\n{'='*80}")
    print(f"EXTRACTING: {struct_name}")
    print(f"TYPEINFO: 0x{typeinfo_va:08X}")
    print(f"{'='*80}")

    # FIX #1 & #6: Parse RTTI correctly
    rtti_info = parse_rtti_borland(data, sections, typeinfo_va)
    if not rtti_info:
        print(f"  ⚠️  Could not parse RTTI")
        return None

    print(f"  Class name: {rtti_info['name']}")
    print(f"  Destructor: 0x{rtti_info['destructor']:08X}")

    # FIX #5: Show parent
    if rtti_info['parent_name']:
        print(f"  Parent: {rtti_info['parent_name']}")

    # Disassemble destructor with recursion
    print(f"  Disassembling destructor...")
    func_data = disassemble_with_recursion(data, sections, rtti_info['destructor'], depth=0, max_depth=2)

    print(f"     Instructions: {len(func_data['instructions'])}")
    print(f"     Strings: {len(func_data['strings'])}")
    print(f"     Called functions: {len(func_data['called_functions'])}")

    # FIX #4: Extract context for each string
    contexts = []
    for string_ref in func_data['strings']:
        context = extract_data_context(data, sections, string_ref['address'])
        if context:
            contexts.append(context)
            print(f"        Context @ 0x{string_ref['address']:08X}: {len(context['strings'])} neighbors")

    result = {
        'struct_name': struct_name,
        'typeinfo_va': typeinfo_va,
        'rtti_info': rtti_info,
        'destructor_analysis': func_data,
        'data_contexts': contexts
    }

    print(f"  ✓ Complete")
    return result


def save_to_markdown(result, output_dir):
    """Save complete extraction to markdown"""
    if not result:
        return

    filename = os.path.join(output_dir, f"{result['struct_name']}_COMPLETE.md")

    with open(filename, 'w') as f:
        f.write(f"# {result['struct_name']} - Complete Extraction\n\n")
        f.write(f"**Structure**: {result['struct_name']}\n")
        f.write(f"**TYPEINFO Address**: 0x{result['typeinfo_va']:08X}\n")
        f.write(f"**Class Name**: {result['rtti_info']['name']}\n")

        # FIX #5: Parent
        if result['rtti_info']['parent_name']:
            f.write(f"**Parent Class**: {result['rtti_info']['parent_name']}\n")

        f.write(f"**Destructor**: 0x{result['rtti_info']['destructor']:08X}\n")
        f.write("\n---\n\n")

        # Destructor analysis
        func = result['destructor_analysis']
        f.write("## Destructor Analysis\n\n")
        f.write(f"**Function**: 0x{result['rtti_info']['destructor']:08X}\n")
        f.write(f"**Instructions**: {len(func['instructions'])}\n")
        f.write(f"**Size**: {func['size']} bytes\n\n")

        # Assembly (limited to first 100 instructions)
        f.write("### Assembly Code\n\n```assembly\n")
        for instr in func['instructions'][:100]:
            f.write(f"{instr['address']:08X}  {instr['mnemonic']:8s} {instr['op_str']}\n")
        if len(func['instructions']) > 100:
            f.write(f"... ({len(func['instructions']) - 100} more instructions)\n")
        f.write("```\n\n")

        # FIX #3: Strings (including from called functions)
        if func['strings']:
            f.write("### Strings Referenced\n\n")
            for s in func['strings']:
                f.write(f"- `\"{s['value']}\"` @ 0x{s['address']:08X}\n")
            f.write("\n")

        # FIX #3: Called functions
        if func['called_functions']:
            f.write("### Functions Called\n\n")
            for cf in func['called_functions']:
                f.write(f"- 0x{cf:08X}\n")
            f.write("\n")

        # FIX #4: DATA contexts
        if result['data_contexts']:
            f.write("### DATA Context (Neighbor Strings)\n\n")
            for ctx in result['data_contexts']:
                f.write(f"**Context 0x{ctx['start_va']:08X} - 0x{ctx['end_va']:08X}**:\n\n")
                for s in ctx['strings']:
                    f.write(f"- `\"{s['value']}\"` @ 0x{s['address']:08X}\n")
                f.write("\n")

        f.write("---\n\n")
        f.write("*Extracted with all expert fixes (#1-#6)*\n")

    print(f"  ✓ Saved: {filename}")


def main():
    if len(sys.argv) < 2:
        print("Usage: extract_tvn_FINAL.py <europeo.exe>")
        sys.exit(1)

    binary_path = sys.argv[1]
    output_dir = "TVN_EXTRACTED_FINAL"

    print("="*80)
    print("TVN EXTRACTOR - FINAL VERSION")
    print("="*80)
    print("\nAll expert fixes applied:")
    print("  ✓ #1: RTTI vs VTable - Using TYPEINFO addresses")
    print("  ✓ #2: Function end detection (padding)")
    print("  ✓ #3: Recursive CALL following (depth 2)")
    print("  ✓ #4: DATA context (±128 bytes)")
    print("  ✓ #5: Parent class extraction")
    print("  ✓ #6: Correct Borland RTTI offsets")
    print()

    os.makedirs(output_dir, exist_ok=True)

    with open(binary_path, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    # Extract structures
    success_count = 0
    for struct_name, typeinfo_va in TYPEINFO_ADDRESSES.items():
        result = extract_structure_complete(data, sections, struct_name, typeinfo_va)
        if result:
            save_to_markdown(result, output_dir)
            success_count += 1

    print("\n" + "="*80)
    print("EXTRACTION COMPLETE")
    print("="*80)
    print(f"\nTotal structures: {len(TYPEINFO_ADDRESSES)}")
    print(f"Successfully extracted: {success_count}")
    print(f"Output directory: {output_dir}/")
    print("\n✓ Done!")


if __name__ == "__main__":
    main()
