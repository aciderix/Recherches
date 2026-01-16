# LoadFromINI Function Analysis

**Function Address**: 0x0041372F
**Rank**: #95
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 297

```assembly
0041372F  push     ebp
00413730  mov      ebp, esp
00413732  add      esp, -0x74
00413735  push     ebx
00413736  push     esi
00413737  push     edi
00413738  mov      ebx, dword ptr [ebp + 0xc]
0041373B  lea      edi, [ebp - 0x3c]
0041373E  mov      eax, 0x440ac4
00413743  call     0x403618
00413748  cmp      ebx, dword ptr [ebp + 8]
0041374B  jne      0x41375d
0041374D  mov      edx, dword ptr [edi]
0041374F  mov      dword ptr fs:[0], edx
00413756  mov      eax, edx
00413758  jmp      0x413ae8
0041375D  lea      ecx, [ebx + 4]
00413760  push     ecx
00413761  mov      eax, dword ptr [ebx + 5]
00413764  call     dword ptr [eax + 4]
00413767  pop      ecx
00413768  mov      esi, eax
0041376A  mov      eax, dword ptr [ebp + 8]
0041376D  add      eax, 4
00413770  push     eax
00413771  mov      edx, dword ptr [ebp + 8]
00413774  mov      ecx, dword ptr [edx + 5]
00413777  call     dword ptr [ecx + 4]
0041377A  pop      ecx
0041377B  add      esi, eax
0041377D  inc      esi
0041377E  mov      eax, dword ptr [ebp + 8]
00413781  cmp      esi, dword ptr [eax]
00413783  jge      0x4137a9
00413785  mov      edx, dword ptr [ebp + 8]
00413788  sub      esi, dword ptr [edx]
0041378A  mov      ecx, dword ptr [ebp + 8]
0041378D  add      esi, dword ptr [ecx + 0xd]
00413790  mov      dword ptr [ebp - 0x40], esi
00413793  push     0
00413795  push     dword ptr [ebp - 0x40]
00413798  mov      eax, dword ptr [ebp + 8]
0041379B  add      eax, 4
0041379E  push     eax
0041379F  call     0x406954
004137A4  add      esp, 0xc
004137A7  jmp      0x4137e7
004137A9  mov      edx, dword ptr [ebp + 8]
004137AC  mov      ecx, dword ptr [edx + 0xd]
004137AF  mov      dword ptr [ebp - 0x44], ecx
004137B2  cmp      dword ptr [ebp - 0x44], -1
004137B6  jne      0x4137bf
004137B8  mov      eax, 0x7fffffff
004137BD  jmp      0x4137c7
004137BF  mov      edx, dword ptr [ebp + 8]
004137C2  mov      eax, dword ptr [edx]
004137C4  add      eax, dword ptr [ebp - 0x44]
004137C7  cmp      esi, eax
004137C9  jl       0x4137e7
004137CB  mov      edx, dword ptr [ebp + 8]
004137CE  sub      esi, dword ptr [edx]
004137D0  mov      dword ptr [ebp - 0x48], esi
004137D3  push     0
004137D5  push     dword ptr [ebp - 0x48]
004137D8  mov      ecx, dword ptr [ebp + 8]
004137DB  add      ecx, 4
004137DE  push     ecx
004137DF  call     0x406954
004137E4  add      esp, 0xc
004137E7  mov      eax, ebx
004137E9  add      eax, 4
004137EC  mov      dword ptr [ebp - 0x74], eax
004137EF  push     eax
004137F0  mov      edx, dword ptr [eax + 1]
004137F3  call     dword ptr [edx]
004137F5  pop      ecx
004137F6  xor      ecx, ecx
004137F8  mov      dword ptr [ebp - 0x6c], ecx
004137FB  mov      dword ptr [ebp - 0x70], ecx
004137FE  mov      dword ptr [ebp - 0x68], eax
00413801  jmp      0x413ad4
00413806  push     0x3d
00413808  call     0x438eec
0041380D  pop      ecx
0041380E  mov      dword ptr [ebp - 0x14], eax
00413811  test     eax, eax
00413813  je       0x413ac1
00413819  mov      word ptr [edi + 0x10], 0x14
0041381F  mov      edx, dword ptr [ebp - 0x70]
00413822  cmp      edx, dword ptr [ebp - 0x68]
00413825  jb       0x4138a3
00413827  push     edi
00413828  push     0
0041382A  push     0
0041382C  push     0
0041382E  push     1
00413830  push     0x403be0
00413835  push     0
00413837  push     0x3db
0041383C  push     0x4414e9
00413841  push     0x4414dd
00413846  push     0x44150b
0041384B  lea      eax, [ebp - 4]
0041384E  push     eax
0041384F  call     0x438f10
00413854  add      esp, 0x14
00413857  lea      edx, [ebp - 4]
0041385A  push     edx
0041385B  inc      dword ptr [edi + 0x1c]
0041385E  lea      ecx, [ebp - 8]
00413861  push     ecx
00413862  call     0x438de4
00413867  add      esp, 8
0041386A  inc      dword ptr [edi + 0x1c]
0041386D  mov      word ptr [edi + 0x10], 0x20
00413873  dec      dword ptr [edi + 0x1c]
00413876  push     2
00413878  lea      eax, [ebp - 4]
0041387B  push     eax
0041387C  call     0x438f64
00413881  add      esp, 8
00413884  mov      word ptr [edi + 0x10], 0x14
0041388A  add      dword ptr [edi + 0x1c], 2
0041388E  add      dword ptr [edi + 0x1c], 3
00413892  lea      edx, [ebp - 8]
00413895  push     edx
00413896  push     0x403b88
0041389B  call     0x438eaa
004138A0  add      esp, 0x24
004138A3  mov      ecx, dword ptr [ebp - 0x70]
004138A6  mov      dword ptr [ebp - 0x50], ecx
004138A9  mov      eax, dword ptr [ebp - 0x74]
004138AC  mov      dword ptr [ebp - 0x54], eax
004138AF  mov      edx, dword ptr [ebp - 0x54]
004138B2  cmp      dword ptr [edx + 9], 0
004138B6  jbe      0x4138cc
004138B8  mov      ecx, dword ptr [ebp - 0x54]
004138BB  cmp      dword ptr [ecx + 5], 0
004138BF  je       0x4138cc
004138C1  mov      eax, dword ptr [ebp - 0x54]
004138C4  mov      edx, dword ptr [eax + 9]
004138C7  cmp      edx, dword ptr [ebp - 0x50]
004138CA  ja       0x413948
004138CC  push     edi
004138CD  push     0
004138CF  push     0
004138D1  push     0
004138D3  push     1
004138D5  push     0x403be0
004138DA  push     0
004138DC  push     0x33a
004138E1  push     0x44153c
004138E6  push     0x441518
004138EB  push     0x44155e
004138F0  lea      ecx, [ebp - 0xc]
004138F3  push     ecx
004138F4  call     0x438f10
004138F9  add      esp, 0x14
004138FC  lea      eax, [ebp - 0xc]
004138FF  push     eax
00413900  inc      dword ptr [edi + 0x1c]
00413903  lea      edx, [ebp - 0x10]
00413906  push     edx
00413907  call     0x438de4
0041390C  add      esp, 8
0041390F  inc      dword ptr [edi + 0x1c]
00413912  mov      word ptr [edi + 0x10], 0x2c
00413918  dec      dword ptr [edi + 0x1c]
0041391B  push     2
0041391D  lea      ecx, [ebp - 0xc]
00413920  push     ecx
00413921  call     0x438f64
00413926  add      esp, 8
00413929  mov      word ptr [edi + 0x10], 0x14
0041392F  add      dword ptr [edi + 0x1c], 2
00413933  add      dword ptr [edi + 0x1c], 3
00413937  lea      eax, [ebp - 0x10]
0041393A  push     eax
0041393B  push     0x403b88
00413940  call     0x438eaa
00413945  add      esp, 0x24
00413948  mov      edx, dword ptr [ebp - 0x54]
0041394B  mov      ecx, dword ptr [edx + 5]
0041394E  mov      eax, dword ptr [ebp - 0x50]
00413951  shl      eax, 2
00413954  add      ecx, eax
00413956  mov      edx, dword ptr [ecx]
00413958  mov      dword ptr [ebp - 0x4c], edx
0041395B  inc      dword ptr [ebp - 0x70]
0041395E  mov      ecx, dword ptr [ebp - 0x4c]
00413961  mov      dword ptr [ebp - 0x58], ecx
00413964  mov      eax, dword ptr [ebp - 0x14]
00413967  mov      dword ptr [eax], 0x4402d4
0041396D  inc      dword ptr [edi + 0x1c]
00413970  mov      edx, dword ptr [ebp - 0x14]
00413973  add      edx, 4
00413976  mov      dword ptr [ebp - 0x5c], edx
00413979  mov      ecx, dword ptr [ebp - 0x5c]
0041397C  mov      dword ptr [ecx], 0x4402c0
00413982  inc      dword ptr [edi + 0x1c]
00413985  mov      eax, dword ptr [ebp - 0x14]
00413988  mov      dword ptr [eax], 0x4402e8
0041398E  mov      edx, dword ptr [ebp - 0x14]
00413991  mov      dword ptr [edx + 4], 0x4402f8
00413998  add      dword ptr [edi + 0x1c], 3
0041399C  mov      ecx, dword ptr [ebp - 0x14]
0041399F  mov      dword ptr [ecx], 0x44181c
004139A5  mov      eax, dword ptr [ebp - 0x14]
004139A8  mov      dword ptr [eax + 4], 0x441848
004139AF  mov      ebx, dword ptr [ebp - 0x14]
004139B2  add      ebx, 8
004139B5  xor      eax, eax
004139B7  mov      dword ptr [ebx], eax
004139B9  lea      esi, [ebx + 4]
004139BC  mov      dword ptr [esi + 1], 0x4400e4
004139C3  push     0x18
004139C5  call     0x438e50
004139CA  pop      ecx
004139CB  mov      dword ptr [ebp - 0x18], eax
004139CE  cmp      dword ptr [ebp - 0x18], 0
004139D2  je       0x413a02
004139D4  mov      word ptr [edi + 0x10], 0x38
004139DA  push     0x40f5da
004139DF  push     1
004139E1  push     0x40f53c
004139E6  push     0x211
004139EB  push     1
004139ED  push     0x14
004139EF  push     dword ptr [ebp - 0x18]
004139F2  call     0x4037e0
004139F7  add      esp, 0x1c
004139FA  mov      word ptr [edi + 0x10], 0x14
00413A00  jmp      0x413a05
00413A02  mov      eax, dword ptr [ebp - 0x18]
00413A05  mov      dword ptr [esi + 5], eax
00413A08  mov      dword ptr [esi + 9], 1
00413A0F  inc      dword ptr [edi + 0x1c]
00413A12  mov      dword ptr [esi + 1], 0x440100
00413A19  add      dword ptr [edi + 0x1c], 2
00413A1D  mov      dword ptr [esi + 1], 0x44011c
00413A24  xor      edx, edx
00413A26  mov      dword ptr [esi + 0xd], edx
00413A29  mov      dword ptr [esi + 0x11], 1
00413A30  add      dword ptr [edi + 0x1c], 3
00413A34  add      dword ptr [edi + 0x1c], 4
00413A38  add      dword ptr [edi + 0x1c], 5
00413A3C  add      dword ptr [edi + 0x1c], 6
00413A40  add      dword ptr [edi + 0x1c], 7
00413A44  add      dword ptr [edi + 0x1c], 8
00413A48  lea      ecx, [ebx + 0x19]
00413A4B  mov      dword ptr [ebp - 0x60], ecx
00413A4E  mov      eax, dword ptr [ebp - 0x60]
00413A51  mov      dword ptr [eax], 0x4402d4
00413A57  inc      dword ptr [edi + 0x1c]
00413A5A  mov      edx, dword ptr [ebp - 0x60]
00413A5D  add      edx, 4
00413A60  mov      dword ptr [ebp - 0x64], edx
00413A63  mov      ecx, dword ptr [ebp - 0x64]
00413A66  mov      dword ptr [ecx], 0x4402c0
00413A6C  inc      dword ptr [edi + 0x1c]
00413A6F  mov      eax, dword ptr [ebp - 0x60]
00413A72  mov      dword ptr [eax], 0x4402e8
00413A78  mov      edx, dword ptr [ebp - 0x60]
00413A7B  mov      dword ptr [edx + 4], 0x4402f8
00413A82  add      dword ptr [edi + 0x1c], 3
00413A86  mov      dword ptr [ebx + 0x21], 0x4400a0
00413A8D  mov      dword ptr [ebx + 0x19], 0x4400c0
00413A94  mov      dword ptr [ebx + 0x1d], 0x4400d0
00413A9B  add      dword ptr [edi + 0x1c], 0xc
00413A9F  push     dword ptr [ebp - 0x14]
00413AA2  call     0x411e5c
00413AA7  pop      ecx
00413AA8  push     dword ptr [ebp - 0x58]
00413AAB  push     dword ptr [ebp - 0x14]
00413AAE  call     0x411e9f
00413AB3  add      esp, 8
00413AB6  mov      word ptr [edi + 0x10], 8
00413ABC  mov      eax, dword ptr [ebp - 0x14]
00413ABF  jmp      0x413ac4
00413AC1  mov      eax, dword ptr [ebp - 0x14]
00413AC4  push     eax
00413AC5  mov      edx, dword ptr [ebp + 8]
00413AC8  add      edx, 4
00413ACB  push     edx
00413ACC  call     0x41405c
00413AD1  add      esp, 8
00413AD4  mov      ecx, dword ptr [ebp - 0x70]
00413AD7  cmp      ecx, dword ptr [ebp - 0x68]
00413ADA  jb       0x413806
00413AE0  mov      eax, dword ptr [edi]
00413AE2  mov      dword ptr fs:[0], eax
00413AE8  pop      edi
00413AE9  pop      esi
00413AEA  pop      ebx
00413AEB  mov      esp, ebp
00413AED  pop      ebp
00413AEE  ret      
```

## Strings Referenced

**Total unique strings**: 10

- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"!EA"` @ 0x00441848
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## DATA Context

**Context around 0x0044EB41**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD

**Context around 0x0044EB24**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

**Context around 0x0044EB64**:

- `"tor_delete_"` @ 0x0044EAE4
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD
- `" N?A"` @ 0x0044EBCF
- `" w1B"` @ 0x0044EBDB

**Context around 0x00441848**:

- `">BA"` @ 0x004417F0
- `"FDA"` @ 0x004417F4
- `">BA"` @ 0x0044180C
- `"$#A"` @ 0x00441838
- `"!EA"` @ 0x00441848
- `"%<@"` @ 0x00441850
- `"%<@"` @ 0x00441894

**Context around 0x004414E9**:

- `"%i,%i,%i,%i"` @ 0x00441469
- `" %u %i %i %i %i"` @ 0x00441475
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00441489
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E

**Context around 0x0044150B**:

- `"m == 0 || Data != 0 && index < Lim"` @ 0x0044148B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B

**Context around 0x00441518**:

- `"a != 0 && index < Lim"` @ 0x00441498
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B

**Context around 0x0044153C**:

- `"\classlib/vectimp.h"` @ 0x004414BC
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D

**Context around 0x004414DD**:

- `"_%u"` @ 0x0044145D
- `"0,0,0,0"` @ 0x00441461
- `"%i,%i,%i,%i"` @ 0x00441469
- `" %u %i %i %i %i"` @ 0x00441475
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00441489
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C

**Context around 0x0044155E**:

- `"ur < Upper"` @ 0x004414DE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D
- `"Precondition"` @ 0x004415BE
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004415CB

## Functions Called

- 0x00403618
- 0x00406954
- 0x00406954
- 0x00438EEC
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438E50
- 0x004037E0
- 0x00411E5C
- 0x00411E9F
- 0x0041405C

---

*Extracted with recursive CALL following and DATA context*
