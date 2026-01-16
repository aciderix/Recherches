# LoadFromINI Function Analysis

**Function Address**: 0x004053E4
**Rank**: #39
**INI String Count**: 6
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 131

```assembly
004053E4  push     ebp
004053E5  mov      ebp, esp
004053E7  add      esp, -0x40
004053EA  push     ebx
004053EB  push     esi
004053EC  push     edi
004053ED  mov      ebx, dword ptr [ebp + 0xc]
004053F0  mov      eax, 0x43a9d4
004053F5  call     0x403618
004053FA  mov      word ptr [ebp - 0x20], 0x14
00405400  push     dword ptr [ebp + 8]
00405403  lea      edx, [ebp - 4]
00405406  push     edx
00405407  call     0x438e38
0040540C  add      esp, 8
0040540F  lea      ecx, [ebp - 4]
00405412  push     ecx
00405413  inc      dword ptr [ebp - 0x14]
00405416  call     0x438e14
0040541B  pop      ecx
0040541C  mov      esi, eax
0040541E  dec      dword ptr [ebp - 0x14]
00405421  push     2
00405423  lea      eax, [ebp - 4]
00405426  push     eax
00405427  call     0x438f64
0040542C  add      esp, 8
0040542F  mov      word ptr [ebp - 0x20], 8
00405435  mov      edx, dword ptr [ebx]
00405437  mov      edi, dword ptr [edx + 6]
0040543A  test     edi, 1
00405440  je       0x405443
00405442  inc      edi
00405443  lea      eax, [edi + 1]
00405446  push     eax
00405447  call     0x438e50
0040544C  pop      ecx
0040544D  mov      dword ptr [ebp - 0x34], eax
00405450  lea      edx, [edi + 1]
00405453  push     edx
00405454  push     0
00405456  push     dword ptr [ebp - 0x34]
00405459  call     0x438dde
0040545E  add      esp, 0xc
00405461  mov      word ptr [ebp - 0x20], 0x20
00405467  push     ebx
00405468  lea      ecx, [ebp - 8]
0040546B  push     ecx
0040546C  call     0x438e38
00405471  add      esp, 8
00405474  lea      eax, [ebp - 8]
00405477  inc      dword ptr [ebp - 0x14]
0040547A  mov      dword ptr [ebp - 0x38], eax
0040547D  mov      edx, dword ptr [ebp - 0x38]
00405480  mov      ecx, dword ptr [edx]
00405482  mov      eax, dword ptr [ecx + 2]
00405485  push     eax
00405486  push     dword ptr [ebp - 0x34]
00405489  call     0x438f0a
0040548E  add      esp, 8
00405491  dec      dword ptr [ebp - 0x14]
00405494  push     2
00405496  lea      edx, [ebp - 8]
00405499  push     edx
0040549A  call     0x438f64
0040549F  add      esp, 8
004054A2  mov      word ptr [ebp - 0x20], 0x2c
004054A8  push     0x43aa74
004054AD  lea      ecx, [ebp - 0xc]
004054B0  push     ecx
004054B1  call     0x438e6e
004054B6  add      esp, 8
004054B9  inc      dword ptr [ebp - 0x14]
004054BC  push     -1
004054BE  push     0
004054C0  lea      eax, [ebp - 0xc]
004054C3  push     eax
004054C4  push     dword ptr [ebp + 0x10]
004054C7  call     0x438f04
004054CC  add      esp, 0x10
004054CF  dec      dword ptr [ebp - 0x14]
004054D2  push     2
004054D4  lea      edx, [ebp - 0xc]
004054D7  push     edx
004054D8  call     0x438f64
004054DD  add      esp, 8
004054E0  xor      ebx, ebx
004054E2  mov      word ptr [ebp - 0x20], 8
004054E8  cmp      edi, ebx
004054EA  jbe      0x405535
004054EC  mov      eax, dword ptr [ebp - 0x34]
004054EF  mov      dx, word ptr [eax + ebx]
004054F3  add      dx, si
004054F6  movzx    ecx, dx
004054F9  push     ecx
004054FA  push     0x43aa75
004054FF  lea      eax, [ebp - 0x40]
00405502  push     eax
00405503  call     0x438dd8
00405508  add      esp, 0xc
0040550B  lea      edx, [ebp - 0x40]
0040550E  push     edx
0040550F  call     0x438e68
00405514  pop      ecx
00405515  push     eax
00405516  push     0
00405518  lea      ecx, [ebp - 0x40]
0040551B  push     ecx
0040551C  push     dword ptr [ebp + 0x10]
0040551F  call     0x438e1a
00405524  add      esp, 0x10
00405527  mov      eax, esi
00405529  neg      eax
0040552B  mov      si, ax
0040552E  add      ebx, 2
00405531  cmp      edi, ebx
00405533  ja       0x4054ec
00405535  push     dword ptr [ebp - 0x34]
00405538  call     0x438f82
0040553D  pop      ecx
0040553E  mov      edx, dword ptr [ebp + 0x10]
00405541  mov      ecx, dword ptr [edx]
00405543  mov      eax, dword ptr [ecx + 6]
00405546  mov      edx, dword ptr [ebp - 0x30]
00405549  mov      dword ptr fs:[0], edx
00405550  pop      edi
00405551  pop      esi
00405552  pop      ebx
00405553  mov      esp, ebp
00405555  pop      ebp
00405556  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"%04X"` @ 0x0043AA75

## DATA Context

**Context around 0x0043AA75**:

- `"%<@"` @ 0x0043AA0C
- `"%<@"` @ 0x0043AA1C
- `"%<@"` @ 0x0043AA2C
- `"%04X"` @ 0x0043AA75
- `"%4hX"` @ 0x0043AA7A
- `"%<@"` @ 0x0043AAA4
- `"%<@"` @ 0x0043AAC8
- `"%<@"` @ 0x0043AAD4

## Functions Called

- 0x00403618
- 0x00438E38
- 0x00438E14
- 0x00438F64
- 0x00438E50
- 0x00438DDE
- 0x00438E38
- 0x00438F0A
- 0x00438F64
- 0x00438E6E
- 0x00438F04
- 0x00438F64
- 0x00438DD8
- 0x00438E68
- 0x00438E1A
- 0x00438F82

---

*Extracted with recursive CALL following and DATA context*
