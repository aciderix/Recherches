# LoadFromINI Function Analysis

**Function Address**: 0x004264AF
**Rank**: #156
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 22

```assembly
004264AF  push     ebp
004264B0  mov      ebp, esp
004264B2  add      esp, -0x28
004264B5  mov      eax, 0x447590
004264BA  call     0x403618
004264BF  mov      edx, dword ptr [ebp + 8]
004264C2  mov      dword ptr [ebp - 4], edx
004264C5  cmp      dword ptr [ebp - 4], 0
004264C9  je       0x4264e5
004264CB  mov      word ptr [ebp - 0x18], 0x14
004264D1  push     3
004264D3  mov      ecx, dword ptr [ebp - 4]
004264D6  push     ecx
004264D7  mov      eax, dword ptr [ecx]
004264D9  call     dword ptr [eax + 8]
004264DC  add      esp, 8
004264DF  mov      word ptr [ebp - 0x18], 8
004264E5  mov      edx, dword ptr [ebp - 0x28]
004264E8  mov      dword ptr fs:[0], edx
004264EF  mov      esp, ebp
004264F1  pop      ebp
004264F2  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618

---

*Extracted with recursive CALL following and DATA context*
