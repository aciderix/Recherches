# LoadFromINI Function Analysis

**Function Address**: 0x00418FDE
**Rank**: #76
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 76

```assembly
00418FDE  push     ebp
00418FDF  mov      ebp, esp
00418FE1  add      esp, -0x2c
00418FE4  push     ebx
00418FE5  push     esi
00418FE6  mov      esi, dword ptr [ebp + 0xc]
00418FE9  mov      ebx, dword ptr [ebp + 8]
00418FEC  mov      eax, 0x442ed4
00418FF1  call     0x403618
00418FF6  cmp      dword ptr [ebx + 0x18], 0
00418FFA  je       0x419004
00418FFC  push     ebx
00418FFD  mov      edx, dword ptr [ebx + 0x14]
00419000  call     dword ptr [edx + 0x10]
00419003  pop      ecx
00419004  cmp      dword ptr [esi], 0
00419007  jbe      0x419013
00419009  cmp      dword ptr [esi + 4], 0
0041900D  jne      0x419095
00419013  lea      ecx, [ebp - 0x2c]
00419016  push     ecx
00419017  push     0
00419019  push     0
0041901B  push     0
0041901D  push     1
0041901F  push     0x40690f
00419024  push     0
00419026  mov      word ptr [ebp - 0x1c], 8
0041902C  push     0x5e
0041902E  push     0x443435
00419033  push     0x44340d
00419038  push     0x443442
0041903D  lea      eax, [ebp - 4]
00419040  push     eax
00419041  call     0x438f10
00419046  add      esp, 0x14
00419049  lea      edx, [ebp - 4]
0041904C  push     edx
0041904D  inc      dword ptr [ebp - 0x10]
00419050  lea      ecx, [ebp - 8]
00419053  push     ecx
00419054  call     0x438de4
00419059  add      esp, 8
0041905C  inc      dword ptr [ebp - 0x10]
0041905F  mov      word ptr [ebp - 0x1c], 0x14
00419065  dec      dword ptr [ebp - 0x10]
00419068  push     2
0041906A  lea      eax, [ebp - 4]
0041906D  push     eax
0041906E  call     0x438f64
00419073  add      esp, 8
00419076  mov      word ptr [ebp - 0x1c], 8
0041907C  add      dword ptr [ebp - 0x10], 2
00419080  add      dword ptr [ebp - 0x10], 3
00419084  lea      edx, [ebp - 8]
00419087  push     edx
00419088  push     0x4068bf
0041908D  call     0x438eaa
00419092  add      esp, 0x24
00419095  mov      ecx, dword ptr [esi]
00419097  mov      dword ptr [ebx], ecx
00419099  mov      eax, dword ptr [esi + 4]
0041909C  mov      dword ptr [ebx + 4], eax
0041909F  mov      edx, dword ptr [esi + 8]
004190A2  mov      dword ptr [ebx + 8], edx
004190A5  mov      ecx, dword ptr [esi + 0xc]
004190A8  mov      dword ptr [ebx + 0xc], ecx
004190AB  mov      eax, dword ptr [esi + 0x10]
004190AE  mov      dword ptr [ebx + 0x10], eax
004190B1  mov      edx, dword ptr [ebp - 0x2c]
004190B4  mov      dword ptr fs:[0], edx
004190BB  pop      esi
004190BC  pop      ebx
004190BD  mov      esp, ebp
004190BF  pop      ebp
004190C0  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"data.Delay > 0 && data.TimeProc != NULL"` @ 0x0044340D
- `"timernfx.cpp"` @ 0x00443435
- `"Check"` @ 0x00443442

## DATA Context

**Context around 0x0044340D**:

- `"`3D"` @ 0x00443390
- `"p3D"` @ 0x004433A8
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

**Context around 0x00443435**:

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

**Context around 0x00443442**:

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

## Functions Called

- 0x00403618
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA

---

*Extracted with recursive CALL following and DATA context*
