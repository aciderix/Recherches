# LoadFromINI Function Analysis

**Function Address**: 0x004135B0
**Rank**: #69
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 138

```assembly
004135B0  push     ebp
004135B1  mov      ebp, esp
004135B3  add      esp, -0x44
004135B6  push     ebx
004135B7  push     esi
004135B8  push     edi
004135B9  mov      ebx, dword ptr [ebp + 8]
004135BC  mov      eax, 0x440a00
004135C1  call     0x403618
004135C6  push     ebx
004135C7  mov      edx, dword ptr [ebx + 0x25]
004135CA  call     dword ptr [edx + 8]
004135CD  pop      ecx
004135CE  mov      dword ptr [ebp - 0x30], eax
004135D1  jmp      0x4136e6
004135D6  mov      ecx, dword ptr [ebp - 0x30]
004135D9  mov      dword ptr [ebp - 0x34], ecx
004135DC  mov      esi, dword ptr [ebp - 0x34]
004135DF  inc      esi
004135E0  cmp      esi, dword ptr [ebx]
004135E2  jge      0x413601
004135E4  mov      eax, esi
004135E6  sub      eax, dword ptr [ebx]
004135E8  add      eax, dword ptr [ebx + 0xd]
004135EB  mov      dword ptr [ebp - 0x38], eax
004135EE  push     0
004135F0  push     dword ptr [ebp - 0x38]
004135F3  lea      edx, [ebx + 4]
004135F6  push     edx
004135F7  call     0x406954
004135FC  add      esp, 0xc
004135FF  jmp      0x413633
00413601  mov      ecx, dword ptr [ebx + 0xd]
00413604  mov      dword ptr [ebp - 0x3c], ecx
00413607  cmp      dword ptr [ebp - 0x3c], -1
0041360B  jne      0x413614
0041360D  mov      eax, 0x7fffffff
00413612  jmp      0x413619
00413614  mov      eax, dword ptr [ebp - 0x3c]
00413617  add      eax, dword ptr [ebx]
00413619  cmp      esi, eax
0041361B  jl       0x413633
0041361D  sub      esi, dword ptr [ebx]
0041361F  mov      dword ptr [ebp - 0x40], esi
00413622  push     0
00413624  push     dword ptr [ebp - 0x40]
00413627  lea      edx, [ebx + 4]
0041362A  push     edx
0041362B  call     0x406954
00413630  add      esp, 0xc
00413633  mov      ecx, dword ptr [ebp - 0x34]
00413636  sub      ecx, dword ptr [ebx]
00413638  mov      dword ptr [ebp - 0x44], ecx
0041363B  lea      edi, [ebx + 4]
0041363E  cmp      dword ptr [edi + 9], 0
00413642  je       0x4136cf
00413648  cmp      dword ptr [edi + 5], 0
0041364C  je       0x413656
0041364E  mov      eax, dword ptr [edi + 9]
00413651  cmp      eax, dword ptr [ebp - 0x44]
00413654  ja       0x4136cf
00413656  lea      edx, [ebp - 0x2c]
00413659  push     edx
0041365A  push     0
0041365C  push     0
0041365E  push     0
00413660  push     1
00413662  push     0x403be0
00413667  push     0
00413669  push     0x334
0041366E  push     0x4414ae
00413673  push     0x441489
00413678  push     0x4414d0
0041367D  lea      ecx, [ebp - 4]
00413680  push     ecx
00413681  call     0x438f10
00413686  add      esp, 0x14
00413689  lea      eax, [ebp - 4]
0041368C  push     eax
0041368D  inc      dword ptr [ebp - 0x10]
00413690  lea      edx, [ebp - 8]
00413693  push     edx
00413694  call     0x438de4
00413699  add      esp, 8
0041369C  inc      dword ptr [ebp - 0x10]
0041369F  mov      word ptr [ebp - 0x1c], 0xc
004136A5  dec      dword ptr [ebp - 0x10]
004136A8  push     2
004136AA  lea      ecx, [ebp - 4]
004136AD  push     ecx
004136AE  call     0x438f64
004136B3  add      esp, 8
004136B6  add      dword ptr [ebp - 0x10], 2
004136BA  add      dword ptr [ebp - 0x10], 3
004136BE  lea      eax, [ebp - 8]
004136C1  push     eax
004136C2  push     0x403b88
004136C7  call     0x438eaa
004136CC  add      esp, 0x24
004136CF  mov      eax, dword ptr [edi + 5]
004136D2  mov      edx, dword ptr [ebp - 0x44]
004136D5  shl      edx, 2
004136D8  add      eax, edx
004136DA  mov      ecx, dword ptr [eax]
004136DC  push     ecx
004136DD  mov      eax, dword ptr [ecx]
004136DF  call     dword ptr [eax + 0xc]
004136E2  pop      ecx
004136E3  inc      dword ptr [ebp - 0x30]
004136E6  push     ebx
004136E7  mov      edx, dword ptr [ebx + 0x25]
004136EA  call     dword ptr [edx + 0xc]
004136ED  pop      ecx
004136EE  cmp      eax, dword ptr [ebp - 0x30]
004136F1  jge      0x4135d6
004136F7  jmp      0x413703
004136F9  cmp      dword ptr [ebx + 0x19], 2
004136FD  je       0x413703
004136FF  xor      eax, eax
00413701  jmp      0x413708
00413703  mov      eax, 1
00413708  add      ebx, 4
0041370B  push     0
0041370D  push     -1
0041370F  push     eax
00413710  push     ebx
00413711  call     0x4141b5
00413716  add      esp, 0x10
00413719  xor      eax, eax
0041371B  mov      dword ptr [ebx + 0xd], eax
0041371E  mov      edx, dword ptr [ebp - 0x2c]
00413721  mov      dword ptr fs:[0], edx
00413728  pop      edi
00413729  pop      esi
0041372A  pop      ebx
0041372B  mov      esp, ebp
0041372D  pop      ebp
0041372E  ret      
```

## Strings Referenced

**Total unique strings**: 6

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00441489
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
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

**Context around 0x00441489**:

- `"ot.cpp"` @ 0x00441409
- `"Check"` @ 0x00441410
- `"ptr != NULL"` @ 0x00441418
- `"hotspot.cpp"` @ 0x00441424
- `"Check"` @ 0x00441430
- `"HSVIDEO_%u"` @ 0x00441436
- `"HSVIDEOFLAGS_%u"` @ 0x00441442
- `"HSVIDEORECT_%u"` @ 0x00441452
- `"0,0,0,0"` @ 0x00441461
- `"%i,%i,%i,%i"` @ 0x00441469
- `" %u %i %i %i %i"` @ 0x00441475
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00441489
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414AE
- `"Precondition"` @ 0x004414D0
- `"Cur < Upper"` @ 0x004414DD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414E9

**Context around 0x004414AE**:

- `"Check"` @ 0x00441430
- `"HSVIDEO_%u"` @ 0x00441436
- `"HSVIDEOFLAGS_%u"` @ 0x00441442
- `"HSVIDEORECT_%u"` @ 0x00441452
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

**Context around 0x004414D0**:

- `"HSVIDEORECT_%u"` @ 0x00441452
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

## Functions Called

- 0x00403618
- 0x00406954
- 0x00406954
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x004141B5

---

*Extracted with recursive CALL following and DATA context*
