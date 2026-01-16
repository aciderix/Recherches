# LoadFromINI Function Analysis

**Function Address**: 0x00413B20
**Rank**: #131
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 156

```assembly
00413B20  push     ebp
00413B21  mov      ebp, esp
00413B23  add      esp, -0x3c
00413B26  push     ebx
00413B27  push     esi
00413B28  push     edi
00413B29  mov      ebx, dword ptr [ebp + 8]
00413B2C  mov      eax, 0x440b5c
00413B31  call     0x403618
00413B36  push     ebx
00413B37  mov      edx, dword ptr [ebx + 0x25]
00413B3A  call     dword ptr [edx + 8]
00413B3D  pop      ecx
00413B3E  mov      dword ptr [ebp - 0x38], eax
00413B41  jmp      0x413cb6
00413B46  mov      edi, dword ptr [ebp - 0x38]
00413B49  cmp      edi, dword ptr [ebx]
00413B4B  jl       0x413b56
00413B4D  mov      ecx, edi
00413B4F  sub      ecx, dword ptr [ebx]
00413B51  cmp      ecx, dword ptr [ebx + 0xd]
00413B54  jb       0x413bcf
00413B56  lea      eax, [ebp - 0x34]
00413B59  push     eax
00413B5A  push     0
00413B5C  push     0
00413B5E  push     0
00413B60  push     1
00413B62  push     0x403be0
00413B67  push     0
00413B69  push     0x15e
00413B6E  push     0x44159d
00413B73  push     0x44156b
00413B78  push     0x4415be
00413B7D  lea      edx, [ebp - 4]
00413B80  push     edx
00413B81  call     0x438f10
00413B86  add      esp, 0x14
00413B89  lea      ecx, [ebp - 4]
00413B8C  push     ecx
00413B8D  inc      dword ptr [ebp - 0x18]
00413B90  lea      eax, [ebp - 8]
00413B93  push     eax
00413B94  call     0x438de4
00413B99  add      esp, 8
00413B9C  inc      dword ptr [ebp - 0x18]
00413B9F  mov      word ptr [ebp - 0x24], 0xc
00413BA5  dec      dword ptr [ebp - 0x18]
00413BA8  push     2
00413BAA  lea      edx, [ebp - 4]
00413BAD  push     edx
00413BAE  call     0x438f64
00413BB3  add      esp, 8
00413BB6  add      dword ptr [ebp - 0x18], 2
00413BBA  add      dword ptr [ebp - 0x18], 3
00413BBE  lea      ecx, [ebp - 8]
00413BC1  push     ecx
00413BC2  push     0x403b88
00413BC7  call     0x438eaa
00413BCC  add      esp, 0x24
00413BCF  sub      edi, dword ptr [ebx]
00413BD1  mov      dword ptr [ebp - 0x3c], edi
00413BD4  lea      esi, [ebx + 4]
00413BD7  cmp      dword ptr [esi + 9], 0
00413BDB  jbe      0x413beb
00413BDD  cmp      dword ptr [esi + 5], 0
00413BE1  je       0x413beb
00413BE3  mov      eax, dword ptr [ebp - 0x3c]
00413BE6  cmp      eax, dword ptr [esi + 9]
00413BE9  jb       0x413c64
00413BEB  lea      edx, [ebp - 0x34]
00413BEE  push     edx
00413BEF  push     0
00413BF1  push     0
00413BF3  push     0
00413BF5  push     1
00413BF7  push     0x403be0
00413BFC  push     0
00413BFE  push     0x33a
00413C03  push     0x4415ef
00413C08  push     0x4415cb
00413C0D  push     0x441611
00413C12  lea      ecx, [ebp - 0xc]
00413C15  push     ecx
00413C16  call     0x438f10
00413C1B  add      esp, 0x14
00413C1E  lea      eax, [ebp - 0xc]
00413C21  push     eax
00413C22  inc      dword ptr [ebp - 0x18]
00413C25  lea      edx, [ebp - 0x10]
00413C28  push     edx
00413C29  call     0x438de4
00413C2E  add      esp, 8
00413C31  inc      dword ptr [ebp - 0x18]
00413C34  mov      word ptr [ebp - 0x24], 0x18
00413C3A  dec      dword ptr [ebp - 0x18]
00413C3D  push     2
00413C3F  lea      ecx, [ebp - 0xc]
00413C42  push     ecx
00413C43  call     0x438f64
00413C48  add      esp, 8
00413C4B  add      dword ptr [ebp - 0x18], 2
00413C4F  add      dword ptr [ebp - 0x18], 3
00413C53  lea      eax, [ebp - 0x10]
00413C56  push     eax
00413C57  push     0x403b88
00413C5C  call     0x438eaa
00413C61  add      esp, 0x24
00413C64  mov      edx, dword ptr [ebp - 0x3c]
00413C67  shl      edx, 2
00413C6A  add      edx, dword ptr [esi + 5]
00413C6D  mov      esi, dword ptr [edx]
00413C6F  push     dword ptr [ebp + 0x18]
00413C72  push     dword ptr [ebp + 0x14]
00413C75  add      esp, -8
00413C78  mov      eax, dword ptr [ebp + 0x10]
00413C7B  mov      edx, dword ptr [eax]
00413C7D  mov      dword ptr [esp], edx
00413C80  mov      eax, dword ptr [eax + 4]
00413C83  mov      dword ptr [esp + 4], eax
00413C87  push     dword ptr [ebp + 0xc]
00413C8A  push     esi
00413C8B  mov      ecx, dword ptr [esi]
00413C8D  call     dword ptr [ecx + 0x18]
00413C90  add      esp, 0x18
00413C93  test     al, al
00413C95  je       0x413cb3
00413C97  cmp      dword ptr [ebp + 0x1c], 0
00413C9B  je       0x413ca5
00413C9D  mov      eax, dword ptr [ebp + 0x1c]
00413CA0  mov      edx, dword ptr [ebp - 0x38]
00413CA3  mov      dword ptr [eax], edx
00413CA5  mov      eax, esi
00413CA7  mov      edx, dword ptr [ebp - 0x34]
00413CAA  mov      dword ptr fs:[0], edx
00413CB1  jmp      0x413ce2
00413CB3  inc      dword ptr [ebp - 0x38]
00413CB6  push     ebx
00413CB7  mov      ecx, dword ptr [ebx + 0x25]
00413CBA  call     dword ptr [ecx + 0xc]
00413CBD  pop      ecx
00413CBE  cmp      eax, dword ptr [ebp - 0x38]
00413CC1  jge      0x413b46
00413CC7  cmp      dword ptr [ebp + 0x1c], 0
00413CCB  je       0x413cd6
00413CCD  mov      eax, dword ptr [ebp + 0x1c]
00413CD0  mov      dword ptr [eax], 0x7fffffff
00413CD6  xor      eax, eax
00413CD8  mov      edx, dword ptr [ebp - 0x34]
00413CDB  mov      dword ptr fs:[0], edx
00413CE2  pop      edi
00413CE3  pop      esi
00413CE4  pop      ebx
00413CE5  mov      esp, ebp
00413CE7  pop      ebp
00413CE8  ret      
```

## Strings Referenced

**Total unique strings**: 6

- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D
- `"Precondition"` @ 0x004415BE
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004415CB
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004415EF
- `"Precondition"` @ 0x00441611

## DATA Context

**Context around 0x0044156B**:

- `"\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004414EB
- `"Precondition"` @ 0x0044150B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441518
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D
- `"Precondition"` @ 0x004415BE
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004415CB

**Context around 0x004415CB**:

- `"classlib/vectimp.h"` @ 0x0044154B
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D
- `"Precondition"` @ 0x004415BE
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004415CB
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004415EF
- `"Precondition"` @ 0x00441611
- `"HSNUM"` @ 0x0044161E
- `"NHOTSPOT"` @ 0x00441624
- `"Lim == 0 || (Data != 0 && v.Data != 0)"` @ 0x0044162D

**Context around 0x004415EF**:

- `">= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156F
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D
- `"Precondition"` @ 0x004415BE
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004415CB
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004415EF
- `"Precondition"` @ 0x00441611
- `"HSNUM"` @ 0x0044161E
- `"NHOTSPOT"` @ 0x00441624
- `"Lim == 0 || (Data != 0 && v.Data != 0)"` @ 0x0044162D
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00441654

**Context around 0x00441611**:

- `"ata.Limit()"` @ 0x00441591
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D
- `"Precondition"` @ 0x004415BE
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004415CB
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004415EF
- `"Precondition"` @ 0x00441611
- `"HSNUM"` @ 0x0044161E
- `"NHOTSPOT"` @ 0x00441624
- `"Lim == 0 || (Data != 0 && v.Data != 0)"` @ 0x0044162D
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00441654
- `"Precondition"` @ 0x00441676
- `"Data != 0"` @ 0x00441683
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044168D

**Context around 0x0044159D**:

- `" 0 && Data != 0 && index < Lim"` @ 0x0044151D
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153C
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D
- `"Precondition"` @ 0x004415BE
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004415CB
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004415EF
- `"Precondition"` @ 0x00441611

**Context around 0x004415BE**:

- `"\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044153E
- `"Precondition"` @ 0x0044155E
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0044156B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0044159D
- `"Precondition"` @ 0x004415BE
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004415CB
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004415EF
- `"Precondition"` @ 0x00441611
- `"HSNUM"` @ 0x0044161E
- `"NHOTSPOT"` @ 0x00441624
- `"Lim == 0 || (Data != 0 && v.Data != 0)"` @ 0x0044162D

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

---

*Extracted with recursive CALL following and DATA context*
