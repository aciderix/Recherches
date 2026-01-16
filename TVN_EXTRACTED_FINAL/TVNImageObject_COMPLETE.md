# TVNImageObject - Complete Extraction

**Structure**: TVNImageObject
**TYPEINFO Address**: 0x0042A40B
**Class Name**: TVNImageObject *
**Destructor**: 0x0042A6E0

---

## Destructor Analysis

**Function**: 0x0042A6E0
**Instructions**: 143
**Size**: 301 bytes

### Assembly Code

```assembly
0042A6E0  xor      byte ptr [eax], al
0042A6E2  add      byte ptr [eax], al
0042A6E4  add      eax, dword ptr [eax]
0042A6E6  xor      byte ptr [eax], al
0042A6E8  add      byte ptr [eax], al
0042A6EA  add      byte ptr [eax], al
0042A6EC  ja       0x42a6ee
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
0042A766  je       0x42a76f
0042A768  push     ebx
0042A769  call     0x438f16
0042A76E  pop      ecx
0042A76F  mov      edx, dword ptr [ebp - 0x24]
0042A772  mov      dword ptr fs:[0], edx
0042A779  pop      ebx
0042A77A  mov      esp, ebp
0042A77C  pop      ebp
0042A77D  ret      
0042A77E  or       eax, 0x3000000
0042A783  add      byte ptr [eax], dh
0042A785  add      byte ptr [ecx], al
0042A787  add      byte ptr [eax], al
0042A789  add      byte ptr [edi], dl
0042A78C  add      byte ptr [eax], al
0042A78E  insb     byte ptr es:[edi], dx
0042A78F  add      byte ptr [eax + eax - 0x3f], bh
0042A793  outsd    dx, dword ptr [esi]
0042A794  inc      eax
0042A795  add      byte ptr [ecx], al
0042A797  add      byte ptr [ecx], al
0042A799  add      bh, cl
0042A79B  outsd    dx, dword ptr [esi]
0042A79C  inc      eax
0042A79D  add      byte ptr [ecx], al
0042A79F  add      byte ptr [eax], al
0042A7A1  add      byte ptr [ecx], al
0042A7A3  add      byte ptr [eax], al
0042A7A5  add      byte ptr [edx], dh
0042A7A7  stosb    byte ptr es:[edi], al
0042A7A8  inc      edx
0042A7A9  add      byte ptr [ecx], al
0042A7AB  add      byte ptr [eax + 0x65565400], al
0042A7B1  arpl     word ptr [edi + ebp*2 + 0x72], si
0042A7B5  dec      ecx
0042A7B6  insd     dword ptr es:[edi], dx
0042A7B7  jo       0x42a7fb
0042A7B9  popal    
0042A7BA  jae      0x42a821
... (43 more instructions)
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
