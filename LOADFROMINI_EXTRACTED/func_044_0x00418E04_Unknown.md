# LoadFromINI Function Analysis

**Function Address**: 0x00418E04
**Rank**: #44
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 86

```assembly
00418E04  push     ebp
00418E05  mov      ebp, esp
00418E07  add      esp, -0x34
00418E0A  mov      eax, 0x442e50
00418E0F  call     0x403618
00418E14  mov      word ptr [ebp - 0x1c], 8
00418E1A  mov      edx, dword ptr [ebp + 8]
00418E1D  mov      dword ptr [edx], 0x4436c8
00418E23  mov      ecx, dword ptr [ebp + 8]
00418E26  xor      eax, eax
00418E28  mov      dword ptr [ecx + 4], eax
00418E2B  cmp      dword ptr [ebp + 0xc], 0
00418E2F  ja       0x418eb7
00418E35  lea      edx, [ebp - 0x2c]
00418E38  push     edx
00418E39  push     0
00418E3B  push     0
00418E3D  push     0
00418E3F  push     1
00418E41  push     0x403be0
00418E46  push     0
00418E48  mov      word ptr [ebp - 0x1c], 0x14
00418E4E  push     0x26
00418E50  push     0x4433f3
00418E55  push     0x4433e4
00418E5A  push     0x443400
00418E5F  lea      ecx, [ebp - 4]
00418E62  push     ecx
00418E63  call     0x438f10
00418E68  add      esp, 0x14
00418E6B  lea      eax, [ebp - 4]
00418E6E  push     eax
00418E6F  inc      dword ptr [ebp - 0x10]
00418E72  lea      edx, [ebp - 8]
00418E75  push     edx
00418E76  call     0x438de4
00418E7B  add      esp, 8
00418E7E  inc      dword ptr [ebp - 0x10]
00418E81  mov      word ptr [ebp - 0x1c], 0x20
00418E87  dec      dword ptr [ebp - 0x10]
00418E8A  push     2
00418E8C  lea      ecx, [ebp - 4]
00418E8F  push     ecx
00418E90  call     0x438f64
00418E95  add      esp, 8
00418E98  mov      word ptr [ebp - 0x1c], 0x14
00418E9E  add      dword ptr [ebp - 0x10], 2
00418EA2  add      dword ptr [ebp - 0x10], 3
00418EA6  lea      eax, [ebp - 8]
00418EA9  push     eax
00418EAA  push     0x403b88
00418EAF  call     0x438eaa
00418EB4  add      esp, 0x24
00418EB7  push     8
00418EB9  lea      edx, [ebp - 0x34]
00418EBC  push     edx
00418EBD  call     0x439846
00418EC2  test     eax, eax
00418EC4  jne      0x418eff
00418EC6  mov      ecx, dword ptr [ebp - 0x34]
00418EC9  cmp      ecx, dword ptr [ebp + 0xc]
00418ECC  jbe      0x418ed3
00418ECE  lea      eax, [ebp - 0x34]
00418ED1  jmp      0x418ed6
00418ED3  lea      eax, [ebp + 0xc]
00418ED6  mov      edx, dword ptr [eax]
00418ED8  cmp      edx, dword ptr [ebp - 0x30]
00418EDB  jb       0x418ee0
00418EDD  lea      eax, [ebp - 0x30]
00418EE0  mov      edx, dword ptr [eax]
00418EE2  mov      ecx, dword ptr [ebp + 8]
00418EE5  mov      dword ptr [ecx + 4], edx
00418EE8  mov      eax, dword ptr [ebp + 8]
00418EEB  push     dword ptr [eax + 4]
00418EEE  call     0x439852
00418EF3  test     eax, eax
00418EF5  je       0x418eff
00418EF7  mov      edx, dword ptr [ebp + 8]
00418EFA  xor      ecx, ecx
00418EFC  mov      dword ptr [edx + 4], ecx
00418EFF  mov      eax, dword ptr [ebp - 0x2c]
00418F02  mov      dword ptr fs:[0], eax
00418F08  mov      eax, dword ptr [ebp + 8]
00418F0B  mov      esp, ebp
00418F0D  pop      ebp
00418F0E  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"resolution > 0"` @ 0x004433E4
- `"timernfx.cpp"` @ 0x004433F3
- `"Precondition"` @ 0x00443400

## DATA Context

**Context around 0x00443400**:

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

**Context around 0x004433F3**:

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

**Context around 0x004433E4**:

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

## Functions Called

- 0x00403618
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00439846
- 0x00439852

---

*Extracted with recursive CALL following and DATA context*
