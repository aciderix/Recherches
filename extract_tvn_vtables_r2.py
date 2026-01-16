#!/usr/bin/env python3
"""
Extract ALL vtables and methods from ALL 35 TVN structures using radare2
"""

import r2pipe
import json

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

# Additional structures - will search for vtables
TVN_STRINGS = [
    "TVNFileNameParms",
    "TVNEventCommand",
    "TVNVariable",
    "TVNScene",
    "TVNHotspot",
    "TVNTimer",
    "TVNWaveMedia",
    "TVNMidiMedia",
    "TVNBitmap",
    "TVNGdiObject",
    "TVNHtmlText",
    "TVNImageObject",
    "TVNTextObject",
    "TVNBmpImg",
    "TVNToolBar",
    "TVNWindow",
    "TVNCDAMedia",
    "TVNAviMedia",
    "TVNFrame",
    "TVNApplication",
]


def is_valid_code_pointer(r2, addr):
    """Check if address is a valid code pointer"""
    if addr < 0x00401000 or addr > 0x00500000:
        return False

    # Check if there's a function at this address
    func_info = r2.cmdj(f"pdfj @ {addr}")
    if func_info and isinstance(func_info, dict):
        return True

    # Check if it's code
    instr = r2.cmdj(f"pdj 1 @ {addr}")
    if instr and len(instr) > 0 and isinstance(instr[0], dict):
        return True

    return False


def extract_vtable_at_offset(r2, vtable_addr, struct_name):
    """Extract all methods from a vtable at given address"""

    print("\n" + "="*100)
    print(f"Extracting vtable for {struct_name} @ 0x{vtable_addr:08X}")
    print("="*100)

    methods = []
    offset = 0

    while offset < 0x100:  # Max 64 methods
        method_ptr_addr = vtable_addr + offset

        # Read pointer value (4 bytes for 32-bit)
        ptr_hex = r2.cmd(f"pv4 @ {method_ptr_addr}").strip()

        try:
            method_ptr = int(ptr_hex, 16) if '0x' in ptr_hex else int(ptr_hex)
        except:
            print(f"  [0x{offset:02X}] Error reading pointer, ending")
            break

        if method_ptr == 0:
            print(f"  [0x{offset:02X}] NULL - end of vtable")
            break

        if not is_valid_code_pointer(r2, method_ptr):
            if offset == 0:
                print(f"  ERROR: First entry is not a valid code pointer!")
                return None
            else:
                print(f"  [0x{offset:02X}] 0x{method_ptr:08X} - invalid, ending")
                break

        # Get function info
        func_info = r2.cmdj(f"pdfj @ {method_ptr}")
        if func_info and isinstance(func_info, dict):
            func_name = func_info.get('name', f"sub_{method_ptr:X}")
            func_size = func_info.get('size', 0)
            role = identify_method_role(func_name, offset // 4, func_size)
        else:
            func_name = f"sub_{method_ptr:X}"
            func_size = 0
            role = "Unknown"

        print(f"  [0x{offset:02X}] 0x{method_ptr:08X}  {func_name:30s}  {role:25s}  size={func_size}")

        methods.append({
            'offset': offset,
            'address': method_ptr,
            'name': func_name,
            'role': role,
            'size': func_size
        })

        offset += 4

    print(f"\nTotal methods found: {len(methods)}")
    return methods


def identify_method_role(func_name, method_index, func_size):
    """Try to identify method role"""

    name_lower = func_name.lower()

    # Name-based detection
    if "destructor" in name_lower or "dtor" in name_lower:
        return "Destructor"
    if "constructor" in name_lower or "ctor" in name_lower:
        return "Constructor"
    if "load" in name_lower:
        return "Load/Parse"
    if "save" in name_lower:
        return "Save/Serialize"
    if "execute" in name_lower or "exec" in name_lower:
        return "Execute"
    if "release" in name_lower or "free" in name_lower:
        return "Release/Cleanup"
    if "init" in name_lower:
        return "Initialize"
    if "parse" in name_lower:
        return "Parse"
    if "clone" in name_lower or "copy" in name_lower:
        return "Clone/Copy"

    # Index-based detection
    if method_index == 0:
        return "Virtual[0] - Likely Destructor"
    elif method_index == 1:
        return "Virtual[1]"

    # Size-based detection
    if func_size > 0:
        if func_size < 10:
            return "Getter/Setter"
        elif func_size > 500:
            return "Complex Logic"

    return f"Method[{method_index}]"


def find_vtable_near_string(r2, struct_name):
    """Try to find vtable by searching near type string"""

    search_str = struct_name + " *"

    # Search for string
    results = r2.cmd(f"/j {search_str}")

    try:
        locations = json.loads(results) if results.strip() else []
    except:
        locations = []

    if not locations:
        print(f"  Warning: String '{search_str}' not found for {struct_name}")
        return None

    string_addr = locations[0]['offset']
    print(f"  Found type string at 0x{string_addr:08X}")

    # Search backwards for vtable (up to 0x200 bytes)
    for i in range(0, 0x200, 4):
        check_addr = string_addr - i

        # Read first pointer
        ptr_hex = r2.cmd(f"pv4 @ {check_addr}").strip()

        try:
            first_ptr = int(ptr_hex, 16) if '0x' in ptr_hex else int(ptr_hex)
        except:
            continue

        if is_valid_code_pointer(r2, first_ptr):
            # Check for consecutive code pointers
            consecutive = 1
            for j in range(1, 10):
                next_addr = check_addr + j * 4
                next_hex = r2.cmd(f"pv4 @ {next_addr}").strip()

                try:
                    next_ptr = int(next_hex, 16) if '0x' in next_hex else int(next_hex)
                except:
                    break

                if is_valid_code_pointer(r2, next_ptr):
                    consecutive += 1
                else:
                    break

            if consecutive >= 3:
                print(f"  Possible vtable found at 0x{check_addr:08X} ({consecutive} methods)")
                return check_addr

    return None


def extract_all_vtables(filepath):
    """Extract vtables from all known TVN structures"""

    print("="*100)
    print("EXTRACTING ALL TVN VTABLES AND METHODS - RADARE2 ANALYSIS")
    print("="*100)
    print()

    # Open binary with radare2
    r2 = r2pipe.open(filepath)

    # Analyze binary
    print("Analyzing binary...")
    r2.cmd("aaa")  # Analyze all
    print("Analysis complete.\n")

    results = {}

    # Phase 1: Known vtable offsets
    print("\n" + "="*100)
    print("PHASE 1: Known Vtable Offsets")
    print("="*100)

    for struct_name in sorted(TVN_VTABLES.keys()):
        vtable_addr = TVN_VTABLES[struct_name]

        methods = extract_vtable_at_offset(r2, vtable_addr, struct_name)

        if methods:
            results[struct_name] = {
                'vtable_address': vtable_addr,
                'methods': methods
            }

    # Phase 2: Search for additional vtables
    print("\n" + "="*100)
    print("PHASE 2: Searching for Additional Vtables")
    print("="*100)

    for struct_name in sorted(TVN_STRINGS):
        print(f"\nSearching for {struct_name}...")
        vtable_addr = find_vtable_near_string(r2, struct_name)

        if vtable_addr:
            methods = extract_vtable_at_offset(r2, vtable_addr, struct_name)

            if methods:
                results[struct_name] = {
                    'vtable_address': vtable_addr,
                    'methods': methods
                }
        else:
            print(f"  Could not locate vtable for {struct_name}")

    # Close radare2
    r2.quit()

    return results


def save_results_to_markdown(results, output_file):
    """Save extraction results to markdown file"""

    with open(output_file, 'w') as f:
        f.write("# Complete TVN Methods Extraction - Radare2 Analysis\n\n")
        f.write("Comprehensive extraction of all vtables and methods from 35 TVN structures.\n\n")
        f.write("**Tool**: radare2 5.5.0\n")
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

            f.write("| Offset | Address | Function | Role | Size |\n")
            f.write("|--------|---------|----------|------|------|\n")

            for method in data['methods']:
                f.write(f"| +0x{method['offset']:02X} | 0x{method['address']:08X} | {method['name']:30s} | {method['role']:25s} | {method['size']:5d} |\n")

            f.write("\n---\n\n")

    print(f"\n✓ Results saved to {output_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: extract_tvn_vtables_r2.py <europeo.exe> [output.md]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "TVN_ALL_METHODS_R2.md"

    results = extract_all_vtables(filepath)

    print("\n" + "="*100)
    print("EXTRACTION COMPLETE")
    print("="*100)
    print(f"\nExtracted {len(results)} structures")
    print(f"Total methods: {sum(len(r['methods']) for r in results.values())}")

    save_results_to_markdown(results, output_file)
    print("\nDone!")
