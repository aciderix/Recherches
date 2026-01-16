# LoadFromINI Function Analysis

**Function Address**: 0x0040235F
**Rank**: #117
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 42

```assembly
0040235F  push     ebp
00402360  mov      ebp, esp
00402362  add      esp, -0x24
00402365  mov      eax, 0x44e65a
0040236A  call     0x403618
0040236F  mov      word ptr [ebp - 0x14], 8
00402375  mov      edx, dword ptr [ebp + 8]
00402378  mov      ecx, dword ptr [ebp + 0xc]
0040237B  mov      dword ptr [edx], ecx
0040237D  mov      eax, dword ptr [ebp + 8]
00402380  mov      edx, dword ptr [ebp + 0x10]
00402383  mov      dword ptr [eax + 4], edx
00402386  xor      eax, eax
00402388  mov      ecx, dword ptr [ebp + 8]
0040238B  mov      dword ptr [ecx + 8], eax
0040238E  xor      ecx, ecx
00402390  mov      edx, dword ptr [ebp + 8]
00402393  mov      dword ptr [edx + 0x10], ecx
00402396  xor      edx, edx
00402398  mov      eax, dword ptr [ebp + 8]
0040239B  mov      dword ptr [eax + 0x14], edx
0040239E  mov      ecx, dword ptr [ebp + 8]
004023A1  mov      eax, dword ptr [ebp + 8]
004023A4  mov      edx, dword ptr [ebp + 8]
004023A7  add      eax, 0x14
004023AA  mov      ecx, dword ptr [ecx + 4]
004023AD  push     eax
004023AE  add      edx, 0xc
004023B1  push     0
004023B3  push     edx
004023B4  push     0
004023B6  push     ecx
004023B7  mov      eax, dword ptr [ebp + 8]
004023BA  mov      edx, dword ptr [eax]
004023BC  push     dword ptr [edx]
004023BE  call     0x439894
004023C3  mov      eax, dword ptr [ebp - 0x24]
004023C6  mov      dword ptr fs:[0], eax
004023CC  mov      eax, dword ptr [ebp + 8]
004023CF  mov      esp, ebp
004023D1  pop      ebp
004023D2  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00439894

---

*Extracted with recursive CALL following and DATA context*
