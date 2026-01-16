# LoadFromINI Function Analysis

**Function Address**: 0x0041DFA5
**Rank**: #150
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 54

```assembly
0041DFA5  push     ebp
0041DFA6  mov      ebp, esp
0041DFA8  add      esp, -0x2c
0041DFAB  push     ebx
0041DFAC  push     esi
0041DFAD  mov      esi, dword ptr [ebp + 0xc]
0041DFB0  mov      ebx, dword ptr [ebp + 8]
0041DFB3  mov      eax, 0x444644
0041DFB8  call     0x403618
0041DFBD  lea      eax, [ebx + 0x30]
0041DFC0  mov      edx, dword ptr [ebp + 0x10]
0041DFC3  mov      dword ptr [eax], edx
0041DFC5  mov      ecx, dword ptr [ebx + 0x2c]
0041DFC8  mov      dword ptr [ebp - 4], ecx
0041DFCB  cmp      dword ptr [ebp - 4], 0
0041DFCF  je       0x41dffa
0041DFD1  mov      word ptr [ebp - 0x1c], 0x14
0041DFD7  add      dword ptr [ebp - 0x10], 2
0041DFDB  dec      dword ptr [ebp - 0x10]
0041DFDE  push     0
0041DFE0  push     dword ptr [ebp - 4]
0041DFE3  call     0x4392b8
0041DFE8  add      esp, 8
0041DFEB  push     dword ptr [ebp - 4]
0041DFEE  call     0x438f16
0041DFF3  pop      ecx
0041DFF4  mov      word ptr [ebp - 0x1c], 8
0041DFFA  xor      eax, eax
0041DFFC  mov      dword ptr [ebx + 0x2c], eax
0041DFFF  test     esi, esi
0041E001  je       0x41e035
0041E003  push     5
0041E005  call     0x438eec
0041E00A  pop      ecx
0041E00B  mov      dword ptr [ebp - 8], eax
0041E00E  test     eax, eax
0041E010  je       0x41e02f
0041E012  mov      word ptr [ebp - 0x1c], 0x2c
0041E018  push     esi
0041E019  push     dword ptr [ebp - 8]
0041E01C  call     0x43943e
0041E021  add      esp, 8
0041E024  mov      word ptr [ebp - 0x1c], 0x20
0041E02A  mov      edx, dword ptr [ebp - 8]
0041E02D  jmp      0x41e032
0041E02F  mov      edx, dword ptr [ebp - 8]
0041E032  mov      dword ptr [ebx + 0x2c], edx
0041E035  mov      eax, dword ptr [ebp - 0x2c]
0041E038  mov      dword ptr fs:[0], eax
0041E03E  pop      esi
0041E03F  pop      ebx
0041E040  mov      esp, ebp
0041E042  pop      ebp
0041E043  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x004392B8
- 0x00438F16
- 0x00438EEC
- 0x0043943E

---

*Extracted with recursive CALL following and DATA context*
