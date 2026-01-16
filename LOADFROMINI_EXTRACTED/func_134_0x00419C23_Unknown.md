# LoadFromINI Function Analysis

**Function Address**: 0x00419C23
**Rank**: #134
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 169

```assembly
00419C23  push     ebp
00419C24  mov      ebp, esp
00419C26  add      esp, -0x34
00419C29  push     ebx
00419C2A  push     esi
00419C2B  push     edi
00419C2C  mov      esi, dword ptr [ebp + 0xc]
00419C2F  mov      edi, dword ptr [ebp + 8]
00419C32  mov      eax, 0x443100
00419C37  call     0x403618
00419C3C  test     esi, esi
00419C3E  je       0x419e16
00419C44  cmp      byte ptr [edi + 0x1c], 0
00419C48  je       0x419c5b
00419C4A  add      esi, dword ptr [edi + 0x4d]
00419C4D  push     esi
00419C4E  push     edi
00419C4F  call     0x4195cc
00419C54  add      esp, 8
00419C57  mov      ebx, eax
00419C59  jmp      0x419c78
00419C5B  cmp      esi, dword ptr [edi + 0x4d]
00419C5E  jbe      0x419c65
00419C60  mov      eax, dword ptr [edi + 0x4d]
00419C63  jmp      0x419c67
00419C65  mov      eax, esi
00419C67  mov      edx, dword ptr [edi + 0x4d]
00419C6A  sub      edx, eax
00419C6C  push     edx
00419C6D  push     edi
00419C6E  call     0x4195cc
00419C73  add      esp, 8
00419C76  mov      ebx, eax
00419C78  test     bl, bl
00419C7A  je       0x419e16
00419C80  cmp      dword ptr [edi + 0x4d], 1
00419C84  jbe      0x419d4c
00419C8A  cmp      dword ptr [ebp + 0x10], 0
00419C8E  je       0x419dea
00419C94  push     dword ptr [ebp + 0x10]
00419C97  push     edi
00419C98  call     0x419a6c
00419C9D  add      esp, 8
00419CA0  test     al, al
00419CA2  je       0x419d3b
00419CA8  mov      esi, dword ptr [edi + 8]
00419CAB  cmp      dword ptr [esi + 0xc], 0
00419CAF  jne      0x419d2a
00419CB1  lea      eax, [ebp - 0x34]
00419CB4  push     eax
00419CB5  push     0
00419CB7  push     0
00419CB9  push     0
00419CBB  push     1
00419CBD  push     0x403be0
00419CC2  push     0
00419CC4  push     0x769
00419CC9  push     0x4434d8
00419CCE  push     0x4434cc
00419CD3  push     0x4434f4
00419CD8  lea      edx, [ebp - 4]
00419CDB  push     edx
00419CDC  call     0x438f10
00419CE1  add      esp, 0x14
00419CE4  lea      ecx, [ebp - 4]
00419CE7  push     ecx
00419CE8  inc      dword ptr [ebp - 0x18]
00419CEB  lea      eax, [ebp - 8]
00419CEE  push     eax
00419CEF  call     0x438de4
00419CF4  add      esp, 8
00419CF7  inc      dword ptr [ebp - 0x18]
00419CFA  mov      word ptr [ebp - 0x24], 0xc
00419D00  dec      dword ptr [ebp - 0x18]
00419D03  push     2
00419D05  lea      edx, [ebp - 4]
00419D08  push     edx
00419D09  call     0x438f64
00419D0E  add      esp, 8
00419D11  add      dword ptr [ebp - 0x18], 2
00419D15  add      dword ptr [ebp - 0x18], 3
00419D19  lea      ecx, [ebp - 8]
00419D1C  push     ecx
00419D1D  push     0x403b88
00419D22  call     0x438eaa
00419D27  add      esp, 0x24
00419D2A  push     0
00419D2C  push     0
00419D2E  push     dword ptr [esi + 0xc]
00419D31  call     0x4391f2
00419D36  jmp      0x419dea
00419D3B  xor      eax, eax
00419D3D  mov      edx, dword ptr [ebp - 0x34]
00419D40  mov      dword ptr fs:[0], edx
00419D47  jmp      0x419e22
00419D4C  mov      esi, dword ptr [edi + 8]
00419D4F  cmp      dword ptr [esi + 0xc], 0
00419D53  jne      0x419dde
00419D59  lea      eax, [ebp - 0x34]
00419D5C  push     eax
00419D5D  push     0
00419D5F  push     0
00419D61  push     0
00419D63  push     1
00419D65  push     0x403be0
00419D6A  push     0
00419D6C  mov      word ptr [ebp - 0x24], 0x18
00419D72  push     0x769
00419D77  push     0x44350d
00419D7C  push     0x443501
00419D81  push     0x443529
00419D86  lea      edx, [ebp - 0xc]
00419D89  push     edx
00419D8A  call     0x438f10
00419D8F  add      esp, 0x14
00419D92  lea      ecx, [ebp - 0xc]
00419D95  push     ecx
00419D96  inc      dword ptr [ebp - 0x18]
00419D99  lea      eax, [ebp - 0x10]
00419D9C  push     eax
00419D9D  call     0x438de4
00419DA2  add      esp, 8
00419DA5  inc      dword ptr [ebp - 0x18]
00419DA8  mov      word ptr [ebp - 0x24], 0x24
00419DAE  dec      dword ptr [ebp - 0x18]
00419DB1  push     2
00419DB3  lea      edx, [ebp - 0xc]
00419DB6  push     edx
00419DB7  call     0x438f64
00419DBC  add      esp, 8
00419DBF  mov      word ptr [ebp - 0x24], 0x18
00419DC5  add      dword ptr [ebp - 0x18], 2
00419DC9  add      dword ptr [ebp - 0x18], 3
00419DCD  lea      ecx, [ebp - 0x10]
00419DD0  push     ecx
00419DD1  push     0x403b88
00419DD6  call     0x438eaa
00419DDB  add      esp, 0x24
00419DDE  push     0
00419DE0  push     0
00419DE2  push     dword ptr [esi + 0xc]
00419DE5  call     0x4391f2
00419DEA  cmp      dword ptr [edi + 0x4d], 0
00419DEE  jbe      0x419e16
00419DF0  cmp      dword ptr [edi + 4], 0
00419DF4  je       0x419e16
00419DF6  cmp      dword ptr [edi + 4], 0
00419DFA  je       0x419e0b
00419DFC  mov      eax, dword ptr [edi + 4]
00419DFF  push     eax
00419E00  mov      edx, dword ptr [eax + 0x14]
00419E03  call     dword ptr [edx + 4]
00419E06  pop      ecx
00419E07  test     al, al
00419E09  jne      0x419e16
00419E0B  mov      ecx, dword ptr [edi + 4]
00419E0E  push     ecx
00419E0F  mov      eax, dword ptr [ecx + 0x14]
00419E12  call     dword ptr [eax + 0xc]
00419E15  pop      ecx
00419E16  mov      eax, ebx
00419E18  mov      edx, dword ptr [ebp - 0x34]
00419E1B  mov      dword ptr fs:[0], edx
00419E22  pop      edi
00419E23  pop      esi
00419E24  pop      ebx
00419E25  mov      esp, ebp
00419E27  pop      ebp
00419E28  ret      
```

## Strings Referenced

**Total unique strings**: 12

- `"GetHandle()"` @ 0x0044346D
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443479
- `"Precondition"` @ 0x00443495
- `"GetHandle()"` @ 0x004434CC
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x004434D8
- `"Precondition"` @ 0x004434F4
- `"GetHandle()"` @ 0x00443501
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044350D
- `"Precondition"` @ 0x00443529
- `"GetHandle()"` @ 0x00443536
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443542
- `"Precondition"` @ 0x0044355E

## DATA Context

**Context around 0x00443501**:

- `"NCLUDE\owl/window.h"` @ 0x00443481
- `"Precondition"` @ 0x00443495
- `"Image && Window"` @ 0x004434A2
- `"timernfx.cpp"` @ 0x004434B2
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

**Context around 0x00443529**:

- `"& Window"` @ 0x004434A9
- `"timernfx.cpp"` @ 0x004434B2
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

**Context around 0x004434CC**:

- `"&& wnd"` @ 0x0044344C
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
- `"Precondition"` @ 0x00443529
- `"GetHandle()"` @ 0x00443536
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443542

**Context around 0x0044350D**:

- `"indow.h"` @ 0x0044348D
- `"Precondition"` @ 0x00443495
- `"Image && Window"` @ 0x004434A2
- `"timernfx.cpp"` @ 0x004434B2
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

**Context around 0x004434F4**:

- `"le()"` @ 0x00443474
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
- `"Precondition"` @ 0x00443529
- `"GetHandle()"` @ 0x00443536
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443542
- `"Precondition"` @ 0x0044355E
- `"GetHandle()"` @ 0x0044356B

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

**Context around 0x004434D8**:

- `"nfx.cpp"` @ 0x00443458
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
- `"Precondition"` @ 0x00443529
- `"GetHandle()"` @ 0x00443536
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00443542

## Functions Called

- 0x00403618
- 0x004195CC
- 0x004195CC
- 0x00419A6C
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x004391F2
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x004391F2

---

*Extracted with recursive CALL following and DATA context*
