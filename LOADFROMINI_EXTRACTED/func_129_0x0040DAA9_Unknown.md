# LoadFromINI Function Analysis

**Function Address**: 0x0040DAA9
**Rank**: #129
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 127

```assembly
0040DAA9  push     ebp
0040DAAA  mov      ebp, esp
0040DAAC  add      esp, -0x44
0040DAAF  push     ebx
0040DAB0  push     esi
0040DAB1  push     edi
0040DAB2  mov      ebx, dword ptr [ebp + 8]
0040DAB5  lea      edi, [ebp - 0x34]
0040DAB8  mov      eax, 0x43ea66
0040DABD  call     0x403618
0040DAC2  mov      eax, ebx
0040DAC4  add      eax, 4
0040DAC7  mov      dword ptr [ebp - 0x44], eax
0040DACA  push     eax
0040DACB  mov      edx, dword ptr [eax + 1]
0040DACE  call     dword ptr [edx]
0040DAD0  pop      ecx
0040DAD1  xor      ecx, ecx
0040DAD3  mov      dword ptr [ebp - 0x3c], ecx
0040DAD6  mov      dword ptr [ebp - 0x40], ecx
0040DAD9  mov      dword ptr [ebp - 0x38], eax
0040DADC  jmp      0x40dc03
0040DAE1  mov      eax, dword ptr [ebp - 0x40]
0040DAE4  cmp      eax, dword ptr [ebp - 0x38]
0040DAE7  jb       0x40db5f
0040DAE9  push     edi
0040DAEA  push     0
0040DAEC  push     0
0040DAEE  push     0
0040DAF0  push     1
0040DAF2  push     0x403be0
0040DAF7  push     0
0040DAF9  push     0x13f
0040DAFE  push     0x43fc87
0040DB03  push     0x43fc7b
0040DB08  push     0x43fca9
0040DB0D  lea      edx, [ebp - 4]
0040DB10  push     edx
0040DB11  call     0x438f10
0040DB16  add      esp, 0x14
0040DB19  lea      eax, [ebp - 4]
0040DB1C  push     eax
0040DB1D  inc      dword ptr [edi + 0x1c]
0040DB20  lea      edx, [ebp - 8]
0040DB23  push     edx
0040DB24  call     0x438de4
0040DB29  add      esp, 8
0040DB2C  inc      dword ptr [edi + 0x1c]
0040DB2F  mov      word ptr [edi + 0x10], 0xc
0040DB35  dec      dword ptr [edi + 0x1c]
0040DB38  push     2
0040DB3A  lea      ecx, [ebp - 4]
0040DB3D  push     ecx
0040DB3E  call     0x438f64
0040DB43  add      esp, 8
0040DB46  add      dword ptr [edi + 0x1c], 2
0040DB4A  add      dword ptr [edi + 0x1c], 3
0040DB4E  lea      eax, [ebp - 8]
0040DB51  push     eax
0040DB52  push     0x403b88
0040DB57  call     0x438eaa
0040DB5C  add      esp, 0x24
0040DB5F  mov      esi, dword ptr [ebp - 0x40]
0040DB62  mov      ebx, dword ptr [ebp - 0x44]
0040DB65  cmp      dword ptr [ebx + 9], 0
0040DB69  jbe      0x40db76
0040DB6B  cmp      dword ptr [ebx + 5], 0
0040DB6F  je       0x40db76
0040DB71  cmp      esi, dword ptr [ebx + 9]
0040DB74  jb       0x40dbec
0040DB76  push     edi
0040DB77  push     0
0040DB79  push     0
0040DB7B  push     0
0040DB7D  push     1
0040DB7F  push     0x403be0
0040DB84  push     0
0040DB86  push     0xc7
0040DB8B  push     0x43fcda
0040DB90  push     0x43fcb6
0040DB95  push     0x43fcfc
0040DB9A  lea      edx, [ebp - 0xc]
0040DB9D  push     edx
0040DB9E  call     0x438f10
0040DBA3  add      esp, 0x14
0040DBA6  lea      ecx, [ebp - 0xc]
0040DBA9  push     ecx
0040DBAA  inc      dword ptr [edi + 0x1c]
0040DBAD  lea      eax, [ebp - 0x10]
0040DBB0  push     eax
0040DBB1  call     0x438de4
0040DBB6  add      esp, 8
0040DBB9  inc      dword ptr [edi + 0x1c]
0040DBBC  mov      word ptr [edi + 0x10], 0x18
0040DBC2  dec      dword ptr [edi + 0x1c]
0040DBC5  push     2
0040DBC7  lea      edx, [ebp - 0xc]
0040DBCA  push     edx
0040DBCB  call     0x438f64
0040DBD0  add      esp, 8
0040DBD3  add      dword ptr [edi + 0x1c], 2
0040DBD7  add      dword ptr [edi + 0x1c], 3
0040DBDB  lea      ecx, [ebp - 0x10]
0040DBDE  push     ecx
0040DBDF  push     0x403b88
0040DBE4  call     0x438eaa
0040DBE9  add      esp, 0x24
0040DBEC  mov      eax, esi
0040DBEE  shl      eax, 4
0040DBF1  add      eax, dword ptr [ebx + 5]
0040DBF4  inc      dword ptr [ebp - 0x40]
0040DBF7  push     dword ptr [ebp + 0xc]
0040DBFA  push     eax
0040DBFB  mov      edx, dword ptr [eax]
0040DBFD  call     dword ptr [edx + 0xc]
0040DC00  add      esp, 8
0040DC03  mov      ecx, dword ptr [ebp - 0x40]
0040DC06  cmp      ecx, dword ptr [ebp - 0x38]
0040DC09  jb       0x40dae1
0040DC0F  mov      eax, dword ptr [edi]
0040DC11  mov      dword ptr fs:[0], eax
0040DC17  pop      edi
0040DC18  pop      esi
0040DC19  pop      ebx
0040DC1A  mov      esp, ebp
0040DC1C  pop      ebp
0040DC1D  ret      
```

## Strings Referenced

**Total unique strings**: 6

- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87
- `"Precondition"` @ 0x0043FCA9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FCB6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FCDA
- `"Precondition"` @ 0x0043FCFC

## DATA Context

**Context around 0x0043FC87**:

- `"E\classlib/arrays.h"` @ 0x0043FC07
- `"Precondition"` @ 0x0043FC1B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FC28
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E
- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87
- `"Precondition"` @ 0x0043FCA9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FCB6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FCDA
- `"Precondition"` @ 0x0043FCFC

**Context around 0x0043FCA9**:

- `"im > 0 && Data != 0 && index < Lim"` @ 0x0043FC29
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E
- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87
- `"Precondition"` @ 0x0043FCA9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FCB6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FCDA
- `"Precondition"` @ 0x0043FCFC
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FD0B

**Context around 0x0043FCB6**:

- `"a != 0 && index < Lim"` @ 0x0043FC36
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E
- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87
- `"Precondition"` @ 0x0043FCA9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FCB6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FCDA
- `"Precondition"` @ 0x0043FCFC
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FD0B

**Context around 0x0043FCDA**:

- `"\classlib/vectimp.h"` @ 0x0043FC5A
- `"Precondition"` @ 0x0043FC6E
- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87
- `"Precondition"` @ 0x0043FCA9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FCB6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FCDA
- `"Precondition"` @ 0x0043FCFC
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FD0B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FD3D

**Context around 0x0043FC7B**:

- `":\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FBFB
- `"Precondition"` @ 0x0043FC1B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FC28
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC4C
- `"Precondition"` @ 0x0043FC6E
- `"Cur < Upper"` @ 0x0043FC7B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87
- `"Precondition"` @ 0x0043FCA9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FCB6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FCDA

**Context around 0x0043FCFC**:

- `"ur < Upper"` @ 0x0043FC7C
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FC87
- `"Precondition"` @ 0x0043FCA9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FCB6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0043FCDA
- `"Precondition"` @ 0x0043FCFC
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x0043FD0B
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x0043FD3D
- `"Precondition"` @ 0x0043FD5E
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0043FD6B

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
