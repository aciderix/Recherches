# LoadFromINI Function Analysis

**Function Address**: 0x0040AE3E
**Rank**: #125
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 37

```assembly
0040AE3E  push     ebp
0040AE3F  mov      ebp, esp
0040AE41  add      esp, 0xfffff004
0040AE47  push     eax
0040AE48  add      esp, -0x24
0040AE4B  push     ebx
0040AE4C  mov      ebx, dword ptr [ebp + 0xc]
0040AE4F  mov      eax, 0x43d9c9
0040AE54  call     0x403618
0040AE59  mov      edx, dword ptr [ebx + 4]
0040AE5C  push     dword ptr [edx + 2]
0040AE5F  movzx    ecx, word ptr [ebx + 0x18]
0040AE63  push     ecx
0040AE64  push     dword ptr [ebx + 0x14]
0040AE67  push     dword ptr [ebx + 0x10]
0040AE6A  push     dword ptr [ebx + 0xc]
0040AE6D  push     dword ptr [ebx + 8]
0040AE70  push     0x43fa1d
0040AE75  lea      eax, [ebp - 0x1024]
0040AE7B  push     eax
0040AE7C  call     0x438dd8
0040AE81  add      esp, 0x20
0040AE84  mov      word ptr [ebp - 0x14], 8
0040AE8A  lea      edx, [ebp - 0x1024]
0040AE90  push     edx
0040AE91  push     dword ptr [ebp + 8]
0040AE94  call     0x438e6e
0040AE99  add      esp, 8
0040AE9C  inc      dword ptr [ebp - 8]
0040AE9F  mov      eax, dword ptr [ebp + 8]
0040AEA2  inc      dword ptr [ebp - 8]
0040AEA5  mov      edx, dword ptr [ebp - 0x24]
0040AEA8  mov      dword ptr fs:[0], edx
0040AEAF  pop      ebx
0040AEB0  mov      esp, ebp
0040AEB2  pop      ebp
0040AEB3  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"%i %i %i %i %u %s"` @ 0x0043FA1D

## DATA Context

**Context around 0x0043FA1D**:

- `""%s" %u %i %i %i %i %s"` @ 0x0043F99D
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
