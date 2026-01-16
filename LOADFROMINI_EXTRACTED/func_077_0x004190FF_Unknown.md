# LoadFromINI Function Analysis

**Function Address**: 0x004190FF
**Rank**: #77
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 18

```assembly
004190FF  push     ebp
00419100  mov      ebp, esp
00419102  push     ebx
00419103  mov      ebx, dword ptr [ebp + 8]
00419106  cmp      dword ptr [ebx + 0x18], 0
0041910A  je       0x41911d
0041910C  push     dword ptr [ebx + 0x18]
0041910F  call     0x439840
00419114  test     eax, eax
00419116  jne      0x41911d
00419118  xor      eax, eax
0041911A  mov      dword ptr [ebx + 0x18], eax
0041911D  cmp      dword ptr [ebx + 0x18], 0
00419121  sete     al
00419124  and      eax, 1
00419127  pop      ebx
00419128  pop      ebp
00419129  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00439840

---

*Extracted with recursive CALL following and DATA context*
