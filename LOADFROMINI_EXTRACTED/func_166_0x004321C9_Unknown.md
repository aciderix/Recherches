# LoadFromINI Function Analysis

**Function Address**: 0x004321C9
**Rank**: #166
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 91

```assembly
004321C9  push     ebp
004321CA  mov      ebp, esp
004321CC  add      esp, -0x34
004321CF  push     ebx
004321D0  mov      ebx, dword ptr [ebp + 8]
004321D3  mov      eax, 0x44b648
004321D8  call     0x403618
004321DD  cmp      dword ptr [ebx + 0x104], 0
004321E4  je       0x4322d6
004321EA  mov      eax, dword ptr [ebx + 0x104]
004321F0  cmp      dword ptr [eax + 4], 0
004321F4  je       0x4321fd
004321F6  mov      edx, dword ptr [eax + 4]
004321F9  mov      byte ptr [edx + 0x1c], 1
004321FD  mov      ecx, dword ptr [ebx + 0x104]
00432203  xor      eax, eax
00432205  mov      dword ptr [ecx + 0x18], eax
00432208  lea      edx, [ebp - 0x34]
0043220B  push     edx
0043220C  call     0x4391c2
00432211  cmp      dword ptr [ebx + 0xc], 0
00432215  jne      0x432290
00432217  lea      ecx, [ebp - 0x2c]
0043221A  push     ecx
0043221B  push     0
0043221D  push     0
0043221F  push     0
00432221  push     1
00432223  push     0x403be0
00432228  push     0
0043222A  push     0x593
0043222F  push     0x44c98c
00432234  push     0x44c980
00432239  push     0x44c9a8
0043223E  lea      eax, [ebp - 4]
00432241  push     eax
00432242  call     0x438f10
00432247  add      esp, 0x14
0043224A  lea      edx, [ebp - 4]
0043224D  push     edx
0043224E  inc      dword ptr [ebp - 0x10]
00432251  lea      ecx, [ebp - 8]
00432254  push     ecx
00432255  call     0x438de4
0043225A  add      esp, 8
0043225D  inc      dword ptr [ebp - 0x10]
00432260  mov      word ptr [ebp - 0x1c], 0xc
00432266  dec      dword ptr [ebp - 0x10]
00432269  push     2
0043226B  lea      eax, [ebp - 4]
0043226E  push     eax
0043226F  call     0x438f64
00432274  add      esp, 8
00432277  add      dword ptr [ebp - 0x10], 2
0043227B  add      dword ptr [ebp - 0x10], 3
0043227F  lea      edx, [ebp - 8]
00432282  push     edx
00432283  push     0x403b88
00432288  call     0x438eaa
0043228D  add      esp, 0x24
00432290  lea      ecx, [ebp - 0x34]
00432293  push     ecx
00432294  push     dword ptr [ebx + 0xc]
00432297  call     0x439258
0043229C  lea      eax, [ebp - 0x34]
0043229F  push     eax
004322A0  push     dword ptr [ebp + 0x10]
004322A3  mov      edx, dword ptr [ebx + 0x104]
004322A9  push     edx
004322AA  mov      ecx, dword ptr [edx]
004322AC  call     dword ptr [ecx + 0xc]
004322AF  add      esp, 0xc
004322B2  test     al, al
004322B4  jne      0x4322c3
004322B6  lea      eax, [ebp - 0x34]
004322B9  push     eax
004322BA  push     ebx
004322BB  call     0x4330f1
004322C0  add      esp, 8
004322C3  mov      eax, dword ptr [ebx + 0x104]
004322C9  cmp      dword ptr [eax + 4], 0
004322CD  je       0x4322d6
004322CF  mov      edx, dword ptr [eax + 4]
004322D2  mov      byte ptr [edx + 0x1c], 0
004322D6  xor      eax, eax
004322D8  mov      edx, dword ptr [ebp - 0x2c]
004322DB  mov      dword ptr fs:[0], edx
004322E2  pop      ebx
004322E3  mov      esp, ebp
004322E5  pop      ebp
004322E6  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"GetHandle()"` @ 0x0044C980
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C98C
- `"Precondition"` @ 0x0044C9A8

## DATA Context

**Context around 0x0044C980**:

- `"w.h"` @ 0x0044C900
- `"Precondition"` @ 0x0044C904
- `"GetApplication()"` @ 0x0044C911
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C922
- `"GetHandle()"` @ 0x0044C93E
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C94A
- `"Precondition"` @ 0x0044C966
- `"Precondition"` @ 0x0044C973
- `"GetHandle()"` @ 0x0044C980
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C98C
- `"Precondition"` @ 0x0044C9A8
- `"GetHandle()"` @ 0x0044C9B5
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C9C1
- `"Precondition"` @ 0x0044C9DD
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044C9EA

**Context around 0x0044C98C**:

- `"tion"` @ 0x0044C90C
- `"GetApplication()"` @ 0x0044C911
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C922
- `"GetHandle()"` @ 0x0044C93E
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C94A
- `"Precondition"` @ 0x0044C966
- `"Precondition"` @ 0x0044C973
- `"GetHandle()"` @ 0x0044C980
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C98C
- `"Precondition"` @ 0x0044C9A8
- `"GetHandle()"` @ 0x0044C9B5
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C9C1
- `"Precondition"` @ 0x0044C9DD
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044C9EA

**Context around 0x0044C9A8**:

- `"\INCLUDE\owl/window.h"` @ 0x0044C928
- `"GetHandle()"` @ 0x0044C93E
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C94A
- `"Precondition"` @ 0x0044C966
- `"Precondition"` @ 0x0044C973
- `"GetHandle()"` @ 0x0044C980
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C98C
- `"Precondition"` @ 0x0044C9A8
- `"GetHandle()"` @ 0x0044C9B5
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C9C1
- `"Precondition"` @ 0x0044C9DD
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044C9EA
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CA0F

## Functions Called

- 0x00403618
- 0x004391C2
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00439258
- 0x004330F1

---

*Extracted with recursive CALL following and DATA context*
