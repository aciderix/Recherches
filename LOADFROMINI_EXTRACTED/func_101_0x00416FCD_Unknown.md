# LoadFromINI Function Analysis

**Function Address**: 0x00416FCD
**Rank**: #101
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 43

```assembly
00416FCD  push     ebp
00416FCE  mov      ebp, esp
00416FD0  push     ebx
00416FD1  push     esi
00416FD2  mov      ebx, dword ptr [ebp + 8]
00416FD5  lea      eax, [ebx + 0x5e]
00416FD8  jmp      0x416fe4
00416FDA  cmp      dword ptr [eax + 0x19], 2
00416FDE  je       0x416fe4
00416FE0  xor      edx, edx
00416FE2  jmp      0x416fe9
00416FE4  mov      edx, 1
00416FE9  lea      esi, [eax + 4]
00416FEC  push     0
00416FEE  push     -1
00416FF0  push     edx
00416FF1  push     esi
00416FF2  call     0x406ba2
00416FF7  add      esp, 0x10
00416FFA  xor      eax, eax
00416FFC  mov      dword ptr [esi + 0xd], eax
00416FFF  jmp      0x41700b
00417001  cmp      dword ptr [ebx + 0x19], 2
00417005  je       0x41700b
00417007  xor      eax, eax
00417009  jmp      0x417010
0041700B  mov      eax, 1
00417010  lea      esi, [ebx + 4]
00417013  push     0
00417015  push     -1
00417017  push     eax
00417018  push     esi
00417019  call     0x4264f3
0041701E  add      esp, 0x10
00417021  xor      eax, eax
00417023  mov      dword ptr [esi + 0xd], eax
00417026  push     ebx
00417027  call     0x4169c5
0041702C  pop      ecx
0041702D  pop      esi
0041702E  pop      ebx
0041702F  pop      ebp
00417030  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00406BA2
- 0x004264F3
- 0x004169C5

---

*Extracted with recursive CALL following and DATA context*
