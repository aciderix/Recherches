# LoadFromINI Function Analysis

**Function Address**: 0x00401E68
**Rank**: #93
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 23

```assembly
00401E68  push     ebp
00401E69  mov      ebp, esp
00401E6B  add      esp, -0x24
00401E6E  mov      eax, 0x44e510
00401E73  call     0x403618
00401E78  cmp      byte ptr [0x44e4ff], 0
00401E7F  jne      0x401eac
00401E81  mov      word ptr [ebp - 0x14], 8
00401E87  push     0x44e892
00401E8C  push     1
00401E8E  push     0x80000006
00401E93  push     0x44e4ee
00401E98  call     0x40206c
00401E9D  inc      dword ptr [ebp - 8]
00401EA0  dec      dword ptr [ebp - 8]
00401EA3  add      esp, 0x10
00401EA6  inc      byte ptr [0x44e4ff]
00401EAC  mov      eax, 0x44e4ee
00401EB1  mov      edx, dword ptr [ebp - 0x24]
00401EB4  mov      dword ptr fs:[0], edx
00401EBB  mov      esp, ebp
00401EBD  pop      ebp
00401EBE  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"HKEY_DYN_DATA"` @ 0x0044E892

## DATA Context

**Context around 0x0044E892**:

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
