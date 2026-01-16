# LoadFromINI Function Analysis

**Function Address**: 0x0041DA7B
**Rank**: #145
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 49

```assembly
0041DA7B  push     ebp
0041DA7C  mov      ebp, esp
0041DA7E  add      esp, -0x2c
0041DA81  push     ebx
0041DA82  mov      ebx, dword ptr [ebp + 8]
0041DA85  mov      eax, 0x444594
0041DA8A  call     0x403618
0041DA8F  test     ebx, ebx
0041DA91  je       0x41dafe
0041DA93  mov      dword ptr [ebx], 0x4449dc
0041DA99  test     byte ptr [ebx + 0xc], 1
0041DA9D  je       0x41dac5
0041DA9F  mov      edx, dword ptr [ebx + 4]
0041DAA2  mov      dword ptr [ebp - 4], edx
0041DAA5  cmp      dword ptr [ebp - 4], 0
0041DAA9  je       0x41dac5
0041DAAB  mov      word ptr [ebp - 0x1c], 0x14
0041DAB1  push     3
0041DAB3  mov      ecx, dword ptr [ebp - 4]
0041DAB6  push     ecx
0041DAB7  mov      eax, dword ptr [ecx + 5]
0041DABA  call     dword ptr [eax]
0041DABC  add      esp, 8
0041DABF  mov      word ptr [ebp - 0x1c], 8
0041DAC5  test     byte ptr [ebx + 0xc], 2
0041DAC9  je       0x41daf1
0041DACB  mov      edx, dword ptr [ebx + 8]
0041DACE  mov      dword ptr [ebp - 8], edx
0041DAD1  cmp      dword ptr [ebp - 8], 0
0041DAD5  je       0x41daf1
0041DAD7  mov      word ptr [ebp - 0x1c], 0x2c
0041DADD  push     3
0041DADF  mov      ecx, dword ptr [ebp - 8]
0041DAE2  push     ecx
0041DAE3  mov      eax, dword ptr [ecx + 5]
0041DAE6  call     dword ptr [eax]
0041DAE8  add      esp, 8
0041DAEB  mov      word ptr [ebp - 0x1c], 0x20
0041DAF1  test     byte ptr [ebp + 0xc], 1
0041DAF5  je       0x41dafe
0041DAF7  push     ebx
0041DAF8  call     0x438f16
0041DAFD  pop      ecx
0041DAFE  mov      edx, dword ptr [ebp - 0x2c]
0041DB01  mov      dword ptr fs:[0], edx
0041DB08  pop      ebx
0041DB09  mov      esp, ebp
0041DB0B  pop      ebp
0041DB0C  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438F16

---

*Extracted with recursive CALL following and DATA context*
