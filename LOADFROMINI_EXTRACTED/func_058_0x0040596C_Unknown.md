# LoadFromINI Function Analysis

**Function Address**: 0x0040596C
**Rank**: #58
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 25

```assembly
0040596C  push     ebp
0040596D  mov      ebp, esp
0040596F  push     ebx
00405970  push     esi
00405971  push     edi
00405972  mov      ebx, dword ptr [ebp + 8]
00405975  lea      edi, [ebx + 8]
00405978  lea      eax, [ebx + 4]
0040597B  push     eax
0040597C  push     dword ptr [ebp + 0xc]
0040597F  call     0x439138
00405984  add      esp, 8
00405987  mov      esi, eax
00405989  push     4
0040598B  push     edi
0040598C  push     esi
0040598D  call     0x439192
00405992  add      esp, 0xc
00405995  mov      eax, dword ptr [ebx + 8]
00405998  mov      dword ptr [ebx + 0xc], eax
0040599B  pop      edi
0040599C  pop      esi
0040599D  pop      ebx
0040599E  pop      ebp
0040599F  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00439138
- 0x00439192

---

*Extracted with recursive CALL following and DATA context*
