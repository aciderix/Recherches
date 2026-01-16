"""
IDA Python script to extract ALL 35 TVN structures with complete DATA sections
Extracts assembly code + all DATA references (strings, constants, etc.)
Run this in IDA Pro: File -> Script file...
"""

import idc
import idaapi
import idautils
import os

# ALL 35 TVN STRUCTURES - with their vtable addresses
# Even if vtable is shared, we extract each structure separately
TVN_STRUCTURES = {
    # Parms structures (16) - share base vtable 0x0040E1E0
    "TVNProjectParms": 0x0040E1E0,
    "TVNMidiParms": 0x0040E1E0,
    "TVNDigitParms": 0x0040E1E0,
    "TVNHtmlParms": 0x0040E1E0,
    "TVNImageParms": 0x0040E1E0,
    "TVNImgObjParms": 0x0040E1E0,
    "TVNImgSeqParms": 0x0040E1E0,
    "TVNExecParms": 0x0040E1E0,
    "TVNSetVarParms": 0x0040E1E0,
    "TVNIfParms": 0x0040E1E0,
    "TVNTextParms": 0x0040E1E0,
    "TVNTextObjParms": 0x0040E1E0,
    "TVNFontParms": 0x0040E1E0,
    "TVNCommand": 0x0040E1E0,
    "TVNSceneParms": 0x0040E1E0,
    "TVNStringParms": 0x0040E1E0,

    # Specific vtables (7)
    "TVNFrame_1": 0x00435B50,
    "TVNFrame_2": 0x00435DD4,
    "TVNHotspot": 0x00413514,
    "TVNImageObject_1": 0x00429980,
    "TVNImageObject_2": 0x004299D0,
    "TVNTimer": 0x004394D4,

    # Missing structures - need to find their vtables
    # These will be marked as TODO in the output
    "TVNFileNameParms": None,
    "TVNEventCommand": None,
    "TVNVariable": None,
    "TVNScene": None,
    "TVNToolBar": None,
    "TVNWindow": None,
    "TVNApplication": None,
    "TVNAviMedia": None,
    "TVNWaveMedia": None,
    "TVNMidiMedia": None,
    "TVNCDAMedia": None,
    "TVNBitmap": None,
    "TVNGdiObject": None,
    "TVNHtmlText": None,
    "TVNImageObject": None,
    "TVNTextObject": None,
    "TVNBmpImg": None,
}


def extract_string_at_address(addr):
    """Extract string at a given address with full DATA section info"""
    str_type = idc.get_str_type(addr)
    if str_type is None:
        return None

    # Get the string
    string_val = idc.get_strlit_contents(addr)
    if not string_val:
        return None

    try:
        decoded = string_val.decode('utf-8', errors='ignore')
    except:
        decoded = str(string_val)

    # Get bytes representation (like IDA DATA section)
    bytes_list = []
    ea = addr
    max_len = len(string_val) + 1  # Include null terminator

    for i in range(max_len):
        byte_val = idc.get_wide_byte(ea + i)
        char = chr(byte_val) if 32 <= byte_val <= 126 else ''
        bytes_list.append({
            'offset': ea + i,
            'byte': byte_val,
            'char': char
        })

    return {
        'address': addr,
        'value': decoded,
        'bytes': bytes_list
    }


def get_all_data_refs_from_function(func_addr):
    """Get ALL data references from a function (not just strings)"""
    func = idaapi.get_func(func_addr)
    if not func:
        return []

    data_refs = []
    ea = func.start_ea

    while ea < func.end_ea:
        # Get all data references from this instruction
        for ref in idautils.DataRefsFrom(ea):
            # Get info about the referenced data
            data_info = {
                'instr_addr': ea,
                'ref_addr': ref,
                'type': 'unknown'
            }

            # Check if it's a string
            str_info = extract_string_at_address(ref)
            if str_info:
                data_info['type'] = 'string'
                data_info['string'] = str_info
                data_refs.append(data_info)
                continue

            # Check if it's a defined data item
            flags = idc.get_full_flags(ref)
            if idc.is_data(flags):
                # Get the data
                item_size = idc.get_item_size(ref)
                data_bytes = []
                for i in range(min(item_size, 32)):  # Max 32 bytes
                    byte_val = idc.get_wide_byte(ref + i)
                    data_bytes.append(byte_val)

                data_info['type'] = 'data'
                data_info['size'] = item_size
                data_info['bytes'] = data_bytes
                data_refs.append(data_info)

        ea = idc.next_head(ea, func.end_ea)

    return data_refs


def format_data_section(data_ref):
    """Format data reference like IDA's DATA section"""
    lines = []

    if data_ref['type'] == 'string':
        string_info = data_ref['string']

        lines.append(f"DATA:{string_info['address']:08X} ; \"{string_info['value']}\"")
        lines.append(f"DATA:{string_info['address']:08X} ; Referenced from 0x{data_ref['instr_addr']:08X}")

        # Show bytes like IDA
        for byte_info in string_info['bytes']:
            char_comment = f" ; {byte_info['char']}" if byte_info['char'] else ""
            if byte_info['byte'] == 0:
                lines.append(f"DATA:{byte_info['offset']:08X}                 db    0{char_comment}")
            else:
                lines.append(f"DATA:{byte_info['offset']:08X}                 db  {byte_info['byte']:02X}h{char_comment}")

    elif data_ref['type'] == 'data':
        lines.append(f"DATA:{data_ref['ref_addr']:08X} ; Data ({data_ref['size']} bytes)")
        lines.append(f"DATA:{data_ref['ref_addr']:08X} ; Referenced from 0x{data_ref['instr_addr']:08X}")

        for i, byte_val in enumerate(data_ref['bytes']):
            offset = data_ref['ref_addr'] + i
            lines.append(f"DATA:{offset:08X}                 db  {byte_val:02X}h")

    return lines


def extract_method_with_data(method, method_index, output_file):
    """Extract method with complete DATA section like IDA"""
    f = output_file

    f.write(f"## Method [{method_index}]: {method['name']}\n\n")
    f.write(f"**Address**: 0x{method['address']:08X}\n")
    f.write(f"**Index in vtable**: {method['index']}\n")
    f.write(f"**Name**: `{method['name']}`\n\n")

    print(f"  [{method_index}] Extracting {method['name']} @ 0x{method['address']:08X}...")

    # Get disassembly
    disasm_lines = []
    func = idaapi.get_func(method['address'])

    if func:
        ea = func.start_ea
        while ea < func.end_ea:
            disasm = idc.generate_disasm_line(ea, 0)
            addr_str = f"{ea:08X}"
            disasm_lines.append(f"{addr_str}  {disasm}")
            ea = idc.next_head(ea, func.end_ea)
    else:
        disasm_lines = ["ERROR: Not a recognized function"]

    # Get ALL data references (strings, constants, etc.)
    data_refs = get_all_data_refs_from_function(method['address'])

    # Write assembly
    f.write("### Assembly Code\n\n")
    f.write("```assembly\n")
    for line in disasm_lines:
        f.write(line + "\n")
    f.write("```\n\n")

    # Write DATA section (like IDA format!)
    if data_refs:
        f.write("### DATA Section References\n\n")
        f.write("Complete DATA section like IDA (strings, constants, etc.):\n\n")
        f.write("```\n")

        for data_ref in data_refs:
            data_lines = format_data_section(data_ref)
            for line in data_lines:
                f.write(line + "\n")
            f.write("\n")

        f.write("```\n\n")

        # Summary of strings found
        string_refs = [d for d in data_refs if d['type'] == 'string']
        if string_refs:
            f.write("**Strings Found**:\n\n")
            for s in string_refs:
                f.write(f"- `\"{s['string']['value']}\"` @ 0x{s['ref_addr']:08X}\n")
            f.write("\n")

    # Get function calls
    calls = []
    if func:
        ea = func.start_ea
        while ea < func.end_ea:
            for ref in idautils.CodeRefsFrom(ea, 0):
                if idc.print_insn_mnem(ea) == 'call':
                    called_name = idc.get_func_name(ref) or f"sub_{ref:X}"
                    calls.append({
                        'addr': ea,
                        'target': ref,
                        'name': called_name
                    })
            ea = idc.next_head(ea, func.end_ea)

    if calls:
        f.write("### Function Calls\n\n")

        # Identify important calls
        important = [c for c in calls if any(kw in c['name'].lower()
                     for kw in ['getstring', 'getint', 'profile', 'loadfrom', 'parse'])]
        other = [c for c in calls if c not in important]

        if important:
            f.write("**Important Calls** (TProfile, GetString, etc.):\n\n")
            for call in important:
                f.write(f"- ⭐ 0x{call['addr']:08X} → `{call['name']}` @ 0x{call['target']:08X}\n")
            f.write("\n")

        if other:
            f.write("**Other Calls**:\n\n")
            for call in other[:20]:
                f.write(f"- 0x{call['addr']:08X} → `{call['name']}`\n")
            if len(other) > 20:
                f.write(f"- ... and {len(other) - 20} more\n")
            f.write("\n")

    f.write("---\n\n")


def is_valid_code_pointer(addr):
    """Check if address is valid code"""
    if addr < 0x00401000 or addr > 0x00500000:
        return False
    flags = idc.get_full_flags(addr)
    return idc.is_code(flags)


def extract_vtable_methods(vtable_addr):
    """Extract all method addresses from a vtable"""
    if vtable_addr is None:
        return None

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


def extract_tvn_structure(struct_name, vtable_addr, output_dir):
    """Extract one TVN structure with all DATA"""

    print(f"\n{'='*100}")
    print(f"EXTRACTING: {struct_name}")
    if vtable_addr:
        print(f"Vtable @ 0x{vtable_addr:08X}")
    else:
        print(f"⚠️  No vtable address known - TODO")
    print(f"{'='*100}")

    # Create output file
    output_file_path = os.path.join(output_dir, f"{struct_name}_COMPLETE.md")

    with open(output_file_path, 'w') as f:
        # Header
        f.write(f"# {struct_name} - Complete Extraction\n\n")
        f.write(f"**Structure**: {struct_name}\n")
        if vtable_addr:
            f.write(f"**Vtable Address**: 0x{vtable_addr:08X}\n")
        else:
            f.write(f"**Vtable Address**: ⚠️ TODO - Not found yet\n")
        f.write(f"**Binary**: europeo.exe\n")
        f.write(f"**Tool**: IDA Pro\n")
        f.write(f"**Date**: 2026-01-16\n\n")
        f.write("---\n\n")

        if vtable_addr is None:
            f.write("## ⚠️ TODO: Vtable Not Found\n\n")
            f.write("This structure's vtable has not been located yet.\n")
            f.write("Manual analysis with IDA is needed to find it.\n\n")
            print(f"  ⚠️  Vtable not found - created TODO file")
            return

        # Extract methods
        methods = extract_vtable_methods(vtable_addr)

        if not methods:
            f.write("## ⚠️ No Methods Found\n\n")
            print(f"  ⚠️  No methods found")
            return

        print(f"  Found {len(methods)} method(s)")

        # Summary
        f.write("## Methods Summary\n\n")
        f.write("| Index | Address | Name |\n")
        f.write("|-------|---------|------|\n")
        for method in methods:
            f.write(f"| {method['index']:2d} | 0x{method['address']:08X} | `{method['name']}` |\n")
        f.write("\n---\n\n")

        # Extract each method WITH DATA
        for i, method in enumerate(methods):
            extract_method_with_data(method, i, f)

    print(f"  ✓ Saved to {struct_name}_COMPLETE.md")


def main():
    """Main extraction function"""

    print("="*100)
    print("EXTRACTING ALL 35 TVN STRUCTURES WITH COMPLETE DATA SECTIONS")
    print("="*100)
    print()

    # Create output directory
    output_dir = "TVN_COMPLETE_35_STRUCTURES"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Output directory: {output_dir}")
    print(f"Total structures: {len(TVN_STRUCTURES)}")
    print()

    # Wait for auto-analysis
    idaapi.auto_wait()

    # Extract each structure
    for struct_name, vtable_addr in TVN_STRUCTURES.items():
        extract_tvn_structure(struct_name, vtable_addr, output_dir)

    # Summary
    print("\n" + "="*100)
    print("EXTRACTION COMPLETE!")
    print("="*100)

    with_vtable = sum(1 for v in TVN_STRUCTURES.values() if v is not None)
    without_vtable = sum(1 for v in TVN_STRUCTURES.values() if v is None)

    print(f"\nTotal structures: {len(TVN_STRUCTURES)}")
    print(f"With vtable: {with_vtable}")
    print(f"Without vtable (TODO): {without_vtable}")
    print(f"\nOutput directory: {output_dir}")
    print()
    print("✓ Done! Files include complete DATA sections like IDA format.")
    print("✓ Check files for strings like 'AREA_%u', 'NAME', 'BKCOLOR', etc.")


if __name__ == "__main__":
    main()
