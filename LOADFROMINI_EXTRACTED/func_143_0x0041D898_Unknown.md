# LoadFromINI Function Analysis

**Function Address**: 0x0041D898
**Rank**: #143
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 31

```assembly
0041D898  push     ebp
0041D899  mov      ebp, esp
0041D89B  add      esp, -0x24
0041D89E  mov      eax, 0x444514
0041D8A3  call     0x403618
0041D8A8  mov      dword ptr [ebp - 8], 2
0041D8AF  cmp      dword ptr [ebp + 8], 0
0041D8B3  je       0x41d8f5
0041D8B5  mov      word ptr [ebp - 0x14], 8
0041D8BB  mov      edx, dword ptr [ebp + 8]
0041D8BE  mov      dword ptr [edx + 5], 0x4449ec
0041D8C5  push     3
0041D8C7  mov      ecx, dword ptr [ebp + 8]
0041D8CA  push     dword ptr [ecx + 9]
0041D8CD  call     0x439678
0041D8D2  add      esp, 8
0041D8D5  sub      dword ptr [ebp - 8], 2
0041D8D9  push     0
0041D8DB  push     dword ptr [ebp + 8]
0041D8DE  call     0x4396e4
0041D8E3  add      esp, 8
0041D8E6  test     byte ptr [ebp + 0xc], 1
0041D8EA  je       0x41d8f5
0041D8EC  push     dword ptr [ebp + 8]
0041D8EF  call     0x438f16
0041D8F4  pop      ecx
0041D8F5  mov      eax, dword ptr [ebp - 0x24]
0041D8F8  mov      dword ptr fs:[0], eax
0041D8FE  mov      esp, ebp
0041D900  pop      ebp
0041D901  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00439678
- 0x004396E4
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
