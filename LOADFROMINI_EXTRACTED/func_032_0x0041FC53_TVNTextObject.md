# LoadFromINI Function Analysis

**Function Address**: 0x0041FC53
**Rank**: #32
**INI String Count**: 7
**Identified Structure**: TVNTextObject
**Confidence Score**: 2

---

## Assembly Code

**Instructions**: 274

```assembly
0041FC53  push     ebp
0041FC54  mov      ebp, esp
0041FC56  add      esp, -0x6c
0041FC59  push     ebx
0041FC5A  push     esi
0041FC5B  push     edi
0041FC5C  mov      esi, dword ptr [ebp + 0x10]
0041FC5F  lea      edi, [ebp - 0x48]
0041FC62  mov      eax, 0x444fec
0041FC67  call     0x403618
0041FC6C  mov      word ptr [edi + 0x10], 0x14
0041FC72  push     0x44646d
0041FC77  lea      edx, [ebp - 4]
0041FC7A  push     edx
0041FC7B  call     0x438e6e
0041FC80  add      esp, 8
0041FC83  inc      dword ptr [edi + 0x1c]
0041FC86  push     0
0041FC88  lea      ecx, [ebp - 4]
0041FC8B  push     ecx
0041FC8C  push     esi
0041FC8D  call     0x438ed4
0041FC92  add      esp, 0xc
0041FC95  mov      ebx, eax
0041FC97  dec      dword ptr [edi + 0x1c]
0041FC9A  push     2
0041FC9C  lea      eax, [ebp - 4]
0041FC9F  push     eax
0041FCA0  call     0x438f64
0041FCA5  add      esp, 8
0041FCA8  mov      word ptr [edi + 0x10], 8
0041FCAE  cmp      ebx, -1
0041FCB1  je       0x41fd90
0041FCB7  xor      edx, edx
0041FCB9  mov      dword ptr [ebp - 0x4c], edx
0041FCBC  lea      ecx, [ebp - 0x4c]
0041FCBF  push     ecx
0041FCC0  push     0x446472
0041FCC5  mov      word ptr [edi + 0x10], 0x2c
0041FCCB  push     ebx
0041FCCC  push     esi
0041FCCD  lea      eax, [ebp - 8]
0041FCD0  push     eax
0041FCD1  call     0x438dc6
0041FCD6  add      esp, 0xc
0041FCD9  lea      edx, [ebp - 8]
0041FCDC  inc      dword ptr [edi + 0x1c]
0041FCDF  mov      dword ptr [ebp - 0x54], edx
0041FCE2  mov      ecx, dword ptr [ebp - 0x54]
0041FCE5  mov      eax, dword ptr [ecx]
0041FCE7  mov      edx, dword ptr [eax + 2]
0041FCEA  push     edx
0041FCEB  call     0x438d96
0041FCF0  add      esp, 0xc
0041FCF3  mov      dword ptr [ebp - 0x50], eax
0041FCF6  dec      dword ptr [edi + 0x1c]
0041FCF9  push     2
0041FCFB  lea      ecx, [ebp - 8]
0041FCFE  push     ecx
0041FCFF  call     0x438f64
0041FD04  add      esp, 8
0041FD07  mov      word ptr [edi + 0x10], 0x20
0041FD0D  cmp      dword ptr [ebp - 0x50], 0
0041FD11  jne      0x41fd5b
0041FD13  lea      eax, [ebp - 0x4c]
0041FD16  push     eax
0041FD17  push     0x44647c
0041FD1C  mov      word ptr [edi + 0x10], 0x38
0041FD22  push     ebx
0041FD23  push     esi
0041FD24  lea      edx, [ebp - 0xc]
0041FD27  push     edx
0041FD28  call     0x438dc6
0041FD2D  add      esp, 0xc
0041FD30  lea      ecx, [ebp - 0xc]
0041FD33  inc      dword ptr [edi + 0x1c]
0041FD36  mov      dword ptr [ebp - 0x58], ecx
0041FD39  mov      eax, dword ptr [ebp - 0x58]
0041FD3C  mov      edx, dword ptr [eax]
0041FD3E  mov      ecx, dword ptr [edx + 2]
0041FD41  push     ecx
0041FD42  call     0x438d96
0041FD47  add      esp, 0xc
0041FD4A  dec      dword ptr [edi + 0x1c]
0041FD4D  push     2
0041FD4F  lea      eax, [ebp - 0xc]
0041FD52  push     eax
0041FD53  call     0x438f64
0041FD58  add      esp, 8
0041FD5B  cmp      dword ptr [ebp - 0x4c], 0
0041FD5F  jge      0x41fd65
0041FD61  add      dword ptr [ebp - 0x4c], 3
0041FD65  cmp      dword ptr [ebp - 0x4c], 0
0041FD69  jle      0x41fd90
0041FD6B  cmp      dword ptr [ebp - 0x4c], 7
0041FD6F  jg       0x41fd90
0041FD71  push     0x48
0041FD73  push     dword ptr [0x444a34]
0041FD79  mov      edx, dword ptr [ebp - 0x4c]
0041FD7C  push     dword ptr [edx*4 + 0x444a14]
0041FD83  call     0x438fe8
0041FD88  neg      eax
0041FD8A  mov      ecx, dword ptr [ebp + 0xc]
0041FD8D  mov      dword ptr [ecx + 4], eax
0041FD90  mov      word ptr [edi + 0x10], 0x44
0041FD96  push     0x446484
0041FD9B  lea      eax, [ebp - 0x10]
0041FD9E  push     eax
0041FD9F  call     0x438e6e
0041FDA4  add      esp, 8
0041FDA7  inc      dword ptr [edi + 0x1c]
0041FDAA  push     0
0041FDAC  lea      edx, [ebp - 0x10]
0041FDAF  push     edx
0041FDB0  push     esi
0041FDB1  call     0x438ed4
0041FDB6  add      esp, 0xc
0041FDB9  mov      ebx, eax
0041FDBB  dec      dword ptr [edi + 0x1c]
0041FDBE  push     2
0041FDC0  lea      eax, [ebp - 0x10]
0041FDC3  push     eax
0041FDC4  call     0x438f64
0041FDC9  add      esp, 8
0041FDCC  cmp      ebx, -1
0041FDCF  je       0x41fea5
0041FDD5  push     ebx
0041FDD6  mov      word ptr [edi + 0x10], 0x50
0041FDDC  push     0x446489
0041FDE1  lea      edx, [ebp - 0x14]
0041FDE4  push     edx
0041FDE5  call     0x438e6e
0041FDEA  add      esp, 8
0041FDED  inc      dword ptr [edi + 0x1c]
0041FDF0  lea      ecx, [ebp - 0x14]
0041FDF3  push     ecx
0041FDF4  push     esi
0041FDF5  call     0x438e98
0041FDFA  add      esp, 0xc
0041FDFD  mov      ebx, eax
0041FDFF  dec      dword ptr [edi + 0x1c]
0041FE02  push     2
0041FE04  lea      eax, [ebp - 0x14]
0041FE07  push     eax
0041FE08  call     0x438f64
0041FE0D  add      esp, 8
0041FE10  cmp      ebx, -1
0041FE13  je       0x41fea5
0041FE19  inc      ebx
0041FE1A  push     ebx
0041FE1B  mov      word ptr [edi + 0x10], 0x5c
0041FE21  push     0x44648b
0041FE26  lea      edx, [ebp - 0x18]
0041FE29  push     edx
0041FE2A  call     0x438e6e
0041FE2F  add      esp, 8
0041FE32  inc      dword ptr [edi + 0x1c]
0041FE35  lea      ecx, [ebp - 0x18]
0041FE38  push     ecx
0041FE39  push     esi
0041FE3A  call     0x438e98
0041FE3F  add      esp, 0xc
0041FE42  mov      dword ptr [ebp - 0x5c], eax
0041FE45  dec      dword ptr [edi + 0x1c]
0041FE48  push     2
0041FE4A  lea      eax, [ebp - 0x18]
0041FE4D  push     eax
0041FE4E  call     0x438f64
0041FE53  add      esp, 8
0041FE56  cmp      dword ptr [ebp - 0x5c], -1
0041FE5A  je       0x41fea5
0041FE5C  mov      word ptr [edi + 0x10], 0x68
0041FE62  mov      edx, dword ptr [ebp - 0x5c]
0041FE65  sub      edx, ebx
0041FE67  push     edx
0041FE68  push     ebx
0041FE69  push     esi
0041FE6A  lea      ecx, [ebp - 0x1c]
0041FE6D  push     ecx
0041FE6E  call     0x438fa6
0041FE73  add      esp, 0x10
0041FE76  lea      eax, [ebp - 0x1c]
0041FE79  inc      dword ptr [edi + 0x1c]
0041FE7C  mov      dword ptr [ebp - 0x60], eax
0041FE7F  mov      edx, dword ptr [ebp - 0x60]
0041FE82  mov      ecx, dword ptr [edx]
0041FE84  mov      eax, dword ptr [ecx + 2]
0041FE87  push     eax
0041FE88  mov      edx, dword ptr [ebp + 0xc]
0041FE8B  add      edx, 0x20
0041FE8E  push     edx
0041FE8F  call     0x438ffa
0041FE94  dec      dword ptr [edi + 0x1c]
0041FE97  push     2
0041FE99  lea      ecx, [ebp - 0x1c]
0041FE9C  push     ecx
0041FE9D  call     0x438f64
0041FEA2  add      esp, 8
0041FEA5  mov      word ptr [edi + 0x10], 0x74
0041FEAB  push     0x44648d
0041FEB0  lea      eax, [ebp - 0x20]
0041FEB3  push     eax
0041FEB4  call     0x438e6e
0041FEB9  add      esp, 8
0041FEBC  inc      dword ptr [edi + 0x1c]
0041FEBF  push     0
0041FEC1  lea      edx, [ebp - 0x20]
0041FEC4  push     edx
0041FEC5  push     esi
0041FEC6  call     0x438ed4
0041FECB  add      esp, 0xc
0041FECE  mov      ebx, eax
0041FED0  dec      dword ptr [edi + 0x1c]
0041FED3  push     2
0041FED5  lea      eax, [ebp - 0x20]
0041FED8  push     eax
0041FED9  call     0x438f64
0041FEDE  add      esp, 8
0041FEE1  cmp      ebx, -1
0041FEE4  je       0x41ff80
0041FEEA  lea      edx, [ebp - 0x64]
0041FEED  push     edx
0041FEEE  push     0x446493
0041FEF3  mov      word ptr [edi + 0x10], 0x80
0041FEF9  push     ebx
0041FEFA  push     esi
0041FEFB  lea      ecx, [ebp - 0x24]
0041FEFE  push     ecx
0041FEFF  call     0x438dc6
0041FF04  add      esp, 0xc
0041FF07  lea      eax, [ebp - 0x24]
0041FF0A  inc      dword ptr [edi + 0x1c]
0041FF0D  mov      dword ptr [ebp - 0x68], eax
0041FF10  mov      edx, dword ptr [ebp - 0x68]
0041FF13  mov      ecx, dword ptr [edx]
0041FF15  mov      eax, dword ptr [ecx + 2]
0041FF18  push     eax
0041FF19  call     0x438d96
0041FF1E  add      esp, 0xc
0041FF21  dec      dword ptr [edi + 0x1c]
0041FF24  push     2
0041FF26  lea      edx, [ebp - 0x24]
0041FF29  push     edx
0041FF2A  call     0x438f64
0041FF2F  add      esp, 8
0041FF32  and      dword ptr [ebp - 0x64], 0xffffff
0041FF39  xor      eax, eax
0041FF3B  mov      al, byte ptr [ebp - 0x64]
0041FF3E  movzx    edx, word ptr [ebp - 0x64]
0041FF42  sar      edx, 8
0041FF45  and      edx, 0xff
0041FF4B  mov      ecx, dword ptr [ebp - 0x64]
0041FF4E  sar      ecx, 0x10
0041FF51  and      ecx, 0xff
0041FF57  and      ecx, 0xff
0041FF5D  and      edx, 0xff
0041FF63  shl      edx, 8
0041FF66  or       ecx, edx
0041FF68  and      eax, 0xff
0041FF6D  shl      eax, 0x10
0041FF70  or       ecx, eax
0041FF72  mov      dword ptr [ebp - 0x6c], ecx
0041FF75  mov      eax, dword ptr [ebp + 0xc]
0041FF78  add      eax, 0x44
0041FF7B  mov      edx, dword ptr [ebp - 0x6c]
0041FF7E  mov      dword ptr [eax], edx
0041FF80  mov      eax, dword ptr [edi]
0041FF82  mov      dword ptr fs:[0], eax
0041FF88  pop      edi
0041FF89  pop      esi
0041FF8A  pop      ebx
0041FF8B  mov      esp, ebp
0041FF8D  pop      ebp
0041FF8E  ret      
```

## Strings Referenced

**Total unique strings**: 6

- `"SIZE"` @ 0x0044646D
- `"SIZE="%i""` @ 0x00446472
- `"SIZE=%i"` @ 0x0044647C
- `"FACE"` @ 0x00446484
- `"COLOR"` @ 0x0044648D
- `"COLOR="#%lX""` @ 0x00446493

## DATA Context

**Context around 0x00446484**:

- `"mldata.cpp"` @ 0x00446404
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
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3

**Context around 0x0044646D**:

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
- `"Precondition"` @ 0x004464C1

**Context around 0x0044648D**:

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
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3

**Context around 0x00446472**:

- `"deg;"` @ 0x004463F2
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
- `"Precondition"` @ 0x004464C1

**Context around 0x00446493**:

- `"ondition"` @ 0x00446413
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
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3

**Context around 0x0044647C**:

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
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE

## Functions Called

- 0x00403618
- 0x00438E6E
- 0x00438ED4
- 0x00438F64
- 0x00438DC6
- 0x00438D96
- 0x00438F64
- 0x00438DC6
- 0x00438D96
- 0x00438F64
- 0x00438FE8
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
- 0x00438FFA
- 0x00438F64
- 0x00438E6E
- 0x00438ED4
- 0x00438F64
- 0x00438DC6
- 0x00438D96
- 0x00438F64

---

*Extracted with recursive CALL following and DATA context*
