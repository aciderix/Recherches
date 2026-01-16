# LoadFromINI Function Analysis

**Function Address**: 0x00401D63
**Rank**: #23
**INI String Count**: 7
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 23

```assembly
00401D63  push     ebp
00401D64  mov      ebp, esp
00401D66  add      esp, -0x24
00401D69  mov      eax, 0x44e46e
00401D6E  call     0x403618
00401D73  cmp      byte ptr [0x44e45d], 0
00401D7A  jne      0x401da7
00401D7C  mov      word ptr [ebp - 0x14], 8
00401D82  push     0x44e860
00401D87  push     1
00401D89  push     0x80000002
00401D8E  push     0x44e44c
00401D93  call     0x40206c
00401D98  inc      dword ptr [ebp - 8]
00401D9B  dec      dword ptr [ebp - 8]
00401D9E  add      esp, 0x10
00401DA1  inc      byte ptr [0x44e45d]
00401DA7  mov      eax, 0x44e44c
00401DAC  mov      edx, dword ptr [ebp - 0x24]
00401DAF  mov      dword ptr fs:[0], edx
00401DB6  mov      esp, ebp
00401DB8  pop      ebp
00401DB9  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"HKEY_LOCAL_MACHINE"` @ 0x0044E860

## DATA Context

**Context around 0x0044E860**:

- `"HKEY_CLASSES_ROOT"` @ 0x0044E836
- `"CLSID"` @ 0x0044E848
- `"HKEY_CURRENT_USER"` @ 0x0044E84E
- `"HKEY_LOCAL_MACHINE"` @ 0x0044E860
- `"HKEY_USERS"` @ 0x0044E873
- `"HKEY_CURRENT_CONFIG"` @ 0x0044E87E
- `"HKEY_DYN_DATA"` @ 0x0044E892
- `"HKEY_PERFORMANCE_DATA"` @ 0x0044E8A0
- `"Registry failure on key: %s, ErrorCode = %lX"` @ 0x0044E8B6

## Functions Called

- 0x00403618
- 0x0040206C

---

*Extracted with recursive CALL following and DATA context*
