# LoadFromINI Function Analysis

**Function Address**: 0x00405E1C
**Rank**: #94
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 152

```assembly
00405E1C  push     ebp
00405E1D  mov      ebp, esp
00405E1F  add      esp, -0x40
00405E22  push     ebx
00405E23  push     esi
00405E24  push     edi
00405E25  mov      ebx, dword ptr [ebp + 8]
00405E28  mov      eax, 0x43ac88
00405E2D  call     0x403618
00405E32  mov      edx, dword ptr [ebp + 0xc]
00405E35  mov      ecx, dword ptr [edx]
00405E37  cmp      dword ptr [ecx + 6], 0
00405E3B  je       0x405fc0
00405E41  xor      eax, eax
00405E43  mov      dword ptr [ebp - 0x38], eax
00405E46  jmp      0x405fac
00405E4B  mov      edi, dword ptr [ebp - 0x38]
00405E4E  cmp      edi, dword ptr [ebx]
00405E50  jl       0x405e5b
00405E52  mov      edx, edi
00405E54  sub      edx, dword ptr [ebx]
00405E56  cmp      edx, dword ptr [ebx + 0xd]
00405E59  jb       0x405ed4
00405E5B  lea      ecx, [ebp - 0x34]
00405E5E  push     ecx
00405E5F  push     0
00405E61  push     0
00405E63  push     0
00405E65  push     1
00405E67  push     0x403be0
00405E6C  push     0
00405E6E  push     0x15e
00405E73  push     0x43b265
00405E78  push     0x43b233
00405E7D  push     0x43b286
00405E82  lea      eax, [ebp - 4]
00405E85  push     eax
00405E86  call     0x438f10
00405E8B  add      esp, 0x14
00405E8E  lea      edx, [ebp - 4]
00405E91  push     edx
00405E92  inc      dword ptr [ebp - 0x18]
00405E95  lea      ecx, [ebp - 8]
00405E98  push     ecx
00405E99  call     0x438de4
00405E9E  add      esp, 8
00405EA1  inc      dword ptr [ebp - 0x18]
00405EA4  mov      word ptr [ebp - 0x24], 0xc
00405EAA  dec      dword ptr [ebp - 0x18]
00405EAD  push     2
00405EAF  lea      eax, [ebp - 4]
00405EB2  push     eax
00405EB3  call     0x438f64
00405EB8  add      esp, 8
00405EBB  add      dword ptr [ebp - 0x18], 2
00405EBF  add      dword ptr [ebp - 0x18], 3
00405EC3  lea      edx, [ebp - 8]
00405EC6  push     edx
00405EC7  push     0x403b88
00405ECC  call     0x438eaa
00405ED1  add      esp, 0x24
00405ED4  sub      edi, dword ptr [ebx]
00405ED6  mov      dword ptr [ebp - 0x3c], edi
00405ED9  lea      esi, [ebx + 4]
00405EDC  cmp      dword ptr [esi + 9], 0
00405EE0  jbe      0x405ef0
00405EE2  cmp      dword ptr [esi + 5], 0
00405EE6  je       0x405ef0
00405EE8  mov      eax, dword ptr [ebp - 0x3c]
00405EEB  cmp      eax, dword ptr [esi + 9]
00405EEE  jb       0x405f69
00405EF0  lea      edx, [ebp - 0x34]
00405EF3  push     edx
00405EF4  push     0
00405EF6  push     0
00405EF8  push     0
00405EFA  push     1
00405EFC  push     0x403be0
00405F01  push     0
00405F03  push     0x33a
00405F08  push     0x43b2b7
00405F0D  push     0x43b293
00405F12  push     0x43b2d9
00405F17  lea      ecx, [ebp - 0xc]
00405F1A  push     ecx
00405F1B  call     0x438f10
00405F20  add      esp, 0x14
00405F23  lea      eax, [ebp - 0xc]
00405F26  push     eax
00405F27  inc      dword ptr [ebp - 0x18]
00405F2A  lea      edx, [ebp - 0x10]
00405F2D  push     edx
00405F2E  call     0x438de4
00405F33  add      esp, 8
00405F36  inc      dword ptr [ebp - 0x18]
00405F39  mov      word ptr [ebp - 0x24], 0x18
00405F3F  dec      dword ptr [ebp - 0x18]
00405F42  push     2
00405F44  lea      ecx, [ebp - 0xc]
00405F47  push     ecx
00405F48  call     0x438f64
00405F4D  add      esp, 8
00405F50  add      dword ptr [ebp - 0x18], 2
00405F54  add      dword ptr [ebp - 0x18], 3
00405F58  lea      eax, [ebp - 0x10]
00405F5B  push     eax
00405F5C  push     0x403b88
00405F61  call     0x438eaa
00405F66  add      esp, 0x24
00405F69  mov      edx, dword ptr [ebp - 0x3c]
00405F6C  shl      edx, 2
00405F6F  add      edx, dword ptr [esi + 5]
00405F72  mov      esi, dword ptr [edx]
00405F74  mov      edi, dword ptr [ebp + 0xc]
00405F77  lea      ecx, [esi + 4]
00405F7A  mov      dword ptr [ebp - 0x40], ecx
00405F7D  push     edi
00405F7E  push     dword ptr [ebp - 0x40]
00405F81  call     0x438ec8
00405F86  add      esp, 8
00405F89  test     eax, eax
00405F8B  jne      0x405fa9
00405F8D  cmp      dword ptr [ebp + 0x10], 0
00405F91  je       0x405f9b
00405F93  mov      eax, dword ptr [ebp + 0x10]
00405F96  mov      edx, dword ptr [ebp - 0x38]
00405F99  mov      dword ptr [eax], edx
00405F9B  mov      eax, esi
00405F9D  mov      edx, dword ptr [ebp - 0x34]
00405FA0  mov      dword ptr fs:[0], edx
00405FA7  jmp      0x405fdb
00405FA9  inc      dword ptr [ebp - 0x38]
00405FAC  lea      ecx, [ebx + 4]
00405FAF  push     ecx
00405FB0  mov      eax, dword ptr [ebx + 5]
00405FB3  call     dword ptr [eax + 4]
00405FB6  pop      ecx
00405FB7  cmp      eax, dword ptr [ebp - 0x38]
00405FBA  jg       0x405e4b
00405FC0  cmp      dword ptr [ebp + 0x10], 0
00405FC4  je       0x405fcf
00405FC6  mov      edx, dword ptr [ebp + 0x10]
00405FC9  mov      dword ptr [edx], 0x7fffffff
00405FCF  xor      eax, eax
00405FD1  mov      edx, dword ptr [ebp - 0x34]
00405FD4  mov      dword ptr fs:[0], edx
00405FDB  pop      edi
00405FDC  pop      esi
00405FDD  pop      ebx
00405FDE  mov      esp, ebp
00405FE0  pop      ebp
00405FE1  ret      
```

## Strings Referenced

**Total unique strings**: 6

- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B233
- `"C:\BC5\INCLUDE\classlib\arrays.h"` @ 0x0043B265
- `"Precondition"` @ 0x0043B286
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B293
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2B7
- `"Precondition"` @ 0x0043B2D9

## DATA Context

**Context around 0x0043B265**:

- `" 0 && Data != 0 && index < Lim"` @ 0x0043B1E5
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B204
- `"Precondition"` @ 0x0043B226
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B233
- `"C:\BC5\INCLUDE\classlib\arrays.h"` @ 0x0043B265
- `"Precondition"` @ 0x0043B286
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B293
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2B7
- `"Precondition"` @ 0x0043B2D9

**Context around 0x0043B286**:

- `"\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B206
- `"Precondition"` @ 0x0043B226
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B233
- `"C:\BC5\INCLUDE\classlib\arrays.h"` @ 0x0043B265
- `"Precondition"` @ 0x0043B286
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B293
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2B7
- `"Precondition"` @ 0x0043B2D9
- `"Cur < Upper"` @ 0x0043B2E6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2F2

**Context around 0x0043B233**:

- `"\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B1B3
- `"Precondition"` @ 0x0043B1D3
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B1E0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B204
- `"Precondition"` @ 0x0043B226
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B233
- `"C:\BC5\INCLUDE\classlib\arrays.h"` @ 0x0043B265
- `"Precondition"` @ 0x0043B286
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B293

**Context around 0x0043B293**:

- `"classlib/vectimp.h"` @ 0x0043B213
- `"Precondition"` @ 0x0043B226
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B233
- `"C:\BC5\INCLUDE\classlib\arrays.h"` @ 0x0043B265
- `"Precondition"` @ 0x0043B286
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B293
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2B7
- `"Precondition"` @ 0x0043B2D9
- `"Cur < Upper"` @ 0x0043B2E6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2F2

**Context around 0x0043B2B7**:

- `">= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B237
- `"C:\BC5\INCLUDE\classlib\arrays.h"` @ 0x0043B265
- `"Precondition"` @ 0x0043B286
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B293
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2B7
- `"Precondition"` @ 0x0043B2D9
- `"Cur < Upper"` @ 0x0043B2E6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2F2
- `"Precondition"` @ 0x0043B314
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B321

**Context around 0x0043B2D9**:

- `"ata.Limit()"` @ 0x0043B259
- `"C:\BC5\INCLUDE\classlib\arrays.h"` @ 0x0043B265
- `"Precondition"` @ 0x0043B286
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B293
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2B7
- `"Precondition"` @ 0x0043B2D9
- `"Cur < Upper"` @ 0x0043B2E6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B2F2
- `"Precondition"` @ 0x0043B314
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B321
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B345

## Functions Called

- 0x00403618
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438EC8

---

*Extracted with recursive CALL following and DATA context*
