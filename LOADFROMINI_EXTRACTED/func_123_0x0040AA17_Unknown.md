# LoadFromINI Function Analysis

**Function Address**: 0x0040AA17
**Rank**: #123
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 153

```assembly
0040AA17  push     ebp
0040AA18  mov      ebp, esp
0040AA1A  add      esp, 0xfffff004
0040AA20  push     eax
0040AA21  add      esp, -0x3c
0040AA24  push     ebx
0040AA25  push     esi
0040AA26  push     edi
0040AA27  mov      ebx, dword ptr [ebp + 0xc]
0040AA2A  mov      eax, 0x43d8a9
0040AA2F  call     0x403618
0040AA34  mov      esi, 0x43c854
0040AA39  lea      edi, [ebp - 0x103c]
0040AA3F  mov      ecx, 0x400
0040AA44  rep movsd dword ptr es:[edi], dword ptr [esi]
0040AA46  lea      eax, [ebx + 0x14]
0040AA49  push     eax
0040AA4A  mov      edx, dword ptr [ebx + 0x14]
0040AA4D  call     dword ptr [edx + 4]
0040AA50  pop      ecx
0040AA51  test     al, al
0040AA53  je       0x40ab9c
0040AA59  cmp      dword ptr [ebx + 0x10], 0
0040AA5D  setne    cl
0040AA60  and      ecx, 1
0040AA63  test     cl, cl
0040AA65  je       0x40ab9c
0040AA6B  lea      eax, [ebx + 0x24]
0040AA6E  push     eax
0040AA6F  mov      edx, dword ptr [ebx + 0x24]
0040AA72  call     dword ptr [edx + 4]
0040AA75  pop      ecx
0040AA76  test     al, al
0040AA78  je       0x40aaf4
0040AA7A  mov      word ptr [ebp - 0x28], 8
0040AA80  lea      ecx, [ebx + 0x14]
0040AA83  push     ecx
0040AA84  lea      eax, [ebp - 4]
0040AA87  push     eax
0040AA88  call     0x40b6e0
0040AA8D  add      esp, 8
0040AA90  lea      edi, [ebp - 4]
0040AA93  inc      dword ptr [ebp - 0x1c]
0040AA96  mov      eax, dword ptr [edi]
0040AA98  mov      edx, dword ptr [eax + 2]
0040AA9B  push     edx
0040AA9C  lea      ecx, [ebx + 4]
0040AA9F  push     ecx
0040AAA0  lea      eax, [ebp - 8]
0040AAA3  push     eax
0040AAA4  mov      edx, dword ptr [ebx + 4]
0040AAA7  call     dword ptr [edx + 4]
0040AAAA  add      esp, 8
0040AAAD  lea      esi, [ebp - 8]
0040AAB0  inc      dword ptr [ebp - 0x1c]
0040AAB3  mov      eax, dword ptr [esi]
0040AAB5  mov      edx, dword ptr [eax + 2]
0040AAB8  push     edx
0040AAB9  push     0x43f9fe
0040AABE  lea      ecx, [ebp - 0x103c]
0040AAC4  push     ecx
0040AAC5  call     0x438dd8
0040AACA  add      esp, 0x10
0040AACD  dec      dword ptr [ebp - 0x1c]
0040AAD0  push     2
0040AAD2  lea      eax, [ebp - 4]
0040AAD5  push     eax
0040AAD6  call     0x438f64
0040AADB  add      esp, 8
0040AADE  dec      dword ptr [ebp - 0x1c]
0040AAE1  push     2
0040AAE3  lea      edx, [ebp - 8]
0040AAE6  push     edx
0040AAE7  call     0x438f64
0040AAEC  add      esp, 8
0040AAEF  jmp      0x40ab9c
0040AAF4  mov      word ptr [ebp - 0x28], 0x14
0040AAFA  lea      ecx, [ebx + 0x24]
0040AAFD  push     ecx
0040AAFE  lea      eax, [ebp - 0xc]
0040AB01  push     eax
0040AB02  call     0x40b6e0
0040AB07  add      esp, 8
0040AB0A  lea      edx, [ebp - 0xc]
0040AB0D  inc      dword ptr [ebp - 0x1c]
0040AB10  mov      dword ptr [ebp - 0x3c], edx
0040AB13  mov      ecx, dword ptr [ebp - 0x3c]
0040AB16  mov      eax, dword ptr [ecx]
0040AB18  mov      edx, dword ptr [eax + 2]
0040AB1B  push     edx
0040AB1C  lea      ecx, [ebx + 0x14]
0040AB1F  push     ecx
0040AB20  lea      eax, [ebp - 0x10]
0040AB23  push     eax
0040AB24  call     0x40b6e0
0040AB29  add      esp, 8
0040AB2C  lea      edi, [ebp - 0x10]
0040AB2F  inc      dword ptr [ebp - 0x1c]
0040AB32  mov      eax, dword ptr [edi]
0040AB34  mov      edx, dword ptr [eax + 2]
0040AB37  push     edx
0040AB38  lea      ecx, [ebx + 4]
0040AB3B  push     ecx
0040AB3C  lea      eax, [ebp - 0x14]
0040AB3F  push     eax
0040AB40  mov      edx, dword ptr [ebx + 4]
0040AB43  call     dword ptr [edx + 4]
0040AB46  add      esp, 8
0040AB49  lea      esi, [ebp - 0x14]
0040AB4C  inc      dword ptr [ebp - 0x1c]
0040AB4F  mov      eax, dword ptr [esi]
0040AB51  mov      edx, dword ptr [eax + 2]
0040AB54  push     edx
0040AB55  push     0x43fa09
0040AB5A  lea      ecx, [ebp - 0x103c]
0040AB60  push     ecx
0040AB61  call     0x438dd8
0040AB66  add      esp, 0x14
0040AB69  dec      dword ptr [ebp - 0x1c]
0040AB6C  push     2
0040AB6E  lea      eax, [ebp - 0xc]
0040AB71  push     eax
0040AB72  call     0x438f64
0040AB77  add      esp, 8
0040AB7A  dec      dword ptr [ebp - 0x1c]
0040AB7D  push     2
0040AB7F  lea      edx, [ebp - 0x10]
0040AB82  push     edx
0040AB83  call     0x438f64
0040AB88  add      esp, 8
0040AB8B  dec      dword ptr [ebp - 0x1c]
0040AB8E  push     2
0040AB90  lea      ecx, [ebp - 0x14]
0040AB93  push     ecx
0040AB94  call     0x438f64
0040AB99  add      esp, 8
0040AB9C  mov      word ptr [ebp - 0x28], 0x20
0040ABA2  lea      eax, [ebp - 0x103c]
0040ABA8  push     eax
0040ABA9  push     dword ptr [ebp + 8]
0040ABAC  call     0x438e6e
0040ABB1  add      esp, 8
0040ABB4  inc      dword ptr [ebp - 0x1c]
0040ABB7  mov      eax, dword ptr [ebp + 8]
0040ABBA  inc      dword ptr [ebp - 0x1c]
0040ABBD  mov      edx, dword ptr [ebp - 0x38]
0040ABC0  mov      dword ptr fs:[0], edx
0040ABC7  pop      edi
0040ABC8  pop      esi
0040ABC9  pop      ebx
0040ABCA  mov      esp, ebp
0040ABCC  pop      ebp
0040ABCD  ret      
```

## Strings Referenced

**Total unique strings**: 3

- `"%s then %s"` @ 0x0043F9FE
- `"%s then %s else %s"` @ 0x0043FA09
- `"%s %s"` @ 0x0043FA62

## DATA Context

**Context around 0x0043FA09**:

- `"i %i %i %i %s"` @ 0x0043F989
- `"%s "%s" %u %i %i %i %i %s"` @ 0x0043F99A
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

**Context around 0x0043FA62**:

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
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x0043FACA

**Context around 0x0043F9FE**:

- `""%s" %u %i %i %i %i %s"` @ 0x0043F980
- `"%s "%s" %u %i %i %i %i %s"` @ 0x0043F99A
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

## Functions Called

- 0x00403618
- 0x0040B6E0
- 0x00438DD8
- 0x00438F64
- 0x00438F64
- 0x0040B6E0
- 0x0040B6E0
- 0x00438DD8
- 0x00438F64
- 0x00438F64
- 0x00438F64
- 0x00438E6E

---

*Extracted with recursive CALL following and DATA context*
