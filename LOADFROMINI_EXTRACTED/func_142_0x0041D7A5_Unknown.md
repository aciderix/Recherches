# LoadFromINI Function Analysis

**Function Address**: 0x0041D7A5
**Rank**: #142
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 78

```assembly
0041D7A5  push     ebp
0041D7A6  mov      ebp, esp
0041D7A8  add      esp, -0x28
0041D7AB  push     ebx
0041D7AC  push     esi
0041D7AD  push     edi
0041D7AE  mov      ebx, dword ptr [ebp + 0x10]
0041D7B1  mov      eax, 0x4444cc
0041D7B6  call     0x403618
0041D7BB  mov      word ptr [ebp - 0x18], 8
0041D7C1  push     dword ptr [ebp + 8]
0041D7C4  call     0x439714
0041D7C9  pop      ecx
0041D7CA  add      dword ptr [ebp - 0xc], 2
0041D7CE  mov      edx, dword ptr [ebp + 8]
0041D7D1  mov      dword ptr [edx + 5], 0x4449ec
0041D7D8  mov      ecx, dword ptr [ebp + 8]
0041D7DB  xor      eax, eax
0041D7DD  mov      dword ptr [ecx + 9], eax
0041D7E0  mov      word ptr [ebp - 0x18], 0x14
0041D7E6  push     0x1c
0041D7E8  call     0x438eec
0041D7ED  pop      ecx
0041D7EE  mov      dword ptr [ebp - 4], eax
0041D7F1  test     eax, eax
0041D7F3  je       0x41d819
0041D7F5  mov      word ptr [ebp - 0x18], 0x2c
0041D7FB  mov      edx, dword ptr [ebp + 0xc]
0041D7FE  mov      ecx, dword ptr [edx]
0041D800  push     dword ptr [ecx + 2]
0041D803  push     dword ptr [ebp - 4]
0041D806  call     0x4394c8
0041D80B  add      esp, 8
0041D80E  mov      word ptr [ebp - 0x18], 0x20
0041D814  mov      eax, dword ptr [ebp - 4]
0041D817  jmp      0x41d81c
0041D819  mov      eax, dword ptr [ebp - 4]
0041D81C  mov      edx, dword ptr [ebp + 8]
0041D81F  mov      dword ptr [edx + 9], eax
0041D822  mov      cx, word ptr [ebp + 0x18]
0041D826  push     ecx
0041D827  mov      ax, word ptr [ebp + 0x14]
0041D82B  push     eax
0041D82C  push     ebx
0041D82D  push     dword ptr [ebp + 8]
0041D830  call     0x41d902
0041D835  add      esp, 0x10
0041D838  push     ebx
0041D839  mov      edx, dword ptr [ebp + 8]
0041D83C  push     dword ptr [edx + 9]
0041D83F  push     dword ptr [ebp + 8]
0041D842  call     0x4396ba
0041D847  add      esp, 0xc
0041D84A  mov      word ptr [ebp - 0x18], 8
0041D850  jmp      0x41d884
0041D852  push     3
0041D854  mov      ecx, dword ptr [ebp + 8]
0041D857  push     dword ptr [ecx + 9]
0041D85A  call     0x439678
0041D85F  add      esp, 8
0041D862  mov      eax, dword ptr [ebp + 8]
0041D865  xor      edx, edx
0041D867  mov      dword ptr [eax + 9], edx
0041D86A  push     0
0041D86C  push     0x7fdf
0041D871  call     0x4393fc
0041D876  add      esp, 8
0041D879  mov      word ptr [ebp - 0x18], 0x1c
0041D87F  call     0x438ee6
0041D884  mov      ecx, dword ptr [ebp - 0x28]
0041D887  mov      dword ptr fs:[0], ecx
0041D88E  mov      eax, dword ptr [ebp + 8]
0041D891  pop      edi
0041D892  pop      esi
0041D893  pop      ebx
0041D894  mov      esp, ebp
0041D896  pop      ebp
0041D897  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885

## DATA Context

**Context around 0x00444878**:

- `",HD"` @ 0x0044484C
- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2

**Context around 0x00444869**:

- `",HD"` @ 0x0044484C
- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5

**Context around 0x00444885**:

- `",HD"` @ 0x0044484C
- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2

## Functions Called

- 0x00403618
- 0x00439714
- 0x00438EEC
- 0x004394C8
- 0x0041D902
- 0x004396BA
- 0x00439678
- 0x004393FC
- 0x00438EE6

---

*Extracted with recursive CALL following and DATA context*
