# TVNHotspot - Complete Assembly Extraction

**Vtable Address**: 0x00413514
**Binary**: europeo.exe
**Tool**: Capstone Disassembler
**Date**: 2026-01-16

---

## Methods Summary

| Index | Address |
|-------|----------|
|  0 | 0x00440460 |
|  1 | 0x00440090 |

---

## Method [0]: 0x00440460

**Address**: 0x00440460
**Index in vtable**: 0

**Size**: ~500 bytes

### Assembly Code

```assembly
00440460  00 30                     add      byte ptr [eax], dh
00440462  2c 30                     sub      al, 0x30
00440464  2c 30                     sub      al, 0x30
00440466  2c 30                     sub      al, 0x30
00440468  00 25 69 2c 25 69         add      byte ptr [0x69252c69], ah
0044046e  2c 25                     sub      al, 0x25
00440470  69 2c 25 69 00 20 25 75 20 25 69  imul     ebp, dword ptr [0x25200069], 0x69252075
0044047b  20 25 69 20 25 69         and      byte ptr [0x69252069], ah
00440481  20 25 69 00 25 75         and      byte ptr [0x75250069], ah
00440487  00 00                     add      byte ptr [eax], al
00440489  4c                        dec      esp
0044048a  69 6d 20 3d 3d 20 30      imul     ebp, dword ptr [ebp + 0x20], 0x30203d3d
00440491  20 7c 7c 20               and      byte ptr [esp + edi*2 + 0x20], bh
00440495  44                        inc      esp
00440496  61                        popal    
00440497  74 61                     je       0x4404fa
00440499  20 21                     and      byte ptr [ecx], ah
0044049b  3d 20 30 20 26            cmp      eax, 0x26203020
004404a0  26 20 69 6e               and      byte ptr es:[ecx + 0x6e], ch
004404a4  64 65 78 20               js       0x4404c8
004404a8  3c 20                     cmp      al, 0x20
004404aa  4c                        dec      esp
004404ab  69 6d 00 43 3a 5c 42      imul     ebp, dword ptr [ebp], 0x425c3a43
004404b2  43                        inc      ebx
004404b3  35 5c 49 4e 43            xor      eax, 0x434e495c
004404b8  4c                        dec      esp
004404b9  55                        push     ebp
004404ba  44                        inc      esp
004404bb  45                        inc      ebp
004404bc  5c                        pop      esp
004404bd  63 6c 61 73               arpl     word ptr [ecx + 0x73], bp
004404c1  73 6c                     jae      0x44052f
004404c3  69 62 2f 76 65 63 74      imul     esp, dword ptr [edx + 0x2f], 0x74636576
004404ca  69 6d 70 2e 68 00 50      imul     ebp, dword ptr [ebp + 0x70], 0x5000682e
004404d1  72 65                     jb       0x440538
004404d3  63 6f 6e                  arpl     word ptr [edi + 0x6e], bp
004404d6  64 69 74 69 6f 6e 00 43 75  imul     esi, dword ptr fs:[ecx + ebp*2 + 0x6f], 0x7543006e
004404df  72 20                     jb       0x440501
004404e1  3c 20                     cmp      al, 0x20
004404e3  55                        push     ebp
004404e4  70 70                     jo       0x440556
004404e6  65 72 00                  jb       0x4404e9
004404e9  43                        inc      ebx
004404ea  3a 5c 42 43               cmp      bl, byte ptr [edx + eax*2 + 0x43]
004404ee  35 5c 49 4e 43            xor      eax, 0x434e495c
004404f3  4c                        dec      esp
004404f4  55                        push     ebp
004404f5  44                        inc      esp
004404f6  45                        inc      ebp
004404f7  5c                        pop      esp
004404f8  63 6c 61 73               arpl     word ptr [ecx + 0x73], bp
004404fc  73 6c                     jae      0x44056a
004404fe  69 62 2f 76 65 63 74      imul     esp, dword ptr [edx + 0x2f], 0x74636576
00440505  69 6d 70 2e 68 00 50      imul     ebp, dword ptr [ebp + 0x70], 0x5000682e
0044050c  72 65                     jb       0x440573
0044050e  63 6f 6e                  arpl     word ptr [edi + 0x6e], bp
00440511  64 69 74 69 6f 6e 00 4c 69  imul     esi, dword ptr fs:[ecx + ebp*2 + 0x6f], 0x694c006e
0044051a  6d                        insd     dword ptr es:[edi], dx
0044051b  20 3e                     and      byte ptr [esi], bh
0044051d  20 30                     and      byte ptr [eax], dh
0044051f  20 26                     and      byte ptr [esi], ah
00440521  26 20 44 61 74            and      byte ptr es:[ecx + 0x74], al
00440526  61                        popal    
00440527  20 21                     and      byte ptr [ecx], ah
00440529  3d 20 30 20 26            cmp      eax, 0x26203020
0044052e  26 20 69 6e               and      byte ptr es:[ecx + 0x6e], ch
00440532  64 65 78 20               js       0x440556
00440536  3c 20                     cmp      al, 0x20
00440538  4c                        dec      esp
00440539  69 6d 00 43 3a 5c 42      imul     ebp, dword ptr [ebp], 0x425c3a43
00440540  43                        inc      ebx
00440541  35 5c 49 4e 43            xor      eax, 0x434e495c
00440546  4c                        dec      esp
00440547  55                        push     ebp
00440548  44                        inc      esp
00440549  45                        inc      ebp
0044054a  5c                        pop      esp
0044054b  63 6c 61 73               arpl     word ptr [ecx + 0x73], bp
0044054f  73 6c                     jae      0x4405bd
00440551  69 62 2f 76 65 63 74      imul     esp, dword ptr [edx + 0x2f], 0x74636576
00440558  69 6d 70 2e 68 00 50      imul     ebp, dword ptr [ebp + 0x70], 0x5000682e
0044055f  72 65                     jb       0x4405c6
00440561  63 6f 6e                  arpl     word ptr [edi + 0x6e], bp
00440564  64 69 74 69 6f 6e 00 6c 6f  imul     esi, dword ptr fs:[ecx + ebp*2 + 0x6f], 0x6f6c006e
0044056d  63 20                     arpl     word ptr [eax], sp
0044056f  3e 3d 20 4c 6f 77         cmp      eax, 0x776f4c20
00440575  65 72 62                  jb       0x4405da
00440578  6f                        outsd    dx, dword ptr [esi]
00440579  75 6e                     jne      0x4405e9
0044057b  64 20 26                  and      byte ptr fs:[esi], ah
0044057e  26 20 5a 65               and      byte ptr es:[edx + 0x65], bl
00440582  72 6f                     jb       0x4405f3
00440584  42                        inc      edx
00440585  61                        popal    
00440586  73 65                     jae      0x4405ed
00440588  28 6c 6f 63               sub      byte ptr [edi + ebp*2 + 0x63], ch
0044058c  29 20                     sub      dword ptr [eax], esp
0044058e  3c 20                     cmp      al, 0x20
00440590  44                        inc      esp
00440591  61                        popal    
00440592  74 61                     je       0x4405f5
00440594  2e 4c                     dec      esp
00440596  69 6d 69 74 28 29 00      imul     ebp, dword ptr [ebp + 0x69], 0x292874
0044059d  43                        inc      ebx
0044059e  3a 5c 42 43               cmp      bl, byte ptr [edx + eax*2 + 0x43]
004405a2  35 5c 49 4e 43            xor      eax, 0x434e495c
004405a7  4c                        dec      esp
004405a8  55                        push     ebp
004405a9  44                        inc      esp
004405aa  45                        inc      ebp
004405ab  5c                        pop      esp
004405ac  63 6c 61 73               arpl     word ptr [ecx + 0x73], bp
004405b0  73 6c                     jae      0x44061e
004405b2  69 62 2f 61 72 72 61      imul     esp, dword ptr [edx + 0x2f], 0x61727261
004405b9  79 73                     jns      0x44062e
004405bb  2e 68 00 50 72 65         push     0x65725000
004405c1  63 6f 6e                  arpl     word ptr [edi + 0x6e], bp
004405c4  64 69 74 69 6f 6e 00 4c 69  imul     esi, dword ptr fs:[ecx + ebp*2 + 0x6f], 0x694c006e
004405cd  6d                        insd     dword ptr es:[edi], dx
004405ce  20 3e                     and      byte ptr [esi], bh
004405d0  20 30                     and      byte ptr [eax], dh
004405d2  20 26                     and      byte ptr [esi], ah
004405d4  26 20 44 61 74            and      byte ptr es:[ecx + 0x74], al
004405d9  61                        popal    
004405da  20 21                     and      byte ptr [ecx], ah
004405dc  3d 20 30 20 26            cmp      eax, 0x26203020
004405e1  26 20 69 6e               and      byte ptr es:[ecx + 0x6e], ch
004405e5  64 65 78 20               js       0x440609
004405e9  3c 20                     cmp      al, 0x20
004405eb  4c                        dec      esp
004405ec  69 6d 00 43 3a 5c 42      imul     ebp, dword ptr [ebp], 0x425c3a43
004405f3  43                        inc      ebx
004405f4  35 5c 49 4e 43            xor      eax, 0x434e495c
004405f9  4c                        dec      esp
004405fa  55                        push     ebp
004405fb  44                        inc      esp
004405fc  45                        inc      ebp
004405fd  5c                        pop      esp
004405fe  63 6c 61 73               arpl     word ptr [ecx + 0x73], bp
00440602  73 6c                     jae      0x440670
00440604  69 62 2f 76 65 63 74      imul     esp, dword ptr [edx + 0x2f], 0x74636576
0044060b  69 6d 70 2e 68 00 50      imul     ebp, dword ptr [ebp + 0x70], 0x5000682e
00440612  72 65                     jb       0x440679
00440614  63 6f 6e                  arpl     word ptr [edi + 0x6e], bp
00440617  64 69 74 69 6f 6e 00 48 53  imul     esi, dword ptr fs:[ecx + ebp*2 + 0x6f], 0x5348006e
00440620  4e                        dec      esi
00440621  55                        push     ebp
00440622  4d                        dec      ebp
00440623  00 4e 48                  add      byte ptr [esi + 0x48], cl
00440626  4f                        dec      edi
00440627  54                        push     esp
00440628  53                        push     ebx
00440629  50                        push     eax
0044062a  4f                        dec      edi
0044062b  54                        push     esp
0044062c  00 4c 69 6d               add      byte ptr [ecx + ebp*2 + 0x6d], cl
00440630  20 3d 3d 20 30 20         and      byte ptr [0x2030203d], bh
00440636  7c 7c                     jl       0x4406b4
00440638  20 28                     and      byte ptr [eax], ch
0044063a  44                        inc      esp
0044063b  61                        popal    
0044063c  74 61                     je       0x44069f
0044063e  20 21                     and      byte ptr [ecx], ah
00440640  3d 20 30 20 26            cmp      eax, 0x26203020
00440645  26 20 76 2e               and      byte ptr es:[esi + 0x2e], dh
00440649  44                        inc      esp
0044064a  61                        popal    
0044064b  74 61                     je       0x4406ae
0044064d  20 21                     and      byte ptr [ecx], ah
0044064f  3d 20 30 29 00            cmp      eax, 0x293020
```

---

## Method [1]: 0x00440090

**Address**: 0x00440090
**Index in vtable**: 1

**Size**: ~500 bytes

### Assembly Code

```assembly
00440090  08 00                     or       byte ptr [eax], al
00440092  05 00 00 00 00            add      eax, 0
00440097  00 6c 10 44               add      byte ptr [eax + edx + 0x44], ch
0044009b  00 00                     add      byte ptr [eax], al
0044009d  00 00                     add      byte ptr [eax], al
0044009f  00 dc                     add      ah, bl
```

---

