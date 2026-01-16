# LoadFromINI Function Analysis

**Function Address**: 0x004134C7
**Rank**: #68
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 69

```assembly
004134C7  push     ebp
004134C8  mov      ebp, esp
004134CA  add      esp, -0x24
004134CD  push     ebx
004134CE  mov      eax, 0x4409c0
004134D3  call     0x403618
004134D8  mov      dword ptr [ebp - 8], 0xa
004134DF  cmp      dword ptr [ebp + 8], 0
004134E3  je       0x4135a1
004134E9  mov      word ptr [ebp - 0x14], 8
004134EF  mov      edx, dword ptr [ebp + 8]
004134F2  mov      dword ptr [edx + 0x25], 0x4417a0
004134F9  mov      ecx, dword ptr [ebp + 8]
004134FC  mov      dword ptr [ecx + 0x1d], 0x4417c0
00413503  mov      eax, dword ptr [ebp + 8]
00413506  mov      dword ptr [eax + 0x21], 0x4417d0
0041350D  mov      edx, dword ptr [ebp + 8]
00413510  push     edx
00413511  mov      ecx, dword ptr [edx + 0x25]
00413514  call     dword ptr [ecx + 0x10]
00413517  pop      ecx
00413518  sub      dword ptr [ebp - 8], 3
0041351C  dec      dword ptr [ebp - 8]
0041351F  dec      dword ptr [ebp - 8]
00413522  sub      dword ptr [ebp - 8], 7
00413526  add      dword ptr [ebp - 8], 7
0041352A  sub      dword ptr [ebp - 8], 6
0041352E  add      dword ptr [ebp - 8], 6
00413532  sub      dword ptr [ebp - 8], 5
00413536  mov      eax, dword ptr [ebp + 8]
00413539  cmp      dword ptr [eax + 0x19], 2
0041353D  je       0x413543
0041353F  xor      eax, eax
00413541  jmp      0x413548
00413543  mov      eax, 1
00413548  mov      ebx, dword ptr [ebp + 8]
0041354B  add      ebx, 4
0041354E  push     0
00413550  push     -1
00413552  push     eax
00413553  push     ebx
00413554  call     0x4141b5
00413559  add      esp, 0x10
0041355C  xor      eax, eax
0041355E  mov      dword ptr [ebx + 0xd], eax
00413561  sub      dword ptr [ebp - 8], 4
00413565  add      dword ptr [ebp - 8], 4
00413569  sub      dword ptr [ebp - 8], 3
0041356D  mov      eax, dword ptr [ebp + 8]
00413570  add      eax, 4
00413573  add      dword ptr [ebp - 8], 3
00413577  sub      dword ptr [ebp - 8], 2
0041357B  add      dword ptr [ebp - 8], 2
0041357F  dec      dword ptr [ebp - 8]
00413582  mov      dword ptr [eax + 1], 0x43b500
00413589  push     dword ptr [eax + 5]
0041358C  call     0x438f82
00413591  pop      ecx
00413592  test     byte ptr [ebp + 0xc], 1
00413596  je       0x4135a1
00413598  push     dword ptr [ebp + 8]
0041359B  call     0x438f16
004135A0  pop      ecx
004135A1  mov      edx, dword ptr [ebp - 0x24]
004135A4  mov      dword ptr fs:[0], edx
004135AB  pop      ebx
004135AC  mov      esp, ebp
004135AE  pop      ebp
004135AF  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x004141B5
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
