# LoadFromINI Function Analysis

**Function Address**: 0x004056E4
**Rank**: #51
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 28

```assembly
004056E4  push     ebp
004056E5  mov      ebp, esp
004056E7  add      esp, -0x24
004056EA  mov      eax, 0x43aa90
004056EF  call     0x403618
004056F4  mov      word ptr [ebp - 0x14], 8
004056FA  mov      edx, dword ptr [ebp + 8]
004056FD  mov      dword ptr [edx], 0x43b554
00405703  mov      ecx, dword ptr [ebp + 8]
00405706  add      ecx, 4
00405709  push     ecx
0040570A  call     0x438ec2
0040570F  pop      ecx
00405710  inc      dword ptr [ebp - 8]
00405713  push     dword ptr [ebp + 8]
00405716  call     0x40573d
0040571B  pop      ecx
0040571C  push     dword ptr [ebp + 0x10]
0040571F  push     dword ptr [ebp + 0xc]
00405722  push     dword ptr [ebp + 8]
00405725  call     0x40596c
0040572A  add      esp, 0xc
0040572D  mov      eax, dword ptr [ebp - 0x24]
00405730  mov      dword ptr fs:[0], eax
00405736  mov      eax, dword ptr [ebp + 8]
00405739  mov      esp, ebp
0040573B  pop      ebp
0040573C  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"-m@"` @ 0x0043B554

## DATA Context

**Context around 0x0043B554**:

- `"condition"` @ 0x0043B4D4
- `"P[@"` @ 0x0043B4EC
- `"cZ@"` @ 0x0043B4F0
- `"+l@"` @ 0x0043B528
- `"+l@"` @ 0x0043B544
- `"1h@"` @ 0x0043B548
- `"-m@"` @ 0x0043B554
- `"%<@"` @ 0x0043B560
- `"i<@"` @ 0x0043B57C
- `"%<@"` @ 0x0043B5AC
- `"%<@"` @ 0x0043B5C4

## Functions Called

- 0x00403618
- 0x00438EC2
- 0x0040573D
- 0x0040596C

---

*Extracted with recursive CALL following and DATA context*
