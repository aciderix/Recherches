#!/usr/bin/env python3
"""
Extract all TVN structure information from europeo.exe
Finds type info strings, vtables, and methods
"""

import struct
import re
from collections import defaultdict


def read_dword(data, offset):
    """Read a DWORD (uint32) at offset"""
    if offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def find_string(data, s):
    """Find all occurrences of a string in data"""
    s_bytes = s.encode('ascii') + b'\x00'
    offsets = []
    start = 0
    while True:
        pos = data.find(s_bytes, start)
        if pos == -1:
            break
        offsets.append(pos)
        start = pos + 1
    return offsets


def find_tvn_structures(filepath):
    """Find all TVN structures and their information"""

    with open(filepath, 'rb') as f:
        data = f.read()

    print("=" * 80)
    print("TVN STRUCTURES EXTRACTION")
    print("=" * 80)
    print()

    # List of all TVN Parms structures
    parms_structures = [
        "TVNProjectParms",
        "TVNMidiParms",
        "TVNDigitParms",
        "TVNHtmlParms",
        "TVNImageParms",
        "TVNImgObjParms",
        "TVNImgSeqParms",
        "TVNExecParms",
        "TVNSetVarParms",
        "TVNIfParms",
        "TVNTextParms",
        "TVNFontParms",
        "TVNSceneParms",
        "TVNStringParms",
        "TVNTextObjParms",
        "TVNCommandParms",
        "TVNConditionParms",
        "TVNDecVarParms",
        "TVNIncVarParms",
        "TVNFileNameParms",
        "TVNHotspotParms",
        "TVNCDAParms",
        "TVNRectParms",
        "TVNTimeParms",
    ]

    # Other TVN classes
    other_structures = [
        "TVNCommand",
        "TVNEventCommand",
        "TVNVariable",
        "TVNScene",
        "TVNHotspot",
        "TVNGdiObject",
        "TVNAviMedia",
        "TVNWaveMedia",
        "TVNMidiMedia",
        "TVNCDAMedia",
        "TVNBitmap",
        "TVNBmpImg",
        "TVNImageObject",
        "TVNTextObject",
        "TVNHtmlText",
        "TVNFrame",
        "TVNWindow",
        "TVNApplication",
        "TVNTimer",
        "TVNToolBar",
    ]

    all_structures = parms_structures + other_structures

    results = {}

    for struct_name in all_structures:
        # Search for the struct name as a string (with pointer marker " *")
        search_str = struct_name + " *"
        offsets = find_string(data, search_str)

        if offsets:
            results[struct_name] = {
                'name': struct_name,
                'string_offsets': offsets,
                'is_parms': struct_name in parms_structures
            }

    # Sort by first offset
    sorted_structs = sorted(results.items(), key=lambda x: x[1]['string_offsets'][0])

    print(f"Found {len(results)} TVN structures in binary\n")
    print("-" * 80)

    for struct_name, info in sorted_structs:
        offset_hex = f"0x{info['string_offsets'][0]:08x}"
        struct_type = "PARMS" if info['is_parms'] else "CLASS"

        print(f"{struct_name:30s}  @ {offset_hex:12s}  [{struct_type}]")

        # Try to find vtable references near this offset
        # Look for patterns like: dd offset <structure_name>
        for str_offset in info['string_offsets'][:1]:  # Just check first occurrence
            # Search backwards for potential vtable
            search_start = max(0, str_offset - 0x100)
            search_end = str_offset

            # Look for pointer patterns (common in vtables)
            # Vtables often have pointers in range 0x00400000-0x00500000 for this exe
            for i in range(search_start, search_end, 4):
                val = read_dword(data, i)
                if val and 0x00400000 <= val < 0x00500000:
                    # Could be a vtable pointer
                    # Check if there are multiple consecutive pointers
                    consecutive = 1
                    for j in range(1, 10):
                        next_val = read_dword(data, i + j*4)
                        if next_val and 0x00400000 <= next_val < 0x00500000:
                            consecutive += 1
                        else:
                            break

                    if consecutive >= 3:  # Likely a vtable
                        print(f"    Possible vtable @ 0x{i:08x} ({consecutive} method pointers)")
                        # Print first few methods
                        for k in range(min(consecutive, 5)):
                            method_ptr = read_dword(data, i + k*4)
                            print(f"      [+{k*4:02x}] 0x{method_ptr:08x}")
                        if consecutive > 5:
                            print(f"      ... (+{consecutive-5} more)")
                        break

    print()
    print("-" * 80)
    print(f"\nTotal structures found: {len(results)}")
    print(f"  - Parms structures: {sum(1 for s in results.values() if s['is_parms'])}")
    print(f"  - Other classes: {sum(1 for s in results.values() if not s['is_parms'])}")

    return results


def find_command_dispatch(data):
    """Try to find the command dispatch/switch table"""

    print("\n" + "=" * 80)
    print("SEARCHING FOR COMMAND DISPATCH LOGIC")
    print("=" * 80)
    print()

    # Search for strings that indicate command names
    command_names = [
        "playavi",
        "playwav",
        "runprj",
        "set_var",
        "inc_var",
        "dec_var",
        "addbmp",
        "delbmp",
        "scene",
        "if",
        "then",
        "else",
    ]

    found_commands = {}

    for cmd in command_names:
        offsets = find_string(data, cmd)
        if offsets:
            found_commands[cmd] = offsets
            print(f"'{cmd}' found at: {', '.join(f'0x{o:08x}' for o in offsets[:5])}")
            if len(offsets) > 5:
                print(f"    ... (+{len(offsets)-5} more)")

    return found_commands


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: extract_tvn_structures.py <europeo.exe>")
        sys.exit(1)

    filepath = sys.argv[1]

    # Find all TVN structures
    structures = find_tvn_structures(filepath)

    # Try to find command dispatch logic
    with open(filepath, 'rb') as f:
        data = f.read()
    commands = find_command_dispatch(data)
