# LoadFromINI Function Analysis

**Function Address**: 0x0040B235
**Rank**: #127
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 40

```assembly
0040B235  push     ebp
0040B236  mov      ebp, esp
0040B238  add      esp, 0xfffff004
0040B23E  push     eax
0040B23F  add      esp, -0x24
0040B242  push     ebx
0040B243  mov      ebx, dword ptr [ebp + 0xc]
0040B246  mov      eax, 0x43db21
0040B24B  call     0x403618
0040B250  mov      edx, dword ptr [ebx + 4]
0040B253  push     dword ptr [edx + 2]
0040B256  movzx    ecx, word ptr [ebx + 0x18]
0040B25A  push     ecx
0040B25B  push     dword ptr [ebx + 0x14]
0040B25E  push     dword ptr [ebx + 0x10]
0040B261  push     dword ptr [ebx + 0xc]
0040B264  push     dword ptr [ebx + 8]
0040B267  push     dword ptr [ebx + 0x1e]
0040B26A  mov      eax, dword ptr [ebx + 0x1a]
0040B26D  push     dword ptr [eax + 2]
0040B270  push     0x43fa30
0040B275  lea      edx, [ebp - 0x1024]
0040B27B  push     edx
0040B27C  call     0x438dd8
0040B281  add      esp, 0x28
0040B284  mov      word ptr [ebp - 0x14], 8
0040B28A  lea      ecx, [ebp - 0x1024]
0040B290  push     ecx
0040B291  push     dword ptr [ebp + 8]
0040B294  call     0x438e6e
0040B299  add      esp, 8
0040B29C  inc      dword ptr [ebp - 8]
0040B29F  mov      eax, dword ptr [ebp + 8]
0040B2A2  inc      dword ptr [ebp - 8]
0040B2A5  mov      edx, dword ptr [ebp - 0x24]
0040B2A8  mov      dword ptr fs:[0], edx
0040B2AF  pop      ebx
0040B2B0  mov      esp, ebp
0040B2B2  pop      ebp
0040B2B3  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"%s %u %i %i %i %i %u %s"` @ 0x0043FA30

## DATA Context

**Context around 0x0043FA30**:

- `" %s"` @ 0x0043F9B0
- `""%s" %u %u %u %i %i %i %i %s"` @ 0x0043F9B6
- `""%s" %s"` @ 0x0043F9D5
- `"%s %li"` @ 0x0043F9DD
- `"%li %s %li"` @ 0x0043F9E4
- `" then "` @ 0x0043F9F0
- `" else "` @ 0x0043F9F7
- `"%s then %s"` @ 0x0043F9FE
- `"%s then %s else %s"` @ 0x0043FA09
- `"%i %i %i %i %u %s"` @ 0x0043FA1D
- `"%s %u %i %i %i %i %u %s"` @ 0x0043FA30
- `"#%lX"` @ 0x0043FA48
- `"%u %u #%lX %i %u %s"` @ 0x0043FA4D
- `"%s %s"` @ 0x0043FA62
- `"wnd"` @ 0x0043FA6B
- `"commands.cpp"` @ 0x0043FA6F
- `"Precondition"` @ 0x0043FA7C
- `"GetHandle()"` @ 0x0043FA89
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0043FA95

## Functions Called

- 0x00403618
- 0x00438DD8
- 0x00438E6E

---

*Extracted with recursive CALL following and DATA context*
