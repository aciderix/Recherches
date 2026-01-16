# LoadFromINI Function Analysis

**Function Address**: 0x0041912A
**Rank**: #78
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 79

```assembly
0041912A  push     ebp
0041912B  mov      ebp, esp
0041912D  add      esp, -0x2c
00419130  push     ebx
00419131  push     esi
00419132  mov      esi, dword ptr [ebp + 0x10]
00419135  mov      ebx, dword ptr [ebp + 0xc]
00419138  mov      eax, 0x442f30
0041913D  call     0x403618
00419142  mov      word ptr [ebp - 0x1c], 8
00419148  mov      edx, dword ptr [ebp + 8]
0041914B  mov      dword ptr [edx], 0x443684
00419151  test     esi, esi
00419153  je       0x41915d
00419155  test     ebx, ebx
00419157  jne      0x4191e2
0041915D  lea      ecx, [ebp - 0x2c]
00419160  push     ecx
00419161  push     0
00419163  push     0
00419165  push     0
00419167  push     1
00419169  push     0x403be0
0041916E  push     0
00419170  mov      word ptr [ebp - 0x1c], 0x14
00419176  push     0x94
0041917B  push     0x443453
00419180  push     0x443448
00419185  push     0x443460
0041918A  lea      eax, [ebp - 4]
0041918D  push     eax
0041918E  call     0x438f10
00419193  add      esp, 0x14
00419196  lea      edx, [ebp - 4]
00419199  push     edx
0041919A  inc      dword ptr [ebp - 0x10]
0041919D  lea      ecx, [ebp - 8]
004191A0  push     ecx
004191A1  call     0x438de4
004191A6  add      esp, 8
004191A9  inc      dword ptr [ebp - 0x10]
004191AC  mov      word ptr [ebp - 0x1c], 0x20
004191B2  dec      dword ptr [ebp - 0x10]
004191B5  push     2
004191B7  lea      eax, [ebp - 4]
004191BA  push     eax
004191BB  call     0x438f64
004191C0  add      esp, 8
004191C3  mov      word ptr [ebp - 0x1c], 0x14
004191C9  add      dword ptr [ebp - 0x10], 2
004191CD  add      dword ptr [ebp - 0x10], 3
004191D1  lea      edx, [ebp - 8]
004191D4  push     edx
004191D5  push     0x403b88
004191DA  call     0x438eaa
004191DF  add      esp, 0x24
004191E2  mov      ecx, dword ptr [ebp + 8]
004191E5  mov      dword ptr [ecx + 8], ebx
004191E8  mov      eax, dword ptr [ebp + 8]
004191EB  mov      dword ptr [eax + 0xc], esi
004191EE  mov      edx, dword ptr [ebp + 8]
004191F1  xor      ecx, ecx
004191F3  mov      dword ptr [edx + 4], ecx
004191F6  mov      eax, dword ptr [ebp + 8]
004191F9  xor      edx, edx
004191FB  mov      dword ptr [eax + 0x18], edx
004191FE  mov      ecx, dword ptr [ebp + 8]
00419201  push     ecx
00419202  mov      eax, dword ptr [ecx]
00419204  call     dword ptr [eax + 4]
00419207  pop      ecx
00419208  mov      edx, dword ptr [ebp - 0x2c]
0041920B  mov      dword ptr fs:[0], edx
00419212  mov      eax, dword ptr [ebp + 8]
00419215  pop      esi
00419216  pop      ebx
00419217  mov      esp, ebp
00419219  pop      ebp
0041921A  ret      
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
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA

---

*Extracted with recursive CALL following and DATA context*
