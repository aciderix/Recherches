#!/usr/bin/env python3
"""
IDAPython script to extract ALL vtables and methods from ALL 35 TVN structures
This script should be run inside IDA: File -> Script file... -> select this file
Or via command line: idat64 -A -S"extract_tvn_vtables_ida.py" europeo.exe
"""

import idc
import idaapi
import idautils

# All 35 TVN structures with their known offsets from VND_CRITICAL_NOTES.md and extract_all_tvn_methods.py
TVN_STRUCTURES = {
    # Parms structures (from VND_CRITICAL_NOTES.md)
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

# Additional structures found in extract_all_tvn_methods.py (string offsets, need to find vtables)
ADDITIONAL_STRUCTURES = {
    "TVNFileNameParms": None,
    "TVNEventCommand": None,
    "TVNVariable": None,
    "TVNScene": None,
    "TVNHotspot": None,
    "TVNTimer": None,
    "TVNWaveMedia": None,
    "TVNMidiMedia": None,
    "TVNBitmap": None,
    "TVNGdiObject": None,
    "TVNHtmlText": None,
    "TVNImageObject": None,
    "TVNTextObject": None,
    "TVNBmpImg": None,
    "TVNToolBar": None,
    "TVNWindow": None,
    "TVNCDAMedia": None,
    "TVNAviMedia": None,
    "TVNFrame": None,
    "TVNApplication": None,
}


def is_valid_code_pointer(addr):
    """Check if address is a valid code pointer"""
    if addr < 0x00401000 or addr > 0x00500000:
        return False

    # Check if it's in a code segment
    seg = idaapi.getseg(addr)
    if not seg:
        return False

    # Check if segment is executable
    if not (seg.perm & idaapi.SEGPERM_EXEC):
        return False

    return True


def extract_vtable_at_offset(vtable_addr, struct_name):
    """Extract all methods from a vtable at given address"""

    print(f"\n{'='*100}")
    print(f"Extracting vtable for {struct_name} @ 0x{vtable_addr:08X}")
    print(f"{'='*100}")

    methods = []
    offset = 0

    while offset < 0x100:  # Max 64 methods (safety limit)
        method_ptr_addr = vtable_addr + offset
        method_ptr = idc.get_wide_dword(method_ptr_addr)

        if method_ptr == 0:
            # NULL pointer - might be end of vtable or padding
            print(f"  [{offset:02X}] NULL - end of vtable")
            break

        if not is_valid_code_pointer(method_ptr):
            # Not a valid code pointer
            if offset == 0:
                print(f"  ERROR: First entry is not a valid code pointer!")
                return None
            else:
                print(f"  [{offset:02X}] 0x{method_ptr:08X} - invalid code pointer, ending")
                break

        # Get function name
        func_name = idc.get_func_name(method_ptr)
        if not func_name:
            func_name = f"sub_{method_ptr:X}"

        # Try to get decompiled code preview
        func = idaapi.get_func(method_ptr)
        func_info = ""

        if func:
            # Get function size
            func_size = func.end_ea - func.start_ea
            func_info = f"size={func_size}"

            # Try to identify method role based on function characteristics
            role = identify_method_role(method_ptr, offset // 4, func_name, func)
        else:
            role = "Unknown"

        print(f"  [{offset:02X}] 0x{method_ptr:08X}  {func_name:30s}  {role:25s}  {func_info}")

        methods.append({
            'offset': offset,
            'address': method_ptr,
            'name': func_name,
            'role': role
        })

        offset += 4

    print(f"\nTotal methods found: {len(methods)}")

    return methods


def identify_method_role(method_addr, method_index, func_name, func):
    """Try to identify the role of a method based on various heuristics"""

    # Common method name patterns
    if "destructor" in func_name.lower() or "dtor" in func_name.lower():
        return "Destructor"
    if "constructor" in func_name.lower() or "ctor" in func_name.lower():
        return "Constructor"
    if "load" in func_name.lower():
        return "Load/Parse"
    if "save" in func_name.lower():
        return "Save/Serialize"
    if "execute" in func_name.lower() or "exec" in func_name.lower():
        return "Execute"
    if "release" in func_name.lower() or "free" in func_name.lower():
        return "Release/Cleanup"
    if "init" in func_name.lower():
        return "Initialize"
    if "parse" in func_name.lower():
        return "Parse"
    if "clone" in func_name.lower() or "copy" in func_name.lower():
        return "Clone/Copy"
    if "validate" in func_name.lower():
        return "Validate"

    # Check by method index (common vtable layout)
    if method_index == 0:
        return "Virtual[0] - Likely Destructor"
    elif method_index == 1:
        return "Virtual[1]"
    elif method_index == 2:
        return "Virtual[2]"

    # Check function characteristics
    if func:
        # Very small functions (< 10 bytes) are often simple getters/setters
        func_size = func.end_ea - func.start_ea
        if func_size < 10:
            return "Getter/Setter"

        # Large functions (> 500 bytes) are often main logic
        if func_size > 500:
            return "Complex Logic"

    return f"Method[{method_index}]"


def find_vtable_near_string(struct_name):
    """Try to find vtable by searching near the type string"""

    # Search for the struct name string
    search_str = struct_name + " *"

    # Find all occurrences
    addr = idc.find_text(0, idc.SEARCH_DOWN, 0, 0, search_str)

    if addr == idc.BADADDR:
        print(f"  Warning: String '{search_str}' not found for {struct_name}")
        return None

    print(f"  Found type string at 0x{addr:08X}")

    # Search backwards for potential vtable (up to 0x200 bytes)
    for offset in range(0x200):
        check_addr = addr - offset

        # Align to 4-byte boundary
        if check_addr % 4 != 0:
            continue

        # Check if this could be start of vtable
        first_ptr = idc.get_wide_dword(check_addr)

        if is_valid_code_pointer(first_ptr):
            # Check if we have at least 3 consecutive valid code pointers
            consecutive = 1
            for i in range(1, 10):
                next_ptr = idc.get_wide_dword(check_addr + i * 4)
                if is_valid_code_pointer(next_ptr):
                    consecutive += 1
                else:
                    break

            if consecutive >= 3:
                print(f"  Possible vtable found at 0x{check_addr:08X} ({consecutive} methods)")
                return check_addr

    return None


def extract_all_vtables():
    """Extract vtables from all known TVN structures"""

    print("="*100)
    print("EXTRACTING ALL TVN VTABLES AND METHODS - IDA ANALYSIS")
    print("="*100)
    print()

    results = {}

    # First, extract vtables from known offsets
    print("\n" + "="*100)
    print("PHASE 1: Known Vtable Offsets")
    print("="*100)

    for struct_name, vtable_addr in sorted(TVN_STRUCTURES.items(), key=lambda x: x[1]):
        if vtable_addr is None:
            continue

        methods = extract_vtable_at_offset(vtable_addr, struct_name)

        if methods:
            results[struct_name] = {
                'vtable_address': vtable_addr,
                'methods': methods
            }

    # Second, try to find vtables for additional structures
    print("\n" + "="*100)
    print("PHASE 2: Searching for Additional Vtables")
    print("="*100)

    for struct_name in sorted(ADDITIONAL_STRUCTURES.keys()):
        print(f"\nSearching for {struct_name}...")
        vtable_addr = find_vtable_near_string(struct_name)

        if vtable_addr:
            methods = extract_vtable_at_offset(vtable_addr, struct_name)

            if methods:
                results[struct_name] = {
                    'vtable_address': vtable_addr,
                    'methods': methods
                }
        else:
            print(f"  Could not locate vtable for {struct_name}")

    return results


def save_results_to_markdown(results, output_file):
    """Save extraction results to markdown file"""

    with open(output_file, 'w') as f:
        f.write("# Complete TVN Methods Extraction - IDA Analysis\n\n")
        f.write("Comprehensive extraction of all vtables and methods from 35 TVN structures.\n\n")
        f.write("**Tool**: IDA Free 8.4\n")
        f.write("**Binary**: DOCS/europeo.exe\n")
        f.write("**Date**: 2026-01-16\n\n")
        f.write("---\n\n")

        # Summary table
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

        # Detailed extraction
        f.write("## Detailed Methods\n\n")

        for struct_name in sorted(results.keys()):
            data = results[struct_name]

            f.write(f"### {struct_name}\n\n")
            f.write(f"**Vtable**: 0x{data['vtable_address']:08X}\n\n")

            f.write("| Offset | Address | Function | Role |\n")
            f.write("|--------|---------|----------|------|\n")

            for method in data['methods']:
                f.write(f"| +0x{method['offset']:02X} | 0x{method['address']:08X} | {method['name']:30s} | {method['role']} |\n")

            f.write("\n---\n\n")

    print(f"\n✓ Results saved to {output_file}")


def main():
    """Main extraction function"""

    # Wait for auto-analysis to complete
    print("Waiting for IDA auto-analysis to complete...")
    idaapi.auto_wait()
    print("Analysis complete.\n")

    # Extract all vtables
    results = extract_all_vtables()

    # Save results
    output_file = idc.get_idb_path().replace('.idb', '_TVN_METHODS_IDA.md').replace('.i64', '_TVN_METHODS_IDA.md')
    save_results_to_markdown(results, output_file)

    print("\n" + "="*100)
    print("EXTRACTION COMPLETE")
    print("="*100)
    print(f"\nExtracted {len(results)} structures")
    print(f"Total methods: {sum(len(r['methods']) for r in results.values())}")
    print(f"\nResults saved to: {output_file}")

    # Exit IDA
    idc.qexit(0)


if __name__ == "__main__":
    main()
