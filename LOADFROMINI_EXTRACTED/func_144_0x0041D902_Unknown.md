# LoadFromINI Function Analysis

**Function Address**: 0x0041D902
**Rank**: #144
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 126

```assembly
0041D902  push     ebp
0041D903  mov      ebp, esp
0041D905  add      esp, -0x30
0041D908  push     ebx
0041D909  push     esi
0041D90A  push     edi
0041D90B  mov      edi, dword ptr [ebp + 0xc]
0041D90E  mov      ebx, dword ptr [ebp + 8]
0041D911  mov      eax, 0x444554
0041D916  call     0x403618
0041D91B  cmp      dword ptr [ebx + 9], 0
0041D91F  je       0x41d929
0041D921  test     edi, edi
0041D923  jne      0x41d9ab
0041D929  lea      edx, [ebp - 0x2c]
0041D92C  push     edx
0041D92D  push     0
0041D92F  push     0
0041D931  push     0
0041D933  push     1
0041D935  push     0x403be0
0041D93A  push     0
0041D93C  mov      word ptr [ebp - 0x1c], 8
0041D942  push     0x52
0041D944  push     0x444878
0041D949  push     0x444869
0041D94E  push     0x444885
0041D953  lea      ecx, [ebp - 4]
0041D956  push     ecx
0041D957  call     0x438f10
0041D95C  add      esp, 0x14
0041D95F  lea      eax, [ebp - 4]
0041D962  push     eax
0041D963  inc      dword ptr [ebp - 0x10]
0041D966  lea      edx, [ebp - 8]
0041D969  push     edx
0041D96A  call     0x438de4
0041D96F  add      esp, 8
0041D972  inc      dword ptr [ebp - 0x10]
0041D975  mov      word ptr [ebp - 0x1c], 0x14
0041D97B  dec      dword ptr [ebp - 0x10]
0041D97E  push     2
0041D980  lea      ecx, [ebp - 4]
0041D983  push     ecx
0041D984  call     0x438f64
0041D989  add      esp, 8
0041D98C  mov      word ptr [ebp - 0x1c], 8
0041D992  add      dword ptr [ebp - 0x10], 2
0041D996  add      dword ptr [ebp - 0x10], 3
0041D99A  lea      eax, [ebp - 8]
0041D99D  push     eax
0041D99E  push     0x403b88
0041D9A3  call     0x438eaa
0041D9A8  add      esp, 0x24
0041D9AB  mov      edx, dword ptr [ebx + 9]
0041D9AE  mov      ebx, dword ptr [edx + 5]
0041D9B1  lea      esi, [ebx + 0x28]
0041D9B4  cmp      dword ptr [ebx + 0x20], 0
0041D9B8  je       0x41d9c0
0041D9BA  mov      ax, word ptr [ebx + 0x20]
0041D9BE  jmp      0x41d9cb
0041D9C0  mov      dx, word ptr [ebx + 0xe]
0041D9C4  push     edx
0041D9C5  call     0x439162
0041D9CA  pop      ecx
0041D9CB  mov      word ptr [ebp - 0x2e], ax
0041D9CF  mov      cx, word ptr [ebp - 0x2e]
0041D9D3  cmp      cx, word ptr [ebp + 0x14]
0041D9D7  jae      0x41d9de
0041D9D9  lea      eax, [ebp - 0x2e]
0041D9DC  jmp      0x41d9e1
0041D9DE  lea      eax, [ebp + 0x14]
0041D9E1  mov      dx, word ptr [eax]
0041D9E4  mov      word ptr [ebp + 0x14], dx
0041D9E8  cmp      word ptr [ebp + 0x14], 0
0041D9ED  je       0x41da5f
0041D9EF  movzx    ecx, word ptr [ebp + 0x14]
0041D9F3  shl      ecx, 2
0041D9F6  push     ecx
0041D9F7  call     0x438e50
0041D9FC  pop      ecx
0041D9FD  mov      ebx, eax
0041D9FF  xor      eax, eax
0041DA01  cmp      ax, word ptr [ebp + 0x14]
0041DA05  jae      0x41da3e
0041DA07  movzx    edx, ax
0041DA0A  mov      cl, byte ptr [esi + edx*4 + 2]
0041DA0E  movzx    edx, ax
0041DA11  mov      byte ptr [ebx + edx*4], cl
0041DA14  movzx    ecx, ax
0041DA17  mov      dl, byte ptr [esi + ecx*4 + 1]
0041DA1B  movzx    ecx, ax
0041DA1E  mov      byte ptr [ebx + ecx*4 + 1], dl
0041DA22  movzx    edx, ax
0041DA25  mov      cl, byte ptr [esi + edx*4]
0041DA28  movzx    edx, ax
0041DA2B  mov      byte ptr [ebx + edx*4 + 2], cl
0041DA2F  movzx    ecx, ax
0041DA32  mov      byte ptr [ebx + ecx*4 + 3], 5
0041DA37  inc      eax
0041DA38  cmp      ax, word ptr [ebp + 0x14]
0041DA3C  jb       0x41da07
0041DA3E  mov      eax, ebx
0041DA40  mov      dx, word ptr [ebp + 0x14]
0041DA44  mov      si, word ptr [ebp + 0x10]
0041DA48  push     eax
0041DA49  movzx    eax, dx
0041DA4C  push     eax
0041DA4D  movzx    edx, si
0041DA50  push     edx
0041DA51  push     dword ptr [edi]
0041DA53  call     0x4397ce
0041DA58  push     ebx
0041DA59  call     0x438f82
0041DA5E  pop      ecx
0041DA5F  cmp      word ptr [ebp + 0x14], 0
0041DA64  seta     al
0041DA67  and      eax, 1
0041DA6A  mov      edx, dword ptr [ebp - 0x2c]
0041DA6D  mov      dword ptr fs:[0], edx
0041DA74  pop      edi
0041DA75  pop      esi
0041DA76  pop      ebx
0041DA77  mov      esp, ebp
0041DA79  pop      ebp
0041DA7A  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885

## DATA Context

**Context around 0x00444878**:

- `",HD"` @ 0x0044484C
- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2

**Context around 0x00444869**:

- `",HD"` @ 0x0044484C
- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5

**Context around 0x00444885**:

- `",HD"` @ 0x0044484C
- `"Dib && palette"` @ 0x00444869
- `"gdiobjec.cpp"` @ 0x00444878
- `"Precondition"` @ 0x00444885
- `"loc >= Lowerbound && ZeroBase(loc) < Data.Limit()"` @ 0x00444892
- `"C:\BC5\INCLUDE\classlib/arrays.h"` @ 0x004448C4
- `"Precondition"` @ 0x004448E5
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x004448F2

## Functions Called

- 0x00403618
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00439162
- 0x00438E50
- 0x004397CE
- 0x00438F82

---

*Extracted with recursive CALL following and DATA context*
