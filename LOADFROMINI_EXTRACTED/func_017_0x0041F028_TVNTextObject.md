# LoadFromINI Function Analysis

**Function Address**: 0x0041F028
**Rank**: #17
**INI String Count**: 8
**Identified Structure**: TVNTextObject
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 76

```assembly
0041F028  push     ebp
0041F029  mov      ebp, esp
0041F02B  add      esp, -0x2c
0041F02E  push     ebx
0041F02F  mov      ebx, dword ptr [ebp + 8]
0041F032  mov      eax, 0x444cd4
0041F037  call     0x403618
0041F03C  test     ebx, ebx
0041F03E  jne      0x41f0c6
0041F044  lea      edx, [ebp - 0x2c]
0041F047  push     edx
0041F048  push     0
0041F04A  push     0
0041F04C  push     0
0041F04E  push     1
0041F050  push     0x403be0
0041F055  push     0
0041F057  mov      word ptr [ebp - 0x1c], 8
0041F05D  push     0x31
0041F05F  push     0x446402
0041F064  push     0x4463fd
0041F069  push     0x44640f
0041F06E  lea      ecx, [ebp - 4]
0041F071  push     ecx
0041F072  call     0x438f10
0041F077  add      esp, 0x14
0041F07A  lea      eax, [ebp - 4]
0041F07D  push     eax
0041F07E  inc      dword ptr [ebp - 0x10]
0041F081  lea      edx, [ebp - 8]
0041F084  push     edx
0041F085  call     0x438de4
0041F08A  add      esp, 8
0041F08D  inc      dword ptr [ebp - 0x10]
0041F090  mov      word ptr [ebp - 0x1c], 0x14
0041F096  dec      dword ptr [ebp - 0x10]
0041F099  push     2
0041F09B  lea      ecx, [ebp - 4]
0041F09E  push     ecx
0041F09F  call     0x438f64
0041F0A4  add      esp, 8
0041F0A7  mov      word ptr [ebp - 0x1c], 8
0041F0AD  add      dword ptr [ebp - 0x10], 2
0041F0B1  add      dword ptr [ebp - 0x10], 3
0041F0B5  lea      eax, [ebp - 8]
0041F0B8  push     eax
0041F0B9  push     0x403b88
0041F0BE  call     0x438eaa
0041F0C3  add      esp, 0x24
0041F0C6  push     0x3c
0041F0C8  push     0
0041F0CA  push     ebx
0041F0CB  call     0x438dde
0041F0D0  add      esp, 0xc
0041F0D3  push     0x48
0041F0D5  push     dword ptr [0x444a34]
0041F0DB  push     dword ptr [0x444a20]
0041F0E1  call     0x438fe8
0041F0E6  neg      eax
0041F0E8  mov      dword ptr [ebx], eax
0041F0EA  mov      dword ptr [ebx + 0x10], 0x190
0041F0F1  mov      byte ptr [ebx + 0x17], 1
0041F0F5  mov      byte ptr [ebx + 0x18], 0
0041F0F9  mov      byte ptr [ebx + 0x19], 0
0041F0FD  mov      byte ptr [ebx + 0x1a], 0
0041F101  mov      byte ptr [ebx + 0x1b], 0
0041F105  push     0x44641c
0041F10A  add      ebx, 0x1c
0041F10D  push     ebx
0041F10E  call     0x438ffa
0041F113  mov      eax, dword ptr [ebp - 0x2c]
0041F116  mov      dword ptr fs:[0], eax
0041F11C  pop      ebx
0041F11D  mov      esp, ebp
0041F11F  pop      ebp
0041F120  ret      
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
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438DDE
- 0x00438FE8
- 0x00438FFA

---

*Extracted with recursive CALL following and DATA context*
