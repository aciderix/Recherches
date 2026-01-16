# LoadFromINI Function Analysis

**Function Address**: 0x004190C1
**Rank**: #132
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 24

```assembly
004190C1  push     ebp
004190C2  mov      ebp, esp
004190C4  push     ebx
004190C5  mov      ebx, dword ptr [ebp + 8]
004190C8  cmp      dword ptr [ebx + 0x18], 0
004190CC  jne      0x4190f2
004190CE  push     dword ptr [ebx + 0x10]
004190D1  push     dword ptr [ebx + 0xc]
004190D4  push     dword ptr [ebx + 4]
004190D7  cmp      dword ptr [ebx + 8], 0
004190DB  jl       0x4190e2
004190DD  mov      eax, dword ptr [ebx + 8]
004190E0  jmp      0x4190e7
004190E2  mov      eax, dword ptr [0x44ec08]
004190E7  push     eax
004190E8  push     dword ptr [ebx]
004190EA  call     0x43983a
004190EF  mov      dword ptr [ebx + 0x18], eax
004190F2  cmp      dword ptr [ebx + 0x18], 0
004190F6  setne    al
004190F9  and      eax, 1
004190FC  pop      ebx
004190FD  pop      ebp
004190FE  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x0043983A

---

*Extracted with recursive CALL following and DATA context*
