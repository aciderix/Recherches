# LoadFromINI Function Analysis

**Function Address**: 0x004262D4
**Rank**: #105
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 91

```assembly
004262D4  push     ebp
004262D5  mov      ebp, esp
004262D7  add      esp, -0x24
004262DA  push     ebx
004262DB  mov      ebx, dword ptr [ebp + 8]
004262DE  mov      eax, 0x4475c8
004262E3  call     0x403618
004262E8  xor      edx, edx
004262EA  mov      dword ptr [ebx], edx
004262EC  mov      eax, ebx
004262EE  jmp      0x4262fa
004262F0  mov      edx, dword ptr [ebp - 0x24]
004262F3  mov      dword ptr fs:[0], edx
004262FA  pop      ebx
004262FB  mov      esp, ebp
004262FD  pop      ebp
004262FE  ret      
004262FF  add      al, 0
00426301  add      byte ptr [eax], al
00426303  nop      
00426304  add      byte ptr [eax + eax], cl
00426307  cli      
00426308  inc      esp
00426309  inc      edx
0042630A  add      byte ptr [esi + edx*2 + 0x4e], dl
0042630E  inc      ecx
0042630F  jo       0x426381
00426311  insb     byte ptr es:[edi], dx
00426312  imul     esp, dword ptr [ebx + 0x61], 0x6e6f6974
00426319  dec      ecx
0042631A  outsb    dx, byte ptr [esi]
0042631B  outsw    dx, word ptr [esi]
0042631D  and      byte ptr [edx], ch
0042631F  add      byte ptr [eax + eax], al
00426322  add      byte ptr [eax], al
00426324  nop      
00426325  add      byte ptr [eax + eax], cl
00426328  add      edx, esp
0042632A  inc      ecx
0042632B  add      byte ptr [eax + edx*2 + 0x61], dl
0042632F  insb     byte ptr es:[edi], dx
00426330  je       0x4263a7
00426333  and      byte ptr gs:[edx], ch
00426336  add      byte ptr [eax + eax], al
00426339  add      byte ptr [eax], al
0042633B  nop      
0042633C  add      byte ptr [eax + eax], cl
0042633F  mov      eax, 0x54004265
00426344  dec      ebp
00426345  outsd    dx, dword ptr [esi]
00426346  jne      0x4263b5
00426349  and      byte ptr gs:[edx], ch
0042634C  add      byte ptr [ebp - 0x75], dl
0042634F  in       al, dx
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


## Functions Called

- 0x00403618

---

*Extracted with recursive CALL following and DATA context*
