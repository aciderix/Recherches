# LoadFromINI Function Analysis

**Function Address**: 0x004372B9
**Rank**: #92
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 58

```assembly
004372B9  push     ebp
004372BA  mov      ebp, esp
004372BC  add      esp, -0x2c
004372BF  push     ebx
004372C0  mov      ebx, dword ptr [ebp + 8]
004372C3  mov      eax, 0x44d538
004372C8  call     0x403618
004372CD  mov      word ptr [ebp - 0x18], 0x14
004372D3  push     0xff
004372D8  call     0x438e50
004372DD  pop      ecx
004372DE  mov      dword ptr [ebp - 4], eax
004372E1  inc      dword ptr [ebp - 0xc]
004372E4  mov      word ptr [ebp - 0x18], 8
004372EA  cmp      dword ptr [ebx + 8], 0
004372EE  je       0x437348
004372F0  push     0x44d840
004372F5  mov      edx, dword ptr [ebx + 4]
004372F8  push     dword ptr [edx]
004372FA  push     0x44d827
004372FF  push     dword ptr [ebp - 4]
00437302  call     0x438dd8
00437307  add      esp, 0x10
0043730A  cmp      dword ptr [ebx + 8], 0
0043730E  je       0x437324
00437310  lea      ecx, [ebp - 0x2c]
00437313  push     ecx
00437314  push     dword ptr [ebp + 0xc]
00437317  push     dword ptr [ebp - 4]
0043731A  push     dword ptr [ebx + 8]
0043731D  call     0x439876
00437322  jmp      0x437326
00437324  xor      eax, eax
00437326  test     eax, eax
00437328  setne    al
0043732B  and      eax, 1
0043732E  push     eax
0043732F  dec      dword ptr [ebp - 0xc]
00437332  push     dword ptr [ebp - 4]
00437335  call     0x438f82
0043733A  pop      ecx
0043733B  pop      eax
0043733C  mov      edx, dword ptr [ebp - 0x28]
0043733F  mov      dword ptr fs:[0], edx
00437346  jmp      0x437362
00437348  xor      eax, eax
0043734A  push     eax
0043734B  dec      dword ptr [ebp - 0xc]
0043734E  push     dword ptr [ebp - 4]
00437351  call     0x438f82
00437356  pop      ecx
00437357  pop      eax
00437358  mov      edx, dword ptr [ebp - 0x28]
0043735B  mov      dword ptr fs:[0], edx
00437362  pop      ebx
00437363  mov      esp, ebp
00437365  pop      ebp
00437366  ret      
```

## Strings Referenced

**Total unique strings**: 2

- `"\StringFileInfo\%08lx\%s"` @ 0x0044D827
- `"ProductName"` @ 0x0044D840

## DATA Context

**Context around 0x0044D840**:

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
- `"GetHandle()"` @ 0x0044D89C
- `"C:\BC5\INCLUDE\owl/static.h"` @ 0x0044D8A8

**Context around 0x0044D827**:

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
- `"GetHandle()"` @ 0x0044D89C

## Functions Called

- 0x00403618
- 0x00438E50
- 0x00438DD8
- 0x00439876
- 0x00438F82
- 0x00438F82

---

*Extracted with recursive CALL following and DATA context*
