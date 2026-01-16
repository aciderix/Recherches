# LoadFromINI Function Analysis

**Function Address**: 0x0043241E
**Rank**: #168
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 13

```assembly
0043241E  push     ebp
0043241F  mov      ebp, esp
00432421  mov      eax, dword ptr [ebp + 8]
00432424  cmp      dword ptr [ebp + 0xc], 0
00432428  setne    dl
0043242B  and      edx, 1
0043242E  push     edx
0043242F  push     eax
00432430  call     0x42ecb9
00432435  add      esp, 8
00432438  xor      eax, eax
0043243A  pop      ebp
0043243B  ret      
```

## Strings Referenced

**Total unique strings**: 6

- `"GetHandle()"` @ 0x0044C702
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C70E
- `"Precondition"` @ 0x0044C72A
- `"GetHandle()"` @ 0x0044C737
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C743
- `"Precondition"` @ 0x0044C75F

## DATA Context

**Context around 0x0044C702**:

- `"window.h"` @ 0x0044C682
- `"Precondition"` @ 0x0044C68B
- `"GetHandle()"` @ 0x0044C698
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C6A4
- `"Precondition"` @ 0x0044C6C0
- `"GetHandle()"` @ 0x0044C6CD
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C6D9
- `"Precondition"` @ 0x0044C6F5
- `"GetHandle()"` @ 0x0044C702
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C70E
- `"Precondition"` @ 0x0044C72A
- `"GetHandle()"` @ 0x0044C737
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C743
- `"Precondition"` @ 0x0044C75F
- `"Cur < Upper"` @ 0x0044C76C
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C778

**Context around 0x0044C743**:

- `"condition"` @ 0x0044C6C3
- `"GetHandle()"` @ 0x0044C6CD
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C6D9
- `"Precondition"` @ 0x0044C6F5
- `"GetHandle()"` @ 0x0044C702
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C70E
- `"Precondition"` @ 0x0044C72A
- `"GetHandle()"` @ 0x0044C737
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C743
- `"Precondition"` @ 0x0044C75F
- `"Cur < Upper"` @ 0x0044C76C
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C778
- `"Precondition"` @ 0x0044C79A
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044C7A7

**Context around 0x0044C72A**:

- `"\INCLUDE\owl/window.h"` @ 0x0044C6AA
- `"Precondition"` @ 0x0044C6C0
- `"GetHandle()"` @ 0x0044C6CD
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C6D9
- `"Precondition"` @ 0x0044C6F5
- `"GetHandle()"` @ 0x0044C702
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C70E
- `"Precondition"` @ 0x0044C72A
- `"GetHandle()"` @ 0x0044C737
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C743
- `"Precondition"` @ 0x0044C75F
- `"Cur < Upper"` @ 0x0044C76C
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C778
- `"Precondition"` @ 0x0044C79A
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044C7A7

**Context around 0x0044C70E**:

- `"condition"` @ 0x0044C68E
- `"GetHandle()"` @ 0x0044C698
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C6A4
- `"Precondition"` @ 0x0044C6C0
- `"GetHandle()"` @ 0x0044C6CD
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C6D9
- `"Precondition"` @ 0x0044C6F5
- `"GetHandle()"` @ 0x0044C702
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C70E
- `"Precondition"` @ 0x0044C72A
- `"GetHandle()"` @ 0x0044C737
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C743
- `"Precondition"` @ 0x0044C75F
- `"Cur < Upper"` @ 0x0044C76C
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C778

**Context around 0x0044C737**:

- `"window.h"` @ 0x0044C6B7
- `"Precondition"` @ 0x0044C6C0
- `"GetHandle()"` @ 0x0044C6CD
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C6D9
- `"Precondition"` @ 0x0044C6F5
- `"GetHandle()"` @ 0x0044C702
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C70E
- `"Precondition"` @ 0x0044C72A
- `"GetHandle()"` @ 0x0044C737
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C743
- `"Precondition"` @ 0x0044C75F
- `"Cur < Upper"` @ 0x0044C76C
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C778
- `"Precondition"` @ 0x0044C79A
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044C7A7

**Context around 0x0044C75F**:

- `"\INCLUDE\owl/window.h"` @ 0x0044C6DF
- `"Precondition"` @ 0x0044C6F5
- `"GetHandle()"` @ 0x0044C702
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C70E
- `"Precondition"` @ 0x0044C72A
- `"GetHandle()"` @ 0x0044C737
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C743
- `"Precondition"` @ 0x0044C75F
- `"Cur < Upper"` @ 0x0044C76C
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C778
- `"Precondition"` @ 0x0044C79A
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044C7A7
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C7CB

## Functions Called

- 0x0042ECB9

---

*Extracted with recursive CALL following and DATA context*
