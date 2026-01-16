# LoadFromINI Function Analysis

**Function Address**: 0x00411E9F
**Rank**: #4
**INI String Count**: 14
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 40

```assembly
00411E9F  push     ebp
00411EA0  mov      ebp, esp
00411EA2  add      esp, -0x24
00411EA5  push     ebx
00411EA6  push     esi
00411EA7  mov      esi, dword ptr [ebp + 0xc]
00411EAA  mov      ebx, dword ptr [ebp + 8]
00411EAD  cmp      ebx, esi
00411EAF  jne      0x411ebf
00411EB1  mov      eax, ebx
00411EB3  mov      edx, dword ptr [ebp - 0x24]
00411EB6  mov      dword ptr fs:[0], edx
00411EBD  jmp      0x411ef4
00411EBF  push     ebx
00411EC0  mov      ecx, dword ptr [ebx]
00411EC2  call     dword ptr [ecx + 0xc]
00411EC5  pop      ecx
00411EC6  mov      eax, dword ptr [esi + 0x31]
00411EC9  mov      dword ptr [ebx + 0x31], eax
00411ECC  lea      eax, [esi + 8]
00411ECF  push     eax
00411ED0  lea      edx, [ebx + 8]
00411ED3  push     edx
00411ED4  mov      ecx, dword ptr [ebx + 0x29]
00411ED7  call     dword ptr [ecx + 4]
00411EDA  add      esp, 8
00411EDD  mov      eax, dword ptr [esi + 0x2d]
00411EE0  mov      dword ptr [ebx + 0x2d], eax
00411EE3  push     dword ptr [esi + 0x35]
00411EE6  push     dword ptr [esi + 0x39]
00411EE9  push     ebx
00411EEA  mov      edx, dword ptr [ebx]
00411EEC  call     dword ptr [edx + 0x10]
00411EEF  add      esp, 0xc
00411EF2  mov      eax, ebx
00411EF4  pop      esi
00411EF5  pop      ebx
00411EF6  mov      esp, ebp
00411EF8  pop      ebp
00411EF9  ret      
```

## Strings Referenced

**Total unique strings**: 0



---

*Extracted with recursive CALL following and DATA context*
