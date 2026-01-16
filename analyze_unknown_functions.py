#!/usr/bin/env python3
"""
Analyze Unknown functions in detail to identify TVN structures
Focus on large functions and string patterns
"""

import os
import re
from collections import defaultdict

def parse_extracted_md(file_path):
    """Parse an extracted function markdown file"""
    with open(file_path, 'r') as f:
        content = f.read()

    data = {}

    # Extract header info
    addr_match = re.search(r'\*\*Function Address\*\*: (0x[0-9A-F]+)', content)
    rank_match = re.search(r'\*\*Rank\*\*: #(\d+)', content)
    ini_count_match = re.search(r'\*\*INI String Count\*\*: (\d+)', content)
    struct_match = re.search(r'\*\*Identified Structure\*\*: (.+)', content)
    confidence_match = re.search(r'\*\*Confidence Score\*\*: (\d+)', content)
    instr_count_match = re.search(r'\*\*Instructions\*\*: (\d+)', content)

    data['address'] = addr_match.group(1) if addr_match else None
    data['rank'] = int(rank_match.group(1)) if rank_match else 0
    data['ini_count'] = int(ini_count_match.group(1)) if ini_count_match else 0
    data['structure'] = struct_match.group(1) if struct_match else 'Unknown'
    data['confidence'] = int(confidence_match.group(1)) if confidence_match else 0
    data['instruction_count'] = int(instr_count_match.group(1)) if instr_count_match else 0

    # Extract strings
    strings_section = re.search(r'## Strings Referenced\s+\*\*Total unique strings\*\*: (\d+)\s+(.*?)(?=##|---|\Z)', content, re.DOTALL)
    data['string_count'] = int(strings_section.group(1)) if strings_section else 0

    strings = []
    if strings_section:
        string_pattern = r'- `"(.+?)"` @ (0x[0-9A-F]+)'
        for match in re.finditer(string_pattern, strings_section.group(2)):
            strings.append({
                'text': match.group(1),
                'address': match.group(2)
            })
    data['strings'] = strings

    return data


def analyze_string_patterns(strings):
    """Analyze strings to identify TVN structure type"""
    all_text = ' '.join([s['text'].upper() for s in strings])

    # Enhanced keyword detection for missing structures
    patterns = {
        'TVNSound': [
            r'SOUND', r'MUSIC', r'VOLUME', r'WAVE', r'WAV', r'MP3', r'AUDIO',
            r'PLAY', r'STOP', r'LOOP', r'FADE'
        ],
        'TVNVideo': [
            r'VIDEO', r'AVI', r'MPEG', r'MOVIE', r'FRAME', r'FPS',
            r'PLAY.*VIDEO', r'VIDEO.*PLAY'
        ],
        'TVNArea': [
            r'AREA_', r'BKCOLOR', r'BACKGROUND', r'TEXTURE', r'AREANAME',
            r'AREA\s*NAME', r'AREA\s*COLOR'
        ],
        'TVNCommand': [
            r'COMMAND', r'CMD', r'ACTION', r'EVENT', r'EXECUTE', r'RUN',
            r'DOCOMMAND', r'RUNCOMMAND'
        ],
        'TVNFont': [
            r'FONT', r'TYPEFACE', r'FONTNAME', r'FONTSIZE', r'FONTSTYLE',
            r'BOLD', r'ITALIC', r'UNDERLINE'
        ],
        'TVNBitmap': [
            r'BITMAP', r'BMP', r'DIB', r'PIXMAP', r'IMAGE.*FILE'
        ],
        'TVNSprite': [
            r'SPRITE', r'ANIMATION', r'ANIMATE', r'FRAME\s*\d+', r'FRAMES'
        ],
        'TVNCursor': [
            r'CURSOR', r'MOUSE', r'POINTER', r'CURSORTYPE', r'SETCURSOR'
        ],
        'TVNRect': [
            r'RECT', r'RECTANGLE', r'LEFT.*RIGHT.*TOP.*BOTTOM',
            r'X\s*Y\s*WIDTH\s*HEIGHT'
        ],
        'TVNPoint': [
            r'POINT', r'COORD', r'X\s*Y', r'POSITION'
        ],
        'TVNMenu': [
            r'MENU', r'MENUITEM', r'POPUP', r'SUBMENU'
        ],
        'TVNButton': [
            r'BUTTON', r'BTN', r'CLICK', r'PRESSED'
        ],
        'TVNDialog': [
            r'DIALOG', r'DLG', r'MODAL', r'MESSAGEBOX'
        ],
        'TVNWindow': [
            r'WINDOW', r'WND', r'HWND', r'CREATEWINDOW'
        ],
    }

    scores = {}
    matched_keywords = {}

    for struct_name, keywords in patterns.items():
        score = 0
        matches = []
        for keyword in keywords:
            if re.search(keyword, all_text):
                score += 1
                matches.append(keyword)

        if score > 0:
            scores[struct_name] = score
            matched_keywords[struct_name] = matches

    return scores, matched_keywords


def main():
    extract_dir = "LOADFROMINI_EXTRACTED"

    print("="*80)
    print("DEEP ANALYSIS OF UNKNOWN FUNCTIONS")
    print("="*80)
    print()

    # Parse all Unknown functions
    unknown_funcs = []

    for filename in sorted(os.listdir(extract_dir)):
        if filename.endswith('_Unknown.md'):
            file_path = os.path.join(extract_dir, filename)
            func_data = parse_extracted_md(file_path)
            func_data['filename'] = filename

            # Analyze string patterns
            scores, keywords = analyze_string_patterns(func_data['strings'])
            func_data['pattern_scores'] = scores
            func_data['matched_keywords'] = keywords

            unknown_funcs.append(func_data)

    print(f"Found {len(unknown_funcs)} Unknown functions\n")

    # Group by potential structure
    potential_structures = defaultdict(list)

    for func in unknown_funcs:
        if func['pattern_scores']:
            # Get best match
            best_match = max(func['pattern_scores'].items(), key=lambda x: x[1])
            potential_structures[best_match[0]].append(func)
        else:
            potential_structures['Truly Unknown'].append(func)

    # Generate detailed report
    output_file = "UNKNOWN_FUNCTIONS_ANALYSIS.md"

    with open(output_file, 'w') as f:
        f.write("# Unknown Functions Deep Analysis\n\n")
        f.write(f"**Total Unknown functions**: {len(unknown_funcs)}\n\n")
        f.write("---\n\n")

        # Summary by potential structure
        f.write("## Potential Structure Identification\n\n")
        for struct_name in sorted(potential_structures.keys()):
            funcs = potential_structures[struct_name]
            f.write(f"### {struct_name} ({len(funcs)} candidates)\n\n")

            # Sort by confidence (pattern score + instruction count)
            funcs.sort(key=lambda x: (
                max(x['pattern_scores'].values()) if x['pattern_scores'] else 0,
                x['instruction_count']
            ), reverse=True)

            for func in funcs[:10]:  # Top 10 per category
                score = max(func['pattern_scores'].values()) if func['pattern_scores'] else 0
                f.write(f"**Rank #{func['rank']:03d}**: {func['address']}\n")
                f.write(f"- Instructions: {func['instruction_count']}\n")
                f.write(f"- Strings: {func['string_count']}\n")
                f.write(f"- Pattern score: {score}\n")

                if func['matched_keywords'] and struct_name in func['matched_keywords']:
                    f.write(f"- Matched keywords: {', '.join(func['matched_keywords'][struct_name][:5])}\n")

                if func['strings'][:5]:
                    f.write("- Sample strings:\n")
                    for s in func['strings'][:5]:
                        f.write(f"  - `\"{s['text'][:60]}...\"`\n" if len(s['text']) > 60 else f"  - `\"{s['text']}\"`\n")

                f.write("\n")

            if len(funcs) > 10:
                f.write(f"... and {len(funcs) - 10} more candidates\n\n")

        # Priority analysis: Large functions
        f.write("## Large Unknown Functions (>200 instructions)\n\n")
        f.write("These are prime candidates for manual IDA analysis.\n\n")

        large_funcs = [f for f in unknown_funcs if f['instruction_count'] > 200]
        large_funcs.sort(key=lambda x: x['instruction_count'], reverse=True)

        for func in large_funcs:
            f.write(f"### Rank #{func['rank']:03d}: {func['address']}\n\n")
            f.write(f"**Instructions**: {func['instruction_count']}\n")
            f.write(f"**Strings**: {func['string_count']}\n")
            f.write(f"**INI Keywords**: {func['ini_count']}\n\n")

            if func['pattern_scores']:
                f.write("**Potential structures**:\n")
                for struct, score in sorted(func['pattern_scores'].items(), key=lambda x: x[1], reverse=True):
                    f.write(f"- {struct}: score {score}\n")
                f.write("\n")

            if func['strings']:
                f.write("**All strings**:\n")
                for s in func['strings']:
                    f.write(f"- `\"{s['text']}\"`\n")
                f.write("\n")

            f.write("---\n\n")

        # Statistics
        f.write("## Statistics\n\n")
        f.write(f"- Unknown functions with pattern matches: {sum(1 for f in unknown_funcs if f['pattern_scores'])}\n")
        f.write(f"- Truly unknown (no patterns): {len(potential_structures['Truly Unknown'])}\n")
        f.write(f"- Large functions (>200 instr): {len(large_funcs)}\n")
        f.write(f"- Functions with strings: {sum(1 for f in unknown_funcs if f['string_count'] > 0)}\n")
        f.write(f"- Functions with 0 strings: {sum(1 for f in unknown_funcs if f['string_count'] == 0)}\n")

    print(f"✓ Analysis saved to {output_file}\n")

    # Console summary
    print("Potential Structure Identification:")
    print("-" * 80)
    for struct_name in sorted(potential_structures.keys()):
        funcs = potential_structures[struct_name]
        print(f"{struct_name:20s}: {len(funcs):3d} candidates")

    print("\nTop 10 Large Unknown Functions:")
    print("-" * 80)
    large_funcs = [f for f in unknown_funcs if f['instruction_count'] > 200]
    large_funcs.sort(key=lambda x: x['instruction_count'], reverse=True)

    for i, func in enumerate(large_funcs[:10]):
        best_match = "No pattern"
        if func['pattern_scores']:
            best_match = max(func['pattern_scores'].items(), key=lambda x: x[1])[0]
        print(f"  {i+1:2d}. {func['address']} - {func['instruction_count']:4d} instr, {func['string_count']:2d} strings - {best_match}")

    print()


if __name__ == "__main__":
    main()
