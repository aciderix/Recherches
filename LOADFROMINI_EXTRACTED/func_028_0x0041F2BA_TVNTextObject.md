# LoadFromINI Function Analysis

**Function Address**: 0x0041F2BA
**Rank**: #28
**INI String Count**: 7
**Identified Structure**: TVNTextObject
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 30

```assembly
0041F2BA  push     ebp
0041F2BB  mov      ebp, esp
0041F2BD  push     ebx
0041F2BE  mov      eax, dword ptr [ebp + 0xc]
0041F2C1  mov      ebx, dword ptr [ebp + 8]
0041F2C4  mov      edx, dword ptr [eax]
0041F2C6  mov      dword ptr [ebx], edx
0041F2C8  mov      ecx, dword ptr [eax + 0x40]
0041F2CB  mov      dword ptr [ebx + 0x40], ecx
0041F2CE  lea      ecx, [eax + 0x44]
0041F2D1  lea      edx, [ebx + 0x44]
0041F2D4  mov      ecx, dword ptr [ecx]
0041F2D6  mov      dword ptr [edx], ecx
0041F2D8  mov      edx, dword ptr [eax + 0x48]
0041F2DB  mov      dword ptr [ebx + 0x48], edx
0041F2DE  mov      edx, dword ptr [eax + 0x4c]
0041F2E1  mov      dword ptr [ebx + 0x4c], edx
0041F2E4  mov      cl, byte ptr [eax + 0x50]
0041F2E7  mov      byte ptr [ebx + 0x50], cl
0041F2EA  mov      dl, byte ptr [eax + 0x51]
0041F2ED  mov      byte ptr [ebx + 0x51], dl
0041F2F0  add      eax, 4
0041F2F3  push     eax
0041F2F4  push     ebx
0041F2F5  call     0x41f231
0041F2FA  add      esp, 8
0041F2FD  mov      eax, ebx
0041F2FF  pop      ebx
0041F300  pop      ebp
0041F301  ret      
```

## Strings Referenced

**Total unique strings**: 4

- `"font"` @ 0x004463FD
- `"htmldata.cpp"` @ 0x00446402
- `"Precondition"` @ 0x0044640F
- `"Times New Roman"` @ 0x0044641C

## DATA Context

**Context around 0x00446402**:

- `"&Uacute;"` @ 0x00446383
- `"&Ucirc;"` @ 0x0044638E
- `"&Uuml;"` @ 0x00446398
- `"&Yacute;"` @ 0x004463A1
- `"&THORN;"` @ 0x004463AC
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

**Context around 0x0044641C**:

- `"&Yacute;"` @ 0x004463A1
- `"&THORN;"` @ 0x004463AC
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

**Context around 0x004463FD**:

- `"ve;"` @ 0x0044637D
- `"&Uacute;"` @ 0x00446383
- `"&Ucirc;"` @ 0x0044638E
- `"&Uuml;"` @ 0x00446398
- `"&Yacute;"` @ 0x004463A1
- `"&THORN;"` @ 0x004463AC
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

**Context around 0x0044640F**:

- `"Ucirc;"` @ 0x0044638F
- `"&Uuml;"` @ 0x00446398
- `"&Yacute;"` @ 0x004463A1
- `"&THORN;"` @ 0x004463AC
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

## Functions Called

- 0x0041F231

---

*Extracted with recursive CALL following and DATA context*
