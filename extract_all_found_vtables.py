#!/usr/bin/env python3
"""
Extract ALL vtables found by deep search and create complete documentation
"""

import struct

# All vtables from deep search (extended list - top 200)
ALL_FOUND_VTABLES = [
    0x00400730, 0x00402928, 0x0040E1E0, 0x00413514, 0x0041A0B8, 0x0041A0BC,
    0x0041A0C0, 0x0041BFC8, 0x0041DECC, 0x00425BE0, 0x00429980, 0x004299D0,
    0x00435B50, 0x00435DD4, 0x0043902C, 0x00439030, 0x00439034, 0x00439044,
    0x00439048, 0x00439130, 0x00439154, 0x004391A0, 0x004391E0, 0x00439274,
    0x00439308, 0x00439478, 0x004394D4, 0x00439514, 0x00439554, 0x00439594,
    0x004395D4, 0x00439614, 0x004396A8, 0x004396E8, 0x0043970C, 0x00439768,
    0x004397E0, 0x00439820, 0x00439860, 0x00439914, 0x00439954, 0x00439A08,
    0x00439AA0, 0x00439AC4, 0x00439AF4, 0x00439B18, 0x00439B3C, 0x00439B60,
    0x00439C30, 0x00439CB0,
]

# Known associations from previous work
KNOWN_ASSOCIATIONS = {
    0x0040E1E0: "TVNCommand/Base (shared by many *Parms)",
    0x00413514: "TVNHotspot",
    0x00429980: "TVNImageObject_1",
    0x004299D0: "TVNImageObject_2 / TVNTextObject_1",
    0x00435B50: "TVNFrame_1",
    0x00435DD4: "TVNFrame_2",
    0x004394D4: "TVNTimer",
    0x00449668: "Unknown (from constructor pattern)",
}


def read_dword(data, offset):
    """Read DWORD at offset"""
    if offset < 0 or offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def is_valid_code_pointer(addr):
    """Check if address is a valid code pointer"""
    return 0x00401000 <= addr <= 0x00500000


def extract_vtable_complete(data, vtable_va, max_methods=15):
    """Extract all methods from a vtable"""

    file_offset = vtable_va - 0x00400000
    methods = []

    for i in range(max_methods):
        offset = file_offset + i * 4
        method_ptr = read_dword(data, offset)

        if method_ptr == 0:
            # NULL pointer - might be end or gap
            if len(methods) >= 2:
                break
            continue

        if is_valid_code_pointer(method_ptr):
            methods.append({
                'index': i,
                'address': method_ptr,
                'offset': i * 4
            })
        else:
            # Not code - end of vtable
            if len(methods) >= 1:
                break

    return methods


def extract_all_vtables(filepath, vtable_list):
    """Extract all vtables from list"""

    with open(filepath, 'rb') as f:
        data = f.read()

    print("="*100)
    print("EXTRACTING ALL FOUND VTABLES")
    print("="*100)

    results = []

    for vtable_va in vtable_list:
        methods = extract_vtable_complete(data, vtable_va)

        if methods:
            association = KNOWN_ASSOCIATIONS.get(vtable_va, "Unknown")

            result = {
                'vtable_va': vtable_va,
                'association': association,
                'methods': methods
            }

            results.append(result)

            print(f"0x{vtable_va:08X} - {len(methods):2d} methods - {association}")

    return results


def save_all_vtables(results, output_file):
    """Save all vtables to comprehensive document"""

    with open(output_file, 'w') as f:
        f.write("# All Extracted Vtables - Complete Reference\n\n")
        f.write("Complete extraction of all vtables found in europeo.exe.\n\n")
        f.write("**Total Vtables**: {}\n".format(len(results)))
        f.write("**Date**: 2026-01-16\n\n")
        f.write("---\n\n")

        # Summary table
        f.write("## Summary\n\n")
        f.write("| # | Vtable Address | Methods | Association |\n")
        f.write("|---|----------------|---------|-------------|\n")

        total_methods = 0
        for i, vtable in enumerate(results, 1):
            total_methods += len(vtable['methods'])
            f.write(f"| {i:3d} | 0x{vtable['vtable_va']:08X} | {len(vtable['methods']):2d} | {vtable['association']} |\n")

        f.write(f"\n**Total Methods**: {total_methods}\n\n")
        f.write("---\n\n")

        # Detailed listings
        f.write("## Detailed Vtables\n\n")

        for i, vtable in enumerate(results, 1):
            f.write(f"### Vtable #{i}: 0x{vtable['vtable_va']:08X}\n\n")
            f.write(f"**Association**: {vtable['association']}\n")
            f.write(f"**Methods**: {len(vtable['methods'])}\n\n")

            f.write("| Index | Offset | Address |\n")
            f.write("|-------|--------|----------|\n")

            for method in vtable['methods']:
                f.write(f"| {method['index']:2d} | +0x{method['offset']:02X} | 0x{method['address']:08X} |\n")

            f.write("\n")

            # C++ structure
            f.write("```cpp\n")
            assoc_clean = vtable['association'].replace("/", "_").replace(" ", "_").replace("(", "").replace(")", "")
            f.write(f"// {vtable['association']}\n")
            f.write(f"struct vtable_0x{vtable['vtable_va']:08X} {{\n")
            for method in vtable['methods']:
                f.write(f"    void* method_{method['index']}; // +0x{method['offset']:02X} @ 0x{method['address']:08X}\n")
            f.write("};\n")
            f.write("```\n\n")

            f.write("---\n\n")

    print(f"\n✓ Saved to {output_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: extract_all_found_vtables.py <europeo.exe> [output.md]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "TVN_ALL_VTABLES_COMPREHENSIVE.md"

    print(f"\nExtracting {len(ALL_FOUND_VTABLES)} vtables...\n")

    results = extract_all_vtables(filepath, ALL_FOUND_VTABLES)

    print("\n" + "="*100)
    print("EXTRACTION COMPLETE")
    print("="*100)
    print(f"\nVtables extracted: {len(results)}")
    print(f"Total methods: {sum(len(v['methods']) for v in results)}")

    save_all_vtables(results, output_file)
    print("\nDone!")
