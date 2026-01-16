# LoadFromINI Function Analysis

**Function Address**: 0x00411E7A
**Rank**: #3
**INI String Count**: 14
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 18

```assembly
00411E7A  push     ebp
00411E7B  mov      ebp, esp
00411E7D  push     ebx
00411E7E  mov      ebx, dword ptr [ebp + 8]
00411E81  lea      eax, [ebx + 8]
00411E84  push     eax
00411E85  mov      edx, dword ptr [ebx + 0x29]
00411E88  call     dword ptr [edx + 0xc]
00411E8B  pop      ecx
00411E8C  push     dword ptr [ebx + 0x39]
00411E8F  call     0x438f82
00411E94  pop      ecx
00411E95  push     ebx
00411E96  call     0x411e5c
00411E9B  pop      ecx
00411E9C  pop      ebx
00411E9D  pop      ebp
00411E9E  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00438F82
- 0x00411E5C

---

*Extracted with recursive CALL following and DATA context*
