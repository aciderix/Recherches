#!/usr/bin/env python3
"""
Use radare2 to analyze RTTI structures
Much more powerful than manual parsing!
"""

import subprocess
import json
import sys

def r2_cmd(binary, commands):
    """Execute radare2 commands and get output"""
    if isinstance(commands, str):
        commands = [commands]

    cmd_string = '; '.join(commands)

    result = subprocess.run(
        ['r2', '-q', '-c', cmd_string, binary],
        capture_output=True,
        text=True,
        timeout=30
    )

    return result.stdout


def analyze_address(binary, addr, name):
    """Analyze an address with radare2"""
    print(f"\n{'='*80}")
    print(f"Analyzing: {name} @ 0x{addr:08X}")
    print(f"{'='*80}\n")

    commands = [
        'aaa',  # Analyze all
        f's 0x{addr:08X}',  # Seek to address
        'px 64',  # Print hex 64 bytes
        'pd 16',  # Print disassembly 16 instructions
        'axt',  # Find xrefs to this address
    ]

    output = r2_cmd(binary, commands)

    print("Raw output from radare2:")
    print(output)

    return output


def find_vtable_xrefs(binary, addr):
    """Find all xrefs to an address (to find constructors)"""
    print(f"\nFinding XREF to 0x{addr:08X}...")

    commands = [
        'aaa',
        f'axt @ 0x{addr:08X}',
    ]

    output = r2_cmd(binary, commands)
    print(output)

    return output


def disassemble_function(binary, func_addr):
    """Disassemble a complete function"""
    print(f"\nDisassembling function @ 0x{func_addr:08X}...")

    commands = [
        'aaa',
        f's 0x{func_addr:08X}',
        'af',  # Analyze function
        'pdf',  # Print disassembly of function
    ]

    output = r2_cmd(binary, commands)
    print(output[:2000])  # Limit output

    return output


def search_strings_near_address(binary, addr):
    """Search for strings near an address"""
    print(f"\nSearching strings near 0x{addr:08X}...")

    commands = [
        'aaa',
        f's 0x{addr:08X}',
        'ps @ 0x{addr:08X}',  # Print string at address
        'px/s 256 @ 0x{addr:08X}',  # Print strings in 256 bytes
    ]

    output = r2_cmd(binary, commands)
    print(output)

    return output


def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_with_r2.py <europeo.exe>")
        sys.exit(1)

    binary = sys.argv[1]

    print("="*80)
    print("RADARE2 RTTI ANALYSIS")
    print("="*80)
    print()

    # Test addresses
    test_addresses = {
        "0x0040E1E0 (Shared RTTI?)": 0x0040E1E0,
        "0x004179AE (TVNScene TYPEINFO)": 0x004179AE,
        "0x0042A40B (TVNImageObject TYPEINFO)": 0x0042A40B,
        "0x0042A448 (TVNTextObject TYPEINFO)": 0x0042A448,
    }

    for name, addr in test_addresses.items():
        # Analyze the address
        analyze_address(binary, addr, name)

        # Search for strings
        search_strings_near_address(binary, addr)

        # Find xrefs (constructors)
        find_vtable_xrefs(binary, addr)

        input("\nPress Enter to continue to next address...")

    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)


if __name__ == "__main__":
    main()
