# TVNTimer - Complete Assembly Extraction

**Vtable Address**: 0x004394D4
**Binary**: europeo.exe
**Tool**: Capstone Disassembler
**Date**: 2026-01-16

---

## Methods Summary

| Index | Address |
|-------|----------|
|  0 | 0x0043A49C |
|  1 | 0x00405181 |

---

## Method [0]: 0x0043A49C

**Address**: 0x0043A49C
**Index in vtable**: 0

**Size**: ~500 bytes

### Assembly Code

```assembly
0043a49c  3d 20 30 20 26            cmp      eax, 0x26203020
0043a4a1  26 20 69 6e               and      byte ptr es:[ecx + 0x6e], ch
0043a4a5  64 65 78 20               js       0x43a4c9
0043a4a9  3c 20                     cmp      al, 0x20
0043a4ab  4c                        dec      esp
0043a4ac  69 6d 00 43 3a 5c 42      imul     ebp, dword ptr [ebp], 0x425c3a43
0043a4b3  43                        inc      ebx
0043a4b4  35 5c 49 4e 43            xor      eax, 0x434e495c
0043a4b9  4c                        dec      esp
0043a4ba  55                        push     ebp
0043a4bb  44                        inc      esp
0043a4bc  45                        inc      ebp
0043a4bd  5c                        pop      esp
0043a4be  63 6c 61 73               arpl     word ptr [ecx + 0x73], bp
0043a4c2  73 6c                     jae      0x43a530
0043a4c4  69 62 2f 76 65 63 74      imul     esp, dword ptr [edx + 0x2f], 0x74636576
0043a4cb  69 6d 70 2e 68 00 50      imul     ebp, dword ptr [ebp + 0x70], 0x5000682e
0043a4d2  72 65                     jb       0x43a539
0043a4d4  63 6f 6e                  arpl     word ptr [edi + 0x6e], bp
0043a4d7  64 69 74 69 6f 6e 00 00 00  imul     esi, dword ptr fs:[ecx + ebp*2 + 0x6f], 0x6e
0043a4e0  89 6d 40                  mov      dword ptr [ebp + 0x40], ebp
0043a4e3  00 00                     add      byte ptr [eax], al
0043a4e5  00 00                     add      byte ptr [eax], al
0043a4e7  00 00                     add      byte ptr [eax], al
0043a4e9  00 00                     add      byte ptr [eax], al
0043a4eb  00 50 5b                  add      byte ptr [eax + 0x5b], dl
0043a4ee  40                        inc      eax
0043a4ef  00 63 5a                  add      byte ptr [ebx + 0x5a], ah
0043a4f2  40                        inc      eax
0043a4f3  00 b5 6c 40 00 00         add      byte ptr [ebp + 0x406c], dh
0043a4f9  00 00                     add      byte ptr [eax], al
0043a4fb  00 00                     add      byte ptr [eax], al
0043a4fd  00 00                     add      byte ptr [eax], al
0043a4ff  00 e5                     add      ch, ah
0043a501  6d                        insd     dword ptr es:[edi], dx
0043a502  40                        inc      eax
0043a503  00 f0                     add      al, dh
0043a505  6d                        insd     dword ptr es:[edi], dx
0043a506  40                        inc      eax
0043a507  00 fb                     add      bl, bh
0043a509  6d                        insd     dword ptr es:[edi], dx
0043a50a  40                        inc      eax
0043a50b  00 02                     add      byte ptr [edx], al
0043a50d  6e                        outsb    dx, byte ptr [esi]
0043a50e  40                        inc      eax
0043a50f  00 07                     add      byte ptr [edi], al
0043a511  6e                        outsb    dx, byte ptr [esi]
0043a512  40                        inc      eax
0043a513  00 00                     add      byte ptr [eax], al
0043a515  00 00                     add      byte ptr [eax], al
0043a517  00 00                     add      byte ptr [eax], al
0043a519  00 00                     add      byte ptr [eax], al
0043a51b  00 e5                     add      ch, ah
0043a51d  6d                        insd     dword ptr es:[edi], dx
0043a51e  40                        inc      eax
0043a51f  00 f0                     add      al, dh
0043a521  6d                        insd     dword ptr es:[edi], dx
0043a522  40                        inc      eax
0043a523  00 fb                     add      bl, bh
0043a525  6d                        insd     dword ptr es:[edi], dx
0043a526  40                        inc      eax
0043a527  00 2b                     add      byte ptr [ebx], ch
0043a529  6c                        insb     byte ptr es:[edi], dx
0043a52a  40                        inc      eax
0043a52b  00 7f 6e                  add      byte ptr [edi + 0x6e], bh
0043a52e  40                        inc      eax
0043a52f  00 00                     add      byte ptr [eax], al
0043a531  00 00                     add      byte ptr [eax], al
0043a533  00 00                     add      byte ptr [eax], al
0043a535  00 00                     add      byte ptr [eax], al
0043a537  00 f7                     add      bh, dh
0043a539  6e                        outsb    dx, byte ptr [esi]
0043a53a  40                        inc      eax
0043a53b  00 02                     add      byte ptr [edx], al
0043a53d  6f                        outsd    dx, dword ptr [esi]
0043a53e  40                        inc      eax
0043a53f  00 0d 6f 40 00 2b         add      byte ptr [0x2b00406f], cl
0043a545  6c                        insb     byte ptr es:[edi], dx
0043a546  40                        inc      eax
0043a547  00 31                     add      byte ptr [ecx], dh
0043a549  68 40 00 00 00            push     0x40
0043a54e  00 00                     add      byte ptr [eax], al
0043a550  00 00                     add      byte ptr [eax], al
0043a552  00 00                     add      byte ptr [eax], al
0043a554  2d 6d 40 00 18            sub      eax, 0x1800406d
0043a559  6f                        outsd    dx, dword ptr [esi]
0043a55a  40                        inc      eax
0043a55b  00 aa 6f 40 00 25         add      byte ptr [edx + 0x2500406f], ch
0043a561  3c 40                     cmp      al, 0x40
0043a563  00 04 00                  add      byte ptr [eax + eax], al
0043a566  00 00                     add      byte ptr [eax], al
0043a568  fc                        cld      
```

---

## Method [1]: 0x00405181

**Address**: 0x00405181
**Index in vtable**: 1

**Size**: ~1988 bytes

### Assembly Code

```assembly
00405181  0a 83 7f 19 02 74         or       al, byte ptr [ebx + 0x7402197f]
00405187  04 33                     add      al, 0x33
00405189  c0 eb 05                  shr      bl, 5
0040518c  b8 01 00 00 00            mov      eax, 1
00405191  8d 57 04                  lea      edx, [edi + 4]
00405194  89 55 c0                  mov      dword ptr [ebp - 0x40], edx
00405197  6a 00                     push     0
00405199  6a ff                     push     -1
0040519b  50                        push     eax
0040519c  ff 75 c0                  push     dword ptr [ebp - 0x40]
0040519f  e8 fe 0f 00 00            call     0x4061a2
004051a4  83 c4 10                  add      esp, 0x10
004051a7  8b 4d c0                  mov      ecx, dword ptr [ebp - 0x40]
004051aa  33 c0                     xor      eax, eax
004051ac  89 41 0d                  mov      dword ptr [ecx + 0xd], eax
004051af  8d 53 04                  lea      edx, [ebx + 4]
004051b2  52                        push     edx
004051b3  8b 4b 05                  mov      ecx, dword ptr [ebx + 5]
004051b6  ff 51 04                  call     dword ptr [ecx + 4]
004051b9  59                        pop      ecx
004051ba  40                        inc      eax
004051bb  89 45 bc                  mov      dword ptr [ebp - 0x44], eax
004051be  8b 07                     mov      eax, dword ptr [edi]
004051c0  3b 45 bc                  cmp      eax, dword ptr [ebp - 0x44]
004051c3  7e 1e                     jle      0x4051e3
004051c5  8b 55 bc                  mov      edx, dword ptr [ebp - 0x44]
004051c8  2b 17                     sub      edx, dword ptr [edi]
004051ca  03 57 0d                  add      edx, dword ptr [edi + 0xd]
004051cd  89 55 b8                  mov      dword ptr [ebp - 0x48], edx
004051d0  6a 00                     push     0
004051d2  ff 75 b8                  push     dword ptr [ebp - 0x48]
004051d5  8d 4f 04                  lea      ecx, [edi + 4]
004051d8  51                        push     ecx
004051d9  e8 76 0d 00 00            call     0x405f54
004051de  83 c4 0c                  add      esp, 0xc
004051e1  eb 36                     jmp      0x405219
004051e3  8b 47 0d                  mov      eax, dword ptr [edi + 0xd]
004051e6  89 45 b4                  mov      dword ptr [ebp - 0x4c], eax
004051e9  83 7d b4 ff               cmp      dword ptr [ebp - 0x4c], -1
004051ed  75 07                     jne      0x4051f6
004051ef  ba ff ff ff 7f            mov      edx, 0x7fffffff
004051f4  eb 05                     jmp      0x4051fb
004051f6  8b 17                     mov      edx, dword ptr [edi]
004051f8  03 55 b4                  add      edx, dword ptr [ebp - 0x4c]
004051fb  3b 55 bc                  cmp      edx, dword ptr [ebp - 0x44]
004051fe  7f 19                     jg       0x405219
00405200  8b 45 bc                  mov      eax, dword ptr [ebp - 0x44]
00405203  2b 07                     sub      eax, dword ptr [edi]
00405205  89 45 b0                  mov      dword ptr [ebp - 0x50], eax
00405208  6a 00                     push     0
0040520a  ff 75 b0                  push     dword ptr [ebp - 0x50]
0040520d  8d 4f 04                  lea      ecx, [edi + 4]
00405210  51                        push     ecx
00405211  e8 3e 0d 00 00            call     0x405f54
00405216  83 c4 0c                  add      esp, 0xc
00405219  8b c3                     mov      eax, ebx
0040521b  83 c0 04                  add      eax, 4
0040521e  89 45 90                  mov      dword ptr [ebp - 0x70], eax
00405221  50                        push     eax
00405222  8b 50 01                  mov      edx, dword ptr [eax + 1]
00405225  ff 12                     call     dword ptr [edx]
00405227  59                        pop      ecx
00405228  33 c9                     xor      ecx, ecx
0040522a  89 4d 98                  mov      dword ptr [ebp - 0x68], ecx
0040522d  89 4d 94                  mov      dword ptr [ebp - 0x6c], ecx
00405230  89 45 9c                  mov      dword ptr [ebp - 0x64], eax
00405233  e9 c6 01 00 00            jmp      0x4053fe
00405238  8b 45 94                  mov      eax, dword ptr [ebp - 0x6c]
0040523b  3b 45 9c                  cmp      eax, dword ptr [ebp - 0x64]
0040523e  72 76                     jb       0x4052b6
00405240  56                        push     esi
00405241  6a 00                     push     0
00405243  6a 00                     push     0
00405245  6a 00                     push     0
00405247  6a 01                     push     1
00405249  68 e0 3b 40 00            push     0x403be0
0040524e  6a 00                     push     0
00405250  68 db 03 00 00            push     0x3db
00405255  68 b1 b1 43 00            push     0x43b1b1
0040525a  68 a5 b1 43 00            push     0x43b1a5
0040525f  68 d3 b1 43 00            push     0x43b1d3
00405264  8d 55 fc                  lea      edx, [ebp - 4]
00405267  52                        push     edx
00405268  e8 a3 32 03 00            call     0x438510
0040526d  83 c4 14                  add      esp, 0x14
00405270  8d 45 fc                  lea      eax, [ebp - 4]
00405273  50                        push     eax
00405274  ff 46 1c                  inc      dword ptr [esi + 0x1c]
00405277  8d 55 f8                  lea      edx, [ebp - 8]
0040527a  52                        push     edx
0040527b  e8 64 31 03 00            call     0x4383e4
00405280  83 c4 08                  add      esp, 8
00405283  ff 46 1c                  inc      dword ptr [esi + 0x1c]
00405286  66 c7 46 10 0c 00         mov      word ptr [esi + 0x10], 0xc
0040528c  ff 4e 1c                  dec      dword ptr [esi + 0x1c]
0040528f  6a 02                     push     2
00405291  8d 4d fc                  lea      ecx, [ebp - 4]
00405294  51                        push     ecx
00405295  e8 ca 32 03 00            call     0x438564
0040529a  83 c4 08                  add      esp, 8
0040529d  83 46 1c 02               add      dword ptr [esi + 0x1c], 2
004052a1  83 46 1c 03               add      dword ptr [esi + 0x1c], 3
004052a5  8d 45 f8                  lea      eax, [ebp - 8]
004052a8  50                        push     eax
004052a9  68 88 3b 40 00            push     0x403b88
004052ae  e8 f7 31 03 00            call     0x4384aa
004052b3  83 c4 24                  add      esp, 0x24
004052b6  8b 55 94                  mov      edx, dword ptr [ebp - 0x6c]
004052b9  89 55 a8                  mov      dword ptr [ebp - 0x58], edx
004052bc  8b 5d 90                  mov      ebx, dword ptr [ebp - 0x70]
004052bf  83 7b 09 00               cmp      dword ptr [ebx + 9], 0
004052c3  76 0e                     jbe      0x4052d3
004052c5  83 7b 05 00               cmp      dword ptr [ebx + 5], 0
004052c9  74 08                     je       0x4052d3
004052cb  8b 4d a8                  mov      ecx, dword ptr [ebp - 0x58]
004052ce  3b 4b 09                  cmp      ecx, dword ptr [ebx + 9]
004052d1  72 76                     jb       0x405349
004052d3  56                        push     esi
004052d4  6a 00                     push     0
004052d6  6a 00                     push     0
004052d8  6a 00                     push     0
004052da  6a 01                     push     1
004052dc  68 e0 3b 40 00            push     0x403be0
004052e1  6a 00                     push     0
004052e3  68 3a 03 00 00            push     0x33a
004052e8  68 04 b2 43 00            push     0x43b204
004052ed  68 e0 b1 43 00            push     0x43b1e0
004052f2  68 26 b2 43 00            push     0x43b226
004052f7  8d 45 f4                  lea      eax, [ebp - 0xc]
004052fa  50                        push     eax
004052fb  e8 10 32 03 00            call     0x438510
00405300  83 c4 14                  add      esp, 0x14
00405303  8d 55 f4                  lea      edx, [ebp - 0xc]
00405306  52                        push     edx
00405307  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0040530a  8d 4d f0                  lea      ecx, [ebp - 0x10]
0040530d  51                        push     ecx
0040530e  e8 d1 30 03 00            call     0x4383e4
00405313  83 c4 08                  add      esp, 8
00405316  ff 46 1c                  inc      dword ptr [esi + 0x1c]
00405319  66 c7 46 10 18 00         mov      word ptr [esi + 0x10], 0x18
0040531f  ff 4e 1c                  dec      dword ptr [esi + 0x1c]
00405322  6a 02                     push     2
00405324  8d 45 f4                  lea      eax, [ebp - 0xc]
00405327  50                        push     eax
00405328  e8 37 32 03 00            call     0x438564
0040532d  83 c4 08                  add      esp, 8
00405330  83 46 1c 02               add      dword ptr [esi + 0x1c], 2
00405334  83 46 1c 03               add      dword ptr [esi + 0x1c], 3
00405338  8d 55 f0                  lea      edx, [ebp - 0x10]
0040533b  52                        push     edx
0040533c  68 88 3b 40 00            push     0x403b88
00405341  e8 64 31 03 00            call     0x4384aa
00405346  83 c4 24                  add      esp, 0x24
00405349  8b 4d a8                  mov      ecx, dword ptr [ebp - 0x58]
0040534c  c1 e1 02                  shl      ecx, 2
0040534f  03 4b 05                  add      ecx, dword ptr [ebx + 5]
00405352  8b 01                     mov      eax, dword ptr [ecx]
00405354  89 45 ac                  mov      dword ptr [ebp - 0x54], eax
00405357  ff 45 94                  inc      dword ptr [ebp - 0x6c]
0040535a  8b 55 ac                  mov      edx, dword ptr [ebp - 0x54]
0040535d  8b da                     mov      ebx, edx
0040535f  53                        push     ebx
00405360  8b 0b                     mov      ecx, dword ptr [ebx]
00405362  ff 51 08                  call     dword ptr [ecx + 8]
00405365  59                        pop      ecx
00405366  84 c0                     test     al, al
00405368  0f 84 90 00 00 00         je       0x4053fe
0040536e  6a 10                     push     0x10
00405370  e8 77 31 03 00            call     0x4384ec
00405375  59                        pop      ecx
00405376  89 45 ec                  mov      dword ptr [ebp - 0x14], eax
00405379  85 c0                     test     eax, eax
0040537b  74 44                     je       0x4053c1
0040537d  66 c7 46 10 30 00         mov      word ptr [esi + 0x10], 0x30
00405383  89 5d a4                  mov      dword ptr [ebp - 0x5c], ebx
00405386  8b 55 ec                  mov      edx, dword ptr [ebp - 0x14]
00405389  c7 02 54 b5 43 00         mov      dword ptr [edx], 0x43b554
0040538f  8b 4d ec                  mov      ecx, dword ptr [ebp - 0x14]
00405392  83 c1 04                  add      ecx, 4
00405395  51                        push     ecx
00405396  e8 27 31 03 00            call     0x4384c2
0040539b  59                        pop      ecx
0040539c  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0040539f  ff 75 ec                  push     dword ptr [ebp - 0x14]
004053a2  e8 96 f9 ff ff            call     0x404d3d
004053a7  59                        pop      ecx
004053a8  ff 75 a4                  push     dword ptr [ebp - 0x5c]
004053ab  ff 75 ec                  push     dword ptr [ebp - 0x14]
004053ae  e8 f6 f9 ff ff            call     0x404da9
004053b3  83 c4 08                  add      esp, 8
004053b6  66 c7 46 10 24 00         mov      word ptr [esi + 0x10], 0x24
004053bc  8b 45 ec                  mov      eax, dword ptr [ebp - 0x14]
004053bf  eb 03                     jmp      0x4053c4
004053c1  8b 45 ec                  mov      eax, dword ptr [ebp - 0x14]
004053c4  8b d8                     mov      ebx, eax
004053c6  89 5d a0                  mov      dword ptr [ebp - 0x60], ebx
004053c9  ff 75 a0                  push     dword ptr [ebp - 0x60]
004053cc  8d 57 04                  lea      edx, [edi + 4]
004053cf  52                        push     edx
004053d0  e8 74 0c 00 00            call     0x406049
004053d5  83 c4 08                  add      esp, 8
004053d8  85 c0                     test     eax, eax
004053da  75 22                     jne      0x4053fe
004053dc  89 5d e8                  mov      dword ptr [ebp - 0x18], ebx
004053df  83 7d e8 00               cmp      dword ptr [ebp - 0x18], 0
004053e3  74 19                     je       0x4053fe
004053e5  66 c7 46 10 48 00         mov      word ptr [esi + 0x10], 0x48
004053eb  6a 03                     push     3
004053ed  8b 4d e8                  mov      ecx, dword ptr [ebp - 0x18]
004053f0  51                        push     ecx
004053f1  8b 01                     mov      eax, dword ptr [ecx]
004053f3  ff 10                     call     dword ptr [eax]
004053f5  83 c4 08                  add      esp, 8
004053f8  66 c7 46 10 3c 00         mov      word ptr [esi + 0x10], 0x3c
004053fe  8b 55 94                  mov      edx, dword ptr [ebp - 0x6c]
00405401  3b 55 9c                  cmp      edx, dword ptr [ebp - 0x64]
00405404  0f 82 2e fe ff ff         jb       0x405238
0040540a  8b c7                     mov      eax, edi
0040540c  8b 16                     mov      edx, dword ptr [esi]
0040540e  64 89 15 00 00 00 00      mov      dword ptr fs:[0], edx
00405415  5f                        pop      edi
00405416  5e                        pop      esi
00405417  5b                        pop      ebx
00405418  8b e5                     mov      esp, ebp
0040541a  5d                        pop      ebp
0040541b  c3                        ret      
0040541c  55                        push     ebp
0040541d  8b ec                     mov      ebp, esp
0040541f  83 c4 c0                  add      esp, -0x40
00405422  53                        push     ebx
00405423  56                        push     esi
00405424  57                        push     edi
00405425  8b 5d 08                  mov      ebx, dword ptr [ebp + 8]
00405428  b8 88 ac 43 00            mov      eax, 0x43ac88
0040542d  e8 e6 d7 ff ff            call     0x402c18
00405432  8b 55 0c                  mov      edx, dword ptr [ebp + 0xc]
00405435  8b 0a                     mov      ecx, dword ptr [edx]
00405437  83 79 06 00               cmp      dword ptr [ecx + 6], 0
0040543b  0f 84 7f 01 00 00         je       0x4055c0
00405441  33 c0                     xor      eax, eax
00405443  89 45 c8                  mov      dword ptr [ebp - 0x38], eax
00405446  e9 61 01 00 00            jmp      0x4055ac
0040544b  8b 7d c8                  mov      edi, dword ptr [ebp - 0x38]
0040544e  3b 3b                     cmp      edi, dword ptr [ebx]
00405450  7c 09                     jl       0x40545b
00405452  8b d7                     mov      edx, edi
00405454  2b 13                     sub      edx, dword ptr [ebx]
00405456  3b 53 0d                  cmp      edx, dword ptr [ebx + 0xd]
00405459  72 79                     jb       0x4054d4
0040545b  8d 4d cc                  lea      ecx, [ebp - 0x34]
0040545e  51                        push     ecx
0040545f  6a 00                     push     0
00405461  6a 00                     push     0
00405463  6a 00                     push     0
00405465  6a 01                     push     1
00405467  68 e0 3b 40 00            push     0x403be0
0040546c  6a 00                     push     0
0040546e  68 5e 01 00 00            push     0x15e
00405473  68 65 b2 43 00            push     0x43b265
00405478  68 33 b2 43 00            push     0x43b233
0040547d  68 86 b2 43 00            push     0x43b286
00405482  8d 45 fc                  lea      eax, [ebp - 4]
00405485  50                        push     eax
00405486  e8 85 30 03 00            call     0x438510
0040548b  83 c4 14                  add      esp, 0x14
0040548e  8d 55 fc                  lea      edx, [ebp - 4]
00405491  52                        push     edx
00405492  ff 45 e8                  inc      dword ptr [ebp - 0x18]
00405495  8d 4d f8                  lea      ecx, [ebp - 8]
00405498  51                        push     ecx
00405499  e8 46 2f 03 00            call     0x4383e4
0040549e  83 c4 08                  add      esp, 8
004054a1  ff 45 e8                  inc      dword ptr [ebp - 0x18]
004054a4  66 c7 45 dc 0c 00         mov      word ptr [ebp - 0x24], 0xc
004054aa  ff 4d e8                  dec      dword ptr [ebp - 0x18]
004054ad  6a 02                     push     2
004054af  8d 45 fc                  lea      eax, [ebp - 4]
004054b2  50                        push     eax
004054b3  e8 ac 30 03 00            call     0x438564
004054b8  83 c4 08                  add      esp, 8
004054bb  83 45 e8 02               add      dword ptr [ebp - 0x18], 2
004054bf  83 45 e8 03               add      dword ptr [ebp - 0x18], 3
004054c3  8d 55 f8                  lea      edx, [ebp - 8]
004054c6  52                        push     edx
004054c7  68 88 3b 40 00            push     0x403b88
004054cc  e8 d9 2f 03 00            call     0x4384aa
004054d1  83 c4 24                  add      esp, 0x24
004054d4  2b 3b                     sub      edi, dword ptr [ebx]
004054d6  89 7d c4                  mov      dword ptr [ebp - 0x3c], edi
004054d9  8d 73 04                  lea      esi, [ebx + 4]
004054dc  83 7e 09 00               cmp      dword ptr [esi + 9], 0
004054e0  76 0e                     jbe      0x4054f0
004054e2  83 7e 05 00               cmp      dword ptr [esi + 5], 0
004054e6  74 08                     je       0x4054f0
004054e8  8b 45 c4                  mov      eax, dword ptr [ebp - 0x3c]
004054eb  3b 46 09                  cmp      eax, dword ptr [esi + 9]
004054ee  72 79                     jb       0x405569
004054f0  8d 55 cc                  lea      edx, [ebp - 0x34]
004054f3  52                        push     edx
004054f4  6a 00                     push     0
004054f6  6a 00                     push     0
004054f8  6a 00                     push     0
004054fa  6a 01                     push     1
004054fc  68 e0 3b 40 00            push     0x403be0
00405501  6a 00                     push     0
00405503  68 3a 03 00 00            push     0x33a
00405508  68 b7 b2 43 00            push     0x43b2b7
0040550d  68 93 b2 43 00            push     0x43b293
00405512  68 d9 b2 43 00            push     0x43b2d9
00405517  8d 4d f4                  lea      ecx, [ebp - 0xc]
0040551a  51                        push     ecx
0040551b  e8 f0 2f 03 00            call     0x438510
00405520  83 c4 14                  add      esp, 0x14
00405523  8d 45 f4                  lea      eax, [ebp - 0xc]
00405526  50                        push     eax
00405527  ff 45 e8                  inc      dword ptr [ebp - 0x18]
0040552a  8d 55 f0                  lea      edx, [ebp - 0x10]
0040552d  52                        push     edx
0040552e  e8 b1 2e 03 00            call     0x4383e4
00405533  83 c4 08                  add      esp, 8
00405536  ff 45 e8                  inc      dword ptr [ebp - 0x18]
00405539  66 c7 45 dc 18 00         mov      word ptr [ebp - 0x24], 0x18
0040553f  ff 4d e8                  dec      dword ptr [ebp - 0x18]
00405542  6a 02                     push     2
00405544  8d 4d f4                  lea      ecx, [ebp - 0xc]
00405547  51                        push     ecx
00405548  e8 17 30 03 00            call     0x438564
0040554d  83 c4 08                  add      esp, 8
00405550  83 45 e8 02               add      dword ptr [ebp - 0x18], 2
00405554  83 45 e8 03               add      dword ptr [ebp - 0x18], 3
00405558  8d 45 f0                  lea      eax, [ebp - 0x10]
0040555b  50                        push     eax
0040555c  68 88 3b 40 00            push     0x403b88
00405561  e8 44 2f 03 00            call     0x4384aa
00405566  83 c4 24                  add      esp, 0x24
00405569  8b 55 c4                  mov      edx, dword ptr [ebp - 0x3c]
0040556c  c1 e2 02                  shl      edx, 2
0040556f  03 56 05                  add      edx, dword ptr [esi + 5]
00405572  8b 32                     mov      esi, dword ptr [edx]
00405574  8b 7d 0c                  mov      edi, dword ptr [ebp + 0xc]
00405577  8d 4e 04                  lea      ecx, [esi + 4]
0040557a  89 4d c0                  mov      dword ptr [ebp - 0x40], ecx
0040557d  57                        push     edi
0040557e  ff 75 c0                  push     dword ptr [ebp - 0x40]
00405581  e8 42 2f 03 00            call     0x4384c8
00405586  83 c4 08                  add      esp, 8
00405589  85 c0                     test     eax, eax
0040558b  75 1c                     jne      0x4055a9
0040558d  83 7d 10 00               cmp      dword ptr [ebp + 0x10], 0
00405591  74 08                     je       0x40559b
00405593  8b 45 10                  mov      eax, dword ptr [ebp + 0x10]
00405596  8b 55 c8                  mov      edx, dword ptr [ebp - 0x38]
00405599  89 10                     mov      dword ptr [eax], edx
0040559b  8b c6                     mov      eax, esi
0040559d  8b 55 cc                  mov      edx, dword ptr [ebp - 0x34]
004055a0  64 89 15 00 00 00 00      mov      dword ptr fs:[0], edx
004055a7  eb 32                     jmp      0x4055db
004055a9  ff 45 c8                  inc      dword ptr [ebp - 0x38]
004055ac  8d 4b 04                  lea      ecx, [ebx + 4]
004055af  51                        push     ecx
004055b0  8b 43 05                  mov      eax, dword ptr [ebx + 5]
004055b3  ff 50 04                  call     dword ptr [eax + 4]
004055b6  59                        pop      ecx
004055b7  3b 45 c8                  cmp      eax, dword ptr [ebp - 0x38]
004055ba  0f 8f 8b fe ff ff         jg       0x40544b
004055c0  83 7d 10 00               cmp      dword ptr [ebp + 0x10], 0
004055c4  74 09                     je       0x4055cf
004055c6  8b 55 10                  mov      edx, dword ptr [ebp + 0x10]
004055c9  c7 02 ff ff ff 7f         mov      dword ptr [edx], 0x7fffffff
004055cf  33 c0                     xor      eax, eax
004055d1  8b 55 cc                  mov      edx, dword ptr [ebp - 0x34]
004055d4  64 89 15 00 00 00 00      mov      dword ptr fs:[0], edx
004055db  5f                        pop      edi
004055dc  5e                        pop      esi
004055dd  5b                        pop      ebx
004055de  8b e5                     mov      esp, ebp
004055e0  5d                        pop      ebp
004055e1  c3                        ret      
004055e2  55                        push     ebp
004055e3  8b ec                     mov      ebp, esp
004055e5  83 c4 cc                  add      esp, -0x34
004055e8  53                        push     ebx
004055e9  56                        push     esi
004055ea  57                        push     edi
004055eb  8b 7d 08                  mov      edi, dword ptr [ebp + 8]
004055ee  b8 e4 ac 43 00            mov      eax, 0x43ace4
004055f3  e8 20 d6 ff ff            call     0x402c18
004055f8  8b 5d 0c                  mov      ebx, dword ptr [ebp + 0xc]
004055fb  85 db                     test     ebx, ebx
004055fd  0f 84 ff 00 00 00         je       0x405702
00405603  6a 00                     push     0
00405605  66 c7 45 e0 14 00         mov      word ptr [ebp - 0x20], 0x14
0040560b  53                        push     ebx
0040560c  8d 45 fc                  lea      eax, [ebp - 4]
0040560f  50                        push     eax
00405610  e8 59 2e 03 00            call     0x43846e
00405615  83 c4 08                  add      esp, 8
00405618  ff 45 ec                  inc      dword ptr [ebp - 0x14]
0040561b  8d 55 fc                  lea      edx, [ebp - 4]
0040561e  52                        push     edx
0040561f  57                        push     edi
00405620  e8 f7 fd ff ff            call     0x40541c
00405625  83 c4 0c                  add      esp, 0xc
00405628  8b f0                     mov      esi, eax
0040562a  ff 4d ec                  dec      dword ptr [ebp - 0x14]
0040562d  6a 02                     push     2
0040562f  8d 45 fc                  lea      eax, [ebp - 4]
00405632  50                        push     eax
00405633  e8 2c 2f 03 00            call     0x438564
00405638  83 c4 08                  add      esp, 8
0040563b  66 c7 45 e0 08 00         mov      word ptr [ebp - 0x20], 8
00405641  85 f6                     test     esi, esi
00405643  74 11                     je       0x405656
00405645  8b c3                     mov      eax, ebx
00405647  50                        push     eax
00405648  56                        push     esi
00405649  e8 94 f7 ff ff            call     0x404de2
0040564e  83 c4 08                  add      esp, 8
00405651  e9 9e 00 00 00            jmp      0x4056f4
00405656  6a 10                     push     0x10
00405658  e8 8f 2e 03 00            call     0x4384ec
0040565d  59                        pop      ecx
0040565e  89 45 f8                  mov      dword ptr [ebp - 8], eax
00405661  85 c0                     test     eax, eax
00405663  74 41                     je       0x4056a6
00405665  66 c7 45 e0 2c 00         mov      word ptr [ebp - 0x20], 0x2c
0040566b  8b f3                     mov      esi, ebx
0040566d  8b 55 f8                  mov      edx, dword ptr [ebp - 8]
00405670  c7 02 54 b5 43 00         mov      dword ptr [edx], 0x43b554
00405676  8b 4d f8                  mov      ecx, dword ptr [ebp - 8]
00405679  83 c1 04                  add      ecx, 4
0040567c  51                        push     ecx
0040567d  e8 40 2e 03 00            call     0x4384c2
00405682  59                        pop      ecx
00405683  ff 45 ec                  inc      dword ptr [ebp - 0x14]
00405686  ff 75 f8                  push     dword ptr [ebp - 8]
00405689  e8 af f6 ff ff            call     0x404d3d
0040568e  59                        pop      ecx
0040568f  56                        push     esi
00405690  ff 75 f8                  push     dword ptr [ebp - 8]
00405693  e8 4a f7 ff ff            call     0x404de2
00405698  83 c4 08                  add      esp, 8
0040569b  66 c7 45 e0 20 00         mov      word ptr [ebp - 0x20], 0x20
004056a1  8b 45 f8                  mov      eax, dword ptr [ebp - 8]
004056a4  eb 03                     jmp      0x4056a9
004056a6  8b 45 f8                  mov      eax, dword ptr [ebp - 8]
004056a9  8b f0                     mov      esi, eax
004056ab  66 c7 45 e0 08 00         mov      word ptr [ebp - 0x20], 8
004056b1  56                        push     esi
004056b2  8b 16                     mov      edx, dword ptr [esi]
004056b4  ff 52 08                  call     dword ptr [edx + 8]
004056b7  59                        pop      ecx
004056b8  84 c0                     test     al, al
004056ba  74 16                     je       0x4056d2
004056bc  89 75 cc                  mov      dword ptr [ebp - 0x34], esi
004056bf  ff 75 cc                  push     dword ptr [ebp - 0x34]
004056c2  8d 4f 04                  lea      ecx, [edi + 4]
004056c5  51                        push     ecx
004056c6  e8 7e 09 00 00            call     0x406049
004056cb  83 c4 08                  add      esp, 8
004056ce  85 c0                     test     eax, eax
004056d0  75 22                     jne      0x4056f4
004056d2  89 75 f4                  mov      dword ptr [ebp - 0xc], esi
004056d5  83 7d f4 00               cmp      dword ptr [ebp - 0xc], 0
004056d9  74 19                     je       0x4056f4
004056db  66 c7 45 e0 44 00         mov      word ptr [ebp - 0x20], 0x44
004056e1  6a 03                     push     3
004056e3  8b 45 f4                  mov      eax, dword ptr [ebp - 0xc]
004056e6  50                        push     eax
004056e7  8b 10                     mov      edx, dword ptr [eax]
004056e9  ff 12                     call     dword ptr [edx]
004056eb  83 c4 08                  add      esp, 8
004056ee  66 c7 45 e0 38 00         mov      word ptr [ebp - 0x20], 0x38
004056f4  8b 9b 04 01 00 00         mov      ebx, dword ptr [ebx + 0x104]
004056fa  85 db                     test     ebx, ebx
004056fc  0f 85 01 ff ff ff         jne      0x405603
00405702  8b 4d d0                  mov      ecx, dword ptr [ebp - 0x30]
00405705  64 89 0d 00 00 00 00      mov      dword ptr fs:[0], ecx
0040570c  5f                        pop      edi
0040570d  5e                        pop      esi
0040570e  5b                        pop      ebx
0040570f  8b e5                     mov      esp, ebp
00405711  5d                        pop      ebp
00405712  c3                        ret      
00405713  55                        push     ebp
00405714  8b ec                     mov      ebp, esp
00405716  83 c4 b0                  add      esp, -0x50
00405719  53                        push     ebx
0040571a  56                        push     esi
0040571b  57                        push     edi
0040571c  8d 75 c4                  lea      esi, [ebp - 0x3c]
0040571f  b8 a8 ad 43 00            mov      eax, 0x43ada8
00405724  e8 ef d4 ff ff            call     0x402c18
00405729  8b 45 0c                  mov      eax, dword ptr [ebp + 0xc]
0040572c  83 c0 04                  add      eax, 4
0040572f  89 45 b0                  mov      dword ptr [ebp - 0x50], eax
00405732  50                        push     eax
00405733  8b 50 01                  mov      edx, dword ptr [eax + 1]
00405736  ff 12                     call     dword ptr [edx]
00405738  59                        pop      ecx
00405739  33 c9                     xor      ecx, ecx
0040573b  89 4d b8                  mov      dword ptr [ebp - 0x48], ecx
0040573e  89 4d b4                  mov      dword ptr [ebp - 0x4c], ecx
00405741  89 45 bc                  mov      dword ptr [ebp - 0x44], eax
00405744  e9 e0 01 00 00            jmp      0x405929
00405749  8b 45 b4                  mov      eax, dword ptr [ebp - 0x4c]
0040574c  3b 45 bc                  cmp      eax, dword ptr [ebp - 0x44]
0040574f  72 76                     jb       0x4057c7
00405751  56                        push     esi
00405752  6a 00                     push     0
00405754  6a 00                     push     0
00405756  6a 00                     push     0
00405758  6a 01                     push     1
0040575a  68 e0 3b 40 00            push     0x403be0
0040575f  6a 00                     push     0
00405761  68 db 03 00 00            push     0x3db
00405766  68 f2 b2 43 00            push     0x43b2f2
0040576b  68 e6 b2 43 00            push     0x43b2e6
00405770  68 14 b3 43 00            push     0x43b314
00405775  8d 55 fc                  lea      edx, [ebp - 4]
00405778  52                        push     edx
00405779  e8 92 2d 03 00            call     0x438510
0040577e  83 c4 14                  add      esp, 0x14
00405781  8d 45 fc                  lea      eax, [ebp - 4]
00405784  50                        push     eax
00405785  ff 46 1c                  inc      dword ptr [esi + 0x1c]
00405788  8d 55 f8                  lea      edx, [ebp - 8]
0040578b  52                        push     edx
0040578c  e8 53 2c 03 00            call     0x4383e4
00405791  83 c4 08                  add      esp, 8
00405794  ff 46 1c                  inc      dword ptr [esi + 0x1c]
00405797  66 c7 46 10 0c 00         mov      word ptr [esi + 0x10], 0xc
0040579d  ff 4e 1c                  dec      dword ptr [esi + 0x1c]
004057a0  6a 02                     push     2
004057a2  8d 4d fc                  lea      ecx, [ebp - 4]
004057a5  51                        push     ecx
004057a6  e8 b9 2d 03 00            call     0x438564
004057ab  83 c4 08                  add      esp, 8
004057ae  83 46 1c 02               add      dword ptr [esi + 0x1c], 2
004057b2  83 46 1c 03               add      dword ptr [esi + 0x1c], 3
004057b6  8d 45 f8                  lea      eax, [ebp - 8]
004057b9  50                        push     eax
004057ba  68 88 3b 40 00            push     0x403b88
004057bf  e8 e6 2c 03 00            call     0x4384aa
004057c4  83 c4 24                  add      esp, 0x24
004057c7  8b 7d b4                  mov      edi, dword ptr [ebp - 0x4c]
004057ca  8b 5d b0                  mov      ebx, dword ptr [ebp - 0x50]
004057cd  83 7b 09 00               cmp      dword ptr [ebx + 9], 0
004057d1  76 0b                     jbe      0x4057de
004057d3  83 7b 05 00               cmp      dword ptr [ebx + 5], 0
004057d7  74 05                     je       0x4057de
004057d9  3b 7b 09                  cmp      edi, dword ptr [ebx + 9]
004057dc  72 76                     jb       0x405854
004057de  56                        push     esi
004057df  6a 00                     push     0
004057e1  6a 00                     push     0
004057e3  6a 00                     push     0
004057e5  6a 01                     push     1
004057e7  68 e0 3b 40 00            push     0x403be0
004057ec  6a 00                     push     0
004057ee  68 3a 03 00 00            push     0x33a
004057f3  68 45 b3 43 00            push     0x43b345
004057f8  68 21 b3 43 00            push     0x43b321
004057fd  68 67 b3 43 00            push     0x43b367
00405802  8d 55 f4                  lea      edx, [ebp - 0xc]
00405805  52                        push     edx
00405806  e8 05 2d 03 00            call     0x438510
0040580b  83 c4 14                  add      esp, 0x14
0040580e  8d 4d f4                  lea      ecx, [ebp - 0xc]
00405811  51                        push     ecx
00405812  ff 46 1c                  inc      dword ptr [esi + 0x1c]
00405815  8d 45 f0                  lea      eax, [ebp - 0x10]
00405818  50                        push     eax
00405819  e8 c6 2b 03 00            call     0x4383e4
0040581e  83 c4 08                  add      esp, 8
00405821  ff 46 1c                  inc      dword ptr [esi + 0x1c]
00405824  66 c7 46 10 18 00         mov      word ptr [esi + 0x10], 0x18
0040582a  ff 4e 1c                  dec      dword ptr [esi + 0x1c]
0040582d  6a 02                     push     2
0040582f  8d 55 f4                  lea      edx, [ebp - 0xc]
00405832  52                        push     edx
00405833  e8 2c 2d 03 00            call     0x438564
00405838  83 c4 08                  add      esp, 8
0040583b  83 46 1c 02               add      dword ptr [esi + 0x1c], 2
0040583f  83 46 1c 03               add      dword ptr [esi + 0x1c], 3
00405843  8d 4d f0                  lea      ecx, [ebp - 0x10]
00405846  51                        push     ecx
00405847  68 88 3b 40 00            push     0x403b88
0040584c  e8 59 2c 03 00            call     0x4384aa
00405851  83 c4 24                  add      esp, 0x24
00405854  c1 e7 02                  shl      edi, 2
00405857  03 7b 05                  add      edi, dword ptr [ebx + 5]
0040585a  8b 07                     mov      eax, dword ptr [edi]
0040585c  89 45 c0                  mov      dword ptr [ebp - 0x40], eax
0040585f  ff 45 b4                  inc      dword ptr [ebp - 0x4c]
00405862  8b 55 c0                  mov      edx, dword ptr [ebp - 0x40]
00405865  8b da                     mov      ebx, edx
00405867  6a 00                     push     0
00405869  8d 4b 04                  lea      ecx, [ebx + 4]
0040586c  51                        push     ecx
0040586d  ff 75 08                  push     dword ptr [ebp + 8]
00405870  e8 a7 fb ff ff            call     0x40541c
00405875  83 c4 0c                  add      esp, 0xc
00405878  85 c0                     test     eax, eax
0040587a  74 11                     je       0x40588d
0040587c  8b d3                     mov      edx, ebx
0040587e  52                        push     edx
0040587f  50                        push     eax
00405880  e8 24 f5 ff ff            call     0x404da9
00405885  83 c4 08                  add      esp, 8
00405888  e9 9c 00 00 00            jmp      0x405929
0040588d  53                        push     ebx
0040588e  8b 03                     mov      eax, dword ptr [ebx]
00405890  ff 50 08                  call     dword ptr [eax + 8]
00405893  59                        pop      ecx
00405894  84 c0                     test     al, al
00405896  0f 84 8d 00 00 00         je       0x405929
0040589c  6a 10                     push     0x10
0040589e  e8 49 2c 03 00            call     0x4384ec
004058a3  59                        pop      ecx
004058a4  89 45 ec                  mov      dword ptr [ebp - 0x14], eax
004058a7  85 c0                     test     eax, eax
004058a9  74 41                     je       0x4058ec
004058ab  66 c7 46 10 30 00         mov      word ptr [esi + 0x10], 0x30
004058b1  8b fb                     mov      edi, ebx
004058b3  8b 55 ec                  mov      edx, dword ptr [ebp - 0x14]
004058b6  c7 02 54 b5 43 00         mov      dword ptr [edx], 0x43b554
004058bc  8b 4d ec                  mov      ecx, dword ptr [ebp - 0x14]
004058bf  83 c1 04                  add      ecx, 4
004058c2  51                        push     ecx
004058c3  e8 fa 2b 03 00            call     0x4384c2
004058c8  59                        pop      ecx
004058c9  ff 46 1c                  inc      dword ptr [esi + 0x1c]
004058cc  ff 75 ec                  push     dword ptr [ebp - 0x14]
004058cf  e8 69 f4 ff ff            call     0x404d3d
004058d4  59                        pop      ecx
004058d5  57                        push     edi
004058d6  ff 75 ec                  push     dword ptr [ebp - 0x14]
004058d9  e8 cb f4 ff ff            call     0x404da9
004058de  83 c4 08                  add      esp, 8
004058e1  66 c7 46 10 24 00         mov      word ptr [esi + 0x10], 0x24
004058e7  8b 45 ec                  mov      eax, dword ptr [ebp - 0x14]
004058ea  eb 03                     jmp      0x4058ef
004058ec  8b 45 ec                  mov      eax, dword ptr [ebp - 0x14]
004058ef  8b d8                     mov      ebx, eax
004058f1  8b fb                     mov      edi, ebx
004058f3  57                        push     edi
004058f4  8b 55 08                  mov      edx, dword ptr [ebp + 8]
004058f7  83 c2 04                  add      edx, 4
004058fa  52                        push     edx
004058fb  e8 49 07 00 00            call     0x406049
00405900  83 c4 08                  add      esp, 8
00405903  85 c0                     test     eax, eax
00405905  75 22                     jne      0x405929
00405907  89 5d e8                  mov      dword ptr [ebp - 0x18], ebx
0040590a  83 7d e8 00               cmp      dword ptr [ebp - 0x18], 0
0040590e  74 19                     je       0x405929
00405910  66 c7 46 10 48 00         mov      word ptr [esi + 0x10], 0x48
00405916  6a 03                     push     3
00405918  8b 4d e8                  mov      ecx, dword ptr [ebp - 0x18]
0040591b  51                        push     ecx
0040591c  8b 01                     mov      eax, dword ptr [ecx]
0040591e  ff 10                     call     dword ptr [eax]
00405920  83 c4 08                  add      esp, 8
00405923  66 c7 46 10 3c 00         mov      word ptr [esi + 0x10], 0x3c
00405929  8b 55 b4                  mov      edx, dword ptr [ebp - 0x4c]
0040592c  3b 55 bc                  cmp      edx, dword ptr [ebp - 0x44]
0040592f  0f 82 14 fe ff ff         jb       0x405749
00405935  8b 0e                     mov      ecx, dword ptr [esi]
00405937  64 89 0d 00 00 00 00      mov      dword ptr fs:[0], ecx
0040593e  5f                        pop      edi
0040593f  5e                        pop      esi
00405940  5b                        pop      ebx
00405941  8b e5                     mov      esp, ebp
00405943  5d                        pop      ebp
00405944  c3                        ret      
```

### Function Calls

**Other Calls**:

- `0040519f` → `sub_4061A2`
- `004051d9` → `sub_405F54`
- `00405211` → `sub_405F54`
- `00405268` → `sub_438510`
- `0040527b` → `sub_4383E4`
- `00405295` → `sub_438564`
- `004052ae` → `sub_4384AA`
- `004052fb` → `sub_438510`
- `0040530e` → `sub_4383E4`
- `00405328` → `sub_438564`
- `00405341` → `sub_4384AA`
- `00405370` → `sub_4384EC`
- `00405396` → `sub_4384C2`
- `004053a2` → `sub_404D3D`
- `004053ae` → `sub_404DA9`
- `004053d0` → `sub_406049`
- `0040542d` → `sub_402C18`
- `00405486` → `sub_438510`
- `00405499` → `sub_4383E4`
- `004054b3` → `sub_438564`
- ... and 32 more

---

