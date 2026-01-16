# LoadFromINI Function Analysis

**Function Address**: 0x004057E2
**Rank**: #54
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 53

```assembly
004057E2  push     ebp
004057E3  mov      ebp, esp
004057E5  add      esp, -0x2c
004057E8  push     ebx
004057E9  push     esi
004057EA  mov      esi, dword ptr [ebp + 0xc]
004057ED  mov      ebx, dword ptr [ebp + 8]
004057F0  mov      eax, 0x43aae4
004057F5  call     0x403618
004057FA  mov      word ptr [ebp - 0x1c], 8
00405800  push     esi
00405801  lea      edx, [ebp - 4]
00405804  push     edx
00405805  call     0x438e6e
0040580A  add      esp, 8
0040580D  inc      dword ptr [ebp - 0x10]
00405810  lea      ecx, [ebp - 4]
00405813  push     ecx
00405814  lea      eax, [ebp - 8]
00405817  push     eax
00405818  call     0x438e38
0040581D  add      esp, 8
00405820  lea      eax, [ebp - 8]
00405823  inc      dword ptr [ebp - 0x10]
00405826  push     -1
00405828  push     0
0040582A  push     eax
0040582B  lea      edx, [ebx + 4]
0040582E  push     edx
0040582F  call     0x438f04
00405834  add      esp, 0x10
00405837  dec      dword ptr [ebp - 0x10]
0040583A  push     2
0040583C  lea      ecx, [ebp - 8]
0040583F  push     ecx
00405840  call     0x438f64
00405845  add      esp, 8
00405848  dec      dword ptr [ebp - 0x10]
0040584B  push     2
0040584D  lea      eax, [ebp - 4]
00405850  push     eax
00405851  call     0x438f64
00405856  add      esp, 8
00405859  mov      edx, dword ptr [esi + 0x100]
0040585F  mov      dword ptr [ebx + 0xc], edx
00405862  mov      eax, ebx
00405864  mov      edx, dword ptr [ebp - 0x2c]
00405867  mov      dword ptr fs:[0], edx
0040586E  pop      esi
0040586F  pop      ebx
00405870  mov      esp, ebp
00405872  pop      ebp
00405873  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438E6E
- 0x00438E38
- 0x00438F04
- 0x00438F64
- 0x00438F64

---

*Extracted with recursive CALL following and DATA context*
