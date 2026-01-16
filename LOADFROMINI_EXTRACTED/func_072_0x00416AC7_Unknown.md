# LoadFromINI Function Analysis

**Function Address**: 0x00416AC7
**Rank**: #72
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 414

```assembly
00416AC7  push     ebp
00416AC8  mov      ebp, esp
00416ACA  add      esp, -0x74
00416ACD  push     ebx
00416ACE  push     esi
00416ACF  push     edi
00416AD0  lea      edi, [ebp - 0x38]
00416AD3  mov      eax, 0x441ed4
00416AD8  call     0x403618
00416ADD  mov      edx, dword ptr [ebp + 8]
00416AE0  cmp      edx, dword ptr [ebp + 0xc]
00416AE3  jne      0x416af6
00416AE5  mov      eax, dword ptr [ebp + 8]
00416AE8  mov      edx, dword ptr [edi]
00416AEA  mov      dword ptr fs:[0], edx
00416AF1  jmp      0x416fc6
00416AF6  push     dword ptr [ebp + 8]
00416AF9  call     0x416fcd
00416AFE  pop      ecx
00416AFF  mov      ecx, dword ptr [ebp + 0xc]
00416B02  add      ecx, 4
00416B05  push     ecx
00416B06  mov      eax, dword ptr [ebp + 0xc]
00416B09  mov      edx, dword ptr [eax + 5]
00416B0C  call     dword ptr [edx + 4]
00416B0F  pop      ecx
00416B10  mov      ebx, eax
00416B12  inc      ebx
00416B13  mov      eax, dword ptr [ebp + 8]
00416B16  cmp      ebx, dword ptr [eax]
00416B18  jge      0x416b3e
00416B1A  mov      edx, dword ptr [ebp + 8]
00416B1D  sub      ebx, dword ptr [edx]
00416B1F  mov      ecx, dword ptr [ebp + 8]
00416B22  add      ebx, dword ptr [ecx + 0xd]
00416B25  mov      dword ptr [ebp - 0x3c], ebx
00416B28  push     0
00416B2A  push     dword ptr [ebp - 0x3c]
00416B2D  mov      eax, dword ptr [ebp + 8]
00416B30  add      eax, 4
00416B33  push     eax
00416B34  call     0x406954
00416B39  add      esp, 0xc
00416B3C  jmp      0x416b77
00416B3E  mov      edx, dword ptr [ebp + 8]
00416B41  mov      esi, dword ptr [edx + 0xd]
00416B44  cmp      esi, -1
00416B47  jne      0x416b50
00416B49  mov      ecx, 0x7fffffff
00416B4E  jmp      0x416b57
00416B50  mov      eax, dword ptr [ebp + 8]
00416B53  mov      ecx, dword ptr [eax]
00416B55  add      ecx, esi
00416B57  cmp      ebx, ecx
00416B59  jl       0x416b77
00416B5B  mov      edx, dword ptr [ebp + 8]
00416B5E  sub      ebx, dword ptr [edx]
00416B60  mov      dword ptr [ebp - 0x40], ebx
00416B63  push     0
00416B65  push     dword ptr [ebp - 0x40]
00416B68  mov      eax, dword ptr [ebp + 8]
00416B6B  add      eax, 4
00416B6E  push     eax
00416B6F  call     0x406954
00416B74  add      esp, 0xc
00416B77  mov      eax, dword ptr [ebp + 0xc]
00416B7A  add      eax, 4
00416B7D  mov      dword ptr [ebp - 0x74], eax
00416B80  push     eax
00416B81  mov      edx, dword ptr [eax + 1]
00416B84  call     dword ptr [edx]
00416B86  pop      ecx
00416B87  xor      ecx, ecx
00416B89  mov      dword ptr [ebp - 0x6c], ecx
00416B8C  mov      dword ptr [ebp - 0x70], ecx
00416B8F  mov      dword ptr [ebp - 0x68], eax
00416B92  jmp      0x416eec
00416B97  push     0x99
00416B9C  call     0x438eec
00416BA1  pop      ecx
00416BA2  mov      dword ptr [ebp - 0x14], eax
00416BA5  test     eax, eax
00416BA7  je       0x416ed9
00416BAD  mov      word ptr [edi + 0x10], 0x14
00416BB3  mov      edx, dword ptr [ebp - 0x70]
00416BB6  cmp      edx, dword ptr [ebp - 0x68]
00416BB9  jb       0x416c37
00416BBB  push     edi
00416BBC  push     0
00416BBE  push     0
00416BC0  push     0
00416BC2  push     1
00416BC4  push     0x403be0
00416BC9  push     0
00416BCB  push     0x3db
00416BD0  push     0x442a61
00416BD5  push     0x442a55
00416BDA  push     0x442a83
00416BDF  lea      eax, [ebp - 4]
00416BE2  push     eax
00416BE3  call     0x438f10
00416BE8  add      esp, 0x14
00416BEB  lea      edx, [ebp - 4]
00416BEE  push     edx
00416BEF  inc      dword ptr [edi + 0x1c]
00416BF2  lea      ecx, [ebp - 8]
00416BF5  push     ecx
00416BF6  call     0x438de4
00416BFB  add      esp, 8
00416BFE  inc      dword ptr [edi + 0x1c]
00416C01  mov      word ptr [edi + 0x10], 0x20
00416C07  dec      dword ptr [edi + 0x1c]
00416C0A  push     2
00416C0C  lea      eax, [ebp - 4]
00416C0F  push     eax
00416C10  call     0x438f64
00416C15  add      esp, 8
00416C18  mov      word ptr [edi + 0x10], 0x14
00416C1E  add      dword ptr [edi + 0x1c], 2
00416C22  add      dword ptr [edi + 0x1c], 3
00416C26  lea      edx, [ebp - 8]
00416C29  push     edx
00416C2A  push     0x403b88
00416C2F  call     0x438eaa
00416C34  add      esp, 0x24
00416C37  mov      ecx, dword ptr [ebp - 0x70]
00416C3A  mov      dword ptr [ebp - 0x48], ecx
00416C3D  mov      eax, dword ptr [ebp - 0x74]
00416C40  mov      dword ptr [ebp - 0x4c], eax
00416C43  mov      edx, dword ptr [ebp - 0x4c]
00416C46  cmp      dword ptr [edx + 9], 0
00416C4A  jbe      0x416c60
00416C4C  mov      ecx, dword ptr [ebp - 0x4c]
00416C4F  cmp      dword ptr [ecx + 5], 0
00416C53  je       0x416c60
00416C55  mov      eax, dword ptr [ebp - 0x4c]
00416C58  mov      edx, dword ptr [eax + 9]
00416C5B  cmp      edx, dword ptr [ebp - 0x48]
00416C5E  ja       0x416cdc
00416C60  push     edi
00416C61  push     0
00416C63  push     0
00416C65  push     0
00416C67  push     1
00416C69  push     0x403be0
00416C6E  push     0
00416C70  push     0x33a
00416C75  push     0x442ab4
00416C7A  push     0x442a90
00416C7F  push     0x442ad6
00416C84  lea      ecx, [ebp - 0xc]
00416C87  push     ecx
00416C88  call     0x438f10
00416C8D  add      esp, 0x14
00416C90  lea      eax, [ebp - 0xc]
00416C93  push     eax
00416C94  inc      dword ptr [edi + 0x1c]
00416C97  lea      edx, [ebp - 0x10]
00416C9A  push     edx
00416C9B  call     0x438de4
00416CA0  add      esp, 8
00416CA3  inc      dword ptr [edi + 0x1c]
00416CA6  mov      word ptr [edi + 0x10], 0x2c
00416CAC  dec      dword ptr [edi + 0x1c]
00416CAF  push     2
00416CB1  lea      ecx, [ebp - 0xc]
00416CB4  push     ecx
00416CB5  call     0x438f64
00416CBA  add      esp, 8
00416CBD  mov      word ptr [edi + 0x10], 0x14
00416CC3  add      dword ptr [edi + 0x1c], 2
00416CC7  add      dword ptr [edi + 0x1c], 3
00416CCB  lea      eax, [ebp - 0x10]
00416CCE  push     eax
00416CCF  push     0x403b88
00416CD4  call     0x438eaa
00416CD9  add      esp, 0x24
00416CDC  mov      edx, dword ptr [ebp - 0x4c]
00416CDF  mov      ecx, dword ptr [edx + 5]
00416CE2  mov      eax, dword ptr [ebp - 0x48]
00416CE5  shl      eax, 2
00416CE8  add      ecx, eax
00416CEA  mov      edx, dword ptr [ecx]
00416CEC  mov      dword ptr [ebp - 0x44], edx
00416CEF  inc      dword ptr [ebp - 0x70]
00416CF2  mov      ecx, dword ptr [ebp - 0x44]
00416CF5  mov      dword ptr [ebp - 0x50], ecx
00416CF8  mov      eax, dword ptr [ebp - 0x14]
00416CFB  mov      dword ptr [eax], 0x442da4
00416D01  mov      edx, dword ptr [ebp - 0x14]
00416D04  add      edx, 8
00416D07  push     edx
00416D08  call     0x438ec2
00416D0D  pop      ecx
00416D0E  inc      dword ptr [edi + 0x1c]
00416D11  push     dword ptr [ebp - 0x14]
00416D14  call     0x414a70
00416D19  pop      ecx
00416D1A  add      dword ptr [edi + 0x1c], 2
00416D1E  mov      ecx, dword ptr [ebp - 0x14]
00416D21  add      ecx, 0x18
00416D24  mov      dword ptr [ebp - 0x54], ecx
00416D27  mov      eax, dword ptr [ebp - 0x54]
00416D2A  mov      dword ptr [eax], 0x4402d4
00416D30  inc      dword ptr [edi + 0x1c]
00416D33  mov      edx, dword ptr [ebp - 0x54]
00416D36  add      edx, 4
00416D39  mov      dword ptr [ebp - 0x58], edx
00416D3C  mov      ecx, dword ptr [ebp - 0x58]
00416D3F  mov      dword ptr [ecx], 0x4402c0
00416D45  inc      dword ptr [edi + 0x1c]
00416D48  mov      eax, dword ptr [ebp - 0x54]
00416D4B  mov      dword ptr [eax], 0x4402e8
00416D51  mov      edx, dword ptr [ebp - 0x54]
00416D54  mov      dword ptr [edx + 4], 0x4402f8
00416D5B  add      dword ptr [edi + 0x1c], 3
00416D5F  mov      ecx, dword ptr [ebp - 0x14]
00416D62  mov      dword ptr [ecx], 0x442d64
00416D68  mov      eax, dword ptr [ebp - 0x14]
00416D6B  mov      dword ptr [eax + 0x18], 0x442d80
00416D72  mov      edx, dword ptr [ebp - 0x14]
00416D75  mov      dword ptr [edx + 0x1c], 0x442d90
00416D7C  mov      ecx, dword ptr [ebp - 0x14]
00416D7F  add      ecx, 0x20
00416D82  push     ecx
00416D83  call     0x438ec2
00416D88  pop      ecx
00416D89  inc      dword ptr [edi + 0x1c]
00416D8C  mov      eax, dword ptr [ebp - 0x14]
00416D8F  add      eax, 0x24
00416D92  push     eax
00416D93  call     0x438ec2
00416D98  pop      ecx
00416D99  inc      dword ptr [edi + 0x1c]
00416D9C  mov      edx, dword ptr [ebp - 0x14]
00416D9F  add      edx, 0x28
00416DA2  push     edx
00416DA3  call     0x438ec2
00416DA8  pop      ecx
00416DA9  inc      dword ptr [edi + 0x1c]
00416DAC  mov      ecx, dword ptr [ebp - 0x14]
00416DAF  add      ecx, 0x2c
00416DB2  push     ecx
00416DB3  call     0x438ec2
00416DB8  pop      ecx
00416DB9  inc      dword ptr [edi + 0x1c]
00416DBC  mov      eax, dword ptr [ebp - 0x14]
00416DBF  add      eax, 0x30
00416DC2  push     eax
00416DC3  call     0x438ec2
00416DC8  pop      ecx
00416DC9  inc      dword ptr [edi + 0x1c]
00416DCC  mov      edx, dword ptr [ebp - 0x14]
00416DCF  add      edx, 0x34
00416DD2  push     edx
00416DD3  call     0x438ec2
00416DD8  pop      ecx
00416DD9  inc      dword ptr [edi + 0x1c]
00416DDC  mov      ebx, dword ptr [ebp - 0x14]
00416DDF  add      ebx, 0x68
00416DE2  mov      dword ptr [ebx], 1
00416DE8  lea      esi, [ebx + 4]
00416DEB  mov      dword ptr [esi + 1], 0x43b500
00416DF2  push     0
00416DF4  push     0
00416DF6  push     0x417940
00416DFB  push     1
00416DFD  push     1
00416DFF  push     4
00416E01  push     4
00416E03  call     0x438e50
00416E08  pop      ecx
00416E09  push     eax
00416E0A  call     0x4037e0
00416E0F  add      esp, 0x1c
00416E12  mov      dword ptr [esi + 5], eax
00416E15  mov      dword ptr [esi + 9], 1
00416E1C  inc      dword ptr [edi + 0x1c]
00416E1F  mov      dword ptr [esi + 1], 0x4417e4
00416E26  add      dword ptr [edi + 0x1c], 2
00416E2A  mov      dword ptr [esi + 1], 0x441800
00416E31  xor      eax, eax
00416E33  mov      dword ptr [esi + 0xd], eax
00416E36  mov      dword ptr [esi + 0x11], 2
00416E3D  add      dword ptr [edi + 0x1c], 3
00416E41  add      dword ptr [edi + 0x1c], 4
00416E45  lea      edx, [ebx + 0x19]
00416E48  mov      dword ptr [ebp - 0x5c], edx
00416E4B  mov      ecx, dword ptr [ebp - 0x5c]
00416E4E  mov      dword ptr [ecx], 2
00416E54  add      dword ptr [edi + 0x1c], 5
00416E58  add      dword ptr [edi + 0x1c], 6
00416E5C  add      dword ptr [edi + 0x1c], 7
00416E60  lea      eax, [ebx + 0x1d]
00416E63  mov      dword ptr [ebp - 0x60], eax
00416E66  mov      edx, dword ptr [ebp - 0x60]
00416E69  mov      dword ptr [edx], 0x4402d4
00416E6F  inc      dword ptr [edi + 0x1c]
00416E72  mov      ecx, dword ptr [ebp - 0x60]
00416E75  add      ecx, 4
00416E78  mov      dword ptr [ebp - 0x64], ecx
00416E7B  mov      eax, dword ptr [ebp - 0x64]
00416E7E  mov      dword ptr [eax], 0x4402c0
00416E84  inc      dword ptr [edi + 0x1c]
00416E87  mov      edx, dword ptr [ebp - 0x60]
00416E8A  mov      dword ptr [edx], 0x4402e8
00416E90  mov      ecx, dword ptr [ebp - 0x60]
00416E93  mov      dword ptr [ecx + 4], 0x4402f8
00416E9A  add      dword ptr [edi + 0x1c], 3
00416E9E  mov      dword ptr [ebx + 0x25], 0x4417a0
00416EA5  mov      dword ptr [ebx + 0x1d], 0x4417c0
00416EAC  mov      dword ptr [ebx + 0x21], 0x4417d0
00416EB3  add      dword ptr [edi + 0x1c], 0xb
00416EB7  push     dword ptr [ebp - 0x14]
00416EBA  call     0x415560
00416EBF  pop      ecx
00416EC0  push     dword ptr [ebp - 0x50]
00416EC3  push     dword ptr [ebp - 0x14]
00416EC6  call     0x415661
00416ECB  add      esp, 8
00416ECE  mov      word ptr [edi + 0x10], 8
00416ED4  mov      eax, dword ptr [ebp - 0x14]
00416ED7  jmp      0x416edc
00416ED9  mov      eax, dword ptr [ebp - 0x14]
00416EDC  push     eax
00416EDD  mov      edx, dword ptr [ebp + 8]
00416EE0  add      edx, 4
00416EE3  push     edx
00416EE4  call     0x426399
00416EE9  add      esp, 8
00416EEC  mov      ecx, dword ptr [ebp - 0x70]
00416EEF  cmp      ecx, dword ptr [ebp - 0x68]
00416EF2  jb       0x416b97
00416EF8  cmp      dword ptr [ebp + 0xc], 0
00416EFC  je       0x416f06
00416EFE  mov      eax, dword ptr [ebp + 0xc]
00416F01  add      eax, 0x1d
00416F04  jmp      0x416f09
00416F06  mov      eax, dword ptr [ebp + 0xc]
00416F09  push     eax
00416F0A  mov      edx, dword ptr [ebp + 8]
00416F0D  add      edx, 0x1d
00416F10  push     edx
00416F11  call     0x416734
00416F16  add      esp, 8
00416F19  mov      eax, dword ptr [ebp + 0xc]
00416F1C  add      eax, 0x31
00416F1F  push     -1
00416F21  push     0
00416F23  push     eax
00416F24  mov      edx, dword ptr [ebp + 8]
00416F27  add      edx, 0x31
00416F2A  push     edx
00416F2B  call     0x438f04
00416F30  add      esp, 0x10
00416F33  mov      eax, dword ptr [ebp + 0xc]
00416F36  add      eax, 0x35
00416F39  push     -1
00416F3B  push     0
00416F3D  push     eax
00416F3E  mov      edx, dword ptr [ebp + 8]
00416F41  add      edx, 0x35
00416F44  push     edx
00416F45  call     0x438f04
00416F4A  add      esp, 0x10
00416F4D  mov      eax, dword ptr [ebp + 0xc]
00416F50  add      eax, 0x39
00416F53  push     -1
00416F55  push     0
00416F57  push     eax
00416F58  mov      edx, dword ptr [ebp + 8]
00416F5B  add      edx, 0x39
00416F5E  push     edx
00416F5F  call     0x438f04
00416F64  add      esp, 0x10
00416F67  mov      ecx, dword ptr [ebp + 0xc]
00416F6A  mov      eax, dword ptr [ecx + 0x3d]
00416F6D  mov      edx, dword ptr [ebp + 8]
00416F70  mov      dword ptr [edx + 0x3d], eax
00416F73  mov      ecx, dword ptr [ebp + 0xc]
00416F76  mov      eax, dword ptr [ecx + 0x41]
00416F79  mov      edx, dword ptr [ebp + 8]
00416F7C  mov      dword ptr [edx + 0x41], eax
00416F7F  mov      ecx, dword ptr [ebp + 0xc]
00416F82  mov      eax, dword ptr [ecx + 0x45]
00416F85  mov      edx, dword ptr [ebp + 8]
00416F88  mov      dword ptr [edx + 0x45], eax
00416F8B  mov      eax, dword ptr [ebp + 0xc]
00416F8E  add      eax, 0x49
00416F91  push     eax
00416F92  mov      edx, dword ptr [ebp + 8]
00416F95  add      edx, 0x49
00416F98  push     edx
00416F99  call     0x4056bb
00416F9E  add      esp, 8
00416FA1  mov      eax, dword ptr [ebp + 0xc]
00416FA4  add      eax, 0x5e
00416FA7  push     eax
00416FA8  mov      edx, dword ptr [ebp + 8]
00416FAB  add      edx, 0x5e
00416FAE  push     edx
00416FAF  mov      ecx, dword ptr [ebp + 8]
00416FB2  mov      eax, dword ptr [ecx + 0x7b]
00416FB5  call     dword ptr [eax]
00416FB7  add      esp, 8
00416FBA  mov      eax, dword ptr [ebp + 8]
00416FBD  mov      edx, dword ptr [edi]
00416FBF  mov      dword ptr fs:[0], edx
00416FC6  pop      edi
00416FC7  pop      esi
00416FC8  pop      ebx
00416FC9  mov      esp, ebp
00416FCB  pop      ebp
00416FCC  ret      
```

## Strings Referenced

**Total unique strings**: 11

- `"Cur < Upper"` @ 0x00442A55
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442A61
- `"Precondition"` @ 0x00442A83
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00442A90
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442AB4
- `"Precondition"` @ 0x00442AD6
- `"uZA"` @ 0x00442D64
- `"*KA"` @ 0x00442DA4
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## DATA Context

**Context around 0x00442A61**:

- `"TXTRECT"` @ 0x004429E4
- `"0,0,0,0"` @ 0x004429EC
- `"%i,%i,%i,%i"` @ 0x004429F4
- `"SETTXT"` @ 0x00442A00
- `"TXTHREFOFFSET"` @ 0x00442A07
- `"TIMER"` @ 0x00442A15
- `"0,0"` @ 0x00442A1B
- `"%i,%i"` @ 0x00442A1F
- `"TOOLBAR"` @ 0x00442A25
- `"0,0,0,0,0"` @ 0x00442A2D
- `"%i,%i,%i,%i,%i"` @ 0x00442A37
- `"PASSWORD"` @ 0x00442A49
- `"Cur < Upper"` @ 0x00442A55
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442A61
- `"Precondition"` @ 0x00442A83
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00442A90
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442AB4
- `"Precondition"` @ 0x00442AD6

**Context around 0x0044EB41**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD

**Context around 0x00442A83**:

- `"TXT"` @ 0x00442A03
- `"TXTHREFOFFSET"` @ 0x00442A07
- `"TIMER"` @ 0x00442A15
- `"0,0"` @ 0x00442A1B
- `"%i,%i"` @ 0x00442A1F
- `"TOOLBAR"` @ 0x00442A25
- `"0,0,0,0,0"` @ 0x00442A2D
- `"%i,%i,%i,%i,%i"` @ 0x00442A37
- `"PASSWORD"` @ 0x00442A49
- `"Cur < Upper"` @ 0x00442A55
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442A61
- `"Precondition"` @ 0x00442A83
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00442A90
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442AB4
- `"Precondition"` @ 0x00442AD6
- `"MAIN"` @ 0x00442AE3
- `"AREAS"` @ 0x00442AE8
- `"TITLE"` @ 0x00442AEE
- `"EXIT_ID"` @ 0x00442AF5
- `"INDEX_ID"` @ 0x00442AFD

**Context around 0x00442DA4**:

- `""|A"` @ 0x00442D28
- `"NhA"` @ 0x00442D34
- `"uZA"` @ 0x00442D64
- `"DTA"` @ 0x00442D6C
- `"*KA"` @ 0x00442DA4
- `"_PA"` @ 0x00442DC8

**Context around 0x00442D64**:

- `"kzA"` @ 0x00442D0C
- `""|A"` @ 0x00442D28
- `"NhA"` @ 0x00442D34
- `"uZA"` @ 0x00442D64
- `"DTA"` @ 0x00442D6C
- `"*KA"` @ 0x00442DA4
- `"_PA"` @ 0x00442DC8

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

**Context around 0x00442A90**:

- `"FSET"` @ 0x00442A10
- `"TIMER"` @ 0x00442A15
- `"0,0"` @ 0x00442A1B
- `"%i,%i"` @ 0x00442A1F
- `"TOOLBAR"` @ 0x00442A25
- `"0,0,0,0,0"` @ 0x00442A2D
- `"%i,%i,%i,%i,%i"` @ 0x00442A37
- `"PASSWORD"` @ 0x00442A49
- `"Cur < Upper"` @ 0x00442A55
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442A61
- `"Precondition"` @ 0x00442A83
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00442A90
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442AB4
- `"Precondition"` @ 0x00442AD6
- `"MAIN"` @ 0x00442AE3
- `"AREAS"` @ 0x00442AE8
- `"TITLE"` @ 0x00442AEE
- `"EXIT_ID"` @ 0x00442AF5
- `"INDEX_ID"` @ 0x00442AFD
- `"VNFILE"` @ 0x00442B06

**Context around 0x00442AB4**:

- `"%i,%i,%i,%i,%i"` @ 0x00442A37
- `"PASSWORD"` @ 0x00442A49
- `"Cur < Upper"` @ 0x00442A55
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442A61
- `"Precondition"` @ 0x00442A83
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00442A90
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442AB4
- `"Precondition"` @ 0x00442AD6
- `"MAIN"` @ 0x00442AE3
- `"AREAS"` @ 0x00442AE8
- `"TITLE"` @ 0x00442AEE
- `"EXIT_ID"` @ 0x00442AF5
- `"INDEX_ID"` @ 0x00442AFD
- `"VNFILE"` @ 0x00442B06
- `"fn.length()"` @ 0x00442B0D
- `"scene.cpp"` @ 0x00442B19
- `"Precondition"` @ 0x00442B23
- `".INI"` @ 0x00442B30

**Context around 0x00442A55**:

- `"SETIMG"` @ 0x004429D8
- `"TXT"` @ 0x004429DF
- `"TXTRECT"` @ 0x004429E4
- `"0,0,0,0"` @ 0x004429EC
- `"%i,%i,%i,%i"` @ 0x004429F4
- `"SETTXT"` @ 0x00442A00
- `"TXTHREFOFFSET"` @ 0x00442A07
- `"TIMER"` @ 0x00442A15
- `"0,0"` @ 0x00442A1B
- `"%i,%i"` @ 0x00442A1F
- `"TOOLBAR"` @ 0x00442A25
- `"0,0,0,0,0"` @ 0x00442A2D
- `"%i,%i,%i,%i,%i"` @ 0x00442A37
- `"PASSWORD"` @ 0x00442A49
- `"Cur < Upper"` @ 0x00442A55
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442A61
- `"Precondition"` @ 0x00442A83
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00442A90
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00442AB4

## Functions Called

- 0x00403618
- 0x00416FCD
- 0x00406954
- 0x00406954
- 0x00438EEC
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438EC2
- 0x00414A70
- 0x00438EC2
- 0x00438EC2
- 0x00438EC2
- 0x00438EC2
- 0x00438EC2
- 0x00438EC2
- 0x00438E50
- 0x004037E0
- 0x00415560
- 0x00415661
- 0x00426399
- 0x00416734
- 0x00438F04
- 0x00438F04
- 0x00438F04
- 0x004056BB

---

*Extracted with recursive CALL following and DATA context*
