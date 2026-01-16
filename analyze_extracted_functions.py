#!/usr/bin/env python3
"""
Analyze all extracted LoadFromINI functions and create comprehensive summary
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


def categorize_by_strings(func_data):
    """Try to categorize function by analyzing its strings"""
    strings_text = ' '.join([s['text'].upper() for s in func_data['strings']])

    # Enhanced keyword matching
    categories = {
        'TVNScene': ['SCENE', 'AREA_', 'HOTSPOT_', 'HSCUR_', 'HSRGN_', 'HSCMD_', 'HSVIDEO'],
        'TVNHotspot': ['HOTSPOT_', 'HSCUR', 'CURSOR', 'COMMAND', 'HSRGN'],
        'TVNArea': ['AREA_', 'BKCOLOR', 'TEXTURE', 'AREANAME'],
        'TVNTextObject': ['TEXT', 'FONT', 'COLOR', 'SIZE', 'FACE'],
        'TVNImageObject': ['IMAGE', 'BITMAP', 'POSITION', 'SPRITE'],
        'TVNSound': ['SOUND', 'MUSIC', 'VOLUME', 'WAVE'],
        'TVNCommand': ['COMMAND', 'ACTION', 'EVENT', 'CMD'],
        'TVNFont': ['FONT', 'CAPS', 'HEIGHT', 'TYPEFACE'],
        'TVNVideo': ['VIDEO', 'FRAME', 'SPEED', 'AVI'],
        'TVNString': ['STRING', 'TEXT', 'CHAR'],
        'TVNHtml': ['HTML', 'TAG', 'HREF'],
        'TVNIf': ['IF', 'CONDITION', 'THEN', 'ELSE'],
        'Registry': ['HKEY_', 'REGISTRY', 'REG_'],
        'Utility': ['CHECK', 'PRECONDITION', 'VECTOR', 'ARRAY'],
    }

    scores = {}
    for category, keywords in categories.items():
        score = sum(1 for kw in keywords if kw in strings_text)
        if score > 0:
            scores[category] = score

    if scores:
        best = max(scores.items(), key=lambda x: x[1])
        return best[0], best[1], scores

    return 'Unknown', 0, {}


def main():
    extract_dir = "LOADFROMINI_EXTRACTED"

    if not os.path.exists(extract_dir):
        print(f"Error: {extract_dir} not found")
        return

    print("="*80)
    print("LOADFROMINI EXTRACTION ANALYSIS")
    print("="*80)
    print()

    # Parse all files
    all_funcs = []
    for filename in sorted(os.listdir(extract_dir)):
        if filename.endswith('.md'):
            file_path = os.path.join(extract_dir, filename)
            func_data = parse_extracted_md(file_path)
            func_data['filename'] = filename

            # Re-categorize with better algorithm
            new_category, new_score, all_scores = categorize_by_strings(func_data)
            func_data['recategorized'] = new_category
            func_data['recategorized_score'] = new_score
            func_data['all_category_scores'] = all_scores

            all_funcs.append(func_data)

    print(f"Analyzed {len(all_funcs)} functions\n")

    # Group by original categorization
    by_original = defaultdict(list)
    for func in all_funcs:
        by_original[func['structure']].append(func)

    # Group by recategorization
    by_new = defaultdict(list)
    for func in all_funcs:
        by_new[func['recategorized']].append(func)

    # Generate summary report
    output_file = "EXTRACTION_SUMMARY.md"
    with open(output_file, 'w') as f:
        f.write("# LoadFromINI Extraction Summary\n\n")
        f.write(f"**Total functions extracted**: {len(all_funcs)}\n\n")
        f.write("---\n\n")

        # Original categorization
        f.write("## Original Categorization\n\n")
        for category in sorted(by_original.keys()):
            funcs = by_original[category]
            f.write(f"### {category} ({len(funcs)} functions)\n\n")
            for func in funcs:
                f.write(f"- Rank #{func['rank']:03d}: {func['address']} - {func['instruction_count']} instr, {func['string_count']} strings\n")
            f.write("\n")

        # Recategorization
        f.write("## Re-categorization (Improved)\n\n")
        for category in sorted(by_new.keys()):
            funcs = by_new[category]
            f.write(f"### {category} ({len(funcs)} functions)\n\n")
            for func in funcs:
                f.write(f"- Rank #{func['rank']:03d}: {func['address']} - {func['instruction_count']} instr, {func['string_count']} strings")
                if func['recategorized'] != func['structure']:
                    f.write(f" *(was: {func['structure']})*")
                f.write("\n")
            f.write("\n")

        # Detailed analysis
        f.write("## Detailed Function Analysis\n\n")
        for func in sorted(all_funcs, key=lambda x: x['rank']):
            f.write(f"### Rank #{func['rank']:03d}: {func['address']}\n\n")
            f.write(f"**Original**: {func['structure']} (score: {func['confidence']})\n\n")
            f.write(f"**Re-categorized**: {func['recategorized']} (score: {func['recategorized_score']})\n\n")
            f.write(f"**Statistics**:\n")
            f.write(f"- Instructions: {func['instruction_count']}\n")
            f.write(f"- Unique strings: {func['string_count']}\n")
            f.write(f"- INI string count: {func['ini_count']}\n\n")

            if func['all_category_scores']:
                f.write("**Category scores**:\n")
                for cat, score in sorted(func['all_category_scores'].items(), key=lambda x: x[1], reverse=True):
                    f.write(f"- {cat}: {score}\n")
                f.write("\n")

            if func['strings']:
                f.write("**Key strings** (first 10):\n")
                for s in func['strings'][:10]:
                    f.write(f"- `\"{s['text']}\"` @ {s['address']}\n")
                if len(func['strings']) > 10:
                    f.write(f"- ... and {len(func['strings']) - 10} more\n")
                f.write("\n")

            f.write("---\n\n")

        # Statistics
        f.write("## Statistics\n\n")
        f.write("### By instruction count\n\n")
        for func in sorted(all_funcs, key=lambda x: x['instruction_count'], reverse=True)[:20]:
            f.write(f"- {func['address']}: {func['instruction_count']} instructions ({func['recategorized']})\n")
        f.write("\n")

        f.write("### By string count\n\n")
        for func in sorted(all_funcs, key=lambda x: x['string_count'], reverse=True)[:20]:
            f.write(f"- {func['address']}: {func['string_count']} unique strings ({func['recategorized']})\n")
        f.write("\n")

    print(f"✓ Summary saved to {output_file}")

    # Console output
    print("\nRe-categorization Summary:")
    print("-" * 80)
    for category in sorted(by_new.keys()):
        funcs = by_new[category]
        print(f"{category:20s}: {len(funcs):3d} functions")

    print("\nTop 10 by instruction count:")
    print("-" * 80)
    for func in sorted(all_funcs, key=lambda x: x['instruction_count'], reverse=True)[:10]:
        print(f"  {func['address']} - {func['instruction_count']:4d} instr - {func['recategorized']}")

    print("\nTop 10 by string count:")
    print("-" * 80)
    for func in sorted(all_funcs, key=lambda x: x['string_count'], reverse=True)[:10]:
        print(f"  {func['address']} - {func['string_count']:3d} strings - {func['recategorized']}")

    print()


if __name__ == "__main__":
    main()
