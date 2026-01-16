# LoadFromINI Function Analysis

**Function Address**: 0x0043591A
**Rank**: #177
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 125

```assembly
0043591A  push     ebp
0043591B  mov      ebp, esp
0043591D  mov      al, 1
0043591F  pop      ebp
00435920  ret      
00435921  add      al, 0
00435923  add      byte ptr [eax], al
00435925  nop      
00435926  add      byte ptr [eax + eax], cl
00435929  pushfd   
0043592A  inc      ebx
0043592C  add      byte ptr [esi + edx*2 + 0x4e], dl
00435930  push     edi
00435931  imul     ebp, dword ptr [esi + 0x64], 0x2a20776f
00435938  add      byte ptr [eax + eax], al
0043593B  add      byte ptr [eax], al
0043593D  nop      
0043593E  add      byte ptr [eax + eax], cl
00435941  dec      eax
00435942  inc      ebx
00435944  add      byte ptr [esi + edx*2 + 0x4e], dl
00435948  inc      ebx
00435949  inc      esp
0043594A  inc      ecx
0043594B  dec      ebp
0043594C  imul     esp, dword ptr fs:[ecx + 0x20], 0x4002a
00435955  add      byte ptr [eax], al
00435957  nop      
00435958  add      byte ptr [eax + eax], cl
0043595B  fsub     qword ptr [ebx + 0x43]
0043595E  add      byte ptr [esi + edx*2 + 0x4e], dl
00435962  inc      ecx
00435963  jbe      0x4359ce
00435965  dec      ebp
00435966  imul     esp, dword ptr fs:[ecx + 0x20], 0x4002a
0043596F  add      byte ptr [eax], al
00435971  nop      
00435972  add      byte ptr [eax + eax], cl
00435975  mov      byte ptr [ebx + 0x43], ah
00435978  add      byte ptr [ebx + eax*2 + 0x6c], dl
0043597C  imul     esp, dword ptr [ebp + 0x6e], 0x20434474
00435983  sub      al, byte ptr [eax]
00435985  add      al, 0
00435987  add      byte ptr [eax], al
00435989  nop      
0043598A  add      byte ptr [eax + eax], cl
0043598D  xor      byte ptr [ebx + 0x43], ah
00435990  add      byte ptr [esi + edx*2 + 0x4e], dl
00435994  inc      edx
00435995  imul     edx, dword ptr [ebp + 0x78], 0x74
0043599A  jne      0x435a0e
0043599C  and      byte ptr gs:[edx], ch
0043599F  add      byte ptr [ebp - 0x75], dl
004359A2  in       al, dx
004359A3  add      esp, -0x28
004359A6  push     ebx
004359A7  push     esi
004359A8  mov      esi, dword ptr [ebp + 0xc]
004359AB  mov      ebx, dword ptr [ebp + 8]
004359AE  mov      eax, 0x44bf74
004359B3  call     0x403618
004359B8  cmp      esi, dword ptr [ebx + 9]
004359BB  jb       0x4359ce
004359BD  xor      eax, eax
004359BF  mov      edx, dword ptr [ebp - 0x28]
004359C2  mov      dword ptr fs:[0], edx
004359C9  jmp      0x435a64
004359CE  cmp      dword ptr [ebp + 0x10], 0
004359D2  je       0x4359fc
004359D4  mov      ecx, dword ptr [ebx + 5]
004359D7  mov      eax, dword ptr [ecx + esi*4]
004359DA  mov      dword ptr [ebp - 4], eax
004359DD  cmp      dword ptr [ebp - 4], 0
004359E1  je       0x4359fc
004359E3  mov      word ptr [ebp - 0x18], 0x14
004359E9  push     3
004359EB  mov      edx, dword ptr [ebp - 4]
004359EE  push     edx
004359EF  mov      ecx, dword ptr [edx]
004359F1  call     dword ptr [ecx]
004359F3  add      esp, 8
004359F6  mov      word ptr [ebp - 0x18], 8
004359FC  cmp      esi, dword ptr [ebx + 0xd]
004359FF  jb       0x435a21
00435A01  lea      eax, [esi + 1]
00435A04  push     eax
00435A05  push     esi
00435A06  push     ebx
00435A07  mov      edx, dword ptr [ebx + 1]
00435A0A  call     dword ptr [edx + 0xc]
00435A0D  add      esp, 0xc
00435A10  mov      eax, 1
00435A15  mov      edx, dword ptr [ebp - 0x28]
00435A18  mov      dword ptr fs:[0], edx
00435A1F  jmp      0x435a64
00435A21  dec      dword ptr [ebx + 0xd]
00435A24  mov      eax, esi
00435A26  jmp      0x435a3e
00435A28  lea      ecx, [eax + 1]
00435A2B  shl      ecx, 2
00435A2E  add      ecx, dword ptr [ebx + 5]
00435A31  mov      edx, eax
00435A33  shl      edx, 2
00435A36  add      edx, dword ptr [ebx + 5]
00435A39  mov      ecx, dword ptr [ecx]
00435A3B  mov      dword ptr [edx], ecx
00435A3D  inc      eax
00435A3E  cmp      eax, dword ptr [ebx + 0xd]
00435A41  jb       0x435a28
00435A43  mov      eax, dword ptr [ebx + 0xd]
00435A46  inc      eax
00435A47  push     eax
00435A48  push     dword ptr [ebx + 0xd]
00435A4B  push     ebx
00435A4C  mov      edx, dword ptr [ebx + 1]
00435A4F  call     dword ptr [edx + 0xc]
00435A52  add      esp, 0xc
00435A55  mov      eax, 1
00435A5A  mov      edx, dword ptr [ebp - 0x28]
00435A5D  mov      dword ptr fs:[0], edx
00435A64  pop      esi
00435A65  pop      ebx
00435A66  mov      esp, ebp
00435A68  pop      ebp
00435A69  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618

---

*Extracted with recursive CALL following and DATA context*
