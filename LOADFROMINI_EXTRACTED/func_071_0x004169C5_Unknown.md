# LoadFromINI Function Analysis

**Function Address**: 0x004169C5
**Rank**: #71
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 88

```assembly
004169C5  push     ebp
004169C6  mov      ebp, esp
004169C8  add      esp, -0x30
004169CB  push     ebx
004169CC  mov      ebx, dword ptr [ebp + 8]
004169CF  mov      eax, 0x441e14
004169D4  call     0x403618
004169D9  lea      edx, [ebx + 0x1d]
004169DC  push     edx
004169DD  call     0x416654
004169E2  pop      ecx
004169E3  mov      word ptr [ebp - 0x20], 8
004169E9  push     0x442a52
004169EE  lea      ecx, [ebp - 4]
004169F1  push     ecx
004169F2  call     0x438e6e
004169F7  add      esp, 8
004169FA  inc      dword ptr [ebp - 0x14]
004169FD  push     -1
004169FF  push     0
00416A01  lea      eax, [ebp - 4]
00416A04  push     eax
00416A05  lea      edx, [ebx + 0x31]
00416A08  push     edx
00416A09  call     0x438f04
00416A0E  add      esp, 0x10
00416A11  dec      dword ptr [ebp - 0x14]
00416A14  push     2
00416A16  lea      ecx, [ebp - 4]
00416A19  push     ecx
00416A1A  call     0x438f64
00416A1F  add      esp, 8
00416A22  mov      word ptr [ebp - 0x20], 0x14
00416A28  push     0x442a53
00416A2D  lea      eax, [ebp - 8]
00416A30  push     eax
00416A31  call     0x438e6e
00416A36  add      esp, 8
00416A39  inc      dword ptr [ebp - 0x14]
00416A3C  push     -1
00416A3E  push     0
00416A40  lea      edx, [ebp - 8]
00416A43  push     edx
00416A44  lea      ecx, [ebx + 0x35]
00416A47  push     ecx
00416A48  call     0x438f04
00416A4D  add      esp, 0x10
00416A50  dec      dword ptr [ebp - 0x14]
00416A53  push     2
00416A55  lea      eax, [ebp - 8]
00416A58  push     eax
00416A59  call     0x438f64
00416A5E  add      esp, 8
00416A61  mov      word ptr [ebp - 0x20], 0x20
00416A67  push     0x442a54
00416A6C  lea      edx, [ebp - 0xc]
00416A6F  push     edx
00416A70  call     0x438e6e
00416A75  add      esp, 8
00416A78  inc      dword ptr [ebp - 0x14]
00416A7B  push     -1
00416A7D  push     0
00416A7F  lea      ecx, [ebp - 0xc]
00416A82  push     ecx
00416A83  lea      eax, [ebx + 0x39]
00416A86  push     eax
00416A87  call     0x438f04
00416A8C  add      esp, 0x10
00416A8F  dec      dword ptr [ebp - 0x14]
00416A92  push     2
00416A94  lea      edx, [ebp - 0xc]
00416A97  push     edx
00416A98  call     0x438f64
00416A9D  add      esp, 8
00416AA0  xor      ecx, ecx
00416AA2  mov      dword ptr [ebx + 0x41], ecx
00416AA5  mov      dword ptr [ebx + 0x3d], ecx
00416AA8  mov      dword ptr [ebx + 0x45], 1
00416AAF  add      ebx, 0x49
00416AB2  push     ebx
00416AB3  call     0x4056a0
00416AB8  pop      ecx
00416AB9  mov      eax, dword ptr [ebp - 0x30]
00416ABC  mov      dword ptr fs:[0], eax
00416AC2  pop      ebx
00416AC3  mov      esp, ebp
00416AC5  pop      ebp
00416AC6  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00416654
- 0x00438E6E
- 0x00438F04
- 0x00438F64
- 0x00438E6E
- 0x00438F04
- 0x00438F64
- 0x00438E6E
- 0x00438F04
- 0x00438F64
- 0x004056A0

---

*Extracted with recursive CALL following and DATA context*
