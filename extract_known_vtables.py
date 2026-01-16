#!/usr/bin/env python3
"""
Extract methods from KNOWN vtable addresses
Based on addresses discovered in TVN_SCENE_LOADER_ANALYSIS.md
"""

import struct

# Known vtable addresses from TVN_SCENE_LOADER_ANALYSIS.md and manual analysis
KNOWN_VTABLES = {
    # TVNSceneParms vtables (from assembly analysis)
    "TVNSceneParms_main": 0x00442DA4,
    "TVNSceneParms_alt": 0x00442D64,
    "TVNSceneParms_sub1": 0x00442D80,
    "TVNSceneParms_sub2": 0x00442D90,
    "TVNSceneParms_internal1": 0x004417C0,
    "TVNSceneParms_internal2": 0x004417D0,
    "TVNSceneParms_internal3": 0x004417A0,
    "TVNSceneParms_array": 0x00441800,

    # Common base vtable (found for many *Parms)
    "TVNCommand_or_Base": 0x0040E1E0,

    # Frame vtables (from extraction)
    "TVNFrame_1": 0x00435B50,
    "TVNFrame_2": 0x00435DD4,

    # ImageObject/TextObject vtables (from extraction)
    "TVNImageObject_1": 0x00429980,
    "TVNImageObject_2": 0x004299D0,

    # Hotspot vtable (from extraction)
    "TVNHotspot": 0x00413514,
}


def read_dword_at_va(data, virtual_addr):
    """Read DWORD at virtual address (convert VA to file offset)"""
    file_offset = virtual_addr - 0x00400000
    if file_offset < 0 or file_offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[file_offset:file_offset+4])[0]


def is_valid_code_pointer(addr):
    """Check if address is a valid code pointer"""
    return 0x00401000 <= addr <= 0x00500000


def extract_vtable_comprehensive(data, vtable_va, vtable_name, max_methods=30):
    """Extract ALL methods from a vtable, being more aggressive"""

    print(f"\n{'='*100}")
    print(f"Extracting: {vtable_name}")
    print(f"Vtable @ 0x{vtable_va:08X}")
    print(f"{'='*100}")

    methods = []
    offset = 0

    while offset < max_methods * 4:  # Check up to max_methods
        method_ptr_addr = vtable_va + offset
        method_ptr = read_dword_at_va(data, method_ptr_addr)

        if method_ptr is None:
            print(f"  [+0x{offset:02X}] Memory read error, ending")
            break

        if method_ptr == 0:
            print(f"  [+0x{offset:02X}] NULL - possible end or gap")
            # Don't break immediately on NULL, might be a gap
            offset += 4
            if offset >= 20 * 4:  # If we've gone far enough, stop
                break
            continue

        if is_valid_code_pointer(method_ptr):
            role = identify_method_role(offset // 4, method_ptr)
            print(f"  [+0x{offset:02X}] 0x{method_ptr:08X}  {role}")

            methods.append({
                'offset': offset,
                'address': method_ptr,
                'role': role
            })
            offset += 4
        else:
            # Not a code pointer
            if len(methods) >= 1:
                # We have at least one method, this might be end of vtable
                print(f"  [+0x{offset:02X}] 0x{method_ptr:08X} - not code, ending")
                break
            else:
                # No methods yet, maybe wrong start address
                print(f"  [+0x{offset:02X}] 0x{method_ptr:08X} - not code")
                break

    print(f"\nTotal methods: {len(methods)}")
    return methods


def identify_method_role(method_index, method_addr):
    """Identify method role"""

    # Check against known function addresses from TVN_SCENE_LOADER_ANALYSIS.md
    if method_addr == 0x00414B2A:
        return "LoadFromINI (from assembly analysis)"
    elif method_addr == 0x00415093:
        return "Constructor (from assembly analysis)"
    elif method_addr == 0x00416FCD:
        return "PreInit scene_obj"
    elif method_addr == 0x00415560:
        return "Configuration AREA"
    elif method_addr == 0x00414A70:
        return "Additional Init AREA"

    # Generic role based on index
    if method_index == 0:
        return "Virtual[0] - Destructor"
    elif method_index == 1:
        return "Virtual[1] - LoadFromINI/Parse"
    elif method_index == 2:
        return "Virtual[2] - Execute/Process"
    elif method_index == 3:
        return "Virtual[3] - Save/Serialize"
    elif method_index == 4:
        return "Virtual[4] - Clone/Copy"
    elif method_index == 5:
        return "Virtual[5] - Validate"
    elif method_index == 6:
        return "Virtual[6] - GetType"
    elif method_index == 7:
        return "Virtual[7] - ToString"
    else:
        return f"Virtual[{method_index}]"


def extract_all_known_vtables(filepath):
    """Extract all known vtables"""

    with open(filepath, 'rb') as f:
        data = f.read()

    print("="*100)
    print("EXTRACTING ALL KNOWN VTABLES")
    print("="*100)

    results = {}

    for vtable_name in sorted(KNOWN_VTABLES.keys()):
        vtable_va = KNOWN_VTABLES[vtable_name]

        methods = extract_vtable_comprehensive(data, vtable_va, vtable_name)

        if methods:
            results[vtable_name] = {
                'virtual_address': vtable_va,
                'methods': methods
            }

    return results


def save_results_to_markdown(results, output_file):
    """Save results to markdown"""

    with open(output_file, 'w') as f:
        f.write("# All TVN Vtables - Known Addresses\n\n")
        f.write("Extraction of all methods from known vtable addresses.\n\n")
        f.write("**Source**: TVN_SCENE_LOADER_ANALYSIS.md + find_and_extract_vtables.py results\n")
        f.write("**Binary**: DOCS/europeo.exe\n")
        f.write("**Date**: 2026-01-16\n\n")
        f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")
        f.write("| Vtable Name | Virtual Address | Methods |\n")
        f.write("|-------------|-----------------|----------|\n")

        total_methods = 0
        for vtable_name in sorted(results.keys()):
            data = results[vtable_name]
            method_count = len(data['methods'])
            total_methods += method_count
            f.write(f"| {vtable_name:40s} | 0x{data['virtual_address']:08X} | {method_count:3d} |\n")

        f.write(f"\n**Total**: {len(results)} vtables, {total_methods} methods\n\n")
        f.write("---\n\n")

        # Detailed methods
        f.write("## Detailed Methods\n\n")

        for vtable_name in sorted(results.keys()):
            data = results[vtable_name]

            f.write(f"### {vtable_name}\n\n")
            f.write(f"**Virtual Address**: 0x{data['virtual_address']:08X}\n")
            f.write(f"**Methods**: {len(data['methods'])}\n\n")

            f.write("| Offset | Address | Role |\n")
            f.write("|--------|---------|------|\n")

            for method in data['methods']:
                f.write(f"| +0x{method['offset']:02X} | 0x{method['address']:08X} | {method['role']} |\n")

            f.write("\n")

            # C++ struct
            f.write("```cpp\n")
            f.write(f"struct {vtable_name}_vtable {{\n")
            for method in data['methods']:
                role_clean = method['role'].replace("Virtual[", "method").replace("]", "").replace(" - ", "_").replace("/", "_").replace(" ", "_").replace("(", "").replace(")", "")
                f.write(f"    void* {role_clean}; // +0x{method['offset']:02X} @ 0x{method['address']:08X}\n")
            f.write("};\n")
            f.write("```\n\n")

            f.write("---\n\n")

    print(f"\n✓ Results saved to {output_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: extract_known_vtables.py <europeo.exe> [output.md]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "TVN_KNOWN_VTABLES_COMPLETE.md"

    results = extract_all_known_vtables(filepath)

    print("\n" + "="*100)
    print("EXTRACTION COMPLETE")
    print("="*100)
    print(f"\nVtables extracted: {len(results)}")
    print(f"Total methods: {sum(len(r['methods']) for r in results.values())}")

    save_results_to_markdown(results, output_file)
    print("\nDone!")
