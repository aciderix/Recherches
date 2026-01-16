# LoadFromINI Function Analysis

**Function Address**: 0x00418C99
**Rank**: #41
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 29

```assembly
00418C99  push     ebp
00418C9A  mov      ebp, esp
00418C9C  add      esp, -0x24
00418C9F  push     ebx
00418CA0  push     esi
00418CA1  mov      ebx, dword ptr [ebp + 8]
00418CA4  mov      eax, 0x442808
00418CA9  call     0x403618
00418CAE  test     ebx, ebx
00418CB0  je       0x418cd8
00418CB2  add      dword ptr [ebp - 8], 2
00418CB6  dec      dword ptr [ebp - 8]
00418CB9  mov      dword ptr [ebx + 1], 0x442ca8
00418CC0  push     dword ptr [ebx + 5]
00418CC3  call     0x438f82
00418CC8  pop      ecx
00418CC9  test     byte ptr [ebp + 0xc], 1
00418CCD  je       0x418cd8
00418CCF  mov      esi, ebx
00418CD1  push     esi
00418CD2  call     0x438f16
00418CD7  pop      ecx
00418CD8  mov      edx, dword ptr [ebp - 0x24]
00418CDB  mov      dword ptr fs:[0], edx
00418CE2  pop      esi
00418CE3  pop      ebx
00418CE4  mov      esp, ebp
00418CE6  pop      ebp
00418CE7  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
