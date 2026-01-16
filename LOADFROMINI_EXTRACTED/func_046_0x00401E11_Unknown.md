# LoadFromINI Function Analysis

**Function Address**: 0x00401E11
**Rank**: #46
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 23

```assembly
00401E11  push     ebp
00401E12  mov      ebp, esp
00401E14  add      esp, -0x24
00401E17  mov      eax, 0x44e4da
00401E1C  call     0x403618
00401E21  cmp      byte ptr [0x44e4c9], 0
00401E28  jne      0x401e55
00401E2A  mov      word ptr [ebp - 0x14], 8
00401E30  push     0x44e87e
00401E35  push     1
00401E37  push     0x80000005
00401E3C  push     0x44e4b8
00401E41  call     0x40206c
00401E46  inc      dword ptr [ebp - 8]
00401E49  dec      dword ptr [ebp - 8]
00401E4C  add      esp, 0x10
00401E4F  inc      byte ptr [0x44e4c9]
00401E55  mov      eax, 0x44e4b8
00401E5A  mov      edx, dword ptr [ebp - 0x24]
00401E5D  mov      dword ptr fs:[0], edx
00401E64  mov      esp, ebp
00401E66  pop      ebp
00401E67  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"HKEY_CURRENT_CONFIG"` @ 0x0044E87E

## DATA Context

**Context around 0x0044E87E**:

- `"HKEY_CLASSES_ROOT"` @ 0x0044E836
- `"CLSID"` @ 0x0044E848
- `"HKEY_CURRENT_USER"` @ 0x0044E84E
- `"HKEY_LOCAL_MACHINE"` @ 0x0044E860
- `"HKEY_USERS"` @ 0x0044E873
- `"HKEY_CURRENT_CONFIG"` @ 0x0044E87E
- `"HKEY_DYN_DATA"` @ 0x0044E892
- `"HKEY_PERFORMANCE_DATA"` @ 0x0044E8A0
- `"Registry failure on key: %s, ErrorCode = %lX"` @ 0x0044E8B6
- `"Registry failure on unknown key: ErrorCode = %lX"` @ 0x0044E8E4

## Functions Called

- 0x00403618
- 0x0040206C

---

*Extracted with recursive CALL following and DATA context*
