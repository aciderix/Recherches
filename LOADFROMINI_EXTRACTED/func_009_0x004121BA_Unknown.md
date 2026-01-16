# LoadFromINI Function Analysis

**Function Address**: 0x004121BA
**Rank**: #9
**INI String Count**: 13
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 123

```assembly
004121BA  push     ebp
004121BB  mov      ebp, esp
004121BD  add      esp, -0x3c
004121C0  push     ebx
004121C1  mov      ebx, dword ptr [ebp + 8]
004121C4  mov      eax, 0x4405a4
004121C9  call     0x403618
004121CE  test     byte ptr [ebx + 0x31], 4
004121D2  setne    dl
004121D5  and      edx, 1
004121D8  test     dl, dl
004121DA  je       0x4121ed
004121DC  xor      eax, eax
004121DE  mov      edx, dword ptr [ebp - 0x2c]
004121E1  mov      dword ptr fs:[0], edx
004121E8  jmp      0x41231f
004121ED  mov      eax, dword ptr [ebp + 0xc]
004121F0  mov      edx, dword ptr [eax]
004121F2  mov      dword ptr [ebp - 0x34], edx
004121F5  mov      ecx, dword ptr [eax + 4]
004121F8  mov      dword ptr [ebp - 0x30], ecx
004121FB  test     byte ptr [ebx + 0x31], 1
004121FF  setne    al
00412202  and      eax, 1
00412205  test     al, al
00412207  je       0x41221f
00412209  xor      edx, edx
0041220B  mov      dword ptr [ebp - 0x3c], edx
0041220E  xor      ecx, ecx
00412210  mov      dword ptr [ebp - 0x38], ecx
00412213  mov      eax, dword ptr [ebp - 0x3c]
00412216  mov      dword ptr [ebp + 0x10], eax
00412219  mov      eax, dword ptr [ebp - 0x38]
0041221C  mov      dword ptr [ebp + 0x14], eax
0041221F  test     byte ptr [ebx + 0x31], 2
00412223  setne    dl
00412226  and      edx, 1
00412229  test     dl, dl
0041222B  je       0x412239
0041222D  xor      ecx, ecx
0041222F  mov      dword ptr [ebp + 0x18], ecx
00412232  mov      dword ptr [ebp + 0x1c], 0x3ff00000
00412239  lea      eax, [ebp + 0x10]
0041223C  push     eax
0041223D  push     dword ptr [ebp + 0x1c]
00412240  push     dword ptr [ebp + 0x18]
00412243  lea      ecx, [ebp - 0x34]
00412246  push     ecx
00412247  call     0x40501d
0041224C  add      esp, 0x10
0041224F  cmp      dword ptr [ebx + 0x35], 2
00412253  jbe      0x4122c6
00412255  mov      word ptr [ebp - 0x1c], 8
0041225B  push     2
0041225D  push     dword ptr [ebx + 0x35]
00412260  push     dword ptr [ebx + 0x39]
00412263  lea      eax, [ebp - 8]
00412266  push     eax
00412267  call     0x439696
0041226C  add      esp, 0x10
0041226F  inc      dword ptr [ebp - 0x10]
00412272  mov      word ptr [ebp - 0x1c], 0x14
00412278  push     dword ptr [ebp - 0x30]
0041227B  push     dword ptr [ebp - 0x34]
0041227E  push     dword ptr [ebp - 8]
00412281  call     0x4397ec
00412286  test     eax, eax
00412288  setne    dl
0041228B  and      edx, 1
0041228E  test     dl, dl
00412290  je       0x4122b3
00412292  mov      al, 1
00412294  push     eax
00412295  dec      dword ptr [ebp - 0x10]
00412298  push     2
0041229A  lea      edx, [ebp - 8]
0041229D  push     edx
0041229E  call     0x439690
004122A3  add      esp, 8
004122A6  pop      eax
004122A7  mov      edx, dword ptr [ebp - 0x2c]
004122AA  mov      dword ptr fs:[0], edx
004122B1  jmp      0x41231f
004122B3  dec      dword ptr [ebp - 0x10]
004122B6  push     2
004122B8  lea      ecx, [ebp - 8]
004122BB  push     ecx
004122BC  call     0x439690
004122C1  add      esp, 8
004122C4  jmp      0x412313
004122C6  cmp      dword ptr [ebx + 0x35], 2
004122CA  jne      0x412305
004122CC  mov      eax, dword ptr [ebx + 0x39]
004122CF  mov      edx, dword ptr [eax]
004122D1  cmp      edx, dword ptr [ebp - 0x34]
004122D4  jg       0x412313
004122D6  mov      ecx, dword ptr [ebx + 0x39]
004122D9  mov      eax, dword ptr [ecx + 8]
004122DC  cmp      eax, dword ptr [ebp - 0x34]
004122DF  jl       0x412313
004122E1  mov      edx, dword ptr [ebx + 0x39]
004122E4  mov      ecx, dword ptr [edx + 4]
004122E7  cmp      ecx, dword ptr [ebp - 0x30]
004122EA  jg       0x412313
004122EC  mov      eax, dword ptr [ebx + 0x39]
004122EF  mov      edx, dword ptr [eax + 0xc]
004122F2  cmp      edx, dword ptr [ebp - 0x30]
004122F5  jl       0x412313
004122F7  mov      al, 1
004122F9  mov      edx, dword ptr [ebp - 0x2c]
004122FC  mov      dword ptr fs:[0], edx
00412303  jmp      0x41231f
00412305  mov      al, 1
00412307  mov      edx, dword ptr [ebp - 0x2c]
0041230A  mov      dword ptr fs:[0], edx
00412311  jmp      0x41231f
00412313  xor      eax, eax
00412315  mov      edx, dword ptr [ebp - 0x2c]
00412318  mov      dword ptr fs:[0], edx
0041231F  pop      ebx
00412320  mov      esp, ebp
00412322  pop      ebp
00412323  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x0040501D
- 0x00439696
- 0x004397EC
- 0x00439690
- 0x00439690

---

*Extracted with recursive CALL following and DATA context*
