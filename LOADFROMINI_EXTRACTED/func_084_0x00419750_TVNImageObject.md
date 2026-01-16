# LoadFromINI Function Analysis

**Function Address**: 0x00419750
**Rank**: #84
**INI String Count**: 5
**Identified Structure**: TVNImageObject
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 252

```assembly
00419750  push     ebp
00419751  mov      ebp, esp
00419753  add      esp, 0xffffff58
00419759  push     ebx
0041975A  push     esi
0041975B  push     edi
0041975C  mov      esi, dword ptr [ebp + 0x10]
0041975F  mov      ebx, dword ptr [ebp + 8]
00419762  mov      eax, 0x443070
00419767  call     0x403618
0041976C  cmp      dword ptr [ebx + 0xc], 0
00419770  je       0x41977c
00419772  cmp      dword ptr [ebx + 8], 0
00419776  jne      0x419801
0041977C  lea      edx, [ebp - 0x50]
0041977F  push     edx
00419780  push     0
00419782  push     0
00419784  push     0
00419786  push     1
00419788  push     0x403be0
0041978D  push     0
0041978F  mov      word ptr [ebp - 0x40], 8
00419795  push     0x11c
0041979A  push     0x4434b2
0041979F  push     0x4434a2
004197A4  push     0x4434bf
004197A9  lea      ecx, [ebp - 4]
004197AC  push     ecx
004197AD  call     0x438f10
004197B2  add      esp, 0x14
004197B5  lea      eax, [ebp - 4]
004197B8  push     eax
004197B9  inc      dword ptr [ebp - 0x34]
004197BC  lea      edx, [ebp - 8]
004197BF  push     edx
004197C0  call     0x438de4
004197C5  add      esp, 8
004197C8  inc      dword ptr [ebp - 0x34]
004197CB  mov      word ptr [ebp - 0x40], 0x14
004197D1  dec      dword ptr [ebp - 0x34]
004197D4  push     2
004197D6  lea      ecx, [ebp - 4]
004197D9  push     ecx
004197DA  call     0x438f64
004197DF  add      esp, 8
004197E2  mov      word ptr [ebp - 0x40], 8
004197E8  add      dword ptr [ebp - 0x34], 2
004197EC  add      dword ptr [ebp - 0x34], 3
004197F0  lea      eax, [ebp - 8]
004197F3  push     eax
004197F4  push     0x403b88
004197F9  call     0x438eaa
004197FE  add      esp, 0x24
00419801  cmp      dword ptr [ebx + 0x4d], 0
00419805  je       0x419a5b
0041980B  mov      eax, esi
0041980D  mov      edx, dword ptr [ebx + 0xc]
00419810  add      edx, 0xd
00419813  mov      ecx, dword ptr [eax + 8]
00419816  cmp      ecx, dword ptr [edx]
00419818  jle      0x419831
0041981A  mov      ecx, dword ptr [eax]
0041981C  cmp      ecx, dword ptr [edx + 8]
0041981F  jge      0x419831
00419821  mov      ecx, dword ptr [eax + 0xc]
00419824  cmp      ecx, dword ptr [edx + 4]
00419827  jle      0x419831
00419829  mov      eax, dword ptr [eax + 4]
0041982C  cmp      eax, dword ptr [edx + 0xc]
0041982F  jl       0x419835
00419831  xor      edx, edx
00419833  jmp      0x41983a
00419835  mov      edx, 1
0041983A  mov      byte ptr [ebp - 0x51], dl
0041983D  test     dl, dl
0041983F  je       0x419a5b
00419845  mov      eax, esi
00419847  mov      edx, dword ptr [ebx + 0xc]
0041984A  add      edx, 0xd
0041984D  mov      ecx, dword ptr [edx]
0041984F  cmp      ecx, dword ptr [eax + 8]
00419852  jge      0x41986b
00419854  mov      ecx, dword ptr [edx + 8]
00419857  cmp      ecx, dword ptr [eax]
00419859  jle      0x41986b
0041985B  mov      ecx, dword ptr [edx + 4]
0041985E  cmp      ecx, dword ptr [eax + 0xc]
00419861  jge      0x41986b
00419863  mov      ecx, dword ptr [edx + 0xc]
00419866  cmp      ecx, dword ptr [eax + 4]
00419869  jg       0x41986f
0041986B  xor      ecx, ecx
0041986D  jmp      0x419874
0041986F  mov      ecx, 1
00419874  mov      byte ptr [ebp - 0x52], cl
00419877  test     cl, cl
00419879  je       0x419926
0041987F  lea      esi, [eax + 0xc]
00419882  lea      ecx, [edx + 0xc]
00419885  mov      dword ptr [ebp - 0x58], ecx
00419888  mov      ecx, dword ptr [ebp - 0x58]
0041988B  mov      ecx, dword ptr [ecx]
0041988D  cmp      ecx, dword ptr [esi]
0041988F  jge      0x419898
00419891  mov      ecx, dword ptr [ebp - 0x58]
00419894  mov      ecx, dword ptr [ecx]
00419896  jmp      0x41989a
00419898  mov      ecx, dword ptr [esi]
0041989A  mov      dword ptr [ebp - 0x5c], ecx
0041989D  lea      ecx, [eax + 8]
004198A0  mov      dword ptr [ebp - 0x60], ecx
004198A3  lea      ecx, [edx + 8]
004198A6  mov      dword ptr [ebp - 0x64], ecx
004198A9  mov      ecx, dword ptr [ebp - 0x64]
004198AC  mov      ecx, dword ptr [ecx]
004198AE  mov      esi, dword ptr [ebp - 0x60]
004198B1  cmp      ecx, dword ptr [esi]
004198B3  jge      0x4198bc
004198B5  mov      ecx, dword ptr [ebp - 0x64]
004198B8  mov      ecx, dword ptr [ecx]
004198BA  jmp      0x4198c1
004198BC  mov      ecx, dword ptr [ebp - 0x60]
004198BF  mov      ecx, dword ptr [ecx]
004198C1  mov      dword ptr [ebp - 0x68], ecx
004198C4  lea      ecx, [eax + 4]
004198C7  mov      dword ptr [ebp - 0x6c], ecx
004198CA  lea      ecx, [edx + 4]
004198CD  mov      dword ptr [ebp - 0x70], ecx
004198D0  mov      ecx, dword ptr [ebp - 0x70]
004198D3  mov      ecx, dword ptr [ecx]
004198D5  mov      esi, dword ptr [ebp - 0x6c]
004198D8  cmp      ecx, dword ptr [esi]
004198DA  jle      0x4198e3
004198DC  mov      ecx, dword ptr [ebp - 0x70]
004198DF  mov      ecx, dword ptr [ecx]
004198E1  jmp      0x4198e8
004198E3  mov      ecx, dword ptr [ebp - 0x6c]
004198E6  mov      ecx, dword ptr [ecx]
004198E8  mov      dword ptr [ebp - 0x74], ecx
004198EB  mov      ecx, dword ptr [edx]
004198ED  cmp      ecx, dword ptr [eax]
004198EF  jle      0x4198f5
004198F1  mov      edx, dword ptr [edx]
004198F3  jmp      0x4198f7
004198F5  mov      edx, dword ptr [eax]
004198F7  mov      dword ptr [ebp - 0x78], edx
004198FA  mov      eax, dword ptr [ebp - 0x78]
004198FD  mov      dword ptr [ebp - 0x98], eax
00419903  mov      ecx, dword ptr [ebp - 0x74]
00419906  mov      dword ptr [ebp - 0x94], ecx
0041990C  mov      eax, dword ptr [ebp - 0x68]
0041990F  mov      dword ptr [ebp - 0x90], eax
00419915  mov      edx, dword ptr [ebp - 0x5c]
00419918  mov      dword ptr [ebp - 0x8c], edx
0041991E  lea      ecx, [ebp - 0x98]
00419924  jmp      0x41994c
00419926  xor      eax, eax
00419928  mov      dword ptr [ebp - 0x98], eax
0041992E  xor      edx, edx
00419930  mov      dword ptr [ebp - 0x94], edx
00419936  xor      ecx, ecx
00419938  mov      dword ptr [ebp - 0x90], ecx
0041993E  xor      eax, eax
00419940  mov      dword ptr [ebp - 0x8c], eax
00419946  lea      ecx, [ebp - 0x98]
0041994C  lea      esi, [ebp - 0x98]
00419952  lea      edi, [ebp - 0x88]
00419958  mov      ecx, 4
0041995D  rep movsd dword ptr es:[edi], dword ptr [esi]
0041995F  lea      esi, [ebp - 0x88]
00419965  lea      edi, [ebp - 0xa8]
0041996B  mov      ecx, 4
00419970  rep movsd dword ptr es:[edi], dword ptr [esi]
00419972  mov      eax, dword ptr [ebx + 0xc]
00419975  add      eax, 0xd
00419978  push     eax
00419979  mov      edx, dword ptr [ebx + 0xc]
0041997C  push     dword ptr [edx + 0x21]
0041997F  push     dword ptr [edx + 0x1d]
00419982  lea      eax, [ebp - 0xa8]
00419988  push     eax
00419989  call     0x405065
0041998E  add      esp, 0x10
00419991  mov      word ptr [ebp - 0x40], 0x20
00419997  push     dword ptr [ebp + 0xc]
0041999A  lea      edx, [ebp - 0x2c]
0041999D  push     edx
0041999E  call     0x439798
004199A3  add      esp, 8
004199A6  add      dword ptr [ebp - 0x34], 3
004199AA  mov      word ptr [ebp - 0x40], 0x2c
004199B0  push     dword ptr [ebx + 0xc]
004199B3  lea      ecx, [ebp - 0x2c]
004199B6  push     ecx
004199B7  call     0x43977a
004199BC  add      esp, 8
004199BF  push     0xcc0020
004199C4  mov      eax, dword ptr [ebp - 0x9c]
004199CA  sub      eax, dword ptr [ebp - 0xa4]
004199D0  push     eax
004199D1  mov      edx, dword ptr [ebp - 0xa0]
004199D7  sub      edx, dword ptr [ebp - 0xa8]
004199DD  push     edx
004199DE  push     dword ptr [ebp - 0xa4]
004199E4  push     dword ptr [ebp - 0xa8]
004199EA  push     dword ptr [ebp - 0x2c]
004199ED  mov      ecx, dword ptr [ebp - 0x7c]
004199F0  sub      ecx, dword ptr [ebp - 0x84]
004199F6  push     ecx
004199F7  mov      eax, dword ptr [ebp - 0x80]
004199FA  sub      eax, dword ptr [ebp - 0x88]
00419A00  push     eax
00419A01  push     dword ptr [ebp - 0x84]
00419A07  push     dword ptr [ebp - 0x88]
00419A0D  mov      edx, dword ptr [ebp + 0xc]
00419A10  push     dword ptr [edx]
00419A12  call     0x4397b0
00419A17  test     eax, eax
00419A19  setne    cl
00419A1C  and      ecx, 1
00419A1F  test     cl, cl
00419A21  je       0x419a3b
00419A23  mov      eax, dword ptr [ebx + 0x4d]
00419A26  mov      dword ptr [ebx + 0x51], eax
00419A29  mov      edx, dword ptr [ebx + 0xc]
00419A2C  lea      esi, [edx + 0xd]
00419A2F  lea      edi, [ebx + 0x3d]
00419A32  mov      ecx, 4
00419A37  rep movsd dword ptr es:[edi], dword ptr [esi]
00419A39  jmp      0x419a49
00419A3B  push     ebx
00419A3C  mov      eax, dword ptr [ebx]
00419A3E  call     dword ptr [eax + 0x10]
00419A41  pop      ecx
00419A42  push     ebx
00419A43  call     0x4194e7
00419A48  pop      ecx
00419A49  sub      dword ptr [ebp - 0x34], 3
00419A4D  push     2
00419A4F  lea      edx, [ebp - 0x2c]
00419A52  push     edx
00419A53  call     0x43978c
00419A58  add      esp, 8
00419A5B  mov      ecx, dword ptr [ebp - 0x50]
00419A5E  mov      dword ptr fs:[0], ecx
00419A65  pop      edi
00419A66  pop      esi
00419A67  pop      ebx
00419A68  mov      esp, ebp
00419A6A  pop      ebp
00419A6B  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"Image && Window"` @ 0x004434A2
- `"timernfx.cpp"` @ 0x004434B2
- `"Precondition"` @ 0x004434BF

## DATA Context

**Context around 0x004434A2**:

- `"a.TimeProc != NULL"` @ 0x00443422
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

**Context around 0x004434B2**:

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
- `"Precondition"` @ 0x00443529

**Context around 0x004434BF**:

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
- `"Precondition"` @ 0x00443529
- `"GetHandle()"` @ 0x00443536

## Functions Called

- 0x00403618
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00405065
- 0x00439798
- 0x0043977A
- 0x004397B0
- 0x004194E7
- 0x0043978C

---

*Extracted with recursive CALL following and DATA context*
