# LoadFromINI Function Analysis

**Function Address**: 0x00411D4D
**Rank**: #1
**INI String Count**: 14
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 77

```assembly
00411D4D  push     ebp
00411D4E  mov      ebp, esp
00411D50  add      esp, -0x28
00411D53  push     ebx
00411D54  push     esi
00411D55  lea      esi, [ebp - 0x28]
00411D58  mov      eax, 0x4404d8
00411D5D  call     0x403618
00411D62  mov      dword ptr [esi + 0x1c], 0xf
00411D69  cmp      dword ptr [ebp + 8], 0
00411D6D  je       0x411e4d
00411D73  mov      word ptr [esi + 0x10], 8
00411D79  mov      edx, dword ptr [ebp + 8]
00411D7C  mov      dword ptr [edx], 0x44181c
00411D82  mov      ecx, dword ptr [ebp + 8]
00411D85  mov      dword ptr [ecx + 4], 0x441848
00411D8C  mov      eax, dword ptr [ebp + 8]
00411D8F  push     eax
00411D90  mov      edx, dword ptr [eax]
00411D92  call     dword ptr [edx + 0xc]
00411D95  pop      ecx
00411D96  sub      dword ptr [esi + 0x1c], 0xc
00411D9A  mov      ebx, dword ptr [ebp + 8]
00411D9D  add      ebx, 8
00411DA0  mov      dword ptr [ebx + 0x21], 0x4400a0
00411DA7  mov      dword ptr [ebx + 0x19], 0x4400c0
00411DAE  mov      dword ptr [ebx + 0x1d], 0x4400d0
00411DB5  push     ebx
00411DB6  mov      eax, dword ptr [ebx + 0x21]
00411DB9  call     dword ptr [eax + 0xc]
00411DBC  pop      ecx
00411DBD  sub      dword ptr [esi + 0x1c], 3
00411DC1  dec      dword ptr [esi + 0x1c]
00411DC4  dec      dword ptr [esi + 0x1c]
00411DC7  sub      dword ptr [esi + 0x1c], 8
00411DCB  add      dword ptr [esi + 0x1c], 8
00411DCF  sub      dword ptr [esi + 0x1c], 7
00411DD3  add      dword ptr [esi + 0x1c], 7
00411DD7  sub      dword ptr [esi + 0x1c], 6
00411DDB  add      dword ptr [esi + 0x1c], 6
00411DDF  sub      dword ptr [esi + 0x1c], 5
00411DE3  add      dword ptr [esi + 0x1c], 5
00411DE7  sub      dword ptr [esi + 0x1c], 4
00411DEB  add      dword ptr [esi + 0x1c], 4
00411DEF  sub      dword ptr [esi + 0x1c], 3
00411DF3  lea      eax, [ebx + 4]
00411DF6  add      dword ptr [esi + 0x1c], 3
00411DFA  sub      dword ptr [esi + 0x1c], 2
00411DFE  add      dword ptr [esi + 0x1c], 2
00411E02  dec      dword ptr [esi + 0x1c]
00411E05  mov      dword ptr [eax + 1], 0x4400e4
00411E0C  mov      edx, dword ptr [eax + 5]
00411E0F  mov      dword ptr [ebp - 4], edx
00411E12  mov      word ptr [esi + 0x10], 0x20
00411E18  push     0x40f5da
00411E1D  push     0x19
00411E1F  push     0
00411E21  push     0x14
00411E23  push     dword ptr [ebp - 4]
00411E26  call     0x4036b8
00411E2B  add      esp, 0x14
00411E2E  mov      word ptr [esi + 0x10], 0x14
00411E34  sub      dword ptr [esi + 0x1c], 3
00411E38  dec      dword ptr [esi + 0x1c]
00411E3B  dec      dword ptr [esi + 0x1c]
00411E3E  test     byte ptr [ebp + 0xc], 1
00411E42  je       0x411e4d
00411E44  push     dword ptr [ebp + 8]
00411E47  call     0x438f16
00411E4C  pop      ecx
00411E4D  mov      ecx, dword ptr [esi]
00411E4F  mov      dword ptr fs:[0], ecx
00411E56  pop      esi
00411E57  pop      ebx
00411E58  mov      esp, ebp
00411E5A  pop      ebp
00411E5B  ret      
```

## Strings Referenced

**Total unique strings**: 2

- `"!EA"` @ 0x00441848
- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0

## DATA Context

**Context around 0x00441848**:

- `">BA"` @ 0x004417F0
- `"FDA"` @ 0x004417F4
- `">BA"` @ 0x0044180C
- `"$#A"` @ 0x00441838
- `"!EA"` @ 0x00441848
- `"%<@"` @ 0x00441850
- `"%<@"` @ 0x00441894

**Context around 0x0044EAD0**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41

## Functions Called

- 0x00403618
- 0x004036B8
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
