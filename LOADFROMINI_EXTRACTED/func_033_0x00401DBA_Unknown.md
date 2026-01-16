# LoadFromINI Function Analysis

**Function Address**: 0x00401DBA
**Rank**: #33
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 23

```assembly
00401DBA  push     ebp
00401DBB  mov      ebp, esp
00401DBD  add      esp, -0x24
00401DC0  mov      eax, 0x44e4a4
00401DC5  call     0x403618
00401DCA  cmp      byte ptr [0x44e493], 0
00401DD1  jne      0x401dfe
00401DD3  mov      word ptr [ebp - 0x14], 8
00401DD9  push     0x44e873
00401DDE  push     1
00401DE0  push     0x80000003
00401DE5  push     0x44e482
00401DEA  call     0x40206c
00401DEF  inc      dword ptr [ebp - 8]
00401DF2  dec      dword ptr [ebp - 8]
00401DF5  add      esp, 0x10
00401DF8  inc      byte ptr [0x44e493]
00401DFE  mov      eax, 0x44e482
00401E03  mov      edx, dword ptr [ebp - 0x24]
00401E06  mov      dword ptr fs:[0], edx
00401E0D  mov      esp, ebp
00401E0F  pop      ebp
00401E10  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"HKEY_USERS"` @ 0x0044E873

## DATA Context

**Context around 0x0044E873**:

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
