"""
IDA Python script to find missing vtables for 13 TVN structures
Uses multiple strategies to locate vtables
Run in IDA: File -> Script file...
"""

import idc
import idaapi
import idautils

# Structures with missing vtables
MISSING_STRUCTURES = [
    "TVNFileNameParms",
    "TVNEventCommand",
    "TVNVariable",
    "TVNScene",
    "TVNToolBar",
    "TVNWindow",
    "TVNApplication",
    "TVNAviMedia",
    "TVNWaveMedia",
    "TVNMidiMedia",
    "TVNCDAMedia",
    "TVNBitmap",
    "TVNGdiObject",
    "TVNHtmlText",
    "TVNImageObject",
    "TVNTextObject",
    "TVNBmpImg",
]


def is_valid_code_pointer(addr):
    """Check if address is valid code"""
    if addr < 0x00401000 or addr > 0x00500000:
        return False
    flags = idc.get_full_flags(addr)
    return idc.is_code(flags)


def is_valid_data_pointer(addr):
    """Check if address is in data section"""
    return 0x00400000 <= addr <= 0x00500000


def find_type_string(struct_name):
    """Find the type string for a structure (e.g. "TVNVariable *")"""

    # Try different patterns
    patterns = [
        struct_name + " *",
        struct_name + "*",
        struct_name,
    ]

    for pattern in patterns:
        # Search for the string
        addr = idc.find_text(0, idc.SEARCH_DOWN, 0, 0, pattern)
        if addr != idc.BADADDR:
            print(f"  Found type string '{pattern}' @ 0x{addr:08X}")
            return addr

    return None


def check_vtable_validity(vtable_addr):
    """Check if an address looks like a valid vtable"""

    methods = []

    for offset in range(0, 0x40, 4):  # Check up to 16 methods
        method_ptr = idc.get_wide_dword(vtable_addr + offset)

        if method_ptr == 0:
            break

        if not is_valid_code_pointer(method_ptr):
            if offset == 0:
                return None  # First entry must be valid
            break

        methods.append(method_ptr)

    if len(methods) >= 2:  # At least 2 methods
        return methods

    return None


def find_vtable_near_string(string_addr):
    """Find vtable by searching near the type string"""

    if not string_addr:
        return []

    candidates = []

    # Search backwards up to 0x500 bytes
    for offset in range(4, 0x500, 4):
        check_addr = string_addr - offset

        methods = check_vtable_validity(check_addr)
        if methods:
            candidates.append({
                'address': check_addr,
                'methods': methods,
                'distance': offset,
                'direction': 'before'
            })

    # Search forwards up to 0x200 bytes
    for offset in range(4, 0x200, 4):
        check_addr = string_addr + offset

        methods = check_vtable_validity(check_addr)
        if methods:
            candidates.append({
                'address': check_addr,
                'methods': methods,
                'distance': offset,
                'direction': 'after'
            })

    return candidates


def find_constructor_references(struct_name):
    """Find constructor functions that might initialize the vtable"""

    constructors = []

    # Search for "mov dword ptr [reg], offset vtable"
    # This is the pattern: C7 01 [vtable_addr] or similar

    # We'll look for functions that reference the type string
    string_addr = find_type_string(struct_name)
    if not string_addr:
        return []

    # Find all code references to the string
    for xref in idautils.XrefsTo(string_addr):
        if xref.type == idaapi.fl_F:  # Code flow reference
            # Get the function containing this reference
            func = idaapi.get_func(xref.frm)
            if func:
                constructors.append({
                    'address': func.start_ea,
                    'name': idc.get_func_name(func.start_ea),
                    'xref_from': xref.frm
                })

    return constructors


def analyze_constructor_for_vtable(func_addr):
    """Analyze a constructor function to find vtable initialization"""

    func = idaapi.get_func(func_addr)
    if not func:
        return []

    vtables_found = []
    ea = func.start_ea

    while ea < func.end_ea:
        # Look for "mov [reg], imm32" patterns
        mnem = idc.print_insn_mnem(ea)

        if mnem == 'mov':
            # Get operands
            op0 = idc.print_operand(ea, 0)
            op1 = idc.print_operand(ea, 1)

            # Check if it's a memory write with immediate
            if '[' in op0 and 'offset' in op1:
                # Extract the address
                import re
                match = re.search(r'offset\s+([a-zA-Z0-9_]+)', op1)
                if match:
                    name = match.group(1)
                    addr = idc.get_name_ea_simple(name)
                    if addr != idc.BADADDR:
                        # Check if it's a valid vtable
                        methods = check_vtable_validity(addr)
                        if methods:
                            vtables_found.append({
                                'address': addr,
                                'methods': methods,
                                'instr_addr': ea
                            })

        ea = idc.next_head(ea, func.end_ea)

    return vtables_found


def find_vtable_for_structure(struct_name):
    """Complete search for a structure's vtable"""

    print(f"\n{'='*100}")
    print(f"SEARCHING: {struct_name}")
    print(f"{'='*100}")

    results = {
        'struct_name': struct_name,
        'type_string_addr': None,
        'vtable_candidates': [],
        'constructors': [],
    }

    # Step 1: Find type string
    print(f"  Step 1: Finding type string...")
    string_addr = find_type_string(struct_name)
    results['type_string_addr'] = string_addr

    if not string_addr:
        print(f"  ⚠️  Type string not found")
        return results

    # Step 2: Search near type string
    print(f"  Step 2: Searching for vtables near type string...")
    candidates = find_vtable_near_string(string_addr)
    results['vtable_candidates'].extend(candidates)

    if candidates:
        print(f"  ✓ Found {len(candidates)} vtable candidate(s) near string")
        for i, cand in enumerate(candidates[:3]):  # Show top 3
            print(f"    #{i+1}: 0x{cand['address']:08X} - {len(cand['methods'])} methods - {cand['distance']} bytes {cand['direction']}")

    # Step 3: Find constructors
    print(f"  Step 3: Finding constructor functions...")
    constructors = find_constructor_references(struct_name)
    results['constructors'] = constructors

    if constructors:
        print(f"  ✓ Found {len(constructors)} constructor candidate(s)")
        for cons in constructors[:3]:  # Show top 3
            print(f"    - {cons['name']} @ 0x{cons['address']:08X}")

            # Analyze constructor
            vtables = analyze_constructor_for_vtable(cons['address'])
            if vtables:
                print(f"      → Found {len(vtables)} vtable(s) in constructor")
                results['vtable_candidates'].extend(vtables)

    # Summary
    unique_vtables = {}
    for cand in results['vtable_candidates']:
        addr = cand['address']
        if addr not in unique_vtables:
            unique_vtables[addr] = cand

    if unique_vtables:
        print(f"\n  ✅ FOUND {len(unique_vtables)} unique vtable(s):")
        for addr, cand in sorted(unique_vtables.items()):
            print(f"     0x{addr:08X} - {len(cand.get('methods', []))} methods")
    else:
        print(f"\n  ❌ No vtables found")

    results['unique_vtables'] = unique_vtables
    return results


def save_results(all_results):
    """Save results to a file"""

    output_file = "MISSING_VTABLES_FOUND.md"

    with open(output_file, 'w') as f:
        f.write("# Missing TVN Vtables - Search Results\n\n")
        f.write("Automated search for vtables of 13+ missing TVN structures.\n\n")
        f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")
        f.write("| Structure | Vtables Found | Type String |\n")
        f.write("|-----------|---------------|-------------|\n")

        for result in all_results:
            name = result['struct_name']
            num_vtables = len(result.get('unique_vtables', {}))
            string_status = "✓" if result['type_string_addr'] else "✗"

            f.write(f"| {name:20s} | {num_vtables:2d} | {string_status} |\n")

        f.write("\n---\n\n")

        # Detailed results
        f.write("## Detailed Results\n\n")

        for result in all_results:
            name = result['struct_name']
            f.write(f"### {name}\n\n")

            if result['type_string_addr']:
                f.write(f"**Type String**: Found @ 0x{result['type_string_addr']:08X}\n\n")
            else:
                f.write(f"**Type String**: ⚠️ Not found\n\n")

            unique_vtables = result.get('unique_vtables', {})

            if unique_vtables:
                f.write(f"**Vtables Found**: {len(unique_vtables)}\n\n")

                for addr, vtable in sorted(unique_vtables.items()):
                    f.write(f"#### Vtable @ 0x{addr:08X}\n\n")
                    f.write(f"- **Address**: 0x{addr:08X}\n")
                    f.write(f"- **Methods**: {len(vtable.get('methods', []))}\n\n")

                    f.write("**Methods**:\n\n")
                    for i, method in enumerate(vtable.get('methods', [])):
                        func_name = idc.get_func_name(method) or f"sub_{method:X}"
                        f.write(f"- [{i}] 0x{method:08X} - `{func_name}`\n")
                    f.write("\n")
            else:
                f.write(f"**Vtables Found**: ❌ None\n\n")

            if result['constructors']:
                f.write(f"**Constructors Found**: {len(result['constructors'])}\n\n")
                for cons in result['constructors']:
                    f.write(f"- `{cons['name']}` @ 0x{cons['address']:08X}\n")
                f.write("\n")

            f.write("---\n\n")

        # Code to add to main script
        f.write("## Code for Main Script\n\n")
        f.write("Add these vtables to `extract_all_35_tvn_complete.py`:\n\n")
        f.write("```python\n")

        for result in all_results:
            name = result['struct_name']
            unique_vtables = result.get('unique_vtables', {})

            if unique_vtables:
                # Take the first (most likely) vtable
                addr = sorted(unique_vtables.keys())[0]
                f.write(f'    "{name}": 0x{addr:08X},\n')
            else:
                f.write(f'    "{name}": None,  # TODO - Not found\n')

        f.write("```\n\n")

    print(f"\n✓ Results saved to {output_file}")


def main():
    """Main search function"""

    print("="*100)
    print("FINDING MISSING TVN VTABLES")
    print("="*100)
    print()
    print(f"Structures to search: {len(MISSING_STRUCTURES)}")
    print()

    # Wait for analysis
    idaapi.auto_wait()

    # Search each structure
    all_results = []

    for struct_name in MISSING_STRUCTURES:
        result = find_vtable_for_structure(struct_name)
        all_results.append(result)

    # Save results
    print("\n" + "="*100)
    print("SEARCH COMPLETE")
    print("="*100)

    total_found = sum(len(r.get('unique_vtables', {})) for r in all_results)
    structures_found = sum(1 for r in all_results if r.get('unique_vtables'))

    print(f"\nStructures searched: {len(MISSING_STRUCTURES)}")
    print(f"Structures with vtables found: {structures_found}")
    print(f"Total vtables found: {total_found}")
    print()

    save_results(all_results)

    print("\n✓ Done! Check MISSING_VTABLES_FOUND.md for results.")
    print("\n📝 Next step: Copy vtable addresses to extract_all_35_tvn_complete.py")


if __name__ == "__main__":
    main()
