#!/usr/bin/env python3
"""
Extract complete assembly code for ALL TVN methods using objdump
One markdown file per TVN structure
Most reliable approach - objdump is standard and stable
"""

import subprocess
import struct
import os
import re

# All TVN structures with their vtable addresses
TVN_VTABLES = {
    # Shared base vtable
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


def read_dword(data, offset):
    """Read DWORD at offset"""
    if offset < 0 or offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def is_valid_code_pointer(addr):
    """Check if address is a valid code pointer"""
    return 0x00401000 <= addr <= 0x00500000


def extract_vtable_methods(data, vtable_va):
    """Extract all method addresses from a vtable"""
    file_offset = vtable_va - 0x00400000
    methods = []

    for offset in range(0, 0x40, 4):
        method_addr = read_dword(data, file_offset + offset)

        if method_addr == 0:
            break

        if not is_valid_code_pointer(method_addr):
            if offset == 0:
                break
            break

        methods.append({
            'index': offset // 4,
            'address': method_addr
        })

    return methods


def disassemble_full_binary(binary_path):
    """Disassemble entire binary with objdump - ONCE for all functions"""

    print("  Disassembling entire binary with objdump (this may take a moment)...")

    cmd = [
        'objdump',
        '-d',           # Disassemble
        '-M', 'intel',  # Intel syntax
        '--no-show-raw-insn',  # Don't show hex bytes
        binary_path
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            print(f"  WARNING: objdump returned {result.returncode}")
        return result.stdout
    except subprocess.TimeoutExpired:
        return "ERROR: Timeout"
    except Exception as e:
        return f"ERROR: {e}"


def extract_function_from_disassembly(full_disasm, func_addr):
    """Extract a specific function from the full disassembly"""

    # Convert address to hex string format used by objdump
    func_hex = f"{func_addr:x}"

    # Find the function in the disassembly
    # objdump format: "  401234:	instruction"
    pattern = rf'^\s*{func_hex}:.*?(?=^\s*[0-9a-f]+:|^Disassembly|$)'

    match = re.search(pattern, full_disasm, re.MULTILINE | re.DOTALL | re.IGNORECASE)

    if match:
        return match.group(0)

    # Alternative: just find lines starting with this address
    lines = []
    in_function = False

    for line in full_disasm.split('\n'):
        # Check if line starts with our function address
        if re.match(rf'^\s*{func_hex}:', line, re.IGNORECASE):
            in_function = True
            lines.append(line)
        elif in_function:
            # Check if we've hit another function
            if re.match(r'^\s*[0-9a-f]+:', line):
                # Still in our function or new function?
                addr_match = re.match(r'^\s*([0-9a-f]+):', line)
                if addr_match:
                    line_addr = int(addr_match.group(1), 16)
                    # If address gap is small, probably still our function
                    if line_addr - func_addr < 1000:  # Max 1KB function
                        lines.append(line)
                    else:
                        break
            elif line.strip() == '':
                # Empty line might end function
                if len(lines) > 10:  # If we have enough lines, stop
                    break
            else:
                lines.append(line)

    return '\n'.join(lines) if lines else None


def extract_strings_from_asm(asm_code):
    """Extract string references from assembly code"""
    strings = []

    # Look for string references in objdump output
    # Format variations:
    # - offset + <string>
    # - "string"
    # - 0xaddr <string>

    patterns = [
        r'<([^>]+)>',      # <string_name>
        r'"([^"]+)"',      # "literal string"
        r'#\s*0x[0-9a-f]+\s+<([^>]+)>',  # # 0xaddr <string>
    ]

    for pattern in patterns:
        matches = re.findall(pattern, asm_code, re.IGNORECASE)
        strings.extend(matches)

    # Clean up
    cleaned = []
    for s in strings:
        s = s.strip()
        # Filter out non-string looking things
        if s and not s.startswith('0x') and 'fcn' not in s:
            cleaned.append(s)

    return list(set(cleaned))  # Remove duplicates


def extract_function_calls(asm_code):
    """Extract function calls from assembly code"""
    calls = []

    # objdump format: call   401234 <function_name>
    #                 call   DWORD PTR [addr]

    patterns = [
        r'call\s+[0-9a-f]+\s+<([^>]+)>',  # call addr <name>
        r'call\s+([0-9a-fx]+)',           # call addr
    ]

    for pattern in patterns:
        matches = re.findall(pattern, asm_code, re.IGNORECASE)
        calls.extend(matches)

    return calls


def identify_important_calls(calls):
    """Identify important function calls (TProfile, GetString, etc.)"""
    important = []
    other = []

    for call in calls:
        call_lower = call.lower()
        if any(keyword in call_lower for keyword in [
            'getstring', 'getint', 'profile', 'tprofile',
            'loadfrom', 'parse', 'readstring', 'ini'
        ]):
            important.append(call)
        else:
            other.append(call)

    return important, other


def extract_method_complete(full_disasm, method, method_index, output_file):
    """Extract complete assembly for one method"""

    f = output_file

    f.write(f"## Method [{method_index}]: 0x{method['address']:08X}\n\n")
    f.write(f"**Address**: 0x{method['address']:08X}\n")
    f.write(f"**Index in vtable**: {method['index']}\n\n")

    # Extract function from full disassembly
    print(f"  [{method_index}] Extracting 0x{method['address']:08X}...")
    asm_code = extract_function_from_disassembly(full_disasm, method['address'])

    if not asm_code:
        f.write(f"⚠️ **Function not found in disassembly**\n\n")
        f.write("---\n\n")
        return

    # Write assembly
    f.write("### Assembly Code\n\n")
    f.write("```assembly\n")
    f.write(asm_code)
    f.write("\n```\n\n")

    # Extract and write string references
    strings = extract_strings_from_asm(asm_code)
    if strings:
        f.write("### String References\n\n")
        for s in sorted(strings):
            f.write(f"- `{s}`\n")
        f.write("\n")

    # Extract and write function calls
    calls = extract_function_calls(asm_code)
    if calls:
        important, other = identify_important_calls(calls)

        f.write("### Function Calls\n\n")

        if important:
            f.write("**Important Calls** (TProfile, GetString, etc.):\n\n")
            for call in sorted(set(important)):
                f.write(f"- ⭐ `{call}`\n")
            f.write("\n")

        if other:
            f.write("**Other Calls**:\n\n")
            other_unique = sorted(set(other))
            for call in other_unique[:20]:  # Limit to first 20
                f.write(f"- `{call}`\n")
            if len(other_unique) > 20:
                f.write(f"- ... and {len(other_unique) - 20} more\n")
            f.write("\n")

    f.write("---\n\n")


def extract_tvn_structure(binary_path, full_disasm, struct_name, vtable_va, output_dir):
    """Extract all methods for one TVN structure"""

    print(f"\n{'='*100}")
    print(f"EXTRACTING: {struct_name}")
    print(f"Vtable @ 0x{vtable_va:08X}")
    print(f"{'='*100}")

    # Read binary to extract vtable
    with open(binary_path, 'rb') as f:
        data = f.read()

    # Extract methods from vtable
    methods = extract_vtable_methods(data, vtable_va)

    if not methods:
        print(f"  ⚠️ No methods found in vtable")
        return

    print(f"  Found {len(methods)} method(s)")

    # Create output file
    output_file = os.path.join(output_dir, f"{struct_name}_COMPLETE.md")

    with open(output_file, 'w') as f:
        # Write header
        f.write(f"# {struct_name} - Complete Assembly Extraction\n\n")
        f.write(f"**Vtable Address**: 0x{vtable_va:08X}\n")
        f.write(f"**Binary**: europeo.exe\n")
        f.write(f"**Tool**: objdump (GNU Binutils)\n")
        f.write(f"**Date**: 2026-01-16\n\n")
        f.write("---\n\n")

        # Write summary
        f.write("## Methods Summary\n\n")
        f.write("| Index | Address |\n")
        f.write("|-------|----------|\n")

        for method in methods:
            f.write(f"| {method['index']:2d} | 0x{method['address']:08X} |\n")

        f.write("\n---\n\n")

        # Extract each method
        for i, method in enumerate(methods):
            extract_method_complete(full_disasm, method, i, f)

    print(f"  ✓ Saved to {struct_name}_COMPLETE.md")


def extract_all_tvn_structures(binary_path, output_dir):
    """Extract all TVN structures"""

    print("="*100)
    print("EXTRACTING COMPLETE ASSEMBLY CODE FOR ALL TVN METHODS")
    print("="*100)
    print()

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}\n")

    # Disassemble entire binary ONCE (for performance)
    print("="*100)
    print("STEP 1: Disassembling entire binary")
    print("="*100)
    full_disasm = disassemble_full_binary(binary_path)

    if "ERROR" in full_disasm:
        print(f"ERROR: Failed to disassemble binary: {full_disasm}")
        return

    print(f"  ✓ Disassembly complete ({len(full_disasm)} bytes)")

    # Track which vtables we've already processed (to avoid duplicates)
    processed_vtables = set()

    print("\n" + "="*100)
    print("STEP 2: Extracting TVN methods")
    print("="*100)

    # Extract each structure
    for struct_name, vtable_va in TVN_VTABLES.items():
        # Skip if we've already processed this vtable (shared vtable)
        if vtable_va in processed_vtables:
            print(f"\n{'='*100}")
            print(f"SKIPPING: {struct_name} (shares vtable 0x{vtable_va:08X})")
            print(f"{'='*100}")
            continue

        processed_vtables.add(vtable_va)
        extract_tvn_structure(binary_path, full_disasm, struct_name, vtable_va, output_dir)

    print("\n" + "="*100)
    print("EXTRACTION COMPLETE")
    print("="*100)
    print(f"\nOutput directory: {output_dir}")
    print(f"Structures extracted: {len(processed_vtables)}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: extract_all_tvn_asm_objdump.py <europeo.exe> [output_dir]")
        print()
        print("This script extracts complete assembly code for all TVN methods using objdump.")
        print("One markdown file is created per TVN structure.")
        print()
        print("Example:")
        print("  python3 extract_all_tvn_asm_objdump.py DOCS/europeo.exe TVN_ASM_EXTRACTS")
        sys.exit(1)

    binary_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "TVN_ASM_EXTRACTS"

    if not os.path.exists(binary_path):
        print(f"ERROR: Binary not found: {binary_path}")
        sys.exit(1)

    extract_all_tvn_structures(binary_path, output_dir)
    print("\nDone!")
