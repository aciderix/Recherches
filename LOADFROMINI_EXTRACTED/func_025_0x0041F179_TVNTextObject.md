# LoadFromINI Function Analysis

**Function Address**: 0x0041F179
**Rank**: #25
**INI String Count**: 7
**Identified Structure**: TVNTextObject
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 31

```assembly
0041F179  push     ebp
0041F17A  mov      ebp, esp
0041F17C  add      esp, -0x24
0041F17F  push     ebx
0041F180  mov      ebx, dword ptr [ebp + 8]
0041F183  mov      eax, 0x444cfc
0041F188  call     0x403618
0041F18D  mov      edx, dword ptr [ebp + 0xc]
0041F190  mov      dword ptr [ebx], edx
0041F192  mov      ecx, dword ptr [ebp + 0x14]
0041F195  mov      dword ptr [ebx + 0x40], ecx
0041F198  lea      eax, [ebx + 0x44]
0041F19B  mov      edx, dword ptr [ebp + 0x18]
0041F19E  mov      dword ptr [eax], edx
0041F1A0  xor      ecx, ecx
0041F1A2  mov      dword ptr [ebx + 0x48], ecx
0041F1A5  xor      eax, eax
0041F1A7  mov      dword ptr [ebx + 0x4c], eax
0041F1AA  mov      byte ptr [ebx + 0x50], 0
0041F1AE  mov      byte ptr [ebx + 0x51], 0
0041F1B2  push     dword ptr [ebp + 0x10]
0041F1B5  push     ebx
0041F1B6  call     0x41f231
0041F1BB  add      esp, 8
0041F1BE  mov      edx, dword ptr [ebp - 0x24]
0041F1C1  mov      dword ptr fs:[0], edx
0041F1C8  mov      eax, ebx
0041F1CA  pop      ebx
0041F1CB  mov      esp, ebp
0041F1CD  pop      ebp
0041F1CE  ret      
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

- 0x00403618
- 0x0041F231

---

*Extracted with recursive CALL following and DATA context*
