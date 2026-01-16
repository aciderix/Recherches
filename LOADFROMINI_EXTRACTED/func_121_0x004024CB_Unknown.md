# LoadFromINI Function Analysis

**Function Address**: 0x004024CB
**Rank**: #121
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 50

```assembly
004024CB  push     ebp
004024CC  mov      ebp, esp
004024CE  add      esp, -0xc
004024D1  push     ebx
004024D2  push     esi
004024D3  push     edi
004024D4  mov      esi, dword ptr [ebp + 0x14]
004024D7  mov      ebx, dword ptr [ebp + 8]
004024DA  mov      edi, esi
004024DC  mov      eax, dword ptr [ebp + 0x10]
004024DF  mov      dword ptr [ebp - 4], eax
004024E2  mov      edx, dword ptr [ebp + 0xc]
004024E5  mov      dword ptr [ebp - 8], edx
004024E8  mov      ecx, dword ptr [ebx + 4]
004024EB  mov      dword ptr [ebp - 0xc], ecx
004024EE  push     edi
004024EF  push     dword ptr [ebp - 4]
004024F2  push     dword ptr [ebp - 8]
004024F5  push     0
004024F7  push     dword ptr [ebp - 0xc]
004024FA  mov      eax, dword ptr [ebx]
004024FC  push     dword ptr [eax]
004024FE  call     0x439888
00402503  mov      edi, eax
00402505  test     edi, edi
00402507  jne      0x402538
00402509  mov      edx, dword ptr [ebp + 0xc]
0040250C  mov      dword ptr [ebx + 0xc], edx
0040250F  mov      eax, dword ptr [ebx + 0x14]
00402512  cmp      esi, eax
00402514  jne      0x402527
00402516  push     eax
00402517  push     dword ptr [ebp + 0x10]
0040251A  push     dword ptr [ebx + 0x10]
0040251D  call     0x438db4
00402522  add      esp, 0xc
00402525  jmp      0x402538
00402527  mov      dword ptr [ebx + 0x14], esi
0040252A  push     dword ptr [ebx + 0x10]
0040252D  call     0x438f82
00402532  pop      ecx
00402533  xor      edx, edx
00402535  mov      dword ptr [ebx + 0x10], edx
00402538  mov      eax, edi
0040253A  pop      edi
0040253B  pop      esi
0040253C  pop      ebx
0040253D  mov      esp, ebp
0040253F  pop      ebp
00402540  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00439888
- 0x00438DB4
- 0x00438F82

---

*Extracted with recursive CALL following and DATA context*
