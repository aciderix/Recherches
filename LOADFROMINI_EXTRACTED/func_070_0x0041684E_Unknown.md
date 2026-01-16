# LoadFromINI Function Analysis

**Function Address**: 0x0041684E
**Rank**: #70
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 119

```assembly
0041684E  push     ebp
0041684F  mov      ebp, esp
00416851  add      esp, -0x24
00416854  push     ebx
00416855  push     esi
00416856  lea      esi, [ebp - 0x24]
00416859  mov      eax, 0x441dd0
0041685E  call     0x403618
00416863  mov      dword ptr [esi + 0x1c], 0x19
0041686A  cmp      dword ptr [ebp + 8], 0
0041686E  je       0x4169b6
00416874  mov      word ptr [esi + 0x10], 8
0041687A  mov      edx, dword ptr [ebp + 8]
0041687D  mov      dword ptr [edx + 0x2d], 0x442d34
00416884  mov      ecx, dword ptr [ebp + 8]
00416887  mov      dword ptr [ecx + 0x1d], 0x442d44
0041688E  push     dword ptr [ebp + 8]
00416891  call     0x416fcd
00416896  pop      ecx
00416897  sub      dword ptr [esi + 0x1c], 8
0041689B  push     2
0041689D  mov      eax, dword ptr [ebp + 8]
004168A0  add      eax, 0x5e
004168A3  push     eax
004168A4  call     0x405a63
004168A9  add      esp, 8
004168AC  sub      dword ptr [esi + 0x1c], 3
004168B0  add      dword ptr [esi + 0x1c], 3
004168B4  dec      dword ptr [esi + 0x1c]
004168B7  dec      dword ptr [esi + 0x1c]
004168BA  dec      dword ptr [esi + 0x1c]
004168BD  push     2
004168BF  mov      edx, dword ptr [ebp + 8]
004168C2  add      edx, 0x39
004168C5  push     edx
004168C6  call     0x438f64
004168CB  add      esp, 8
004168CE  dec      dword ptr [esi + 0x1c]
004168D1  push     2
004168D3  mov      ecx, dword ptr [ebp + 8]
004168D6  add      ecx, 0x35
004168D9  push     ecx
004168DA  call     0x438f64
004168DF  add      esp, 8
004168E2  dec      dword ptr [esi + 0x1c]
004168E5  push     2
004168E7  mov      eax, dword ptr [ebp + 8]
004168EA  add      eax, 0x31
004168ED  push     eax
004168EE  call     0x438f64
004168F3  add      esp, 8
004168F6  sub      dword ptr [esi + 0x1c], 4
004168FA  mov      ebx, dword ptr [ebp + 8]
004168FD  add      ebx, 0x1d
00416900  add      dword ptr [esi + 0x1c], 4
00416904  dec      dword ptr [esi + 0x1c]
00416907  push     2
00416909  lea      eax, [ebx + 0xc]
0041690C  push     eax
0041690D  call     0x438f64
00416912  add      esp, 8
00416915  dec      dword ptr [esi + 0x1c]
00416918  push     2
0041691A  lea      edx, [ebx + 8]
0041691D  push     edx
0041691E  call     0x438f64
00416923  add      esp, 8
00416926  dec      dword ptr [esi + 0x1c]
00416929  push     2
0041692B  add      ebx, 4
0041692E  push     ebx
0041692F  call     0x438f64
00416934  add      esp, 8
00416937  sub      dword ptr [esi + 0x1c], 7
0041693B  add      dword ptr [esi + 0x1c], 7
0041693F  sub      dword ptr [esi + 0x1c], 6
00416943  add      dword ptr [esi + 0x1c], 6
00416947  sub      dword ptr [esi + 0x1c], 5
0041694B  mov      eax, dword ptr [ebp + 8]
0041694E  cmp      dword ptr [eax + 0x19], 2
00416952  je       0x416958
00416954  xor      eax, eax
00416956  jmp      0x41695d
00416958  mov      eax, 1
0041695D  mov      ebx, dword ptr [ebp + 8]
00416960  add      ebx, 4
00416963  push     0
00416965  push     -1
00416967  push     eax
00416968  push     ebx
00416969  call     0x4264f3
0041696E  add      esp, 0x10
00416971  xor      eax, eax
00416973  mov      dword ptr [ebx + 0xd], eax
00416976  sub      dword ptr [esi + 0x1c], 4
0041697A  add      dword ptr [esi + 0x1c], 4
0041697E  sub      dword ptr [esi + 0x1c], 3
00416982  mov      eax, dword ptr [ebp + 8]
00416985  add      eax, 4
00416988  add      dword ptr [esi + 0x1c], 3
0041698C  sub      dword ptr [esi + 0x1c], 2
00416990  add      dword ptr [esi + 0x1c], 2
00416994  dec      dword ptr [esi + 0x1c]
00416997  mov      dword ptr [eax + 1], 0x43b500
0041699E  push     dword ptr [eax + 5]
004169A1  call     0x438f82
004169A6  pop      ecx
004169A7  test     byte ptr [ebp + 0xc], 1
004169AB  je       0x4169b6
004169AD  push     dword ptr [ebp + 8]
004169B0  call     0x438f16
004169B5  pop      ecx
004169B6  mov      edx, dword ptr [esi]
004169B8  mov      dword ptr fs:[0], edx
004169BF  pop      esi
004169C0  pop      ebx
004169C1  mov      esp, ebp
004169C3  pop      ebp
004169C4  ret      
```

## Strings Referenced

**Total unique strings**: 2

- `"P[@"` @ 0x0043B4EC
- `"NhA"` @ 0x00442D34

## DATA Context

**Context around 0x0043B4EC**:

- `"LUDE\classlib/vectimp.h"` @ 0x0043B46C
- `"Check"` @ 0x0043B484
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0043B48A
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B4AF
- `"Precondition"` @ 0x0043B4D1
- `"P[@"` @ 0x0043B4EC
- `"cZ@"` @ 0x0043B4F0
- `"+l@"` @ 0x0043B528
- `"+l@"` @ 0x0043B544
- `"1h@"` @ 0x0043B548
- `"-m@"` @ 0x0043B554
- `"%<@"` @ 0x0043B560

**Context around 0x00442D34**:

- `"*{A"` @ 0x00442CD4
- `"kzA"` @ 0x00442D0C
- `""|A"` @ 0x00442D28
- `"NhA"` @ 0x00442D34
- `"uZA"` @ 0x00442D64
- `"DTA"` @ 0x00442D6C
- `"*KA"` @ 0x00442DA4

## Functions Called

- 0x00403618
- 0x00416FCD
- 0x00405A63
- 0x00438F64
- 0x00438F64
- 0x00438F64
- 0x00438F64
- 0x00438F64
- 0x00438F64
- 0x004264F3
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
