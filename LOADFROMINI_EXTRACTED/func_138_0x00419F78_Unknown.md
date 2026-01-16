# LoadFromINI Function Analysis

**Function Address**: 0x00419F78
**Rank**: #138
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 72

```assembly
00419F78  push     ebp
00419F79  mov      ebp, esp
00419F7B  add      esp, -0x2c
00419F7E  push     ebx
00419F7F  mov      ebx, dword ptr [ebp + 8]
00419F82  mov      eax, 0x4431b0
00419F87  call     0x403618
00419F8C  cmp      dword ptr [ebx + 0x4d], 0
00419F90  je       0x41a041
00419F96  push     ebx
00419F97  mov      edx, dword ptr [ebx]
00419F99  call     dword ptr [edx + 0x10]
00419F9C  pop      ecx
00419F9D  lea      ecx, [ebx + 0x1d]
00419FA0  push     ecx
00419FA1  push     dword ptr [ebx + 0xc]
00419FA4  call     0x41debb
00419FA9  add      esp, 8
00419FAC  push     ebx
00419FAD  call     0x419361
00419FB2  pop      ecx
00419FB3  mov      ebx, dword ptr [ebx + 8]
00419FB6  cmp      dword ptr [ebx + 0xc], 0
00419FBA  jne      0x41a035
00419FBC  lea      eax, [ebp - 0x2c]
00419FBF  push     eax
00419FC0  push     0
00419FC2  push     0
00419FC4  push     0
00419FC6  push     1
00419FC8  push     0x403be0
00419FCD  push     0
00419FCF  push     0x769
00419FD4  push     0x443577
00419FD9  push     0x44356b
00419FDE  push     0x443593
00419FE3  lea      edx, [ebp - 4]
00419FE6  push     edx
00419FE7  call     0x438f10
00419FEC  add      esp, 0x14
00419FEF  lea      ecx, [ebp - 4]
00419FF2  push     ecx
00419FF3  inc      dword ptr [ebp - 0x10]
00419FF6  lea      eax, [ebp - 8]
00419FF9  push     eax
00419FFA  call     0x438de4
00419FFF  add      esp, 8
0041A002  inc      dword ptr [ebp - 0x10]
0041A005  mov      word ptr [ebp - 0x1c], 0xc
0041A00B  dec      dword ptr [ebp - 0x10]
0041A00E  push     2
0041A010  lea      edx, [ebp - 4]
0041A013  push     edx
0041A014  call     0x438f64
0041A019  add      esp, 8
0041A01C  add      dword ptr [ebp - 0x10], 2
0041A020  add      dword ptr [ebp - 0x10], 3
0041A024  lea      ecx, [ebp - 8]
0041A027  push     ecx
0041A028  push     0x403b88
0041A02D  call     0x438eaa
0041A032  add      esp, 0x24
0041A035  push     0
0041A037  push     0
0041A039  push     dword ptr [ebx + 0xc]
0041A03C  call     0x4391f2
0041A041  mov      eax, dword ptr [ebp - 0x2c]
0041A044  mov      dword ptr fs:[0], eax
0041A04A  pop      ebx
0041A04B  mov      esp, ebp
0041A04D  pop      ebp
0041A04E  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"GetHandle()"` @ 0x0044356B
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443577
- `"Precondition"` @ 0x00443593

## DATA Context

**Context around 0x0044356B**:

- `"window.h"` @ 0x004434EB
- `"Precondition"` @ 0x004434F4
- `"GetHandle()"` @ 0x00443501
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044350D
- `"Precondition"` @ 0x00443529
- `"GetHandle()"` @ 0x00443536
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443542
- `"Precondition"` @ 0x0044355E
- `"GetHandle()"` @ 0x0044356B
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443577
- `"Precondition"` @ 0x00443593
- `"Image->Width() && Image->Height()"` @ 0x004435A0
- `"timernfx.cpp"` @ 0x004435C2
- `"Check"` @ 0x004435CF
- `"tics"` @ 0x004435D5
- `"timernfx.cpp"` @ 0x004435DA
- `"Precondition"` @ 0x004435E7

**Context around 0x00443593**:

- `"\INCLUDE\owl/window.h"` @ 0x00443513
- `"Precondition"` @ 0x00443529
- `"GetHandle()"` @ 0x00443536
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443542
- `"Precondition"` @ 0x0044355E
- `"GetHandle()"` @ 0x0044356B
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443577
- `"Precondition"` @ 0x00443593
- `"Image->Width() && Image->Height()"` @ 0x004435A0
- `"timernfx.cpp"` @ 0x004435C2
- `"Check"` @ 0x004435CF
- `"tics"` @ 0x004435D5
- `"timernfx.cpp"` @ 0x004435DA
- `"Precondition"` @ 0x004435E7
- `"GetHandle()"` @ 0x004435F4
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443600

**Context around 0x00443577**:

- `"condition"` @ 0x004434F7
- `"GetHandle()"` @ 0x00443501
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044350D
- `"Precondition"` @ 0x00443529
- `"GetHandle()"` @ 0x00443536
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443542
- `"Precondition"` @ 0x0044355E
- `"GetHandle()"` @ 0x0044356B
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443577
- `"Precondition"` @ 0x00443593
- `"Image->Width() && Image->Height()"` @ 0x004435A0
- `"timernfx.cpp"` @ 0x004435C2
- `"Check"` @ 0x004435CF
- `"tics"` @ 0x004435D5
- `"timernfx.cpp"` @ 0x004435DA
- `"Precondition"` @ 0x004435E7
- `"GetHandle()"` @ 0x004435F4

## Functions Called

- 0x00403618
- 0x0041DEBB
- 0x00419361
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x004391F2

---

*Extracted with recursive CALL following and DATA context*
