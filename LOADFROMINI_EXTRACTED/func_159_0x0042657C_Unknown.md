# LoadFromINI Function Analysis

**Function Address**: 0x0042657C
**Rank**: #159
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 81

```assembly
0042657C  push     ebp
0042657D  mov      ebp, esp
0042657F  push     ecx
00426580  push     ebx
00426581  push     esi
00426582  mov      ecx, dword ptr [ebp + 8]
00426585  lea      ebx, [ebp - 4]
00426588  mov      eax, dword ptr [ebp + 0xc]
0042658B  jmp      0x42659c
0042658D  mov      edx, dword ptr [ecx + 5]
00426590  mov      esi, eax
00426592  shl      esi, 2
00426595  add      edx, esi
00426597  xor      esi, esi
00426599  mov      dword ptr [edx], esi
0042659B  inc      eax
0042659C  mov      edx, dword ptr [ecx + 9]
0042659F  mov      dword ptr [ebx], edx
004265A1  mov      edx, dword ptr [ebx]
004265A3  cmp      edx, dword ptr [ebp + 0x10]
004265A6  jae      0x4265ac
004265A8  mov      edx, ebx
004265AA  jmp      0x4265af
004265AC  lea      edx, [ebp + 0x10]
004265AF  cmp      eax, dword ptr [edx]
004265B1  jb       0x42658d
004265B3  pop      esi
004265B4  pop      ebx
004265B5  pop      ecx
004265B6  pop      ebp
004265B7  ret      
004265B8  adc      eax, 0x3000000
004265BD  add      byte ptr [eax], dh
004265BF  add      byte ptr [eax], al
004265C1  add      byte ptr [eax], al
004265C3  add      byte ptr [edi], dh
004265C6  add      byte ptr [eax], al
004265C8  cmp      byte ptr [eax], al
004265CA  dec      eax
004265CB  add      byte ptr [eax], al
004265CD  add      byte ptr [eax], al
004265CF  add      byte ptr [eax], al
004265D1  add      byte ptr [eax], al
004265D3  add      byte ptr [eax], al
004265D5  add      byte ptr [eax], al
004265D7  add      byte ptr [edx], al
004265D9  add      byte ptr [eax], al
004265DB  add      byte ptr [edx], al
004265DD  add      byte ptr [eax], al
004265DF  add      byte ptr [eax], ah
004265E1  xchg     edi, eax
004265E2  inc      ebx
004265E3  add      byte ptr [ecx], al
004265E5  add      byte ptr [eax + eax + 0x54], cl
004265E9  dec      ebp
004265EA  outsd    dx, dword ptr [esi]
004265EB  jne      0x42665a
004265EE  add      byte ptr gs:[eax + 0x41c9], ah
004265F5  add      byte ptr [eax], al
004265F7  add      byte ptr [ebx], al
004265F9  add      byte ptr [eax], al
004265FB  add      byte ptr [eax], al
004265FD  add      byte ptr [eax], al
004265FF  add      byte ptr [eax], al
00426601  add      byte ptr [eax], al
00426603  add      byte ptr [eax], al
00426605  add      byte ptr [eax], al
00426607  add      byte ptr [ebp - 0x75], dl
0042660A  in       al, dx
0042660B  mov      eax, dword ptr [ebp + 8]
0042660E  cmp      dword ptr [eax + 8], 0
00426612  jbe      0x426620
00426614  cmp      dword ptr [eax + 0xc], 0
00426618  jbe      0x426620
0042661A  cmp      dword ptr [eax + 0x10], 0
0042661E  ja       0x426624
00426620  xor      eax, eax
00426622  jmp      0x426629
00426624  mov      eax, 1
00426629  pop      ebp
0042662A  ret      
```

## Strings Referenced

**Total unique strings**: 0



---

*Extracted with recursive CALL following and DATA context*
