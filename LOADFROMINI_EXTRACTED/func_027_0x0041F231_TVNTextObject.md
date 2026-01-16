# LoadFromINI Function Analysis

**Function Address**: 0x0041F231
**Rank**: #27
**INI String Count**: 7
**Identified Structure**: TVNTextObject
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 54

```assembly
0041F231  push     ebp
0041F232  mov      ebp, esp
0041F234  push     ebx
0041F235  push     esi
0041F236  mov      esi, dword ptr [ebp + 0xc]
0041F239  mov      ebx, dword ptr [ebp + 8]
0041F23C  test     esi, esi
0041F23E  je       0x41f2ac
0041F240  push     0x3c
0041F242  push     0
0041F244  lea      eax, [ebx + 4]
0041F247  push     eax
0041F248  call     0x438dde
0041F24D  add      esp, 0xc
0041F250  mov      edx, dword ptr [esi]
0041F252  mov      dword ptr [ebx + 4], edx
0041F255  mov      ecx, dword ptr [esi + 4]
0041F258  mov      dword ptr [ebx + 8], ecx
0041F25B  mov      eax, dword ptr [esi + 8]
0041F25E  mov      dword ptr [ebx + 0xc], eax
0041F261  mov      edx, dword ptr [esi + 0xc]
0041F264  mov      dword ptr [ebx + 0x10], edx
0041F267  mov      ecx, dword ptr [esi + 0x10]
0041F26A  mov      dword ptr [ebx + 0x14], ecx
0041F26D  mov      al, byte ptr [esi + 0x14]
0041F270  mov      byte ptr [ebx + 0x18], al
0041F273  mov      dl, byte ptr [esi + 0x15]
0041F276  mov      byte ptr [ebx + 0x19], dl
0041F279  mov      cl, byte ptr [esi + 0x16]
0041F27C  mov      byte ptr [ebx + 0x1a], cl
0041F27F  mov      al, byte ptr [esi + 0x17]
0041F282  mov      byte ptr [ebx + 0x1b], al
0041F285  mov      dl, byte ptr [esi + 0x18]
0041F288  mov      byte ptr [ebx + 0x1c], dl
0041F28B  mov      cl, byte ptr [esi + 0x19]
0041F28E  mov      byte ptr [ebx + 0x1d], cl
0041F291  mov      al, byte ptr [esi + 0x1a]
0041F294  mov      byte ptr [ebx + 0x1e], al
0041F297  mov      dl, byte ptr [esi + 0x1b]
0041F29A  mov      byte ptr [ebx + 0x1f], dl
0041F29D  add      esi, 0x1c
0041F2A0  push     esi
0041F2A1  add      ebx, 0x20
0041F2A4  push     ebx
0041F2A5  call     0x438ffa
0041F2AA  jmp      0x41f2b6
0041F2AC  add      ebx, 4
0041F2AF  push     ebx
0041F2B0  call     0x41f028
0041F2B5  pop      ecx
0041F2B6  pop      esi
0041F2B7  pop      ebx
0041F2B8  pop      ebp
0041F2B9  ret      
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

- 0x00438DDE
- 0x00438FFA
- 0x0041F028

---

*Extracted with recursive CALL following and DATA context*
