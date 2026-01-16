# Ghidra script to extract ALL vtables and methods from ALL 35 TVN structures
# @category TVN.Analysis

from ghidra.program.model.symbol import SymbolType
from ghidra.program.model.listing import CodeUnit
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
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

# Additional structures - need to find vtables
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


def is_valid_code_pointer(addr):
    """Check if address is a valid code pointer"""
    if addr is None:
        return False

    offset = addr.getOffset()

    # Check if in valid code range for europeo.exe
    if offset < 0x00401000 or offset > 0x00500000:
        return False

    # Check if it's a function
    func = getFunctionAt(addr)
    if func is not None:
        return True

    # Check if there's an instruction at this address
    instr = getInstructionAt(addr)
    if instr is not None:
        return True

    return False


def extract_vtable_at_offset(vtable_addr, struct_name):
    """Extract all methods from a vtable at given address"""

    print("\n" + "="*100)
    print("Extracting vtable for {} @ 0x{:08X}".format(struct_name, vtable_addr))
    print("="*100)

    addr = toAddr(vtable_addr)
    methods = []
    offset = 0

    while offset < 0x100:  # Max 64 methods
        method_ptr_addr = addr.add(offset)

        # Read pointer (4 bytes for 32-bit)
        method_ptr_value = getInt(method_ptr_addr)

        if method_ptr_value == 0:
            print("  [0x{:02X}] NULL - end of vtable".format(offset))
            break

        # Create address from pointer value
        method_addr = toAddr(method_ptr_value)

        if not is_valid_code_pointer(method_addr):
            if offset == 0:
                print("  ERROR: First entry is not a valid code pointer!")
                return None
            else:
                print("  [0x{:02X}] 0x{:08X} - invalid, ending".format(offset, method_ptr_value))
                break

        # Get function info
        func = getFunctionAt(method_addr)
        if func is not None:
            func_name = func.getName()
            func_size = func.getBody().getNumAddresses()
            role = identify_method_role(func_name, offset // 4, func_size)
        else:
            func_name = "sub_{:X}".format(method_ptr_value)
            role = "Unknown"
            func_size = 0

        print("  [0x{:02X}] 0x{:08X}  {:30s}  {:25s}  size={}".format(
            offset, method_ptr_value, func_name, role, func_size))

        methods.append({
            'offset': offset,
            'address': method_ptr_value,
            'name': func_name,
            'role': role,
            'size': func_size
        })

        offset += 4

    print("\nTotal methods found: {}".format(len(methods)))
    return methods


def identify_method_role(func_name, method_index, func_size):
    """Try to identify method role"""

    # Name-based detection
    name_lower = func_name.lower()

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

    return "Method[{}]".format(method_index)


def find_vtable_near_string(struct_name):
    """Try to find vtable by searching near type string"""

    search_str = struct_name + " *"

    # Search for string in program
    found_addr = find(search_str)

    if found_addr is None:
        print("  Warning: String '{}' not found for {}".format(search_str, struct_name))
        return None

    print("  Found type string at 0x{:08X}".format(found_addr.getOffset()))

    # Search backwards for vtable (up to 0x200 bytes before string)
    for i in range(0, 0x200, 4):
        check_addr = found_addr.subtract(i)

        # Read first pointer
        first_ptr_value = getInt(check_addr)
        if first_ptr_value is None:
            continue

        first_ptr = toAddr(first_ptr_value)

        if is_valid_code_pointer(first_ptr):
            # Check for consecutive code pointers
            consecutive = 1
            for j in range(1, 10):
                next_addr = check_addr.add(j * 4)
                next_ptr_value = getInt(next_addr)
                if next_ptr_value is None:
                    break

                next_ptr = toAddr(next_ptr_value)
                if is_valid_code_pointer(next_ptr):
                    consecutive += 1
                else:
                    break

            if consecutive >= 3:
                vtable_offset = check_addr.getOffset()
                print("  Possible vtable found at 0x{:08X} ({} methods)".format(
                    vtable_offset, consecutive))
                return vtable_offset

    return None


def extract_all_vtables():
    """Extract vtables from all known TVN structures"""

    print("="*100)
    print("EXTRACTING ALL TVN VTABLES AND METHODS - GHIDRA ANALYSIS")
    print("="*100)
    print("")

    results = {}

    # Phase 1: Known vtable offsets
    print("\n" + "="*100)
    print("PHASE 1: Known Vtable Offsets")
    print("="*100)

    for struct_name in sorted(TVN_VTABLES.keys()):
        vtable_addr = TVN_VTABLES[struct_name]

        methods = extract_vtable_at_offset(vtable_addr, struct_name)

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
        print("\nSearching for {}...".format(struct_name))
        vtable_addr = find_vtable_near_string(struct_name)

        if vtable_addr:
            methods = extract_vtable_at_offset(vtable_addr, struct_name)

            if methods:
                results[struct_name] = {
                    'vtable_address': vtable_addr,
                    'methods': methods
                }
        else:
            print("  Could not locate vtable for {}".format(struct_name))

    return results


def save_results_to_markdown(results):
    """Save extraction results to markdown file"""

    output_file = "/home/user/Recherches/TVN_ALL_METHODS_GHIDRA.md"

    with open(output_file, 'w') as f:
        f.write("# Complete TVN Methods Extraction - Ghidra Analysis\n\n")
        f.write("Comprehensive extraction of all vtables and methods from 35 TVN structures.\n\n")
        f.write("**Tool**: Ghidra 12.0.1 Headless Analyzer\n")
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
            f.write("| {:30s} | 0x{:08X} | {:3d} |\n".format(
                struct_name, data['vtable_address'], method_count))

        f.write("\n**Total**: {} structures, {} methods\n\n".format(
            len(results), total_methods))
        f.write("---\n\n")

        # Detailed methods
        f.write("## Detailed Methods\n\n")

        for struct_name in sorted(results.keys()):
            data = results[struct_name]

            f.write("### {}\n\n".format(struct_name))
            f.write("**Vtable**: 0x{:08X}\n".format(data['vtable_address']))
            f.write("**Methods**: {}\n\n".format(len(data['methods'])))

            f.write("| Offset | Address | Function | Role | Size |\n")
            f.write("|--------|---------|----------|------|------|\n")

            for method in data['methods']:
                f.write("| +0x{:02X} | 0x{:08X} | {:30s} | {:25s} | {:5d} |\n".format(
                    method['offset'],
                    method['address'],
                    method['name'],
                    method['role'],
                    method['size']
                ))

            f.write("\n---\n\n")

    print("\n✓ Results saved to {}".format(output_file))


# Main execution
print("Starting TVN vtable extraction...")
results = extract_all_vtables()

print("\n" + "="*100)
print("EXTRACTION COMPLETE")
print("="*100)
print("\nExtracted {} structures".format(len(results)))
print("Total methods: {}".format(sum(len(r['methods']) for r in results.values())))

save_results_to_markdown(results)
print("\nDone!")
