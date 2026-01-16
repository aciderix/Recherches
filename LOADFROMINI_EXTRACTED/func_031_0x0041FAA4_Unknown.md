# LoadFromINI Function Analysis

**Function Address**: 0x0041FAA4
**Rank**: #31
**INI String Count**: 7
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 147

```assembly
0041FAA4  push     ebp
0041FAA5  mov      ebp, esp
0041FAA7  add      esp, -0x40
0041FAAA  push     ebx
0041FAAB  push     esi
0041FAAC  push     edi
0041FAAD  mov      edi, dword ptr [ebp + 0x10]
0041FAB0  mov      esi, dword ptr [ebp + 0xc]
0041FAB3  mov      eax, 0x444f0c
0041FAB8  call     0x403618
0041FABD  mov      dword ptr [edi], 0xffffffff
0041FAC3  mov      word ptr [ebp - 0x28], 0x14
0041FAC9  push     0x446461
0041FACE  lea      edx, [ebp - 4]
0041FAD1  push     edx
0041FAD2  call     0x438e6e
0041FAD7  add      esp, 8
0041FADA  inc      dword ptr [ebp - 0x1c]
0041FADD  push     0
0041FADF  lea      ecx, [ebp - 4]
0041FAE2  push     ecx
0041FAE3  push     esi
0041FAE4  call     0x438ed4
0041FAE9  add      esp, 0xc
0041FAEC  mov      ebx, eax
0041FAEE  dec      dword ptr [ebp - 0x1c]
0041FAF1  push     2
0041FAF3  lea      eax, [ebp - 4]
0041FAF6  push     eax
0041FAF7  call     0x438f64
0041FAFC  add      esp, 8
0041FAFF  mov      word ptr [ebp - 0x28], 8
0041FB05  cmp      ebx, -1
0041FB08  je       0x41fc42
0041FB0E  push     ebx
0041FB0F  mov      word ptr [ebp - 0x28], 0x20
0041FB15  push     0x446466
0041FB1A  lea      edx, [ebp - 8]
0041FB1D  push     edx
0041FB1E  call     0x438e6e
0041FB23  add      esp, 8
0041FB26  inc      dword ptr [ebp - 0x1c]
0041FB29  lea      ecx, [ebp - 8]
0041FB2C  push     ecx
0041FB2D  push     esi
0041FB2E  call     0x438e98
0041FB33  add      esp, 0xc
0041FB36  mov      ebx, eax
0041FB38  dec      dword ptr [ebp - 0x1c]
0041FB3B  push     2
0041FB3D  lea      eax, [ebp - 8]
0041FB40  push     eax
0041FB41  call     0x438f64
0041FB46  add      esp, 8
0041FB49  cmp      ebx, -1
0041FB4C  je       0x41fc42
0041FB52  inc      ebx
0041FB53  push     ebx
0041FB54  mov      word ptr [ebp - 0x28], 0x2c
0041FB5A  push     0x446469
0041FB5F  lea      edx, [ebp - 0xc]
0041FB62  push     edx
0041FB63  call     0x438e6e
0041FB68  add      esp, 8
0041FB6B  inc      dword ptr [ebp - 0x1c]
0041FB6E  lea      ecx, [ebp - 0xc]
0041FB71  push     ecx
0041FB72  push     esi
0041FB73  call     0x438e98
0041FB78  add      esp, 0xc
0041FB7B  mov      dword ptr [ebp - 0x3c], eax
0041FB7E  dec      dword ptr [ebp - 0x1c]
0041FB81  push     2
0041FB83  lea      eax, [ebp - 0xc]
0041FB86  push     eax
0041FB87  call     0x438f64
0041FB8C  add      esp, 8
0041FB8F  cmp      dword ptr [ebp - 0x3c], -1
0041FB93  je       0x41fc42
0041FB99  mov      edx, dword ptr [ebp - 0x3c]
0041FB9C  sub      edx, ebx
0041FB9E  je       0x41fc42
0041FBA4  mov      word ptr [ebp - 0x28], 0x44
0041FBAA  mov      ecx, dword ptr [ebp - 0x3c]
0041FBAD  sub      ecx, ebx
0041FBAF  push     ecx
0041FBB0  push     ebx
0041FBB1  push     esi
0041FBB2  lea      eax, [ebp - 0x14]
0041FBB5  push     eax
0041FBB6  call     0x438fa6
0041FBBB  add      esp, 0x10
0041FBBE  lea      edx, [ebp - 0x14]
0041FBC1  inc      dword ptr [ebp - 0x1c]
0041FBC4  mov      dword ptr [ebp - 0x40], edx
0041FBC7  mov      ecx, dword ptr [ebp - 0x40]
0041FBCA  mov      eax, dword ptr [ecx]
0041FBCC  mov      edx, dword ptr [eax + 2]
0041FBCF  push     edx
0041FBD0  lea      ecx, [ebp - 0x10]
0041FBD3  push     ecx
0041FBD4  call     0x438e6e
0041FBD9  add      esp, 8
0041FBDC  inc      dword ptr [ebp - 0x1c]
0041FBDF  dec      dword ptr [ebp - 0x1c]
0041FBE2  push     2
0041FBE4  lea      eax, [ebp - 0x14]
0041FBE7  push     eax
0041FBE8  call     0x438f64
0041FBED  add      esp, 8
0041FBF0  mov      word ptr [ebp - 0x28], 0x38
0041FBF6  push     0
0041FBF8  lea      edx, [ebp - 0x10]
0041FBFB  push     edx
0041FBFC  call     0x438ee0
0041FC01  add      esp, 8
0041FC04  movsx    ecx, byte ptr [eax]
0041FC07  cmp      ecx, 0x30
0041FC0A  jl       0x41fc31
0041FC0C  push     0
0041FC0E  lea      eax, [ebp - 0x10]
0041FC11  push     eax
0041FC12  call     0x438ee0
0041FC17  add      esp, 8
0041FC1A  movsx    edx, byte ptr [eax]
0041FC1D  cmp      edx, 0x39
0041FC20  jg       0x41fc31
0041FC22  mov      ecx, dword ptr [ebp - 0x10]
0041FC25  mov      ebx, dword ptr [ecx + 2]
0041FC28  push     ebx
0041FC29  call     0x438eb0
0041FC2E  pop      ecx
0041FC2F  mov      dword ptr [edi], eax
0041FC31  dec      dword ptr [ebp - 0x1c]
0041FC34  push     2
0041FC36  lea      eax, [ebp - 0x10]
0041FC39  push     eax
0041FC3A  call     0x438f64
0041FC3F  add      esp, 8
0041FC42  mov      edx, dword ptr [ebp - 0x38]
0041FC45  mov      dword ptr fs:[0], edx
0041FC4C  pop      edi
0041FC4D  pop      esi
0041FC4E  pop      ebx
0041FC4F  mov      esp, ebp
0041FC51  pop      ebp
0041FC52  ret      
```

## Strings Referenced

**Total unique strings**: 2

- `"HREF"` @ 0x00446461
- `"."'"` @ 0x00446469

## DATA Context

**Context around 0x00446461**:

- `"&middot;"` @ 0x004463E6
- `"&deg;"` @ 0x004463F1
- `"font"` @ 0x004463FD
- `"htmldata.cpp"` @ 0x00446402
- `"Precondition"` @ 0x0044640F
- `"Times New Roman"` @ 0x0044641C
- `"Text[start] == '<'"` @ 0x0044642D
- `"htmldata.cpp"` @ 0x00446440
- `"Precondition"` @ 0x0044644D
- `"HREF"` @ 0x00446461
- `"."'"` @ 0x00446469
- `"SIZE"` @ 0x0044646D
- `"SIZE="%i""` @ 0x00446472
- `"SIZE=%i"` @ 0x0044647C
- `"FACE"` @ 0x00446484
- `"COLOR"` @ 0x0044648D
- `"COLOR="#%lX""` @ 0x00446493
- `"%u."` @ 0x004464A0
- `"Text.length()"` @ 0x004464A6
- `"htmldata.cpp"` @ 0x004464B4

**Context around 0x00446469**:

- `"ddot;"` @ 0x004463E9
- `"&deg;"` @ 0x004463F1
- `"font"` @ 0x004463FD
- `"htmldata.cpp"` @ 0x00446402
- `"Precondition"` @ 0x0044640F
- `"Times New Roman"` @ 0x0044641C
- `"Text[start] == '<'"` @ 0x0044642D
- `"htmldata.cpp"` @ 0x00446440
- `"Precondition"` @ 0x0044644D
- `"HREF"` @ 0x00446461
- `"."'"` @ 0x00446469
- `"SIZE"` @ 0x0044646D
- `"SIZE="%i""` @ 0x00446472
- `"SIZE=%i"` @ 0x0044647C
- `"FACE"` @ 0x00446484
- `"COLOR"` @ 0x0044648D
- `"COLOR="#%lX""` @ 0x00446493
- `"%u."` @ 0x004464A0
- `"Text.length()"` @ 0x004464A6
- `"htmldata.cpp"` @ 0x004464B4

## Functions Called

- 0x00403618
- 0x00438E6E
- 0x00438ED4
- 0x00438F64
- 0x00438E6E
- 0x00438E98
- 0x00438F64
- 0x00438E6E
- 0x00438E98
- 0x00438F64
- 0x00438FA6
- 0x00438E6E
- 0x00438F64
- 0x00438EE0
- 0x00438EE0
- 0x00438EB0
- 0x00438F64

---

*Extracted with recursive CALL following and DATA context*
