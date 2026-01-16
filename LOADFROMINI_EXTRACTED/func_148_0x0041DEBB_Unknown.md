# LoadFromINI Function Analysis

**Function Address**: 0x0041DEBB
**Rank**: #148
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 56

```assembly
0041DEBB  push     ebp
0041DEBC  mov      ebp, esp
0041DEBE  add      esp, -0x20
0041DEC1  push     ebx
0041DEC2  push     esi
0041DEC3  push     edi
0041DEC4  mov      ebx, dword ptr [ebp + 8]
0041DEC7  mov      eax, dword ptr [ebp + 0xc]
0041DECA  mov      esi, eax
0041DECC  lea      edi, [ebx + 0xd]
0041DECF  mov      ecx, 4
0041DED4  rep movsd dword ptr es:[edi], dword ptr [esi]
0041DED6  push     ebx
0041DED7  mov      eax, dword ptr [ebx + 5]
0041DEDA  call     dword ptr [eax + 8]
0041DEDD  pop      ecx
0041DEDE  mov      dword ptr [ebp - 0x14], eax
0041DEE1  fild     dword ptr [ebp - 0x14]
0041DEE4  lea      esi, [ebx + 0xd]
0041DEE7  mov      eax, dword ptr [esi + 0xc]
0041DEEA  sub      eax, dword ptr [esi + 4]
0041DEED  mov      dword ptr [ebp - 0x18], eax
0041DEF0  fild     dword ptr [ebp - 0x18]
0041DEF3  fdivrp   st(1)
0041DEF5  fstp     qword ptr [ebp - 8]
0041DEF8  push     ebx
0041DEF9  mov      edx, dword ptr [ebx + 5]
0041DEFC  call     dword ptr [edx + 4]
0041DEFF  pop      ecx
0041DF00  mov      dword ptr [ebp - 0x1c], eax
0041DF03  fild     dword ptr [ebp - 0x1c]
0041DF06  lea      edi, [ebx + 0xd]
0041DF09  mov      eax, dword ptr [edi + 8]
0041DF0C  sub      eax, dword ptr [edi]
0041DF0E  mov      dword ptr [ebp - 0x20], eax
0041DF11  fild     dword ptr [ebp - 0x20]
0041DF14  fdivrp   st(1)
0041DF16  fstp     qword ptr [ebp - 0x10]
0041DF19  fld      qword ptr [ebp - 0x10]
0041DF1C  fcomp    qword ptr [ebp - 8]
0041DF1F  fnstsw   ax
0041DF21  sahf     
0041DF22  jbe      0x41df29
0041DF24  lea      edx, [ebp - 0x10]
0041DF27  jmp      0x41df2c
0041DF29  lea      edx, [ebp - 8]
0041DF2C  mov      eax, dword ptr [edx]
0041DF2E  mov      dword ptr [ebx + 0x1d], eax
0041DF31  mov      eax, dword ptr [edx + 4]
0041DF34  mov      dword ptr [ebx + 0x21], eax
0041DF37  pop      edi
0041DF38  pop      esi
0041DF39  pop      ebx
0041DF3A  mov      esp, ebp
0041DF3C  pop      ebp
0041DF3D  ret      
```

## Strings Referenced

**Total unique strings**: 0



---

*Extracted with recursive CALL following and DATA context*
