#!/usr/bin/env python3
"""
Ghidra headless analysis script for TVN structures
Automatically finds vtables, functions, and strings
"""

import subprocess
import os
import json
import re

# Ghidra script to run inside Ghidra
GHIDRA_SCRIPT_CONTENT = '''
# Ghidra Python script - runs inside Ghidra
from ghidra.program.model.symbol import SourceType
from ghidra.program.model.listing import CodeUnit
import json

results = {
    'vtables': [],
    'functions': [],
    'strings': [],
    'typeinfo': []
}

# Find all vtables
vtableManager = currentProgram.getVTableManager()
vtables = vtableManager.getAllVTables()

print("[GHIDRA] Found {} vtables".format(len(vtables)))

for vtable in vtables:
    addr = vtable.getAddress()
    namespace = vtable.getNamespace().getName(True)

    # Get methods
    methods = []
    for entry in vtable.getFunctionEntries():
        method_addr = entry.getAddress()
        method_func = getFunctionAt(method_addr)
        if method_func:
            methods.append({
                'address': '0x{}'.format(method_addr),
                'name': method_func.getName()
            })

    results['vtables'].append({
        'address': '0x{}'.format(addr),
        'namespace': namespace,
        'methods': methods
    })

# Find all functions with "TVN" in name
listing = currentProgram.getListing()
functionManager = currentProgram.getFunctionManager()

for func in functionManager.getFunctions(True):
    fname = func.getName()
    if 'TVN' in fname or 'LoadFromINI' in fname:
        results['functions'].append({
            'address': '0x{}'.format(func.getEntryPoint()),
            'name': fname,
            'namespace': func.getParentNamespace().getName(True)
        })

# Find all strings
mem = currentProgram.getMemory()
for block in mem.getBlocks():
    if block.isInitialized():
        addr = block.getStart()
        while addr and addr.compareTo(block.getEnd()) < 0:
            data = getDataAt(addr)
            if data and data.hasStringValue():
                string_val = data.getValue()
                if string_val and len(str(string_val)) > 2:
                    # Check if TVN-related
                    s = str(string_val)
                    if 'TVN' in s or 'AREA' in s or 'NAME' in s or 'COLOR' in s:
                        results['strings'].append({
                            'address': '0x{}'.format(addr),
                            'value': s
                        })
            addr = addr.next()

# Save results
output_file = '/tmp/ghidra_results.json'
with open(output_file, 'w') as f:
    json.dump(results, f, indent=2)

print("[GHIDRA] Results saved to {}".format(output_file))
print("[GHIDRA] VTables: {}".format(len(results['vtables'])))
print("[GHIDRA] Functions: {}".format(len(results['functions'])))
print("[GHIDRA] Strings: {}".format(len(results['strings'])))
'''


def create_ghidra_script():
    """Create Ghidra script file"""
    script_path = '/tmp/analyze_tvn.py'
    with open(script_path, 'w') as f:
        f.write(GHIDRA_SCRIPT_CONTENT)
    return script_path


def run_ghidra_headless(binary_path, script_path):
    """Run Ghidra in headless mode"""
    project_dir = '/tmp/ghidra_project'
    project_name = 'europeo_analysis'

    # Clean up old project
    if os.path.exists(project_dir):
        subprocess.run(['rm', '-rf', project_dir])

    os.makedirs(project_dir, exist_ok=True)

    cmd = [
        'analyzeHeadless',
        project_dir,
        project_name,
        '-import', binary_path,
        '-postScript', script_path,
        '-deleteProject',  # Clean up after
    ]

    print("Running Ghidra headless analysis...")
    print(f"Command: {' '.join(cmd)}")
    print()

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=300  # 5 minutes max
    )

    print("STDOUT:")
    print(result.stdout)
    print("\nSTDERR:")
    print(result.stderr)

    return result.returncode == 0


def parse_ghidra_results():
    """Parse Ghidra results"""
    results_file = '/tmp/ghidra_results.json'

    if not os.path.exists(results_file):
        print("⚠️  Ghidra results file not found")
        return None

    with open(results_file, 'r') as f:
        results = json.load(f)

    return results


def save_results_markdown(results, output_file):
    """Save results to markdown"""
    with open(output_file, 'w') as f:
        f.write("# Ghidra Automatic Analysis Results\n\n")
        f.write("**Binary**: europeo.exe\n")
        f.write("**Tool**: Ghidra 12.0.1 (headless)\n\n")
        f.write("---\n\n")

        # VTables
        f.write(f"## VTables Found ({len(results['vtables'])})\n\n")
        for vtable in results['vtables']:
            f.write(f"### {vtable['namespace']} @ {vtable['address']}\n\n")
            f.write(f"**Methods**: {len(vtable['methods'])}\n\n")
            for method in vtable['methods']:
                f.write(f"- `{method['name']}` @ {method['address']}\n")
            f.write("\n")

        # Functions
        f.write(f"\n## TVN-Related Functions ({len(results['functions'])})\n\n")
        for func in results['functions']:
            f.write(f"- `{func['namespace']}::{func['name']}` @ {func['address']}\n")

        # Strings
        f.write(f"\n## TVN-Related Strings ({len(results['strings'])})\n\n")
        for string in results['strings'][:100]:  # Limit to first 100
            f.write(f"- `\"{string['value']}\"` @ {string['address']}\n")

        if len(results['strings']) > 100:
            f.write(f"\n... and {len(results['strings']) - 100} more strings\n")


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: ghidra_analyze_tvn.py <europeo.exe>")
        sys.exit(1)

    binary_path = os.path.abspath(sys.argv[1])

    print("="*80)
    print("GHIDRA HEADLESS ANALYSIS FOR TVN STRUCTURES")
    print("="*80)
    print()

    # Create script
    script_path = create_ghidra_script()
    print(f"✓ Created Ghidra script: {script_path}")

    # Run Ghidra
    success = run_ghidra_headless(binary_path, script_path)

    if not success:
        print("\n⚠️  Ghidra analysis may have failed, but continuing...")

    # Parse results
    print("\n" + "="*80)
    print("PARSING RESULTS")
    print("="*80)

    results = parse_ghidra_results()

    if results:
        print(f"\n✓ Found:")
        print(f"  - VTables: {len(results['vtables'])}")
        print(f"  - Functions: {len(results['functions'])}")
        print(f"  - Strings: {len(results['strings'])}")

        # Save to markdown
        output_file = "GHIDRA_TVN_ANALYSIS.md"
        save_results_markdown(results, output_file)
        print(f"\n✓ Results saved to {output_file}")
    else:
        print("\n❌ Could not parse Ghidra results")

    print("\n" + "="*80)
    print("DONE")
    print("="*80)


if __name__ == "__main__":
    main()
