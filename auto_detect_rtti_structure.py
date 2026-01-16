#!/usr/bin/env python3
"""
Automatic RTTI structure detection
Tries different offset combinations to find the correct Borland RTTI layout
"""

import struct
import sys

def parse_pe_sections(data):
    """Parse PE sections"""
    pe_offset = struct.unpack('<I', data[0x3C:0x40])[0]
    coff_offset = pe_offset + 4
    num_sections = struct.unpack('<H', data[coff_offset+2:coff_offset+4])[0]
    size_of_optional = struct.unpack('<H', data[coff_offset+16:coff_offset+18])[0]
    section_offset = coff_offset + 20 + size_of_optional

    sections = []
    for i in range(num_sections):
        sec_data = data[section_offset + i*40:section_offset + (i+1)*40]
        sections.append({
            'Name': sec_data[0:8].rstrip(b'\x00').decode('ascii', errors='ignore'),
            'VirtualSize': struct.unpack('<I', sec_data[8:12])[0],
            'VirtualAddress': struct.unpack('<I', sec_data[12:16])[0],
            'SizeOfRawData': struct.unpack('<I', sec_data[16:20])[0],
            'PointerToRawData': struct.unpack('<I', sec_data[20:24])[0]
        })
    return sections


def va_to_file_offset(va, sections):
    """Convert VA to file offset"""
    va_no_base = va - 0x00400000 if va >= 0x00400000 else va
    for section in sections:
        virt_start = section['VirtualAddress']
        virt_end = virt_start + section['VirtualSize']
        if virt_start <= va_no_base < virt_end:
            offset_in_section = va_no_base - virt_start
            if offset_in_section < section['SizeOfRawData']:
                return section['PointerToRawData'] + offset_in_section
    return None


def read_dword(data, offset):
    if offset < 0 or offset + 4 > len(data):
        return None
    return struct.unpack('<I', data[offset:offset+4])[0]


def read_string(data, offset, max_len=64):
    if offset < 0 or offset >= len(data):
        return None
    result = []
    for i in range(max_len):
        if offset + i >= len(data):
            break
        byte = data[offset + i]
        if byte == 0:
            break
        if 32 <= byte <= 126:
            result.append(chr(byte))
        else:
            break
    return ''.join(result) if len(result) >= 3 else None


def is_valid_code_pointer(addr):
    return 0x00401000 <= addr <= 0x00500000


def is_valid_data_pointer(addr):
    return 0x00400000 <= addr <= 0x00500000


def check_if_vtable(data, sections, va):
    """Check if address looks like a vtable (array of code pointers)"""
    offset = va_to_file_offset(va, sections)
    if offset is None:
        return False

    # Check first 4 pointers
    valid_count = 0
    for i in range(4):
        ptr = read_dword(data, offset + i*4)
        if ptr and is_valid_code_pointer(ptr):
            valid_count += 1

    return valid_count >= 2


def try_parse_rtti(data, sections, va, offset_config):
    """
    Try to parse RTTI with a specific offset configuration

    offset_config = {
        'vtable': 0,      # offset for vtable pointer
        'parent': 4,      # offset for parent pointer
        'destructor': 8,  # offset for destructor
        'name': 12        # offset for name string
    }
    """
    file_offset = va_to_file_offset(va, sections)
    if file_offset is None:
        return None

    result = {
        'config': offset_config,
        'score': 0,
        'details': {}
    }

    # Read vtable pointer
    vtable_offset = offset_config['vtable']
    vtable_ptr = read_dword(data, file_offset + vtable_offset)
    if vtable_ptr:
        result['details']['vtable'] = f"0x{vtable_ptr:08X}"
        if check_if_vtable(data, sections, vtable_ptr):
            result['score'] += 20  # Big bonus if it's a valid vtable

    # Read parent pointer
    parent_offset = offset_config['parent']
    parent_ptr = read_dword(data, file_offset + parent_offset)
    if parent_ptr:
        result['details']['parent'] = f"0x{parent_ptr:08X}"
        if is_valid_data_pointer(parent_ptr):
            result['score'] += 5

    # Read destructor
    destructor_offset = offset_config['destructor']
    destructor_ptr = read_dword(data, file_offset + destructor_offset)
    if destructor_ptr:
        result['details']['destructor'] = f"0x{destructor_ptr:08X}"
        if is_valid_code_pointer(destructor_ptr):
            result['score'] += 10  # Good sign if it's valid code

    # Read name (try as inline and as pointer)
    name_offset = offset_config['name']

    # Try inline
    name_inline = read_string(data, file_offset + name_offset)
    if name_inline and 'TVN' in name_inline:
        result['details']['name'] = name_inline
        result['score'] += 30  # Big bonus if name contains TVN!

    # Try as pointer
    name_ptr = read_dword(data, file_offset + name_offset)
    if name_ptr and is_valid_data_pointer(name_ptr):
        name_ptr_offset = va_to_file_offset(name_ptr, sections)
        if name_ptr_offset:
            name_pointed = read_string(data, name_ptr_offset)
            if name_pointed and 'TVN' in name_pointed:
                result['details']['name_via_ptr'] = name_pointed
                result['score'] += 30

    return result


def analyze_address(data, sections, va, name):
    """Analyze one address with all possible offset combinations"""

    print(f"\n{'='*80}")
    print(f"Analyzing: {name} @ 0x{va:08X}")
    print(f"{'='*80}")

    # Try different offset configurations
    configs = [
        # Standard layouts
        {'vtable': 0, 'parent': 4, 'destructor': 8, 'name': 12},
        {'vtable': 0, 'parent': 4, 'destructor': 8, 'name': 16},
        {'vtable': 0, 'parent': 4, 'destructor': 8, 'name': 20},

        # Name might come first
        {'vtable': 4, 'parent': 8, 'destructor': 12, 'name': 0},

        # Larger offsets
        {'vtable': 0, 'parent': 8, 'destructor': 12, 'name': 16},
        {'vtable': 0, 'parent': 8, 'destructor': 16, 'name': 20},

        # Name at different positions
        {'vtable': 0, 'parent': 4, 'destructor': 12, 'name': 8},
    ]

    results = []
    for config in configs:
        result = try_parse_rtti(data, sections, va, config)
        if result:
            results.append(result)

    # Sort by score
    results.sort(key=lambda x: x['score'], reverse=True)

    # Show top 3
    print("\nTop 3 configurations:\n")
    for i, result in enumerate(results[:3]):
        print(f"#{i+1} - Score: {result['score']}")
        print(f"     Offsets: vtable={result['config']['vtable']}, "
              f"parent={result['config']['parent']}, "
              f"destructor={result['config']['destructor']}, "
              f"name={result['config']['name']}")
        for key, value in result['details'].items():
            print(f"     {key}: {value}")
        print()

    return results[0] if results else None


def main():
    if len(sys.argv) < 2:
        print("Usage: auto_detect_rtti_structure.py <europeo.exe>")
        sys.exit(1)

    binary_path = sys.argv[1]

    print("="*80)
    print("AUTOMATIC RTTI STRUCTURE DETECTION")
    print("="*80)
    print()
    print("Strategy: Try different offset combinations and score each")
    print("Scoring:")
    print("  +30 pts: Name contains 'TVN'")
    print("  +20 pts: VTable pointer is valid vtable")
    print("  +10 pts: Destructor is valid code pointer")
    print("  +5 pts: Parent is valid data pointer")
    print()

    with open(binary_path, 'rb') as f:
        data = f.read()

    sections = parse_pe_sections(data)

    # Test addresses from CSV
    test_addresses = {
        "TVNSceneParms (shared RTTI?)": 0x0040E1E0,
        "TVNScene (TYPEINFO)": 0x004179AE,
        "TVNImageObject (TYPEINFO)": 0x0042A40B,
        "TVNTextObject (TYPEINFO)": 0x0042A448,
    }

    all_results = {}
    for name, va in test_addresses.items():
        result = analyze_address(data, sections, va, name)
        all_results[name] = result

    # Final recommendation
    print("\n" + "="*80)
    print("FINAL RECOMMENDATION")
    print("="*80)
    print()

    # Find most common high-scoring config
    best_configs = [r for r in all_results.values() if r and r['score'] >= 30]

    if best_configs:
        best = max(best_configs, key=lambda x: x['score'])
        print(f"✓ RECOMMENDED CONFIGURATION (Score: {best['score']}):\n")
        print(f"  RTTI_OFFSET_VTABLE = 0x{best['config']['vtable']:02X}")
        print(f"  RTTI_OFFSET_PARENT = 0x{best['config']['parent']:02X}")
        print(f"  RTTI_OFFSET_DESTRUCTOR = 0x{best['config']['destructor']:02X}")
        print(f"  RTTI_OFFSET_NAME = 0x{best['config']['name']:02X}")
        print()
        print("Use these offsets in extract_tvn_corrected.py")
    else:
        print("⚠️  Could not determine offsets automatically")
        print("Manual IDA verification required")

    print()


if __name__ == "__main__":
    main()
