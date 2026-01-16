# LoadFromINI Function Analysis

**Function Address**: 0x004133BC
**Rank**: #67
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 74

```assembly
004133BC  push     ebp
004133BD  mov      ebp, esp
004133BF  add      esp, -0x24
004133C2  push     ebx
004133C3  push     esi
004133C4  lea      esi, [ebp - 0x24]
004133C7  mov      eax, 0x44099c
004133CC  call     0x403618
004133D1  mov      word ptr [esi + 0x10], 8
004133D7  mov      edx, dword ptr [ebp + 8]
004133DA  mov      dword ptr [edx], 1
004133E0  mov      ebx, dword ptr [ebp + 8]
004133E3  add      ebx, 4
004133E6  mov      dword ptr [ebx + 1], 0x43b500
004133ED  push     0
004133EF  push     0
004133F1  push     0x413f85
004133F6  push     1
004133F8  push     1
004133FA  push     4
004133FC  push     4
004133FE  call     0x438e50
00413403  pop      ecx
00413404  push     eax
00413405  call     0x4037e0
0041340A  add      esp, 0x1c
0041340D  mov      dword ptr [ebx + 5], eax
00413410  mov      dword ptr [ebx + 9], 1
00413417  inc      dword ptr [esi + 0x1c]
0041341A  mov      dword ptr [ebx + 1], 0x4417e4
00413421  add      dword ptr [esi + 0x1c], 2
00413425  mov      dword ptr [ebx + 1], 0x441800
0041342C  xor      eax, eax
0041342E  mov      dword ptr [ebx + 0xd], eax
00413431  mov      dword ptr [ebx + 0x11], 2
00413438  add      dword ptr [esi + 0x1c], 3
0041343C  add      dword ptr [esi + 0x1c], 4
00413440  mov      eax, dword ptr [ebp + 8]
00413443  add      eax, 0x19
00413446  mov      dword ptr [eax], 2
0041344C  add      dword ptr [esi + 0x1c], 5
00413450  add      dword ptr [esi + 0x1c], 6
00413454  add      dword ptr [esi + 0x1c], 7
00413458  mov      eax, dword ptr [ebp + 8]
0041345B  add      eax, 0x1d
0041345E  mov      dword ptr [eax], 0x4402d4
00413464  inc      dword ptr [esi + 0x1c]
00413467  lea      edx, [eax + 4]
0041346A  mov      dword ptr [edx], 0x4402c0
00413470  inc      dword ptr [esi + 0x1c]
00413473  mov      dword ptr [eax], 0x4402e8
00413479  mov      dword ptr [eax + 4], 0x4402f8
00413480  add      dword ptr [esi + 0x1c], 3
00413484  mov      ecx, dword ptr [ebp + 8]
00413487  mov      dword ptr [ecx + 0x25], 0x4417a0
0041348E  mov      eax, dword ptr [ebp + 8]
00413491  mov      dword ptr [eax + 0x1d], 0x4417c0
00413498  mov      edx, dword ptr [ebp + 8]
0041349B  mov      dword ptr [edx + 0x21], 0x4417d0
004134A2  push     dword ptr [ebp + 0x10]
004134A5  push     dword ptr [ebp + 0xc]
004134A8  mov      ecx, dword ptr [ebp + 8]
004134AB  push     ecx
004134AC  mov      eax, dword ptr [ecx + 0x25]
004134AF  call     dword ptr [eax + 0x14]
004134B2  add      esp, 0xc
004134B5  mov      edx, dword ptr [esi]
004134B7  mov      dword ptr fs:[0], edx
004134BE  mov      eax, dword ptr [ebp + 8]
004134C1  pop      esi
004134C2  pop      ebx
004134C3  mov      esp, ebp
004134C5  pop      ebp
004134C6  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## DATA Context

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

## Functions Called

- 0x00403618
- 0x00438E50
- 0x004037E0

---

*Extracted with recursive CALL following and DATA context*
