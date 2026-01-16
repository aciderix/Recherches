# LoadFromINI Function Analysis

**Function Address**: 0x0041E206
**Rank**: #153
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 148

```assembly
0041E206  push     ebp
0041E207  mov      ebp, esp
0041E209  add      esp, -0x40
0041E20C  push     ebx
0041E20D  push     esi
0041E20E  push     edi
0041E20F  mov      ebx, dword ptr [ebp + 8]
0041E212  mov      eax, 0x4446f4
0041E217  call     0x403618
0041E21C  xor      edx, edx
0041E21E  mov      dword ptr [ebp - 0x38], edx
0041E221  jmp      0x41e387
0041E226  mov      edi, dword ptr [ebp - 0x38]
0041E229  cmp      edi, dword ptr [ebx]
0041E22B  jl       0x41e236
0041E22D  mov      ecx, edi
0041E22F  sub      ecx, dword ptr [ebx]
0041E231  cmp      ecx, dword ptr [ebx + 0xd]
0041E234  jb       0x41e2af
0041E236  lea      eax, [ebp - 0x34]
0041E239  push     eax
0041E23A  push     0
0041E23C  push     0
0041E23E  push     0
0041E240  push     1
0041E242  push     0x403be0
0041E247  push     0
0041E249  push     0x15e
0041E24E  push     0x4448c4
0041E253  push     0x444892
0041E258  push     0x4448e5
0041E25D  lea      edx, [ebp - 4]
0041E260  push     edx
0041E261  call     0x438f10
0041E266  add      esp, 0x14
0041E269  lea      ecx, [ebp - 4]
0041E26C  push     ecx
0041E26D  inc      dword ptr [ebp - 0x18]
0041E270  lea      eax, [ebp - 8]
0041E273  push     eax
0041E274  call     0x438de4
0041E279  add      esp, 8
0041E27C  inc      dword ptr [ebp - 0x18]
0041E27F  mov      word ptr [ebp - 0x24], 0xc
0041E285  dec      dword ptr [ebp - 0x18]
0041E288  push     2
0041E28A  lea      edx, [ebp - 4]
0041E28D  push     edx
0041E28E  call     0x438f64
0041E293  add      esp, 8
0041E296  add      dword ptr [ebp - 0x18], 2
0041E29A  add      dword ptr [ebp - 0x18], 3
0041E29E  lea      ecx, [ebp - 8]
0041E2A1  push     ecx
0041E2A2  push     0x403b88
0041E2A7  call     0x438eaa
0041E2AC  add      esp, 0x24
0041E2AF  sub      edi, dword ptr [ebx]
0041E2B1  mov      dword ptr [ebp - 0x3c], edi
0041E2B4  lea      esi, [ebx + 4]
0041E2B7  cmp      dword ptr [esi + 9], 0
0041E2BB  jbe      0x41e2cb
0041E2BD  cmp      dword ptr [esi + 5], 0
0041E2C1  je       0x41e2cb
0041E2C3  mov      eax, dword ptr [ebp - 0x3c]
0041E2C6  cmp      eax, dword ptr [esi + 9]
0041E2C9  jb       0x41e344
0041E2CB  lea      edx, [ebp - 0x34]
0041E2CE  push     edx
0041E2CF  push     0
0041E2D1  push     0
0041E2D3  push     0
0041E2D5  push     1
0041E2D7  push     0x403be0
0041E2DC  push     0
0041E2DE  push     0x33a
0041E2E3  push     0x444916
0041E2E8  push     0x4448f2
0041E2ED  push     0x444938
0041E2F2  lea      ecx, [ebp - 0xc]
0041E2F5  push     ecx
0041E2F6  call     0x438f10
0041E2FB  add      esp, 0x14
0041E2FE  lea      eax, [ebp - 0xc]
0041E301  push     eax
0041E302  inc      dword ptr [ebp - 0x18]
0041E305  lea      edx, [ebp - 0x10]
0041E308  push     edx
0041E309  call     0x438de4
0041E30E  add      esp, 8
0041E311  inc      dword ptr [ebp - 0x18]
0041E314  mov      word ptr [ebp - 0x24], 0x18
0041E31A  dec      dword ptr [ebp - 0x18]
0041E31D  push     2
0041E31F  lea      ecx, [ebp - 0xc]
0041E322  push     ecx
0041E323  call     0x438f64
0041E328  add      esp, 8
0041E32B  add      dword ptr [ebp - 0x18], 2
0041E32F  add      dword ptr [ebp - 0x18], 3
0041E333  lea      eax, [ebp - 0x10]
0041E336  push     eax
0041E337  push     0x403b88
0041E33C  call     0x438eaa
0041E341  add      esp, 0x24
0041E344  mov      edx, dword ptr [ebp - 0x3c]
0041E347  shl      edx, 2
0041E34A  add      edx, dword ptr [esi + 5]
0041E34D  mov      esi, dword ptr [edx]
0041E34F  mov      edi, dword ptr [ebp + 0xc]
0041E352  lea      ecx, [esi + 0x14]
0041E355  mov      dword ptr [ebp - 0x40], ecx
0041E358  push     edi
0041E359  push     dword ptr [ebp - 0x40]
0041E35C  call     0x438ec8
0041E361  add      esp, 8
0041E364  test     eax, eax
0041E366  jne      0x41e384
0041E368  cmp      dword ptr [ebp + 0x10], 0
0041E36C  je       0x41e376
0041E36E  mov      eax, dword ptr [ebp + 0x10]
0041E371  mov      edx, dword ptr [ebp - 0x38]
0041E374  mov      dword ptr [eax], edx
0041E376  mov      eax, esi
0041E378  mov      edx, dword ptr [ebp - 0x34]
0041E37B  mov      dword ptr fs:[0], edx
0041E382  jmp      0x41e3b6
0041E384  inc      dword ptr [ebp - 0x38]
0041E387  lea      ecx, [ebx + 4]
0041E38A  push     ecx
0041E38B  mov      eax, dword ptr [ebx + 5]
0041E38E  call     dword ptr [eax + 4]
0041E391  pop      ecx
0041E392  cmp      eax, dword ptr [ebp - 0x38]
0041E395  jg       0x41e226
0041E39B  cmp      dword ptr [ebp + 0x10], 0
0041E39F  je       0x41e3aa
0041E3A1  mov      edx, dword ptr [ebp + 0x10]
0041E3A4  mov      dword ptr [edx], 0x7fffffff
0041E3AA  xor      eax, eax
0041E3AC  mov      edx, dword ptr [ebp - 0x34]
0041E3AF  mov      dword ptr fs:[0], edx
0041E3B6  pop      edi
0041E3B7  pop      esi
0041E3B8  pop      ebx
0041E3B9  mov      esp, ebp
0041E3BB  pop      ebp
0041E3BC  ret      
```

## Strings Referenced

**Total unique strings**: 6

- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00444916
- `"Precondition"` @ 0x00444938

## DATA Context

**Context around 0x004448C4**:

- `",HD"` @ 0x0044484C
- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00444916
- `"Precondition"` @ 0x00444938

**Context around 0x004448E5**:

- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00444916
- `"Precondition"` @ 0x00444938
- `"a != NULL"` @ 0x00444945
- `"gdiobjec.cpp"` @ 0x0044494F
- `"Precondition"` @ 0x0044495C

**Context around 0x00444892**:

- `",HD"` @ 0x0044484C
- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2

**Context around 0x004448F2**:

- `"lette"` @ 0x00444872
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00444916
- `"Precondition"` @ 0x00444938
- `"a != NULL"` @ 0x00444945
- `"gdiobjec.cpp"` @ 0x0044494F
- `"Precondition"` @ 0x0044495C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00444969

**Context around 0x00444916**:

- `">= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444896
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00444916
- `"Precondition"` @ 0x00444938
- `"a != NULL"` @ 0x00444945
- `"gdiobjec.cpp"` @ 0x0044494F
- `"Precondition"` @ 0x0044495C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00444969
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044498E

**Context around 0x00444938**:

- `"ata.Limit()"` @ 0x004448B8
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00444916
- `"Precondition"` @ 0x00444938
- `"a != NULL"` @ 0x00444945
- `"gdiobjec.cpp"` @ 0x0044494F
- `"Precondition"` @ 0x0044495C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00444969
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044498E
- `"Precondition"` @ 0x004449B0

## Functions Called

- 0x00403618
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438EC8

---

*Extracted with recursive CALL following and DATA context*
