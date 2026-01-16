# LoadFromINI Function Analysis

**Function Address**: 0x00419A6C
**Rank**: #133
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 164

```assembly
00419A6C  push     ebp
00419A6D  mov      ebp, esp
00419A6F  add      esp, -0x58
00419A72  push     ebx
00419A73  push     esi
00419A74  push     edi
00419A75  mov      esi, dword ptr [ebp + 0xc]
00419A78  mov      ebx, dword ptr [ebp + 8]
00419A7B  cmp      dword ptr [ebx + 0x4d], 1
00419A7F  ja       0x419a88
00419A81  xor      eax, eax
00419A83  jmp      0x419c1c
00419A88  mov      eax, dword ptr [ebx + 0xc]
00419A8B  add      eax, 0xd
00419A8E  mov      ecx, dword ptr [eax + 8]
00419A91  sub      ecx, dword ptr [eax]
00419A93  mov      dword ptr [ebp - 0x54], ecx
00419A96  fild     dword ptr [ebp - 0x54]
00419A99  lea      edx, [ebx + 0x3d]
00419A9C  mov      eax, dword ptr [edx + 8]
00419A9F  sub      eax, dword ptr [edx]
00419AA1  mov      dword ptr [ebp - 0x58], eax
00419AA4  fild     dword ptr [ebp - 0x58]
00419AA7  fdivp    st(1)
00419AA9  fstp     qword ptr [ebp - 0x10]
00419AAC  mov      edx, dword ptr [ebx + 0x3d]
00419AAF  sub      edx, dword ptr [esi]
00419AB1  mov      dword ptr [ebp - 0x54], edx
00419AB4  fild     dword ptr [ebp - 0x54]
00419AB7  fmul     qword ptr [ebp - 0x10]
00419ABA  fild     dword ptr [esi]
00419ABC  faddp    st(1)
00419ABE  call     0x438eda
00419AC3  mov      dword ptr [ebp - 8], eax
00419AC6  mov      edx, dword ptr [ebx + 0x41]
00419AC9  sub      edx, dword ptr [esi + 4]
00419ACC  mov      dword ptr [ebp - 0x54], edx
00419ACF  fild     dword ptr [ebp - 0x54]
00419AD2  fmul     qword ptr [ebp - 0x10]
00419AD5  fild     dword ptr [esi + 4]
00419AD8  faddp    st(1)
00419ADA  call     0x438eda
00419ADF  mov      dword ptr [ebp - 4], eax
00419AE2  mov      edx, dword ptr [ebx + 0xc]
00419AE5  mov      ecx, dword ptr [edx + 0xd]
00419AE8  sub      dword ptr [ebp - 8], ecx
00419AEB  mov      eax, dword ptr [ebx + 0xc]
00419AEE  mov      edx, dword ptr [eax + 0x11]
00419AF1  sub      dword ptr [ebp - 4], edx
00419AF4  mov      edx, dword ptr [ebp - 4]
00419AF7  mov      esi, dword ptr [ebp - 8]
00419AFA  mov      eax, dword ptr [ebx + 0xc]
00419AFD  add      eax, 0xd
00419B00  mov      edi, dword ptr [eax + 0xc]
00419B03  add      edi, edx
00419B05  mov      ecx, dword ptr [eax + 8]
00419B08  add      ecx, esi
00419B0A  mov      dword ptr [ebp - 0x14], ecx
00419B0D  add      edx, dword ptr [eax + 4]
00419B10  mov      dword ptr [ebp - 0x18], edx
00419B13  add      esi, dword ptr [eax]
00419B15  mov      dword ptr [ebp - 0x1c], esi
00419B18  mov      eax, dword ptr [ebp - 0x1c]
00419B1B  mov      dword ptr [ebp - 0x40], eax
00419B1E  mov      edx, dword ptr [ebp - 0x18]
00419B21  mov      dword ptr [ebp - 0x3c], edx
00419B24  mov      eax, dword ptr [ebp - 0x14]
00419B27  mov      dword ptr [ebp - 0x38], eax
00419B2A  mov      dword ptr [ebp - 0x34], edi
00419B2D  lea      edx, [ebp - 0x40]
00419B30  push     edx
00419B31  push     dword ptr [ebx + 0xc]
00419B34  call     0x41debb
00419B39  add      esp, 8
00419B3C  mov      eax, dword ptr [ebx + 0xc]
00419B3F  add      eax, 0xd
00419B42  mov      edx, dword ptr [eax + 8]
00419B45  sub      edx, dword ptr [eax]
00419B47  test     edx, edx
00419B49  jle      0x419b5b
00419B4B  mov      eax, dword ptr [ebx + 0xc]
00419B4E  add      eax, 0xd
00419B51  mov      edx, dword ptr [eax + 0xc]
00419B54  sub      edx, dword ptr [eax + 4]
00419B57  test     edx, edx
00419B59  jg       0x419b69
00419B5B  push     ebx
00419B5C  call     0x4194e7
00419B61  pop      ecx
00419B62  xor      eax, eax
00419B64  jmp      0x419c1c
00419B69  xor      eax, eax
00419B6B  xor      edx, edx
00419B6D  mov      ecx, dword ptr [ebx + 0xc]
00419B70  cmp      dword ptr [ecx + 0xd], 0
00419B74  jle      0x419b80
00419B76  mov      eax, dword ptr [ebx + 0xc]
00419B79  mov      eax, dword ptr [eax + 0xd]
00419B7C  neg      eax
00419B7E  jmp      0x419b97
00419B80  mov      ecx, dword ptr [ebx + 0xc]
00419B83  mov      ecx, dword ptr [ecx + 0x15]
00419B86  cmp      ecx, dword ptr [ebx + 0x10]
00419B89  jge      0x419b97
00419B8B  mov      eax, dword ptr [ebx + 0xc]
00419B8E  push     dword ptr [eax + 0x15]
00419B91  mov      eax, dword ptr [ebx + 0x10]
00419B94  pop      ecx
00419B95  sub      eax, ecx
00419B97  mov      ecx, dword ptr [ebx + 0xc]
00419B9A  cmp      dword ptr [ecx + 0x11], 0
00419B9E  jle      0x419baa
00419BA0  mov      edx, dword ptr [ebx + 0xc]
00419BA3  mov      edx, dword ptr [edx + 0x11]
00419BA6  neg      edx
00419BA8  jmp      0x419bc1
00419BAA  mov      ecx, dword ptr [ebx + 0xc]
00419BAD  mov      ecx, dword ptr [ecx + 0x19]
00419BB0  cmp      ecx, dword ptr [ebx + 0x14]
00419BB3  jge      0x419bc1
00419BB5  mov      edx, dword ptr [ebx + 0xc]
00419BB8  push     dword ptr [edx + 0x19]
00419BBB  mov      edx, dword ptr [ebx + 0x14]
00419BBE  pop      ecx
00419BBF  sub      edx, ecx
00419BC1  test     eax, eax
00419BC3  jne      0x419bc9
00419BC5  test     edx, edx
00419BC7  je       0x419c1a
00419BC9  mov      edi, edx
00419BCB  mov      dword ptr [ebp - 0x20], eax
00419BCE  mov      esi, dword ptr [ebx + 0xc]
00419BD1  add      esi, 0xd
00419BD4  mov      eax, dword ptr [esi + 0xc]
00419BD7  add      eax, edi
00419BD9  mov      dword ptr [ebp - 0x24], eax
00419BDC  mov      edx, dword ptr [esi + 8]
00419BDF  add      edx, dword ptr [ebp - 0x20]
00419BE2  mov      dword ptr [ebp - 0x28], edx
00419BE5  add      edi, dword ptr [esi + 4]
00419BE8  mov      dword ptr [ebp - 0x2c], edi
00419BEB  mov      ecx, dword ptr [esi]
00419BED  add      ecx, dword ptr [ebp - 0x20]
00419BF0  mov      dword ptr [ebp - 0x30], ecx
00419BF3  mov      eax, dword ptr [ebp - 0x30]
00419BF6  mov      dword ptr [ebp - 0x50], eax
00419BF9  mov      edx, dword ptr [ebp - 0x2c]
00419BFC  mov      dword ptr [ebp - 0x4c], edx
00419BFF  mov      ecx, dword ptr [ebp - 0x28]
00419C02  mov      dword ptr [ebp - 0x48], ecx
00419C05  mov      eax, dword ptr [ebp - 0x24]
00419C08  mov      dword ptr [ebp - 0x44], eax
00419C0B  lea      edx, [ebp - 0x50]
00419C0E  push     edx
00419C0F  push     dword ptr [ebx + 0xc]
00419C12  call     0x41debb
00419C17  add      esp, 8
00419C1A  mov      al, 1
00419C1C  pop      edi
00419C1D  pop      esi
00419C1E  pop      ebx
00419C1F  mov      esp, ebp
00419C21  pop      ebp
00419C22  ret      
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

- 0x00438EDA
- 0x00438EDA
- 0x0041DEBB
- 0x004194E7
- 0x0041DEBB

---

*Extracted with recursive CALL following and DATA context*
