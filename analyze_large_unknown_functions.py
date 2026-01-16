#!/usr/bin/env python3
"""
Deep analysis of large Unknown functions (>200 instructions, 0 strings)
These are prime candidates for important TVN structures
"""

import os
import re
import struct

# The 6 large Unknown functions from UNKNOWN_FUNCTIONS_ANALYSIS.md
LARGE_UNKNOWNS = [
    {'addr': 0x0040AEB4, 'rank': 126, 'instr': 312, 'hypothesis': 'TVNArea or TVNCommand?'},
    {'addr': 0x004161FA, 'rank': 96, 'instr': 298, 'hypothesis': 'TVNCommand or TVNDialog?'},
    {'addr': 0x0041DB36, 'rank': 147, 'instr': 283, 'hypothesis': 'Unknown - needs analysis'},
    {'addr': 0x0040ABCE, 'rank': 124, 'instr': 211, 'hypothesis': 'Unknown - needs analysis'},
    {'addr': 0x0041EE33, 'rank': 45, 'instr': 215, 'hypothesis': 'Unknown - needs analysis'},
    {'addr': 0x004268F8, 'rank': 165, 'instr': 215, 'hypothesis': 'Unknown - needs analysis'},
]


def find_extracted_file(addr):
    """Find the extracted markdown file for an address"""
    for filename in os.listdir('LOADFROMINI_EXTRACTED'):
        if f'0x{addr:08X}' in filename:
            return f'LOADFROMINI_EXTRACTED/{filename}'
    return None


def parse_extracted_file(filepath):
    """Parse an extracted function markdown file"""
    with open(filepath, 'r') as f:
        content = f.read()

    data = {}

    # Extract metadata
    addr_match = re.search(r'\*\*Function Address\*\*: (0x[0-9A-F]+)', content)
    rank_match = re.search(r'\*\*Rank\*\*: #(\d+)', content)
    instr_match = re.search(r'\*\*Instructions\*\*: (\d+)', content)

    data['address'] = addr_match.group(1) if addr_match else None
    data['rank'] = int(rank_match.group(1)) if rank_match else 0
    data['instructions'] = int(instr_match.group(1)) if instr_match else 0

    # Extract ALL assembly instructions
    asm_section = re.search(r'## Assembly Code.*?```assembly\n(.*?)\n```', content, re.DOTALL)
    if asm_section:
        data['assembly'] = asm_section.group(1)
    else:
        data['assembly'] = 'No assembly found'

    # Extract function calls
    calls_section = re.search(r'## Functions Called.*?\n(.*?)(?=##|\Z)', content, re.DOTALL)
    calls = []
    if calls_section:
        call_pattern = r'- (0x[0-9A-F]+)'
        for match in re.finditer(call_pattern, calls_section.group(1)):
            calls.append(match.group(1))
    data['calls'] = calls

    return data


def analyze_assembly_patterns(asm_code):
    """Analyze assembly for patterns that indicate structure type"""
    patterns = {
        'API calls': [],
        'String operations': 0,
        'Memory allocations': 0,
        'Virtual calls': 0,
        'Loops': 0,
        'Conditionals': 0,
    }

    lines = asm_code.split('\n')

    for line in lines:
        # Count loops (jne, jl, etc. jumping backwards)
        if any(instr in line for instr in ['jne', 'jl', 'jle', 'jg', 'jge', 'jnz']):
            patterns['Conditionals'] += 1
            # Check if backward jump (loop)
            if re.search(r'j\w+\s+0x[0-9A-F]+', line):
                addr_match = re.search(r'(0x[0-9A-F]+)\s+j\w+\s+(0x[0-9A-F]+)', line)
                if addr_match:
                    current = int(addr_match.group(1), 16)
                    target = int(addr_match.group(2), 16)
                    if target < current:
                        patterns['Loops'] += 1

        # Virtual calls (call [reg + offset])
        if 'call     dword ptr [' in line:
            patterns['Virtual calls'] += 1

        # Memory operations
        if any(op in line for op in ['alloc', 'new', 'malloc']):
            patterns['Memory allocations'] += 1

        # String operations
        if any(op in line for op in ['str', 'rep movs', 'rep stos']):
            patterns['String operations'] += 1

        # API calls
        if 'call     0x' in line and 'dword ptr' not in line:
            api_match = re.search(r'call\s+(0x[0-9A-F]+)', line)
            if api_match:
                patterns['API calls'].append(api_match.group(1))

    return patterns


def correlate_with_typeinfo(binary_path, func_addr):
    """Check if function is near any TYPEINFO address"""
    from correlate_typeinfo_loadfromini import TYPEINFO_ADDRESSES

    # Load binary and check for references
    try:
        with open(binary_path, 'rb') as f:
            data = f.read()

        # Simple check: is function address within 16KB of any TYPEINFO?
        nearby_structures = []
        for struct_name, typeinfo_va in TYPEINFO_ADDRESSES.items():
            distance = abs(func_addr - typeinfo_va)
            if distance < 0x4000:  # 16KB
                nearby_structures.append({
                    'struct': struct_name,
                    'typeinfo': typeinfo_va,
                    'distance': func_addr - typeinfo_va
                })

        return nearby_structures
    except:
        return []


def main():
    import sys

    binary_path = sys.argv[1] if len(sys.argv) > 1 else 'DOCS/europeo.exe'

    print("="*80)
    print("DEEP ANALYSIS OF 6 LARGE UNKNOWN FUNCTIONS")
    print("="*80)
    print()

    results = []

    for func in LARGE_UNKNOWNS:
        print(f"\n{'='*80}")
        print(f"Analyzing 0x{func['addr']:08X} - {func['instr']} instructions")
        print(f"Hypothesis: {func['hypothesis']}")
        print(f"{'='*80}\n")

        # Find extracted file
        filepath = find_extracted_file(func['addr'])
        if not filepath:
            print(f"  ❌ ERROR: Extracted file not found")
            continue

        # Parse file
        data = parse_extracted_file(filepath)

        # Analyze assembly
        patterns = analyze_assembly_patterns(data['assembly'])

        print(f"[Assembly Pattern Analysis]")
        print(f"  Instructions: {data['instructions']}")
        print(f"  Virtual calls: {patterns['Virtual calls']}")
        print(f"  Loops detected: {patterns['Loops']}")
        print(f"  Conditionals: {patterns['Conditionals']}")
        print(f"  Memory allocations: {patterns['Memory allocations']}")
        print(f"  String operations: {patterns['String operations']}")
        print(f"  Function calls: {len(data['calls'])}")
        print()

        # Check proximity to TYPEINFO
        print(f"[TYPEINFO Proximity Check]")
        nearby = correlate_with_typeinfo(binary_path, func['addr'])
        if nearby:
            print(f"  Found {len(nearby)} nearby structures:")
            for s in nearby:
                print(f"    - {s['struct']}: {s['distance']:+d} bytes from TYPEINFO")
        else:
            print(f"  No TYPEINFO addresses within 16KB")
        print()

        # Complexity analysis
        print(f"[Complexity Analysis]")
        complexity_score = (
            data['instructions'] +
            patterns['Virtual calls'] * 10 +
            patterns['Loops'] * 5 +
            len(data['calls']) * 2
        )
        print(f"  Complexity score: {complexity_score}")

        if patterns['Virtual calls'] > 5:
            print(f"  → HIGH virtual call count suggests complex OOP structure")
        if patterns['Loops'] > 3:
            print(f"  → Multiple loops suggest data processing/iteration")
        if len(data['calls']) > 20:
            print(f"  → Many function calls suggest high-level logic")

        print()

        # Show first 50 instructions
        print(f"[First 50 Instructions]")
        all_asm_lines = data['assembly'].split('\n')
        asm_lines = all_asm_lines[:50]
        for line in asm_lines:
            print(f"  {line}")
        line_count = len(all_asm_lines)
        if line_count > 50:
            print(f"  ... and {line_count - 50} more instructions")
        print()

        # Verdict
        print(f"[Educated Guess]")

        # Make guess based on patterns
        guess = "Unknown"
        confidence = "LOW"

        if patterns['Virtual calls'] > 10 and complexity_score > 500:
            guess = "TVNArea or TVNScene (complex rendering)"
            confidence = "MEDIUM"
        elif patterns['Virtual calls'] > 5 and patterns['Loops'] > 5:
            guess = "TVNCommand or event processing"
            confidence = "MEDIUM"
        elif len(data['calls']) > 30:
            guess = "High-level coordinator/manager"
            confidence = "LOW"
        elif complexity_score > 400:
            guess = "Significant structure (manual IDA check recommended)"
            confidence = "LOW"

        if nearby:
            guess += f" (near {nearby[0]['struct']})"
            confidence = "MEDIUM-HIGH"

        print(f"  Best guess: {guess}")
        print(f"  Confidence: {confidence}")
        print()

        results.append({
            'addr': func['addr'],
            'rank': func['rank'],
            'instructions': data['instructions'],
            'calls': len(data['calls']),
            'virtual_calls': patterns['Virtual calls'],
            'loops': patterns['Loops'],
            'complexity': complexity_score,
            'nearby_typeinfo': len(nearby),
            'guess': guess,
            'confidence': confidence
        })

    # Summary
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}\n")

    print(f"{'Address':<12} {'Rank':<6} {'Instr':<7} {'V-Calls':<8} {'Complex':<8} {'Guess'}")
    print("-" * 100)

    for r in results:
        print(f"0x{r['addr']:08X}  #{r['rank']:<5} {r['instructions']:<7} {r['virtual_calls']:<8} {r['complexity']:<8} {r['guess'][:60]}")

    print()

    # Generate report
    with open("LARGE_UNKNOWN_ANALYSIS.md", 'w') as f:
        f.write("# Deep Analysis of Large Unknown Functions\n\n")
        f.write(f"**Total analyzed**: {len(results)}\n\n")
        f.write("These functions have >200 instructions but 0 strings, suggesting:\n")
        f.write("- Wrapper/coordinator functions\n")
        f.write("- Complex logic that doesn't use string literals\n")
        f.write("- Important TVN structures\n\n")
        f.write("---\n\n")

        for r in results:
            f.write(f"## Function 0x{r['addr']:08X} (Rank #{r['rank']})\n\n")
            f.write(f"**Instructions**: {r['instructions']}\n")
            f.write(f"**Function calls**: {r['calls']}\n")
            f.write(f"**Virtual calls**: {r['virtual_calls']}\n")
            f.write(f"**Loops**: {r['loops']}\n")
            f.write(f"**Complexity score**: {r['complexity']}\n")
            f.write(f"**Nearby TYPEINFO**: {r['nearby_typeinfo']} structures\n\n")
            f.write(f"**Best guess**: {r['guess']}\n")
            f.write(f"**Confidence**: {r['confidence']}\n\n")
            f.write("---\n\n")

    print(f"✓ Detailed report saved to LARGE_UNKNOWN_ANALYSIS.md")
    print()


if __name__ == "__main__":
    main()
