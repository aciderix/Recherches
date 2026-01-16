# LoadFromINI Function Analysis

**Function Address**: 0x004058E5
**Rank**: #56
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 29

```assembly
004058E5  push     ebp
004058E6  mov      ebp, esp
004058E8  push     ebx
004058E9  push     esi
004058EA  push     edi
004058EB  mov      eax, dword ptr [ebp + 8]
004058EE  lea      esi, [eax + 0xc]
004058F1  lea      edi, [eax + 8]
004058F4  add      eax, 4
004058F7  push     eax
004058F8  push     dword ptr [ebp + 0xc]
004058FB  call     0x439138
00405900  add      esp, 8
00405903  mov      ebx, eax
00405905  push     4
00405907  push     edi
00405908  push     ebx
00405909  call     0x439192
0040590E  add      esp, 0xc
00405911  push     4
00405913  push     esi
00405914  push     ebx
00405915  call     0x439192
0040591A  add      esp, 0xc
0040591D  pop      edi
0040591E  pop      esi
0040591F  pop      ebx
00405920  pop      ebp
00405921  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00439138
- 0x00439192
- 0x00439192

---

*Extracted with recursive CALL following and DATA context*
