# LoadFromINI Function Analysis

**Function Address**: 0x00411BE4
**Rank**: #12
**INI String Count**: 11
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 96

```assembly
00411BE4  push     ebp
00411BE5  mov      ebp, esp
00411BE7  add      esp, -0x28
00411BEA  push     ebx
00411BEB  push     esi
00411BEC  mov      eax, 0x44048c
00411BF1  call     0x403618
00411BF6  mov      word ptr [ebp - 0x18], 8
00411BFC  mov      edx, dword ptr [ebp + 8]
00411BFF  mov      dword ptr [edx], 0x4402d4
00411C05  inc      dword ptr [ebp - 0xc]
00411C08  mov      eax, dword ptr [ebp + 8]
00411C0B  add      eax, 4
00411C0E  mov      dword ptr [eax], 0x4402c0
00411C14  inc      dword ptr [ebp - 0xc]
00411C17  mov      edx, dword ptr [ebp + 8]
00411C1A  mov      dword ptr [edx], 0x4402e8
00411C20  mov      ecx, dword ptr [ebp + 8]
00411C23  mov      dword ptr [ecx + 4], 0x4402f8
00411C2A  add      dword ptr [ebp - 0xc], 3
00411C2E  mov      eax, dword ptr [ebp + 8]
00411C31  mov      dword ptr [eax], 0x44181c
00411C37  mov      edx, dword ptr [ebp + 8]
00411C3A  mov      dword ptr [edx + 4], 0x441848
00411C41  mov      ebx, dword ptr [ebp + 8]
00411C44  add      ebx, 8
00411C47  xor      eax, eax
00411C49  mov      dword ptr [ebx], eax
00411C4B  lea      esi, [ebx + 4]
00411C4E  mov      dword ptr [esi + 1], 0x4400e4
00411C55  push     0x18
00411C57  call     0x438e50
00411C5C  pop      ecx
00411C5D  mov      dword ptr [ebp - 4], eax
00411C60  cmp      dword ptr [ebp - 4], 0
00411C64  je       0x411c94
00411C66  mov      word ptr [ebp - 0x18], 0x20
00411C6C  push     0x40f5da
00411C71  push     1
00411C73  push     0x40f53c
00411C78  push     0x211
00411C7D  push     1
00411C7F  push     0x14
00411C81  push     dword ptr [ebp - 4]
00411C84  call     0x4037e0
00411C89  add      esp, 0x1c
00411C8C  mov      word ptr [ebp - 0x18], 0x14
00411C92  jmp      0x411c97
00411C94  mov      eax, dword ptr [ebp - 4]
00411C97  mov      dword ptr [esi + 5], eax
00411C9A  mov      dword ptr [esi + 9], 1
00411CA1  inc      dword ptr [ebp - 0xc]
00411CA4  mov      dword ptr [esi + 1], 0x440100
00411CAB  add      dword ptr [ebp - 0xc], 2
00411CAF  mov      dword ptr [esi + 1], 0x44011c
00411CB6  xor      edx, edx
00411CB8  mov      dword ptr [esi + 0xd], edx
00411CBB  mov      dword ptr [esi + 0x11], 1
00411CC2  add      dword ptr [ebp - 0xc], 3
00411CC6  add      dword ptr [ebp - 0xc], 4
00411CCA  add      dword ptr [ebp - 0xc], 5
00411CCE  add      dword ptr [ebp - 0xc], 6
00411CD2  add      dword ptr [ebp - 0xc], 7
00411CD6  add      dword ptr [ebp - 0xc], 8
00411CDA  lea      eax, [ebx + 0x19]
00411CDD  mov      dword ptr [eax], 0x4402d4
00411CE3  inc      dword ptr [ebp - 0xc]
00411CE6  lea      edx, [eax + 4]
00411CE9  mov      dword ptr [edx], 0x4402c0
00411CEF  inc      dword ptr [ebp - 0xc]
00411CF2  mov      dword ptr [eax], 0x4402e8
00411CF8  mov      dword ptr [eax + 4], 0x4402f8
00411CFF  add      dword ptr [ebp - 0xc], 3
00411D03  mov      dword ptr [ebx + 0x21], 0x4400a0
00411D0A  mov      dword ptr [ebx + 0x19], 0x4400c0
00411D11  mov      dword ptr [ebx + 0x1d], 0x4400d0
00411D18  add      dword ptr [ebp - 0xc], 0xc
00411D1C  push     dword ptr [ebp + 8]
00411D1F  call     0x411e5c
00411D24  pop      ecx
00411D25  push     dword ptr [ebp + 0x14]
00411D28  push     dword ptr [ebp + 0x10]
00411D2B  push     dword ptr [ebp + 0xc]
00411D2E  mov      ecx, dword ptr [ebp + 8]
00411D31  push     ecx
00411D32  mov      eax, dword ptr [ecx]
00411D34  call     dword ptr [eax + 0x1c]
00411D37  add      esp, 0x10
00411D3A  mov      edx, dword ptr [ebp - 0x28]
00411D3D  mov      dword ptr fs:[0], edx
00411D44  mov      eax, dword ptr [ebp + 8]
00411D47  pop      esi
00411D48  pop      ebx
00411D49  mov      esp, ebp
00411D4B  pop      ebp
00411D4C  ret      
```

## Strings Referenced

**Total unique strings**: 4

- `"!EA"` @ 0x00441848
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## DATA Context

**Context around 0x00441848**:

- `">BA"` @ 0x004417F0
- `"FDA"` @ 0x004417F4
- `">BA"` @ 0x0044180C
- `"$#A"` @ 0x00441838
- `"!EA"` @ 0x00441848
- `"%<@"` @ 0x00441850
- `"%<@"` @ 0x00441894

**Context around 0x0044EB41**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD

**Context around 0x0044EB64**:

- `"tor_delete_"` @ 0x0044EAE4
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD
- `" N?A"` @ 0x0044EBCF
- `" w1B"` @ 0x0044EBDB

**Context around 0x0044EB24**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## Functions Called

- 0x00403618
- 0x00438E50
- 0x004037E0
- 0x00411E5C

---

*Extracted with recursive CALL following and DATA context*
