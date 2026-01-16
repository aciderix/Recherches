# LoadFromINI Function Analysis

**Function Address**: 0x004322E7
**Rank**: #167
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 97

```assembly
004322E7  push     ebp
004322E8  mov      ebp, esp
004322EA  add      esp, -0x34
004322ED  push     ebx
004322EE  mov      ebx, dword ptr [ebp + 8]
004322F1  mov      eax, 0x44b694
004322F6  call     0x403618
004322FB  cmp      dword ptr [ebx + 0x100], 0
00432302  je       0x43240d
00432308  mov      eax, dword ptr [ebx + 0x100]
0043230E  cmp      dword ptr [eax + 4], 0
00432312  je       0x43231b
00432314  mov      edx, dword ptr [eax + 4]
00432317  mov      byte ptr [edx + 0x1c], 1
0043231B  mov      ecx, dword ptr [ebx + 0x100]
00432321  xor      eax, eax
00432323  mov      dword ptr [ecx + 0x18], eax
00432326  lea      edx, [ebp - 0x34]
00432329  push     edx
0043232A  call     0x4391c2
0043232F  cmp      dword ptr [ebx + 0xc], 0
00432333  jne      0x4323ae
00432335  lea      ecx, [ebp - 0x2c]
00432338  push     ecx
00432339  push     0
0043233B  push     0
0043233D  push     0
0043233F  push     1
00432341  push     0x403be0
00432346  push     0
00432348  push     0x593
0043234D  push     0x44c9c1
00432352  push     0x44c9b5
00432357  push     0x44c9dd
0043235C  lea      eax, [ebp - 4]
0043235F  push     eax
00432360  call     0x438f10
00432365  add      esp, 0x14
00432368  lea      edx, [ebp - 4]
0043236B  push     edx
0043236C  inc      dword ptr [ebp - 0x10]
0043236F  lea      ecx, [ebp - 8]
00432372  push     ecx
00432373  call     0x438de4
00432378  add      esp, 8
0043237B  inc      dword ptr [ebp - 0x10]
0043237E  mov      word ptr [ebp - 0x1c], 0xc
00432384  dec      dword ptr [ebp - 0x10]
00432387  push     2
00432389  lea      eax, [ebp - 4]
0043238C  push     eax
0043238D  call     0x438f64
00432392  add      esp, 8
00432395  add      dword ptr [ebp - 0x10], 2
00432399  add      dword ptr [ebp - 0x10], 3
0043239D  lea      edx, [ebp - 8]
004323A0  push     edx
004323A1  push     0x403b88
004323A6  call     0x438eaa
004323AB  add      esp, 0x24
004323AE  lea      ecx, [ebp - 0x34]
004323B1  push     ecx
004323B2  push     dword ptr [ebx + 0xc]
004323B5  call     0x439258
004323BA  lea      eax, [ebp - 0x34]
004323BD  push     eax
004323BE  push     dword ptr [ebp + 0x10]
004323C1  mov      edx, dword ptr [ebx + 0x100]
004323C7  push     edx
004323C8  mov      ecx, dword ptr [edx]
004323CA  call     dword ptr [ecx + 0xc]
004323CD  add      esp, 0xc
004323D0  test     al, al
004323D2  jne      0x4323fa
004323D4  cmp      dword ptr [ebx + 0xfc], 0
004323DB  je       0x4323ed
004323DD  push     1
004323DF  push     dword ptr [ebx + 0xfc]
004323E5  call     0x42d858
004323EA  add      esp, 8
004323ED  lea      eax, [ebp - 0x34]
004323F0  push     eax
004323F1  push     ebx
004323F2  call     0x4330f1
004323F7  add      esp, 8
004323FA  mov      eax, dword ptr [ebx + 0x100]
00432400  cmp      dword ptr [eax + 4], 0
00432404  je       0x43240d
00432406  mov      edx, dword ptr [eax + 4]
00432409  mov      byte ptr [edx + 0x1c], 0
0043240D  xor      eax, eax
0043240F  mov      edx, dword ptr [ebp - 0x2c]
00432412  mov      dword ptr fs:[0], edx
00432419  pop      ebx
0043241A  mov      esp, ebp
0043241C  pop      ebp
0043241D  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"GetHandle()"` @ 0x0044C9B5
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C9C1
- `"Precondition"` @ 0x0044C9DD

## DATA Context

**Context around 0x0044C9DD**:

- `"window.h"` @ 0x0044C95D
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
- `"Precondition"` @ 0x0044CA31
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044CA3E

**Context around 0x0044C9C1**:

- `"Handle()"` @ 0x0044C941
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
- `"Precondition"` @ 0x0044CA31
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044CA3E

**Context around 0x0044C9B5**:

- `"window.h"` @ 0x0044C935
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
- `"Precondition"` @ 0x0044CA31

## Functions Called

- 0x00403618
- 0x004391C2
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00439258
- 0x0042D858
- 0x004330F1

---

*Extracted with recursive CALL following and DATA context*
