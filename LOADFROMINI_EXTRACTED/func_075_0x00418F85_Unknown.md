# LoadFromINI Function Analysis

**Function Address**: 0x00418F85
**Rank**: #75
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 28

```assembly
00418F85  push     ebp
00418F86  mov      ebp, esp
00418F88  add      esp, -0x24
00418F8B  mov      eax, 0x442e94
00418F90  call     0x403618
00418F95  mov      word ptr [ebp - 0x14], 8
00418F9B  push     dword ptr [ebp + 8]
00418F9E  call     0x418f46
00418FA3  pop      ecx
00418FA4  mov      edx, dword ptr [ebp + 8]
00418FA7  mov      dword ptr [edx + 0x14], 0x4436a8
00418FAE  mov      ecx, dword ptr [ebp + 8]
00418FB1  xor      eax, eax
00418FB3  mov      dword ptr [ecx + 0x18], eax
00418FB6  mov      edx, dword ptr [ebp + 8]
00418FB9  mov      byte ptr [edx + 0x1c], 0
00418FBD  push     dword ptr [ebp + 0xc]
00418FC0  mov      ecx, dword ptr [ebp + 8]
00418FC3  push     ecx
00418FC4  mov      eax, dword ptr [ecx + 0x14]
00418FC7  call     dword ptr [eax + 8]
00418FCA  add      esp, 8
00418FCD  mov      edx, dword ptr [ebp - 0x24]
00418FD0  mov      dword ptr fs:[0], edx
00418FD7  mov      eax, dword ptr [ebp + 8]
00418FDA  mov      esp, ebp
00418FDC  pop      ebp
00418FDD  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00418F46

---

*Extracted with recursive CALL following and DATA context*
