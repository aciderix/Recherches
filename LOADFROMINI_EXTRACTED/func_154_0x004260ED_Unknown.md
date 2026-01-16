# LoadFromINI Function Analysis

**Function Address**: 0x004260ED
**Rank**: #154
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 51

```assembly
004260ED  push     ebp
004260EE  mov      ebp, esp
004260F0  add      esp, -0x28
004260F3  push     ebx
004260F4  mov      ebx, dword ptr [ebp + 8]
004260F7  mov      eax, 0x447308
004260FC  call     0x403618
00426101  mov      word ptr [ebp - 0x18], 8
00426107  push     dword ptr [ebp + 0xc]
0042610A  lea      edx, [ebp - 4]
0042610D  push     edx
0042610E  call     0x438e6e
00426113  add      esp, 8
00426116  inc      dword ptr [ebp - 0xc]
00426119  push     -1
0042611B  push     0
0042611D  lea      ecx, [ebp - 4]
00426120  push     ecx
00426121  lea      eax, [ebx + 0x24]
00426124  push     eax
00426125  call     0x438f04
0042612A  add      esp, 0x10
0042612D  dec      dword ptr [ebp - 0xc]
00426130  push     2
00426132  lea      edx, [ebp - 4]
00426135  push     edx
00426136  call     0x438f64
0042613B  add      esp, 8
0042613E  mov      ecx, dword ptr [ebx + 0x24]
00426141  cmp      dword ptr [ecx + 6], 0
00426145  je       0x42616b
00426147  mov      eax, dword ptr [ebx + 0x24]
0042614A  push     dword ptr [eax + 2]
0042614D  push     ebx
0042614E  call     0x425ab4
00426153  add      esp, 8
00426156  mov      byte ptr [ebx + 0xdf], 0
0042615D  mov      al, 1
0042615F  mov      edx, dword ptr [ebp - 0x28]
00426162  mov      dword ptr fs:[0], edx
00426169  jmp      0x42617f
0042616B  push     0x72
0042616D  call     0x404ed9
00426172  pop      ecx
00426173  xor      eax, eax
00426175  mov      edx, dword ptr [ebp - 0x28]
00426178  mov      dword ptr fs:[0], edx
0042617F  pop      ebx
00426180  mov      esp, ebp
00426182  pop      ebp
00426183  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438E6E
- 0x00438F04
- 0x00438F64
- 0x00425AB4
- 0x00404ED9

---

*Extracted with recursive CALL following and DATA context*
