# LoadFromINI Function Analysis

**Function Address**: 0x0040D786
**Rank**: #63
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 80

```assembly
0040D786  push     ebp
0040D787  mov      ebp, esp
0040D789  add      esp, -0x28
0040D78C  push     ebx
0040D78D  push     esi
0040D78E  lea      esi, [ebp - 0x28]
0040D791  mov      eax, 0x43e966
0040D796  call     0x403618
0040D79B  mov      word ptr [esi + 0x10], 8
0040D7A1  mov      edx, dword ptr [ebp + 8]
0040D7A4  xor      ecx, ecx
0040D7A6  mov      dword ptr [edx], ecx
0040D7A8  mov      ebx, dword ptr [ebp + 8]
0040D7AB  add      ebx, 4
0040D7AE  mov      dword ptr [ebx + 1], 0x4401ac
0040D7B5  push     0x14
0040D7B7  call     0x438e50
0040D7BC  pop      ecx
0040D7BD  mov      dword ptr [ebp - 4], eax
0040D7C0  cmp      dword ptr [ebp - 4], 0
0040D7C4  je       0x40d7f4
0040D7C6  mov      word ptr [esi + 0x10], 0x20
0040D7CC  push     0x40f471
0040D7D1  push     1
0040D7D3  push     0x40f3ed
0040D7D8  push     0x211
0040D7DD  push     1
0040D7DF  push     0x10
0040D7E1  push     dword ptr [ebp - 4]
0040D7E4  call     0x4037e0
0040D7E9  add      esp, 0x1c
0040D7EC  mov      word ptr [esi + 0x10], 0x14
0040D7F2  jmp      0x40d7f7
0040D7F4  mov      eax, dword ptr [ebp - 4]
0040D7F7  mov      dword ptr [ebx + 5], eax
0040D7FA  mov      dword ptr [ebx + 9], 1
0040D801  inc      dword ptr [esi + 0x1c]
0040D804  mov      dword ptr [ebx + 1], 0x4401c8
0040D80B  add      dword ptr [esi + 0x1c], 2
0040D80F  mov      dword ptr [ebx + 1], 0x4401e4
0040D816  xor      edx, edx
0040D818  mov      dword ptr [ebx + 0xd], edx
0040D81B  mov      dword ptr [ebx + 0x11], 1
0040D822  add      dword ptr [esi + 0x1c], 3
0040D826  add      dword ptr [esi + 0x1c], 4
0040D82A  add      dword ptr [esi + 0x1c], 5
0040D82E  add      dword ptr [esi + 0x1c], 6
0040D832  add      dword ptr [esi + 0x1c], 7
0040D836  add      dword ptr [esi + 0x1c], 8
0040D83A  mov      eax, dword ptr [ebp + 8]
0040D83D  add      eax, 0x19
0040D840  mov      dword ptr [eax], 0x4402d4
0040D846  inc      dword ptr [esi + 0x1c]
0040D849  lea      edx, [eax + 4]
0040D84C  mov      dword ptr [edx], 0x4402c0
0040D852  inc      dword ptr [esi + 0x1c]
0040D855  mov      dword ptr [eax], 0x4402e8
0040D85B  mov      dword ptr [eax + 4], 0x4402f8
0040D862  add      dword ptr [esi + 0x1c], 3
0040D866  mov      ecx, dword ptr [ebp + 8]
0040D869  mov      dword ptr [ecx + 0x21], 0x44016c
0040D870  mov      eax, dword ptr [ebp + 8]
0040D873  mov      dword ptr [eax + 0x19], 0x440188
0040D87A  mov      edx, dword ptr [ebp + 8]
0040D87D  mov      dword ptr [edx + 0x1d], 0x440198
0040D884  push     dword ptr [ebp + 0x10]
0040D887  push     dword ptr [ebp + 0xc]
0040D88A  mov      ecx, dword ptr [ebp + 8]
0040D88D  push     ecx
0040D88E  mov      eax, dword ptr [ecx + 0x21]
0040D891  call     dword ptr [eax + 0x10]
0040D894  add      esp, 0xc
0040D897  mov      edx, dword ptr [esi]
0040D899  mov      dword ptr fs:[0], edx
0040D8A0  mov      eax, dword ptr [ebp + 8]
0040D8A3  pop      esi
0040D8A4  pop      ebx
0040D8A5  mov      esp, ebp
0040D8A7  pop      ebp
0040D8A8  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## DATA Context

**Context around 0x0044EB64**:

- `"tor_delete_"` @ 0x0044EAE4
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD
- `" N?A"` @ 0x0044EBCF
- `" w1B"` @ 0x0044EBDB

**Context around 0x0044EB41**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64
- `" HDB"` @ 0x0044EBA5
- `" cXC"` @ 0x0044EBAB
- `" 8/@"` @ 0x0044EBBD

**Context around 0x0044EB24**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24
- `"Illegal dtorMode in _vector_new_"` @ 0x0044EB41
- `"Pure virtual function called"` @ 0x0044EB64

## Functions Called

- 0x00403618
- 0x00438E50
- 0x004037E0

---

*Extracted with recursive CALL following and DATA context*
