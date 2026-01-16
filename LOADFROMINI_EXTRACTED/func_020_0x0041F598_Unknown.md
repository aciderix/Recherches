# LoadFromINI Function Analysis

**Function Address**: 0x0041F598
**Rank**: #20
**INI String Count**: 8
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 78

```assembly
0041F598  push     ebp
0041F599  mov      ebp, esp
0041F59B  add      esp, -0x24
0041F59E  push     ebx
0041F59F  lea      ebx, [ebp - 0x24]
0041F5A2  mov      eax, 0x444d64
0041F5A7  call     0x403618
0041F5AC  mov      dword ptr [ebx + 0x1c], 0x11
0041F5B3  cmp      dword ptr [ebp + 8], 0
0041F5B7  je       0x41f6a0
0041F5BD  mov      word ptr [ebx + 0x10], 8
0041F5C3  mov      edx, dword ptr [ebp + 8]
0041F5C6  mov      dword ptr [edx], 0x446a88
0041F5CC  push     dword ptr [ebp + 8]
0041F5CF  call     0x421aaf
0041F5D4  pop      ecx
0041F5D5  dec      dword ptr [ebx + 0x1c]
0041F5D8  push     2
0041F5DA  mov      ecx, dword ptr [ebp + 8]
0041F5DD  add      ecx, 0x36
0041F5E0  push     ecx
0041F5E1  call     0x438f64
0041F5E6  add      esp, 8
0041F5E9  sub      dword ptr [ebx + 0x1c], 8
0041F5ED  mov      eax, dword ptr [ebp + 8]
0041F5F0  add      eax, 0x1d
0041F5F3  add      dword ptr [ebx + 0x1c], 8
0041F5F7  sub      dword ptr [ebx + 0x1c], 7
0041F5FB  add      dword ptr [ebx + 0x1c], 7
0041F5FF  sub      dword ptr [ebx + 0x1c], 6
0041F603  add      dword ptr [ebx + 0x1c], 6
0041F607  sub      dword ptr [ebx + 0x1c], 5
0041F60B  add      dword ptr [ebx + 0x1c], 5
0041F60F  sub      dword ptr [ebx + 0x1c], 4
0041F613  add      dword ptr [ebx + 0x1c], 4
0041F617  sub      dword ptr [ebx + 0x1c], 3
0041F61B  add      eax, 4
0041F61E  add      dword ptr [ebx + 0x1c], 3
0041F622  sub      dword ptr [ebx + 0x1c], 2
0041F626  add      dword ptr [ebx + 0x1c], 2
0041F62A  dec      dword ptr [ebx + 0x1c]
0041F62D  mov      dword ptr [eax + 1], 0x4469d8
0041F634  push     dword ptr [eax + 5]
0041F637  call     0x438f82
0041F63C  pop      ecx
0041F63D  sub      dword ptr [ebx + 0x1c], 8
0041F641  mov      eax, dword ptr [ebp + 8]
0041F644  add      eax, 4
0041F647  add      dword ptr [ebx + 0x1c], 8
0041F64B  sub      dword ptr [ebx + 0x1c], 7
0041F64F  add      dword ptr [ebx + 0x1c], 7
0041F653  sub      dword ptr [ebx + 0x1c], 6
0041F657  add      dword ptr [ebx + 0x1c], 6
0041F65B  sub      dword ptr [ebx + 0x1c], 5
0041F65F  add      dword ptr [ebx + 0x1c], 5
0041F663  sub      dword ptr [ebx + 0x1c], 4
0041F667  add      dword ptr [ebx + 0x1c], 4
0041F66B  sub      dword ptr [ebx + 0x1c], 3
0041F66F  add      eax, 4
0041F672  add      dword ptr [ebx + 0x1c], 3
0041F676  sub      dword ptr [ebx + 0x1c], 2
0041F67A  add      dword ptr [ebx + 0x1c], 2
0041F67E  dec      dword ptr [ebx + 0x1c]
0041F681  mov      dword ptr [eax + 1], 0x446a30
0041F688  push     dword ptr [eax + 5]
0041F68B  call     0x438f82
0041F690  pop      ecx
0041F691  test     byte ptr [ebp + 0xc], 1
0041F695  je       0x41f6a0
0041F697  push     dword ptr [ebp + 8]
0041F69A  call     0x438f16
0041F69F  pop      ecx
0041F6A0  mov      edx, dword ptr [ebx]
0041F6A2  mov      dword ptr fs:[0], edx
0041F6A9  pop      ebx
0041F6AA  mov      esp, ebp
0041F6AC  pop      ebp
0041F6AD  ret      
```

## Strings Referenced

**Total unique strings**: 2

- `"!8B"` @ 0x00446A30
- `"T9B"` @ 0x00446A88

## DATA Context

**Context around 0x00446A88**:

- `"!8B"` @ 0x00446A30
- `",8B"` @ 0x00446A34
- `"78B"` @ 0x00446A38
- `">8B"` @ 0x00446A3C
- `"C8B"` @ 0x00446A40
- `"!8B"` @ 0x00446A4C
- `",8B"` @ 0x00446A50
- `"78B"` @ 0x00446A54
- `">8B"` @ 0x00446A58
- `"39B"` @ 0x00446A68
- `">9B"` @ 0x00446A6C
- `"I9B"` @ 0x00446A70
- `">8B"` @ 0x00446A74
- `"R2B"` @ 0x00446A78
- `"T9B"` @ 0x00446A88
- `"%<@"` @ 0x00446AC8
- `"%<@"` @ 0x00446AD4

**Context around 0x00446A30**:

- `"classlib/vectimp.h"` @ 0x004469B0
- `"Check"` @ 0x004469C3
- `"!8B"` @ 0x00446A30
- `",8B"` @ 0x00446A34
- `"78B"` @ 0x00446A38
- `">8B"` @ 0x00446A3C
- `"C8B"` @ 0x00446A40
- `"!8B"` @ 0x00446A4C
- `",8B"` @ 0x00446A50
- `"78B"` @ 0x00446A54
- `">8B"` @ 0x00446A58
- `"39B"` @ 0x00446A68
- `">9B"` @ 0x00446A6C
- `"I9B"` @ 0x00446A70
- `">8B"` @ 0x00446A74
- `"R2B"` @ 0x00446A78
- `"T9B"` @ 0x00446A88

## Functions Called

- 0x00403618
- 0x00421AAF
- 0x00438F64
- 0x00438F82
- 0x00438F82
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
