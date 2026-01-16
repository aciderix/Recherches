# LoadFromINI Function Analysis

**Function Address**: 0x0042634D
**Rank**: #106
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 39

```assembly
0042634D  push     ebp
0042634E  mov      ebp, esp
00426350  push     ebx
00426351  push     esi
00426352  push     edi
00426353  mov      edi, dword ptr [ebp + 0xc]
00426356  mov      esi, dword ptr [ebp + 8]
00426359  push     esi
0042635A  mov      eax, dword ptr [esi + 1]
0042635D  call     dword ptr [eax]
0042635F  pop      ecx
00426360  test     eax, eax
00426362  je       0x426391
00426364  xor      ebx, ebx
00426366  jmp      0x426386
00426368  mov      eax, dword ptr [esi + 5]
0042636B  cmp      dword ptr [eax + ebx*4], 0
0042636F  je       0x426385
00426371  mov      edx, dword ptr [esi + 5]
00426374  cmp      edi, dword ptr [edx + ebx*4]
00426377  sete     cl
0042637A  and      ecx, 1
0042637D  test     cl, cl
0042637F  je       0x426385
00426381  mov      eax, ebx
00426383  jmp      0x426394
00426385  inc      ebx
00426386  push     esi
00426387  mov      edx, dword ptr [esi + 1]
0042638A  call     dword ptr [edx]
0042638C  pop      ecx
0042638D  cmp      ebx, eax
0042638F  jb       0x426368
00426391  or       eax, 0xffffffff
00426394  pop      edi
00426395  pop      esi
00426396  pop      ebx
00426397  pop      ebp
00426398  ret      
```

## Strings Referenced

**Total unique strings**: 0



---

*Extracted with recursive CALL following and DATA context*
