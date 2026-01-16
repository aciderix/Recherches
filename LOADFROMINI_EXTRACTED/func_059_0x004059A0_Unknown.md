# LoadFromINI Function Analysis

**Function Address**: 0x004059A0
**Rank**: #59
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 56

```assembly
004059A0  push     ebp
004059A1  mov      ebp, esp
004059A3  add      esp, -0x24
004059A6  push     ebx
004059A7  mov      eax, 0x43ab2c
004059AC  call     0x403618
004059B1  mov      word ptr [ebp - 0x14], 8
004059B7  mov      edx, dword ptr [ebp + 8]
004059BA  xor      ecx, ecx
004059BC  mov      dword ptr [edx], ecx
004059BE  mov      ebx, dword ptr [ebp + 8]
004059C1  add      ebx, 4
004059C4  mov      dword ptr [ebx + 1], 0x43b500
004059CB  push     0
004059CD  push     0
004059CF  push     0x4067cd
004059D4  push     1
004059D6  push     1
004059D8  push     4
004059DA  push     4
004059DC  call     0x438e50
004059E1  pop      ecx
004059E2  push     eax
004059E3  call     0x4037e0
004059E8  add      esp, 0x1c
004059EB  mov      dword ptr [ebx + 5], eax
004059EE  mov      dword ptr [ebx + 9], 1
004059F5  inc      dword ptr [ebp - 8]
004059F8  mov      dword ptr [ebx + 1], 0x43b51c
004059FF  add      dword ptr [ebp - 8], 2
00405A03  mov      dword ptr [ebx + 1], 0x43b538
00405A0A  xor      eax, eax
00405A0C  mov      dword ptr [ebx + 0xd], eax
00405A0F  mov      dword ptr [ebx + 0x11], 1
00405A16  add      dword ptr [ebp - 8], 3
00405A1A  add      dword ptr [ebp - 8], 4
00405A1E  mov      eax, dword ptr [ebp + 8]
00405A21  add      eax, 0x19
00405A24  mov      dword ptr [eax], 2
00405A2A  add      dword ptr [ebp - 8], 5
00405A2E  add      dword ptr [ebp - 8], 6
00405A32  add      dword ptr [ebp - 8], 7
00405A36  mov      edx, dword ptr [ebp + 8]
00405A39  mov      dword ptr [edx + 0x1d], 0x43b4ec
00405A40  push     dword ptr [ebp + 0x10]
00405A43  push     dword ptr [ebp + 0xc]
00405A46  push     dword ptr [ebp + 8]
00405A49  call     0x4066a1
00405A4E  add      esp, 0xc
00405A51  mov      ecx, dword ptr [ebp - 0x24]
00405A54  mov      dword ptr fs:[0], ecx
00405A5B  mov      eax, dword ptr [ebp + 8]
00405A5E  pop      ebx
00405A5F  mov      esp, ebp
00405A61  pop      ebp
00405A62  ret      
```

## Strings Referenced

**Total unique strings**: 4

- `"P[@"` @ 0x0043B4EC
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

**Context around 0x0043B4EC**:

- `"LUDE\classlib/vectimp.h"` @ 0x0043B46C
- `"Check"` @ 0x0043B484
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0043B48A
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B4AF
- `"Precondition"` @ 0x0043B4D1
- `"P[@"` @ 0x0043B4EC
- `"cZ@"` @ 0x0043B4F0
- `"+l@"` @ 0x0043B528
- `"+l@"` @ 0x0043B544
- `"1h@"` @ 0x0043B548
- `"-m@"` @ 0x0043B554
- `"%<@"` @ 0x0043B560

**Context around 0x0044EB24**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## Functions Called

- 0x00403618
- 0x00438E50
- 0x004037E0
- 0x004066A1

---

*Extracted with recursive CALL following and DATA context*
