# LoadFromINI Function Analysis

**Function Address**: 0x004268F8
**Rank**: #165
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 215

```assembly
004268F8  push     ebp
004268F9  mov      ebp, esp
004268FB  add      esp, -0x5c
004268FE  push     ebx
004268FF  push     esi
00426900  push     edi
00426901  mov      ebx, dword ptr [ebp + 0xc]
00426904  mov      esi, dword ptr [ebp + 8]
00426907  mov      edi, 0x44ec10
0042690C  mov      eax, 0x447bc4
00426911  call     0x403618
00426916  cmp      byte ptr [ebp + 0x10], 0
0042691A  je       0x426988
0042691C  push     esi
0042691D  mov      edx, dword ptr [esi + 8]
00426920  call     dword ptr [edx + 0x7c]
00426923  pop      ecx
00426924  test     eax, eax
00426926  je       0x426988
00426928  push     esi
00426929  mov      ecx, dword ptr [esi + 8]
0042692C  call     dword ptr [ecx + 0x7c]
0042692F  pop      ecx
00426930  mov      dword ptr [ebp - 0x38], eax
00426933  push     dword ptr [ebp - 0x38]
00426936  lea      eax, [edi + 0x64]
00426939  push     eax
0042693A  call     0x42634d
0042693F  add      esp, 8
00426942  mov      dword ptr [ebp - 0x3c], eax
00426945  cmp      dword ptr [ebp - 0x3c], -1
00426949  jne      0x426952
0042694B  mov      edx, 0x7fffffff
00426950  jmp      0x426958
00426952  mov      edx, dword ptr [ebp - 0x3c]
00426955  add      edx, dword ptr [edi + 0x60]
00426958  add      ebx, edx
0042695A  lea      eax, [edi + 0x64]
0042695D  push     eax
0042695E  mov      ecx, dword ptr [edi + 0x65]
00426961  call     dword ptr [ecx + 4]
00426964  pop      ecx
00426965  cmp      ebx, eax
00426967  jle      0x426976
00426969  lea      eax, [edi + 0x64]
0042696C  push     eax
0042696D  mov      edx, dword ptr [edi + 0x65]
00426970  call     dword ptr [edx + 4]
00426973  pop      ecx
00426974  sub      ebx, eax
00426976  cmp      ebx, 1
00426979  jge      0x426988
0042697B  lea      ecx, [edi + 0x64]
0042697E  push     ecx
0042697F  mov      eax, dword ptr [edi + 0x65]
00426982  call     dword ptr [eax + 4]
00426985  pop      ecx
00426986  add      ebx, eax
00426988  mov      dword ptr [ebp - 0x40], ebx
0042698B  cmp      dword ptr [ebp - 0x40], 1
0042698F  jl       0x4269a1
00426991  lea      edx, [edi + 0x64]
00426994  push     edx
00426995  mov      ecx, dword ptr [edi + 0x65]
00426998  call     dword ptr [ecx + 4]
0042699B  pop      ecx
0042699C  cmp      eax, dword ptr [ebp - 0x40]
0042699F  jge      0x4269a5
004269A1  xor      eax, eax
004269A3  jmp      0x4269aa
004269A5  mov      eax, 1
004269AA  test     al, al
004269AC  je       0x426b44
004269B2  mov      word ptr [ebp - 0x24], 8
004269B8  mov      dword ptr [ebp - 0x44], ebx
004269BB  lea      edx, [edi + 0x24]
004269BE  push     edx
004269BF  lea      ecx, [ebp - 8]
004269C2  push     ecx
004269C3  call     0x438e3e
004269C8  add      esp, 8
004269CB  inc      dword ptr [ebp - 0x18]
004269CE  mov      eax, dword ptr [ebp - 0x44]
004269D1  mov      dword ptr [ebp - 4], eax
004269D4  lea      edx, [ebp - 8]
004269D7  add      dword ptr [ebp - 0x18], 2
004269DB  push     edx
004269DC  lea      ecx, [esi + 0x8e]
004269E2  push     ecx
004269E3  call     0x435f74
004269E8  add      esp, 8
004269EB  sub      dword ptr [ebp - 0x18], 2
004269EF  add      dword ptr [ebp - 0x18], 2
004269F3  dec      dword ptr [ebp - 0x18]
004269F6  push     2
004269F8  lea      eax, [ebp - 8]
004269FB  push     eax
004269FC  call     0x438f64
00426A01  add      esp, 8
00426A04  push     esi
00426A05  call     0x433f55
00426A0A  pop      ecx
00426A0B  mov      dl, byte ptr [ebp + 0x14]
00426A0E  push     edx
00426A0F  mov      dword ptr [ebp - 0x48], ebx
00426A12  mov      ecx, dword ptr [ebp - 0x48]
00426A15  inc      ecx
00426A16  mov      dword ptr [ebp - 0x4c], ecx
00426A19  mov      eax, dword ptr [ebp - 0x4c]
00426A1C  cmp      eax, dword ptr [edi + 0x60]
00426A1F  jge      0x426a40
00426A21  mov      edx, dword ptr [ebp - 0x4c]
00426A24  sub      edx, dword ptr [edi + 0x60]
00426A27  add      edx, dword ptr [edi + 0x6d]
00426A2A  mov      dword ptr [ebp - 0x50], edx
00426A2D  push     0
00426A2F  push     dword ptr [ebp - 0x50]
00426A32  lea      ecx, [edi + 0x64]
00426A35  push     ecx
00426A36  call     0x406954
00426A3B  add      esp, 0xc
00426A3E  jmp      0x426a78
00426A40  mov      eax, dword ptr [edi + 0x6d]
00426A43  mov      dword ptr [ebp - 0x54], eax
00426A46  cmp      dword ptr [ebp - 0x54], -1
00426A4A  jne      0x426a53
00426A4C  mov      edx, 0x7fffffff
00426A51  jmp      0x426a59
00426A53  mov      edx, dword ptr [ebp - 0x54]
00426A56  add      edx, dword ptr [edi + 0x60]
00426A59  cmp      edx, dword ptr [ebp - 0x4c]
00426A5C  jg       0x426a78
00426A5E  mov      eax, dword ptr [ebp - 0x4c]
00426A61  sub      eax, dword ptr [edi + 0x60]
00426A64  mov      dword ptr [ebp - 0x58], eax
00426A67  push     0
00426A69  push     dword ptr [ebp - 0x58]
00426A6C  lea      ecx, [edi + 0x64]
00426A6F  push     ecx
00426A70  call     0x406954
00426A75  add      esp, 0xc
00426A78  mov      eax, dword ptr [ebp - 0x48]
00426A7B  sub      eax, dword ptr [edi + 0x60]
00426A7E  mov      dword ptr [ebp - 0x5c], eax
00426A81  cmp      dword ptr [edi + 0x6d], 0
00426A85  je       0x426b22
00426A8B  cmp      dword ptr [edi + 0x69], 0
00426A8F  je       0x426a9d
00426A91  mov      edx, dword ptr [ebp - 0x5c]
00426A94  cmp      edx, dword ptr [edi + 0x6d]
00426A97  jb       0x426b22
00426A9D  lea      ecx, [ebp - 0x34]
00426AA0  push     ecx
00426AA1  push     0
00426AA3  push     0
00426AA5  push     0
00426AA7  push     1
00426AA9  push     0x403be0
00426AAE  push     0
00426AB0  mov      word ptr [ebp - 0x24], 0x14
00426AB6  push     0x334
00426ABB  push     0x448f2a
00426AC0  push     0x448f05
00426AC5  push     0x448f4c
00426ACA  lea      eax, [ebp - 0xc]
00426ACD  push     eax
00426ACE  call     0x438f10
00426AD3  add      esp, 0x14
00426AD6  lea      edx, [ebp - 0xc]
00426AD9  push     edx
00426ADA  inc      dword ptr [ebp - 0x18]
00426ADD  lea      ecx, [ebp - 0x10]
00426AE0  push     ecx
00426AE1  call     0x438de4
00426AE6  add      esp, 8
00426AE9  inc      dword ptr [ebp - 0x18]
00426AEC  mov      word ptr [ebp - 0x24], 0x20
00426AF2  dec      dword ptr [ebp - 0x18]
00426AF5  push     2
00426AF7  lea      eax, [ebp - 0xc]
00426AFA  push     eax
00426AFB  call     0x438f64
00426B00  add      esp, 8
00426B03  mov      word ptr [ebp - 0x24], 0x14
00426B09  add      dword ptr [ebp - 0x18], 2
00426B0D  add      dword ptr [ebp - 0x18], 3
00426B11  lea      edx, [ebp - 0x10]
00426B14  push     edx
00426B15  push     0x403b88
00426B1A  call     0x438eaa
00426B1F  add      esp, 0x24
00426B22  mov      ecx, dword ptr [ebp - 0x5c]
00426B25  shl      ecx, 2
00426B28  add      ecx, dword ptr [edi + 0x69]
00426B2B  push     dword ptr [ecx]
00426B2D  push     esi
00426B2E  call     0x434070
00426B33  add      esp, 0xc
00426B36  mov      al, 1
00426B38  mov      edx, dword ptr [ebp - 0x34]
00426B3B  mov      dword ptr fs:[0], edx
00426B42  jmp      0x426b5b
00426B44  push     ebx
00426B45  push     0x68
00426B47  call     0x404f9c
00426B4C  add      esp, 8
00426B4F  xor      eax, eax
00426B51  mov      edx, dword ptr [ebp - 0x34]
00426B54  mov      dword ptr fs:[0], edx
00426B5B  pop      edi
00426B5C  pop      esi
00426B5D  pop      ebx
00426B5E  mov      esp, ebp
00426B60  pop      ebp
00426B61  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C

## DATA Context

**Context around 0x00448F2A**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E
- `"Precondition"` @ 0x00448FA0

**Context around 0x00448F4C**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E
- `"Precondition"` @ 0x00448FA0
- `"GetHandle()"` @ 0x00448FAD
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00448FB9

**Context around 0x00448F05**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E

## Functions Called

- 0x00403618
- 0x0042634D
- 0x00438E3E
- 0x00435F74
- 0x00438F64
- 0x00433F55
- 0x00406954
- 0x00406954
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00434070
- 0x00404F9C

---

*Extracted with recursive CALL following and DATA context*
