# LoadFromINI Function Analysis

**Function Address**: 0x004266AE
**Rank**: #163
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 420

```assembly
004266AE  push     ebp
004266AF  mov      ebp, esp
004266B1  mov      eax, dword ptr [ebp + 8]
004266B4  mov      eax, dword ptr [eax + 0x11]
004266B7  pop      ebp
004266B8  ret      
004266B9  or       byte ptr [eax], al
004266BB  add      byte ptr [eax], al
004266BD  add      eax, dword ptr [eax]
004266BF  and      byte ptr [eax], al
004266C1  add      byte ptr [eax], al
004266C3  add      byte ptr [eax], al
004266C5  push     ecx
004266C6  add      byte ptr [eax], al
004266C8  add      byte ptr [eax + eax], ch
004266CB  xor      byte ptr [eax], al
004266CD  add      byte ptr [eax], al
004266CF  add      byte ptr [eax], al
004266D1  add      byte ptr [eax], al
004266D3  add      byte ptr [eax], al
004266D5  add      byte ptr [eax], al
004266D7  add      byte ptr [eax], al
004266D9  push     esp
004266DA  push     esi
004266DB  dec      esi
004266DC  push     esi
004266DD  jb       0x426753
004266E0  imul     ebp, dword ptr [edi + 0x6e], 0
004266E7  add      byte ptr [eax], al
004266E9  add      byte ptr [eax], al
004266EB  add      byte ptr [eax], al
004266ED  add      byte ptr [eax], al
004266EF  add      byte ptr [ebp - 0x75], dl
004266F2  in       al, dx
004266F3  add      esp, -0x3c
004266F6  push     ebx
004266F7  push     esi
004266F8  mov      ebx, dword ptr [ebp + 8]
004266FB  mov      eax, 0x447acc
00426700  call     0x403618
00426705  push     ebx
00426706  call     0x4394f8
0042670B  pop      ecx
0042670C  mov      edx, dword ptr [ebx]
0042670E  cmp      dword ptr [edx + 0x14], 0
00426712  je       0x426894
00426718  mov      ecx, dword ptr [ebx]
0042671A  mov      esi, dword ptr [ecx + 0x14]
0042671D  cmp      dword ptr [esi + 0xc], 0
00426721  jne      0x42679c
00426723  lea      eax, [ebp - 0x34]
00426726  push     eax
00426727  push     0
00426729  push     0
0042672B  push     0
0042672D  push     1
0042672F  push     0x403be0
00426734  push     0
00426736  push     0x6b4
0042673B  push     0x447b28
00426740  push     0x447b1c
00426745  push     0x447b44
0042674A  lea      edx, [ebp - 4]
0042674D  push     edx
0042674E  call     0x438f10
00426753  add      esp, 0x14
00426756  lea      ecx, [ebp - 4]
00426759  push     ecx
0042675A  inc      dword ptr [ebp - 0x18]
0042675D  lea      eax, [ebp - 8]
00426760  push     eax
00426761  call     0x438de4
00426766  add      esp, 8
00426769  inc      dword ptr [ebp - 0x18]
0042676C  mov      word ptr [ebp - 0x24], 0xc
00426772  dec      dword ptr [ebp - 0x18]
00426775  push     2
00426777  lea      edx, [ebp - 4]
0042677A  push     edx
0042677B  call     0x438f64
00426780  add      esp, 8
00426783  add      dword ptr [ebp - 0x18], 2
00426787  add      dword ptr [ebp - 0x18], 3
0042678B  lea      ecx, [ebp - 8]
0042678E  push     ecx
0042678F  push     0x403b88
00426794  call     0x438eaa
00426799  add      esp, 0x24
0042679C  push     dword ptr [esi + 0xc]
0042679F  call     0x4391b6
004267A4  test     eax, eax
004267A6  setne    al
004267A9  and      eax, 1
004267AC  test     al, al
004267AE  jne      0x426894
004267B4  mov      edx, dword ptr [ebx]
004267B6  mov      ecx, dword ptr [edx + 0x14]
004267B9  mov      eax, dword ptr [ecx + 0x28]
004267BC  mov      edx, dword ptr [ebx]
004267BE  sub      eax, dword ptr [edx + 0x28]
004267C1  sar      eax, 1
004267C3  jns      0x4267c8
004267C5  adc      eax, 0
004267C8  mov      ecx, dword ptr [ebx]
004267CA  mov      edx, dword ptr [ecx + 0x14]
004267CD  add      eax, dword ptr [edx + 0x20]
004267D0  mov      dword ptr [ebp - 0x3c], eax
004267D3  mov      eax, dword ptr [ebx]
004267D5  mov      ecx, dword ptr [eax + 0x14]
004267D8  mov      eax, dword ptr [ecx + 0x2c]
004267DB  mov      edx, dword ptr [ebx]
004267DD  sub      eax, dword ptr [edx + 0x2c]
004267E0  sar      eax, 1
004267E2  jns      0x4267e7
004267E4  adc      eax, 0
004267E7  mov      ecx, dword ptr [ebx]
004267E9  mov      edx, dword ptr [ecx + 0x14]
004267EC  add      eax, dword ptr [edx + 0x24]
004267EF  mov      dword ptr [ebp - 0x38], eax
004267F2  mov      eax, dword ptr [ebx]
004267F4  mov      esi, dword ptr [eax + 0x14]
004267F7  cmp      dword ptr [esi + 0xc], 0
004267FB  jne      0x426886
00426801  lea      eax, [ebp - 0x34]
00426804  push     eax
00426805  push     0
00426807  push     0
00426809  push     0
0042680B  push     1
0042680D  push     0x403be0
00426812  push     0
00426814  mov      word ptr [ebp - 0x24], 0x18
0042681A  push     0x5c5
0042681F  push     0x447b5d
00426824  push     0x447b51
00426829  push     0x447b79
0042682E  lea      edx, [ebp - 0xc]
00426831  push     edx
00426832  call     0x438f10
00426837  add      esp, 0x14
0042683A  lea      ecx, [ebp - 0xc]
0042683D  push     ecx
0042683E  inc      dword ptr [ebp - 0x18]
00426841  lea      eax, [ebp - 0x10]
00426844  push     eax
00426845  call     0x438de4
0042684A  add      esp, 8
0042684D  inc      dword ptr [ebp - 0x18]
00426850  mov      word ptr [ebp - 0x24], 0x24
00426856  dec      dword ptr [ebp - 0x18]
00426859  push     2
0042685B  lea      edx, [ebp - 0xc]
0042685E  push     edx
0042685F  call     0x438f64
00426864  add      esp, 8
00426867  mov      word ptr [ebp - 0x24], 0x18
0042686D  add      dword ptr [ebp - 0x18], 2
00426871  add      dword ptr [ebp - 0x18], 3
00426875  lea      ecx, [ebp - 0x10]
00426878  push     ecx
00426879  push     0x403b88
0042687E  call     0x438eaa
00426883  add      esp, 0x24
00426886  lea      eax, [ebp - 0x3c]
00426889  push     eax
0042688A  push     dword ptr [esi + 0xc]
0042688D  call     0x4391bc
00426892  jmp      0x4268cd
00426894  mov      edx, dword ptr [0x455b1c]
0042689A  mov      esi, dword ptr [edx]
0042689C  push     esi
0042689D  call     0x439210
004268A2  mov      ecx, dword ptr [ebx]
004268A4  sub      eax, dword ptr [ecx + 0x28]
004268A7  sar      eax, 1
004268A9  jns      0x4268ae
004268AB  adc      eax, 0
004268AE  mov      dword ptr [ebp - 0x3c], eax
004268B1  mov      eax, dword ptr [0x455b18]
004268B6  mov      esi, dword ptr [eax]
004268B8  push     esi
004268B9  call     0x439210
004268BE  mov      edx, dword ptr [ebx]
004268C0  sub      eax, dword ptr [edx + 0x2c]
004268C3  sar      eax, 1
004268C5  jns      0x4268ca
004268C7  adc      eax, 0
004268CA  mov      dword ptr [ebp - 0x38], eax
004268CD  push     5
004268CF  push     0
004268D1  push     0
004268D3  push     dword ptr [ebp - 0x38]
004268D6  push     dword ptr [ebp - 0x3c]
004268D9  push     0
004268DB  push     dword ptr [ebx]
004268DD  call     0x439450
004268E2  add      esp, 0x1c
004268E5  mov      ecx, dword ptr [ebp - 0x34]
004268E8  mov      dword ptr fs:[0], ecx
004268EF  pop      esi
004268F0  pop      ebx
004268F1  mov      esp, ebp
004268F3  pop      ebp
004268F4  ret      
004268F5  add      byte ptr [eax], al
004268F7  add      byte ptr [ebp - 0x75], dl
004268FA  in       al, dx
004268FB  add      esp, -0x5c
004268FE  push     ebx
004268FF  push     esi
00426900  push     edi
00426901  mov      ebx, dword ptr [ebp + 0xc]
00426904  mov      esi, dword ptr [ebp + 8]
00426907  mov      edi, 0x44ec10
0042690C  mov      eax, 0x447bc4
00426911  call     0x403618
00426916  cmp      byte ptr [ebp + 0x10], 0
0042691A  je       0x426988
0042691C  push     esi
0042691D  mov      edx, dword ptr [esi + 8]
00426920  call     dword ptr [edx + 0x7c]
00426923  pop      ecx
00426924  test     eax, eax
00426926  je       0x426988
00426928  push     esi
00426929  mov      ecx, dword ptr [esi + 8]
0042692C  call     dword ptr [ecx + 0x7c]
0042692F  pop      ecx
00426930  mov      dword ptr [ebp - 0x38], eax
00426933  push     dword ptr [ebp - 0x38]
00426936  lea      eax, [edi + 0x64]
00426939  push     eax
0042693A  call     0x42634d
0042693F  add      esp, 8
00426942  mov      dword ptr [ebp - 0x3c], eax
00426945  cmp      dword ptr [ebp - 0x3c], -1
00426949  jne      0x426952
0042694B  mov      edx, 0x7fffffff
00426950  jmp      0x426958
00426952  mov      edx, dword ptr [ebp - 0x3c]
00426955  add      edx, dword ptr [edi + 0x60]
00426958  add      ebx, edx
0042695A  lea      eax, [edi + 0x64]
0042695D  push     eax
0042695E  mov      ecx, dword ptr [edi + 0x65]
00426961  call     dword ptr [ecx + 4]
00426964  pop      ecx
00426965  cmp      ebx, eax
00426967  jle      0x426976
00426969  lea      eax, [edi + 0x64]
0042696C  push     eax
0042696D  mov      edx, dword ptr [edi + 0x65]
00426970  call     dword ptr [edx + 4]
00426973  pop      ecx
00426974  sub      ebx, eax
00426976  cmp      ebx, 1
00426979  jge      0x426988
0042697B  lea      ecx, [edi + 0x64]
0042697E  push     ecx
0042697F  mov      eax, dword ptr [edi + 0x65]
00426982  call     dword ptr [eax + 4]
00426985  pop      ecx
00426986  add      ebx, eax
00426988  mov      dword ptr [ebp - 0x40], ebx
0042698B  cmp      dword ptr [ebp - 0x40], 1
0042698F  jl       0x4269a1
00426991  lea      edx, [edi + 0x64]
00426994  push     edx
00426995  mov      ecx, dword ptr [edi + 0x65]
00426998  call     dword ptr [ecx + 4]
0042699B  pop      ecx
0042699C  cmp      eax, dword ptr [ebp - 0x40]
0042699F  jge      0x4269a5
004269A1  xor      eax, eax
004269A3  jmp      0x4269aa
004269A5  mov      eax, 1
004269AA  test     al, al
004269AC  je       0x426b44
004269B2  mov      word ptr [ebp - 0x24], 8
004269B8  mov      dword ptr [ebp - 0x44], ebx
004269BB  lea      edx, [edi + 0x24]
004269BE  push     edx
004269BF  lea      ecx, [ebp - 8]
004269C2  push     ecx
004269C3  call     0x438e3e
004269C8  add      esp, 8
004269CB  inc      dword ptr [ebp - 0x18]
004269CE  mov      eax, dword ptr [ebp - 0x44]
004269D1  mov      dword ptr [ebp - 4], eax
004269D4  lea      edx, [ebp - 8]
004269D7  add      dword ptr [ebp - 0x18], 2
004269DB  push     edx
004269DC  lea      ecx, [esi + 0x8e]
004269E2  push     ecx
004269E3  call     0x435f74
004269E8  add      esp, 8
004269EB  sub      dword ptr [ebp - 0x18], 2
004269EF  add      dword ptr [ebp - 0x18], 2
004269F3  dec      dword ptr [ebp - 0x18]
004269F6  push     2
004269F8  lea      eax, [ebp - 8]
004269FB  push     eax
004269FC  call     0x438f64
00426A01  add      esp, 8
00426A04  push     esi
00426A05  call     0x433f55
00426A0A  pop      ecx
00426A0B  mov      dl, byte ptr [ebp + 0x14]
00426A0E  push     edx
00426A0F  mov      dword ptr [ebp - 0x48], ebx
00426A12  mov      ecx, dword ptr [ebp - 0x48]
00426A15  inc      ecx
00426A16  mov      dword ptr [ebp - 0x4c], ecx
00426A19  mov      eax, dword ptr [ebp - 0x4c]
00426A1C  cmp      eax, dword ptr [edi + 0x60]
00426A1F  jge      0x426a40
00426A21  mov      edx, dword ptr [ebp - 0x4c]
00426A24  sub      edx, dword ptr [edi + 0x60]
00426A27  add      edx, dword ptr [edi + 0x6d]
00426A2A  mov      dword ptr [ebp - 0x50], edx
00426A2D  push     0
00426A2F  push     dword ptr [ebp - 0x50]
00426A32  lea      ecx, [edi + 0x64]
00426A35  push     ecx
00426A36  call     0x406954
00426A3B  add      esp, 0xc
00426A3E  jmp      0x426a78
00426A40  mov      eax, dword ptr [edi + 0x6d]
00426A43  mov      dword ptr [ebp - 0x54], eax
00426A46  cmp      dword ptr [ebp - 0x54], -1
00426A4A  jne      0x426a53
00426A4C  mov      edx, 0x7fffffff
00426A51  jmp      0x426a59
00426A53  mov      edx, dword ptr [ebp - 0x54]
00426A56  add      edx, dword ptr [edi + 0x60]
00426A59  cmp      edx, dword ptr [ebp - 0x4c]
00426A5C  jg       0x426a78
00426A5E  mov      eax, dword ptr [ebp - 0x4c]
00426A61  sub      eax, dword ptr [edi + 0x60]
00426A64  mov      dword ptr [ebp - 0x58], eax
00426A67  push     0
00426A69  push     dword ptr [ebp - 0x58]
00426A6C  lea      ecx, [edi + 0x64]
00426A6F  push     ecx
00426A70  call     0x406954
00426A75  add      esp, 0xc
00426A78  mov      eax, dword ptr [ebp - 0x48]
00426A7B  sub      eax, dword ptr [edi + 0x60]
00426A7E  mov      dword ptr [ebp - 0x5c], eax
00426A81  cmp      dword ptr [edi + 0x6d], 0
00426A85  je       0x426b22
00426A8B  cmp      dword ptr [edi + 0x69], 0
00426A8F  je       0x426a9d
00426A91  mov      edx, dword ptr [ebp - 0x5c]
00426A94  cmp      edx, dword ptr [edi + 0x6d]
00426A97  jb       0x426b22
00426A9D  lea      ecx, [ebp - 0x34]
00426AA0  push     ecx
00426AA1  push     0
00426AA3  push     0
00426AA5  push     0
00426AA7  push     1
00426AA9  push     0x403be0
00426AAE  push     0
00426AB0  mov      word ptr [ebp - 0x24], 0x14
00426AB6  push     0x334
00426ABB  push     0x448f2a
00426AC0  push     0x448f05
00426AC5  push     0x448f4c
00426ACA  lea      eax, [ebp - 0xc]
00426ACD  push     eax
00426ACE  call     0x438f10
00426AD3  add      esp, 0x14
00426AD6  lea      edx, [ebp - 0xc]
00426AD9  push     edx
00426ADA  inc      dword ptr [ebp - 0x18]
00426ADD  lea      ecx, [ebp - 0x10]
00426AE0  push     ecx
00426AE1  call     0x438de4
00426AE6  add      esp, 8
00426AE9  inc      dword ptr [ebp - 0x18]
00426AEC  mov      word ptr [ebp - 0x24], 0x20
00426AF2  dec      dword ptr [ebp - 0x18]
00426AF5  push     2
00426AF7  lea      eax, [ebp - 0xc]
00426AFA  push     eax
00426AFB  call     0x438f64
00426B00  add      esp, 8
00426B03  mov      word ptr [ebp - 0x24], 0x14
00426B09  add      dword ptr [ebp - 0x18], 2
00426B0D  add      dword ptr [ebp - 0x18], 3
00426B11  lea      edx, [ebp - 0x10]
00426B14  push     edx
00426B15  push     0x403b88
00426B1A  call     0x438eaa
00426B1F  add      esp, 0x24
00426B22  mov      ecx, dword ptr [ebp - 0x5c]
00426B25  shl      ecx, 2
00426B28  add      ecx, dword ptr [edi + 0x69]
00426B2B  push     dword ptr [ecx]
00426B2D  push     esi
00426B2E  call     0x434070
00426B33  add      esp, 0xc
00426B36  mov      al, 1
00426B38  mov      edx, dword ptr [ebp - 0x34]
00426B3B  mov      dword ptr fs:[0], edx
00426B42  jmp      0x426b5b
00426B44  push     ebx
00426B45  push     0x68
00426B47  call     0x404f9c
00426B4C  add      esp, 8
00426B4F  xor      eax, eax
00426B51  mov      edx, dword ptr [ebp - 0x34]
00426B54  mov      dword ptr fs:[0], edx
00426B5B  pop      edi
00426B5C  pop      esi
00426B5D  pop      ebx
00426B5E  mov      esp, ebp
00426B60  pop      ebp
00426B61  ret      
```

## Strings Referenced

**Total unique strings**: 9

- `"GetHandle()"` @ 0x00447B1C
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B28
- `"Precondition"` @ 0x00447B44
- `"GetHandle()"` @ 0x00447B51
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B5D
- `"Precondition"` @ 0x00447B79
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C

## DATA Context

**Context around 0x00447B44**:

- `"tzD"` @ 0x00447ADC
- `"GetHandle()"` @ 0x00447B1C
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B28
- `"Precondition"` @ 0x00447B44
- `"GetHandle()"` @ 0x00447B51
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B5D
- `"Precondition"` @ 0x00447B79
- `"%<@"` @ 0x00447B98
- `"i<@"` @ 0x00447BB4

**Context around 0x00448F05**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E

**Context around 0x00447B28**:

- `"i<@"` @ 0x00447ABC
- `"tzD"` @ 0x00447ADC
- `"GetHandle()"` @ 0x00447B1C
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B28
- `"Precondition"` @ 0x00447B44
- `"GetHandle()"` @ 0x00447B51
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B5D
- `"Precondition"` @ 0x00447B79
- `"%<@"` @ 0x00447B98

**Context around 0x00448F2A**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E
- `"Precondition"` @ 0x00448FA0

**Context around 0x00448F4C**:

- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F05
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F2A
- `"Precondition"` @ 0x00448F4C
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x00448F59
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x00448F7E
- `"Precondition"` @ 0x00448FA0
- `"GetHandle()"` @ 0x00448FAD
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00448FB9

**Context around 0x00447B51**:

- `"tzD"` @ 0x00447ADC
- `"GetHandle()"` @ 0x00447B1C
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B28
- `"Precondition"` @ 0x00447B44
- `"GetHandle()"` @ 0x00447B51
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B5D
- `"Precondition"` @ 0x00447B79
- `"%<@"` @ 0x00447B98
- `"i<@"` @ 0x00447BB4

**Context around 0x00447B79**:

- `"GetHandle()"` @ 0x00447B1C
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B28
- `"Precondition"` @ 0x00447B44
- `"GetHandle()"` @ 0x00447B51
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B5D
- `"Precondition"` @ 0x00447B79
- `"%<@"` @ 0x00447B98
- `"i<@"` @ 0x00447BB4
- `"%<@"` @ 0x00447BF0

**Context around 0x00447B1C**:

- `"%<@"` @ 0x00447AA0
- `"i<@"` @ 0x00447ABC
- `"tzD"` @ 0x00447ADC
- `"GetHandle()"` @ 0x00447B1C
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B28
- `"Precondition"` @ 0x00447B44
- `"GetHandle()"` @ 0x00447B51
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B5D
- `"Precondition"` @ 0x00447B79
- `"%<@"` @ 0x00447B98

**Context around 0x00447B5D**:

- `"GetHandle()"` @ 0x00447B1C
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B28
- `"Precondition"` @ 0x00447B44
- `"GetHandle()"` @ 0x00447B51
- `"C:\BC5\INCLUDE\owl/window.h"` @ 0x00447B5D
- `"Precondition"` @ 0x00447B79
- `"%<@"` @ 0x00447B98
- `"i<@"` @ 0x00447BB4

## Functions Called

- 0x00403618
- 0x004394F8
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x004391B6
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x004391BC
- 0x00439210
- 0x00439210
- 0x00439450
- 0x00403618
- 0x0042634D
- 0x00438E3E
- 0x00435F74
- 0x00438F64
- 0x00433F55
- 0x00406954
- 0x00406954
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00434070
- 0x00404F9C

---

*Extracted with recursive CALL following and DATA context*
