# TVNImageObject_1 - Complete Assembly Extraction

**Vtable Address**: 0x00429980
**Binary**: europeo.exe
**Tool**: Capstone Disassembler
**Date**: 2026-01-16

---

## Methods Summary

| Index | Address |
|-------|----------|
|  0 | 0x0042A738 |
|  1 | 0x00440001 |

---

## Method [0]: 0x0042A738

**Address**: 0x0042A738
**Index in vtable**: 0

**Size**: ~1758 bytes

### Assembly Code

```assembly
0042a738  51                        push     ecx
0042a739  8b 41 08                  mov      eax, dword ptr [ecx + 8]
0042a73c  ff 50 5c                  call     dword ptr [eax + 0x5c]
0042a73f  83 c4 08                  add      esp, 8
0042a742  8b 53 41                  mov      edx, dword ptr [ebx + 0x41]
0042a745  f6 02 10                  test     byte ptr [edx], 0x10
0042a748  0f 95 c1                  setne    cl
0042a74b  83 e1 01                  and      ecx, 1
0042a74e  51                        push     ecx
0042a74f  8b 43 2d                  mov      eax, dword ptr [ebx + 0x2d]
0042a752  8b 10                     mov      edx, dword ptr [eax]
0042a754  52                        push     edx
0042a755  8b 4a 08                  mov      ecx, dword ptr [edx + 8]
0042a758  ff 51 5c                  call     dword ptr [ecx + 0x5c]
0042a75b  83 c4 08                  add      esp, 8
0042a75e  8b 43 41                  mov      eax, dword ptr [ebx + 0x41]
0042a761  f6 00 20                  test     byte ptr [eax], 0x20
0042a764  0f 95 c2                  setne    dl
0042a767  83 e2 01                  and      edx, 1
0042a76a  52                        push     edx
0042a76b  8b 4b 31                  mov      ecx, dword ptr [ebx + 0x31]
0042a76e  8b 01                     mov      eax, dword ptr [ecx]
0042a770  50                        push     eax
0042a771  8b 50 08                  mov      edx, dword ptr [eax + 8]
0042a774  ff 52 5c                  call     dword ptr [edx + 0x5c]
0042a777  83 c4 08                  add      esp, 8
0042a77a  8b 4b 41                  mov      ecx, dword ptr [ebx + 0x41]
0042a77d  f6 01 40                  test     byte ptr [ecx], 0x40
0042a780  0f 95 c0                  setne    al
0042a783  83 e0 01                  and      eax, 1
0042a786  50                        push     eax
0042a787  8b 53 35                  mov      edx, dword ptr [ebx + 0x35]
0042a78a  8b 0a                     mov      ecx, dword ptr [edx]
0042a78c  51                        push     ecx
0042a78d  8b 41 08                  mov      eax, dword ptr [ecx + 8]
0042a790  ff 50 5c                  call     dword ptr [eax + 0x5c]
0042a793  83 c4 08                  add      esp, 8
0042a796  8b 53 41                  mov      edx, dword ptr [ebx + 0x41]
0042a799  f6 02 80                  test     byte ptr [edx], 0x80
0042a79c  0f 95 c1                  setne    cl
0042a79f  83 e1 01                  and      ecx, 1
0042a7a2  51                        push     ecx
0042a7a3  8b 43 39                  mov      eax, dword ptr [ebx + 0x39]
0042a7a6  8b 10                     mov      edx, dword ptr [eax]
0042a7a8  52                        push     edx
0042a7a9  8b 4a 08                  mov      ecx, dword ptr [edx + 8]
0042a7ac  ff 51 5c                  call     dword ptr [ecx + 0x5c]
0042a7af  83 c4 08                  add      esp, 8
0042a7b2  8b 43 41                  mov      eax, dword ptr [ebx + 0x41]
0042a7b5  f6 40 01 01               test     byte ptr [eax + 1], 1
0042a7b9  0f 95 c2                  setne    dl
0042a7bc  83 e2 01                  and      edx, 1
0042a7bf  52                        push     edx
0042a7c0  8b 4b 3d                  mov      ecx, dword ptr [ebx + 0x3d]
0042a7c3  8b 01                     mov      eax, dword ptr [ecx]
0042a7c5  50                        push     eax
0042a7c6  8b 50 08                  mov      edx, dword ptr [eax + 8]
0042a7c9  ff 52 5c                  call     dword ptr [edx + 0x5c]
0042a7cc  83 c4 08                  add      esp, 8
0042a7cf  eb 0e                     jmp      0x42a7df
0042a7d1  85 f6                     test     esi, esi
0042a7d3  75 0a                     jne      0x42a7df
0042a7d5  8b 53 41                  mov      edx, dword ptr [ebx + 0x41]
0042a7d8  8b 43 19                  mov      eax, dword ptr [ebx + 0x19]
0042a7db  8b 0a                     mov      ecx, dword ptr [edx]
0042a7dd  21 08                     and      dword ptr [eax], ecx
0042a7df  5e                        pop      esi
0042a7e0  5b                        pop      ebx
0042a7e1  5d                        pop      ebp
0042a7e2  c3                        ret      
0042a7e3  04 00                     add      al, 0
0042a7e5  00 00                     add      byte ptr [eax], al
0042a7e7  90                        nop      
0042a7e8  00 0c 00                  add      byte ptr [eax + eax], cl
0042a7eb  01 b2 42 00 54 56         add      dword ptr [edx + 0x56540042], esi
0042a7f1  4e                        dec      esi
0042a7f2  55                        push     ebp
0042a7f3  73 65                     jae      0x42a85a
0042a7f5  72 50                     jb       0x42a847
0042a7f7  72 65                     jb       0x42a85e
0042a7f9  66 73 44                  jae      0x42a840
0042a7fc  6c                        insb     byte ptr es:[edi], dx
0042a7fd  67 20 2a                  and      byte ptr [bp + si], ch
0042a800  00 db                     add      bl, bl
0042a802  00 00                     add      byte ptr [eax], al
0042a804  00 03                     add      byte ptr [ebx], al
0042a806  00 30                     add      byte ptr [eax], dh
0042a808  00 0c 00                  add      byte ptr [eax + eax], cl
0042a80b  00 00                     add      byte ptr [eax], al
0042a80d  7f 00                     jg       0x42a80f
0042a80f  00 00                     add      byte ptr [eax], al
0042a811  40                        inc      eax
0042a812  00 50 00                  add      byte ptr [eax], dl
0042a815  00 00                     add      byte ptr [eax], al
0042a817  00 00                     add      byte ptr [eax], al
0042a819  00 00                     add      byte ptr [eax], al
0042a81b  00 00                     add      byte ptr [eax], al
0042a81d  00 00                     add      byte ptr [eax], al
0042a81f  00 00                     add      byte ptr [eax], al
0042a821  05 00 00 00 03            add      eax, 0x3000000
0042a826  00 00                     add      byte ptr [eax], al
0042a828  00 80 af 42 00 01         add      byte ptr [eax + 0x10042af], al
0042a82e  00 78 00                  add      byte ptr [eax], bh
0042a831  54                        push     esp
0042a832  56                        push     esi
0042a833  4e                        dec      esi
0042a834  55                        push     ebp
0042a835  73 65                     jae      0x42a89c
0042a837  72 50                     jb       0x42a889
0042a839  72 65                     jb       0x42a8a0
0042a83b  66 73 44                  jae      0x42a882
0042a83e  6c                        insb     byte ptr es:[edi], dx
0042a83f  67 00 91 b3 42            add      byte ptr [bx + di + 0x42b3], dl
0042a844  00 00                     add      byte ptr [eax], al
0042a846  00 00                     add      byte ptr [eax], al
0042a848  00 03                     add      byte ptr [ebx], al
0042a84a  00 00                     add      byte ptr [eax], al
0042a84c  00 00                     add      byte ptr [eax], al
0042a84e  00 00                     add      byte ptr [eax], al
0042a850  00 ec                     add      ah, ch
0042a852  c9                        leave    
0042a853  41                        inc      ecx
0042a854  00 04 00                  add      byte ptr [eax + eax], al
0042a857  00 00                     add      byte ptr [eax], al
0042a859  0d 00 00 00 a0            or       eax, 0xa0000000
0042a85e  c9                        leave    
0042a85f  41                        inc      ecx
0042a860  00 08                     add      byte ptr [eax], cl
0042a862  00 00                     add      byte ptr [eax], al
0042a864  00 0d 00 00 00 73         add      byte ptr [0x73000000], cl
0042a86a  ca 41 00                  retf     0x41
0042a86d  00 00                     add      byte ptr [eax], al
0042a86f  00 00                     add      byte ptr [eax], al
0042a871  0d 00 00 00 00            or       eax, 0
0042a876  00 00                     add      byte ptr [eax], al
0042a878  00 00                     add      byte ptr [eax], al
0042a87a  00 00                     add      byte ptr [eax], al
0042a87c  00 8b 44 24 04 03         add      byte ptr [ebx + 0x3042444], cl
0042a882  40                        inc      eax
0042a883  fc                        cld      
0042a884  83 c0 ab                  add      eax, -0x55
0042a887  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a88b  e9 da e2 00 00            jmp      0x438b6a
0042a890  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a894  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a897  83 c0 ab                  add      eax, -0x55
0042a89a  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a89e  e9 55 e2 00 00            jmp      0x438af8
0042a8a3  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a8a7  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a8aa  83 c0 ab                  add      eax, -0x55
0042a8ad  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a8b1  e9 96 e2 00 00            jmp      0x438b4c
0042a8b6  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a8ba  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a8bd  83 c0 ab                  add      eax, -0x55
0042a8c0  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a8c4  e9 71 e2 00 00            jmp      0x438b3a
0042a8c9  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a8cd  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a8d0  83 c0 ab                  add      eax, -0x55
0042a8d3  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a8d7  e9 99 fd ff ff            jmp      0x42a675
0042a8dc  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a8e0  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a8e3  83 c0 ab                  add      eax, -0x55
0042a8e6  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a8ea  e9 33 e2 00 00            jmp      0x438b22
0042a8ef  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a8f3  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a8f6  83 c0 ab                  add      eax, -0x55
0042a8f9  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a8fd  e9 0e e2 00 00            jmp      0x438b10
0042a902  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a906  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a909  83 c0 ab                  add      eax, -0x55
0042a90c  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a910  e9 09 e3 00 00            jmp      0x438c1e
0042a915  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a919  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a91c  83 c0 ab                  add      eax, -0x55
0042a91f  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a923  e9 7e e2 00 00            jmp      0x438ba6
0042a928  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a92c  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a92f  83 c0 ab                  add      eax, -0x55
0042a932  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a936  e9 41 e2 00 00            jmp      0x438b7c
0042a93b  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a93f  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a942  83 c0 ab                  add      eax, -0x55
0042a945  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a949  e9 9a e2 00 00            jmp      0x438be8
0042a94e  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a952  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a955  83 c0 ab                  add      eax, -0x55
0042a958  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a95c  e9 a5 e2 00 00            jmp      0x438c06
0042a961  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a965  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a968  83 c0 ab                  add      eax, -0x55
0042a96b  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a96f  e9 0c fc ff ff            jmp      0x42a580
0042a974  83 44 24 04 b3            add      dword ptr [esp + 4], -0x4d
0042a979  e9 02 fc ff ff            jmp      0x42a580
0042a97e  8b 44 24 04               mov      eax, dword ptr [esp + 4]
0042a982  03 40 fc                  add      eax, dword ptr [eax - 4]
0042a985  83 c0 b7                  add      eax, -0x49
0042a988  89 44 24 04               mov      dword ptr [esp + 4], eax
0042a98c  e9 d9 e1 00 00            jmp      0x438b6a
0042a991  d7                        xlatb    
0042a992  00 00                     add      byte ptr [eax], al
0042a994  00 03                     add      byte ptr [ebx], al
0042a996  00 30                     add      byte ptr [eax], dh
0042a998  00 0c 00                  add      byte ptr [eax + eax], cl
0042a99b  00 00                     add      byte ptr [eax], al
0042a99d  7f 00                     jg       0x42a99f
0042a99f  00 00                     add      byte ptr [eax], al
0042a9a1  40                        inc      eax
0042a9a2  00 50 00                  add      byte ptr [eax], dl
0042a9a5  00 00                     add      byte ptr [eax], al
0042a9a7  00 00                     add      byte ptr [eax], al
0042a9a9  00 00                     add      byte ptr [eax], al
0042a9ab  00 00                     add      byte ptr [eax], al
0042a9ad  00 00                     add      byte ptr [eax], al
0042a9af  00 00                     add      byte ptr [eax], al
0042a9b1  04 00                     add      al, 0
0042a9b3  00 00                     add      byte ptr [eax], al
0042a9b5  02 00                     add      al, byte ptr [eax]
0042a9b7  00 00                     add      byte ptr [eax], al
0042a9b9  16                        push     ss
0042a9ba  b8 42 00 01 00            mov      eax, 0x10042
0042a9bf  78 00                     js       0x42a9c1
0042a9c1  54                        push     esp
0042a9c2  56                        push     esi
0042a9c3  4e                        dec      esi
0042a9c4  50                        push     eax
0042a9c5  72 6a                     jb       0x42aa31
0042a9c7  43                        inc      ebx
0042a9c8  61                        popal    
0042a9c9  70 73                     jo       0x42aa3e
0042a9cb  44                        inc      esp
0042a9cc  6c                        insb     byte ptr es:[edi], dx
0042a9cd  67 00 00                  add      byte ptr [bx + si], al
0042a9d0  00 0d b4 42 00 00         add      byte ptr [0x42b4], cl
0042a9d6  00 00                     add      byte ptr [eax], al
0042a9d8  00 03                     add      byte ptr [ebx], al
0042a9da  00 00                     add      byte ptr [eax], al
0042a9dc  00 00                     add      byte ptr [eax], al
0042a9de  00 00                     add      byte ptr [eax], al
0042a9e0  00 ec                     add      ah, ch
0042a9e2  c9                        leave    
0042a9e3  41                        inc      ecx
0042a9e4  00 04 00                  add      byte ptr [eax + eax], al
0042a9e7  00 00                     add      byte ptr [eax], al
0042a9e9  0d 00 00 00 a0            or       eax, 0xa0000000
0042a9ee  c9                        leave    
0042a9ef  41                        inc      ecx
0042a9f0  00 08                     add      byte ptr [eax], cl
0042a9f2  00 00                     add      byte ptr [eax], al
0042a9f4  00 0d 00 00 00 73         add      byte ptr [0x73000000], cl
0042a9fa  ca 41 00                  retf     0x41
0042a9fd  00 00                     add      byte ptr [eax], al
0042a9ff  00 00                     add      byte ptr [eax], al
0042aa01  0d 00 00 00 00            or       eax, 0
0042aa06  00 00                     add      byte ptr [eax], al
0042aa08  00 00                     add      byte ptr [eax], al
0042aa0a  00 00                     add      byte ptr [eax], al
0042aa0c  00 af 00 00 00 03         add      byte ptr [edi + 0x3000000], ch
0042aa12  00 30                     add      byte ptr [eax], dh
0042aa14  00 0c 00                  add      byte ptr [eax + eax], cl
0042aa17  00 00                     add      byte ptr [eax], al
0042aa19  7f 00                     jg       0x42aa1b
0042aa1b  00 00                     add      byte ptr [eax], al
0042aa1d  38 00                     cmp      byte ptr [eax], al
0042aa1f  3c 00                     cmp      al, 0
0042aa21  00 00                     add      byte ptr [eax], al
0042aa23  00 00                     add      byte ptr [eax], al
0042aa25  00 00                     add      byte ptr [eax], al
0042aa27  00 00                     add      byte ptr [eax], al
0042aa29  00 00                     add      byte ptr [eax], al
0042aa2b  00 00                     add      byte ptr [eax], al
0042aa2d  03 00                     add      eax, dword ptr [eax]
0042aa2f  00 00                     add      byte ptr [eax], al
0042aa31  01 00                     add      dword ptr [eax], eax
0042aa33  00 00                     add      byte ptr [eax], al
0042aa35  30 96 43 00 01 00         xor      byte ptr [esi + 0x10043], dl
0042aa3b  64 00 54 44 69            add      byte ptr fs:[esp + eax*2 + 0x69], dl
0042aa40  61                        popal    
0042aa41  6c                        insb     byte ptr es:[edi], dx
0042aa42  6f                        outsd    dx, dword ptr [esi]
0042aa43  67 00 00                  add      byte ptr [bx + si], al
0042aa46  00 00                     add      byte ptr [eax], al
0042aa48  00 ec                     add      ah, ch
0042aa4a  c9                        leave    
0042aa4b  41                        inc      ecx
0042aa4c  00 04 00                  add      byte ptr [eax + eax], al
0042aa4f  00 00                     add      byte ptr [eax], al
0042aa51  0e                        push     cs
0042aa52  00 00                     add      byte ptr [eax], al
0042aa54  00 a0 c9 41 00 08         add      byte ptr [eax + 0x80041c9], ah
0042aa5a  00 00                     add      byte ptr [eax], al
0042aa5c  00 0e                     add      byte ptr [esi], cl
0042aa5e  00 00                     add      byte ptr [eax], al
0042aa60  00 73 ca                  add      byte ptr [ebx - 0x36], dh
0042aa63  41                        inc      ecx
0042aa64  00 00                     add      byte ptr [eax], al
0042aa66  00 00                     add      byte ptr [eax], al
0042aa68  00 07                     add      byte ptr [edi], al
0042aa6a  00 00                     add      byte ptr [eax], al
0042aa6c  00 00                     add      byte ptr [eax], al
0042aa6e  00 00                     add      byte ptr [eax], al
0042aa70  00 00                     add      byte ptr [eax], al
0042aa72  00 00                     add      byte ptr [eax], al
0042aa74  00 00                     add      byte ptr [eax], al
0042aa76  00 00                     add      byte ptr [eax], al
0042aa78  55                        push     ebp
0042aa79  8b ec                     mov      ebp, esp
0042aa7b  83 c4 b8                  add      esp, -0x48
0042aa7e  53                        push     ebx
0042aa7f  56                        push     esi
0042aa80  8d 5d 08                  lea      ebx, [ebp + 8]
0042aa83  8d 75 b8                  lea      esi, [ebp - 0x48]
0042aa86  b8 90 97 44 00            mov      eax, 0x449790
0042aa8b  e8 88 81 fd ff            call     0x402c18
0042aa90  66 c7 46 10 08 00         mov      word ptr [esi + 0x10], 8
0042aa96  83 7d 0c 00               cmp      dword ptr [ebp + 0xc], 0
0042aa9a  0f 85 86 00 00 00         jne      0x42ab26
0042aaa0  8b 13                     mov      edx, dword ptr [ebx]
0042aaa2  83 c2 51                  add      edx, 0x51
0042aaa5  8b 0b                     mov      ecx, dword ptr [ebx]
0042aaa7  89 11                     mov      dword ptr [ecx], edx
0042aaa9  8b 03                     mov      eax, dword ptr [ebx]
0042aaab  83 c0 45                  add      eax, 0x45
0042aaae  8b 13                     mov      edx, dword ptr [ebx]
0042aab0  89 42 51                  mov      dword ptr [edx + 0x51], eax
0042aab3  8b 0b                     mov      ecx, dword ptr [ebx]
0042aab5  83 c1 49                  add      ecx, 0x49
0042aab8  8b 03                     mov      eax, dword ptr [ebx]
0042aaba  89 48 55                  mov      dword ptr [eax + 0x55], ecx
0042aabd  8b 13                     mov      edx, dword ptr [ebx]
0042aabf  83 c2 45                  add      edx, 0x45
0042aac2  8b 0b                     mov      ecx, dword ptr [ebx]
0042aac4  89 51 04                  mov      dword ptr [ecx + 4], edx
0042aac7  8b 03                     mov      eax, dword ptr [ebx]
0042aac9  83 c0 49                  add      eax, 0x49
0042aacc  8b 13                     mov      edx, dword ptr [ebx]
0042aace  89 42 08                  mov      dword ptr [edx + 8], eax
0042aad1  8b 0b                     mov      ecx, dword ptr [ebx]
0042aad3  33 c0                     xor      eax, eax
0042aad5  89 41 41                  mov      dword ptr [ecx + 0x41], eax
0042aad8  8b 13                     mov      edx, dword ptr [ebx]
0042aada  33 c9                     xor      ecx, ecx
0042aadc  89 4a 4d                  mov      dword ptr [edx + 0x4d], ecx
0042aadf  8b 03                     mov      eax, dword ptr [ebx]
0042aae1  83 c0 45                  add      eax, 0x45
0042aae4  c7 00 30 40 44 00         mov      dword ptr [eax], 0x444030
0042aaea  8b 03                     mov      eax, dword ptr [ebx]
0042aaec  83 c0 49                  add      eax, 0x49
0042aaef  c7 00 20 40 44 00         mov      dword ptr [eax], 0x444020
0042aaf5  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0042aaf8  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0042aafb  8b 13                     mov      edx, dword ptr [ebx]
0042aafd  8b 4a 04                  mov      ecx, dword ptr [edx + 4]
0042ab00  81 69 fc 6a ff ff ff      sub      dword ptr [ecx - 4], 0xffffff6a
0042ab07  6a 01                     push     1
0042ab09  8b 03                     mov      eax, dword ptr [ebx]
0042ab0b  83 c0 51                  add      eax, 0x51
0042ab0e  50                        push     eax
0042ab0f  e8 04 e1 00 00            call     0x438c18
0042ab14  83 c4 08                  add      esp, 8
0042ab17  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0042ab1a  8b 13                     mov      edx, dword ptr [ebx]
0042ab1c  8b 4a 04                  mov      ecx, dword ptr [edx + 4]
0042ab1f  81 41 fc 6a ff ff ff      add      dword ptr [ecx - 4], 0xffffff6a
0042ab26  8b 03                     mov      eax, dword ptr [ebx]
0042ab28  8b 50 04                  mov      edx, dword ptr [eax + 4]
0042ab2b  83 6a fc 28               sub      dword ptr [edx - 4], 0x28
0042ab2f  8b 0b                     mov      ecx, dword ptr [ebx]
0042ab31  8b 01                     mov      eax, dword ptr [ecx]
0042ab33  83 68 fc 28               sub      dword ptr [eax - 4], 0x28
0042ab37  ff 75 1c                  push     dword ptr [ebp + 0x1c]
0042ab3a  83 c4 fc                  add      esp, -4
0042ab3d  8b 55 18                  mov      edx, dword ptr [ebp + 0x18]
0042ab40  89 14 24                  mov      dword ptr [esp], edx
0042ab43  ff 75 10                  push     dword ptr [ebp + 0x10]
0042ab46  6a 01                     push     1
0042ab48  ff 33                     push     dword ptr [ebx]
0042ab4a  e8 f9 e0 00 00            call     0x438c48
0042ab4f  83 c4 14                  add      esp, 0x14
0042ab52  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0042ab55  8b 0b                     mov      ecx, dword ptr [ebx]
0042ab57  8b 41 04                  mov      eax, dword ptr [ecx + 4]
0042ab5a  83 40 fc 28               add      dword ptr [eax - 4], 0x28
0042ab5e  8b 13                     mov      edx, dword ptr [ebx]
0042ab60  8b 0a                     mov      ecx, dword ptr [edx]
0042ab62  83 41 fc 28               add      dword ptr [ecx - 4], 0x28
0042ab66  8b 03                     mov      eax, dword ptr [ebx]
0042ab68  c7 40 0c a4 9d 44 00      mov      dword ptr [eax + 0xc], 0x449da4
0042ab6f  8b 13                     mov      edx, dword ptr [ebx]
0042ab71  8b 4a 04                  mov      ecx, dword ptr [edx + 4]
0042ab74  c7 01 ec 9d 44 00         mov      dword ptr [ecx], 0x449dec
0042ab7a  8b 03                     mov      eax, dword ptr [ebx]
0042ab7c  8b 50 08                  mov      edx, dword ptr [eax + 8]
0042ab7f  c7 02 f8 9d 44 00         mov      dword ptr [edx], 0x449df8
0042ab85  8b 0b                     mov      ecx, dword ptr [ebx]
0042ab87  8b 01                     mov      eax, dword ptr [ecx]
0042ab89  c7 40 08 04 9e 44 00      mov      dword ptr [eax + 8], 0x449e04
0042ab90  8b 13                     mov      edx, dword ptr [ebx]
0042ab92  8b 4d 14                  mov      ecx, dword ptr [ebp + 0x14]
0042ab95  89 4a 19                  mov      dword ptr [edx + 0x19], ecx
0042ab98  68 b0 00 00 00            push     0xb0
0042ab9d  e8 4a d9 00 00            call     0x4384ec
0042aba2  59                        pop      ecx
0042aba3  89 45 fc                  mov      dword ptr [ebp - 4], eax
0042aba6  85 c0                     test     eax, eax
0042aba8  74 2b                     je       0x42abd5
0042abaa  66 c7 46 10 20 00         mov      word ptr [esi + 0x10], 0x20
0042abb0  6a 00                     push     0
0042abb2  6a 00                     push     0
0042abb4  68 e9 03 00 00            push     0x3e9
0042abb9  8b 13                     mov      edx, dword ptr [ebx]
0042abbb  ff 32                     push     dword ptr [edx]
0042abbd  6a 00                     push     0
0042abbf  ff 75 fc                  push     dword ptr [ebp - 4]
0042abc2  e8 e5 df 00 00            call     0x438bac
0042abc7  83 c4 18                  add      esp, 0x18
0042abca  66 c7 46 10 14 00         mov      word ptr [esi + 0x10], 0x14
0042abd0  8b 4d fc                  mov      ecx, dword ptr [ebp - 4]
0042abd3  eb 03                     jmp      0x42abd8
0042abd5  8b 4d fc                  mov      ecx, dword ptr [ebp - 4]
0042abd8  8b 03                     mov      eax, dword ptr [ebx]
0042abda  89 48 1d                  mov      dword ptr [eax + 0x1d], ecx
0042abdd  68 b0 00 00 00            push     0xb0
0042abe2  e8 05 d9 00 00            call     0x4384ec
0042abe7  59                        pop      ecx
0042abe8  89 45 f8                  mov      dword ptr [ebp - 8], eax
0042abeb  85 c0                     test     eax, eax
0042abed  74 2b                     je       0x42ac1a
0042abef  66 c7 46 10 38 00         mov      word ptr [esi + 0x10], 0x38
0042abf5  6a 00                     push     0
0042abf7  6a 00                     push     0
0042abf9  68 ea 03 00 00            push     0x3ea
0042abfe  8b 13                     mov      edx, dword ptr [ebx]
0042ac00  ff 32                     push     dword ptr [edx]
0042ac02  6a 00                     push     0
0042ac04  ff 75 f8                  push     dword ptr [ebp - 8]
0042ac07  e8 a0 df 00 00            call     0x438bac
0042ac0c  83 c4 18                  add      esp, 0x18
0042ac0f  66 c7 46 10 2c 00         mov      word ptr [esi + 0x10], 0x2c
0042ac15  8b 4d f8                  mov      ecx, dword ptr [ebp - 8]
0042ac18  eb 03                     jmp      0x42ac1d
0042ac1a  8b 4d f8                  mov      ecx, dword ptr [ebp - 8]
0042ac1d  8b 03                     mov      eax, dword ptr [ebx]
0042ac1f  89 48 21                  mov      dword ptr [eax + 0x21], ecx
0042ac22  68 b0 00 00 00            push     0xb0
0042ac27  e8 c0 d8 00 00            call     0x4384ec
0042ac2c  59                        pop      ecx
0042ac2d  89 45 f4                  mov      dword ptr [ebp - 0xc], eax
0042ac30  85 c0                     test     eax, eax
0042ac32  74 2b                     je       0x42ac5f
0042ac34  66 c7 46 10 50 00         mov      word ptr [esi + 0x10], 0x50
0042ac3a  6a 00                     push     0
0042ac3c  6a 00                     push     0
0042ac3e  68 eb 03 00 00            push     0x3eb
0042ac43  8b 13                     mov      edx, dword ptr [ebx]
0042ac45  ff 32                     push     dword ptr [edx]
0042ac47  6a 00                     push     0
0042ac49  ff 75 f4                  push     dword ptr [ebp - 0xc]
0042ac4c  e8 5b df 00 00            call     0x438bac
0042ac51  83 c4 18                  add      esp, 0x18
0042ac54  66 c7 46 10 44 00         mov      word ptr [esi + 0x10], 0x44
0042ac5a  8b 4d f4                  mov      ecx, dword ptr [ebp - 0xc]
0042ac5d  eb 03                     jmp      0x42ac62
0042ac5f  8b 4d f4                  mov      ecx, dword ptr [ebp - 0xc]
0042ac62  8b 03                     mov      eax, dword ptr [ebx]
0042ac64  89 48 25                  mov      dword ptr [eax + 0x25], ecx
0042ac67  68 b0 00 00 00            push     0xb0
0042ac6c  e8 7b d8 00 00            call     0x4384ec
0042ac71  59                        pop      ecx
0042ac72  89 45 f0                  mov      dword ptr [ebp - 0x10], eax
0042ac75  85 c0                     test     eax, eax
0042ac77  74 2b                     je       0x42aca4
0042ac79  66 c7 46 10 68 00         mov      word ptr [esi + 0x10], 0x68
0042ac7f  6a 00                     push     0
0042ac81  6a 00                     push     0
0042ac83  68 ec 03 00 00            push     0x3ec
0042ac88  8b 13                     mov      edx, dword ptr [ebx]
0042ac8a  ff 32                     push     dword ptr [edx]
0042ac8c  6a 00                     push     0
0042ac8e  ff 75 f0                  push     dword ptr [ebp - 0x10]
0042ac91  e8 16 df 00 00            call     0x438bac
0042ac96  83 c4 18                  add      esp, 0x18
0042ac99  66 c7 46 10 5c 00         mov      word ptr [esi + 0x10], 0x5c
0042ac9f  8b 4d f0                  mov      ecx, dword ptr [ebp - 0x10]
0042aca2  eb 03                     jmp      0x42aca7
0042aca4  8b 4d f0                  mov      ecx, dword ptr [ebp - 0x10]
0042aca7  8b 03                     mov      eax, dword ptr [ebx]
0042aca9  89 48 29                  mov      dword ptr [eax + 0x29], ecx
0042acac  68 b0 00 00 00            push     0xb0
0042acb1  e8 36 d8 00 00            call     0x4384ec
0042acb6  59                        pop      ecx
0042acb7  89 45 ec                  mov      dword ptr [ebp - 0x14], eax
0042acba  85 c0                     test     eax, eax
0042acbc  74 2b                     je       0x42ace9
0042acbe  66 c7 46 10 80 00         mov      word ptr [esi + 0x10], 0x80
0042acc4  6a 00                     push     0
0042acc6  6a 00                     push     0
0042acc8  68 ed 03 00 00            push     0x3ed
0042accd  8b 13                     mov      edx, dword ptr [ebx]
0042accf  ff 32                     push     dword ptr [edx]
0042acd1  6a 00                     push     0
0042acd3  ff 75 ec                  push     dword ptr [ebp - 0x14]
0042acd6  e8 d1 de 00 00            call     0x438bac
0042acdb  83 c4 18                  add      esp, 0x18
0042acde  66 c7 46 10 74 00         mov      word ptr [esi + 0x10], 0x74
0042ace4  8b 4d ec                  mov      ecx, dword ptr [ebp - 0x14]
0042ace7  eb 03                     jmp      0x42acec
0042ace9  8b 4d ec                  mov      ecx, dword ptr [ebp - 0x14]
0042acec  8b 03                     mov      eax, dword ptr [ebx]
0042acee  89 48 2d                  mov      dword ptr [eax + 0x2d], ecx
0042acf1  68 b0 00 00 00            push     0xb0
0042acf6  e8 f1 d7 00 00            call     0x4384ec
0042acfb  59                        pop      ecx
0042acfc  89 45 e8                  mov      dword ptr [ebp - 0x18], eax
0042acff  85 c0                     test     eax, eax
0042ad01  74 2b                     je       0x42ad2e
0042ad03  66 c7 46 10 98 00         mov      word ptr [esi + 0x10], 0x98
0042ad09  6a 00                     push     0
0042ad0b  6a 00                     push     0
0042ad0d  68 ee 03 00 00            push     0x3ee
0042ad12  8b 13                     mov      edx, dword ptr [ebx]
0042ad14  ff 32                     push     dword ptr [edx]
0042ad16  6a 00                     push     0
0042ad18  ff 75 e8                  push     dword ptr [ebp - 0x18]
0042ad1b  e8 8c de 00 00            call     0x438bac
0042ad20  83 c4 18                  add      esp, 0x18
0042ad23  66 c7 46 10 8c 00         mov      word ptr [esi + 0x10], 0x8c
0042ad29  8b 4d e8                  mov      ecx, dword ptr [ebp - 0x18]
0042ad2c  eb 03                     jmp      0x42ad31
0042ad2e  8b 4d e8                  mov      ecx, dword ptr [ebp - 0x18]
0042ad31  8b 03                     mov      eax, dword ptr [ebx]
0042ad33  89 48 31                  mov      dword ptr [eax + 0x31], ecx
0042ad36  68 b0 00 00 00            push     0xb0
0042ad3b  e8 ac d7 00 00            call     0x4384ec
0042ad40  59                        pop      ecx
0042ad41  89 45 e4                  mov      dword ptr [ebp - 0x1c], eax
0042ad44  85 c0                     test     eax, eax
0042ad46  74 2b                     je       0x42ad73
0042ad48  66 c7 46 10 b0 00         mov      word ptr [esi + 0x10], 0xb0
0042ad4e  6a 00                     push     0
0042ad50  6a 00                     push     0
0042ad52  68 ef 03 00 00            push     0x3ef
0042ad57  8b 13                     mov      edx, dword ptr [ebx]
0042ad59  ff 32                     push     dword ptr [edx]
0042ad5b  6a 00                     push     0
0042ad5d  ff 75 e4                  push     dword ptr [ebp - 0x1c]
0042ad60  e8 47 de 00 00            call     0x438bac
0042ad65  83 c4 18                  add      esp, 0x18
0042ad68  66 c7 46 10 a4 00         mov      word ptr [esi + 0x10], 0xa4
0042ad6e  8b 4d e4                  mov      ecx, dword ptr [ebp - 0x1c]
0042ad71  eb 03                     jmp      0x42ad76
0042ad73  8b 4d e4                  mov      ecx, dword ptr [ebp - 0x1c]
0042ad76  8b 03                     mov      eax, dword ptr [ebx]
0042ad78  89 48 35                  mov      dword ptr [eax + 0x35], ecx
0042ad7b  68 b0 00 00 00            push     0xb0
0042ad80  e8 67 d7 00 00            call     0x4384ec
0042ad85  59                        pop      ecx
0042ad86  89 45 e0                  mov      dword ptr [ebp - 0x20], eax
0042ad89  85 c0                     test     eax, eax
0042ad8b  74 2b                     je       0x42adb8
0042ad8d  66 c7 46 10 c8 00         mov      word ptr [esi + 0x10], 0xc8
0042ad93  6a 00                     push     0
0042ad95  6a 00                     push     0
0042ad97  68 f0 03 00 00            push     0x3f0
0042ad9c  8b 13                     mov      edx, dword ptr [ebx]
0042ad9e  ff 32                     push     dword ptr [edx]
0042ada0  6a 00                     push     0
0042ada2  ff 75 e0                  push     dword ptr [ebp - 0x20]
0042ada5  e8 02 de 00 00            call     0x438bac
0042adaa  83 c4 18                  add      esp, 0x18
0042adad  66 c7 46 10 bc 00         mov      word ptr [esi + 0x10], 0xbc
0042adb3  8b 4d e0                  mov      ecx, dword ptr [ebp - 0x20]
0042adb6  eb 03                     jmp      0x42adbb
0042adb8  8b 4d e0                  mov      ecx, dword ptr [ebp - 0x20]
0042adbb  8b 03                     mov      eax, dword ptr [ebx]
0042adbd  89 48 39                  mov      dword ptr [eax + 0x39], ecx
0042adc0  68 b0 00 00 00            push     0xb0
0042adc5  e8 22 d7 00 00            call     0x4384ec
0042adca  59                        pop      ecx
0042adcb  89 45 dc                  mov      dword ptr [ebp - 0x24], eax
0042adce  85 c0                     test     eax, eax
0042add0  74 2b                     je       0x42adfd
0042add2  66 c7 46 10 e0 00         mov      word ptr [esi + 0x10], 0xe0
0042add8  6a 00                     push     0
0042adda  6a 00                     push     0
0042addc  68 f1 03 00 00            push     0x3f1
0042ade1  8b 13                     mov      edx, dword ptr [ebx]
0042ade3  ff 32                     push     dword ptr [edx]
0042ade5  6a 00                     push     0
0042ade7  ff 75 dc                  push     dword ptr [ebp - 0x24]
0042adea  e8 bd dd 00 00            call     0x438bac
0042adef  83 c4 18                  add      esp, 0x18
0042adf2  66 c7 46 10 d4 00         mov      word ptr [esi + 0x10], 0xd4
0042adf8  8b 4d dc                  mov      ecx, dword ptr [ebp - 0x24]
0042adfb  eb 03                     jmp      0x42ae00
0042adfd  8b 4d dc                  mov      ecx, dword ptr [ebp - 0x24]
0042ae00  8b 03                     mov      eax, dword ptr [ebx]
0042ae02  89 48 3d                  mov      dword ptr [eax + 0x3d], ecx
0042ae05  8b 16                     mov      edx, dword ptr [esi]
0042ae07  64 89 15 00 00 00 00      mov      dword ptr fs:[0], edx
0042ae0e  8b 03                     mov      eax, dword ptr [ebx]
0042ae10  5e                        pop      esi
0042ae11  5b                        pop      ebx
0042ae12  8b e5                     mov      esp, ebp
0042ae14  5d                        pop      ebp
0042ae15  c3                        ret      
```

### Function Calls

**Other Calls**:

- `0042aa8b` → `sub_402C18`
- `0042ab0f` → `sub_438C18`
- `0042ab4a` → `sub_438C48`
- `0042ab9d` → `sub_4384EC`
- `0042abc2` → `sub_438BAC`
- `0042abe2` → `sub_4384EC`
- `0042ac07` → `sub_438BAC`
- `0042ac27` → `sub_4384EC`
- `0042ac4c` → `sub_438BAC`
- `0042ac6c` → `sub_4384EC`
- `0042ac91` → `sub_438BAC`
- `0042acb1` → `sub_4384EC`
- `0042acd6` → `sub_438BAC`
- `0042acf6` → `sub_4384EC`
- `0042ad1b` → `sub_438BAC`
- `0042ad3b` → `sub_4384EC`
- `0042ad60` → `sub_438BAC`
- `0042ad80` → `sub_4384EC`
- `0042ada5` → `sub_438BAC`
- `0042adc5` → `sub_4384EC`
- ... and 1 more

---

## Method [1]: 0x00440001

**Address**: 0x00440001
**Index in vtable**: 1

**Size**: ~500 bytes

### Assembly Code

```assembly
00440001  00 05 00 00 00 00         add      byte ptr [0], al
00440007  00 00                     add      byte ptr [eax], al
00440009  00 00                     add      byte ptr [eax], al
0044000b  00 14 00                  add      byte ptr [eax + eax], dl
0044000e  05 00 0b 00 00            add      eax, 0xb00
00440013  00 dc                     add      ah, bl
00440015  0f 44 00                  cmove    eax, dword ptr [eax]
00440018  fa                        cli      
00440019  11 41 00                  adc      dword ptr [ecx], eax
0044001c  05 00 00 00 08            add      eax, 0x8000000
00440021  00 00                     add      byte ptr [eax], al
00440023  00 00                     add      byte ptr [eax], al
00440025  00 00                     add      byte ptr [eax], al
00440027  00 00                     add      byte ptr [eax], al
00440029  00 00                     add      byte ptr [eax], al
0044002b  00 dc                     add      ah, bl
```

---

