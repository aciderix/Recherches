# LoadFromINI Function Analysis

**Function Address**: 0x0041EF0A
**Rank**: #15
**INI String Count**: 8
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 119

```assembly
0041EF0A  push     ebp
0041EF0B  mov      ebp, esp
0041EF0D  add      esp, -0x24
0041EF10  push     ebx
0041EF11  push     esi
0041EF12  mov      ebx, dword ptr [ebp + 8]
0041EF15  mov      eax, 0x444858
0041EF1A  call     0x403618
0041EF1F  test     ebx, ebx
0041EF21  je       0x41ef51
0041EF23  add      dword ptr [ebp - 8], 3
0041EF27  sub      dword ptr [ebp - 8], 2
0041EF2B  add      dword ptr [ebp - 8], 2
0041EF2F  dec      dword ptr [ebp - 8]
0041EF32  mov      dword ptr [ebx + 1], 0x43b500
0041EF39  push     dword ptr [ebx + 5]
0041EF3C  call     0x438f82
0041EF41  pop      ecx
0041EF42  test     byte ptr [ebp + 0xc], 1
0041EF46  je       0x41ef51
0041EF48  mov      esi, ebx
0041EF4A  push     esi
0041EF4B  call     0x438f16
0041EF50  pop      ecx
0041EF51  mov      edx, dword ptr [ebp - 0x24]
0041EF54  mov      dword ptr fs:[0], edx
0041EF5B  pop      esi
0041EF5C  pop      ebx
0041EF5D  mov      esp, ebp
0041EF5F  pop      ebp
0041EF60  ret      
0041EF61  or       eax, 0x3000000
0041EF66  add      byte ptr [eax], dh
0041EF68  add      byte ptr [ecx], al
0041EF6A  add      byte ptr [eax], al
0041EF6C  add      byte ptr [edi], dl
0041EF6F  add      byte ptr [eax], al
0041EF71  pushal   
0041EF72  add      byte ptr [eax], dh
0041EF75  shr      dword ptr [edi + 0x40], 0
0041EF79  add      dword ptr [eax], eax
0041EF7B  add      dword ptr [eax], eax
0041EF7D  iretd    
0041EF7E  outsd    dx, dword ptr [esi]
0041EF7F  inc      eax
0041EF80  add      byte ptr [edx], al
0041EF82  add      byte ptr [eax], al
0041EF84  add      byte ptr [edx], al
0041EF86  add      byte ptr [eax], al
0041EF88  add      cl, bl
0041EF8A  out      dx, eax
0041EF8B  inc      ecx
0041EF8C  add      byte ptr [ecx], al
0041EF8E  add      byte ptr [eax + eax + 0x54], dh
0041EF92  dec      ebp
0041EF93  dec      ecx
0041EF94  push     esi
0041EF95  arpl     word ptr gs:[edi + ebp*2 + 0x72], si
0041EF9A  dec      ecx
0041EF9B  insd     dword ptr es:[edi], dx
0041EF9C  jo       0x41efda
0041EF9E  push     esp
0041EF9F  push     esi
0041EFA0  dec      esi
0041EFA1  inc      edi
0041EFA2  imul     ecx, dword ptr fs:[edi + 0x62], 0x7463656a
0041EFAA  sub      al, 0x54
0041EFAC  push     ebx
0041EFAD  je       0x41f010
0041EFAF  outsb    dx, byte ptr [esi]
0041EFB0  popal    
0041EFB2  jb       0x41f018
0041EFB4  inc      ecx
0041EFB5  insb     byte ptr es:[edi], dx
0041EFB6  insb     byte ptr es:[edi], dx
0041EFB7  outsd    dx, dword ptr [esi]
0041EFB8  arpl     word ptr [ecx + 0x74], sp
0041EFBB  outsd    dx, dword ptr [esi]
0041EFBC  jb       0x41effc
0041EFBE  add      byte ptr [eax], al
0041EFC0  add      byte ptr [ebp + 0x406c], dh
0041EFC6  add      byte ptr [eax], al
0041EFC8  add      byte ptr [ebx], al
0041EFCA  add      byte ptr [eax], al
0041EFCC  add      byte ptr [eax], al
0041EFCE  add      byte ptr [eax], al
0041EFD0  add      byte ptr [eax], al
0041EFD2  add      byte ptr [eax], al
0041EFD4  add      byte ptr [eax], al
0041EFD6  add      byte ptr [eax], al
0041EFD8  add      byte ptr [ebp - 0x75], dl
0041EFDB  in       al, dx
0041EFDC  add      esp, -0x24
0041EFDF  push     ebx
0041EFE0  push     esi
0041EFE1  mov      ebx, dword ptr [ebp + 8]
0041EFE4  mov      eax, 0x444860
0041EFE9  call     0x403618
0041EFEE  test     ebx, ebx
0041EFF0  je       0x41f018
0041EFF2  add      dword ptr [ebp - 8], 2
0041EFF6  dec      dword ptr [ebp - 8]
0041EFF9  mov      dword ptr [ebx + 1], 0x43b500
0041F000  push     dword ptr [ebx + 5]
0041F003  call     0x438f82
0041F008  pop      ecx
0041F009  test     byte ptr [ebp + 0xc], 1
0041F00D  je       0x41f018
0041F00F  mov      esi, ebx
0041F011  push     esi
0041F012  call     0x438f16
0041F017  pop      ecx
0041F018  mov      edx, dword ptr [ebp - 0x24]
0041F01B  mov      dword ptr fs:[0], edx
0041F022  pop      esi
0041F023  pop      ebx
0041F024  mov      esp, ebp
0041F026  pop      ebp
0041F027  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438F82
- 0x00438F16
- 0x00403618
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
