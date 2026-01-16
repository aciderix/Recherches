# LoadFromINI Function Analysis

**Function Address**: 0x0040206C
**Rank**: #113
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 66

```assembly
0040206C  push     ebp
0040206D  mov      ebp, esp
0040206F  add      esp, -0x24
00402072  mov      eax, 0x44e5b2
00402077  push     ebx
00402078  push     esi
00402079  push     edi
0040207A  call     0x403618
0040207F  mov      word ptr [ebp - 0x14], 8
00402085  mov      edx, dword ptr [ebp + 8]
00402088  mov      ecx, dword ptr [ebp + 0xc]
0040208B  mov      dword ptr [edx], ecx
0040208D  push     0
0040208F  push     dword ptr [ebp + 0x14]
00402092  call     0x439168
00402097  add      esp, 8
0040209A  mov      edx, dword ptr [ebp + 8]
0040209D  mov      dword ptr [edx + 4], eax
004020A0  mov      eax, dword ptr [ebp + 8]
004020A3  mov      cl, byte ptr [ebp + 0x10]
004020A6  mov      byte ptr [eax + 0x10], cl
004020A9  mov      word ptr [ebp - 0x14], 0x14
004020AF  push     0
004020B1  push     0
004020B3  push     0
004020B5  push     0
004020B7  mov      eax, dword ptr [ebp + 8]
004020BA  add      eax, 0xc
004020BD  push     eax
004020BE  push     0
004020C0  push     0
004020C2  mov      edx, dword ptr [ebp + 8]
004020C5  add      edx, 8
004020C8  push     edx
004020C9  push     0
004020CB  push     0
004020CD  push     dword ptr [ebp + 8]
004020D0  call     0x40215c
004020D5  add      esp, 0x2c
004020D8  mov      word ptr [ebp - 0x14], 0x14
004020DE  test     eax, eax
004020E0  je       0x4020ee
004020E2  cmp      eax, 0x7a
004020E5  je       0x4020ee
004020E7  mov      ecx, dword ptr [ebp + 8]
004020EA  xor      eax, eax
004020EC  mov      dword ptr [ecx], eax
004020EE  mov      word ptr [ebp - 0x14], 8
004020F4  jmp      0x40210d
004020F6  cmp      dword ptr [ebp - 0x10], 0xc0000005
004020FD  mov      eax, 1
00402102  je       0x402105
00402104  dec      eax
00402105  ret      
00402106  mov      edx, dword ptr [ebp + 8]
00402109  xor      ecx, ecx
0040210B  mov      dword ptr [edx], ecx
0040210D  mov      eax, dword ptr [ebp - 0x24]
00402110  mov      dword ptr fs:[0], eax
00402116  mov      eax, dword ptr [ebp + 8]
00402119  mov      esp, ebp
0040211B  mov      edi, dword ptr [ebp - 0x30]
0040211E  mov      esi, dword ptr [ebp - 0x2c]
00402121  mov      ebx, dword ptr [ebp - 0x28]
00402124  pop      ebp
00402125  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00439168
- 0x0040215C

---

*Extracted with recursive CALL following and DATA context*
