# LoadFromINI Function Analysis

**Function Address**: 0x0041F44F
**Rank**: #19
**INI String Count**: 8
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 97

```assembly
0041F44F  push     ebp
0041F450  mov      ebp, esp
0041F452  add      esp, -0x24
0041F455  push     ebx
0041F456  push     esi
0041F457  push     edi
0041F458  lea      edi, [ebp - 0x24]
0041F45B  mov      eax, 0x444d40
0041F460  call     0x403618
0041F465  mov      word ptr [edi + 0x10], 8
0041F46B  mov      edx, dword ptr [ebp + 8]
0041F46E  mov      dword ptr [edx], 0x446a88
0041F474  mov      esi, dword ptr [ebp + 8]
0041F477  add      esi, 4
0041F47A  xor      eax, eax
0041F47C  mov      dword ptr [esi], eax
0041F47E  lea      ebx, [esi + 4]
0041F481  mov      dword ptr [ebx + 1], 0x446a30
0041F488  push     0
0041F48A  push     0
0041F48C  push     0x41f121
0041F491  push     1
0041F493  push     1
0041F495  push     0x52
0041F497  push     0x52
0041F499  call     0x438e50
0041F49E  pop      ecx
0041F49F  push     eax
0041F4A0  call     0x4037e0
0041F4A5  add      esp, 0x1c
0041F4A8  mov      dword ptr [ebx + 5], eax
0041F4AB  mov      dword ptr [ebx + 9], 1
0041F4B2  inc      dword ptr [edi + 0x1c]
0041F4B5  mov      dword ptr [ebx + 1], 0x446a4c
0041F4BC  add      dword ptr [edi + 0x1c], 2
0041F4C0  mov      dword ptr [ebx + 1], 0x446a68
0041F4C7  xor      eax, eax
0041F4C9  mov      dword ptr [ebx + 0xd], eax
0041F4CC  mov      dword ptr [ebx + 0x11], 5
0041F4D3  add      dword ptr [edi + 0x1c], 3
0041F4D7  add      dword ptr [edi + 0x1c], 4
0041F4DB  add      dword ptr [edi + 0x1c], 5
0041F4DF  add      dword ptr [edi + 0x1c], 6
0041F4E3  add      dword ptr [edi + 0x1c], 7
0041F4E7  add      dword ptr [edi + 0x1c], 8
0041F4EB  mov      esi, dword ptr [ebp + 8]
0041F4EE  add      esi, 0x1d
0041F4F1  mov      dword ptr [esi], 5
0041F4F7  lea      ebx, [esi + 4]
0041F4FA  mov      dword ptr [ebx + 1], 0x4469d8
0041F501  push     0
0041F503  push     0
0041F505  push     0x4231b0
0041F50A  push     1
0041F50C  push     -4
0041F50E  push     0x14
0041F510  push     -0x50
0041F512  call     0x438e50
0041F517  pop      ecx
0041F518  push     eax
0041F519  call     0x4037e0
0041F51E  add      esp, 0x1c
0041F521  mov      dword ptr [ebx + 5], eax
0041F524  mov      dword ptr [ebx + 9], 0xfffffffc
0041F52B  inc      dword ptr [edi + 0x1c]
0041F52E  mov      dword ptr [ebx + 1], 0x4469f4
0041F535  add      dword ptr [edi + 0x1c], 2
0041F539  mov      dword ptr [ebx + 1], 0x446a10
0041F540  xor      eax, eax
0041F542  mov      dword ptr [ebx + 0xd], eax
0041F545  mov      dword ptr [ebx + 0x11], 5
0041F54C  add      dword ptr [edi + 0x1c], 3
0041F550  add      dword ptr [edi + 0x1c], 4
0041F554  add      dword ptr [edi + 0x1c], 5
0041F558  add      dword ptr [edi + 0x1c], 6
0041F55C  add      dword ptr [edi + 0x1c], 7
0041F560  add      dword ptr [edi + 0x1c], 8
0041F564  mov      edx, dword ptr [ebp + 8]
0041F567  add      edx, 0x36
0041F56A  push     edx
0041F56B  call     0x438ec2
0041F570  pop      ecx
0041F571  inc      dword ptr [edi + 0x1c]
0041F574  push     dword ptr [ebp + 0x10]
0041F577  push     dword ptr [ebp + 0xc]
0041F57A  push     dword ptr [ebp + 8]
0041F57D  call     0x41f6ae
0041F582  add      esp, 0xc
0041F585  mov      ecx, dword ptr [edi]
0041F587  mov      dword ptr fs:[0], ecx
0041F58E  mov      eax, dword ptr [ebp + 8]
0041F591  pop      edi
0041F592  pop      esi
0041F593  pop      ebx
0041F594  mov      esp, ebp
0041F596  pop      ebp
0041F597  ret      
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
- 0x00438EC2
- 0x0041F6AE

---

*Extracted with recursive CALL following and DATA context*
