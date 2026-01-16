# LoadFromINI Function Analysis

**Function Address**: 0x004194E7
**Rank**: #82
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 75

```assembly
004194E7  push     ebp
004194E8  mov      ebp, esp
004194EA  add      esp, -0x2c
004194ED  push     ebx
004194EE  mov      ebx, dword ptr [ebp + 8]
004194F1  mov      eax, 0x443004
004194F6  call     0x403618
004194FB  cmp      dword ptr [ebx + 0x51], 0
004194FF  jbe      0x4195b6
00419505  mov      edx, dword ptr [ebx + 0x51]
00419508  cmp      edx, dword ptr [ebx + 0x4d]
0041950B  je       0x4195bd
00419511  mov      ecx, dword ptr [ebx + 0x51]
00419514  mov      dword ptr [ebx + 0x4d], ecx
00419517  lea      eax, [ebx + 0x3d]
0041951A  push     eax
0041951B  push     dword ptr [ebx + 0xc]
0041951E  call     0x41debb
00419523  add      esp, 8
00419526  mov      ebx, dword ptr [ebx + 8]
00419529  cmp      dword ptr [ebx + 0xc], 0
0041952D  jne      0x4195a8
0041952F  lea      edx, [ebp - 0x2c]
00419532  push     edx
00419533  push     0
00419535  push     0
00419537  push     0
00419539  push     1
0041953B  push     0x403be0
00419540  push     0
00419542  push     0x769
00419547  push     0x443479
0041954C  push     0x44346d
00419551  push     0x443495
00419556  lea      ecx, [ebp - 4]
00419559  push     ecx
0041955A  call     0x438f10
0041955F  add      esp, 0x14
00419562  lea      eax, [ebp - 4]
00419565  push     eax
00419566  inc      dword ptr [ebp - 0x10]
00419569  lea      edx, [ebp - 8]
0041956C  push     edx
0041956D  call     0x438de4
00419572  add      esp, 8
00419575  inc      dword ptr [ebp - 0x10]
00419578  mov      word ptr [ebp - 0x1c], 0xc
0041957E  dec      dword ptr [ebp - 0x10]
00419581  push     2
00419583  lea      ecx, [ebp - 4]
00419586  push     ecx
00419587  call     0x438f64
0041958C  add      esp, 8
0041958F  add      dword ptr [ebp - 0x10], 2
00419593  add      dword ptr [ebp - 0x10], 3
00419597  lea      eax, [ebp - 8]
0041959A  push     eax
0041959B  push     0x403b88
004195A0  call     0x438eaa
004195A5  add      esp, 0x24
004195A8  push     0
004195AA  push     0
004195AC  push     dword ptr [ebx + 0xc]
004195AF  call     0x4391f2
004195B4  jmp      0x4195bd
004195B6  push     ebx
004195B7  mov      edx, dword ptr [ebx]
004195B9  call     dword ptr [edx + 0x14]
004195BC  pop      ecx
004195BD  mov      ecx, dword ptr [ebp - 0x2c]
004195C0  mov      dword ptr fs:[0], ecx
004195C7  pop      ebx
004195C8  mov      esp, ebp
004195CA  pop      ebp
004195CB  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"GetHandle()"` @ 0x0044346D
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443479
- `"Precondition"` @ 0x00443495

## DATA Context

**Context around 0x00443479**:

- `"fx.cpp"` @ 0x004433F9
- `"Precondition"` @ 0x00443400
- `"data.Delay > 0 && data.TimeProc != NULL"` @ 0x0044340D
- `"timernfx.cpp"` @ 0x00443435
- `"Check"` @ 0x00443442
- `"img && wnd"` @ 0x00443448
- `"timernfx.cpp"` @ 0x00443453
- `"Precondition"` @ 0x00443460
- `"GetHandle()"` @ 0x0044346D
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443479
- `"Precondition"` @ 0x00443495
- `"Image && Window"` @ 0x004434A2
- `"timernfx.cpp"` @ 0x004434B2
- `"Precondition"` @ 0x004434BF
- `"GetHandle()"` @ 0x004434CC
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004434D8
- `"Precondition"` @ 0x004434F4

**Context around 0x0044346D**:

- `"n > 0"` @ 0x004433ED
- `"timernfx.cpp"` @ 0x004433F3
- `"Precondition"` @ 0x00443400
- `"data.Delay > 0 && data.TimeProc != NULL"` @ 0x0044340D
- `"timernfx.cpp"` @ 0x00443435
- `"Check"` @ 0x00443442
- `"img && wnd"` @ 0x00443448
- `"timernfx.cpp"` @ 0x00443453
- `"Precondition"` @ 0x00443460
- `"GetHandle()"` @ 0x0044346D
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443479
- `"Precondition"` @ 0x00443495
- `"Image && Window"` @ 0x004434A2
- `"timernfx.cpp"` @ 0x004434B2
- `"Precondition"` @ 0x004434BF
- `"GetHandle()"` @ 0x004434CC
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004434D8

**Context around 0x00443495**:

- `"ay > 0 && data.TimeProc != NULL"` @ 0x00443415
- `"timernfx.cpp"` @ 0x00443435
- `"Check"` @ 0x00443442
- `"img && wnd"` @ 0x00443448
- `"timernfx.cpp"` @ 0x00443453
- `"Precondition"` @ 0x00443460
- `"GetHandle()"` @ 0x0044346D
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443479
- `"Precondition"` @ 0x00443495
- `"Image && Window"` @ 0x004434A2
- `"timernfx.cpp"` @ 0x004434B2
- `"Precondition"` @ 0x004434BF
- `"GetHandle()"` @ 0x004434CC
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004434D8
- `"Precondition"` @ 0x004434F4
- `"GetHandle()"` @ 0x00443501
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044350D

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
