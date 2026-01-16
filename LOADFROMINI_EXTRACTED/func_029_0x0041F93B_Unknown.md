# LoadFromINI Function Analysis

**Function Address**: 0x0041F93B
**Rank**: #29
**INI String Count**: 7
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 46

```assembly
0041F93B  push     ebp
0041F93C  mov      ebp, esp
0041F93E  push     ecx
0041F93F  push     ebx
0041F940  push     esi
0041F941  push     edi
0041F942  mov      ebx, dword ptr [ebp + 0x18]
0041F945  mov      edi, dword ptr [ebp + 0x10]
0041F948  mov      esi, dword ptr [ebp + 0xc]
0041F94B  push     ebx
0041F94C  push     edi
0041F94D  push     esi
0041F94E  call     0x438ed4
0041F953  add      esp, 0xc
0041F956  mov      ebx, eax
0041F958  cmp      ebx, -1
0041F95B  je       0x41f994
0041F95D  mov      eax, dword ptr [ebp + 0x14]
0041F960  mov      edx, dword ptr [edi]
0041F962  mov      edx, dword ptr [edx + 6]
0041F965  mov      dword ptr [ebp - 4], ebx
0041F968  push     -1
0041F96A  push     0
0041F96C  push     eax
0041F96D  push     edx
0041F96E  push     dword ptr [ebp - 4]
0041F971  push     esi
0041F972  call     0x438ea4
0041F977  add      esp, 0x18
0041F97A  mov      eax, dword ptr [ebp + 0x14]
0041F97D  mov      ecx, dword ptr [eax]
0041F97F  add      ebx, dword ptr [ecx + 6]
0041F982  push     ebx
0041F983  push     edi
0041F984  push     esi
0041F985  call     0x438ed4
0041F98A  add      esp, 0xc
0041F98D  mov      ebx, eax
0041F98F  cmp      ebx, -1
0041F992  jne      0x41f95d
0041F994  pop      edi
0041F995  pop      esi
0041F996  pop      ebx
0041F997  pop      ecx
0041F998  pop      ebp
0041F999  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00438ED4
- 0x00438EA4
- 0x00438ED4

---

*Extracted with recursive CALL following and DATA context*
