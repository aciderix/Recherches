# LoadFromINI Function Analysis

**Function Address**: 0x00405B50
**Rank**: #61
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 246

```assembly
00405B50  push     ebp
00405B51  mov      ebp, esp
00405B53  add      esp, -0x70
00405B56  push     ebx
00405B57  push     esi
00405B58  push     edi
00405B59  mov      ebx, dword ptr [ebp + 0xc]
00405B5C  mov      edi, dword ptr [ebp + 8]
00405B5F  lea      esi, [ebp - 0x3c]
00405B62  mov      eax, 0x43abd8
00405B67  call     0x403618
00405B6C  cmp      ebx, edi
00405B6E  jne      0x405b8c
00405B70  mov      eax, edi
00405B72  mov      edx, dword ptr [esi]
00405B74  mov      dword ptr fs:[0], edx
00405B7B  jmp      0x405e15
00405B80  jmp      0x405b8c
00405B82  cmp      dword ptr [edi + 0x19], 2
00405B86  je       0x405b8c
00405B88  xor      eax, eax
00405B8A  jmp      0x405b91
00405B8C  mov      eax, 1
00405B91  lea      edx, [edi + 4]
00405B94  mov      dword ptr [ebp - 0x40], edx
00405B97  push     0
00405B99  push     -1
00405B9B  push     eax
00405B9C  push     dword ptr [ebp - 0x40]
00405B9F  call     0x406ba2
00405BA4  add      esp, 0x10
00405BA7  mov      ecx, dword ptr [ebp - 0x40]
00405BAA  xor      eax, eax
00405BAC  mov      dword ptr [ecx + 0xd], eax
00405BAF  lea      edx, [ebx + 4]
00405BB2  push     edx
00405BB3  mov      ecx, dword ptr [ebx + 5]
00405BB6  call     dword ptr [ecx + 4]
00405BB9  pop      ecx
00405BBA  inc      eax
00405BBB  mov      dword ptr [ebp - 0x44], eax
00405BBE  mov      eax, dword ptr [edi]
00405BC0  cmp      eax, dword ptr [ebp - 0x44]
00405BC3  jle      0x405be3
00405BC5  mov      edx, dword ptr [ebp - 0x44]
00405BC8  sub      edx, dword ptr [edi]
00405BCA  add      edx, dword ptr [edi + 0xd]
00405BCD  mov      dword ptr [ebp - 0x48], edx
00405BD0  push     0
00405BD2  push     dword ptr [ebp - 0x48]
00405BD5  lea      ecx, [edi + 4]
00405BD8  push     ecx
00405BD9  call     0x406954
00405BDE  add      esp, 0xc
00405BE1  jmp      0x405c19
00405BE3  mov      eax, dword ptr [edi + 0xd]
00405BE6  mov      dword ptr [ebp - 0x4c], eax
00405BE9  cmp      dword ptr [ebp - 0x4c], -1
00405BED  jne      0x405bf6
00405BEF  mov      edx, 0x7fffffff
00405BF4  jmp      0x405bfb
00405BF6  mov      edx, dword ptr [edi]
00405BF8  add      edx, dword ptr [ebp - 0x4c]
00405BFB  cmp      edx, dword ptr [ebp - 0x44]
00405BFE  jg       0x405c19
00405C00  mov      eax, dword ptr [ebp - 0x44]
00405C03  sub      eax, dword ptr [edi]
00405C05  mov      dword ptr [ebp - 0x50], eax
00405C08  push     0
00405C0A  push     dword ptr [ebp - 0x50]
00405C0D  lea      ecx, [edi + 4]
00405C10  push     ecx
00405C11  call     0x406954
00405C16  add      esp, 0xc
00405C19  mov      eax, ebx
00405C1B  add      eax, 4
00405C1E  mov      dword ptr [ebp - 0x70], eax
00405C21  push     eax
00405C22  mov      edx, dword ptr [eax + 1]
00405C25  call     dword ptr [edx]
00405C27  pop      ecx
00405C28  xor      ecx, ecx
00405C2A  mov      dword ptr [ebp - 0x68], ecx
00405C2D  mov      dword ptr [ebp - 0x6c], ecx
00405C30  mov      dword ptr [ebp - 0x64], eax
00405C33  jmp      0x405dfe
00405C38  mov      eax, dword ptr [ebp - 0x6c]
00405C3B  cmp      eax, dword ptr [ebp - 0x64]
00405C3E  jb       0x405cb6
00405C40  push     esi
00405C41  push     0
00405C43  push     0
00405C45  push     0
00405C47  push     1
00405C49  push     0x403be0
00405C4E  push     0
00405C50  push     0x3db
00405C55  push     0x43b1b1
00405C5A  push     0x43b1a5
00405C5F  push     0x43b1d3
00405C64  lea      edx, [ebp - 4]
00405C67  push     edx
00405C68  call     0x438f10
00405C6D  add      esp, 0x14
00405C70  lea      eax, [ebp - 4]
00405C73  push     eax
00405C74  inc      dword ptr [esi + 0x1c]
00405C77  lea      edx, [ebp - 8]
00405C7A  push     edx
00405C7B  call     0x438de4
00405C80  add      esp, 8
00405C83  inc      dword ptr [esi + 0x1c]
00405C86  mov      word ptr [esi + 0x10], 0xc
00405C8C  dec      dword ptr [esi + 0x1c]
00405C8F  push     2
00405C91  lea      ecx, [ebp - 4]
00405C94  push     ecx
00405C95  call     0x438f64
00405C9A  add      esp, 8
00405C9D  add      dword ptr [esi + 0x1c], 2
00405CA1  add      dword ptr [esi + 0x1c], 3
00405CA5  lea      eax, [ebp - 8]
00405CA8  push     eax
00405CA9  push     0x403b88
00405CAE  call     0x438eaa
00405CB3  add      esp, 0x24
00405CB6  mov      edx, dword ptr [ebp - 0x6c]
00405CB9  mov      dword ptr [ebp - 0x58], edx
00405CBC  mov      ebx, dword ptr [ebp - 0x70]
00405CBF  cmp      dword ptr [ebx + 9], 0
00405CC3  jbe      0x405cd3
00405CC5  cmp      dword ptr [ebx + 5], 0
00405CC9  je       0x405cd3
00405CCB  mov      ecx, dword ptr [ebp - 0x58]
00405CCE  cmp      ecx, dword ptr [ebx + 9]
00405CD1  jb       0x405d49
00405CD3  push     esi
00405CD4  push     0
00405CD6  push     0
00405CD8  push     0
00405CDA  push     1
00405CDC  push     0x403be0
00405CE1  push     0
00405CE3  push     0x33a
00405CE8  push     0x43b204
00405CED  push     0x43b1e0
00405CF2  push     0x43b226
00405CF7  lea      eax, [ebp - 0xc]
00405CFA  push     eax
00405CFB  call     0x438f10
00405D00  add      esp, 0x14
00405D03  lea      edx, [ebp - 0xc]
00405D06  push     edx
00405D07  inc      dword ptr [esi + 0x1c]
00405D0A  lea      ecx, [ebp - 0x10]
00405D0D  push     ecx
00405D0E  call     0x438de4
00405D13  add      esp, 8
00405D16  inc      dword ptr [esi + 0x1c]
00405D19  mov      word ptr [esi + 0x10], 0x18
00405D1F  dec      dword ptr [esi + 0x1c]
00405D22  push     2
00405D24  lea      eax, [ebp - 0xc]
00405D27  push     eax
00405D28  call     0x438f64
00405D2D  add      esp, 8
00405D30  add      dword ptr [esi + 0x1c], 2
00405D34  add      dword ptr [esi + 0x1c], 3
00405D38  lea      edx, [ebp - 0x10]
00405D3B  push     edx
00405D3C  push     0x403b88
00405D41  call     0x438eaa
00405D46  add      esp, 0x24
00405D49  mov      ecx, dword ptr [ebp - 0x58]
00405D4C  shl      ecx, 2
00405D4F  add      ecx, dword ptr [ebx + 5]
00405D52  mov      eax, dword ptr [ecx]
00405D54  mov      dword ptr [ebp - 0x54], eax
00405D57  inc      dword ptr [ebp - 0x6c]
00405D5A  mov      edx, dword ptr [ebp - 0x54]
00405D5D  mov      ebx, edx
00405D5F  push     ebx
00405D60  mov      ecx, dword ptr [ebx]
00405D62  call     dword ptr [ecx + 8]
00405D65  pop      ecx
00405D66  test     al, al
00405D68  je       0x405dfe
00405D6E  push     0x10
00405D70  call     0x438eec
00405D75  pop      ecx
00405D76  mov      dword ptr [ebp - 0x14], eax
00405D79  test     eax, eax
00405D7B  je       0x405dc1
00405D7D  mov      word ptr [esi + 0x10], 0x30
00405D83  mov      dword ptr [ebp - 0x5c], ebx
00405D86  mov      edx, dword ptr [ebp - 0x14]
00405D89  mov      dword ptr [edx], 0x43b554
00405D8F  mov      ecx, dword ptr [ebp - 0x14]
00405D92  add      ecx, 4
00405D95  push     ecx
00405D96  call     0x438ec2
00405D9B  pop      ecx
00405D9C  inc      dword ptr [esi + 0x1c]
00405D9F  push     dword ptr [ebp - 0x14]
00405DA2  call     0x40573d
00405DA7  pop      ecx
00405DA8  push     dword ptr [ebp - 0x5c]
00405DAB  push     dword ptr [ebp - 0x14]
00405DAE  call     0x4057a9
00405DB3  add      esp, 8
00405DB6  mov      word ptr [esi + 0x10], 0x24
00405DBC  mov      eax, dword ptr [ebp - 0x14]
00405DBF  jmp      0x405dc4
00405DC1  mov      eax, dword ptr [ebp - 0x14]
00405DC4  mov      ebx, eax
00405DC6  mov      dword ptr [ebp - 0x60], ebx
00405DC9  push     dword ptr [ebp - 0x60]
00405DCC  lea      edx, [edi + 4]
00405DCF  push     edx
00405DD0  call     0x406a49
00405DD5  add      esp, 8
00405DD8  test     eax, eax
00405DDA  jne      0x405dfe
00405DDC  mov      dword ptr [ebp - 0x18], ebx
00405DDF  cmp      dword ptr [ebp - 0x18], 0
00405DE3  je       0x405dfe
00405DE5  mov      word ptr [esi + 0x10], 0x48
00405DEB  push     3
00405DED  mov      ecx, dword ptr [ebp - 0x18]
00405DF0  push     ecx
00405DF1  mov      eax, dword ptr [ecx]
00405DF3  call     dword ptr [eax]
00405DF5  add      esp, 8
00405DF8  mov      word ptr [esi + 0x10], 0x3c
00405DFE  mov      edx, dword ptr [ebp - 0x6c]
00405E01  cmp      edx, dword ptr [ebp - 0x64]
00405E04  jb       0x405c38
00405E0A  mov      eax, edi
00405E0C  mov      edx, dword ptr [esi]
00405E0E  mov      dword ptr fs:[0], edx
00405E15  pop      edi
00405E16  pop      esi
00405E17  pop      ebx
00405E18  mov      esp, ebp
00405E1A  pop      ebp
00405E1B  ret      
```

## Strings Referenced

**Total unique strings**: 10

- `"Cur < Upper"` @ 0x0043B1A5
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B1B1
- `"Precondition"` @ 0x0043B1D3
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B1E0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B204
- `"Precondition"` @ 0x0043B226
- `"-m@"` @ 0x0043B554
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## DATA Context

**Context around 0x0043B1E0**:

- `"%li"` @ 0x0043B19D
- `"%lu"` @ 0x0043B1A1
- `"Cur < Upper"` @ 0x0043B1A5
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B1B1
- `"Precondition"` @ 0x0043B1D3
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B1E0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B204
- `"Precondition"` @ 0x0043B226
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B233

**Context around 0x0044EB41**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD

**Context around 0x0043B204**:

- `"%li"` @ 0x0043B19D
- `"%lu"` @ 0x0043B1A1
- `"Cur < Upper"` @ 0x0043B1A5
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B1B1
- `"Precondition"` @ 0x0043B1D3
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B1E0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B204
- `"Precondition"` @ 0x0043B226
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B233
- `"C:\BC5\INCLUDE\classlib\arrays.h"` @ 0x0043B265

**Context around 0x0043B1A5**:

- `"%li"` @ 0x0043B19D
- `"%lu"` @ 0x0043B1A1
- `"Cur < Upper"` @ 0x0043B1A5
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B1B1
- `"Precondition"` @ 0x0043B1D3
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B1E0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B204

**Context around 0x0043B226**:

- `"ur < Upper"` @ 0x0043B1A6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B1B1
- `"Precondition"` @ 0x0043B1D3
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B1E0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B204
- `"Precondition"` @ 0x0043B226
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B233
- `"C:\BC5\INCLUDE\classlib\arrays.h"` @ 0x0043B265
- `"Precondition"` @ 0x0043B286
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B293

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

**Context around 0x0043B1B1**:

- `"%li"` @ 0x0043B19D
- `"%lu"` @ 0x0043B1A1
- `"Cur < Upper"` @ 0x0043B1A5
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B1B1
- `"Precondition"` @ 0x0043B1D3
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B1E0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B204
- `"Precondition"` @ 0x0043B226

**Context around 0x0043B1D3**:

- `"%li"` @ 0x0043B19D
- `"%lu"` @ 0x0043B1A1
- `"Cur < Upper"` @ 0x0043B1A5
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B1B1
- `"Precondition"` @ 0x0043B1D3
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043B1E0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043B204
- `"Precondition"` @ 0x0043B226
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043B233

**Context around 0x0043B554**:

- `"condition"` @ 0x0043B4D4
- `"P[@"` @ 0x0043B4EC
- `"cZ@"` @ 0x0043B4F0
- `"+l@"` @ 0x0043B528
- `"+l@"` @ 0x0043B544
- `"1h@"` @ 0x0043B548
- `"-m@"` @ 0x0043B554
- `"%<@"` @ 0x0043B560
- `"i<@"` @ 0x0043B57C
- `"%<@"` @ 0x0043B5AC
- `"%<@"` @ 0x0043B5C4

## Functions Called

- 0x00403618
- 0x00406BA2
- 0x00406954
- 0x00406954
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438EEC
- 0x00438EC2
- 0x0040573D
- 0x004057A9
- 0x00406A49

---

*Extracted with recursive CALL following and DATA context*
