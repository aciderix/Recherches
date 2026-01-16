# LoadFromINI Function Analysis

**Function Address**: 0x0041DF3E
**Rank**: #149
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 42

```assembly
0041DF3E  push     ebp
0041DF3F  mov      ebp, esp
0041DF41  add      esp, -8
0041DF44  push     ebx
0041DF45  push     esi
0041DF46  push     edi
0041DF47  mov      ebx, dword ptr [ebp + 8]
0041DF4A  lea      esi, [ebx + 0x18]
0041DF4D  lea      edi, [ebx + 4]
0041DF50  mov      ecx, 4
0041DF55  rep movsd dword ptr es:[edi], dword ptr [esi]
0041DF57  test     byte ptr [ebx + 0x28], 2
0041DF5B  je       0x41df73
0041DF5D  xor      eax, eax
0041DF5F  mov      dword ptr [ebp - 8], eax
0041DF62  xor      edx, edx
0041DF64  mov      dword ptr [ebp - 4], edx
0041DF67  mov      ecx, dword ptr [ebp - 8]
0041DF6A  mov      dword ptr [ebp + 0xc], ecx
0041DF6D  mov      ecx, dword ptr [ebp - 4]
0041DF70  mov      dword ptr [ebp + 0x10], ecx
0041DF73  test     byte ptr [ebx + 0x28], 4
0041DF77  je       0x41df85
0041DF79  xor      eax, eax
0041DF7B  mov      dword ptr [ebp + 0x14], eax
0041DF7E  mov      dword ptr [ebp + 0x18], 0x3ff00000
0041DF85  lea      edx, [ebp + 0xc]
0041DF88  push     edx
0041DF89  push     dword ptr [ebp + 0x18]
0041DF8C  push     dword ptr [ebp + 0x14]
0041DF8F  lea      eax, [ebx + 4]
0041DF92  push     eax
0041DF93  call     0x405119
0041DF98  add      esp, 0x10
0041DF9B  lea      eax, [ebx + 4]
0041DF9E  pop      edi
0041DF9F  pop      esi
0041DFA0  pop      ebx
0041DFA1  pop      ecx
0041DFA2  pop      ecx
0041DFA3  pop      ebp
0041DFA4  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00405119

---

*Extracted with recursive CALL following and DATA context*
