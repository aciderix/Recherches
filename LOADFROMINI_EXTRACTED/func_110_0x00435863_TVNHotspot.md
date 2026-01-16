# LoadFromINI Function Analysis

**Function Address**: 0x00435863
**Rank**: #110
**INI String Count**: 4
**Identified Structure**: TVNHotspot
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 16

```assembly
00435863  push     ebp
00435864  mov      ebp, esp
00435866  push     0x44c54e
0043586B  call     0x439246
00435870  mov      dword ptr [0x44a5e8], eax
00435875  push     0x44c55b
0043587A  call     0x439246
0043587F  mov      dword ptr [0x44a600], eax
00435884  push     0x44c565
00435889  call     0x439246
0043588E  mov      dword ptr [0x44a618], eax
00435893  push     0x44c56d
00435898  call     0x439246
0043589D  mov      dword ptr [0x44a630], eax
004358A2  pop      ebp
004358A3  ret      
```

## Strings Referenced

**Total unique strings**: 4

- `"wm_vncommand"` @ 0x0044C54E
- `"wm_scroll"` @ 0x0044C55B
- `"wm_zoom"` @ 0x0044C565
- `"wm_fullscreen"` @ 0x0044C56D

## DATA Context

**Context around 0x0044C56D**:

- `"BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C4ED
- `"Precondition"` @ 0x0044C50C
- `"GetHandle()"` @ 0x0044C519
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C525
- `"Precondition"` @ 0x0044C541
- `"wm_vncommand"` @ 0x0044C54E
- `"wm_scroll"` @ 0x0044C55B
- `"wm_zoom"` @ 0x0044C565
- `"wm_fullscreen"` @ 0x0044C56D
- `"Img"` @ 0x0044C57B
- `"gdiobjec.h"` @ 0x0044C57F
- `"Precondition"` @ 0x0044C58A
- `"Img"` @ 0x0044C597
- `"gdiobjec.h"` @ 0x0044C59B
- `"Precondition"` @ 0x0044C5A6
- `"cdaudio"` @ 0x0044C5B3
- `"avivideo"` @ 0x0044C5BB
- `"GetHandle()"` @ 0x0044C5C4
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C5D0
- `"Precondition"` @ 0x0044C5EC

**Context around 0x0044C55B**:

- `"&& index < Lim"` @ 0x0044C4DB
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C4EA
- `"Precondition"` @ 0x0044C50C
- `"GetHandle()"` @ 0x0044C519
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C525
- `"Precondition"` @ 0x0044C541
- `"wm_vncommand"` @ 0x0044C54E
- `"wm_scroll"` @ 0x0044C55B
- `"wm_zoom"` @ 0x0044C565
- `"wm_fullscreen"` @ 0x0044C56D
- `"Img"` @ 0x0044C57B
- `"gdiobjec.h"` @ 0x0044C57F
- `"Precondition"` @ 0x0044C58A
- `"Img"` @ 0x0044C597
- `"gdiobjec.h"` @ 0x0044C59B
- `"Precondition"` @ 0x0044C5A6
- `"cdaudio"` @ 0x0044C5B3
- `"avivideo"` @ 0x0044C5BB
- `"GetHandle()"` @ 0x0044C5C4
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C5D0

**Context around 0x0044C565**:

- `" Lim"` @ 0x0044C4E5
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C4EA
- `"Precondition"` @ 0x0044C50C
- `"GetHandle()"` @ 0x0044C519
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C525
- `"Precondition"` @ 0x0044C541
- `"wm_vncommand"` @ 0x0044C54E
- `"wm_scroll"` @ 0x0044C55B
- `"wm_zoom"` @ 0x0044C565
- `"wm_fullscreen"` @ 0x0044C56D
- `"Img"` @ 0x0044C57B
- `"gdiobjec.h"` @ 0x0044C57F
- `"Precondition"` @ 0x0044C58A
- `"Img"` @ 0x0044C597
- `"gdiobjec.h"` @ 0x0044C59B
- `"Precondition"` @ 0x0044C5A6
- `"cdaudio"` @ 0x0044C5B3
- `"avivideo"` @ 0x0044C5BB
- `"GetHandle()"` @ 0x0044C5C4
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C5D0

**Context around 0x0044C54E**:

- `"|| Data != 0 && index < Lim"` @ 0x0044C4CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x0044C4EA
- `"Precondition"` @ 0x0044C50C
- `"GetHandle()"` @ 0x0044C519
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0044C525
- `"Precondition"` @ 0x0044C541
- `"wm_vncommand"` @ 0x0044C54E
- `"wm_scroll"` @ 0x0044C55B
- `"wm_zoom"` @ 0x0044C565
- `"wm_fullscreen"` @ 0x0044C56D
- `"Img"` @ 0x0044C57B
- `"gdiobjec.h"` @ 0x0044C57F
- `"Precondition"` @ 0x0044C58A
- `"Img"` @ 0x0044C597
- `"gdiobjec.h"` @ 0x0044C59B
- `"Precondition"` @ 0x0044C5A6
- `"cdaudio"` @ 0x0044C5B3
- `"avivideo"` @ 0x0044C5BB
- `"GetHandle()"` @ 0x0044C5C4

## Functions Called

- 0x00439246
- 0x00439246
- 0x00439246
- 0x00439246

---

*Extracted with recursive CALL following and DATA context*
