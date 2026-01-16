# LoadFromINI Function Analysis

**Function Address**: 0x0040B2B4
**Rank**: #128
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 161

```assembly
0040B2B4  push     ebp
0040B2B5  mov      ebp, esp
0040B2B7  add      esp, -0x44
0040B2BA  push     ebx
0040B2BB  push     esi
0040B2BC  lea      esi, [ebp - 0x38]
0040B2BF  mov      eax, 0x43db8d
0040B2C4  call     0x403618
0040B2C9  mov      word ptr [esi + 0x10], 8
0040B2CF  mov      edx, dword ptr [ebp + 8]
0040B2D2  mov      dword ptr [edx], 0x440458
0040B2D8  mov      ecx, dword ptr [ebp + 8]
0040B2DB  mov      dword ptr [ecx], 0x440270
0040B2E1  mov      edx, dword ptr [0x455ad8]
0040B2E7  mov      eax, dword ptr [ebp + 8]
0040B2EA  add      eax, 0xc
0040B2ED  mov      ecx, dword ptr [edx]
0040B2EF  mov      dword ptr [eax], ecx
0040B2F1  mov      eax, dword ptr [ebp + 8]
0040B2F4  add      eax, 0x10
0040B2F7  push     eax
0040B2F8  call     0x438ec2
0040B2FD  pop      ecx
0040B2FE  inc      dword ptr [esi + 0x1c]
0040B301  push     0
0040B303  mov      edx, dword ptr [ebp + 0xc]
0040B306  mov      ecx, dword ptr [edx]
0040B308  push     dword ptr [ecx + 2]
0040B30B  call     0x439168
0040B310  add      esp, 8
0040B313  mov      ebx, eax
0040B315  push     0
0040B317  mov      word ptr [esi + 0x10], 0x14
0040B31D  push     0
0040B31F  push     ebx
0040B320  call     0x407ed3
0040B325  add      esp, 8
0040B328  push     eax
0040B329  lea      eax, [ebp - 4]
0040B32C  push     eax
0040B32D  call     0x438e6e
0040B332  add      esp, 8
0040B335  inc      dword ptr [esi + 0x1c]
0040B338  lea      edx, [ebp - 4]
0040B33B  push     edx
0040B33C  call     0x407fe5
0040B341  add      esp, 8
0040B344  mov      ecx, dword ptr [ebp + 8]
0040B347  mov      dword ptr [ecx + 4], eax
0040B34A  dec      dword ptr [esi + 0x1c]
0040B34D  push     2
0040B34F  lea      eax, [ebp - 4]
0040B352  push     eax
0040B353  call     0x438f64
0040B358  add      esp, 8
0040B35B  push     0
0040B35D  mov      word ptr [esi + 0x10], 0x20
0040B363  push     0
0040B365  push     0
0040B367  call     0x407ed3
0040B36C  add      esp, 8
0040B36F  push     eax
0040B370  lea      edx, [ebp - 8]
0040B373  push     edx
0040B374  call     0x438e6e
0040B379  add      esp, 8
0040B37C  inc      dword ptr [esi + 0x1c]
0040B37F  lea      ecx, [ebp - 8]
0040B382  push     ecx
0040B383  call     0x407fe5
0040B388  add      esp, 8
0040B38B  mov      edx, dword ptr [ebp + 8]
0040B38E  mov      dword ptr [edx + 8], eax
0040B391  dec      dword ptr [esi + 0x1c]
0040B394  push     2
0040B396  lea      eax, [ebp - 8]
0040B399  push     eax
0040B39A  call     0x438f64
0040B39F  add      esp, 8
0040B3A2  lea      ecx, [ebp - 0x3c]
0040B3A5  push     ecx
0040B3A6  push     0
0040B3A8  call     0x407ed3
0040B3AD  add      esp, 8
0040B3B0  mov      word ptr [esi + 0x10], 8
0040B3B6  test     eax, eax
0040B3B8  je       0x40b3e2
0040B3BA  cmp      byte ptr [eax], 0
0040B3BD  je       0x40b3e2
0040B3BF  lea      edx, [ebp - 0x40]
0040B3C2  push     edx
0040B3C3  push     0x43fa48
0040B3C8  push     eax
0040B3C9  call     0x438d96
0040B3CE  add      esp, 0xc
0040B3D1  mov      eax, dword ptr [ebp - 0x40]
0040B3D4  mov      dword ptr [ebp - 0x44], eax
0040B3D7  mov      eax, dword ptr [ebp + 8]
0040B3DA  add      eax, 0xc
0040B3DD  mov      edx, dword ptr [ebp - 0x44]
0040B3E0  mov      dword ptr [eax], edx
0040B3E2  mov      word ptr [esi + 0x10], 0x2c
0040B3E8  push     0x43f76a
0040B3ED  lea      ecx, [ebp - 0xc]
0040B3F0  push     ecx
0040B3F1  call     0x438e6e
0040B3F6  add      esp, 8
0040B3F9  inc      dword ptr [esi + 0x1c]
0040B3FC  lea      eax, [ebp - 0xc]
0040B3FF  push     eax
0040B400  push     dword ptr [ebp - 0x3c]
0040B403  lea      edx, [ebp - 0x10]
0040B406  push     edx
0040B407  call     0x438e6e
0040B40C  add      esp, 8
0040B40F  inc      dword ptr [esi + 0x1c]
0040B412  lea      ecx, [ebp - 0x10]
0040B415  push     ecx
0040B416  lea      eax, [ebp - 0x14]
0040B419  push     eax
0040B41A  call     0x40804e
0040B41F  add      esp, 0xc
0040B422  lea      eax, [ebp - 0x14]
0040B425  inc      dword ptr [esi + 0x1c]
0040B428  push     -1
0040B42A  push     0
0040B42C  push     eax
0040B42D  mov      edx, dword ptr [ebp + 8]
0040B430  add      edx, 0x10
0040B433  push     edx
0040B434  call     0x438f04
0040B439  add      esp, 0x10
0040B43C  dec      dword ptr [esi + 0x1c]
0040B43F  push     2
0040B441  lea      ecx, [ebp - 0x14]
0040B444  push     ecx
0040B445  call     0x438f64
0040B44A  add      esp, 8
0040B44D  dec      dword ptr [esi + 0x1c]
0040B450  push     2
0040B452  lea      eax, [ebp - 0x10]
0040B455  push     eax
0040B456  call     0x438f64
0040B45B  add      esp, 8
0040B45E  dec      dword ptr [esi + 0x1c]
0040B461  push     2
0040B463  lea      edx, [ebp - 0xc]
0040B466  push     edx
0040B467  call     0x438f64
0040B46C  add      esp, 8
0040B46F  push     ebx
0040B470  call     0x438f82
0040B475  pop      ecx
0040B476  mov      ecx, dword ptr [esi]
0040B478  mov      dword ptr fs:[0], ecx
0040B47F  mov      eax, dword ptr [ebp + 8]
0040B482  pop      esi
0040B483  pop      ebx
0040B484  mov      esp, ebp
0040B486  pop      ebp
0040B487  ret      
```

## Strings Referenced

**Total unique strings**: 1

- `"#%lX"` @ 0x0043FA48

## DATA Context

**Context around 0x0043FA48**:

- `"i %i %i %s"` @ 0x0043F9C8
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
- `"Precondition"` @ 0x0043FAB1
- `"GetHandle()"` @ 0x0043FABE

## Functions Called

- 0x00403618
- 0x00438EC2
- 0x00439168
- 0x00407ED3
- 0x00438E6E
- 0x00407FE5
- 0x00438F64
- 0x00407ED3
- 0x00438E6E
- 0x00407FE5
- 0x00438F64
- 0x00407ED3
- 0x00438D96
- 0x00438E6E
- 0x00438E6E
- 0x0040804E
- 0x00438F04
- 0x00438F64
- 0x00438F64
- 0x00438F64
- 0x00438F82

---

*Extracted with recursive CALL following and DATA context*
