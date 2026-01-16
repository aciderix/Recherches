# LoadFromINI Function Analysis

**Function Address**: 0x004120F3
**Rank**: #7
**INI String Count**: 13
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 50

```assembly
004120F3  push     ebp
004120F4  mov      ebp, esp
004120F6  push     ebx
004120F7  push     esi
004120F8  push     edi
004120F9  mov      esi, dword ptr [ebp + 0x10]
004120FC  mov      ebx, dword ptr [ebp + 8]
004120FF  push     dword ptr [ebx + 0x39]
00412102  call     0x438f82
00412107  pop      ecx
00412108  cmp      dword ptr [ebp + 0xc], 0
0041210C  je       0x412159
0041210E  cmp      esi, 1
00412111  jbe      0x412159
00412113  mov      dword ptr [ebx + 0x35], esi
00412116  push     0
00412118  push     0
0041211A  push     0x413fc9
0041211F  push     1
00412121  push     esi
00412122  push     8
00412124  push     0
00412126  call     0x4037e0
0041212B  add      esp, 0x1c
0041212E  mov      dword ptr [ebx + 0x39], eax
00412131  xor      eax, eax
00412133  cmp      esi, eax
00412135  jbe      0x412150
00412137  mov      edx, dword ptr [ebx + 0x39]
0041213A  mov      ecx, dword ptr [ebp + 0xc]
0041213D  mov      edi, dword ptr [ecx + eax*8]
00412140  mov      dword ptr [edx + eax*8], edi
00412143  mov      edi, dword ptr [ecx + eax*8 + 4]
00412147  mov      dword ptr [edx + eax*8 + 4], edi
0041214B  inc      eax
0041214C  cmp      esi, eax
0041214E  ja       0x412137
00412150  push     ebx
00412151  call     0x412168
00412156  pop      ecx
00412157  jmp      0x412163
00412159  xor      eax, eax
0041215B  mov      dword ptr [ebx + 0x35], eax
0041215E  xor      edx, edx
00412160  mov      dword ptr [ebx + 0x39], edx
00412163  pop      edi
00412164  pop      esi
00412165  pop      ebx
00412166  pop      ebp
00412167  ret      
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

- 0x00438F82
- 0x004037E0
- 0x00412168

---

*Extracted with recursive CALL following and DATA context*
