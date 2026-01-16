# LoadFromINI Function Analysis

**Function Address**: 0x0041FF8F
**Rank**: #85
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 120

```assembly
0041FF8F  push     ebp
0041FF90  mov      ebp, esp
0041FF92  add      esp, 0xfffffed8
0041FF98  push     ebx
0041FF99  push     esi
0041FF9A  push     edi
0041FF9B  mov      eax, dword ptr [ebp + 0x1c]
0041FF9E  mov      edi, dword ptr [ebp + 0x10]
0041FFA1  mov      ebx, dword ptr [ebp + 0xc]
0041FFA4  test     al, al
0041FFA6  je       0x41ffc4
0041FFA8  and      eax, 0xff
0041FFAD  push     eax
0041FFAE  push     0x4464a0
0041FFB3  lea      edx, [ebp - 0x128]
0041FFB9  push     edx
0041FFBA  call     0x438dd8
0041FFBF  add      esp, 0xc
0041FFC2  jmp      0x41ffd8
0041FFC4  push     0x4464a4
0041FFC9  lea      ecx, [ebp - 0x128]
0041FFCF  push     ecx
0041FFD0  call     0x438f0a
0041FFD5  add      esp, 8
0041FFD8  lea      eax, [ebp - 0x128]
0041FFDE  push     eax
0041FFDF  call     0x438e68
0041FFE4  pop      ecx
0041FFE5  mov      esi, eax
0041FFE7  cmp      byte ptr [ebp + 0x18], 0
0041FFEB  je       0x420091
0041FFF1  mov      eax, dword ptr [ebp + 8]
0041FFF4  test     byte ptr [eax + 0x3a], 3
0041FFF8  je       0x420091
0041FFFE  push     dword ptr [0x455ad4]
00420004  push     ebx
00420005  lea      edx, [ebp - 4]
00420008  push     edx
00420009  mov      ecx, dword ptr [ebx + 5]
0042000C  call     dword ptr [ecx + 0x24]
0042000F  add      esp, 0xc
00420012  mov      eax, esi
00420014  mov      edx, dword ptr [ebp + 0x14]
00420017  mov      ecx, dword ptr [edi + 4]
0042001A  inc      ecx
0042001B  mov      dword ptr [ebp - 8], ecx
0042001E  mov      ecx, dword ptr [edi]
00420020  inc      ecx
00420021  mov      dword ptr [ebp - 0xc], ecx
00420024  mov      ecx, dword ptr [ebp - 0xc]
00420027  mov      dword ptr [ebp - 0x14], ecx
0042002A  mov      ecx, dword ptr [ebp - 8]
0042002D  mov      dword ptr [ebp - 0x10], ecx
00420030  push     0
00420032  push     eax
00420033  lea      eax, [ebp - 0x128]
00420039  push     eax
0042003A  push     edx
0042003B  push     4
0042003D  push     dword ptr [ebp - 0x10]
00420040  push     dword ptr [ebp - 0x14]
00420043  push     ebx
00420044  mov      edx, dword ptr [ebx + 5]
00420047  call     dword ptr [edx + 0x48]
0042004A  add      esp, 0x20
0042004D  mov      eax, dword ptr [ebp + 8]
00420050  test     byte ptr [eax + 0x3a], 2
00420054  je       0x420091
00420056  mov      eax, esi
00420058  mov      edx, dword ptr [ebp + 0x14]
0042005B  mov      ecx, dword ptr [edi + 4]
0042005E  dec      ecx
0042005F  mov      dword ptr [ebp - 0x18], ecx
00420062  mov      ecx, dword ptr [edi]
00420064  dec      ecx
00420065  mov      dword ptr [ebp - 0x1c], ecx
00420068  mov      ecx, dword ptr [ebp - 0x1c]
0042006B  mov      dword ptr [ebp - 0x24], ecx
0042006E  mov      ecx, dword ptr [ebp - 0x18]
00420071  mov      dword ptr [ebp - 0x20], ecx
00420074  push     0
00420076  push     eax
00420077  lea      eax, [ebp - 0x128]
0042007D  push     eax
0042007E  push     edx
0042007F  push     4
00420081  push     dword ptr [ebp - 0x20]
00420084  push     dword ptr [ebp - 0x24]
00420087  push     ebx
00420088  mov      edx, dword ptr [ebx + 5]
0042008B  call     dword ptr [edx + 0x48]
0042008E  add      esp, 0x20
00420091  push     dword ptr [0x455ad8]
00420097  push     ebx
00420098  lea      eax, [ebp - 0x28]
0042009B  push     eax
0042009C  mov      edx, dword ptr [ebx + 5]
0042009F  call     dword ptr [edx + 0x24]
004200A2  add      esp, 0xc
004200A5  mov      edx, esi
004200A7  mov      esi, dword ptr [ebp + 0x14]
004200AA  mov      eax, edi
004200AC  push     0
004200AE  push     edx
004200AF  lea      edx, [ebp - 0x128]
004200B5  push     edx
004200B6  push     esi
004200B7  push     4
004200B9  push     dword ptr [eax + 4]
004200BC  push     dword ptr [eax]
004200BE  push     ebx
004200BF  mov      ecx, dword ptr [ebx + 5]
004200C2  call     dword ptr [ecx + 0x48]
004200C5  add      esp, 0x20
004200C8  pop      edi
004200C9  pop      esi
004200CA  pop      ebx
004200CB  mov      esp, ebp
004200CD  pop      ebp
004200CE  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"%u."` @ 0x004464A0

## DATA Context

**Context around 0x004464A0**:

- `"s New Roman"` @ 0x00446420
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
- `"Precondition"` @ 0x00446515

## Functions Called

- 0x00438DD8
- 0x00438F0A
- 0x00438E68

---

*Extracted with recursive CALL following and DATA context*
