# LoadFromINI Function Analysis

**Function Address**: 0x004195CC
**Rank**: #83
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 126

```assembly
004195CC  push     ebp
004195CD  mov      ebp, esp
004195CF  add      esp, -0x44
004195D2  push     ebx
004195D3  push     esi
004195D4  push     edi
004195D5  mov      esi, dword ptr [ebp + 0xc]
004195D8  mov      ebx, dword ptr [ebp + 8]
004195DB  test     esi, esi
004195DD  jl       0x4195e4
004195DF  cmp      esi, dword ptr [ebx + 0x4d]
004195E2  jne      0x4195eb
004195E4  xor      eax, eax
004195E6  jmp      0x419731
004195EB  mov      byte ptr [ebp - 1], 0
004195EF  test     esi, esi
004195F1  jne      0x419601
004195F3  push     ebx
004195F4  mov      edx, dword ptr [ebx]
004195F6  call     dword ptr [edx + 0x14]
004195F9  pop      ecx
004195FA  xor      eax, eax
004195FC  jmp      0x419731
00419601  cmp      esi, 1
00419604  jne      0x419614
00419606  push     ebx
00419607  call     0x419e5d
0041960C  pop      ecx
0041960D  mov      al, 1
0041960F  jmp      0x419731
00419614  lea      edx, [esi - 1]
00419617  mov      dword ptr [ebp - 0x40], edx
0041961A  fild     dword ptr [ebp - 0x40]
0041961D  add      esp, -8
00419620  fstp     qword ptr [esp]
00419623  cmp      dword ptr [ebx + 4], 0
00419627  je       0x419631
00419629  fld      qword ptr [0x419738]
0041962F  jmp      0x419637
00419631  fld      qword ptr [0x419740]
00419637  fadd     dword ptr [0x419748]
0041963D  add      esp, -8
00419640  fstp     qword ptr [esp]
00419643  call     0x438fa0
00419648  add      esp, 0x10
0041964B  fsub     dword ptr [0x419748]
00419651  fmul     dword ptr [0x41974c]
00419657  fstp     qword ptr [ebp - 0xc]
0041965A  mov      dword ptr [ebx + 0x4d], esi
0041965D  lea      ecx, [ebx + 0x2d]
00419660  mov      dword ptr [ebp - 0x14], ecx
00419663  mov      eax, dword ptr [ebp - 0x14]
00419666  mov      edx, dword ptr [eax + 0xc]
00419669  mov      ecx, dword ptr [ebp - 0x14]
0041966C  sub      edx, dword ptr [ecx + 4]
0041966F  mov      dword ptr [ebp - 0x40], edx
00419672  fild     dword ptr [ebp - 0x40]
00419675  fmul     qword ptr [ebp - 0xc]
00419678  call     0x438eda
0041967D  mov      dword ptr [ebp - 0x10], eax
00419680  lea      edx, [ebx + 0x2d]
00419683  mov      dword ptr [ebp - 0x1c], edx
00419686  mov      ecx, dword ptr [ebp - 0x1c]
00419689  mov      eax, dword ptr [ecx + 8]
0041968C  mov      edx, dword ptr [ebp - 0x1c]
0041968F  sub      eax, dword ptr [edx]
00419691  mov      dword ptr [ebp - 0x44], eax
00419694  fild     dword ptr [ebp - 0x44]
00419697  fmul     qword ptr [ebp - 0xc]
0041969A  call     0x438eda
0041969F  mov      dword ptr [ebp - 0x18], eax
004196A2  lea      edi, [ebx + 0x2d]
004196A5  mov      eax, dword ptr [edi + 0xc]
004196A8  add      eax, dword ptr [ebp - 0x10]
004196AB  mov      dword ptr [ebp - 0x20], eax
004196AE  mov      edx, dword ptr [edi + 8]
004196B1  add      edx, dword ptr [ebp - 0x18]
004196B4  mov      dword ptr [ebp - 0x24], edx
004196B7  mov      ecx, dword ptr [edi + 4]
004196BA  sub      ecx, dword ptr [ebp - 0x10]
004196BD  mov      dword ptr [ebp - 0x28], ecx
004196C0  mov      eax, dword ptr [edi]
004196C2  sub      eax, dword ptr [ebp - 0x18]
004196C5  mov      dword ptr [ebp - 0x2c], eax
004196C8  mov      edx, dword ptr [ebp - 0x2c]
004196CB  mov      dword ptr [ebp - 0x3c], edx
004196CE  mov      ecx, dword ptr [ebp - 0x28]
004196D1  mov      dword ptr [ebp - 0x38], ecx
004196D4  mov      eax, dword ptr [ebp - 0x24]
004196D7  mov      dword ptr [ebp - 0x34], eax
004196DA  mov      edx, dword ptr [ebp - 0x20]
004196DD  mov      dword ptr [ebp - 0x30], edx
004196E0  lea      ecx, [ebp - 0x3c]
004196E3  push     ecx
004196E4  push     dword ptr [ebx + 0xc]
004196E7  call     0x41debb
004196EC  add      esp, 8
004196EF  mov      eax, dword ptr [ebx + 0xc]
004196F2  add      eax, 0xd
004196F5  mov      edx, dword ptr [eax + 8]
004196F8  sub      edx, dword ptr [eax]
004196FA  test     edx, edx
004196FC  jle      0x41970e
004196FE  mov      eax, dword ptr [ebx + 0xc]
00419701  add      eax, 0xd
00419704  mov      edx, dword ptr [eax + 0xc]
00419707  sub      edx, dword ptr [eax + 4]
0041970A  test     edx, edx
0041970C  jg       0x419713
0041970E  dec      esi
0041970F  mov      byte ptr [ebp - 1], 1
00419713  cmp      byte ptr [ebp - 1], 0
00419717  je       0x419725
00419719  mov      ecx, dword ptr [ebx + 0x4d]
0041971C  cmp      ecx, dword ptr [ebx + 0x51]
0041971F  ja       0x4195ef
00419725  mov      eax, dword ptr [ebx + 0x4d]
00419728  cmp      eax, dword ptr [ebx + 0x51]
0041972B  setne    al
0041972E  and      eax, 1
00419731  pop      edi
00419732  pop      esi
00419733  pop      ebx
00419734  mov      esp, ebp
00419736  pop      ebp
00419737  ret      
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

- 0x00419E5D
- 0x00438FA0
- 0x00438EDA
- 0x00438EDA
- 0x0041DEBB

---

*Extracted with recursive CALL following and DATA context*
