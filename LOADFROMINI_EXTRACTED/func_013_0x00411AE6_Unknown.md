# LoadFromINI Function Analysis

**Function Address**: 0x00411AE6
**Rank**: #13
**INI String Count**: 10
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 41

```assembly
00411AE6  push     ebp
00411AE7  mov      ebp, esp
00411AE9  add      esp, -0x28
00411AEC  push     ebx
00411AED  push     esi
00411AEE  mov      ebx, dword ptr [ebp + 8]
00411AF1  mov      eax, 0x43f71a
00411AF6  call     0x403618
00411AFB  test     ebx, ebx
00411AFD  je       0x411b55
00411AFF  add      dword ptr [ebp - 0xc], 4
00411B03  sub      dword ptr [ebp - 0xc], 3
00411B07  lea      esi, [ebx + 4]
00411B0A  add      dword ptr [ebp - 0xc], 3
00411B0E  sub      dword ptr [ebp - 0xc], 2
00411B12  add      dword ptr [ebp - 0xc], 2
00411B16  dec      dword ptr [ebp - 0xc]
00411B19  mov      dword ptr [esi + 1], 0x4400e4
00411B20  mov      eax, dword ptr [esi + 5]
00411B23  mov      dword ptr [ebp - 4], eax
00411B26  mov      word ptr [ebp - 0x18], 0x14
00411B2C  push     0x40f5da
00411B31  push     0x19
00411B33  push     0
00411B35  push     0x14
00411B37  push     dword ptr [ebp - 4]
00411B3A  call     0x4036b8
00411B3F  add      esp, 0x14
00411B42  mov      word ptr [ebp - 0x18], 8
00411B48  test     byte ptr [ebp + 0xc], 1
00411B4C  je       0x411b55
00411B4E  push     ebx
00411B4F  call     0x438f16
00411B54  pop      ecx
00411B55  mov      edx, dword ptr [ebp - 0x28]
00411B58  mov      dword ptr fs:[0], edx
00411B5F  pop      esi
00411B60  pop      ebx
00411B61  mov      esp, ebp
00411B63  pop      ebp
00411B64  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0

## DATA Context

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
