# LoadFromINI Function Analysis

**Function Address**: 0x004358A4
**Rank**: #176
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 17

```assembly
004358A4  push     ebp
004358A5  mov      ebp, esp
004358A7  add      esp, -0x24
004358AA  push     ebx
004358AB  mov      ebx, dword ptr [ebp + 8]
004358AE  mov      eax, 0x44c248
004358B3  call     0x403618
004358B8  xor      edx, edx
004358BA  mov      dword ptr [ebx], edx
004358BC  mov      eax, ebx
004358BE  jmp      0x4358ca
004358C0  mov      edx, dword ptr [ebp - 0x24]
004358C3  mov      dword ptr fs:[0], edx
004358CA  pop      ebx
004358CB  mov      esp, ebp
004358CD  pop      ebp
004358CE  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618

---

*Extracted with recursive CALL following and DATA context*
