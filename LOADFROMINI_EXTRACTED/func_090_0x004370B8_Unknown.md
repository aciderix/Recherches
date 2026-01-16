# LoadFromINI Function Analysis

**Function Address**: 0x004370B8
**Rank**: #90
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 143

```assembly
004370B8  push     ebp
004370B9  mov      ebp, esp
004370BB  add      esp, 0xfffffec8
004370C1  push     ebx
004370C2  mov      ebx, dword ptr [ebp + 0xc]
004370C5  mov      eax, 0x44d4d4
004370CA  call     0x403618
004370CF  mov      word ptr [ebp - 0x20], 8
004370D5  mov      edx, dword ptr [ebp + 8]
004370D8  mov      dword ptr [edx], 0x44d984
004370DE  mov      word ptr [ebp - 0x20], 0x20
004370E4  push     0xff
004370E9  call     0x438e50
004370EE  pop      ecx
004370EF  mov      dword ptr [ebp - 4], eax
004370F2  inc      dword ptr [ebp - 0x14]
004370F5  mov      word ptr [ebp - 0x20], 0x14
004370FB  mov      ecx, dword ptr [ebp + 8]
004370FE  xor      eax, eax
00437100  mov      dword ptr [ecx + 8], eax
00437103  cmp      dword ptr [ebx + 8], 0x20
00437107  ja       0x437192
0043710D  lea      edx, [ebp - 0x30]
00437110  push     edx
00437111  push     0
00437113  push     0
00437115  push     0
00437117  push     1
00437119  push     0x403be0
0043711E  push     0
00437120  mov      word ptr [ebp - 0x20], 0x2c
00437126  push     0x3da
0043712B  push     0x44d7e5
00437130  push     0x44d7c1
00437135  push     0x44d801
0043713A  lea      ecx, [ebp - 8]
0043713D  push     ecx
0043713E  call     0x438f10
00437143  add      esp, 0x14
00437146  lea      eax, [ebp - 8]
00437149  push     eax
0043714A  inc      dword ptr [ebp - 0x14]
0043714D  lea      edx, [ebp - 0xc]
00437150  push     edx
00437151  call     0x438de4
00437156  add      esp, 8
00437159  inc      dword ptr [ebp - 0x14]
0043715C  mov      word ptr [ebp - 0x20], 0x38
00437162  dec      dword ptr [ebp - 0x14]
00437165  push     2
00437167  lea      ecx, [ebp - 8]
0043716A  push     ecx
0043716B  call     0x438f64
00437170  add      esp, 8
00437173  mov      word ptr [ebp - 0x20], 0x2c
00437179  add      dword ptr [ebp - 0x14], 2
0043717D  add      dword ptr [ebp - 0x14], 3
00437181  lea      eax, [ebp - 0xc]
00437184  push     eax
00437185  push     0x403b88
0043718A  call     0x438eaa
0043718F  add      esp, 0x24
00437192  push     0xff
00437197  lea      edx, [ebp - 0x138]
0043719D  push     edx
0043719E  push     dword ptr [ebx + 8]
004371A1  call     0x438fdc
004371A6  lea      ecx, [ebp - 0x138]
004371AC  push     ecx
004371AD  lea      eax, [ebp - 0x138]
004371B3  push     eax
004371B4  call     0x439264
004371B9  lea      edx, [ebp - 0x34]
004371BC  push     edx
004371BD  lea      ecx, [ebp - 0x138]
004371C3  push     ecx
004371C4  call     0x43987c
004371C9  mov      ebx, eax
004371CB  mov      word ptr [ebp - 0x20], 0x14
004371D1  test     ebx, ebx
004371D3  je       0x43726c
004371D9  push     ebx
004371DA  call     0x438e50
004371DF  pop      ecx
004371E0  mov      edx, dword ptr [ebp + 8]
004371E3  mov      dword ptr [edx + 8], eax
004371E6  mov      eax, dword ptr [ebp + 8]
004371E9  push     dword ptr [eax + 8]
004371EC  push     ebx
004371ED  push     dword ptr [ebp - 0x34]
004371F0  lea      ecx, [ebp - 0x138]
004371F6  push     ecx
004371F7  call     0x439882
004371FC  test     eax, eax
004371FE  je       0x43726c
00437200  push     0x44d80e
00437205  push     dword ptr [ebp - 4]
00437208  call     0x438f0a
0043720D  add      esp, 8
00437210  lea      eax, [ebp - 0x38]
00437213  push     eax
00437214  mov      edx, dword ptr [ebp + 8]
00437217  add      edx, 4
0043721A  push     edx
0043721B  push     dword ptr [ebp - 4]
0043721E  mov      ecx, dword ptr [ebp + 8]
00437221  push     dword ptr [ecx + 8]
00437224  call     0x439876
00437229  test     eax, eax
0043722B  jne      0x437243
0043722D  mov      eax, dword ptr [ebp + 8]
00437230  push     dword ptr [eax + 8]
00437233  call     0x438f82
00437238  pop      ecx
00437239  mov      edx, dword ptr [ebp + 8]
0043723C  xor      ecx, ecx
0043723E  mov      dword ptr [edx + 8], ecx
00437241  jmp      0x43726c
00437243  mov      eax, dword ptr [ebp + 8]
00437246  mov      edx, dword ptr [eax + 4]
00437249  mov      ecx, dword ptr [edx]
0043724B  shr      ecx, 0x10
0043724E  and      cx, 0xffff
00437253  movzx    eax, cx
00437256  mov      edx, dword ptr [ebp + 8]
00437259  mov      ecx, dword ptr [edx + 4]
0043725C  movzx    edx, word ptr [ecx]
0043725F  shl      edx, 0x10
00437262  or       eax, edx
00437264  mov      ecx, dword ptr [ebp + 8]
00437267  mov      edx, dword ptr [ecx + 4]
0043726A  mov      dword ptr [edx], eax
0043726C  dec      dword ptr [ebp - 0x14]
0043726F  push     dword ptr [ebp - 4]
00437272  call     0x438f82
00437277  pop      ecx
00437278  mov      eax, dword ptr [ebp - 0x30]
0043727B  mov      dword ptr fs:[0], eax
00437281  mov      eax, dword ptr [ebp + 8]
00437284  pop      ebx
00437285  mov      esp, ebp
00437287  pop      ebp
00437288  ret      
```

## Strings Referenced

**Total unique strings**: 4

- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x0044D7C1
- `"C:\BC5\INCLUDE\owl/module.h"` @ 0x0044D7E5
- `"Precondition"` @ 0x0044D801
- `"\VarFileInfo\Translation"` @ 0x0044D80E

## DATA Context

**Context around 0x0044D7C1**:

- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x0044D7C1
- `"C:\BC5\INCLUDE\owl/module.h"` @ 0x0044D7E5
- `"Precondition"` @ 0x0044D801
- `"\VarFileInfo\Translation"` @ 0x0044D80E
- `"\StringFileInfo\%08lx\%s"` @ 0x0044D827
- `"ProductName"` @ 0x0044D840

**Context around 0x0044D7E5**:

- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x0044D7C1
- `"C:\BC5\INCLUDE\owl/module.h"` @ 0x0044D7E5
- `"Precondition"` @ 0x0044D801
- `"\VarFileInfo\Translation"` @ 0x0044D80E
- `"\StringFileInfo\%08lx\%s"` @ 0x0044D827
- `"ProductName"` @ 0x0044D840
- `"\StringFileInfo\%08lx\%s"` @ 0x0044D84C

**Context around 0x0044D801**:

- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x0044D7C1
- `"C:\BC5\INCLUDE\owl/module.h"` @ 0x0044D7E5
- `"Precondition"` @ 0x0044D801
- `"\VarFileInfo\Translation"` @ 0x0044D80E
- `"\StringFileInfo\%08lx\%s"` @ 0x0044D827
- `"ProductName"` @ 0x0044D840
- `"\StringFileInfo\%08lx\%s"` @ 0x0044D84C
- `"ProductVersion"` @ 0x0044D865
- `"\StringFileInfo\%08lx\%s"` @ 0x0044D874

**Context around 0x0044D80E**:

- `"Handle > HINSTANCE(HINSTANCE_ERROR)"` @ 0x0044D7C1
- `"C:\BC5\INCLUDE\owl/module.h"` @ 0x0044D7E5
- `"Precondition"` @ 0x0044D801
- `"\VarFileInfo\Translation"` @ 0x0044D80E
- `"\StringFileInfo\%08lx\%s"` @ 0x0044D827
- `"ProductName"` @ 0x0044D840
- `"\StringFileInfo\%08lx\%s"` @ 0x0044D84C
- `"ProductVersion"` @ 0x0044D865
- `"\StringFileInfo\%08lx\%s"` @ 0x0044D874
- `"LegalCopyright"` @ 0x0044D88D

## Functions Called

- 0x00403618
- 0x00438E50
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438FDC
- 0x00439264
- 0x0043987C
- 0x00438E50
- 0x00439882
- 0x00438F0A
- 0x00439876
- 0x00438F82
- 0x00438F82

---

*Extracted with recursive CALL following and DATA context*
