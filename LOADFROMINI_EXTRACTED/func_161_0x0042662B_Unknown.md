# LoadFromINI Function Analysis

**Function Address**: 0x0042662B
**Rank**: #161
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 41

```assembly
0042662B  push     ebp
0042662C  mov      ebp, esp
0042662E  push     ecx
0042662F  push     ebx
00426630  push     esi
00426631  push     edi
00426632  mov      eax, dword ptr [ebp + 8]
00426635  lea      esi, [eax + 0x14]
00426638  lea      edi, [eax + 0x10]
0042663B  lea      edx, [eax + 0xc]
0042663E  mov      dword ptr [ebp - 4], edx
00426641  add      eax, 8
00426644  mov      ebx, dword ptr [ebp + 0xc]
00426647  push     4
00426649  push     eax
0042664A  push     ebx
0042664B  call     0x439192
00426650  add      esp, 0xc
00426653  push     4
00426655  push     dword ptr [ebp - 4]
00426658  push     ebx
00426659  call     0x439192
0042665E  add      esp, 0xc
00426661  push     4
00426663  push     edi
00426664  push     ebx
00426665  call     0x439192
0042666A  add      esp, 0xc
0042666D  push     ebx
0042666E  call     0x439180
00426673  pop      ecx
00426674  test     eax, eax
00426676  setne    al
00426679  and      eax, 1
0042667C  mov      byte ptr [esi], al
0042667E  pop      edi
0042667F  pop      esi
00426680  pop      ebx
00426681  pop      ecx
00426682  pop      ebp
00426683  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00439192
- 0x00439192
- 0x00439192
- 0x00439180

---

*Extracted with recursive CALL following and DATA context*
