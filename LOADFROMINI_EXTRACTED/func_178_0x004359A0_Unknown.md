# LoadFromINI Function Analysis

**Function Address**: 0x004359A0
**Rank**: #178
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 73

```assembly
004359A0  push     ebp
004359A1  mov      ebp, esp
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
