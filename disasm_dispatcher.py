#!/usr/bin/env python3
"""
Désassemble sub_43177D (répartiteur VND) avec capstone
"""

import struct
import sys

try:
    from capstone import *
except ImportError:
    print("Capstone not installed. Using hexdump only.")
    Cs = None

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

def main():
    binary = "DOCS/europeo.exe"

    # Load binary
    with open(binary, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    # Target: sub_43177D (Dispatcher)
    target_va = 0x0043177D
    target_size = 2000  # 2KB should be enough

    print("="*80)
    print(f"DÉSASSEMBLAGE sub_43177D @ 0x{target_va:08X}")
    print("="*80)
    print()

    offset = va_to_file_offset(target_va, sections)
    if not offset:
        print("✗ Adresse invalide")
        return

    print(f"File offset: 0x{offset:08X}\n")

    code = data[offset:offset+target_size]

    if Cs:
        # Use capstone if available
        md = Cs(CS_ARCH_X86, CS_MODE_32)
        md.detail = True

        print("Assembly:")
        print("-"*80)

        for i, insn in enumerate(md.disasm(code, target_va)):
            print(f"{insn.address:08x}:  {insn.mnemonic:8s} {insn.op_str}")

            # Stop at ret
            if insn.mnemonic == 'ret':
                print(f"\n✓ Function end at 0x{insn.address:08X}")
                print(f"  Function size: {insn.address - target_va + 1} bytes")
                break

            # Safety: stop after 500 instructions
            if i > 500:
                print("\n⚠ Stopped after 500 instructions")
                break
    else:
        # Fallback: hexdump
        print("Hexdump (first 512 bytes):")
        print("-"*80)
        for i in range(0, min(512, len(code)), 16):
            chunk = code[i:i+16]
            hex_str = ' '.join(f'{b:02x}' for b in chunk)
            ascii_str = ''.join(chr(b) if 0x20 <= b <= 0x7E else '.' for b in chunk)
            print(f"{target_va + i:08x}:  {hex_str:48s}  {ascii_str}")

if __name__ == "__main__":
    main()
