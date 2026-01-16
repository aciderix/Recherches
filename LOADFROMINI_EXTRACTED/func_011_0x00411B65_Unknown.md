# LoadFromINI Function Analysis

**Function Address**: 0x00411B65
**Rank**: #11
**INI String Count**: 11
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 41

```assembly
00411B65  push     ebp
00411B66  mov      ebp, esp
00411B68  add      esp, -0x28
00411B6B  push     ebx
00411B6C  push     esi
00411B6D  mov      ebx, dword ptr [ebp + 8]
00411B70  mov      eax, 0x43f74a
00411B75  call     0x403618
00411B7A  test     ebx, ebx
00411B7C  je       0x411bd4
00411B7E  add      dword ptr [ebp - 0xc], 4
00411B82  sub      dword ptr [ebp - 0xc], 3
00411B86  lea      esi, [ebx + 4]
00411B89  add      dword ptr [ebp - 0xc], 3
00411B8D  sub      dword ptr [ebp - 0xc], 2
00411B91  add      dword ptr [ebp - 0xc], 2
00411B95  dec      dword ptr [ebp - 0xc]
00411B98  mov      dword ptr [esi + 1], 0x4401ac
00411B9F  mov      eax, dword ptr [esi + 5]
00411BA2  mov      dword ptr [ebp - 4], eax
00411BA5  mov      word ptr [ebp - 0x18], 0x14
00411BAB  push     0x40f471
00411BB0  push     0x19
00411BB2  push     0
00411BB4  push     0x10
00411BB6  push     dword ptr [ebp - 4]
00411BB9  call     0x4036b8
00411BBE  add      esp, 0x14
00411BC1  mov      word ptr [ebp - 0x18], 8
00411BC7  test     byte ptr [ebp + 0xc], 1
00411BCB  je       0x411bd4
00411BCD  push     ebx
00411BCE  call     0x438f16
00411BD3  pop      ecx
00411BD4  mov      edx, dword ptr [ebp - 0x28]
00411BD7  mov      dword ptr fs:[0], edx
00411BDE  pop      esi
00411BDF  pop      ebx
00411BE0  mov      esp, ebp
00411BE2  pop      ebp
00411BE3  ret      
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
