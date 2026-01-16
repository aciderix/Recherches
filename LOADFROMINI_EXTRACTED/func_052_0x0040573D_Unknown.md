# LoadFromINI Function Analysis

**Function Address**: 0x0040573D
**Rank**: #52
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 38

```assembly
0040573D  push     ebp
0040573E  mov      ebp, esp
00405740  add      esp, -0x28
00405743  push     ebx
00405744  mov      ebx, dword ptr [ebp + 8]
00405747  mov      eax, 0x43aab4
0040574C  call     0x403618
00405751  mov      word ptr [ebp - 0x18], 8
00405757  push     0x43b19c
0040575C  lea      edx, [ebp - 4]
0040575F  push     edx
00405760  call     0x438e6e
00405765  add      esp, 8
00405768  inc      dword ptr [ebp - 0xc]
0040576B  push     -1
0040576D  push     0
0040576F  lea      ecx, [ebp - 4]
00405772  push     ecx
00405773  lea      eax, [ebx + 4]
00405776  push     eax
00405777  call     0x438f04
0040577C  add      esp, 0x10
0040577F  dec      dword ptr [ebp - 0xc]
00405782  push     2
00405784  lea      edx, [ebp - 4]
00405787  push     edx
00405788  call     0x438f64
0040578D  add      esp, 8
00405790  xor      ecx, ecx
00405792  mov      dword ptr [ebx + 8], ecx
00405795  xor      eax, eax
00405797  mov      dword ptr [ebx + 0xc], eax
0040579A  mov      edx, dword ptr [ebp - 0x28]
0040579D  mov      dword ptr fs:[0], edx
004057A4  pop      ebx
004057A5  mov      esp, ebp
004057A7  pop      ebp
004057A8  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438E6E
- 0x00438F04
- 0x00438F64

---

*Extracted with recursive CALL following and DATA context*
