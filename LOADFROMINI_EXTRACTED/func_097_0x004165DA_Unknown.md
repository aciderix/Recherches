# LoadFromINI Function Analysis

**Function Address**: 0x004165DA
**Rank**: #97
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 42

```assembly
004165DA  push     ebp
004165DB  mov      ebp, esp
004165DD  add      esp, -0x24
004165E0  mov      eax, 0x441cf4
004165E5  call     0x403618
004165EA  mov      word ptr [ebp - 0x14], 8
004165F0  mov      edx, dword ptr [ebp + 8]
004165F3  mov      dword ptr [edx], 0x442d54
004165F9  mov      ecx, dword ptr [ebp + 8]
004165FC  add      ecx, 4
004165FF  push     ecx
00416600  call     0x438ec2
00416605  pop      ecx
00416606  inc      dword ptr [ebp - 8]
00416609  mov      eax, dword ptr [ebp + 8]
0041660C  add      eax, 8
0041660F  push     eax
00416610  call     0x438ec2
00416615  pop      ecx
00416616  inc      dword ptr [ebp - 8]
00416619  mov      edx, dword ptr [ebp + 8]
0041661C  add      edx, 0xc
0041661F  push     edx
00416620  call     0x438ec2
00416625  pop      ecx
00416626  inc      dword ptr [ebp - 8]
00416629  push     dword ptr [ebp + 8]
0041662C  call     0x416654
00416631  pop      ecx
00416632  push     dword ptr [ebp + 0x10]
00416635  push     dword ptr [ebp + 0xc]
00416638  mov      ecx, dword ptr [ebp + 8]
0041663B  push     ecx
0041663C  mov      eax, dword ptr [ecx]
0041663E  call     dword ptr [eax]
00416640  add      esp, 0xc
00416643  mov      edx, dword ptr [ebp - 0x24]
00416646  mov      dword ptr fs:[0], edx
0041664D  mov      eax, dword ptr [ebp + 8]
00416650  mov      esp, ebp
00416652  pop      ebp
00416653  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438EC2
- 0x00438EC2
- 0x00438EC2
- 0x00416654

---

*Extracted with recursive CALL following and DATA context*
