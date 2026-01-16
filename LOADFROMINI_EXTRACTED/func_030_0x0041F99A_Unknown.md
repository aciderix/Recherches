# LoadFromINI Function Analysis

**Function Address**: 0x0041F99A
**Rank**: #30
**INI String Count**: 7
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 94

```assembly
0041F99A  push     ebp
0041F99B  mov      ebp, esp
0041F99D  add      esp, -0x2c
0041F9A0  push     ebx
0041F9A1  push     esi
0041F9A2  push     edi
0041F9A3  mov      edi, 0x444a38
0041F9A8  mov      eax, 0x444e84
0041F9AD  call     0x403618
0041F9B2  push     0
0041F9B4  mov      word ptr [ebp - 0x1c], 0x14
0041F9BA  push     0x44645d
0041F9BF  lea      edx, [ebp - 4]
0041F9C2  push     edx
0041F9C3  call     0x438e6e
0041F9C8  add      esp, 8
0041F9CB  inc      dword ptr [ebp - 0x10]
0041F9CE  lea      ecx, [ebp - 4]
0041F9D1  push     ecx
0041F9D2  push     dword ptr [ebp + 0xc]
0041F9D5  call     0x438ed4
0041F9DA  add      esp, 0xc
0041F9DD  mov      esi, eax
0041F9DF  dec      dword ptr [ebp - 0x10]
0041F9E2  push     2
0041F9E4  lea      eax, [ebp - 4]
0041F9E7  push     eax
0041F9E8  call     0x438f64
0041F9ED  add      esp, 8
0041F9F0  mov      word ptr [ebp - 0x1c], 8
0041F9F6  cmp      esi, -1
0041F9F9  je       0x41fa94
0041F9FF  xor      ebx, ebx
0041FA01  jmp      0x41fa44
0041FA03  mov      eax, dword ptr [edi + ebx*4]
0041FA06  push     dword ptr [eax + 6]
0041FA09  push     esi
0041FA0A  push     dword ptr [ebp + 0xc]
0041FA0D  mov      edx, ebx
0041FA0F  shl      edx, 2
0041FA12  add      edx, edi
0041FA14  push     edx
0041FA15  call     0x438dfc
0041FA1A  add      esp, 0x10
0041FA1D  test     eax, eax
0041FA1F  jne      0x41fa41
0041FA21  push     esi
0041FA22  lea      ecx, [ebx + 1]
0041FA25  shl      ecx, 2
0041FA28  add      ecx, edi
0041FA2A  push     ecx
0041FA2B  shl      ebx, 2
0041FA2E  add      ebx, edi
0041FA30  push     ebx
0041FA31  push     dword ptr [ebp + 0xc]
0041FA34  push     dword ptr [ebp + 8]
0041FA37  call     0x41f93b
0041FA3C  add      esp, 0x14
0041FA3F  jmp      0x41fa4d
0041FA41  add      ebx, 2
0041FA44  mov      eax, dword ptr [edi + ebx*4]
0041FA47  cmp      dword ptr [eax + 6], 0
0041FA4B  jne      0x41fa03
0041FA4D  inc      esi
0041FA4E  push     esi
0041FA4F  mov      word ptr [ebp - 0x1c], 0x20
0041FA55  push     0x44645f
0041FA5A  lea      eax, [ebp - 8]
0041FA5D  push     eax
0041FA5E  call     0x438e6e
0041FA63  add      esp, 8
0041FA66  inc      dword ptr [ebp - 0x10]
0041FA69  lea      edx, [ebp - 8]
0041FA6C  push     edx
0041FA6D  push     dword ptr [ebp + 0xc]
0041FA70  call     0x438ed4
0041FA75  add      esp, 0xc
0041FA78  mov      esi, eax
0041FA7A  dec      dword ptr [ebp - 0x10]
0041FA7D  push     2
0041FA7F  lea      ecx, [ebp - 8]
0041FA82  push     ecx
0041FA83  call     0x438f64
0041FA88  add      esp, 8
0041FA8B  cmp      esi, -1
0041FA8E  jne      0x41f9ff
0041FA94  mov      eax, dword ptr [ebp - 0x2c]
0041FA97  mov      dword ptr fs:[0], eax
0041FA9D  pop      edi
0041FA9E  pop      esi
0041FA9F  pop      ebx
0041FAA0  mov      esp, ebp
0041FAA2  pop      ebp
0041FAA3  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438E6E
- 0x00438ED4
- 0x00438F64
- 0x00438DFC
- 0x0041F93B
- 0x00438E6E
- 0x00438ED4
- 0x00438F64

---

*Extracted with recursive CALL following and DATA context*
