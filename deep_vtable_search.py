#!/usr/bin/env python3
"""
Deep search for TVN vtables using multiple strategies:
1. Look for vtable references in code sections
2. Search for constructor patterns
3. Analyze data section for vtable arrays
"""

import struct
import re

# Structures that need vtables found
MISSING_VTABLES = [
    "TVNApplication",
    "TVNAviMedia",
    "TVNBitmap",
    "TVNBmpImg",
    "TVNCDAMedia",
    "TVNEventCommand",
    "TVNFileNameParms",
    "TVNGdiObject",
    "TVNHtmlText",
    "TVNMidiMedia",
    "TVNScene",
    "TVNTimer",
    "TVNToolBar",
    "TVNVariable",
    "TVNWaveMedia",
    "TVNWindow",
]


def read_dword(data, offset):
    """Read DWORD at offset"""
    if offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def is_valid_code_pointer(addr):
    """Check if address is a valid code pointer"""
    return 0x00401000 <= addr <= 0x00500000


def is_valid_data_pointer(addr):
    """Check if address is in data section"""
    return 0x00400000 <= addr <= 0x00500000


def find_constructor_patterns(data):
    """
    Find constructor patterns that initialize vtables
    Pattern: mov dword ptr [ecx], offset vtable
    Opcodes: C7 01 [vtable_addr]
    """

    print("="*100)
    print("SEARCHING FOR CONSTRUCTOR PATTERNS")
    print("="*100)

    # Search for pattern: C7 01 (mov [ecx], imm32)
    pattern = rb'\xC7\x01'

    vtables_found = {}

    for match in re.finditer(pattern, data):
        offset = match.start()

        # Read the immediate value (vtable address)
        vtable_addr = read_dword(data, offset + 2)

        if vtable_addr and is_valid_data_pointer(vtable_addr):
            # Check if this looks like a vtable
            first_ptr = read_dword(data, vtable_addr - 0x00400000)

            if first_ptr and is_valid_code_pointer(first_ptr):
                # Count consecutive code pointers
                consecutive = 0
                test_offset = vtable_addr - 0x00400000

                for i in range(10):
                    ptr = read_dword(data, test_offset + i * 4)
                    if ptr and is_valid_code_pointer(ptr):
                        consecutive += 1
                    elif ptr == 0:
                        break
                    else:
                        break

                if consecutive >= 2:
                    if vtable_addr not in vtables_found:
                        vtables_found[vtable_addr] = {
                            'methods': consecutive,
                            'constructor_at': offset + 0x00400000
                        }

    print(f"\nFound {len(vtables_found)} unique vtables via constructor pattern")

    for vtable_addr in sorted(vtables_found.keys()):
        info = vtables_found[vtable_addr]
        print(f"  Vtable @ 0x{vtable_addr:08X} - {info['methods']} methods - constructor @ 0x{info['constructor_at']:08X}")

    return vtables_found


def find_vtable_arrays(data):
    """
    Find arrays of vtable pointers in data section
    These are often vtable arrays for polymorphic classes
    """

    print("\n" + "="*100)
    print("SEARCHING FOR VTABLE ARRAYS")
    print("="*100)

    vtable_arrays = []

    # Search in data section (roughly 0x40000 - 0x50000 in file)
    search_start = 0x40000
    search_end = min(len(data), 0x50000)

    for offset in range(search_start, search_end, 4):
        # Read potential vtable pointer
        ptr = read_dword(data, offset)

        if not ptr or not is_valid_data_pointer(ptr):
            continue

        # Check if this points to a vtable
        file_offset = ptr - 0x00400000
        if file_offset < 0 or file_offset >= len(data):
            continue

        first_method = read_dword(data, file_offset)

        if first_method and is_valid_code_pointer(first_method):
            # Count consecutive vtable-like pointers
            consecutive_vtables = 0
            current_offset = offset

            for i in range(20):
                vtable_ptr = read_dword(data, current_offset)

                if not vtable_ptr or not is_valid_data_pointer(vtable_ptr):
                    break

                # Check if it points to code
                vtable_file_offset = vtable_ptr - 0x00400000
                if vtable_file_offset < 0 or vtable_file_offset >= len(data):
                    break

                method_ptr = read_dword(data, vtable_file_offset)
                if method_ptr and is_valid_code_pointer(method_ptr):
                    consecutive_vtables += 1
                    current_offset += 4
                else:
                    break

            if consecutive_vtables >= 3:
                vtable_arrays.append({
                    'file_offset': offset,
                    'virtual_address': offset + 0x00400000,
                    'count': consecutive_vtables
                })

    print(f"\nFound {len(vtable_arrays)} vtable arrays")

    for arr in vtable_arrays:
        print(f"  Array @ 0x{arr['virtual_address']:08X} - {arr['count']} vtable pointers")

    return vtable_arrays


def scan_data_section_exhaustive(data):
    """
    Exhaustive scan of data section for ANY vtable-like structure
    """

    print("\n" + "="*100)
    print("EXHAUSTIVE DATA SECTION SCAN")
    print("="*100)

    vtables = {}

    # Scan entire data section
    for offset in range(0, min(len(data), 0x50000), 4):
        ptr = read_dword(data, offset)

        if not ptr or not is_valid_code_pointer(ptr):
            continue

        # This could be the start of a vtable
        methods = []
        current_offset = offset

        for i in range(15):
            method_ptr = read_dword(data, current_offset)

            if method_ptr == 0:
                # NULL - possible end
                if len(methods) >= 2:
                    break
                else:
                    break

            if is_valid_code_pointer(method_ptr):
                methods.append(method_ptr)
                current_offset += 4
            else:
                break

        if len(methods) >= 2:
            va = offset + 0x00400000

            # Only add if not already found
            if va not in vtables:
                vtables[va] = methods

    print(f"\nFound {len(vtables)} potential vtables")

    # Sort by address and show top 50
    sorted_vtables = sorted(vtables.items(), key=lambda x: x[0])

    print("\nTop 50 vtables:")
    for va, methods in sorted_vtables[:50]:
        print(f"  0x{va:08X} - {len(methods)} methods - First: 0x{methods[0]:08X}")

    return vtables


def extract_all_vtables_deep(filepath):
    """Deep extraction using multiple strategies"""

    with open(filepath, 'rb') as f:
        data = f.read()

    print("="*100)
    print("DEEP VTABLE EXTRACTION FOR MISSING STRUCTURES")
    print("="*100)
    print()

    # Strategy 1: Constructor patterns
    constructor_vtables = find_constructor_patterns(data)

    # Strategy 2: Vtable arrays
    vtable_arrays = find_vtable_arrays(data)

    # Strategy 3: Exhaustive scan
    all_vtables = scan_data_section_exhaustive(data)

    return {
        'constructor_vtables': constructor_vtables,
        'vtable_arrays': vtable_arrays,
        'all_vtables': all_vtables
    }


def save_results(results, output_file):
    """Save deep search results"""

    with open(output_file, 'w') as f:
        f.write("# Deep Vtable Search Results\n\n")
        f.write("Multiple search strategies for finding missing TVN vtables.\n\n")
        f.write("---\n\n")

        # Constructor vtables
        f.write("## Constructor Pattern Matches\n\n")
        f.write("Vtables found via `mov [ecx], vtable` pattern in constructors.\n\n")
        f.write("| Vtable Address | Methods | Constructor Location |\n")
        f.write("|----------------|---------|----------------------|\n")

        for vtable_addr in sorted(results['constructor_vtables'].keys()):
            info = results['constructor_vtables'][vtable_addr]
            f.write(f"| 0x{vtable_addr:08X} | {info['methods']:2d} | 0x{info['constructor_at']:08X} |\n")

        f.write(f"\n**Total**: {len(results['constructor_vtables'])} vtables\n\n")
        f.write("---\n\n")

        # Vtable arrays
        f.write("## Vtable Arrays\n\n")
        f.write("Arrays of vtable pointers found in data section.\n\n")
        f.write("| Array Address | Vtable Count |\n")
        f.write("|---------------|-------------|\n")

        for arr in results['vtable_arrays']:
            f.write(f"| 0x{arr['virtual_address']:08X} | {arr['count']:2d} |\n")

        f.write(f"\n**Total**: {len(results['vtable_arrays'])} arrays\n\n")
        f.write("---\n\n")

        # All vtables summary
        f.write("## All Vtables Found (Exhaustive Scan)\n\n")
        f.write("Complete list of all vtable-like structures.\n\n")
        f.write("| Address | Methods | First Method |\n")
        f.write("|---------|---------|-------------|\n")

        sorted_vtables = sorted(results['all_vtables'].items(), key=lambda x: x[0])

        for va, methods in sorted_vtables[:100]:  # Top 100
            f.write(f"| 0x{va:08X} | {len(methods):2d} | 0x{methods[0]:08X} |\n")

        f.write(f"\n**Total**: {len(results['all_vtables'])} vtables (showing top 100)\n\n")

    print(f"\n✓ Results saved to {output_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: deep_vtable_search.py <europeo.exe> [output.md]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "TVN_DEEP_VTABLE_SEARCH.md"

    results = extract_all_vtables_deep(filepath)

    print("\n" + "="*100)
    print("DEEP SEARCH COMPLETE")
    print("="*100)
    print(f"\nConstructor vtables: {len(results['constructor_vtables'])}")
    print(f"Vtable arrays: {len(results['vtable_arrays'])}")
    print(f"Total vtables: {len(results['all_vtables'])}")

    save_results(results, output_file)
    print("\nDone!")
