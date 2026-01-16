#!/usr/bin/env python3
"""
Find and extract ALL vtables for ALL 35 TVN structures
Searches near type strings to locate actual vtables
"""

import struct

# Type string offsets from VND_CRITICAL_NOTES.md
TVN_TYPE_STRINGS = {
    "TVNProjectParms": 0x0000e20e,
    "TVNMidiParms": 0x0000e22c,
    "TVNDigitParms": 0x0000e247,
    "TVNHtmlParms": 0x0000e263,
    "TVNImageParms": 0x0000e27e,
    "TVNImgObjParms": 0x0000e29a,
    "TVNImgSeqParms": 0x0000e2b7,
    "TVNExecParms": 0x0000e2d4,
    "TVNSetVarParms": 0x0000e2ef,
    "TVNIfParms": 0x0000e30c,
    "TVNTextParms": 0x0000e381,
    "TVNTextObjParms": 0x0000e39c,
    "TVNFontParms": 0x0000e3ba,
    "TVNCommand": 0x0000e3d5,
    "TVNSceneParms": 0x0000e3ee,
    "TVNStringParms": 0x0000e40a,
    "TVNFileNameParms": 0x0000e9da,
    "TVNEventCommand": 0x0000eb2a,
    "TVNVariable": 0x00005e04,
    "TVNScene": 0x00016fbb,
    "TVNHotspot": 0x000135bc,
    "TVNTimer": 0x00019bdf,
    "TVNWaveMedia": 0x0001bb29,
    "TVNMidiMedia": 0x0001bb9c,
    "TVNBitmap": 0x0001dc08,
    "TVNGdiObject": 0x0001dc7f,
    "TVNHtmlText": 0x000227fc,
    "TVNImageObject": 0x00029a17,
    "TVNTextObject": 0x00029a54,
    "TVNBmpImg": 0x00034edb,
    "TVNToolBar": 0x00034f0d,
    "TVNWindow": 0x00034f2d,
    "TVNCDAMedia": 0x00034f45,
    "TVNAviMedia": 0x00034f5f,
    "TVNFrame": 0x0003603c,
    "TVNApplication": 0x00038086,
}


def read_dword(data, offset):
    """Read a DWORD at offset"""
    if offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def is_valid_code_pointer(addr):
    """Check if address is a valid code pointer"""
    return 0x00401000 <= addr <= 0x00500000


def find_vtables_near_string(data, string_offset, struct_name):
    """Find vtables near a type string by scanning backwards and forwards"""

    vtables = []

    # Search ranges: 0x200 bytes before and after the string
    search_ranges = [
        (max(0, string_offset - 0x500), string_offset),  # Before
        (string_offset, min(len(data), string_offset + 0x200))  # After
    ]

    for start, end in search_ranges:
        # Align to 4-byte boundaries
        start = (start // 4) * 4

        for offset in range(start, end, 4):
            ptr = read_dword(data, offset)
            if not ptr or not is_valid_code_pointer(ptr):
                continue

            # Check if this could be the start of a vtable
            # Vtables have multiple consecutive valid code pointers
            methods = []
            current_offset = offset

            for i in range(20):  # Check up to 20 method slots
                method_ptr = read_dword(data, current_offset)
                if not method_ptr:
                    break

                if is_valid_code_pointer(method_ptr):
                    methods.append(method_ptr)
                    current_offset += 4
                elif method_ptr == 0:
                    # NULL pointer = end of vtable
                    break
                else:
                    # Not a code pointer
                    if len(methods) >= 2:  # Valid vtable needs at least 2 methods
                        break
                    else:
                        methods = []
                        break

            if len(methods) >= 2:
                # Found a potential vtable
                vtables.append({
                    'file_offset': offset,
                    'virtual_address': offset + 0x00400000,  # Convert to VA
                    'methods': methods,
                    'distance_from_string': offset - string_offset
                })

    return vtables


def extract_all_vtables(filepath):
    """Extract vtables from all TVN structures"""

    with open(filepath, 'rb') as f:
        data = f.read()

    print("="*100)
    print("FINDING AND EXTRACTING ALL TVN VTABLES")
    print("="*100)
    print()

    all_results = {}

    for struct_name in sorted(TVN_TYPE_STRINGS.keys()):
        string_offset = TVN_TYPE_STRINGS[struct_name]

        print(f"\n{'='*100}")
        print(f"ANALYZING: {struct_name}")
        print(f"Type string @ file offset: 0x{string_offset:08x}")
        print(f"{'='*100}")

        # Find vtables near this string
        vtables = find_vtables_near_string(data, string_offset, struct_name)

        if not vtables:
            print(f"  ⚠️  No vtable found for {struct_name}")
            all_results[struct_name] = {'vtables': []}
            continue

        print(f"  ✓ Found {len(vtables)} potential vtable(s)")

        struct_results = {
            'string_offset': string_offset,
            'vtables': []
        }

        for vtable_idx, vtable in enumerate(vtables):
            print(f"\n  Vtable #{vtable_idx+1}:")
            print(f"    File offset: 0x{vtable['file_offset']:08x}")
            print(f"    Virtual address: 0x{vtable['virtual_address']:08x}")
            print(f"    Distance from string: {vtable['distance_from_string']:+d} bytes")
            print(f"    Methods: {len(vtable['methods'])}")
            print(f"    {'-'*96}")

            vtable_info = {
                'file_offset': vtable['file_offset'],
                'virtual_address': vtable['virtual_address'],
                'methods': []
            }

            for method_idx, method_addr in enumerate(vtable['methods']):
                role = identify_method_role_by_index(method_idx)
                print(f"      [{method_idx:2d}] 0x{method_addr:08x}  {role}")

                vtable_info['methods'].append({
                    'index': method_idx,
                    'address': method_addr,
                    'role': role
                })

            struct_results['vtables'].append(vtable_info)

        all_results[struct_name] = struct_results

    return all_results


def identify_method_role_by_index(method_index):
    """Identify method role based on common vtable patterns"""

    if method_index == 0:
        return "Virtual[0] - Destructor"
    elif method_index == 1:
        return "Virtual[1] - Load/Parse/Init"
    elif method_index == 2:
        return "Virtual[2] - Execute/Process"
    elif method_index == 3:
        return "Virtual[3] - Save/Serialize"
    elif method_index == 4:
        return "Virtual[4] - Clone/Copy"
    elif method_index == 5:
        return "Virtual[5] - Validate"
    else:
        return f"Virtual[{method_index}]"


def save_results_to_markdown(results, output_file):
    """Save extraction results to markdown file"""

    with open(output_file, 'w') as f:
        f.write("# Complete TVN Methods Extraction\n\n")
        f.write("Comprehensive extraction of all vtables and methods from 35 TVN structures.\n\n")
        f.write("**Binary**: DOCS/europeo.exe\n")
        f.write("**Date**: 2026-01-16\n")
        f.write("**Method**: Type string proximity search\n\n")
        f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")
        f.write("| Structure | Vtables Found | Total Methods |\n")
        f.write("|-----------|---------------|---------------|\n")

        total_vtables = 0
        total_methods = 0

        for struct_name in sorted(results.keys()):
            data = results[struct_name]
            vtables = data.get('vtables', [])
            num_vtables = len(vtables)
            num_methods = sum(len(v['methods']) for v in vtables)

            total_vtables += num_vtables
            total_methods += num_methods

            status = "✓" if num_vtables > 0 else "✗"
            f.write(f"| {status} {struct_name:30s} | {num_vtables:2d} | {num_methods:3d} |\n")

        f.write(f"\n**Total**: {total_vtables} vtables, {total_methods} methods\n\n")
        f.write("---\n\n")

        # Detailed results
        f.write("## Detailed Methods\n\n")

        for struct_name in sorted(results.keys()):
            data = results[struct_name]

            if not data.get('vtables'):
                continue

            f.write(f"### {struct_name}\n\n")
            f.write(f"**Type String Offset**: 0x{data['string_offset']:08x}\n\n")

            for vtable_idx, vtable in enumerate(data['vtables']):
                f.write(f"#### Vtable #{vtable_idx+1}\n\n")
                f.write(f"- **File Offset**: 0x{vtable['file_offset']:08x}\n")
                f.write(f"- **Virtual Address**: 0x{vtable['virtual_address']:08x}\n")
                f.write(f"- **Methods**: {len(vtable['methods'])}\n\n")

                f.write("| Index | Address | Role |\n")
                f.write("|-------|---------|------|\n")

                for method in vtable['methods']:
                    f.write(f"| {method['index']:2d} | 0x{method['address']:08x} | {method['role']} |\n")

                f.write("\n")

                # C++ struct
                f.write("```cpp\n")
                f.write(f"struct {struct_name}_vtable_{vtable_idx+1} {{\n")
                for method in vtable['methods']:
                    role_clean = method['role'].replace("Virtual[", "method").replace("]", "").replace(" - ", "_").replace("/", "_").replace(" ", "_")
                    f.write(f"    void* {role_clean}; // [{method['index']:2d}] @ 0x{method['address']:08x}\n")
                f.write("};\n")
                f.write("```\n\n")

            f.write("---\n\n")

    print(f"\n✓ Results saved to {output_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: find_and_extract_vtables.py <europeo.exe> [output.md]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "TVN_ALL_METHODS_COMPLETE.md"

    results = extract_all_vtables(filepath)

    print("\n" + "="*100)
    print("EXTRACTION COMPLETE")
    print("="*100)

    total_vtables = sum(len(r.get('vtables', [])) for r in results.values())
    total_methods = sum(sum(len(v['methods']) for v in r.get('vtables', [])) for r in results.values())

    print(f"\nStructures analyzed: {len(results)}")
    print(f"Total vtables found: {total_vtables}")
    print(f"Total methods found: {total_methods}")

    save_results_to_markdown(results, output_file)
    print("\nDone!")
