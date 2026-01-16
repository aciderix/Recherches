# LoadFromINI Function Analysis

**Function Address**: 0x0043243C
**Rank**: #169
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 31

```assembly
0043243C  push     ebp
0043243D  mov      ebp, esp
0043243F  push     ebx
00432440  push     esi
00432441  push     edi
00432442  mov      ebx, dword ptr [ebp + 0xc]
00432445  mov      esi, dword ptr [ebp + 8]
00432448  mov      edi, ebx
0043244A  push     0x44ec34
0043244F  push     edi
00432450  call     0x438ec8
00432455  add      esp, 8
00432458  test     eax, eax
0043245A  jne      0x43246e
0043245C  push     0
0043245E  push     0
00432460  push     dword ptr [ebx + 4]
00432463  push     esi
00432464  call     0x4268f8
00432469  add      esp, 0x10
0043246C  jmp      0x43247b
0043246E  push     dword ptr [ebx + 4]
00432471  push     ebx
00432472  push     esi
00432473  call     0x42908f
00432478  add      esp, 0xc
0043247B  pop      edi
0043247C  pop      esi
0043247D  pop      ebx
0043247E  pop      ebp
0043247F  ret      
```

## Strings Referenced

**Total unique strings**: 10

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

**Context around 0x00449215**:

- `"condition"` @ 0x00449195
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

## Functions Called

- 0x00438EC8
- 0x004268F8
- 0x0042908F

---

*Extracted with recursive CALL following and DATA context*
