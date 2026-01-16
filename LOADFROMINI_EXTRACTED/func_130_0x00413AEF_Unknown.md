# LoadFromINI Function Analysis

**Function Address**: 0x00413AEF
**Rank**: #130
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 25

```assembly
00413AEF  push     ebp
00413AF0  mov      ebp, esp
00413AF2  push     ebx
00413AF3  push     esi
00413AF4  mov      esi, dword ptr [ebp + 0xc]
00413AF7  mov      ebx, dword ptr [ebp + 8]
00413AFA  cmp      ebx, esi
00413AFC  jne      0x413b02
00413AFE  mov      eax, ebx
00413B00  jmp      0x413b1c
00413B02  cmp      byte ptr [ebp + 0x10], 0
00413B06  je       0x413b10
00413B08  push     ebx
00413B09  mov      edx, dword ptr [ebx + 0x25]
00413B0C  call     dword ptr [edx + 0x10]
00413B0F  pop      ecx
00413B10  push     esi
00413B11  push     ebx
00413B12  call     0x41372f
00413B17  add      esp, 8
00413B1A  mov      eax, ebx
00413B1C  pop      esi
00413B1D  pop      ebx
00413B1E  pop      ebp
00413B1F  ret      
```

## Strings Referenced

**Total unique strings**: 7

- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"!EA"` @ 0x00441848

## DATA Context

**Context around 0x00441848**:

- `">BA"` @ 0x004417F0
- `"FDA"` @ 0x004417F4
- `">BA"` @ 0x0044180C
- `"$#A"` @ 0x00441838
- `"!EA"` @ 0x00441848
- `"%<@"` @ 0x00441850
- `"%<@"` @ 0x00441894

**Context around 0x004414E9**:

- `"%i,%i,%i,%i"` @ 0x00441469
- `" %u %i %i %i %i"` @ 0x00441475
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00441489
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E

**Context around 0x0044150B**:

- `"m == 0 || Data != 0 && index < Lim"` @ 0x0044148B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B

**Context around 0x00441518**:

- `"a != 0 && index < Lim"` @ 0x00441498
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B

**Context around 0x0044153C**:

- `"\classlib/vectimp.h"` @ 0x004414BC
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D

**Context around 0x004414DD**:

- `"_%u"` @ 0x0044145D
- `"0,0,0,0"` @ 0x00441461
- `"%i,%i,%i,%i"` @ 0x00441469
- `" %u %i %i %i %i"` @ 0x00441475
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00441489
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C

**Context around 0x0044155E**:

- `"ur < Upper"` @ 0x004414DE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D
- `"Precondition"` @ 0x004415BE
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004415CB

## Functions Called

- 0x0041372F

---

*Extracted with recursive CALL following and DATA context*
