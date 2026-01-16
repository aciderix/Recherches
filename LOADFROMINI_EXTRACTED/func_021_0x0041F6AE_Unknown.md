# LoadFromINI Function Analysis

**Function Address**: 0x0041F6AE
**Rank**: #21
**INI String Count**: 8
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 66

```assembly
0041F6AE  push     ebp
0041F6AF  mov      ebp, esp
0041F6B1  add      esp, 0xffffff4c
0041F6B7  push     ebx
0041F6B8  mov      ebx, dword ptr [ebp + 8]
0041F6BB  mov      eax, 0x444d98
0041F6C0  call     0x403618
0041F6C5  push     ebx
0041F6C6  call     0x421aaf
0041F6CB  pop      ecx
0041F6CC  mov      edx, dword ptr [ebp + 0x10]
0041F6CF  mov      dword ptr [ebx + 0x3a], edx
0041F6D2  mov      word ptr [ebp - 0xa4], 8
0041F6DB  mov      ecx, dword ptr [0x4558f4]
0041F6E1  push     dword ptr [ecx]
0041F6E3  push     1
0041F6E5  mov      eax, dword ptr [ebp + 0xc]
0041F6E8  mov      edx, dword ptr [eax]
0041F6EA  push     dword ptr [edx + 2]
0041F6ED  push     0
0041F6EF  lea      ecx, [ebp - 0x90]
0041F6F5  push     ecx
0041F6F6  call     0x438e7a
0041F6FB  add      esp, 0x14
0041F6FE  add      dword ptr [ebp - 0x98], 6
0041F705  mov      word ptr [ebp - 0xa4], 0x14
0041F70E  mov      eax, dword ptr [ebp - 0x90]
0041F714  test     byte ptr [eax + 0xc], 0x86
0041F718  je       0x41f745
0041F71A  xor      eax, eax
0041F71C  push     eax
0041F71D  sub      dword ptr [ebp - 0x98], 6
0041F724  push     2
0041F726  lea      edx, [ebp - 0x90]
0041F72C  push     edx
0041F72D  call     0x438e0e
0041F732  add      esp, 8
0041F735  pop      eax
0041F736  mov      edx, dword ptr [ebp - 0xb4]
0041F73C  mov      dword ptr fs:[0], edx
0041F743  jmp      0x41f78b
0041F745  lea      ecx, [ebp - 0x4c]
0041F748  push     ecx
0041F749  add      ebx, 0x36
0041F74C  push     ebx
0041F74D  call     0x438f4c
0041F752  add      esp, 8
0041F755  lea      eax, [ebp - 0x90]
0041F75B  push     eax
0041F75C  call     0x438e56
0041F761  pop      ecx
0041F762  mov      al, 1
0041F764  push     eax
0041F765  sub      dword ptr [ebp - 0x98], 6
0041F76C  push     2
0041F76E  lea      edx, [ebp - 0x90]
0041F774  push     edx
0041F775  call     0x438e0e
0041F77A  add      esp, 8
0041F77D  pop      eax
0041F77E  mov      edx, dword ptr [ebp - 0xb4]
0041F784  mov      dword ptr fs:[0], edx
0041F78B  pop      ebx
0041F78C  mov      esp, ebp
0041F78E  pop      ebp
0041F78F  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00421AAF
- 0x00438E7A
- 0x00438E0E
- 0x00438F4C
- 0x00438E56
- 0x00438E0E

---

*Extracted with recursive CALL following and DATA context*
