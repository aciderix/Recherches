# LoadFromINI Function Analysis

**Function Address**: 0x00401FC8
**Rank**: #112
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 61

```assembly
00401FC8  push     ebp
00401FC9  mov      ebp, esp
00401FCB  add      esp, -0x24
00401FCE  mov      eax, 0x44e58e
00401FD3  push     ebx
00401FD4  push     esi
00401FD5  mov      ebx, dword ptr [ebp + 0xc]
00401FD8  call     0x403618
00401FDD  mov      word ptr [ebp - 0x14], 8
00401FE3  mov      edx, dword ptr [ebp + 8]
00401FE6  xor      ecx, ecx
00401FE8  mov      dword ptr [edx], ecx
00401FEA  push     0x105
00401FEF  call     0x438e50
00401FF4  pop      ecx
00401FF5  mov      esi, eax
00401FF7  mov      eax, dword ptr [ebp + 8]
00401FFA  mov      dword ptr [eax + 4], esi
00401FFD  mov      eax, esi
00401FFF  mov      edx, dword ptr [ebx + 4]
00402002  push     0x105
00402007  push     eax
00402008  push     edx
00402009  mov      ecx, dword ptr [ebx]
0040200B  push     dword ptr [ecx]
0040200D  call     0x4398b2
00402012  push     dword ptr [ebp + 8]
00402015  push     dword ptr [ebp + 0x10]
00402018  push     0
0040201A  mov      eax, dword ptr [ebp + 8]
0040201D  push     dword ptr [eax + 4]
00402020  mov      edx, dword ptr [ebx]
00402022  push     dword ptr [edx]
00402024  call     0x4398a6
00402029  mov      ecx, dword ptr [ebp + 8]
0040202C  mov      byte ptr [ecx + 0x10], 1
00402030  push     0
00402032  push     0
00402034  push     0
00402036  push     0
00402038  mov      eax, dword ptr [ebp + 8]
0040203B  add      eax, 0xc
0040203E  push     eax
0040203F  push     0
00402041  push     0
00402043  mov      edx, dword ptr [ebp + 8]
00402046  add      edx, 8
00402049  push     edx
0040204A  push     0
0040204C  push     0
0040204E  push     dword ptr [ebp + 8]
00402051  call     0x40215c
00402056  add      esp, 0x2c
00402059  mov      ecx, dword ptr [ebp - 0x24]
0040205C  mov      dword ptr fs:[0], ecx
00402063  mov      eax, dword ptr [ebp + 8]
00402066  pop      esi
00402067  pop      ebx
00402068  mov      esp, ebp
0040206A  pop      ebp
0040206B  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438E50
- 0x004398B2
- 0x004398A6
- 0x0040215C

---

*Extracted with recursive CALL following and DATA context*
