# LoadFromINI Function Analysis

**Function Address**: 0x0041D5D3
**Rank**: #140
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 69

```assembly
0041D5D3  push     ebp
0041D5D4  mov      ebp, esp
0041D5D6  add      esp, -0x28
0041D5D9  push     ebx
0041D5DA  push     esi
0041D5DB  push     edi
0041D5DC  mov      eax, 0x4443dc
0041D5E1  call     0x403618
0041D5E6  mov      word ptr [ebp - 0x18], 8
0041D5EC  push     dword ptr [ebp + 8]
0041D5EF  call     0x439714
0041D5F4  pop      ecx
0041D5F5  add      dword ptr [ebp - 0xc], 2
0041D5F9  mov      edx, dword ptr [ebp + 8]
0041D5FC  mov      dword ptr [edx + 5], 0x4449ec
0041D603  mov      ecx, dword ptr [ebp + 8]
0041D606  xor      eax, eax
0041D608  mov      dword ptr [ecx + 9], eax
0041D60B  mov      word ptr [ebp - 0x18], 0x14
0041D611  push     0x1c
0041D613  call     0x438eec
0041D618  pop      ecx
0041D619  mov      dword ptr [ebp - 4], eax
0041D61C  test     eax, eax
0041D61E  je       0x41d644
0041D620  mov      word ptr [ebp - 0x18], 0x2c
0041D626  mov      edx, dword ptr [ebp + 0xc]
0041D629  mov      ecx, dword ptr [edx]
0041D62B  push     dword ptr [ecx + 2]
0041D62E  push     dword ptr [ebp - 4]
0041D631  call     0x4394c8
0041D636  add      esp, 8
0041D639  mov      word ptr [ebp - 0x18], 0x20
0041D63F  mov      eax, dword ptr [ebp - 4]
0041D642  jmp      0x41d647
0041D644  mov      eax, dword ptr [ebp - 4]
0041D647  mov      edx, dword ptr [ebp + 8]
0041D64A  mov      dword ptr [edx + 9], eax
0041D64D  push     dword ptr [ebp + 0x10]
0041D650  mov      ecx, dword ptr [ebp + 8]
0041D653  push     dword ptr [ecx + 9]
0041D656  push     dword ptr [ebp + 8]
0041D659  call     0x4396ba
0041D65E  add      esp, 0xc
0041D661  mov      word ptr [ebp - 0x18], 8
0041D667  jmp      0x41d69b
0041D669  push     3
0041D66B  mov      eax, dword ptr [ebp + 8]
0041D66E  push     dword ptr [eax + 9]
0041D671  call     0x439678
0041D676  add      esp, 8
0041D679  mov      edx, dword ptr [ebp + 8]
0041D67C  xor      ecx, ecx
0041D67E  mov      dword ptr [edx + 9], ecx
0041D681  push     0
0041D683  push     0x7fdf
0041D688  call     0x4393fc
0041D68D  add      esp, 8
0041D690  mov      word ptr [ebp - 0x18], 0x1c
0041D696  call     0x438ee6
0041D69B  mov      eax, dword ptr [ebp - 0x28]
0041D69E  mov      dword ptr fs:[0], eax
0041D6A4  mov      eax, dword ptr [ebp + 8]
0041D6A7  pop      edi
0041D6A8  pop      esi
0041D6A9  pop      ebx
0041D6AA  mov      esp, ebp
0041D6AC  pop      ebp
0041D6AD  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00439714
- 0x00438EEC
- 0x004394C8
- 0x004396BA
- 0x00439678
- 0x004393FC
- 0x00438EE6

---

*Extracted with recursive CALL following and DATA context*
