# LoadFromINI Function Analysis

**Function Address**: 0x0041EE33
**Rank**: #45
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 215

```assembly
0041EE33  push     ebp
0041EE34  mov      ebp, esp
0041EE36  add      esp, -0x24
0041EE39  push     ebx
0041EE3A  push     esi
0041EE3B  mov      ebx, dword ptr [ebp + 8]
0041EE3E  mov      eax, 0x444850
0041EE43  call     0x403618
0041EE48  test     ebx, ebx
0041EE4A  je       0x41ee83
0041EE4C  add      dword ptr [ebp - 8], 4
0041EE50  sub      dword ptr [ebp - 8], 3
0041EE54  lea      esi, [ebx + 4]
0041EE57  add      dword ptr [ebp - 8], 3
0041EE5B  sub      dword ptr [ebp - 8], 2
0041EE5F  add      dword ptr [ebp - 8], 2
0041EE63  dec      dword ptr [ebp - 8]
0041EE66  mov      dword ptr [esi + 1], 0x43b500
0041EE6D  push     dword ptr [esi + 5]
0041EE70  call     0x438f82
0041EE75  pop      ecx
0041EE76  test     byte ptr [ebp + 0xc], 1
0041EE7A  je       0x41ee83
0041EE7C  push     ebx
0041EE7D  call     0x438f16
0041EE82  pop      ecx
0041EE83  mov      eax, dword ptr [ebp - 0x24]
0041EE86  mov      dword ptr fs:[0], eax
0041EE8C  pop      esi
0041EE8D  pop      ebx
0041EE8E  mov      esp, ebp
0041EE90  pop      ebp
0041EE91  ret      
0041EE92  adc      eax, 0x3000000
0041EE97  add      byte ptr [eax], dh
0041EE99  add      byte ptr [ecx], al
0041EE9B  add      byte ptr [eax], al
0041EE9D  add      byte ptr [edi], dl
0041EEA0  add      byte ptr [eax], al
0041EEA2  pushal   
0041EEA3  add      byte ptr [eax], dh
0041EEA6  shr      dword ptr [edi + 0x40], 0
0041EEAA  add      dword ptr [eax], eax
0041EEAC  add      dword ptr [eax], eax
0041EEAE  iretd    
0041EEAF  outsd    dx, dword ptr [esi]
0041EEB0  inc      eax
0041EEB1  add      byte ptr [ebx], al
0041EEB3  add      byte ptr [eax], al
0041EEB5  add      byte ptr [ebx], al
0041EEB7  add      byte ptr [eax], al
0041EEB9  add      byte ptr [edx], cl
0041EEBB  out      dx, eax
0041EEBC  inc      ecx
0041EEBD  add      byte ptr [ecx], al
0041EEBF  add      byte ptr [eax + eax + 0x54], dh
0041EEC3  dec      ebp
0041EEC4  dec      ecx
0041EEC5  inc      ebx
0041EEC6  push     esi
0041EEC7  arpl     word ptr gs:[edi + ebp*2 + 0x72], si
0041EECC  dec      ecx
0041EECD  insd     dword ptr es:[edi], dx
0041EECE  jo       0x41ef0c
0041EED0  push     esp
0041EED1  push     esi
0041EED2  dec      esi
0041EED3  inc      edi
0041EED4  imul     ecx, dword ptr fs:[edi + 0x62], 0x7463656a
0041EEDC  sub      al, 0x54
0041EEDE  push     ebx
0041EEDF  je       0x41ef42
0041EEE1  outsb    dx, byte ptr [esi]
0041EEE2  popal    
0041EEE4  jb       0x41ef4a
0041EEE6  inc      ecx
0041EEE7  insb     byte ptr es:[edi], dx
0041EEE8  insb     byte ptr es:[edi], dx
0041EEE9  outsd    dx, dword ptr [esi]
0041EEEA  arpl     word ptr [ecx + 0x74], sp
0041EEED  outsd    dx, dword ptr [esi]
0041EEEE  jb       0x41ef2e
0041EEF0  add      byte ptr [eax], al
0041EEF2  popal    
0041EEF3  out      dx, eax
0041EEF4  inc      ecx
0041EEF5  add      byte ptr [eax], al
0041EEF7  add      byte ptr [eax], al
0041EEF9  add      byte ptr [ebx], al
0041EEFB  add      byte ptr [eax], al
0041EEFD  add      byte ptr [eax], al
0041EEFF  add      byte ptr [eax], al
0041EF01  add      byte ptr [eax], al
0041EF03  add      byte ptr [eax], al
0041EF05  add      byte ptr [eax], al
0041EF07  add      byte ptr [eax], al
0041EF09  add      byte ptr [ebp - 0x75], dl
0041EF0C  in       al, dx
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
- 0x00403618
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
