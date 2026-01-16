# LoadFromINI Function Analysis

**Function Address**: 0x0041318B
**Rank**: #65
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 95

```assembly
0041318B  push     ebp
0041318C  mov      ebp, esp
0041318E  add      esp, -0x28
00413191  push     ebx
00413192  push     esi
00413193  mov      eax, 0x440960
00413198  call     0x403618
0041319D  mov      word ptr [ebp - 0x18], 8
004131A3  mov      edx, dword ptr [ebp + 8]
004131A6  mov      dword ptr [edx], 0x4402d4
004131AC  inc      dword ptr [ebp - 0xc]
004131AF  mov      eax, dword ptr [ebp + 8]
004131B2  add      eax, 4
004131B5  mov      dword ptr [eax], 0x4402c0
004131BB  inc      dword ptr [ebp - 0xc]
004131BE  mov      edx, dword ptr [ebp + 8]
004131C1  mov      dword ptr [edx], 0x4402e8
004131C7  mov      ecx, dword ptr [ebp + 8]
004131CA  mov      dword ptr [ecx + 4], 0x4402f8
004131D1  add      dword ptr [ebp - 0xc], 3
004131D5  mov      eax, dword ptr [ebp + 8]
004131D8  mov      dword ptr [eax], 0x44181c
004131DE  mov      edx, dword ptr [ebp + 8]
004131E1  mov      dword ptr [edx + 4], 0x441848
004131E8  mov      ebx, dword ptr [ebp + 8]
004131EB  add      ebx, 8
004131EE  xor      eax, eax
004131F0  mov      dword ptr [ebx], eax
004131F2  lea      esi, [ebx + 4]
004131F5  mov      dword ptr [esi + 1], 0x4400e4
004131FC  push     0x18
004131FE  call     0x438e50
00413203  pop      ecx
00413204  mov      dword ptr [ebp - 4], eax
00413207  cmp      dword ptr [ebp - 4], 0
0041320B  je       0x41323b
0041320D  mov      word ptr [ebp - 0x18], 0x20
00413213  push     0x40f5da
00413218  push     1
0041321A  push     0x40f53c
0041321F  push     0x211
00413224  push     1
00413226  push     0x14
00413228  push     dword ptr [ebp - 4]
0041322B  call     0x4037e0
00413230  add      esp, 0x1c
00413233  mov      word ptr [ebp - 0x18], 0x14
00413239  jmp      0x41323e
0041323B  mov      eax, dword ptr [ebp - 4]
0041323E  mov      dword ptr [esi + 5], eax
00413241  mov      dword ptr [esi + 9], 1
00413248  inc      dword ptr [ebp - 0xc]
0041324B  mov      dword ptr [esi + 1], 0x440100
00413252  add      dword ptr [ebp - 0xc], 2
00413256  mov      dword ptr [esi + 1], 0x44011c
0041325D  xor      edx, edx
0041325F  mov      dword ptr [esi + 0xd], edx
00413262  mov      dword ptr [esi + 0x11], 1
00413269  add      dword ptr [ebp - 0xc], 3
0041326D  add      dword ptr [ebp - 0xc], 4
00413271  add      dword ptr [ebp - 0xc], 5
00413275  add      dword ptr [ebp - 0xc], 6
00413279  add      dword ptr [ebp - 0xc], 7
0041327D  add      dword ptr [ebp - 0xc], 8
00413281  lea      eax, [ebx + 0x19]
00413284  mov      dword ptr [eax], 0x4402d4
0041328A  inc      dword ptr [ebp - 0xc]
0041328D  lea      edx, [eax + 4]
00413290  mov      dword ptr [edx], 0x4402c0
00413296  inc      dword ptr [ebp - 0xc]
00413299  mov      dword ptr [eax], 0x4402e8
0041329F  mov      dword ptr [eax + 4], 0x4402f8
004132A6  add      dword ptr [ebp - 0xc], 3
004132AA  mov      dword ptr [ebx + 0x21], 0x4400a0
004132B1  mov      dword ptr [ebx + 0x19], 0x4400c0
004132B8  mov      dword ptr [ebx + 0x1d], 0x4400d0
004132BF  add      dword ptr [ebp - 0xc], 0xc
004132C3  push     dword ptr [ebp + 8]
004132C6  call     0x411e5c
004132CB  pop      ecx
004132CC  push     dword ptr [ebp + 0x10]
004132CF  push     dword ptr [ebp + 0xc]
004132D2  mov      ecx, dword ptr [ebp + 8]
004132D5  push     ecx
004132D6  mov      eax, dword ptr [ecx]
004132D8  call     dword ptr [eax + 0x20]
004132DB  add      esp, 0xc
004132DE  mov      edx, dword ptr [ebp - 0x28]
004132E1  mov      dword ptr fs:[0], edx
004132E8  mov      eax, dword ptr [ebp + 8]
004132EB  pop      esi
004132EC  pop      ebx
004132ED  mov      esp, ebp
004132EF  pop      ebp
004132F0  ret      
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
