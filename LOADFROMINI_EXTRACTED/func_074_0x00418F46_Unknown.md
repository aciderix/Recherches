# LoadFromINI Function Analysis

**Function Address**: 0x00418F46
**Rank**: #74
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 24

```assembly
00418F46  push     ebp
00418F47  mov      ebp, esp
00418F49  add      esp, -0x24
00418F4C  push     ebx
00418F4D  mov      ebx, dword ptr [ebp + 8]
00418F50  mov      eax, 0x442e7c
00418F55  call     0x403618
00418F5A  xor      edx, edx
00418F5C  mov      dword ptr [ebx], edx
00418F5E  xor      ecx, ecx
00418F60  mov      dword ptr [ebx + 4], ecx
00418F63  mov      eax, dword ptr [0x44ec08]
00418F68  mov      dword ptr [ebx + 8], eax
00418F6B  xor      edx, edx
00418F6D  mov      dword ptr [ebx + 0xc], edx
00418F70  xor      ecx, ecx
00418F72  mov      dword ptr [ebx + 0x10], ecx
00418F75  mov      eax, dword ptr [ebp - 0x24]
00418F78  mov      dword ptr fs:[0], eax
00418F7E  mov      eax, ebx
00418F80  pop      ebx
00418F81  mov      esp, ebp
00418F83  pop      ebp
00418F84  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618

---

*Extracted with recursive CALL following and DATA context*
