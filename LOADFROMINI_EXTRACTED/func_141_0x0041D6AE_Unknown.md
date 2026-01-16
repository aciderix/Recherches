# LoadFromINI Function Analysis

**Function Address**: 0x0041D6AE
**Rank**: #141
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 79

```assembly
0041D6AE  push     ebp
0041D6AF  mov      ebp, esp
0041D6B1  add      esp, -0x28
0041D6B4  push     ebx
0041D6B5  push     esi
0041D6B6  push     edi
0041D6B7  mov      ebx, dword ptr [ebp + 0x14]
0041D6BA  mov      eax, 0x444454
0041D6BF  call     0x403618
0041D6C4  mov      word ptr [ebp - 0x18], 8
0041D6CA  push     dword ptr [ebp + 8]
0041D6CD  call     0x439714
0041D6D2  pop      ecx
0041D6D3  add      dword ptr [ebp - 0xc], 2
0041D6D7  mov      edx, dword ptr [ebp + 8]
0041D6DA  mov      dword ptr [edx + 5], 0x4449ec
0041D6E1  mov      ecx, dword ptr [ebp + 8]
0041D6E4  xor      eax, eax
0041D6E6  mov      dword ptr [ecx + 9], eax
0041D6E9  mov      word ptr [ebp - 0x18], 0x14
0041D6EF  push     0x1c
0041D6F1  call     0x438eec
0041D6F6  pop      ecx
0041D6F7  mov      dword ptr [ebp - 4], eax
0041D6FA  test     eax, eax
0041D6FC  je       0x41d726
0041D6FE  mov      word ptr [ebp - 0x18], 0x2c
0041D704  add      esp, -4
0041D707  mov      edx, dword ptr [ebp + 0x10]
0041D70A  mov      dword ptr [esp], edx
0041D70D  push     dword ptr [ebp + 0xc]
0041D710  push     dword ptr [ebp - 4]
0041D713  call     0x4394e6
0041D718  add      esp, 0xc
0041D71B  mov      word ptr [ebp - 0x18], 0x20
0041D721  mov      ecx, dword ptr [ebp - 4]
0041D724  jmp      0x41d729
0041D726  mov      ecx, dword ptr [ebp - 4]
0041D729  mov      eax, dword ptr [ebp + 8]
0041D72C  mov      dword ptr [eax + 9], ecx
0041D72F  mov      dx, word ptr [ebp + 0x1c]
0041D733  push     edx
0041D734  mov      ax, word ptr [ebp + 0x18]
0041D738  push     eax
0041D739  push     ebx
0041D73A  push     dword ptr [ebp + 8]
0041D73D  call     0x41d902
0041D742  add      esp, 0x10
0041D745  push     ebx
0041D746  mov      edx, dword ptr [ebp + 8]
0041D749  push     dword ptr [edx + 9]
0041D74C  push     dword ptr [ebp + 8]
0041D74F  call     0x4396ba
0041D754  add      esp, 0xc
0041D757  mov      word ptr [ebp - 0x18], 8
0041D75D  jmp      0x41d791
0041D75F  push     3
0041D761  mov      ecx, dword ptr [ebp + 8]
0041D764  push     dword ptr [ecx + 9]
0041D767  call     0x439678
0041D76C  add      esp, 8
0041D76F  mov      eax, dword ptr [ebp + 8]
0041D772  xor      edx, edx
0041D774  mov      dword ptr [eax + 9], edx
0041D777  push     0
0041D779  push     0x7fdf
0041D77E  call     0x4393fc
0041D783  add      esp, 8
0041D786  mov      word ptr [ebp - 0x18], 0x1c
0041D78C  call     0x438ee6
0041D791  mov      ecx, dword ptr [ebp - 0x28]
0041D794  mov      dword ptr fs:[0], ecx
0041D79B  mov      eax, dword ptr [ebp + 8]
0041D79E  pop      edi
0041D79F  pop      esi
0041D7A0  pop      ebx
0041D7A1  mov      esp, ebp
0041D7A3  pop      ebp
0041D7A4  ret      
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
- 0x004394E6
- 0x0041D902
- 0x004396BA
- 0x00439678
- 0x004393FC
- 0x00438EE6

---

*Extracted with recursive CALL following and DATA context*
