# LoadFromINI Function Analysis

**Function Address**: 0x0041E119
**Rank**: #152
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 74

```assembly
0041E119  push     ebp
0041E11A  mov      ebp, esp
0041E11C  add      esp, -0x24
0041E11F  push     ebx
0041E120  mov      eax, 0x44468c
0041E125  call     0x403618
0041E12A  mov      dword ptr [ebp - 8], 7
0041E131  cmp      dword ptr [ebp + 8], 0
0041E135  je       0x41e1f7
0041E13B  mov      word ptr [ebp - 0x14], 8
0041E141  mov      edx, dword ptr [ebp + 8]
0041E144  mov      dword ptr [edx + 0x1d], 0x4449cc
0041E14B  jmp      0x41e15a
0041E14D  mov      ecx, dword ptr [ebp + 8]
0041E150  cmp      dword ptr [ecx + 0x19], 2
0041E154  je       0x41e15a
0041E156  xor      eax, eax
0041E158  jmp      0x41e15f
0041E15A  mov      eax, 1
0041E15F  mov      ebx, dword ptr [ebp + 8]
0041E162  add      ebx, 4
0041E165  push     0
0041E167  push     -1
0041E169  push     eax
0041E16A  push     ebx
0041E16B  call     0x435bc3
0041E170  add      esp, 0x10
0041E173  xor      eax, eax
0041E175  mov      dword ptr [ebx + 0xd], eax
0041E178  sub      dword ptr [ebp - 8], 7
0041E17C  add      dword ptr [ebp - 8], 7
0041E180  sub      dword ptr [ebp - 8], 6
0041E184  add      dword ptr [ebp - 8], 6
0041E188  sub      dword ptr [ebp - 8], 5
0041E18C  mov      edx, dword ptr [ebp + 8]
0041E18F  cmp      dword ptr [edx + 0x19], 2
0041E193  je       0x41e199
0041E195  xor      eax, eax
0041E197  jmp      0x41e19e
0041E199  mov      eax, 1
0041E19E  mov      ebx, dword ptr [ebp + 8]
0041E1A1  add      ebx, 4
0041E1A4  push     0
0041E1A6  push     -1
0041E1A8  push     eax
0041E1A9  push     ebx
0041E1AA  call     0x435bc3
0041E1AF  add      esp, 0x10
0041E1B2  xor      eax, eax
0041E1B4  mov      dword ptr [ebx + 0xd], eax
0041E1B7  sub      dword ptr [ebp - 8], 4
0041E1BB  add      dword ptr [ebp - 8], 4
0041E1BF  sub      dword ptr [ebp - 8], 3
0041E1C3  mov      eax, dword ptr [ebp + 8]
0041E1C6  add      eax, 4
0041E1C9  add      dword ptr [ebp - 8], 3
0041E1CD  sub      dword ptr [ebp - 8], 2
0041E1D1  add      dword ptr [ebp - 8], 2
0041E1D5  dec      dword ptr [ebp - 8]
0041E1D8  mov      dword ptr [eax + 1], 0x43b500
0041E1DF  push     dword ptr [eax + 5]
0041E1E2  call     0x438f82
0041E1E7  pop      ecx
0041E1E8  test     byte ptr [ebp + 0xc], 1
0041E1EC  je       0x41e1f7
0041E1EE  push     dword ptr [ebp + 8]
0041E1F1  call     0x438f16
0041E1F6  pop      ecx
0041E1F7  mov      edx, dword ptr [ebp - 0x24]
0041E1FA  mov      dword ptr fs:[0], edx
0041E201  pop      ebx
0041E202  mov      esp, ebp
0041E204  pop      ebp
0041E205  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00435BC3
- 0x00435BC3
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
