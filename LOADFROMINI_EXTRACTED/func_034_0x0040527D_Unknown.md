# LoadFromINI Function Analysis

**Function Address**: 0x0040527D
**Rank**: #34
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 34

```assembly
0040527D  push     ebp
0040527E  mov      ebp, esp
00405280  add      esp, 0xfffffedc
00405286  push     ebx
00405287  mov      ebx, dword ptr [ebp + 0xc]
0040528A  mov      eax, 0x43a904
0040528F  call     0x403618
00405294  mov      eax, dword ptr [ebx + 4]
00405297  shr      eax, 0x10
0040529A  and      ax, 0xffff
0040529E  movzx    eax, ax
004052A1  movzx    edx, word ptr [ebx + 4]
004052A5  push     edx
004052A6  push     eax
004052A7  push     0x43a99c
004052AC  lea      ecx, [ebp - 0x124]
004052B2  push     ecx
004052B3  call     0x438dd8
004052B8  add      esp, 0x10
004052BB  mov      word ptr [ebp - 0x14], 8
004052C1  lea      eax, [ebp - 0x124]
004052C7  push     eax
004052C8  push     dword ptr [ebp + 8]
004052CB  call     0x438e6e
004052D0  add      esp, 8
004052D3  inc      dword ptr [ebp - 8]
004052D6  mov      eax, dword ptr [ebp + 8]
004052D9  inc      dword ptr [ebp - 8]
004052DC  mov      edx, dword ptr [ebp - 0x24]
004052DF  mov      dword ptr fs:[0], edx
004052E6  pop      ebx
004052E7  mov      esp, ebp
004052E9  pop      ebp
004052EA  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"%u.%u"` @ 0x0043A99C

## DATA Context

**Context around 0x0043A99C**:

- `"%<@"` @ 0x0043A928
- `"%<@"` @ 0x0043A958
- `"%<@"` @ 0x0043A968
- `"%u.%u"` @ 0x0043A99C
- `"%<@"` @ 0x0043A9A4
- `"%<@"` @ 0x0043A9B4
- `"%<@"` @ 0x0043A9C4
- `"%<@"` @ 0x0043AA0C

## Functions Called

- 0x00403618
- 0x00438DD8
- 0x00438E6E

---

*Extracted with recursive CALL following and DATA context*
