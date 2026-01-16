# LoadFromINI Function Analysis

**Function Address**: 0x00436F85
**Rank**: #87
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 90

```assembly
00436F85  push     ebp
00436F86  mov      ebp, esp
00436F88  push     ebx
00436F89  mov      ebx, dword ptr [ebp + 8]
00436F8C  test     ebx, ebx
00436F8E  je       0x436fab
00436F90  mov      dword ptr [ebx], 0x44d474
00436F96  push     dword ptr [ebx + 4]
00436F99  call     0x43905a
00436F9E  test     byte ptr [ebp + 0xc], 1
00436FA2  je       0x436fab
00436FA4  push     ebx
00436FA5  call     0x438f16
00436FAA  pop      ecx
00436FAB  pop      ebx
00436FAC  pop      ebp
00436FAD  ret      
00436FAE  or       dword ptr [eax], eax
00436FB0  add      byte ptr [eax], al
00436FB2  add      eax, dword ptr [eax]
00436FB4  xor      byte ptr [eax], al
00436FB6  add      byte ptr [eax], al
00436FB8  add      byte ptr [eax], al
00436FBA  push     edi
00436FBB  add      byte ptr [eax], al
00436FBD  add      byte ptr [eax], bh
00436FBF  add      byte ptr [eax], cl
00436FC2  add      byte ptr [eax], al
00436FC4  add      byte ptr [eax], al
00436FC6  add      byte ptr [eax], al
00436FC8  add      byte ptr [eax], al
00436FCA  add      byte ptr [eax], al
00436FCC  add      byte ptr [eax], al
00436FCE  add      al, byte ptr [eax]
00436FD0  add      byte ptr [eax], al
00436FD2  add      al, byte ptr [eax]
00436FD4  add      byte ptr [eax], al
00436FD6  outsb    dx, byte ptr [esi]
00436FD7  jo       0x43701c
00436FD9  add      byte ptr [ecx], al
00436FDB  add      byte ptr [eax + eax + 0x54], cl
00436FDF  dec      ebp
00436FE0  jne      0x437056
00436FE2  js       0x436fe5
00436FE5  add      byte ptr [0x436f], bh
00436FEB  add      byte ptr [eax], al
00436FED  add      byte ptr [ebx], al
00436FEF  add      byte ptr [eax], al
00436FF1  add      byte ptr [eax], al
00436FF3  add      byte ptr [eax], al
00436FF5  add      byte ptr [eax], al
00436FF7  add      byte ptr [eax], al
00436FF9  add      byte ptr [eax], al
00436FFB  add      byte ptr [eax], al
00436FFD  add      byte ptr [ebp - 0x75], dl
00437000  in       al, dx
00437001  add      esp, -0x28
00437004  push     ebx
00437005  mov      ebx, dword ptr [ebp + 8]
00437008  mov      eax, 0x44d314
0043700D  call     0x403618
00437012  test     ebx, ebx
00437014  je       0x437060
00437016  call     0x4390e4
0043701B  test     al, al
0043701D  je       0x437053
0043701F  mov      dword ptr [ebp - 4], ebx
00437022  cmp      dword ptr [ebp - 4], 0
00437026  je       0x437053
00437028  sub      dword ptr [ebp - 0xc], 2
0043702C  mov      word ptr [ebp - 0x18], 0x14
00437032  add      dword ptr [ebp - 0xc], 2
00437036  dec      dword ptr [ebp - 0xc]
00437039  mov      edx, dword ptr [ebp - 4]
0043703C  mov      dword ptr [edx], 0x44d474
00437042  mov      ecx, dword ptr [ebp - 4]
00437045  push     dword ptr [ecx + 4]
00437048  call     0x43905a
0043704D  mov      word ptr [ebp - 0x18], 8
00437053  test     byte ptr [ebp + 0xc], 1
00437057  je       0x437060
00437059  push     ebx
0043705A  call     0x438f16
0043705F  pop      ecx
00437060  mov      eax, dword ptr [ebp - 0x28]
00437063  mov      dword ptr fs:[0], eax
00437069  pop      ebx
0043706A  mov      esp, ebp
0043706C  pop      ebp
0043706D  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x0043905A
- 0x00438F16
- 0x00403618
- 0x004390E4
- 0x0043905A
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
