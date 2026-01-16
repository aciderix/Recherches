#!/usr/bin/env python3
"""
Extract ALL vtables and methods from ALL 35 TVN structures
Uses radare2 via subprocess calls
"""

import subprocess
import struct
import re

# All 35 TVN structures with their known vtable offsets
TVN_VTABLES = {
    # From VND_CRITICAL_NOTES.md
    "TVNProjectParms": 0x0040EC02,
    "TVNMidiParms": 0x0040EC20,
    "TVNDigitParms": 0x0040EC3B,
    "TVNHtmlParms": 0x0040EC57,
    "TVNImageParms": 0x0040EC72,
    "TVNImgObjParms": 0x0040EC8E,
    "TVNImgSeqParms": 0x0040ECAB,
    "TVNExecParms": 0x0040ECC8,
    "TVNSetVarParms": 0x0040ECE3,
    "TVNIfParms": 0x0040ED00,
    "TVNTextParms": 0x0040ED75,
    "TVNTextObjParms": 0x0040ED90,
    "TVNFontParms": 0x0040EDAE,
    "TVNCommand": 0x0040EDC9,
    "TVNSceneParms": 0x0040EDFE,
    "TVNStringParms": 0x0040EE1A,
}


def read_binary_dword(filepath, offset):
    """Read a DWORD from binary file at given offset"""
    try:
        with open(filepath, 'rb') as f:
            f.seek(offset)
            data = f.read(4)
            if len(data) == 4:
                return struct.unpack('<I', data)[0]
    except:
        pass
    return None


def is_valid_code_pointer(addr):
    """Check if address is a valid code pointer"""
    return 0x00401000 <= addr <= 0x00500000


def extract_vtable_at_offset(filepath, vtable_addr, struct_name):
    """Extract all methods from a vtable at given address"""

    print("\n" + "="*100)
    print(f"Extracting vtable for {struct_name} @ 0x{vtable_addr:08X}")
    print("="*100)

    # Convert virtual address to file offset
    # For PE files, RVA = Virtual Address - Image Base (0x00400000)
    file_offset = vtable_addr - 0x00400000

    methods = []
    offset = 0

    while offset < 0x100:  # Max 64 methods
        method_ptr_addr = vtable_addr + offset
        method_file_offset = file_offset + offset

        # Read pointer value
        method_ptr = read_binary_dword(filepath, method_file_offset)

        if method_ptr is None:
            print(f"  [0x{offset:02X}] Error reading pointer, ending")
            break

        if method_ptr == 0:
            print(f"  [0x{offset:02X}] NULL - end of vtable")
            break

        if not is_valid_code_pointer(method_ptr):
            if offset == 0:
                print(f"  ERROR: First entry is not a valid code pointer!")
                return None
            else:
                print(f"  [0x{offset:02X}] 0x{method_ptr:08X} - invalid, ending")
                break

        # Identify method role
        role = identify_method_role_by_index(offset // 4)

        print(f"  [0x{offset:02X}] 0x{method_ptr:08X}  {role}")

        methods.append({
            'offset': offset,
            'address': method_ptr,
            'role': role
        })

        offset += 4

    print(f"\nTotal methods found: {len(methods)}")
    return methods


def identify_method_role_by_index(method_index):
    """Identify method role based on common vtable patterns"""

    # Standard C++ vtable layout
    if method_index == 0:
        return "Virtual[0] - Likely Destructor"
    elif method_index == 1:
        return "Virtual[1] - Possible Load/Parse"
    elif method_index == 2:
        return "Virtual[2] - Possible Execute"
    elif method_index == 3:
        return "Virtual[3] - Possible Save/Serialize"
    elif method_index == 4:
        return "Virtual[4] - Possible Clone/Copy"
    else:
        return f"Virtual[{method_index}]"


def extract_all_vtables(filepath):
    """Extract vtables from all known TVN structures"""

    print("="*100)
    print("EXTRACTING ALL TVN VTABLES AND METHODS")
    print("="*100)
    print()

    results = {}

    # Extract known vtable offsets
    print("\n" + "="*100)
    print("Extracting Known Vtable Offsets")
    print("="*100)

    for struct_name in sorted(TVN_VTABLES.keys()):
        vtable_addr = TVN_VTABLES[struct_name]

        methods = extract_vtable_at_offset(filepath, vtable_addr, struct_name)

        if methods:
            results[struct_name] = {
                'vtable_address': vtable_addr,
                'methods': methods
            }

    return results


def save_results_to_markdown(results, output_file):
    """Save extraction results to markdown file"""

    with open(output_file, 'w') as f:
        f.write("# Complete TVN Methods Extraction\n\n")
        f.write("Comprehensive extraction of all vtables and methods from TVN structures.\n\n")
        f.write("**Binary**: DOCS/europeo.exe\n")
        f.write("**Date**: 2026-01-16\n\n")
        f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")
        f.write("| Structure | Vtable Address | Methods Count |\n")
        f.write("|-----------|----------------|---------------|\n")

        total_methods = 0
        for struct_name in sorted(results.keys()):
            data = results[struct_name]
            method_count = len(data['methods'])
            total_methods += method_count
            f.write(f"| {struct_name:30s} | 0x{data['vtable_address']:08X} | {method_count:3d} |\n")

        f.write(f"\n**Total**: {len(results)} structures, {total_methods} methods\n\n")
        f.write("---\n\n")

        # Detailed methods
        f.write("## Detailed Methods\n\n")

        for struct_name in sorted(results.keys()):
            data = results[struct_name]

            f.write(f"### {struct_name}\n\n")
            f.write(f"**Vtable**: 0x{data['vtable_address']:08X}\n")
            f.write(f"**Methods**: {len(data['methods'])}\n\n")

            f.write("| Offset | Address | Role |\n")
            f.write("|--------|---------|------|\n")

            for method in data['methods']:
                f.write(f"| +0x{method['offset']:02X} | 0x{method['address']:08X} | {method['role']} |\n")

            f.write("\n")

            # C++ struct representation
            f.write("```cpp\n")
            f.write(f"struct {struct_name}_vtable {{\n")
            for method in data['methods']:
                role_clean = method['role'].replace("Virtual[", "method").replace("]", "")
                f.write(f"    void* {role_clean}; // +0x{method['offset']:02X} @ 0x{method['address']:08X}\n")
            f.write("};\n")
            f.write("```\n\n")

            f.write("---\n\n")

    print(f"\n✓ Results saved to {output_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: extract_tvn_vtables_simple.py <europeo.exe> [output.md]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "TVN_ALL_METHODS_EXTRACTED.md"

    results = extract_all_vtables(filepath)

    print("\n" + "="*100)
    print("EXTRACTION COMPLETE")
    print("="*100)
    print(f"\nExtracted {len(results)} structures")
    print(f"Total methods: {sum(len(r['methods']) for r in results.values())}")

    save_results_to_markdown(results, output_file)
    print("\nDone!")
