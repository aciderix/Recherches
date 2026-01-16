# LoadFromINI Function Analysis

**Function Address**: 0x0040D8A9
**Rank**: #64
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 176

```assembly
0040D8A9  push     ebp
0040D8AA  mov      ebp, esp
0040D8AC  add      esp, -0x4c
0040D8AF  push     ebx
0040D8B0  push     esi
0040D8B1  push     edi
0040D8B2  mov      ebx, dword ptr [ebp + 0xc]
0040D8B5  mov      edi, dword ptr [ebp + 8]
0040D8B8  mov      eax, 0x43e9e6
0040D8BD  call     0x403618
0040D8C2  cmp      ebx, edi
0040D8C4  jne      0x40d8d7
0040D8C6  mov      eax, edi
0040D8C8  mov      edx, dword ptr [ebp - 0x34]
0040D8CB  mov      dword ptr fs:[0], edx
0040D8D2  jmp      0x40daa2
0040D8D7  lea      eax, [edi + 4]
0040D8DA  xor      edx, edx
0040D8DC  mov      dword ptr [eax + 0xd], edx
0040D8DF  lea      ecx, [ebx + 4]
0040D8E2  push     ecx
0040D8E3  mov      eax, dword ptr [ebx + 5]
0040D8E6  call     dword ptr [eax + 4]
0040D8E9  pop      ecx
0040D8EA  mov      dword ptr [ebp - 0x38], eax
0040D8ED  mov      esi, dword ptr [ebp - 0x38]
0040D8F0  inc      esi
0040D8F1  cmp      esi, dword ptr [edi]
0040D8F3  jge      0x40d910
0040D8F5  sub      esi, dword ptr [edi]
0040D8F7  add      esi, dword ptr [edi + 0xd]
0040D8FA  mov      dword ptr [ebp - 0x3c], esi
0040D8FD  push     0
0040D8FF  push     dword ptr [ebp - 0x3c]
0040D902  lea      eax, [edi + 4]
0040D905  push     eax
0040D906  call     0x40f7b9
0040D90B  add      esp, 0xc
0040D90E  jmp      0x40d942
0040D910  mov      edx, dword ptr [edi + 0xd]
0040D913  mov      dword ptr [ebp - 0x40], edx
0040D916  cmp      dword ptr [ebp - 0x40], -1
0040D91A  jne      0x40d923
0040D91C  mov      ecx, 0x7fffffff
0040D921  jmp      0x40d928
0040D923  mov      ecx, dword ptr [edi]
0040D925  add      ecx, dword ptr [ebp - 0x40]
0040D928  cmp      esi, ecx
0040D92A  jl       0x40d942
0040D92C  sub      esi, dword ptr [edi]
0040D92E  mov      dword ptr [ebp - 0x44], esi
0040D931  push     0
0040D933  push     dword ptr [ebp - 0x44]
0040D936  lea      eax, [edi + 4]
0040D939  push     eax
0040D93A  call     0x40f7b9
0040D93F  add      esp, 0xc
0040D942  xor      edx, edx
0040D944  mov      dword ptr [ebp - 0x48], edx
0040D947  mov      eax, dword ptr [ebp - 0x48]
0040D94A  cmp      eax, dword ptr [ebp - 0x38]
0040D94D  jae      0x40da96
0040D953  mov      esi, dword ptr [ebp - 0x48]
0040D956  cmp      esi, dword ptr [ebx]
0040D958  jl       0x40d963
0040D95A  mov      eax, esi
0040D95C  sub      eax, dword ptr [ebx]
0040D95E  cmp      eax, dword ptr [ebx + 0xd]
0040D961  jb       0x40d9dc
0040D963  lea      edx, [ebp - 0x34]
0040D966  push     edx
0040D967  push     0
0040D969  push     0
0040D96B  push     0
0040D96D  push     1
0040D96F  push     0x403be0
0040D974  push     0
0040D976  push     0xda
0040D97B  push     0x43fbfa
0040D980  push     0x43fbc8
0040D985  push     0x43fc1b
0040D98A  lea      ecx, [ebp - 4]
0040D98D  push     ecx
0040D98E  call     0x438f10
0040D993  add      esp, 0x14
0040D996  lea      eax, [ebp - 4]
0040D999  push     eax
0040D99A  inc      dword ptr [ebp - 0x18]
0040D99D  lea      edx, [ebp - 8]
0040D9A0  push     edx
0040D9A1  call     0x438de4
0040D9A6  add      esp, 8
0040D9A9  inc      dword ptr [ebp - 0x18]
0040D9AC  mov      word ptr [ebp - 0x24], 0xc
0040D9B2  dec      dword ptr [ebp - 0x18]
0040D9B5  push     2
0040D9B7  lea      ecx, [ebp - 4]
0040D9BA  push     ecx
0040D9BB  call     0x438f64
0040D9C0  add      esp, 8
0040D9C3  add      dword ptr [ebp - 0x18], 2
0040D9C7  add      dword ptr [ebp - 0x18], 3
0040D9CB  lea      eax, [ebp - 8]
0040D9CE  push     eax
0040D9CF  push     0x403b88
0040D9D4  call     0x438eaa
0040D9D9  add      esp, 0x24
0040D9DC  sub      esi, dword ptr [ebx]
0040D9DE  mov      dword ptr [ebp - 0x4c], esi
0040D9E1  lea      esi, [ebx + 4]
0040D9E4  cmp      dword ptr [esi + 9], 0
0040D9E8  jbe      0x40d9f8
0040D9EA  cmp      dword ptr [esi + 5], 0
0040D9EE  je       0x40d9f8
0040D9F0  mov      eax, dword ptr [ebp - 0x4c]
0040D9F3  cmp      eax, dword ptr [esi + 9]
0040D9F6  jb       0x40da71
0040D9F8  lea      edx, [ebp - 0x34]
0040D9FB  push     edx
0040D9FC  push     0
0040D9FE  push     0
0040DA00  push     0
0040DA02  push     1
0040DA04  push     0x403be0
0040DA09  push     0
0040DA0B  push     0xc7
0040DA10  push     0x43fc4c
0040DA15  push     0x43fc28
0040DA1A  push     0x43fc6e
0040DA1F  lea      ecx, [ebp - 0xc]
0040DA22  push     ecx
0040DA23  call     0x438f10
0040DA28  add      esp, 0x14
0040DA2B  lea      eax, [ebp - 0xc]
0040DA2E  push     eax
0040DA2F  inc      dword ptr [ebp - 0x18]
0040DA32  lea      edx, [ebp - 0x10]
0040DA35  push     edx
0040DA36  call     0x438de4
0040DA3B  add      esp, 8
0040DA3E  inc      dword ptr [ebp - 0x18]
0040DA41  mov      word ptr [ebp - 0x24], 0x18
0040DA47  dec      dword ptr [ebp - 0x18]
0040DA4A  push     2
0040DA4C  lea      ecx, [ebp - 0xc]
0040DA4F  push     ecx
0040DA50  call     0x438f64
0040DA55  add      esp, 8
0040DA58  add      dword ptr [ebp - 0x18], 2
0040DA5C  add      dword ptr [ebp - 0x18], 3
0040DA60  lea      eax, [ebp - 0x10]
0040DA63  push     eax
0040DA64  push     0x403b88
0040DA69  call     0x438eaa
0040DA6E  add      esp, 0x24
0040DA71  mov      eax, dword ptr [ebp - 0x4c]
0040DA74  shl      eax, 4
0040DA77  add      eax, dword ptr [esi + 5]
0040DA7A  push     eax
0040DA7B  lea      edx, [edi + 4]
0040DA7E  push     edx
0040DA7F  call     0x40f706
0040DA84  add      esp, 8
0040DA87  inc      dword ptr [ebp - 0x48]
0040DA8A  mov      ecx, dword ptr [ebp - 0x48]
0040DA8D  cmp      ecx, dword ptr [ebp - 0x38]
0040DA90  jb       0x40d953
0040DA96  mov      eax, edi
0040DA98  mov      edx, dword ptr [ebp - 0x34]
0040DA9B  mov      dword ptr fs:[0], edx
0040DAA2  pop      edi
0040DAA3  pop      esi
0040DAA4  pop      ebx
0040DAA5  mov      esp, ebp
0040DAA7  pop      ebp
0040DAA8  ret      
```

## Strings Referenced

**Total unique strings**: 10

- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FBC8
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FBFA
- `"Precondition"` @ 0x0043FC1B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FC28
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E
- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
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

**Context around 0x0043FBC8**:

- `"indow.h"` @ 0x0043FB48
- `"Precondition"` @ 0x0043FB50
- `"GetHandle()"` @ 0x0043FB5D
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0043FB69
- `"Precondition"` @ 0x0043FB85
- `"GetHandle()"` @ 0x0043FB92
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0043FB9E
- `"Precondition"` @ 0x0043FBBA
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FBC8
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FBFA
- `"Precondition"` @ 0x0043FC1B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FC28

**Context around 0x0043FC28**:

- `"LUDE\owl/window.h"` @ 0x0043FBA8
- `"Precondition"` @ 0x0043FBBA
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FBC8
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FBFA
- `"Precondition"` @ 0x0043FC1B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FC28
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E
- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87

**Context around 0x0043FC4C**:

- `">= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FBCC
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FBFA
- `"Precondition"` @ 0x0043FC1B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FC28
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E
- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87
- `"Precondition"` @ 0x0043FCA9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FCB6

**Context around 0x0043FC6E**:

- `"ata.Limit()"` @ 0x0043FBEE
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FBFA
- `"Precondition"` @ 0x0043FC1B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FC28
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E
- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87
- `"Precondition"` @ 0x0043FCA9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FCB6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FCDA

**Context around 0x0044EAD0**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41

**Context around 0x0043FBFA**:

- `"l/window.h"` @ 0x0043FB7A
- `"Precondition"` @ 0x0043FB85
- `"GetHandle()"` @ 0x0043FB92
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0043FB9E
- `"Precondition"` @ 0x0043FBBA
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FBC8
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FBFA
- `"Precondition"` @ 0x0043FC1B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FC28
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E

**Context around 0x0043FC1B**:

- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0043FB9E
- `"Precondition"` @ 0x0043FBBA
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FBC8
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FBFA
- `"Precondition"` @ 0x0043FC1B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FC28
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E
- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87

## Functions Called

- 0x00403618
- 0x0040F7B9
- 0x0040F7B9
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x0040F706

---

*Extracted with recursive CALL following and DATA context*
