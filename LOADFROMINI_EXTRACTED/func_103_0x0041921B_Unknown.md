# LoadFromINI Function Analysis

**Function Address**: 0x0041921B
**Rank**: #103
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 26

```assembly
0041921B  push     ebp
0041921C  mov      ebp, esp
0041921E  add      esp, -0x20
00419221  push     ebx
00419222  push     esi
00419223  push     edi
00419224  mov      ebx, dword ptr [ebp + 8]
00419227  lea      eax, [ebp - 0x20]
0041922A  push     eax
0041922B  push     dword ptr [ebx + 8]
0041922E  call     0x439516
00419233  add      esp, 8
00419236  lea      esi, [ebp - 0x20]
00419239  lea      edi, [ebp - 0x10]
0041923C  mov      ecx, 4
00419241  rep movsd dword ptr es:[edi], dword ptr [esi]
00419243  mov      eax, dword ptr [ebp - 8]
00419246  mov      dword ptr [ebx + 0x10], eax
00419249  mov      edx, dword ptr [ebp - 4]
0041924C  mov      dword ptr [ebx + 0x14], edx
0041924F  pop      edi
00419250  pop      esi
00419251  pop      ebx
00419252  mov      esp, ebp
00419254  pop      ebp
00419255  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00439516

---

*Extracted with recursive CALL following and DATA context*
