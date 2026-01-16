#!/usr/bin/env python3
"""
Verify top LoadFromINI candidates using radare2 analysis
This replaces manual IDA verification with automated analysis
"""

import subprocess
import json
import sys

# Top 10 candidates to verify (from RAPPORT_FINAL_STRUCTURES_TVN.md)
TOP_CANDIDATES = {
    'TVNAviMedia': {
        'typeinfo': 0x00435953,
        'destructor': 0x004363DC,
        'candidate': 0x00405B50,
        'expected': 'Video/AVI handling'
    },
    'TVNBitmap': {
        'typeinfo': 0x0041E5FC,
        'destructor': 0x0041E7DE,
        'candidate': 0x0041D902,
        'expected': 'DIB/Bitmap operations'
    },
    'TVNHtmlText': {
        'typeinfo': 0x004231F0,
        'destructor': 0x00423692,
        'candidate': 0x0041FAA4,
        'expected': 'HTML rendering'
    },
    'TVNCDAMedia': {
        'typeinfo': 0x00435939,
        'destructor': 0x00436448,
        'candidate': 0x004357CF,
        'expected': 'CD audio'
    },
    'TVNWaveMedia': {
        'typeinfo': 0x0041C51D,
        'destructor': 0x0041C742,
        'candidate': 0x00437289,
        'expected': 'Wave audio'
    },
    'TVNMidiMedia': {
        'typeinfo': 0x0041C590,
        'destructor': 0x0041C64B,
        'candidate': 0x00437289,
        'expected': 'MIDI audio'
    },
    'TVNBmpImg': {
        'typeinfo': 0x004358CF,
        'destructor': 0x00436570,
        'candidate': 0x004357CF,
        'expected': 'Bitmap image'
    },
    'TVNGdiObject': {
        'typeinfo': 0x0041E673,
        'destructor': 0x0041E68E,
        'candidate': 0x0041EF0A,
        'expected': 'GDI object'
    },
    'TVNEventCommand': {
        'typeinfo': 0x0040F51E,
        'destructor': 0x0040F6AE,
        'candidate': 0x00411D4D,
        'expected': 'Event/command'
    },
    'TVNToolBar': {
        'typeinfo': 0x00435901,
        'destructor': 0x00436528,
        'candidate': 0x004357CF,
        'expected': 'Toolbar UI'
    },
}


def run_r2_command(binary, addr, cmd):
    """Run radare2 command and return output"""
    try:
        result = subprocess.run(
            ['r2', '-q', '-c', f's {addr:#x}; {cmd}', binary],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"


def analyze_function(binary, addr, struct_name):
    """Analyze a function using radare2"""
    print(f"\n{'='*80}")
    print(f"Analyzing {struct_name} @ 0x{addr:08X}")
    print(f"{'='*80}\n")

    # Get function info
    print("[1/5] Function Analysis...")
    func_info = run_r2_command(binary, addr, 'afi')
    if func_info and 'Error' not in func_info:
        lines = func_info.split('\n')
        for line in lines[:10]:  # First 10 lines
            print(f"  {line}")
    print()

    # Get cross-references (what calls this function)
    print("[2/5] Cross-References (who calls this)...")
    xrefs = run_r2_command(binary, addr, 'axt')
    if xrefs and 'Error' not in xrefs:
        xref_lines = xrefs.split('\n')[:10]
        for line in xref_lines:
            print(f"  {line}")
        if len(xrefs.split('\n')) > 10:
            print(f"  ... and {len(xrefs.split('\n')) - 10} more")
    else:
        print("  No xrefs found")
    print()

    # Get strings referenced by function
    print("[3/5] Strings Referenced...")
    # Disassemble and look for string refs
    disasm = run_r2_command(binary, addr, 'pdf @ $F')
    if disasm and 'Error' not in disasm:
        # Extract string references
        strings_found = []
        for line in disasm.split('\n'):
            if 'str.' in line or '; "' in line:
                strings_found.append(line.strip())

        if strings_found:
            for s in strings_found[:15]:  # First 15 strings
                print(f"  {s}")
            if len(strings_found) > 15:
                print(f"  ... and {len(strings_found) - 15} more")
        else:
            print("  No strings found in disassembly")
    print()

    # Get function calls (what this function calls)
    print("[4/5] Function Calls (what this calls)...")
    calls = run_r2_command(binary, addr, 'axf @ $F')
    if calls and 'Error' not in calls:
        call_lines = calls.split('\n')[:15]
        for line in call_lines:
            print(f"  {line}")
        if len(calls.split('\n')) > 15:
            print(f"  ... and {len(calls.split('\n')) - 15} more")
    else:
        print("  No function calls found")
    print()

    # Get first 30 instructions
    print("[5/5] First 30 Instructions...")
    instr = run_r2_command(binary, addr, 'pd 30 @ $F')
    if instr and 'Error' not in instr:
        print(instr)
    print()


def check_destructor_correlation(binary, candidate_addr, destructor_addr):
    """Check if candidate function references the destructor"""
    print(f"[Correlation Check] Does 0x{candidate_addr:08X} reference destructor 0x{destructor_addr:08X}?")

    # Disassemble candidate and look for destructor address
    disasm = run_r2_command(binary, candidate_addr, 'pdf @ $F')

    if disasm and 'Error' not in disasm:
        destructor_hex = f"{destructor_addr:x}"
        if destructor_hex in disasm.lower():
            print(f"  ✓ YES - Found destructor reference!")
            return True
        else:
            print(f"  ✗ NO - No direct destructor reference")
            return False
    return False


def main():
    if len(sys.argv) < 2:
        print("Usage: verify_top_candidates.py <europeo.exe>")
        sys.exit(1)

    binary = sys.argv[1]

    print("="*80)
    print("TOP CANDIDATES VERIFICATION USING RADARE2")
    print("="*80)
    print()
    print("This analysis replaces manual IDA verification")
    print()

    # Analyze each candidate
    results = []

    for struct_name, info in TOP_CANDIDATES.items():
        analyze_function(binary, info['candidate'], struct_name)

        # Check correlation
        correlated = check_destructor_correlation(
            binary,
            info['candidate'],
            info['destructor']
        )

        results.append({
            'structure': struct_name,
            'candidate': info['candidate'],
            'destructor': info['destructor'],
            'correlated': correlated,
            'expected': info['expected']
        })

        print("\n" + "="*80 + "\n")

    # Summary
    print("\n" + "="*80)
    print("VERIFICATION SUMMARY")
    print("="*80 + "\n")

    for r in results:
        status = "✓ CORRELATED" if r['correlated'] else "✗ NOT CORRELATED"
        print(f"{r['structure']:20s} @ 0x{r['candidate']:08X} - {status}")
        print(f"  Expected: {r['expected']}")
        print()

    correlated_count = sum(1 for r in results if r['correlated'])
    print(f"Total: {correlated_count}/{len(results)} candidates show destructor correlation")
    print()


if __name__ == "__main__":
    main()
