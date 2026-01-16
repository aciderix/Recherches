# LoadFromINI Function Analysis

**Function Address**: 0x0040222E
**Rank**: #116
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 107

```assembly
0040222E  push     ebp
0040222F  mov      ebp, esp
00402231  add      esp, -0x54
00402234  mov      eax, 0x44e612
00402239  push     ebx
0040223A  push     esi
0040223B  push     edi
0040223C  lea      edi, [ebp - 0x54]
0040223F  lea      esi, [ebp - 0x4c]
00402242  call     0x403618
00402247  mov      word ptr [esi + 0x10], 8
0040224D  push     1
0040224F  push     0xf003f
00402254  push     dword ptr [ebp + 0xc]
00402257  mov      edx, dword ptr [ebp + 8]
0040225A  lea      ecx, [ebp - 0x14]
0040225D  push     dword ptr [edx]
0040225F  push     ecx
00402260  call     0x401f16
00402265  add      esp, 0x14
00402268  inc      dword ptr [esi + 0x1c]
0040226B  mov      word ptr [esi + 0x10], 0x14
00402271  lea      eax, [ebp - 0x14]
00402274  mov      dword ptr [edi], eax
00402276  xor      edx, edx
00402278  mov      dword ptr [edi + 4], edx
0040227B  jmp      0x402311
00402280  mov      word ptr [esi + 0x10], 0x20
00402286  push     0xf003f
0040228B  push     edi
0040228C  lea      ecx, [ebp - 0x28]
0040228F  push     ecx
00402290  call     0x401fc8
00402295  add      esp, 0xc
00402298  inc      dword ptr [esi + 0x1c]
0040229B  mov      word ptr [esi + 0x10], 0x2c
004022A1  cmp      dword ptr [ebp - 0x28], 0
004022A5  jne      0x4022ba
004022A7  dec      dword ptr [esi + 0x1c]
004022AA  push     2
004022AC  lea      eax, [ebp - 0x28]
004022AF  push     eax
004022B0  call     0x402126
004022B5  add      esp, 8
004022B8  jmp      0x402330
004022BA  push     dword ptr [ebp - 0x24]
004022BD  lea      edx, [ebp - 0x14]
004022C0  push     edx
004022C1  call     0x40222e
004022C6  add      esp, 8
004022C9  mov      ebx, eax
004022CB  test     ebx, ebx
004022CD  je       0x402300
004022CF  mov      eax, ebx
004022D1  lea      edx, [ebp - 0x28]
004022D4  push     eax
004022D5  dec      dword ptr [esi + 0x1c]
004022D8  push     2
004022DA  push     edx
004022DB  call     0x402126
004022E0  add      esp, 8
004022E3  dec      dword ptr [esi + 0x1c]
004022E6  push     2
004022E8  lea      ecx, [ebp - 0x14]
004022EB  push     ecx
004022EC  call     0x402126
004022F1  add      esp, 8
004022F4  pop      eax
004022F5  mov      edx, dword ptr [esi]
004022F7  mov      dword ptr fs:[0], edx
004022FE  jmp      0x402358
00402300  dec      dword ptr [esi + 0x1c]
00402303  push     2
00402305  lea      ecx, [ebp - 0x28]
00402308  push     ecx
00402309  call     0x402126
0040230E  add      esp, 8
00402311  mov      eax, dword ptr [edi + 4]
00402314  test     eax, eax
00402316  jl       0x40231f
00402318  mov      edx, dword ptr [edi]
0040231A  cmp      eax, dword ptr [edx + 8]
0040231D  jl       0x402323
0040231F  xor      ecx, ecx
00402321  jmp      0x402328
00402323  mov      ecx, 1
00402328  test     cl, cl
0040232A  jne      0x402280
00402330  dec      dword ptr [esi + 0x1c]
00402333  push     2
00402335  lea      eax, [ebp - 0x14]
00402338  push     eax
00402339  call     0x402126
0040233E  add      esp, 8
00402341  mov      ebx, dword ptr [ebp + 0xc]
00402344  push     ebx
00402345  mov      edx, dword ptr [ebp + 8]
00402348  push     dword ptr [edx]
0040234A  call     0x4398b8
0040234F  mov      ecx, dword ptr [esi]
00402351  mov      dword ptr fs:[0], ecx
00402358  pop      edi
00402359  pop      esi
0040235A  pop      ebx
0040235B  mov      esp, ebp
0040235D  pop      ebp
0040235E  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00401F16
- 0x00401FC8
- 0x00402126
- 0x0040222E
- 0x00402126
- 0x00402126
- 0x00402126
- 0x00402126
- 0x004398B8

---

*Extracted with recursive CALL following and DATA context*
