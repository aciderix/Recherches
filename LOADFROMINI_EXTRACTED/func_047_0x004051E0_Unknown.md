# LoadFromINI Function Analysis

**Function Address**: 0x004051E0
**Rank**: #47
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 65

```assembly
004051E0  push     ebp
004051E1  mov      ebp, esp
004051E3  add      esp, -8
004051E6  push     ebx
004051E7  push     esi
004051E8  push     edi
004051E9  mov      ebx, dword ptr [ebp + 0xc]
004051EC  mov      eax, dword ptr [ebx]
004051EE  mov      edx, dword ptr [eax + 6]
004051F1  inc      edx
004051F2  push     edx
004051F3  call     0x438e50
004051F8  pop      ecx
004051F9  mov      esi, eax
004051FB  mov      eax, dword ptr [ebx]
004051FD  push     dword ptr [eax + 2]
00405200  push     esi
00405201  call     0x438f0a
00405206  add      esp, 8
00405209  push     0x43a998
0040520E  push     esi
0040520F  call     0x438e74
00405214  add      esp, 8
00405217  mov      ebx, eax
00405219  xor      edi, edi
0040521B  mov      dword ptr [ebp - 8], ebx
0040521E  push     dword ptr [ebp - 8]
00405221  call     0x438eb0
00405226  pop      ecx
00405227  mov      word ptr [ebp - 2], ax
0040522B  push     0x43a99a
00405230  push     0
00405232  call     0x438e74
00405237  add      esp, 8
0040523A  mov      ebx, eax
0040523C  test     ebx, ebx
0040523E  je       0x40525d
00405240  mov      edi, ebx
00405242  push     edi
00405243  call     0x438eb0
00405248  pop      ecx
00405249  mov      edi, eax
0040524B  cmp      byte ptr [ebx + 1], 0
0040524F  jne      0x40525d
00405251  movzx    eax, di
00405254  mov      edx, eax
00405256  add      edx, edx
00405258  lea      edx, [edx + edx*4]
0040525B  mov      edi, edx
0040525D  movzx    ecx, di
00405260  movzx    eax, word ptr [ebp - 2]
00405264  shl      eax, 0x10
00405267  or       ecx, eax
00405269  mov      edx, dword ptr [ebp + 8]
0040526C  mov      dword ptr [edx + 4], ecx
0040526F  push     esi
00405270  call     0x438f82
00405275  pop      ecx
00405276  pop      edi
00405277  pop      esi
00405278  pop      ebx
00405279  pop      ecx
0040527A  pop      ecx
0040527B  pop      ebp
0040527C  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00438E50
- 0x00438F0A
- 0x00438E74
- 0x00438EB0
- 0x00438E74
- 0x00438EB0
- 0x00438F82

---

*Extracted with recursive CALL following and DATA context*
