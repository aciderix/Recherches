# LoadFromINI Function Analysis

**Function Address**: 0x00411EFA
**Rank**: #5
**INI String Count**: 14
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 13

```assembly
00411EFA  push     ebp
00411EFB  mov      ebp, esp
00411EFD  mov      edx, dword ptr [ebp + 0xc]
00411F00  mov      eax, dword ptr [ebp + 8]
00411F03  cmp      byte ptr [ebp + 0x10], 0
00411F07  je       0x411f0e
00411F09  or       dword ptr [eax + 0x31], edx
00411F0C  pop      ebp
00411F0D  ret      
00411F0E  not      edx
00411F10  and      dword ptr [eax + 0x31], edx
00411F13  pop      ebp
00411F14  ret      
```

## Strings Referenced

**Total unique strings**: 0



---

*Extracted with recursive CALL following and DATA context*
