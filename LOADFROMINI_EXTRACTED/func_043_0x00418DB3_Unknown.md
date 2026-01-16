# LoadFromINI Function Analysis

**Function Address**: 0x00418DB3
**Rank**: #43
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 29

```assembly
00418DB3  push     ebp
00418DB4  mov      ebp, esp
00418DB6  add      esp, -0x24
00418DB9  push     ebx
00418DBA  push     esi
00418DBB  mov      ebx, dword ptr [ebp + 8]
00418DBE  mov      eax, 0x4428b0
00418DC3  call     0x403618
00418DC8  test     ebx, ebx
00418DCA  je       0x418df2
00418DCC  add      dword ptr [ebp - 8], 2
00418DD0  dec      dword ptr [ebp - 8]
00418DD3  mov      dword ptr [ebx + 1], 0x43b500
00418DDA  push     dword ptr [ebx + 5]
00418DDD  call     0x438f82
00418DE2  pop      ecx
00418DE3  test     byte ptr [ebp + 0xc], 1
00418DE7  je       0x418df2
00418DE9  mov      esi, ebx
00418DEB  push     esi
00418DEC  call     0x438f16
00418DF1  pop      ecx
00418DF2  mov      edx, dword ptr [ebp - 0x24]
00418DF5  mov      dword ptr fs:[0], edx
00418DFC  pop      esi
00418DFD  pop      ebx
00418DFE  mov      esp, ebp
00418E00  pop      ebp
00418E01  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
