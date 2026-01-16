# LoadFromINI Function Analysis

**Function Address**: 0x00419E5D
**Rank**: #137
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 96

```assembly
00419E5D  push     ebp
00419E5E  mov      ebp, esp
00419E60  add      esp, -0x2c
00419E63  push     ebx
00419E64  mov      ebx, dword ptr [ebp + 8]
00419E67  mov      eax, 0x443164
00419E6C  call     0x403618
00419E71  xor      edx, edx
00419E73  mov      dword ptr [ebx + 0x51], edx
00419E76  lea      eax, [ebx + 0x3d]
00419E79  xor      edx, edx
00419E7B  mov      dword ptr [eax], edx
00419E7D  xor      ecx, ecx
00419E7F  mov      dword ptr [eax + 4], ecx
00419E82  xor      edx, edx
00419E84  mov      dword ptr [eax + 8], edx
00419E87  xor      ecx, ecx
00419E89  mov      dword ptr [eax + 0xc], ecx
00419E8C  mov      dword ptr [ebx + 0x4d], 1
00419E93  lea      eax, [ebx + 0x2d]
00419E96  push     eax
00419E97  push     dword ptr [ebx + 0xc]
00419E9A  call     0x41debb
00419E9F  add      esp, 8
00419EA2  mov      eax, dword ptr [ebx + 0xc]
00419EA5  add      eax, 0xd
00419EA8  mov      edx, dword ptr [eax + 8]
00419EAB  sub      edx, dword ptr [eax]
00419EAD  test     edx, edx
00419EAF  jle      0x419ec1
00419EB1  mov      eax, dword ptr [ebx + 0xc]
00419EB4  add      eax, 0xd
00419EB7  mov      edx, dword ptr [eax + 0xc]
00419EBA  sub      edx, dword ptr [eax + 4]
00419EBD  test     edx, edx
00419EBF  jg       0x419ed9
00419EC1  push     ebx
00419EC2  mov      ecx, dword ptr [ebx]
00419EC4  call     dword ptr [ecx + 0x14]
00419EC7  pop      ecx
00419EC8  xor      eax, eax
00419ECA  mov      edx, dword ptr [ebp - 0x2c]
00419ECD  mov      dword ptr fs:[0], edx
00419ED4  jmp      0x419f73
00419ED9  mov      ebx, dword ptr [ebx + 8]
00419EDC  cmp      dword ptr [ebx + 0xc], 0
00419EE0  jne      0x419f5b
00419EE2  lea      ecx, [ebp - 0x2c]
00419EE5  push     ecx
00419EE6  push     0
00419EE8  push     0
00419EEA  push     0
00419EEC  push     1
00419EEE  push     0x403be0
00419EF3  push     0
00419EF5  push     0x769
00419EFA  push     0x443542
00419EFF  push     0x443536
00419F04  push     0x44355e
00419F09  lea      eax, [ebp - 4]
00419F0C  push     eax
00419F0D  call     0x438f10
00419F12  add      esp, 0x14
00419F15  lea      edx, [ebp - 4]
00419F18  push     edx
00419F19  inc      dword ptr [ebp - 0x10]
00419F1C  lea      ecx, [ebp - 8]
00419F1F  push     ecx
00419F20  call     0x438de4
00419F25  add      esp, 8
00419F28  inc      dword ptr [ebp - 0x10]
00419F2B  mov      word ptr [ebp - 0x1c], 0xc
00419F31  dec      dword ptr [ebp - 0x10]
00419F34  push     2
00419F36  lea      eax, [ebp - 4]
00419F39  push     eax
00419F3A  call     0x438f64
00419F3F  add      esp, 8
00419F42  add      dword ptr [ebp - 0x10], 2
00419F46  add      dword ptr [ebp - 0x10], 3
00419F4A  lea      edx, [ebp - 8]
00419F4D  push     edx
00419F4E  push     0x403b88
00419F53  call     0x438eaa
00419F58  add      esp, 0x24
00419F5B  push     0
00419F5D  push     0
00419F5F  push     dword ptr [ebx + 0xc]
00419F62  call     0x4391f2
00419F67  mov      al, 1
00419F69  mov      edx, dword ptr [ebp - 0x2c]
00419F6C  mov      dword ptr fs:[0], edx
00419F73  pop      ebx
00419F74  mov      esp, ebp
00419F76  pop      ebp
00419F77  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"GetHandle()"` @ 0x00443536
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443542
- `"Precondition"` @ 0x0044355E

## DATA Context

**Context around 0x0044355E**:

- `"\INCLUDE\owl/window.h"` @ 0x004434DE
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

**Context around 0x00443542**:

- `"condition"` @ 0x004434C2
- `"GetHandle()"` @ 0x004434CC
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004434D8
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

**Context around 0x00443536**:

- `"rnfx.cpp"` @ 0x004434B6
- `"Precondition"` @ 0x004434BF
- `"GetHandle()"` @ 0x004434CC
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004434D8
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

## Functions Called

- 0x00403618
- 0x0041DEBB
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x004391F2

---

*Extracted with recursive CALL following and DATA context*
