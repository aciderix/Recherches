# LoadFromINI Function Analysis

**Function Address**: 0x00436FFE
**Rank**: #88
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 36

```assembly
00436FFE  push     ebp
00436FFF  mov      ebp, esp
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

- 0x00403618
- 0x004390E4
- 0x0043905A
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
