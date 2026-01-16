# LoadFromINI Function Analysis

**Function Address**: 0x0041E044
**Rank**: #151
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 92

```assembly
0041E044  push     ebp
0041E045  mov      ebp, esp
0041E047  push     ecx
0041E048  push     ebx
0041E049  push     esi
0041E04A  push     edi
0041E04B  mov      esi, dword ptr [ebp + 0xc]
0041E04E  mov      edi, dword ptr [ebp + 8]
0041E051  mov      eax, dword ptr [edi + 0x34]
0041E054  mov      edx, dword ptr [eax + 2]
0041E057  cmp      byte ptr [edx], 0
0041E05A  je       0x41e067
0041E05C  push     edi
0041E05D  mov      ecx, dword ptr [edi]
0041E05F  call     dword ptr [ecx + 4]
0041E062  pop      ecx
0041E063  test     al, al
0041E065  jne      0x41e06e
0041E067  xor      eax, eax
0041E069  jmp      0x41e113
0041E06E  push     esi
0041E06F  mov      edx, dword ptr [esi + 5]
0041E072  call     dword ptr [edx + 0x58]
0041E075  pop      ecx
0041E076  cmp      eax, dword ptr [esi]
0041E078  je       0x41e083
0041E07A  push     1
0041E07C  push     dword ptr [esi]
0041E07E  call     0x4397d4
0041E083  push     1
0041E085  push     esi
0041E086  mov      ecx, dword ptr [esi + 5]
0041E089  call     dword ptr [ecx + 0x58]
0041E08C  pop      ecx
0041E08D  push     eax
0041E08E  call     0x4397d4
0041E093  cmp      dword ptr [edi + 0x2c], 0
0041E097  je       0x41e0a6
0041E099  push     dword ptr [edi + 0x2c]
0041E09C  push     esi
0041E09D  mov      eax, dword ptr [esi + 5]
0041E0A0  call     dword ptr [eax + 0x14]
0041E0A3  add      esp, 8
0041E0A6  lea      edx, [edi + 0x30]
0041E0A9  push     edx
0041E0AA  push     esi
0041E0AB  lea      ecx, [ebp - 4]
0041E0AE  push     ecx
0041E0AF  mov      eax, dword ptr [esi + 5]
0041E0B2  call     dword ptr [eax + 0x24]
0041E0B5  add      esp, 0xc
0041E0B8  mov      dx, word ptr [edi + 0x38]
0041E0BC  or       dx, 0x400
0041E0C1  push     edx
0041E0C2  lea      ecx, [edi + 4]
0041E0C5  push     ecx
0041E0C6  mov      eax, dword ptr [edi + 0x34]
0041E0C9  push     dword ptr [eax + 6]
0041E0CC  mov      edx, dword ptr [edi + 0x34]
0041E0CF  push     dword ptr [edx + 2]
0041E0D2  push     esi
0041E0D3  mov      ecx, dword ptr [esi + 5]
0041E0D6  call     dword ptr [ecx + 0x50]
0041E0D9  add      esp, 0x14
0041E0DC  mov      ax, word ptr [edi + 0x38]
0041E0E0  push     eax
0041E0E1  lea      edx, [edi + 4]
0041E0E4  push     edx
0041E0E5  mov      ecx, dword ptr [edi + 0x34]
0041E0E8  push     dword ptr [ecx + 6]
0041E0EB  mov      eax, dword ptr [edi + 0x34]
0041E0EE  push     dword ptr [eax + 2]
0041E0F1  push     esi
0041E0F2  mov      edx, dword ptr [esi + 5]
0041E0F5  call     dword ptr [edx + 0x50]
0041E0F8  add      esp, 0x14
0041E0FB  test     eax, eax
0041E0FD  setne    bl
0041E100  and      ebx, 1
0041E103  cmp      dword ptr [edi + 0x2c], 0
0041E107  je       0x41e111
0041E109  push     esi
0041E10A  mov      eax, dword ptr [esi + 5]
0041E10D  call     dword ptr [eax + 0x1c]
0041E110  pop      ecx
0041E111  mov      eax, ebx
0041E113  pop      edi
0041E114  pop      esi
0041E115  pop      ebx
0041E116  pop      ecx
0041E117  pop      ebp
0041E118  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x004397D4
- 0x004397D4

---

*Extracted with recursive CALL following and DATA context*
