#!/usr/bin/env python3
"""
Verify top 10 LoadFromINI candidates using already extracted data
Much simpler and more reliable than r2!
"""

import os
import re

# Top 10 candidates from correlation
TOP_CANDIDATES = [
    {'struct': 'TVNAviMedia', 'addr': 0x00405B50, 'rank': 61, 'expected': 'Video/AVI'},
    {'struct': 'TVNBitmap', 'addr': 0x0041D902, 'rank': 144, 'expected': 'DIB/Bitmap'},
    {'struct': 'TVNHtmlText', 'addr': 0x0041FAA4, 'rank': 31, 'expected': 'HTML rendering'},
    {'struct': 'TVNCDAMedia', 'addr': 0x004357CF, 'rank': 109, 'expected': 'CD audio'},
    {'struct': 'TVNWaveMedia', 'addr': 0x00437289, 'rank': 91, 'expected': 'Wave audio'},
    {'struct': 'TVNMidiMedia', 'addr': 0x00437289, 'rank': 91, 'expected': 'MIDI audio'},
    {'struct': 'TVNBmpImg', 'addr': 0x004357CF, 'rank': 109, 'expected': 'Bitmap image'},
    {'struct': 'TVNGdiObject', 'addr': 0x0041EF0A, 'rank': 15, 'expected': 'GDI object'},
    {'struct': 'TVNEventCommand', 'addr': 0x00411D4D, 'rank': 1, 'expected': 'Event/command'},
    {'struct': 'TVNToolBar', 'addr': 0x004357CF, 'rank': 109, 'expected': 'Toolbar UI'},
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
    strings_match = re.search(r'\*\*Total unique strings\*\*: (\d+)', content)

    data['address'] = addr_match.group(1) if addr_match else None
    data['rank'] = int(rank_match.group(1)) if rank_match else 0
    data['instructions'] = int(instr_match.group(1)) if instr_match else 0
    data['string_count'] = int(strings_match.group(1)) if strings_match else 0

    # Extract strings
    strings_section = re.search(r'## Strings Referenced.*?\n(.*?)(?=##|\Z)', content, re.DOTALL)
    strings = []
    if strings_section:
        string_pattern = r'- `"(.+?)"` @ (0x[0-9A-F]+)'
        for match in re.finditer(string_pattern, strings_section.group(1)):
            strings.append(match.group(1))

    data['strings'] = strings

    # Extract first 30 assembly instructions
    asm_section = re.search(r'## Assembly Code.*?```assembly\n(.*?)\n```', content, re.DOTALL)
    if asm_section:
        asm_lines = asm_section.group(1).split('\n')[:30]
        data['assembly'] = '\n'.join(asm_lines)
    else:
        data['assembly'] = 'No assembly found'

    return data


def analyze_candidate(candidate):
    """Analyze a candidate structure"""
    print(f"\n{'='*80}")
    print(f"Analyzing: {candidate['struct']} @ 0x{candidate['addr']:08X}")
    print(f"Expected: {candidate['expected']}")
    print(f"{'='*80}\n")

    # Find extracted file
    filepath = find_extracted_file(candidate['addr'])

    if not filepath:
        print(f"  ❌ ERROR: Extracted file not found for 0x{candidate['addr']:08X}")
        return None

    # Parse file
    data = parse_extracted_file(filepath)

    print(f"[Metadata]")
    print(f"  Rank: #{data['rank']}")
    print(f"  Instructions: {data['instructions']}")
    print(f"  Unique strings: {data['string_count']}\n")

    # Analyze strings for structure indicators
    print(f"[String Analysis]")
    if data['strings']:
        print(f"  Found {len(data['strings'])} strings:")
        for i, s in enumerate(data['strings'][:15], 1):
            # Highlight interesting strings
            highlight = ""
            s_upper = s.upper()
            if any(kw in s_upper for kw in ['DIB', 'BITMAP', 'BMP', 'PALETTE']):
                highlight = " ⭐ BITMAP RELATED"
            elif any(kw in s_upper for kw in ['AVI', 'VIDEO', 'FRAME']):
                highlight = " ⭐ VIDEO RELATED"
            elif any(kw in s_upper for kw in ['WAVE', 'MIDI', 'AUDIO', 'SOUND']):
                highlight = " ⭐ AUDIO RELATED"
            elif any(kw in s_upper for kw in ['HTML', 'TAG', 'HREF']):
                highlight = " ⭐ HTML RELATED"
            elif any(kw in s_upper for kw in ['GDI', 'DC', 'HANDLE']):
                highlight = " ⭐ GDI RELATED"
            elif any(kw in s_upper for kw in ['COMMAND', 'EVENT', 'ACTION']):
                highlight = " ⭐ COMMAND RELATED"

            print(f"    {i:2d}. \"{s[:60]}...\"{highlight}" if len(s) > 60 else f"    {i:2d}. \"{s}\"{highlight}")

        if len(data['strings']) > 15:
            print(f"    ... and {len(data['strings']) - 15} more")
    else:
        print(f"  ⚠️  No strings found (wrapper function?)")

    print(f"\n[First 20 Instructions]")
    asm_lines = data['assembly'].split('\n')[:20]
    for line in asm_lines:
        print(f"  {line}")

    # Verdict
    print(f"\n[Verdict]")
    confidence = "???"
    if data['string_count'] > 5:
        confidence = "HIGH ✓✓✓"
    elif data['string_count'] > 0:
        confidence = "MEDIUM ✓✓"
    elif data['instructions'] > 200:
        confidence = "LOW ✓ (large function, manual check needed)"
    else:
        confidence = "VERY LOW ✗ (small wrapper?)"

    print(f"  Confidence: {confidence}")
    print(f"  Instructions: {data['instructions']}")
    print(f"  Strings: {data['string_count']}")

    return {
        'struct': candidate['struct'],
        'addr': candidate['addr'],
        'instructions': data['instructions'],
        'strings': data['string_count'],
        'confidence': confidence
    }


def main():
    print("="*80)
    print("TOP 10 CANDIDATES VERIFICATION")
    print("Using already extracted LoadFromINI data")
    print("="*80)

    results = []

    for candidate in TOP_CANDIDATES:
        result = analyze_candidate(candidate)
        if result:
            results.append(result)

    # Summary
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}\n")

    print(f"{'Structure':<20} {'Address':<12} {'Instr':<8} {'Strings':<8} {'Confidence'}")
    print("-" * 80)

    for r in results:
        print(f"{r['struct']:<20} 0x{r['addr']:08X}  {r['instructions']:<8} {r['strings']:<8} {r['confidence']}")

    # Group by confidence
    print(f"\n{'='*80}")
    print("BY CONFIDENCE LEVEL")
    print(f"{'='*80}\n")

    high_conf = [r for r in results if 'HIGH' in r['confidence']]
    med_conf = [r for r in results if 'MEDIUM' in r['confidence']]
    low_conf = [r for r in results if 'LOW' in r['confidence']]

    print(f"HIGH confidence ({len(high_conf)}): {', '.join([r['struct'] for r in high_conf])}")
    print(f"MEDIUM confidence ({len(med_conf)}): {', '.join([r['struct'] for r in med_conf])}")
    print(f"LOW confidence ({len(low_conf)}): {', '.join([r['struct'] for r in low_conf])}")

    print()


if __name__ == "__main__":
    main()
