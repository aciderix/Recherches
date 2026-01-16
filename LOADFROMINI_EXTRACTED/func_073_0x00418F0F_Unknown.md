# LoadFromINI Function Analysis

**Function Address**: 0x00418F0F
**Rank**: #73
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 22

```assembly
00418F0F  push     ebp
00418F10  mov      ebp, esp
00418F12  push     ebx
00418F13  mov      ebx, dword ptr [ebp + 8]
00418F16  test     ebx, ebx
00418F18  je       0x418f43
00418F1A  mov      dword ptr [ebx], 0x4436c8
00418F20  cmp      dword ptr [ebx + 4], 0
00418F24  setne    al
00418F27  and      eax, 1
00418F2A  test     al, al
00418F2C  je       0x418f36
00418F2E  push     dword ptr [ebx + 4]
00418F31  call     0x43984c
00418F36  test     byte ptr [ebp + 0xc], 1
00418F3A  je       0x418f43
00418F3C  push     ebx
00418F3D  call     0x438f16
00418F42  pop      ecx
00418F43  pop      ebx
00418F44  pop      ebp
00418F45  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x0043984C
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
