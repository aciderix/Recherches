# LoadFromINI Function Analysis

**Function Address**: 0x00401D0C
**Rank**: #14
**INI String Count**: 8
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 23

```assembly
00401D0C  push     ebp
00401D0D  mov      ebp, esp
00401D0F  add      esp, -0x24
00401D12  mov      eax, 0x44e438
00401D17  call     0x403618
00401D1C  cmp      byte ptr [0x44e427], 0
00401D23  jne      0x401d50
00401D25  mov      word ptr [ebp - 0x14], 8
00401D2B  push     0x44e84e
00401D30  push     1
00401D32  push     0x80000001
00401D37  push     0x44e416
00401D3C  call     0x40206c
00401D41  inc      dword ptr [ebp - 8]
00401D44  dec      dword ptr [ebp - 8]
00401D47  add      esp, 0x10
00401D4A  inc      byte ptr [0x44e427]
00401D50  mov      eax, 0x44e416
00401D55  mov      edx, dword ptr [ebp - 0x24]
00401D58  mov      dword ptr fs:[0], edx
00401D5F  mov      esp, ebp
00401D61  pop      ebp
00401D62  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"HKEY_CURRENT_USER"` @ 0x0044E84E

## DATA Context

**Context around 0x0044E84E**:

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
