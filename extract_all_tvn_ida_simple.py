"""
IDA Python script to extract ALL TVN methods assembly code
Run this in IDA Pro: File -> Script file... -> select this script

This replicates the manual work you did for the 5 assembly extracts,
but does it automatically for all 35 TVN structures.

Output: TVN_IDA_EXTRACTS/ directory with one .md file per TVN structure
"""

import idc
import idaapi
import idautils
import os

# All TVN structures with their vtable addresses
TVN_VTABLES = {
    # Shared base vtable (16 structures)
    "TVNCommand": 0x0040E1E0,
    "TVNDigitParms": 0x0040E1E0,
    "TVNExecParms": 0x0040E1E0,
    "TVNFontParms": 0x0040E1E0,
    "TVNHtmlParms": 0x0040E1E0,
    "TVNIfParms": 0x0040E1E0,
    "TVNImageParms": 0x0040E1E0,
    "TVNImgObjParms": 0x0040E1E0,
    "TVNImgSeqParms": 0x0040E1E0,
    "TVNMidiParms": 0x0040E1E0,
    "TVNProjectParms": 0x0040E1E0,
    "TVNSceneParms": 0x0040E1E0,
    "TVNSetVarParms": 0x0040E1E0,
    "TVNStringParms": 0x0040E1E0,
    "TVNTextObjParms": 0x0040E1E0,
    "TVNTextParms": 0x0040E1E0,

    # Specific vtables
    "TVNFrame_1": 0x00435B50,
    "TVNFrame_2": 0x00435DD4,
    "TVNHotspot": 0x00413514,
    "TVNImageObject_1": 0x00429980,
    "TVNImageObject_2": 0x004299D0,
    "TVNTimer": 0x004394D4,
}


def is_valid_code_pointer(addr):
    """Check if address is valid code"""
    if addr < 0x00401000 or addr > 0x00500000:
        return False

    # Check if it's code
    flags = idc.get_full_flags(addr)
    return idc.is_code(flags)


def extract_vtable_methods(vtable_addr):
    """Extract all method addresses from a vtable"""
    methods = []

    for offset in range(0, 0x40, 4):
        method_ptr_addr = vtable_addr + offset
        method_addr = idc.get_wide_dword(method_ptr_addr)

        if method_addr == 0:
            break

        if not is_valid_code_pointer(method_addr):
            if offset == 0:
                break
            break

        methods.append({
            'index': offset // 4,
            'address': method_addr,
            'name': idc.get_func_name(method_addr) or f"sub_{method_addr:X}"
        })

    return methods


def get_function_disassembly(func_addr):
    """Get complete disassembly of a function"""
    lines = []

    # Get function
    func = idaapi.get_func(func_addr)
    if not func:
        return ["ERROR: Not a function"]

    # Iterate through all instructions in the function
    ea = func.start_ea
    while ea < func.end_ea:
        # Get disassembly line
        disasm = idc.generate_disasm_line(ea, 0)

        # Get address
        addr_str = f"{ea:08X}"

        # Get bytes
        item_size = idc.get_item_size(ea)
        bytes_str = " ".join([f"{idc.get_wide_byte(ea + i):02X}" for i in range(min(item_size, 8))])

        # Format: address  bytes  disassembly
        line = f"{addr_str}  {bytes_str:24s}  {disasm}"
        lines.append(line)

        # Next instruction
        ea = idc.next_head(ea, func.end_ea)

    return lines


def extract_strings_from_function(func_addr):
    """Extract string references from a function"""
    strings = []

    func = idaapi.get_func(func_addr)
    if not func:
        return strings

    ea = func.start_ea
    while ea < func.end_ea:
        # Get all data references from this instruction
        for ref in idautils.DataRefsFrom(ea):
            # Check if it's a string
            str_type = idc.get_str_type(ref)
            if str_type is not None:
                string_val = idc.get_strlit_contents(ref)
                if string_val:
                    strings.append({
                        'addr': ea,
                        'ref_addr': ref,
                        'value': string_val.decode('utf-8', errors='ignore')
                    })

        ea = idc.next_head(ea, func.end_ea)

    return strings


def extract_function_calls(func_addr):
    """Extract function calls from a function"""
    calls = []

    func = idaapi.get_func(func_addr)
    if not func:
        return calls

    ea = func.start_ea
    while ea < func.end_ea:
        # Get all code references from this instruction
        for ref in idautils.CodeRefsFrom(ea, 0):
            # Check if it's a call
            if idc.print_insn_mnem(ea) in ['call', 'jmp']:
                called_name = idc.get_func_name(ref) or f"sub_{ref:X}"
                calls.append({
                    'addr': ea,
                    'target': ref,
                    'name': called_name
                })

        ea = idc.next_head(ea, func.end_ea)

    return calls


def identify_important_calls(calls):
    """Identify important calls (TProfile, GetString, etc.)"""
    important = []
    other = []

    for call in calls:
        name_lower = call['name'].lower()
        if any(keyword in name_lower for keyword in [
            'getstring', 'getint', 'profile', 'tprofile',
            'loadfrom', 'parse', 'readstring', 'ini'
        ]):
            important.append(call)
        else:
            other.append(call)

    return important, other


def extract_method_complete(method, method_index, output_file):
    """Extract complete assembly for one method"""

    f = output_file

    f.write(f"## Method [{method_index}]: {method['name']}\n\n")
    f.write(f"**Address**: 0x{method['address']:08X}\n")
    f.write(f"**Index in vtable**: {method['index']}\n")
    f.write(f"**Name**: `{method['name']}`\n\n")

    print(f"  [{method_index}] Extracting {method['name']} @ 0x{method['address']:08X}...")

    # Get disassembly
    disasm_lines = get_function_disassembly(method['address'])

    # Write assembly
    f.write("### Assembly Code\n\n")
    f.write("```assembly\n")
    for line in disasm_lines:
        f.write(line + "\n")
    f.write("```\n\n")

    # Extract strings
    strings = extract_strings_from_function(method['address'])
    if strings:
        f.write("### String References\n\n")
        for s in strings:
            f.write(f"- 0x{s['addr']:08X} → 0x{s['ref_addr']:08X}: `{s['value']}`\n")
        f.write("\n")

    # Extract function calls
    calls = extract_function_calls(method['address'])
    if calls:
        important, other = identify_important_calls(calls)

        f.write("### Function Calls\n\n")

        if important:
            f.write("**Important Calls** (TProfile, GetString, etc.):\n\n")
            for call in important:
                f.write(f"- ⭐ 0x{call['addr']:08X} → `{call['name']}` @ 0x{call['target']:08X}\n")
            f.write("\n")

        if other:
            f.write("**Other Calls**:\n\n")
            for call in other[:20]:  # Limit
                f.write(f"- 0x{call['addr']:08X} → `{call['name']}`\n")
            if len(other) > 20:
                f.write(f"- ... and {len(other) - 20} more\n")
            f.write("\n")

    f.write("---\n\n")


def extract_tvn_structure(struct_name, vtable_addr, output_dir):
    """Extract all methods for one TVN structure"""

    print("\n" + "="*100)
    print(f"EXTRACTING: {struct_name}")
    print(f"Vtable @ 0x{vtable_addr:08X}")
    print("="*100)

    # Extract methods from vtable
    methods = extract_vtable_methods(vtable_addr)

    if not methods:
        print(f"  ⚠️ No methods found in vtable")
        return

    print(f"  Found {len(methods)} method(s)")

    # Create output file
    output_file_path = os.path.join(output_dir, f"{struct_name}_COMPLETE.md")

    with open(output_file_path, 'w') as f:
        # Write header
        f.write(f"# {struct_name} - Complete Assembly Extraction\n\n")
        f.write(f"**Vtable Address**: 0x{vtable_addr:08X}\n")
        f.write(f"**Binary**: europeo.exe\n")
        f.write(f"**Tool**: IDA Pro\n")
        f.write(f"**Date**: 2026-01-16\n\n")
        f.write("---\n\n")

        # Write summary
        f.write("## Methods Summary\n\n")
        f.write("| Index | Address | Name |\n")
        f.write("|-------|---------|------|\n")

        for method in methods:
            f.write(f"| {method['index']:2d} | 0x{method['address']:08X} | `{method['name']}` |\n")

        f.write("\n---\n\n")

        # Extract each method
        for i, method in enumerate(methods):
            extract_method_complete(method, i, f)

    print(f"  ✓ Saved to {struct_name}_COMPLETE.md")


def main():
    """Main extraction function"""

    print("="*100)
    print("EXTRACTING COMPLETE ASSEMBLY CODE FOR ALL TVN METHODS - IDA")
    print("="*100)
    print()

    # Create output directory
    output_dir = "TVN_IDA_EXTRACTS"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Output directory: {output_dir}")
    print()

    # Wait for auto-analysis if needed
    idaapi.auto_wait()

    # Track which vtables we've processed
    processed_vtables = set()

    # Extract each structure
    for struct_name, vtable_addr in TVN_VTABLES.items():
        # Skip duplicates (shared vtable)
        if vtable_addr in processed_vtables:
            print("\n" + "="*100)
            print(f"SKIPPING: {struct_name} (shares vtable 0x{vtable_addr:08X})")
            print("="*100)
            continue

        processed_vtables.add(vtable_addr)
        extract_tvn_structure(struct_name, vtable_addr, output_dir)

    print("\n" + "="*100)
    print("EXTRACTION COMPLETE!")
    print("="*100)
    print(f"\nOutput directory: {output_dir}")
    print(f"Structures extracted: {len(processed_vtables)}")
    print()
    print("✓ Done! Check the TVN_IDA_EXTRACTS/ folder for results.")


if __name__ == "__main__":
    main()
