# LoadFromINI Function Analysis

**Function Address**: 0x00411F15
**Rank**: #6
**INI String Count**: 14
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 164

```assembly
00411F15  push     ebp
00411F16  mov      ebp, esp
00411F18  add      esp, -0x4c
00411F1B  push     ebx
00411F1C  push     esi
00411F1D  push     edi
00411F1E  mov      ebx, dword ptr [ebp + 0xc]
00411F21  mov      esi, dword ptr [ebp + 8]
00411F24  mov      eax, 0x440558
00411F29  call     0x403618
00411F2E  push     dword ptr [esi + 0x39]
00411F31  call     0x438f82
00411F36  pop      ecx
00411F37  lea      edx, [ebx + 4]
00411F3A  push     edx
00411F3B  mov      ecx, dword ptr [ebx + 5]
00411F3E  call     dword ptr [ecx + 4]
00411F41  pop      ecx
00411F42  mov      edi, eax
00411F44  cmp      edi, 1
00411F47  jbe      0x4120d9
00411F4D  mov      dword ptr [esi + 0x35], edi
00411F50  push     0
00411F52  push     0
00411F54  push     0x413fc9
00411F59  push     1
00411F5B  push     edi
00411F5C  push     8
00411F5E  push     0
00411F60  call     0x4037e0
00411F65  add      esp, 0x1c
00411F68  mov      dword ptr [esi + 0x39], eax
00411F6B  xor      eax, eax
00411F6D  mov      dword ptr [ebp - 0x38], eax
00411F70  mov      eax, ebx
00411F72  add      eax, 4
00411F75  mov      dword ptr [ebp - 0x4c], eax
00411F78  push     eax
00411F79  mov      edx, dword ptr [eax + 1]
00411F7C  call     dword ptr [edx]
00411F7E  pop      ecx
00411F7F  xor      ecx, ecx
00411F81  mov      dword ptr [ebp - 0x44], ecx
00411F84  mov      dword ptr [ebp - 0x48], ecx
00411F87  mov      dword ptr [ebp - 0x40], eax
00411F8A  jmp      0x4120c4
00411F8F  mov      eax, dword ptr [ebp - 0x48]
00411F92  cmp      eax, dword ptr [ebp - 0x40]
00411F95  jb       0x412010
00411F97  lea      edx, [ebp - 0x34]
00411F9A  push     edx
00411F9B  push     0
00411F9D  push     0
00411F9F  push     0
00411FA1  push     1
00411FA3  push     0x403be0
00411FA8  push     0
00411FAA  push     0x13f
00411FAF  push     0x44126a
00411FB4  push     0x44125e
00411FB9  push     0x44128c
00411FBE  lea      eax, [ebp - 4]
00411FC1  push     eax
00411FC2  call     0x438f10
00411FC7  add      esp, 0x14
00411FCA  lea      edx, [ebp - 4]
00411FCD  push     edx
00411FCE  inc      dword ptr [ebp - 0x18]
00411FD1  lea      ecx, [ebp - 8]
00411FD4  push     ecx
00411FD5  call     0x438de4
00411FDA  add      esp, 8
00411FDD  inc      dword ptr [ebp - 0x18]
00411FE0  mov      word ptr [ebp - 0x24], 0xc
00411FE6  dec      dword ptr [ebp - 0x18]
00411FE9  push     2
00411FEB  lea      eax, [ebp - 4]
00411FEE  push     eax
00411FEF  call     0x438f64
00411FF4  add      esp, 8
00411FF7  add      dword ptr [ebp - 0x18], 2
00411FFB  add      dword ptr [ebp - 0x18], 3
00411FFF  lea      edx, [ebp - 8]
00412002  push     edx
00412003  push     0x403b88
00412008  call     0x438eaa
0041200D  add      esp, 0x24
00412010  mov      edi, dword ptr [ebp - 0x48]
00412013  mov      ebx, dword ptr [ebp - 0x4c]
00412016  cmp      dword ptr [ebx + 9], 0
0041201A  jbe      0x412027
0041201C  cmp      dword ptr [ebx + 5], 0
00412020  je       0x412027
00412022  cmp      edi, dword ptr [ebx + 9]
00412025  jb       0x4120a0
00412027  lea      ecx, [ebp - 0x34]
0041202A  push     ecx
0041202B  push     0
0041202D  push     0
0041202F  push     0
00412031  push     1
00412033  push     0x403be0
00412038  push     0
0041203A  push     0xc7
0041203F  push     0x4412bd
00412044  push     0x441299
00412049  push     0x4412df
0041204E  lea      eax, [ebp - 0xc]
00412051  push     eax
00412052  call     0x438f10
00412057  add      esp, 0x14
0041205A  lea      edx, [ebp - 0xc]
0041205D  push     edx
0041205E  inc      dword ptr [ebp - 0x18]
00412061  lea      ecx, [ebp - 0x10]
00412064  push     ecx
00412065  call     0x438de4
0041206A  add      esp, 8
0041206D  inc      dword ptr [ebp - 0x18]
00412070  mov      word ptr [ebp - 0x24], 0x18
00412076  dec      dword ptr [ebp - 0x18]
00412079  push     2
0041207B  lea      eax, [ebp - 0xc]
0041207E  push     eax
0041207F  call     0x438f64
00412084  add      esp, 8
00412087  add      dword ptr [ebp - 0x18], 2
0041208B  add      dword ptr [ebp - 0x18], 3
0041208F  lea      edx, [ebp - 0x10]
00412092  push     edx
00412093  push     0x403b88
00412098  call     0x438eaa
0041209D  add      esp, 0x24
004120A0  shl      edi, 3
004120A3  add      edi, dword ptr [ebx + 5]
004120A6  mov      dword ptr [ebp - 0x3c], edi
004120A9  inc      dword ptr [ebp - 0x48]
004120AC  mov      ecx, dword ptr [ebp - 0x3c]
004120AF  mov      eax, dword ptr [esi + 0x39]
004120B2  mov      edx, dword ptr [ebp - 0x38]
004120B5  mov      ebx, dword ptr [ecx]
004120B7  mov      dword ptr [eax + edx*8], ebx
004120BA  mov      ebx, dword ptr [ecx + 4]
004120BD  mov      dword ptr [eax + edx*8 + 4], ebx
004120C1  inc      dword ptr [ebp - 0x38]
004120C4  mov      eax, dword ptr [ebp - 0x48]
004120C7  cmp      eax, dword ptr [ebp - 0x40]
004120CA  jb       0x411f8f
004120D0  push     esi
004120D1  call     0x412168
004120D6  pop      ecx
004120D7  jmp      0x4120e3
004120D9  xor      edx, edx
004120DB  mov      dword ptr [esi + 0x35], edx
004120DE  xor      ecx, ecx
004120E0  mov      dword ptr [esi + 0x39], ecx
004120E3  mov      eax, dword ptr [ebp - 0x34]
004120E6  mov      dword ptr fs:[0], eax
004120EC  pop      edi
004120ED  pop      esi
004120EE  pop      ebx
004120EF  mov      esp, ebp
004120F1  pop      ebp
004120F2  ret      
```

## Strings Referenced

**Total unique strings**: 9

- `"Cur < Upper"` @ 0x0044125E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044126A
- `"Precondition"` @ 0x0044128C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441299
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF
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

**Context around 0x0044126A**:

- `"default"` @ 0x00441212
- `"east_arrow"` @ 0x0044121A
- `"north_arrow"` @ 0x00441225
- `"west_arrow"` @ 0x00441231
- `"south_arrow"` @ 0x0044123C
- `"hand"` @ 0x00441248
- `"zoom"` @ 0x0044124D
- `"exit"` @ 0x00441252
- `"video"` @ 0x00441257
- `"Cur < Upper"` @ 0x0044125E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044126A
- `"Precondition"` @ 0x0044128C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441299
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF

**Context around 0x0044128C**:

- `"default"` @ 0x00441212
- `"east_arrow"` @ 0x0044121A
- `"north_arrow"` @ 0x00441225
- `"west_arrow"` @ 0x00441231
- `"south_arrow"` @ 0x0044123C
- `"hand"` @ 0x00441248
- `"zoom"` @ 0x0044124D
- `"exit"` @ 0x00441252
- `"video"` @ 0x00441257
- `"Cur < Upper"` @ 0x0044125E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044126A
- `"Precondition"` @ 0x0044128C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441299
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF
- `"HSCUR_%u"` @ 0x004412EC
- `"HSRGN_%u"` @ 0x004412F6
- `"ptr != NULL"` @ 0x00441302

**Context around 0x00441299**:

- `"east_arrow"` @ 0x0044121A
- `"north_arrow"` @ 0x00441225
- `"west_arrow"` @ 0x00441231
- `"south_arrow"` @ 0x0044123C
- `"hand"` @ 0x00441248
- `"zoom"` @ 0x0044124D
- `"exit"` @ 0x00441252
- `"video"` @ 0x00441257
- `"Cur < Upper"` @ 0x0044125E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044126A
- `"Precondition"` @ 0x0044128C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441299
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF
- `"HSCUR_%u"` @ 0x004412EC
- `"HSRGN_%u"` @ 0x004412F6
- `"ptr != NULL"` @ 0x00441302
- `"hotspot.cpp"` @ 0x0044130E

**Context around 0x004412BD**:

- `"outh_arrow"` @ 0x0044123D
- `"hand"` @ 0x00441248
- `"zoom"` @ 0x0044124D
- `"exit"` @ 0x00441252
- `"video"` @ 0x00441257
- `"Cur < Upper"` @ 0x0044125E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044126A
- `"Precondition"` @ 0x0044128C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441299
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF
- `"HSCUR_%u"` @ 0x004412EC
- `"HSRGN_%u"` @ 0x004412F6
- `"ptr != NULL"` @ 0x00441302
- `"hotspot.cpp"` @ 0x0044130E
- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B

**Context around 0x0044125E**:

- `"default"` @ 0x00441212
- `"east_arrow"` @ 0x0044121A
- `"north_arrow"` @ 0x00441225
- `"west_arrow"` @ 0x00441231
- `"south_arrow"` @ 0x0044123C
- `"hand"` @ 0x00441248
- `"zoom"` @ 0x0044124D
- `"exit"` @ 0x00441252
- `"video"` @ 0x00441257
- `"Cur < Upper"` @ 0x0044125E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044126A
- `"Precondition"` @ 0x0044128C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441299
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD

**Context around 0x004412DF**:

- `"ur < Upper"` @ 0x0044125F
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044126A
- `"Precondition"` @ 0x0044128C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441299
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF
- `"HSCUR_%u"` @ 0x004412EC
- `"HSRGN_%u"` @ 0x004412F6
- `"ptr != NULL"` @ 0x00441302
- `"hotspot.cpp"` @ 0x0044130E
- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B
- `"ptr != NULL"` @ 0x00441343
- `"hotspot.cpp"` @ 0x0044134F
- `"Check"` @ 0x0044135B

## Functions Called

- 0x00403618
- 0x00438F82
- 0x004037E0
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00412168

---

*Extracted with recursive CALL following and DATA context*
