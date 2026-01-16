# LoadFromINI Function Analysis

**Function Address**: 0x0041A04F
**Rank**: #139
**INI String Count**: 3
**Identified Structure**: TVNImageObject
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 84

```assembly
0041A04F  push     ebp
0041A050  mov      ebp, esp
0041A052  add      esp, -0x2c
0041A055  mov      eax, 0x44320c
0041A05A  call     0x403618
0041A05F  mov      word ptr [ebp - 0x1c], 8
0041A065  push     dword ptr [ebp + 0x10]
0041A068  push     dword ptr [ebp + 0xc]
0041A06B  push     dword ptr [ebp + 8]
0041A06E  call     0x41912a
0041A073  add      esp, 0xc
0041A076  inc      dword ptr [ebp - 0x10]
0041A079  mov      edx, dword ptr [ebp + 8]
0041A07C  mov      dword ptr [edx], 0x443638
0041A082  mov      ecx, dword ptr [ebp + 8]
0041A085  mov      eax, dword ptr [ecx + 0xc]
0041A088  push     eax
0041A089  mov      edx, dword ptr [eax + 5]
0041A08C  call     dword ptr [edx + 4]
0041A08F  pop      ecx
0041A090  test     eax, eax
0041A092  je       0x41a0aa
0041A094  mov      ecx, dword ptr [ebp + 8]
0041A097  mov      eax, dword ptr [ecx + 0xc]
0041A09A  push     eax
0041A09B  mov      edx, dword ptr [eax + 5]
0041A09E  call     dword ptr [edx + 8]
0041A0A1  pop      ecx
0041A0A2  test     eax, eax
0041A0A4  jne      0x41a12f
0041A0AA  lea      ecx, [ebp - 0x2c]
0041A0AD  push     ecx
0041A0AE  push     0
0041A0B0  push     0
0041A0B2  push     0
0041A0B4  push     1
0041A0B6  push     0x40690f
0041A0BB  push     0
0041A0BD  mov      word ptr [ebp - 0x1c], 0x14
0041A0C3  push     0x1bf
0041A0C8  push     0x4435c2
0041A0CD  push     0x4435a0
0041A0D2  push     0x4435cf
0041A0D7  lea      eax, [ebp - 4]
0041A0DA  push     eax
0041A0DB  call     0x438f10
0041A0E0  add      esp, 0x14
0041A0E3  lea      edx, [ebp - 4]
0041A0E6  push     edx
0041A0E7  inc      dword ptr [ebp - 0x10]
0041A0EA  lea      ecx, [ebp - 8]
0041A0ED  push     ecx
0041A0EE  call     0x438de4
0041A0F3  add      esp, 8
0041A0F6  inc      dword ptr [ebp - 0x10]
0041A0F9  mov      word ptr [ebp - 0x1c], 0x20
0041A0FF  dec      dword ptr [ebp - 0x10]
0041A102  push     2
0041A104  lea      eax, [ebp - 4]
0041A107  push     eax
0041A108  call     0x438f64
0041A10D  add      esp, 8
0041A110  mov      word ptr [ebp - 0x1c], 0x14
0041A116  add      dword ptr [ebp - 0x10], 2
0041A11A  add      dword ptr [ebp - 0x10], 3
0041A11E  lea      edx, [ebp - 8]
0041A121  push     edx
0041A122  push     0x4068bf
0041A127  call     0x438eaa
0041A12C  add      esp, 0x24
0041A12F  mov      ecx, dword ptr [ebp + 8]
0041A132  xor      eax, eax
0041A134  mov      dword ptr [ecx + 0x1c], eax
0041A137  mov      edx, dword ptr [ebp + 8]
0041A13A  xor      ecx, ecx
0041A13C  mov      dword ptr [edx + 0x24], ecx
0041A13F  mov      eax, dword ptr [ebp + 8]
0041A142  mov      dword ptr [eax + 0x20], ecx
0041A145  mov      edx, dword ptr [ebp - 0x2c]
0041A148  mov      dword ptr fs:[0], edx
0041A14F  mov      eax, dword ptr [ebp + 8]
0041A152  mov      esp, ebp
0041A154  pop      ebp
0041A155  ret      
```

## Strings Referenced

**Total unique strings**: 6

- `"img && wnd"` @ 0x00443448
- `"timernfx.cpp"` @ 0x00443453
- `"Precondition"` @ 0x00443460
- `"Image->Width() && Image->Height()"` @ 0x004435A0
- `"timernfx.cpp"` @ 0x004435C2
- `"Check"` @ 0x004435CF

## DATA Context

**Context around 0x004435A0**:

- `"window.h"` @ 0x00443520
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
- `"Precondition"` @ 0x0044361C

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

**Context around 0x004435C2**:

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
- `"Precondition"` @ 0x0044361C

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

**Context around 0x004435CF**:

- `"E\owl/window.h"` @ 0x0044354F
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
- `"Precondition"` @ 0x0044361C

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

## Functions Called

- 0x00403618
- 0x0041912A
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA

---

*Extracted with recursive CALL following and DATA context*
