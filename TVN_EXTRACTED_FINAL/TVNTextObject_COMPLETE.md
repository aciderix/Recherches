# TVNTextObject - Complete Extraction

**Structure**: TVNTextObject
**TYPEINFO Address**: 0x0042A448
**Class Name**: TVNTextObject *
**Destructor**: 0x0042A680

---

## Destructor Analysis

**Function**: 0x0042A680
**Instructions**: 183
**Size**: 397 bytes

### Assembly Code

```assembly
0042A680  cmp      al, byte ptr [eax]
0042A682  add      byte ptr [eax], al
0042A684  add      eax, dword ptr [eax]
0042A686  xor      byte ptr [eax], al
0042A688  add      byte ptr [eax], al
0042A68A  add      byte ptr [eax], al
0042A68C  ja       0x42a68e
0042A68E  add      byte ptr [eax], al
0042A690  inc      eax
0042A691  add      byte ptr [eax], dl
0042A694  add      byte ptr [eax], al
0042A696  add      byte ptr [eax], al
0042A698  add      byte ptr [eax], al
0042A69A  add      byte ptr [eax], al
0042A69C  add      byte ptr [eax], al
0042A69E  add      byte ptr [eax], al
0042A6A0  add      al, 0
0042A6A2  add      byte ptr [eax], al
0042A6A4  add      al, 0
0042A6A6  add      byte ptr [eax], al
0042A6A8  sbb      ebp, dword ptr [ecx + 0x10042]
0042A6AE  push     esp
0042A6AF  add      byte ptr [esi + edx*2 + 0x4e], dl
0042A6B3  push     esp
0042A6B4  js       0x42a72b
0042A6B7  dec      edi
0042A6B8  bound    ebp, qword ptr [edx + 0x65]
0042A6BB  arpl     word ptr [eax + eax], si
0042A6BF  add      byte ptr [esi + 0x41e6], cl
0042A6C5  add      byte ptr [eax], al
0042A6C7  add      byte ptr [ebx], al
0042A6C9  add      byte ptr [eax], al
0042A6CB  add      byte ptr [eax], al
0042A6CD  add      byte ptr [eax], al
0042A6CF  add      byte ptr [eax], al
0042A6D1  add      byte ptr [eax], al
0042A6D3  add      byte ptr [0x3400403c], ah
0042A6D9  add      byte ptr [eax], al
0042A6DB  add      byte ptr [eax], al
0042A6DD  add      byte ptr [eax], al
0042A6DF  add      byte ptr [eax], dh
0042A6E1  add      byte ptr [eax], al
0042A6E3  add      byte ptr [ebx], al
0042A6E5  add      byte ptr [eax], dh
0042A6E7  add      byte ptr [eax], al
0042A6E9  add      byte ptr [eax], al
0042A6EB  add      byte ptr [edi], dh
0042A6EE  add      byte ptr [eax], al
0042A6F0  inc      eax
0042A6F1  add      byte ptr [eax], dl
0042A6F4  add      byte ptr [eax], al
0042A6F6  add      byte ptr [eax], al
0042A6F8  add      byte ptr [eax], al
0042A6FA  add      byte ptr [eax], al
0042A6FC  add      byte ptr [eax], al
0042A6FE  add      byte ptr [eax], al
0042A700  add      eax, dword ptr [eax]
0042A702  add      byte ptr [eax], al
0042A704  add      eax, dword ptr [eax]
0042A706  add      byte ptr [eax], al
0042A708  js       0x42a6b3
0042A70A  inc      edx
0042A70B  add      byte ptr [ecx], al
0042A70D  add      byte ptr [eax + eax + 0x54], dl
0042A711  push     esi
0042A712  dec      esi
0042A713  dec      ecx
0042A714  insd     dword ptr es:[edi], dx
0042A715  popal    
0042A716  dec      edi
0042A719  bound    ebp, qword ptr [edx + 0x65]
0042A71C  arpl     word ptr [eax + eax], si
0042A720  mov      fs, esi
0042A722  inc      ecx
0042A723  add      byte ptr [eax], al
0042A725  add      byte ptr [eax], al
0042A727  add      byte ptr [ebx], al
0042A729  add      byte ptr [eax], al
0042A72B  add      byte ptr [eax], al
0042A72D  add      byte ptr [eax], al
0042A72F  add      byte ptr [eax], al
0042A731  add      byte ptr [eax], al
0042A733  add      byte ptr [eax], al
0042A735  add      byte ptr [eax], al
0042A737  add      byte ptr [ebp - 0x75], dl
0042A73A  in       al, dx
0042A73B  add      esp, -0x24
0042A73E  push     ebx
0042A73F  mov      ebx, dword ptr [ebp + 8]
0042A742  mov      eax, 0x448d28
0042A747  call     0x403618
0042A74C  test     ebx, ebx
0042A74E  je       0x42a76f
0042A750  add      dword ptr [ebp - 8], 2
0042A754  dec      dword ptr [ebp - 8]
0042A757  push     2
0042A759  push     ebx
0042A75A  call     0x438f64
0042A75F  add      esp, 8
0042A762  test     byte ptr [ebp + 0xc], 1
... (83 more instructions)
```

### Strings Referenced

- `"TextObject"` @ 0x0042A6B3
- `"_^["` @ 0x004037D9
- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"_^["` @ 0x004037D9
- `"_^["` @ 0x004037D9
- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"_^["` @ 0x004037D9

### Functions Called

- 0x00403618
- 0x00438F64
- 0x00438F16

### DATA Context (Neighbor Strings)

**Context 0x0042A633 - 0x0042A733**:

- `"opstream"` @ 0x0042A65C
- `"TVNTextObject"` @ 0x0042A6B0
- `"%<@"` @ 0x0042A6D4
- `"TVNImageObject"` @ 0x0042A710

**Context 0x00403759 - 0x00403859**:


**Context 0x0044EA50 - 0x0044EB50**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24

**Context 0x00403759 - 0x00403859**:


**Context 0x00403759 - 0x00403859**:


**Context 0x0044EA50 - 0x0044EB50**:

- `"Illegal mode in _vector_delete_"` @ 0x0044EAD0
- `"Illegal mode in _vector_new_"` @ 0x0044EB24

**Context 0x00403759 - 0x00403859**:


---

*Extracted with all expert fixes (#1-#6)*
