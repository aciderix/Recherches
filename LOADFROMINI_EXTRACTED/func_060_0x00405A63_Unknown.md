# LoadFromINI Function Analysis

**Function Address**: 0x00405A63
**Rank**: #60
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 74

```assembly
00405A63  push     ebp
00405A64  mov      ebp, esp
00405A66  add      esp, -0x24
00405A69  push     ebx
00405A6A  mov      eax, 0x43ab50
00405A6F  call     0x403618
00405A74  mov      dword ptr [ebp - 8], 7
00405A7B  cmp      dword ptr [ebp + 8], 0
00405A7F  je       0x405b41
00405A85  mov      word ptr [ebp - 0x14], 8
00405A8B  mov      edx, dword ptr [ebp + 8]
00405A8E  mov      dword ptr [edx + 0x1d], 0x43b4ec
00405A95  jmp      0x405aa4
00405A97  mov      ecx, dword ptr [ebp + 8]
00405A9A  cmp      dword ptr [ecx + 0x19], 2
00405A9E  je       0x405aa4
00405AA0  xor      eax, eax
00405AA2  jmp      0x405aa9
00405AA4  mov      eax, 1
00405AA9  mov      ebx, dword ptr [ebp + 8]
00405AAC  add      ebx, 4
00405AAF  push     0
00405AB1  push     -1
00405AB3  push     eax
00405AB4  push     ebx
00405AB5  call     0x406ba2
00405ABA  add      esp, 0x10
00405ABD  xor      eax, eax
00405ABF  mov      dword ptr [ebx + 0xd], eax
00405AC2  sub      dword ptr [ebp - 8], 7
00405AC6  add      dword ptr [ebp - 8], 7
00405ACA  sub      dword ptr [ebp - 8], 6
00405ACE  add      dword ptr [ebp - 8], 6
00405AD2  sub      dword ptr [ebp - 8], 5
00405AD6  mov      edx, dword ptr [ebp + 8]
00405AD9  cmp      dword ptr [edx + 0x19], 2
00405ADD  je       0x405ae3
00405ADF  xor      eax, eax
00405AE1  jmp      0x405ae8
00405AE3  mov      eax, 1
00405AE8  mov      ebx, dword ptr [ebp + 8]
00405AEB  add      ebx, 4
00405AEE  push     0
00405AF0  push     -1
00405AF2  push     eax
00405AF3  push     ebx
00405AF4  call     0x406ba2
00405AF9  add      esp, 0x10
00405AFC  xor      eax, eax
00405AFE  mov      dword ptr [ebx + 0xd], eax
00405B01  sub      dword ptr [ebp - 8], 4
00405B05  add      dword ptr [ebp - 8], 4
00405B09  sub      dword ptr [ebp - 8], 3
00405B0D  mov      eax, dword ptr [ebp + 8]
00405B10  add      eax, 4
00405B13  add      dword ptr [ebp - 8], 3
00405B17  sub      dword ptr [ebp - 8], 2
00405B1B  add      dword ptr [ebp - 8], 2
00405B1F  dec      dword ptr [ebp - 8]
00405B22  mov      dword ptr [eax + 1], 0x43b500
00405B29  push     dword ptr [eax + 5]
00405B2C  call     0x438f82
00405B31  pop      ecx
00405B32  test     byte ptr [ebp + 0xc], 1
00405B36  je       0x405b41
00405B38  push     dword ptr [ebp + 8]
00405B3B  call     0x438f16
00405B40  pop      ecx
00405B41  mov      edx, dword ptr [ebp - 0x24]
00405B44  mov      dword ptr fs:[0], edx
00405B4B  pop      ebx
00405B4C  mov      esp, ebp
00405B4E  pop      ebp
00405B4F  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"P[@"` @ 0x0043B4EC

## DATA Context

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

## Functions Called

- 0x00403618
- 0x00406BA2
- 0x00406BA2
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
