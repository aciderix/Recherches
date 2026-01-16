# LoadFromINI Function Analysis

**Function Address**: 0x0041F790
**Rank**: #22
**INI String Count**: 8
**Identified Structure**: TVNTextObject
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 144

```assembly
0041F790  push     ebp
0041F791  mov      ebp, esp
0041F793  add      esp, -0x38
0041F796  push     ebx
0041F797  push     esi
0041F798  push     edi
0041F799  mov      esi, dword ptr [ebp + 0x10]
0041F79C  mov      ebx, dword ptr [ebp + 8]
0041F79F  mov      eax, 0x444e14
0041F7A4  call     0x403618
0041F7A9  mov      edi, esi
0041F7AB  push     edi
0041F7AC  lea      edx, [ebx + 0x36]
0041F7AF  push     edx
0041F7B0  call     0x438ee0
0041F7B5  add      esp, 8
0041F7B8  movsx    ecx, byte ptr [eax]
0041F7BB  cmp      ecx, 0x3c
0041F7BE  je       0x41f849
0041F7C4  lea      eax, [ebp - 0x38]
0041F7C7  push     eax
0041F7C8  push     0
0041F7CA  push     0
0041F7CC  push     0
0041F7CE  push     1
0041F7D0  push     0x403be0
0041F7D5  push     0
0041F7D7  mov      word ptr [ebp - 0x28], 8
0041F7DD  push     0xae
0041F7E2  push     0x446440
0041F7E7  push     0x44642d
0041F7EC  push     0x44644d
0041F7F1  lea      edx, [ebp - 4]
0041F7F4  push     edx
0041F7F5  call     0x438f10
0041F7FA  add      esp, 0x14
0041F7FD  lea      ecx, [ebp - 4]
0041F800  push     ecx
0041F801  inc      dword ptr [ebp - 0x1c]
0041F804  lea      eax, [ebp - 8]
0041F807  push     eax
0041F808  call     0x438de4
0041F80D  add      esp, 8
0041F810  inc      dword ptr [ebp - 0x1c]
0041F813  mov      word ptr [ebp - 0x28], 0x14
0041F819  dec      dword ptr [ebp - 0x1c]
0041F81C  push     2
0041F81E  lea      edx, [ebp - 4]
0041F821  push     edx
0041F822  call     0x438f64
0041F827  add      esp, 8
0041F82A  mov      word ptr [ebp - 0x28], 8
0041F830  add      dword ptr [ebp - 0x1c], 2
0041F834  add      dword ptr [ebp - 0x1c], 3
0041F838  lea      ecx, [ebp - 8]
0041F83B  push     ecx
0041F83C  push     0x403b88
0041F841  call     0x438eaa
0041F846  add      esp, 0x24
0041F849  push     esi
0041F84A  mov      word ptr [ebp - 0x28], 0x2c
0041F850  push     0x44645a
0041F855  lea      eax, [ebp - 0xc]
0041F858  push     eax
0041F859  call     0x438e6e
0041F85E  add      esp, 8
0041F861  inc      dword ptr [ebp - 0x1c]
0041F864  lea      edx, [ebp - 0xc]
0041F867  push     edx
0041F868  lea      ecx, [ebx + 0x36]
0041F86B  push     ecx
0041F86C  call     0x438e98
0041F871  add      esp, 0xc
0041F874  mov      edi, eax
0041F876  dec      dword ptr [ebp - 0x1c]
0041F879  push     2
0041F87B  lea      eax, [ebp - 0xc]
0041F87E  push     eax
0041F87F  call     0x438f64
0041F884  add      esp, 8
0041F887  mov      word ptr [ebp - 0x28], 0x20
0041F88D  cmp      edi, -1
0041F890  jne      0x41f8e2
0041F892  mov      word ptr [ebp - 0x28], 0x38
0041F898  push     0x44645c
0041F89D  lea      edx, [ebp - 0x10]
0041F8A0  push     edx
0041F8A1  call     0x438e6e
0041F8A6  add      esp, 8
0041F8A9  inc      dword ptr [ebp - 0x1c]
0041F8AC  push     -1
0041F8AE  push     0
0041F8B0  lea      ecx, [ebp - 0x10]
0041F8B3  push     ecx
0041F8B4  push     dword ptr [ebp + 0xc]
0041F8B7  call     0x438f04
0041F8BC  add      esp, 0x10
0041F8BF  dec      dword ptr [ebp - 0x1c]
0041F8C2  push     2
0041F8C4  lea      eax, [ebp - 0x10]
0041F8C7  push     eax
0041F8C8  call     0x438f64
0041F8CD  add      esp, 8
0041F8D0  mov      edx, dword ptr [ebx + 0x36]
0041F8D3  mov      eax, dword ptr [edx + 6]
0041F8D6  mov      edx, dword ptr [ebp - 0x38]
0041F8D9  mov      dword ptr fs:[0], edx
0041F8E0  jmp      0x41f934
0041F8E2  mov      word ptr [ebp - 0x28], 0x44
0041F8E8  mov      ecx, edi
0041F8EA  sub      ecx, esi
0041F8EC  dec      ecx
0041F8ED  push     ecx
0041F8EE  inc      esi
0041F8EF  push     esi
0041F8F0  add      ebx, 0x36
0041F8F3  push     ebx
0041F8F4  lea      eax, [ebp - 0x14]
0041F8F7  push     eax
0041F8F8  call     0x438fa6
0041F8FD  add      esp, 0x10
0041F900  lea      eax, [ebp - 0x14]
0041F903  inc      dword ptr [ebp - 0x1c]
0041F906  push     -1
0041F908  push     0
0041F90A  push     eax
0041F90B  push     dword ptr [ebp + 0xc]
0041F90E  call     0x438f04
0041F913  add      esp, 0x10
0041F916  dec      dword ptr [ebp - 0x1c]
0041F919  push     2
0041F91B  lea      edx, [ebp - 0x14]
0041F91E  push     edx
0041F91F  call     0x438f64
0041F924  add      esp, 8
0041F927  lea      eax, [edi + 1]
0041F92A  mov      edx, dword ptr [ebp - 0x38]
0041F92D  mov      dword ptr fs:[0], edx
0041F934  pop      edi
0041F935  pop      esi
0041F936  pop      ebx
0041F937  mov      esp, ebp
0041F939  pop      ebp
0041F93A  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"Text[start] == '<'"` @ 0x0044642D
- `"htmldata.cpp"` @ 0x00446440
- `"Precondition"` @ 0x0044644D

## DATA Context

**Context around 0x00446440**:

- `"slash;"` @ 0x004463C0
- `"&thorn;"` @ 0x004463C9
- `"&szlig;"` @ 0x004463D3
- `"&sup2;"` @ 0x004463DD
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

**Context around 0x0044644D**:

- `"rn;"` @ 0x004463CD
- `"&szlig;"` @ 0x004463D3
- `"&sup2;"` @ 0x004463DD
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

**Context around 0x0044642D**:

- `"THORN;"` @ 0x004463AD
- `"&eth;"` @ 0x004463B6
- `"&oslash;"` @ 0x004463BE
- `"&thorn;"` @ 0x004463C9
- `"&szlig;"` @ 0x004463D3
- `"&sup2;"` @ 0x004463DD
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

## Functions Called

- 0x00403618
- 0x00438EE0
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438E6E
- 0x00438E98
- 0x00438F64
- 0x00438E6E
- 0x00438F04
- 0x00438F64
- 0x00438FA6
- 0x00438F04
- 0x00438F64

---

*Extracted with recursive CALL following and DATA context*
