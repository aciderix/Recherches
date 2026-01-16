#!/usr/bin/env python3
"""
Correlate found vtables to missing TVN structures
by searching for type string references near vtable usage
"""

import struct
import re

# Structures that need vtables
MISSING_STRUCTURES = {
    "TVNApplication": 0x00038086,
    "TVNAviMedia": 0x00034f5f,
    "TVNBitmap": 0x0001dc08,
    "TVNBmpImg": 0x00034edb,
    "TVNCDAMedia": 0x00034f45,
    "TVNEventCommand": 0x0000eb2a,
    "TVNFileNameParms": 0x0000e9da,
    "TVNGdiObject": 0x0001dc7f,
    "TVNHtmlText": 0x000227fc,
    "TVNMidiMedia": 0x0001bb9c,
    "TVNScene": 0x00016fbb,
    "TVNTimer": 0x00019bdf,
    "TVNToolBar": 0x00034f0d,
    "TVNVariable": 0x00005e04,
    "TVNWaveMedia": 0x0001bb29,
    "TVNWindow": 0x00034f2d,
}

# Known vtables from deep search (top candidates)
CANDIDATE_VTABLES = [
    0x00400730,
    0x00402928,
    0x0041A0B8,
    0x0041A0BC,
    0x0041A0C0,
    0x0041BFC8,
    0x0041DECC,
    0x00425BE0,
    0x0043902C,
    0x00439030,
    0x00439034,
    0x00439044,
    0x00439048,
    0x00439130,
    0x00439154,
    0x004391A0,
    0x004391E0,
    0x00439274,
    0x00439308,
    0x00439478,
    0x004394D4,
    0x00439514,
    0x00439554,
    0x00439594,
    0x004395D4,
    0x00439614,
    0x004396A8,
    0x004396E8,
    0x0043970C,
    0x00439768,
    0x004397E0,
    0x00439820,
    0x00439860,
    0x00439914,
    0x00439954,
    0x00439A08,
    0x00439AA0,
    0x00439AC4,
    0x00439AF4,
    0x00439B18,
    0x00439B3C,
    0x00439B60,
    0x00439C30,
    0x00439CB0,
]


def read_dword(data, offset):
    """Read DWORD at offset"""
    if offset < 0 or offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def is_valid_code_pointer(addr):
    """Check if address is a valid code pointer"""
    return 0x00401000 <= addr <= 0x00500000


def search_vtable_references(data, vtable_va):
    """
    Search for references to a vtable address in code
    Pattern: mov reg, offset vtable_addr
    """

    # Convert VA to bytes (little endian)
    vtable_bytes = struct.pack('<I', vtable_va)

    references = []

    # Search for the vtable address as an immediate value
    for match in re.finditer(re.escape(vtable_bytes), data):
        offset = match.start()

        # Check if it's in code section (roughly)
        if offset < 0x1000 or offset > 0x80000:
            continue

        # This is a potential reference
        references.append(offset)

    return references


def extract_vtable_methods(data, vtable_va, max_methods=10):
    """Extract methods from a vtable"""

    file_offset = vtable_va - 0x00400000
    methods = []

    for i in range(max_methods):
        method_ptr = read_dword(data, file_offset + i * 4)

        if method_ptr == 0:
            break

        if is_valid_code_pointer(method_ptr):
            methods.append(method_ptr)
        else:
            break

    return methods


def correlate_structure_to_vtable(data, struct_name, string_offset, candidate_vtables):
    """
    Try to correlate a structure to vtables by finding which vtable
    is referenced near the structure's type string
    """

    print(f"\n{'='*100}")
    print(f"ANALYZING: {struct_name}")
    print(f"Type string @ 0x{string_offset:08x}")
    print(f"{'='*100}")

    # For each candidate vtable, check if it's referenced near this structure
    correlations = []

    for vtable_va in candidate_vtables:
        # Search for references to this vtable
        refs = search_vtable_references(data, vtable_va)

        if not refs:
            continue

        # Calculate distances from references to type string
        for ref_offset in refs:
            distance = abs(ref_offset - string_offset)

            # If reference is close to type string (within 5KB)
            if distance < 5000:
                methods = extract_vtable_methods(data, vtable_va)

                correlations.append({
                    'vtable_va': vtable_va,
                    'reference_offset': ref_offset,
                    'distance': distance,
                    'methods': methods
                })

    if correlations:
        # Sort by distance (closest first)
        correlations.sort(key=lambda x: x['distance'])

        print(f"\n✓ Found {len(correlations)} potential vtable correlation(s)")

        for i, corr in enumerate(correlations[:5]):  # Top 5
            print(f"\n  Correlation #{i+1}:")
            print(f"    Vtable VA:    0x{corr['vtable_va']:08X}")
            print(f"    Ref offset:   0x{corr['reference_offset']:08x}")
            print(f"    Distance:     {corr['distance']} bytes")
            print(f"    Methods:      {len(corr['methods'])}")

            for j, method in enumerate(corr['methods'][:5]):
                print(f"      [{j}] 0x{method:08X}")

        return correlations[0]  # Return closest match

    else:
        print(f"\n✗ No vtable correlations found")
        return None


def correlate_all_structures(filepath):
    """Correlate all missing structures to vtables"""

    with open(filepath, 'rb') as f:
        data = f.read()

    print("="*100)
    print("CORRELATING MISSING STRUCTURES TO VTABLES")
    print("="*100)

    results = {}

    for struct_name in sorted(MISSING_STRUCTURES.keys()):
        string_offset = MISSING_STRUCTURES[struct_name]

        correlation = correlate_structure_to_vtable(
            data, struct_name, string_offset, CANDIDATE_VTABLES
        )

        if correlation:
            results[struct_name] = correlation

    return results


def save_correlation_results(results, output_file):
    """Save correlation results"""

    with open(output_file, 'w') as f:
        f.write("# Vtable Correlation Results\n\n")
        f.write("Vtables correlated to missing TVN structures via reference proximity.\n\n")
        f.write("---\n\n")

        f.write("## Summary\n\n")
        f.write("| Structure | Vtable Address | Methods | Distance |\n")
        f.write("|-----------|----------------|---------|----------|\n")

        for struct_name in sorted(results.keys()):
            corr = results[struct_name]
            f.write(f"| {struct_name:20s} | 0x{corr['vtable_va']:08X} | {len(corr['methods']):2d} | {corr['distance']:5d} bytes |\n")

        f.write(f"\n**Total**: {len(results)} structures matched\n\n")
        f.write("---\n\n")

        f.write("## Detailed Correlations\n\n")

        for struct_name in sorted(results.keys()):
            corr = results[struct_name]

            f.write(f"### {struct_name}\n\n")
            f.write(f"- **Vtable**: 0x{corr['vtable_va']:08X}\n")
            f.write(f"- **Reference**: 0x{corr['reference_offset']:08x} (distance: {corr['distance']} bytes)\n")
            f.write(f"- **Methods**: {len(corr['methods'])}\n\n")

            f.write("| Index | Address |\n")
            f.write("|-------|----------|\n")

            for i, method in enumerate(corr['methods']):
                f.write(f"| {i:2d} | 0x{method:08X} |\n")

            f.write("\n")

            # C++ struct
            f.write("```cpp\n")
            f.write(f"struct {struct_name}_vtable {{\n")
            for i, method in enumerate(corr['methods']):
                f.write(f"    void* method_{i}; // @ 0x{method:08X}\n")
            f.write("};\n")
            f.write("```\n\n")

            f.write("---\n\n")

    print(f"\n✓ Results saved to {output_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: correlate_vtables_to_structures.py <europeo.exe> [output.md]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "TVN_VTABLE_CORRELATIONS.md"

    results = correlate_all_structures(filepath)

    print("\n" + "="*100)
    print("CORRELATION COMPLETE")
    print("="*100)
    print(f"\nStructures correlated: {len(results)}/{len(MISSING_STRUCTURES)}")

    save_correlation_results(results, output_file)
    print("\nDone!")
