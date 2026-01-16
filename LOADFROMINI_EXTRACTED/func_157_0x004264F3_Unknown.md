# LoadFromINI Function Analysis

**Function Address**: 0x004264F3
**Rank**: #157
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 37

```assembly
004264F3  push     ebp
004264F4  mov      ebp, esp
004264F6  push     ecx
004264F7  push     ebx
004264F8  push     esi
004264F9  mov      esi, dword ptr [ebp + 0x14]
004264FC  mov      ebx, dword ptr [ebp + 8]
004264FF  mov      eax, dword ptr [ebx + 9]
00426502  mov      dword ptr [ebp - 4], eax
00426505  mov      edx, dword ptr [ebp + 0x10]
00426508  cmp      edx, dword ptr [ebp - 4]
0042650B  jae      0x426512
0042650D  lea      ecx, [ebp + 0x10]
00426510  jmp      0x426515
00426512  lea      ecx, [ebp - 4]
00426515  mov      eax, dword ptr [ecx]
00426517  mov      dword ptr [ebp + 0x10], eax
0042651A  cmp      dword ptr [ebp + 0xc], 0
0042651E  je       0x426534
00426520  push     dword ptr [ebp + 0x10]
00426523  push     esi
00426524  push     0
00426526  push     0x4264af
0042652B  push     ebx
0042652C  call     0x426547
00426531  add      esp, 0x14
00426534  push     dword ptr [ebp + 0x10]
00426537  push     esi
00426538  push     ebx
00426539  mov      edx, dword ptr [ebx + 1]
0042653C  call     dword ptr [edx + 0xc]
0042653F  add      esp, 0xc
00426542  pop      esi
00426543  pop      ebx
00426544  pop      ecx
00426545  pop      ebp
00426546  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00426547

---

*Extracted with recursive CALL following and DATA context*
