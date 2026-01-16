# LoadFromINI Function Analysis

**Function Address**: 0x0041930A
**Rank**: #79
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 28

```assembly
0041930A  push     ebp
0041930B  mov      ebp, esp
0041930D  add      esp, -0x24
00419310  mov      eax, 0x442fc4
00419315  call     0x403618
0041931A  mov      word ptr [ebp - 0x14], 8
00419320  push     dword ptr [ebp + 0x10]
00419323  push     dword ptr [ebp + 0xc]
00419326  push     dword ptr [ebp + 8]
00419329  call     0x41912a
0041932E  add      esp, 0xc
00419331  inc      dword ptr [ebp - 8]
00419334  mov      edx, dword ptr [ebp + 8]
00419337  mov      dword ptr [edx], 0x443660
0041933D  push     dword ptr [ebp + 8]
00419340  call     0x419361
00419345  pop      ecx
00419346  mov      ecx, dword ptr [ebp + 8]
00419349  push     ecx
0041934A  mov      eax, dword ptr [ecx]
0041934C  call     dword ptr [eax + 4]
0041934F  pop      ecx
00419350  mov      edx, dword ptr [ebp - 0x24]
00419353  mov      dword ptr fs:[0], edx
0041935A  mov      eax, dword ptr [ebp + 8]
0041935D  mov      esp, ebp
0041935F  pop      ebp
00419360  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"img && wnd"` @ 0x00443448
- `"timernfx.cpp"` @ 0x00443453
- `"Precondition"` @ 0x00443460

## DATA Context

**Context around 0x00443448**:

- `"resolution > 0"` @ 0x004433E4
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

**Context around 0x00443453**:

- `"resolution > 0"` @ 0x004433E4
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

**Context around 0x00443460**:

- `"resolution > 0"` @ 0x004433E4
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

## Functions Called

- 0x00403618
- 0x0041912A
- 0x00419361

---

*Extracted with recursive CALL following and DATA context*
