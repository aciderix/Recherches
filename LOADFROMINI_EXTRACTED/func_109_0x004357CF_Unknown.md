# LoadFromINI Function Analysis

**Function Address**: 0x004357CF
**Rank**: #109
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 61

```assembly
004357CF  push     ebp
004357D0  mov      ebp, esp
004357D2  push     ebx
004357D3  push     esi
004357D4  push     edi
004357D5  mov      ebx, dword ptr [ebp + 8]
004357D8  push     0x44ec70
004357DD  mov      eax, dword ptr [0x44ec9d]
004357E2  call     dword ptr [eax + 4]
004357E5  pop      ecx
004357E6  test     al, al
004357E8  je       0x435844
004357EA  push     ebx
004357EB  mov      edx, dword ptr [ebx + 8]
004357EE  call     dword ptr [edx + 0x7c]
004357F1  pop      ecx
004357F2  test     eax, eax
004357F4  jne      0x435837
004357F6  mov      esi, dword ptr [0x44ecb5]
004357FC  mov      edi, esi
004357FE  cmp      edi, 1
00435801  jl       0x435815
00435803  push     0x44ec74
00435808  mov      eax, dword ptr [0x44ec75]
0043580D  call     dword ptr [eax + 4]
00435810  pop      ecx
00435811  cmp      edi, eax
00435813  jle      0x435819
00435815  xor      edx, edx
00435817  jmp      0x43581e
00435819  mov      edx, 1
0043581E  test     dl, dl
00435820  jne      0x435827
00435822  mov      esi, 1
00435827  push     1
00435829  push     0
0043582B  push     esi
0043582C  push     ebx
0043582D  call     0x4268f8
00435832  add      esp, 0x10
00435835  jmp      0x435851
00435837  push     1
00435839  push     ebx
0043583A  call     0x42ec92
0043583F  add      esp, 8
00435842  jmp      0x435851
00435844  push     1
00435846  push     0
00435848  push     ebx
00435849  call     0x434070
0043584E  add      esp, 0xc
00435851  mov      eax, dword ptr [ebx + 0x68]
00435854  add      eax, 0x19
00435857  push     eax
00435858  call     0x439084
0043585D  pop      ecx
0043585E  pop      edi
0043585F  pop      esi
00435860  pop      ebx
00435861  pop      ebp
00435862  ret      
```

## Strings Referenced

**Total unique strings**: 32

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"SYSTEM"` @ 0x0044CBEF
- `"system"` @ 0x0044CBF6
- `"Cur < Upper"` @ 0x0044CBFD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC09
- `"Precondition"` @ 0x0044CC2B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CC38
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC5C
- `"Precondition"` @ 0x0044CC7E
- `"Cur < Upper"` @ 0x0044CC8B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC97
- `"Precondition"` @ 0x0044CCB9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CCC6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CCEA
- `"Precondition"` @ 0x0044CD0C
- `"GetHandle()"` @ 0x0044CD19
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044CD25
- `"Precondition"` @ 0x0044CD41
- `"Cur < Upper"` @ 0x0044CD4E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CD5A
- `"Precondition"` @ 0x0044CD7C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CD89
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CDAD
- `"Precondition"` @ 0x0044CDCF
- `"Cur < Upper"` @ 0x0044CDDC
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CDE8
- `"Precondition"` @ 0x0044CE0A
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CE17
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CE3B
- `"Precondition"` @ 0x0044CE5D

## DATA Context

**Context around 0x00448F05**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E

**Context around 0x0044CC09**:

- `"andle()"` @ 0x0044CB89
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044CB91
- `"Precondition"` @ 0x0044CBAD
- `"GetHandle()"` @ 0x0044CBBA
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044CBC6
- `"Precondition"` @ 0x0044CBE2
- `"SYSTEM"` @ 0x0044CBEF
- `"system"` @ 0x0044CBF6
- `"Cur < Upper"` @ 0x0044CBFD
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC09
- `"Precondition"` @ 0x0044CC2B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CC38
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC5C
- `"Precondition"` @ 0x0044CC7E

**Context around 0x0044CD89**:

- `"Precondition"` @ 0x0044CD0C
- `"GetHandle()"` @ 0x0044CD19
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044CD25
- `"Precondition"` @ 0x0044CD41
- `"Cur < Upper"` @ 0x0044CD4E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CD5A
- `"Precondition"` @ 0x0044CD7C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CD89
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CDAD
- `"Precondition"` @ 0x0044CDCF
- `"Cur < Upper"` @ 0x0044CDDC
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CDE8

**Context around 0x0044CC8B**:

- `"\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC0B
- `"Precondition"` @ 0x0044CC2B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CC38
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC5C
- `"Precondition"` @ 0x0044CC7E
- `"Cur < Upper"` @ 0x0044CC8B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC97
- `"Precondition"` @ 0x0044CCB9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CCC6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CCEA

**Context around 0x0044CD0C**:

- `"ur < Upper"` @ 0x0044CC8C
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC97
- `"Precondition"` @ 0x0044CCB9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CCC6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CCEA
- `"Precondition"` @ 0x0044CD0C
- `"GetHandle()"` @ 0x0044CD19
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044CD25
- `"Precondition"` @ 0x0044CD41
- `"Cur < Upper"` @ 0x0044CD4E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CD5A
- `"Precondition"` @ 0x0044CD7C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CD89

**Context around 0x0044CE0A**:

- `"im > 0 && Data != 0 && index < Lim"` @ 0x0044CD8A
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CDAD
- `"Precondition"` @ 0x0044CDCF
- `"Cur < Upper"` @ 0x0044CDDC
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CDE8
- `"Precondition"` @ 0x0044CE0A
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CE17
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CE3B
- `"Precondition"` @ 0x0044CE5D
- `"Lim == 0 || (Data != 0 && v.Data != 0)"` @ 0x0044CE6A

**Context around 0x0044CC97**:

- `"\classlib/vectimp.h"` @ 0x0044CC17
- `"Precondition"` @ 0x0044CC2B
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CC38
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC5C
- `"Precondition"` @ 0x0044CC7E
- `"Cur < Upper"` @ 0x0044CC8B
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC97
- `"Precondition"` @ 0x0044CCB9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CCC6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CCEA
- `"Precondition"` @ 0x0044CD0C

**Context around 0x0044CE17**:

- `"a != 0 && index < Lim"` @ 0x0044CD97
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CDAD
- `"Precondition"` @ 0x0044CDCF
- `"Cur < Upper"` @ 0x0044CDDC
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CDE8
- `"Precondition"` @ 0x0044CE0A
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CE17
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CE3B
- `"Precondition"` @ 0x0044CE5D
- `"Lim == 0 || (Data != 0 && v.Data != 0)"` @ 0x0044CE6A
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CE91

**Context around 0x0044CD19**:

- `"\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CC99
- `"Precondition"` @ 0x0044CCB9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CCC6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CCEA
- `"Precondition"` @ 0x0044CD0C
- `"GetHandle()"` @ 0x0044CD19
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044CD25
- `"Precondition"` @ 0x0044CD41
- `"Cur < Upper"` @ 0x0044CD4E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CD5A
- `"Precondition"` @ 0x0044CD7C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CD89

**Context around 0x0044CD25**:

- `"\classlib/vectimp.h"` @ 0x0044CCA5
- `"Precondition"` @ 0x0044CCB9
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CCC6
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CCEA
- `"Precondition"` @ 0x0044CD0C
- `"GetHandle()"` @ 0x0044CD19
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044CD25
- `"Precondition"` @ 0x0044CD41
- `"Cur < Upper"` @ 0x0044CD4E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044CD5A
- `"Precondition"` @ 0x0044CD7C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x0044CD89

## Functions Called

- 0x004268F8
- 0x0042EC92
- 0x00434070
- 0x00439084

---

*Extracted with recursive CALL following and DATA context*
