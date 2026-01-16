# LoadFromINI Function Analysis

**Function Address**: 0x0040248E
**Rank**: #120
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 28

```assembly
0040248E  push     ebp
0040248F  mov      ebp, esp
00402491  push     ecx
00402492  push     ebx
00402493  mov      ebx, dword ptr [ebp + 8]
00402496  cmp      dword ptr [ebx + 0x10], 0
0040249A  jne      0x4024c7
0040249C  push     dword ptr [ebx + 0x14]
0040249F  call     0x438e50
004024A4  pop      ecx
004024A5  mov      dword ptr [ebx + 0x10], eax
004024A8  mov      eax, dword ptr [ebx + 0x14]
004024AB  lea      ecx, [ebp - 4]
004024AE  mov      dword ptr [ebp - 4], eax
004024B1  mov      eax, dword ptr [ebx + 0x10]
004024B4  mov      edx, dword ptr [ebx + 4]
004024B7  push     ecx
004024B8  push     eax
004024B9  push     0
004024BB  push     0
004024BD  push     edx
004024BE  mov      eax, dword ptr [ebx]
004024C0  push     dword ptr [eax]
004024C2  call     0x439894
004024C7  pop      ebx
004024C8  pop      ecx
004024C9  pop      ebp
004024CA  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00438E50
- 0x00439894

---

*Extracted with recursive CALL following and DATA context*
