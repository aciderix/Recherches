# LoadFromINI Function Analysis

**Function Address**: 0x00401EBF
**Rank**: #111
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 23

```assembly
00401EBF  push     ebp
00401EC0  mov      ebp, esp
00401EC2  add      esp, -0x24
00401EC5  mov      eax, 0x44e546
00401ECA  call     0x403618
00401ECF  cmp      byte ptr [0x44e535], 0
00401ED6  jne      0x401f03
00401ED8  mov      word ptr [ebp - 0x14], 8
00401EDE  push     0x44e8a0
00401EE3  push     1
00401EE5  push     0x80000004
00401EEA  push     0x44e524
00401EEF  call     0x40206c
00401EF4  inc      dword ptr [ebp - 8]
00401EF7  dec      dword ptr [ebp - 8]
00401EFA  add      esp, 0x10
00401EFD  inc      byte ptr [0x44e535]
00401F03  mov      eax, 0x44e524
00401F08  mov      edx, dword ptr [ebp - 0x24]
00401F0B  mov      dword ptr fs:[0], edx
00401F12  mov      esp, ebp
00401F14  pop      ebp
00401F15  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"HKEY_PERFORMANCE_DATA"` @ 0x0044E8A0

## DATA Context

**Context around 0x0044E8A0**:

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
- `" = "` @ 0x0044E916

## Functions Called

- 0x00403618
- 0x0040206C

---

*Extracted with recursive CALL following and DATA context*
