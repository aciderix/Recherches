# LoadFromINI Function Analysis

**Function Address**: 0x0040215C
**Rank**: #115
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 87

```assembly
0040215C  push     ebp
0040215D  mov      ebp, esp
0040215F  add      esp, 0xfffffed8
00402165  push     ebx
00402166  push     esi
00402167  push     edi
00402168  xor      ebx, ebx
0040216A  mov      edi, dword ptr [ebp + 0x18]
0040216D  mov      esi, dword ptr [ebp + 0x14]
00402170  mov      ecx, dword ptr [ebp + 0x10]
00402173  mov      edx, dword ptr [ebp + 0xc]
00402176  mov      eax, dword ptr [ebp + 8]
00402179  mov      dword ptr [ebp - 4], 0x100
00402180  mov      dword ptr [ebp - 8], ebx
00402183  xor      ebx, ebx
00402185  mov      dword ptr [ebp - 0xc], ebx
00402188  xor      ebx, ebx
0040218A  mov      dword ptr [ebp - 0x10], ebx
0040218D  xor      ebx, ebx
0040218F  mov      dword ptr [ebp - 0x14], ebx
00402192  xor      ebx, ebx
00402194  mov      dword ptr [ebp - 0x18], ebx
00402197  xor      ebx, ebx
00402199  mov      dword ptr [ebp - 0x1c], ebx
0040219C  xor      ebx, ebx
0040219E  mov      dword ptr [ebp - 0x20], ebx
004021A1  cmp      dword ptr [ebp + 0x30], 0
004021A5  je       0x4021ac
004021A7  mov      ebx, dword ptr [ebp + 0x30]
004021AA  jmp      0x4021af
004021AC  lea      ebx, [ebp - 0x28]
004021AF  push     ebx
004021B0  cmp      dword ptr [ebp + 0x2c], 0
004021B4  je       0x4021bb
004021B6  mov      ebx, dword ptr [ebp + 0x2c]
004021B9  jmp      0x4021be
004021BB  lea      ebx, [ebp - 0x20]
004021BE  push     ebx
004021BF  cmp      dword ptr [ebp + 0x28], 0
004021C3  je       0x4021ca
004021C5  mov      ebx, dword ptr [ebp + 0x28]
004021C8  jmp      0x4021cd
004021CA  lea      ebx, [ebp - 0x1c]
004021CD  push     ebx
004021CE  cmp      dword ptr [ebp + 0x24], 0
004021D2  je       0x4021d9
004021D4  mov      ebx, dword ptr [ebp + 0x24]
004021D7  jmp      0x4021dc
004021D9  lea      ebx, [ebp - 0x18]
004021DC  push     ebx
004021DD  cmp      dword ptr [ebp + 0x20], 0
004021E1  je       0x4021e8
004021E3  mov      ebx, dword ptr [ebp + 0x20]
004021E6  jmp      0x4021eb
004021E8  lea      ebx, [ebp - 0x14]
004021EB  push     ebx
004021EC  cmp      dword ptr [ebp + 0x1c], 0
004021F0  je       0x4021f7
004021F2  mov      ebx, dword ptr [ebp + 0x1c]
004021F5  jmp      0x4021fa
004021F7  lea      ebx, [ebp - 0x10]
004021FA  push     ebx
004021FB  test     edi, edi
004021FD  jne      0x402202
004021FF  lea      edi, [ebp - 0xc]
00402202  push     edi
00402203  test     esi, esi
00402205  jne      0x40220a
00402207  lea      esi, [ebp - 8]
0040220A  push     esi
0040220B  push     0
0040220D  test     ecx, ecx
0040220F  jne      0x402214
00402211  lea      ecx, [ebp - 4]
00402214  push     ecx
00402215  test     edx, edx
00402217  jne      0x40221f
00402219  lea      edx, [ebp - 0x128]
0040221F  push     edx
00402220  push     dword ptr [eax]
00402222  call     0x4398a0
00402227  pop      edi
00402228  pop      esi
00402229  pop      ebx
0040222A  mov      esp, ebp
0040222C  pop      ebp
0040222D  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x004398A0

---

*Extracted with recursive CALL following and DATA context*
