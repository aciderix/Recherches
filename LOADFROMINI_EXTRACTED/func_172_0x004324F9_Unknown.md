# LoadFromINI Function Analysis

**Function Address**: 0x004324F9
**Rank**: #172
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 29

```assembly
004324F9  push     ebp
004324FA  mov      ebp, esp
004324FC  push     ebx
004324FD  mov      ebx, dword ptr [ebp + 8]
00432500  lea      eax, [ebx + 0x8e]
00432506  mov      edx, dword ptr [eax + 4]
00432509  inc      edx
0043250A  cmp      edx, dword ptr [eax + 8]
0043250D  jge      0x432517
0043250F  mov      ecx, dword ptr [eax + 4]
00432512  inc      ecx
00432513  test     ecx, ecx
00432515  jge      0x43251b
00432517  xor      eax, eax
00432519  jmp      0x432520
0043251B  mov      eax, 1
00432520  test     al, al
00432522  je       0x43253b
00432524  lea      edx, [ebx + 0x8e]
0043252A  push     edx
0043252B  call     0x436086
00432530  pop      ecx
00432531  push     eax
00432532  push     ebx
00432533  call     0x43243c
00432538  add      esp, 8
0043253B  pop      ebx
0043253C  pop      ebp
0043253D  ret      
```

## Strings Referenced

**Total unique strings**: 13

- `"P[@"` @ 0x0043B4EC
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"GetHandle()"` @ 0x00449209
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00449215
- `"Precondition"` @ 0x00449231
- `"GetHandle()"` @ 0x0044923E
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044924A
- `"Precondition"` @ 0x00449266
- `"CanDoNext()"` @ 0x0044CF67
- `"histqueu.h"` @ 0x0044CF73
- `"Precondition"` @ 0x0044CF7E

## DATA Context

**Context around 0x00448F05**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E

**Context around 0x00449266**:

- `"\INCLUDE\owl/window.h"` @ 0x004491E6
- `"Precondition"` @ 0x004491FC
- `"GetHandle()"` @ 0x00449209
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00449215
- `"Precondition"` @ 0x00449231
- `"GetHandle()"` @ 0x0044923E
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044924A
- `"Precondition"` @ 0x00449266
- `"VNSetDLLArguments"` @ 0x00449273
- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x00449285
- `"C:\BC5\INCLUDE\owl/module.h"` @ 0x004492A9
- `"Precondition"` @ 0x004492C5
- `"VNCreateDLLWindow"` @ 0x004492D2
- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x004492E4

**Context around 0x0044CF67**:

- `"mp.h"` @ 0x0044CEE7
- `"Check"` @ 0x0044CEEC
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044CEF2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CF17
- `"Precondition"` @ 0x0044CF39
- `"Size > 0"` @ 0x0044CF46
- `"histqueu.h"` @ 0x0044CF4F
- `"Precondition"` @ 0x0044CF5A
- `"CanDoNext()"` @ 0x0044CF67
- `"histqueu.h"` @ 0x0044CF73
- `"Precondition"` @ 0x0044CF7E
- `"CanDoPrev()"` @ 0x0044CF8B
- `"histqueu.h"` @ 0x0044CF97
- `"Precondition"` @ 0x0044CFA2
- `"GetHandle()"` @ 0x0044CFB0
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044CFBC
- `"Precondition"` @ 0x0044CFD8

**Context around 0x0044923E**:

- `"window.h"` @ 0x004491BE
- `"Precondition"` @ 0x004491C7
- `"GetHandle()"` @ 0x004491D4
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004491E0
- `"Precondition"` @ 0x004491FC
- `"GetHandle()"` @ 0x00449209
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00449215
- `"Precondition"` @ 0x00449231
- `"GetHandle()"` @ 0x0044923E
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044924A
- `"Precondition"` @ 0x00449266
- `"VNSetDLLArguments"` @ 0x00449273
- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x00449285
- `"C:\BC5\INCLUDE\owl/module.h"` @ 0x004492A9

**Context around 0x00449209**:

- `"window.h"` @ 0x00449189
- `"Precondition"` @ 0x00449192
- `"GetHandle()"` @ 0x0044919F
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004491AB
- `"Precondition"` @ 0x004491C7
- `"GetHandle()"` @ 0x004491D4
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004491E0
- `"Precondition"` @ 0x004491FC
- `"GetHandle()"` @ 0x00449209
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00449215
- `"Precondition"` @ 0x00449231
- `"GetHandle()"` @ 0x0044923E
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044924A
- `"Precondition"` @ 0x00449266
- `"VNSetDLLArguments"` @ 0x00449273
- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x00449285

**Context around 0x00448F2A**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E
- `"Precondition"` @ 0x00448FA0

**Context around 0x0044924A**:

- `"condition"` @ 0x004491CA
- `"GetHandle()"` @ 0x004491D4
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004491E0
- `"Precondition"` @ 0x004491FC
- `"GetHandle()"` @ 0x00449209
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00449215
- `"Precondition"` @ 0x00449231
- `"GetHandle()"` @ 0x0044923E
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044924A
- `"Precondition"` @ 0x00449266
- `"VNSetDLLArguments"` @ 0x00449273
- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x00449285
- `"C:\BC5\INCLUDE\owl/module.h"` @ 0x004492A9
- `"Precondition"` @ 0x004492C5

**Context around 0x00448F4C**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E
- `"Precondition"` @ 0x00448FA0
- `"GetHandle()"` @ 0x00448FAD
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00448FB9

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

**Context around 0x00449231**:

- `"\INCLUDE\owl/window.h"` @ 0x004491B1
- `"Precondition"` @ 0x004491C7
- `"GetHandle()"` @ 0x004491D4
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004491E0
- `"Precondition"` @ 0x004491FC
- `"GetHandle()"` @ 0x00449209
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00449215
- `"Precondition"` @ 0x00449231
- `"GetHandle()"` @ 0x0044923E
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044924A
- `"Precondition"` @ 0x00449266
- `"VNSetDLLArguments"` @ 0x00449273
- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x00449285
- `"C:\BC5\INCLUDE\owl/module.h"` @ 0x004492A9

## Functions Called

- 0x00436086
- 0x0043243C

---

*Extracted with recursive CALL following and DATA context*
