# LoadFromINI Function Analysis

**Function Address**: 0x004132F1
**Rank**: #66
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 85

```assembly
004132F1  push     ebp
004132F2  mov      ebp, esp
004132F4  push     ecx
004132F5  push     ebx
004132F6  push     esi
004132F7  push     edi
004132F8  mov      ebx, dword ptr [ebp + 8]
004132FB  push     ebx
004132FC  mov      eax, dword ptr [ebx]
004132FE  call     dword ptr [eax + 0xc]
00413301  pop      ecx
00413302  push     dword ptr [ebp + 0x10]
00413305  push     dword ptr [ebp + 0xc]
00413308  lea      edx, [ebx + 8]
0041330B  push     edx
0041330C  mov      ecx, dword ptr [ebx + 0x29]
0041330F  call     dword ptr [ecx + 0x14]
00413312  add      esp, 0xc
00413315  lea      edi, [ebx + 0x2d]
00413318  mov      esi, dword ptr [ebp + 0xc]
0041331B  push     esi
0041331C  call     0x439186
00413321  pop      ecx
00413322  mov      dword ptr [edi], eax
00413324  push     esi
00413325  call     0x439186
0041332A  pop      ecx
0041332B  test     eax, eax
0041332D  je       0x413393
0041332F  mov      dword ptr [ebx + 0x35], eax
00413332  push     0
00413334  push     0
00413336  push     0x413fc9
0041333B  push     1
0041333D  push     dword ptr [ebx + 0x35]
00413340  push     8
00413342  push     0
00413344  call     0x4037e0
00413349  add      esp, 0x1c
0041334C  mov      dword ptr [ebx + 0x39], eax
0041334F  xor      esi, esi
00413351  jmp      0x413387
00413353  mov      eax, esi
00413355  shl      eax, 3
00413358  add      eax, dword ptr [ebx + 0x39]
0041335B  add      eax, 4
0041335E  mov      dword ptr [ebp - 4], eax
00413361  mov      eax, esi
00413363  shl      eax, 3
00413366  add      eax, dword ptr [ebx + 0x39]
00413369  mov      edi, dword ptr [ebp + 0xc]
0041336C  push     4
0041336E  push     eax
0041336F  push     edi
00413370  call     0x439192
00413375  add      esp, 0xc
00413378  push     4
0041337A  push     dword ptr [ebp - 4]
0041337D  push     edi
0041337E  call     0x439192
00413383  add      esp, 0xc
00413386  inc      esi
00413387  cmp      esi, dword ptr [ebx + 0x35]
0041338A  jb       0x413353
0041338C  push     ebx
0041338D  call     0x412168
00413392  pop      ecx
00413393  mov      eax, dword ptr [ebp + 0x10]
00413396  cmp      dword ptr [eax + 4], 0x2000c
0041339D  setae    dl
004133A0  and      edx, 1
004133A3  test     dl, dl
004133A5  je       0x4133b6
004133A7  lea      esi, [ebx + 0x31]
004133AA  mov      ebx, dword ptr [ebp + 0xc]
004133AD  push     ebx
004133AE  call     0x439186
004133B3  pop      ecx
004133B4  mov      dword ptr [esi], eax
004133B6  pop      edi
004133B7  pop      esi
004133B8  pop      ebx
004133B9  pop      ecx
004133BA  pop      ebp
004133BB  ret      
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

- 0x00439186
- 0x00439186
- 0x004037E0
- 0x00439192
- 0x00439192
- 0x00412168
- 0x00439186

---

*Extracted with recursive CALL following and DATA context*
