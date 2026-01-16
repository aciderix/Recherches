# LoadFromINI Function Analysis

**Function Address**: 0x00433F55
**Rank**: #175
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 104

```assembly
00433F55  push     ebp
00433F56  mov      ebp, esp
00433F58  add      esp, -0x10
00433F5B  push     ebx
00433F5C  push     esi
00433F5D  mov      ebx, dword ptr [ebp + 8]
00433F60  push     ebx
00433F61  mov      eax, dword ptr [ebx + 8]
00433F64  call     dword ptr [eax + 0x7c]
00433F67  pop      ecx
00433F68  test     eax, eax
00433F6A  je       0x43406a
00433F70  cmp      dword ptr [ebx + 0x100], 0
00433F77  je       0x433f86
00433F79  mov      edx, dword ptr [ebx + 0x100]
00433F7F  push     edx
00433F80  mov      ecx, dword ptr [edx]
00433F82  call     dword ptr [ecx + 0x14]
00433F85  pop      ecx
00433F86  cmp      dword ptr [ebx + 0x104], 0
00433F8D  je       0x433f9c
00433F8F  mov      eax, dword ptr [ebx + 0x104]
00433F95  push     eax
00433F96  mov      edx, dword ptr [eax]
00433F98  call     dword ptr [edx + 0x14]
00433F9B  pop      ecx
00433F9C  cmp      dword ptr [ebx + 0xb2], 0
00433FA3  je       0x434018
00433FA5  push     ebx
00433FA6  mov      ecx, dword ptr [ebx + 8]
00433FA9  call     dword ptr [ecx + 0x7c]
00433FAC  pop      ecx
00433FAD  mov      esi, eax
00433FAF  test     byte ptr [esi + 4], 0x80
00433FB3  setne    al
00433FB6  and      eax, 1
00433FB9  test     al, al
00433FBB  je       0x434018
00433FBD  mov      eax, dword ptr [ebx + 0xb2]
00433FC3  add      eax, 0xd
00433FC6  mov      edx, dword ptr [eax]
00433FC8  mov      dword ptr [ebp - 8], edx
00433FCB  mov      ecx, dword ptr [eax + 4]
00433FCE  mov      dword ptr [ebp - 4], ecx
00433FD1  cmp      dword ptr [ebp - 8], 0
00433FD5  je       0x434004
00433FD7  cmp      dword ptr [ebp - 4], 0
00433FDB  je       0x434004
00433FDD  xor      eax, eax
00433FDF  mov      dword ptr [ebp - 0x10], eax
00433FE2  xor      edx, edx
00433FE4  mov      dword ptr [ebp - 0xc], edx
00433FE7  lea      ecx, [ebp - 0x10]
00433FEA  push     ecx
00433FEB  push     ebx
00433FEC  call     0x43353d
00433FF1  pop      ecx
00433FF2  add      esp, -8
00433FF5  fstp     qword ptr [esp]
00433FF8  lea      eax, [ebp - 8]
00433FFB  push     eax
00433FFC  call     0x40501d
00434001  add      esp, 0x10
00434004  push     ebx
00434005  mov      edx, dword ptr [ebx + 8]
00434008  call     dword ptr [edx + 0x7c]
0043400B  pop      ecx
0043400C  mov      ecx, dword ptr [ebp - 8]
0043400F  mov      dword ptr [eax + 0x38], ecx
00434012  mov      ecx, dword ptr [ebp - 4]
00434015  mov      dword ptr [eax + 0x3c], ecx
00434018  push     ebx
00434019  call     0x42e2e6
0043401E  pop      ecx
0043401F  cmp      dword ptr [ebx + 0xaa], 0
00434026  je       0x434035
00434028  mov      eax, dword ptr [ebx + 0xaa]
0043402E  push     eax
0043402F  mov      edx, dword ptr [eax]
00434031  call     dword ptr [edx + 0x30]
00434034  pop      ecx
00434035  xor      ecx, ecx
00434037  mov      dword ptr [ebx + 0x8a], ecx
0043403D  lea      eax, [ebx + 0x17c]
00434043  jmp      0x43404f
00434045  cmp      dword ptr [eax + 0x19], 2
00434049  je       0x43404f
0043404B  xor      edx, edx
0043404D  jmp      0x434054
0043404F  mov      edx, 1
00434054  lea      ebx, [eax + 4]
00434057  push     0
00434059  push     -1
0043405B  push     edx
0043405C  push     ebx
0043405D  call     0x435bc3
00434062  add      esp, 0x10
00434065  xor      eax, eax
00434067  mov      dword ptr [ebx + 0xd], eax
0043406A  pop      esi
0043406B  pop      ebx
0043406C  mov      esp, ebp
0043406E  pop      ebp
0043406F  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x0043353D
- 0x0040501D
- 0x0042E2E6
- 0x00435BC3

---

*Extracted with recursive CALL following and DATA context*
