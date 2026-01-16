# LoadFromINI Function Analysis

**Function Address**: 0x00435A6A
**Rank**: #179
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 94

```assembly
00435A6A  push     ebp
00435A6B  mov      ebp, esp
00435A6D  add      esp, -0x2c
00435A70  push     ebx
00435A71  push     esi
00435A72  push     edi
00435A73  mov      ebx, dword ptr [ebp + 8]
00435A76  lea      edi, [ebp - 0x2c]
00435A79  mov      eax, 0x44bfc0
00435A7E  call     0x403618
00435A83  jmp      0x435a88
00435A85  inc      dword ptr [ebx + 0xd]
00435A88  mov      edx, dword ptr [ebx + 0xd]
00435A8B  cmp      edx, dword ptr [ebx + 9]
00435A8E  jae      0x435b31
00435A94  mov      esi, dword ptr [ebx + 0xd]
00435A97  cmp      dword ptr [ebx + 9], 0
00435A9B  je       0x435b22
00435AA1  cmp      dword ptr [ebx + 5], 0
00435AA5  je       0x435aac
00435AA7  cmp      esi, dword ptr [ebx + 9]
00435AAA  jb       0x435b22
00435AAC  push     edi
00435AAD  push     0
00435AAF  push     0
00435AB1  push     0
00435AB3  push     1
00435AB5  push     0x403be0
00435ABA  push     0
00435ABC  push     0x334
00435AC1  push     0x44cf17
00435AC6  push     0x44cef2
00435ACB  push     0x44cf39
00435AD0  lea      ecx, [ebp - 4]
00435AD3  push     ecx
00435AD4  call     0x438f10
00435AD9  add      esp, 0x14
00435ADC  lea      eax, [ebp - 4]
00435ADF  push     eax
00435AE0  inc      dword ptr [edi + 0x1c]
00435AE3  lea      edx, [ebp - 8]
00435AE6  push     edx
00435AE7  call     0x438de4
00435AEC  add      esp, 8
00435AEF  inc      dword ptr [edi + 0x1c]
00435AF2  mov      word ptr [edi + 0x10], 0xc
00435AF8  dec      dword ptr [edi + 0x1c]
00435AFB  push     2
00435AFD  lea      ecx, [ebp - 4]
00435B00  push     ecx
00435B01  call     0x438f64
00435B06  add      esp, 8
00435B09  add      dword ptr [edi + 0x1c], 2
00435B0D  add      dword ptr [edi + 0x1c], 3
00435B11  lea      eax, [ebp - 8]
00435B14  push     eax
00435B15  push     0x403b88
00435B1A  call     0x438eaa
00435B1F  add      esp, 0x24
00435B22  shl      esi, 2
00435B25  add      esi, dword ptr [ebx + 5]
00435B28  cmp      dword ptr [esi], 0
00435B2B  jne      0x435a85
00435B31  mov      edx, dword ptr [ebx + 0xd]
00435B34  cmp      edx, dword ptr [ebx + 9]
00435B37  jb       0x435b5a
00435B39  push     0
00435B3B  mov      ecx, dword ptr [ebx + 0xd]
00435B3E  inc      ecx
00435B3F  push     ecx
00435B40  push     ebx
00435B41  call     0x406954
00435B46  add      esp, 0xc
00435B49  test     eax, eax
00435B4B  jne      0x435b5a
00435B4D  xor      eax, eax
00435B4F  mov      edx, dword ptr [edi]
00435B51  mov      dword ptr fs:[0], edx
00435B58  jmp      0x435b79
00435B5A  mov      edx, dword ptr [ebp + 0xc]
00435B5D  mov      eax, dword ptr [ebx + 0xd]
00435B60  inc      dword ptr [ebx + 0xd]
00435B63  shl      eax, 2
00435B66  add      eax, dword ptr [ebx + 5]
00435B69  mov      dword ptr [eax], edx
00435B6B  mov      eax, 1
00435B70  mov      edx, dword ptr [edi]
00435B72  mov      dword ptr fs:[0], edx
00435B79  pop      edi
00435B7A  pop      esi
00435B7B  pop      ebx
00435B7C  mov      esp, ebp
00435B7E  pop      ebp
00435B7F  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044CEF2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CF17
- `"Precondition"` @ 0x0044CF39

## DATA Context

**Context around 0x0044CF39**:

- `"dition"` @ 0x0044CEB9
- `"Data != 0"` @ 0x0044CEC0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CECA
- `"Check"` @ 0x0044CEEC
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044CEF2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CF17
- `"Precondition"` @ 0x0044CF39
- `"Size > 0"` @ 0x0044CF46
- `"histqueu.h"` @ 0x0044CF4F
- `"Precondition"` @ 0x0044CF5A
- `"CanDoNext()"` @ 0x0044CF67
- `"histqueu.h"` @ 0x0044CF73
- `"Precondition"` @ 0x0044CF7E
- `"CanDoPrev()"` @ 0x0044CF8B
- `"histqueu.h"` @ 0x0044CF97
- `"Precondition"` @ 0x0044CFA2
- `"GetHandle()"` @ 0x0044CFB0

**Context around 0x0044CEF2**:

- `" || (Data != 0 && v.Data != 0)"` @ 0x0044CE72
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CE91
- `"Precondition"` @ 0x0044CEB3
- `"Data != 0"` @ 0x0044CEC0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CECA
- `"Check"` @ 0x0044CEEC
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044CEF2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CF17
- `"Precondition"` @ 0x0044CF39
- `"Size > 0"` @ 0x0044CF46
- `"histqueu.h"` @ 0x0044CF4F
- `"Precondition"` @ 0x0044CF5A
- `"CanDoNext()"` @ 0x0044CF67

**Context around 0x0044CF17**:

- `"\INCLUDE\classlib/vectimp.h"` @ 0x0044CE97
- `"Precondition"` @ 0x0044CEB3
- `"Data != 0"` @ 0x0044CEC0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CECA
- `"Check"` @ 0x0044CEEC
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044CEF2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CF17
- `"Precondition"` @ 0x0044CF39
- `"Size > 0"` @ 0x0044CF46
- `"histqueu.h"` @ 0x0044CF4F
- `"Precondition"` @ 0x0044CF5A
- `"CanDoNext()"` @ 0x0044CF67
- `"histqueu.h"` @ 0x0044CF73
- `"Precondition"` @ 0x0044CF7E
- `"CanDoPrev()"` @ 0x0044CF8B

## Functions Called

- 0x00403618
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00406954

---

*Extracted with recursive CALL following and DATA context*
