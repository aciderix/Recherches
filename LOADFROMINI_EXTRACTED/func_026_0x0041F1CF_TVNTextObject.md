# LoadFromINI Function Analysis

**Function Address**: 0x0041F1CF
**Rank**: #26
**INI String Count**: 7
**Identified Structure**: TVNTextObject
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 38

```assembly
0041F1CF  push     ebp
0041F1D0  mov      ebp, esp
0041F1D2  add      esp, -0x24
0041F1D5  push     ebx
0041F1D6  push     esi
0041F1D7  mov      esi, dword ptr [ebp + 0xc]
0041F1DA  mov      ebx, dword ptr [ebp + 8]
0041F1DD  mov      eax, 0x444d04
0041F1E2  call     0x403618
0041F1E7  mov      edx, dword ptr [esi]
0041F1E9  mov      dword ptr [ebx], edx
0041F1EB  mov      ecx, dword ptr [esi + 0x40]
0041F1EE  mov      dword ptr [ebx + 0x40], ecx
0041F1F1  lea      edx, [esi + 0x44]
0041F1F4  lea      eax, [ebx + 0x44]
0041F1F7  mov      ecx, dword ptr [edx]
0041F1F9  mov      dword ptr [eax], ecx
0041F1FB  mov      eax, dword ptr [esi + 0x48]
0041F1FE  mov      dword ptr [ebx + 0x48], eax
0041F201  mov      edx, dword ptr [esi + 0x4c]
0041F204  mov      dword ptr [ebx + 0x4c], edx
0041F207  mov      cl, byte ptr [esi + 0x50]
0041F20A  mov      byte ptr [ebx + 0x50], cl
0041F20D  mov      al, byte ptr [esi + 0x51]
0041F210  mov      byte ptr [ebx + 0x51], al
0041F213  add      esi, 4
0041F216  push     esi
0041F217  push     ebx
0041F218  call     0x41f231
0041F21D  add      esp, 8
0041F220  mov      eax, dword ptr [ebp - 0x24]
0041F223  mov      dword ptr fs:[0], eax
0041F229  mov      eax, ebx
0041F22B  pop      esi
0041F22C  pop      ebx
0041F22D  mov      esp, ebp
0041F22F  pop      ebp
0041F230  ret      
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
