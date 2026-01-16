# LoadFromINI Function Analysis

**Function Address**: 0x004052EB
**Rank**: #35
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 36

```assembly
004052EB  push     ebp
004052EC  mov      ebp, esp
004052EE  add      esp, -0x28
004052F1  push     ebx
004052F2  mov      ebx, dword ptr [ebp + 8]
004052F5  mov      eax, 0x43a938
004052FA  call     0x403618
004052FF  mov      word ptr [ebp - 0x18], 8
00405305  lea      edx, [ebp - 4]
00405308  push     edx
00405309  call     0x438ec2
0040530E  pop      ecx
0040530F  inc      dword ptr [ebp - 0xc]
00405312  mov      word ptr [ebp - 0x18], 0x14
00405318  lea      ecx, [ebp - 4]
0040531B  push     ecx
0040531C  push     dword ptr [ebp + 0xc]
0040531F  call     0x439138
00405324  add      esp, 8
00405327  lea      eax, [ebp - 4]
0040532A  push     eax
0040532B  push     ebx
0040532C  call     0x4051e0
00405331  add      esp, 8
00405334  dec      dword ptr [ebp - 0xc]
00405337  push     2
00405339  lea      edx, [ebp - 4]
0040533C  push     edx
0040533D  call     0x438f64
00405342  add      esp, 8
00405345  mov      ecx, dword ptr [ebp - 0x28]
00405348  mov      dword ptr fs:[0], ecx
0040534F  pop      ebx
00405350  mov      esp, ebp
00405352  pop      ebp
00405353  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438EC2
- 0x00439138
- 0x004051E0
- 0x00438F64

---

*Extracted with recursive CALL following and DATA context*
