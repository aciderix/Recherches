# LoadFromINI Function Analysis

**Function Address**: 0x00418CE8
**Rank**: #42
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 118

```assembly
00418CE8  push     ebp
00418CE9  mov      ebp, esp
00418CEB  add      esp, -0x24
00418CEE  push     ebx
00418CEF  push     esi
00418CF0  mov      ebx, dword ptr [ebp + 8]
00418CF3  mov      eax, 0x442878
00418CF8  call     0x403618
00418CFD  test     ebx, ebx
00418CFF  je       0x418d2f
00418D01  add      dword ptr [ebp - 8], 3
00418D05  sub      dword ptr [ebp - 8], 2
00418D09  add      dword ptr [ebp - 8], 2
00418D0D  dec      dword ptr [ebp - 8]
00418D10  mov      dword ptr [ebx + 1], 0x43b500
00418D17  push     dword ptr [ebx + 5]
00418D1A  call     0x438f82
00418D1F  pop      ecx
00418D20  test     byte ptr [ebp + 0xc], 1
00418D24  je       0x418d2f
00418D26  mov      esi, ebx
00418D28  push     esi
00418D29  call     0x438f16
00418D2E  pop      ecx
00418D2F  mov      edx, dword ptr [ebp - 0x24]
00418D32  mov      dword ptr fs:[0], edx
00418D39  pop      esi
00418D3A  pop      ebx
00418D3B  mov      esp, ebp
00418D3D  pop      ebp
00418D3E  ret      
00418D3F  or       eax, 0x3000000
00418D44  add      byte ptr [eax], dh
00418D46  add      byte ptr [ecx], al
00418D48  add      byte ptr [eax], al
00418D4A  add      byte ptr [edi], dl
00418D4D  add      byte ptr [eax], al
00418D4F  pop      esp
00418D50  add      byte ptr [eax + eax - 0x3f], ch
00418D54  outsd    dx, dword ptr [esi]
00418D55  inc      eax
00418D56  add      byte ptr [ecx], al
00418D58  add      byte ptr [ecx], al
00418D5A  add      bh, cl
00418D5C  outsd    dx, dword ptr [esi]
00418D5D  inc      eax
00418D5E  add      byte ptr [edx], al
00418D60  add      byte ptr [eax], al
00418D62  add      byte ptr [edx], al
00418D64  add      byte ptr [eax], al
00418D66  add      byte ptr [ebx + 0x100418d], dh
00418D6C  add      byte ptr [eax], dh
00418D6F  push     esp
00418D70  dec      ebp
00418D71  dec      ecx
00418D72  push     esi
00418D73  arpl     word ptr gs:[edi + ebp*2 + 0x72], si
00418D78  dec      ecx
00418D79  insd     dword ptr es:[edi], dx
00418D7A  jo       0x418db8
00418D7C  push     esp
00418D7D  push     esi
00418D7E  dec      esi
00418D7F  push     ebx
00418D80  arpl     word ptr [ebp + 0x6e], sp
00418D83  sub      al, 0x54
00418D86  push     ebx
00418D87  je       0x418dea
00418D89  outsb    dx, byte ptr [esi]
00418D8A  popal    
00418D8C  jb       0x418df2
00418D8E  inc      ecx
00418D8F  insb     byte ptr es:[edi], dx
00418D90  insb     byte ptr es:[edi], dx
00418D91  outsd    dx, dword ptr [esi]
00418D92  arpl     word ptr [ecx + 0x74], sp
00418D95  outsd    dx, dword ptr [esi]
00418D96  jb       0x418dd6
00418D98  add      byte ptr [eax], al
00418D9A  add      byte ptr [ebp + 0x406c], dh
00418DA0  add      byte ptr [eax], al
00418DA2  add      byte ptr [ebx], al
00418DA4  add      byte ptr [eax], al
00418DA6  add      byte ptr [eax], al
00418DA8  add      byte ptr [eax], al
00418DAA  add      byte ptr [eax], al
00418DAC  add      byte ptr [eax], al
00418DAE  add      byte ptr [eax], al
00418DB0  add      byte ptr [eax], al
00418DB2  add      byte ptr [ebp - 0x75], dl
00418DB5  in       al, dx
00418DB6  add      esp, -0x24
00418DB9  push     ebx
00418DBA  push     esi
00418DBB  mov      ebx, dword ptr [ebp + 8]
00418DBE  mov      eax, 0x4428b0
00418DC3  call     0x403618
00418DC8  test     ebx, ebx
00418DCA  je       0x418df2
00418DCC  add      dword ptr [ebp - 8], 2
00418DD0  dec      dword ptr [ebp - 8]
00418DD3  mov      dword ptr [ebx + 1], 0x43b500
00418DDA  push     dword ptr [ebx + 5]
00418DDD  call     0x438f82
00418DE2  pop      ecx
00418DE3  test     byte ptr [ebp + 0xc], 1
00418DE7  je       0x418df2
00418DE9  mov      esi, ebx
00418DEB  push     esi
00418DEC  call     0x438f16
00418DF1  pop      ecx
00418DF2  mov      edx, dword ptr [ebp - 0x24]
00418DF5  mov      dword ptr fs:[0], edx
00418DFC  pop      esi
00418DFD  pop      ebx
00418DFE  mov      esp, ebp
00418E00  pop      ebp
00418E01  ret      
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
