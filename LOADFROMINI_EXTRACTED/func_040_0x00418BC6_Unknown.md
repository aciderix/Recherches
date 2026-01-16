# LoadFromINI Function Analysis

**Function Address**: 0x00418BC6
**Rank**: #40
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 33

```assembly
00418BC6  push     ebp
00418BC7  mov      ebp, esp
00418BC9  add      esp, -0x24
00418BCC  push     ebx
00418BCD  push     esi
00418BCE  mov      ebx, dword ptr [ebp + 8]
00418BD1  mov      eax, 0x4427dc
00418BD6  call     0x403618
00418BDB  test     ebx, ebx
00418BDD  je       0x418c16
00418BDF  add      dword ptr [ebp - 8], 4
00418BE3  sub      dword ptr [ebp - 8], 3
00418BE7  lea      esi, [ebx + 4]
00418BEA  add      dword ptr [ebp - 8], 3
00418BEE  sub      dword ptr [ebp - 8], 2
00418BF2  add      dword ptr [ebp - 8], 2
00418BF6  dec      dword ptr [ebp - 8]
00418BF9  mov      dword ptr [esi + 1], 0x43b500
00418C00  push     dword ptr [esi + 5]
00418C03  call     0x438f82
00418C08  pop      ecx
00418C09  test     byte ptr [ebp + 0xc], 1
00418C0D  je       0x418c16
00418C0F  push     ebx
00418C10  call     0x438f16
00418C15  pop      ecx
00418C16  mov      eax, dword ptr [ebp - 0x24]
00418C19  mov      dword ptr fs:[0], eax
00418C1F  pop      esi
00418C20  pop      ebx
00418C21  mov      esp, ebp
00418C23  pop      ebp
00418C24  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
