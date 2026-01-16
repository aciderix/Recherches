# LoadFromINI Function Analysis

**Function Address**: 0x004023D3
**Rank**: #118
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 53

```assembly
004023D3  push     ebp
004023D4  mov      ebp, esp
004023D6  add      esp, -0x28
004023D9  mov      eax, 0x44e67e
004023DE  push     ebx
004023DF  push     esi
004023E0  mov      ebx, dword ptr [ebp + 0xc]
004023E3  call     0x403618
004023E8  mov      word ptr [ebp - 0x14], 8
004023EE  mov      edx, dword ptr [ebp + 8]
004023F1  mov      ecx, dword ptr [ebx]
004023F3  mov      dword ptr [edx], ecx
004023F5  mov      eax, dword ptr [ebp + 8]
004023F8  xor      edx, edx
004023FA  mov      dword ptr [eax + 0x10], edx
004023FD  mov      dword ptr [ebp - 0x28], 0x104
00402404  push     dword ptr [ebp - 0x28]
00402407  call     0x438e50
0040240C  pop      ecx
0040240D  mov      ecx, dword ptr [ebp + 8]
00402410  mov      dword ptr [ecx + 8], eax
00402413  mov      edx, dword ptr [ebp + 8]
00402416  mov      dword ptr [edx + 4], eax
00402419  xor      eax, eax
0040241B  mov      ecx, dword ptr [ebp + 8]
0040241E  mov      dword ptr [ecx + 0x14], eax
00402421  mov      ecx, dword ptr [ebp + 8]
00402424  mov      eax, dword ptr [ebp + 8]
00402427  mov      edx, dword ptr [ebp + 8]
0040242A  add      eax, 0x14
0040242D  mov      esi, dword ptr [ecx + 8]
00402430  mov      ecx, dword ptr [ebx + 4]
00402433  push     eax
00402434  add      edx, 0xc
00402437  push     0
00402439  push     edx
0040243A  lea      eax, [ebp - 0x28]
0040243D  push     0
0040243F  push     eax
00402440  push     esi
00402441  push     ecx
00402442  mov      edx, dword ptr [ebp + 8]
00402445  mov      eax, dword ptr [edx]
00402447  push     dword ptr [eax]
00402449  call     0x4398ac
0040244E  mov      edx, dword ptr [ebp - 0x24]
00402451  mov      dword ptr fs:[0], edx
00402458  mov      eax, dword ptr [ebp + 8]
0040245B  pop      esi
0040245C  pop      ebx
0040245D  mov      esp, ebp
0040245F  pop      ebp
00402460  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438E50
- 0x004398AC

---

*Extracted with recursive CALL following and DATA context*
