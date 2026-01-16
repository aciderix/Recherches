# LoadFromINI Function Analysis

**Function Address**: 0x0041F302
**Rank**: #18
**INI String Count**: 8
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 100

```assembly
0041F302  push     ebp
0041F303  mov      ebp, esp
0041F305  add      esp, -0x24
0041F308  push     ebx
0041F309  push     esi
0041F30A  push     edi
0041F30B  lea      edi, [ebp - 0x24]
0041F30E  mov      eax, 0x444d1c
0041F313  call     0x403618
0041F318  mov      word ptr [edi + 0x10], 8
0041F31E  mov      edx, dword ptr [ebp + 8]
0041F321  mov      dword ptr [edx], 0x446a88
0041F327  mov      esi, dword ptr [ebp + 8]
0041F32A  add      esi, 4
0041F32D  xor      eax, eax
0041F32F  mov      dword ptr [esi], eax
0041F331  lea      ebx, [esi + 4]
0041F334  mov      dword ptr [ebx + 1], 0x446a30
0041F33B  push     0
0041F33D  push     0
0041F33F  push     0x41f121
0041F344  push     1
0041F346  push     1
0041F348  push     0x52
0041F34A  push     0x52
0041F34C  call     0x438e50
0041F351  pop      ecx
0041F352  push     eax
0041F353  call     0x4037e0
0041F358  add      esp, 0x1c
0041F35B  mov      dword ptr [ebx + 5], eax
0041F35E  mov      dword ptr [ebx + 9], 1
0041F365  inc      dword ptr [edi + 0x1c]
0041F368  mov      dword ptr [ebx + 1], 0x446a4c
0041F36F  add      dword ptr [edi + 0x1c], 2
0041F373  mov      dword ptr [ebx + 1], 0x446a68
0041F37A  xor      eax, eax
0041F37C  mov      dword ptr [ebx + 0xd], eax
0041F37F  mov      dword ptr [ebx + 0x11], 5
0041F386  add      dword ptr [edi + 0x1c], 3
0041F38A  add      dword ptr [edi + 0x1c], 4
0041F38E  add      dword ptr [edi + 0x1c], 5
0041F392  add      dword ptr [edi + 0x1c], 6
0041F396  add      dword ptr [edi + 0x1c], 7
0041F39A  add      dword ptr [edi + 0x1c], 8
0041F39E  mov      esi, dword ptr [ebp + 8]
0041F3A1  add      esi, 0x1d
0041F3A4  xor      eax, eax
0041F3A6  mov      dword ptr [esi], eax
0041F3A8  lea      ebx, [esi + 4]
0041F3AB  mov      dword ptr [ebx + 1], 0x4469d8
0041F3B2  push     0
0041F3B4  push     0
0041F3B6  push     0x4231b0
0041F3BB  push     1
0041F3BD  push     1
0041F3BF  push     0x14
0041F3C1  push     0x14
0041F3C3  call     0x438e50
0041F3C8  pop      ecx
0041F3C9  push     eax
0041F3CA  call     0x4037e0
0041F3CF  add      esp, 0x1c
0041F3D2  mov      dword ptr [ebx + 5], eax
0041F3D5  mov      dword ptr [ebx + 9], 1
0041F3DC  inc      dword ptr [edi + 0x1c]
0041F3DF  mov      dword ptr [ebx + 1], 0x4469f4
0041F3E6  add      dword ptr [edi + 0x1c], 2
0041F3EA  mov      dword ptr [ebx + 1], 0x446a10
0041F3F1  xor      eax, eax
0041F3F3  mov      dword ptr [ebx + 0xd], eax
0041F3F6  mov      dword ptr [ebx + 0x11], 5
0041F3FD  add      dword ptr [edi + 0x1c], 3
0041F401  add      dword ptr [edi + 0x1c], 4
0041F405  add      dword ptr [edi + 0x1c], 5
0041F409  add      dword ptr [edi + 0x1c], 6
0041F40D  add      dword ptr [edi + 0x1c], 7
0041F411  add      dword ptr [edi + 0x1c], 8
0041F415  push     0x44642c
0041F41A  mov      edx, dword ptr [ebp + 8]
0041F41D  add      edx, 0x36
0041F420  push     edx
0041F421  call     0x438e6e
0041F426  add      esp, 8
0041F429  inc      dword ptr [edi + 0x1c]
0041F42C  mov      ecx, dword ptr [ebp + 8]
0041F42F  mov      eax, dword ptr [ebp + 0xc]
0041F432  mov      dword ptr [ecx + 0x3a], eax
0041F435  mov      edx, dword ptr [ebp + 8]
0041F438  xor      ecx, ecx
0041F43A  mov      dword ptr [edx + 0x3e], ecx
0041F43D  mov      eax, dword ptr [edi]
0041F43F  mov      dword ptr fs:[0], eax
0041F445  mov      eax, dword ptr [ebp + 8]
0041F448  pop      edi
0041F449  pop      esi
0041F44A  pop      ebx
0041F44B  mov      esp, ebp
0041F44D  pop      ebp
0041F44E  ret      
```

## Strings Referenced

**Total unique strings**: 7

- `"!8B"` @ 0x00446A30
- `"!8B"` @ 0x00446A4C
- `"39B"` @ 0x00446A68
- `"T9B"` @ 0x00446A88
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## DATA Context

**Context around 0x0044EB41**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD

**Context around 0x0044EB24**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

**Context around 0x0044EB64**:

- `"tor_delete_"` @ 0x0044EAE4
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD
- `" N?A"` @ 0x0044EBCF
- `" w1B"` @ 0x0044EBDB

**Context around 0x00446A88**:

- `"!8B"` @ 0x00446A30
- `",8B"` @ 0x00446A34
- `"78B"` @ 0x00446A38
- `">8B"` @ 0x00446A3C
- `"C8B"` @ 0x00446A40
- `"!8B"` @ 0x00446A4C
- `",8B"` @ 0x00446A50
- `"78B"` @ 0x00446A54
- `">8B"` @ 0x00446A58
- `"39B"` @ 0x00446A68
- `">9B"` @ 0x00446A6C
- `"I9B"` @ 0x00446A70
- `">8B"` @ 0x00446A74
- `"R2B"` @ 0x00446A78
- `"T9B"` @ 0x00446A88
- `"%<@"` @ 0x00446AC8
- `"%<@"` @ 0x00446AD4

**Context around 0x00446A68**:

- `"!8B"` @ 0x00446A30
- `",8B"` @ 0x00446A34
- `"78B"` @ 0x00446A38
- `">8B"` @ 0x00446A3C
- `"C8B"` @ 0x00446A40
- `"!8B"` @ 0x00446A4C
- `",8B"` @ 0x00446A50
- `"78B"` @ 0x00446A54
- `">8B"` @ 0x00446A58
- `"39B"` @ 0x00446A68
- `">9B"` @ 0x00446A6C
- `"I9B"` @ 0x00446A70
- `">8B"` @ 0x00446A74
- `"R2B"` @ 0x00446A78
- `"T9B"` @ 0x00446A88
- `"%<@"` @ 0x00446AC8
- `"%<@"` @ 0x00446AD4

**Context around 0x00446A4C**:

- `"!8B"` @ 0x00446A30
- `",8B"` @ 0x00446A34
- `"78B"` @ 0x00446A38
- `">8B"` @ 0x00446A3C
- `"C8B"` @ 0x00446A40
- `"!8B"` @ 0x00446A4C
- `",8B"` @ 0x00446A50
- `"78B"` @ 0x00446A54
- `">8B"` @ 0x00446A58
- `"39B"` @ 0x00446A68
- `">9B"` @ 0x00446A6C
- `"I9B"` @ 0x00446A70
- `">8B"` @ 0x00446A74
- `"R2B"` @ 0x00446A78
- `"T9B"` @ 0x00446A88
- `"%<@"` @ 0x00446AC8

**Context around 0x00446A30**:

- `"classlib/vectimp.h"` @ 0x004469B0
- `"Check"` @ 0x004469C3
- `"!8B"` @ 0x00446A30
- `",8B"` @ 0x00446A34
- `"78B"` @ 0x00446A38
- `">8B"` @ 0x00446A3C
- `"C8B"` @ 0x00446A40
- `"!8B"` @ 0x00446A4C
- `",8B"` @ 0x00446A50
- `"78B"` @ 0x00446A54
- `">8B"` @ 0x00446A58
- `"39B"` @ 0x00446A68
- `">9B"` @ 0x00446A6C
- `"I9B"` @ 0x00446A70
- `">8B"` @ 0x00446A74
- `"R2B"` @ 0x00446A78
- `"T9B"` @ 0x00446A88

## Functions Called

- 0x00403618
- 0x00438E50
- 0x004037E0
- 0x00438E50
- 0x004037E0
- 0x00438E6E

---

*Extracted with recursive CALL following and DATA context*
