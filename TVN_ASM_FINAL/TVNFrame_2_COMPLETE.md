# TVNFrame_2 - Complete Assembly Extraction

**Vtable Address**: 0x00435DD4
**Binary**: europeo.exe
**Tool**: Capstone Disassembler
**Date**: 2026-01-16

---

## Methods Summary

| Index | Address |
|-------|----------|
|  0 | 0x0042D3BD |
|  1 | 0x00480001 |

---

## Method [0]: 0x0042D3BD

**Address**: 0x0042D3BD
**Index in vtable**: 0

**Size**: ~1761 bytes

### Assembly Code

```assembly
0042d3bd  00 83 c4 fc c7 04         add      byte ptr [ebx + 0x4c7fcc4], al
0042d3c3  24 cb                     and      al, 0xcb
0042d3c5  00 00                     add      byte ptr [eax], al
0042d3c7  00 8b 15 f1 ec 44         add      byte ptr [ebx + 0x44ecf115], cl
0042d3cd  00 ff                     add      bh, bh
0042d3cf  72 08                     jb       0x42d3d9
0042d3d1  ff 75 d4                  push     dword ptr [ebp - 0x2c]
0042d3d4  e8 1b f7 fe ff            call     0x41caf4
0042d3d9  83 c4 10                  add      esp, 0x10
0042d3dc  66 c7 45 c0 74 00         mov      word ptr [ebp - 0x40], 0x74
0042d3e2  8b 75 d4                  mov      esi, dword ptr [ebp - 0x2c]
0042d3e5  eb 03                     jmp      0x42d3ea
0042d3e7  8b 75 d4                  mov      esi, dword ptr [ebp - 0x2c]
0042d3ea  8b 45 dc                  mov      eax, dword ptr [ebp - 0x24]
0042d3ed  c7 00 dc 49 44 00         mov      dword ptr [eax], 0x4449dc
0042d3f3  8b 55 dc                  mov      edx, dword ptr [ebp - 0x24]
0042d3f6  89 72 04                  mov      dword ptr [edx + 4], esi
0042d3f9  8b 4d dc                  mov      ecx, dword ptr [ebp - 0x24]
0042d3fc  89 59 08                  mov      dword ptr [ecx + 8], ebx
0042d3ff  8b 45 dc                  mov      eax, dword ptr [ebp - 0x24]
0042d402  c7 40 0c 03 00 00 00      mov      dword ptr [eax + 0xc], 3
0042d409  8b 55 dc                  mov      edx, dword ptr [ebp - 0x24]
0042d40c  83 7a 04 00               cmp      dword ptr [edx + 4], 0
0042d410  75 7c                     jne      0x42d48e
0042d412  8d 4d b0                  lea      ecx, [ebp - 0x50]
0042d415  51                        push     ecx
0042d416  6a 00                     push     0
0042d418  6a 00                     push     0
0042d41a  6a 00                     push     0
0042d41c  6a 01                     push     1
0042d41e  68 e0 3b 40 00            push     0x403be0
0042d423  6a 00                     push     0
0042d425  6a 72                     push     0x72
0042d427  68 9b c5 44 00            push     0x44c59b
0042d42c  68 97 c5 44 00            push     0x44c597
0042d431  68 a6 c5 44 00            push     0x44c5a6
0042d436  8d 45 e4                  lea      eax, [ebp - 0x1c]
0042d439  50                        push     eax
0042d43a  e8 d1 b0 00 00            call     0x438510
0042d43f  83 c4 14                  add      esp, 0x14
0042d442  8d 55 e4                  lea      edx, [ebp - 0x1c]
0042d445  52                        push     edx
0042d446  ff 45 cc                  inc      dword ptr [ebp - 0x34]
0042d449  8d 4d e0                  lea      ecx, [ebp - 0x20]
0042d44c  51                        push     ecx
0042d44d  e8 92 af 00 00            call     0x4383e4
0042d452  83 c4 08                  add      esp, 8
0042d455  ff 45 cc                  inc      dword ptr [ebp - 0x34]
0042d458  66 c7 45 c0 98 00         mov      word ptr [ebp - 0x40], 0x98
0042d45e  ff 4d cc                  dec      dword ptr [ebp - 0x34]
0042d461  6a 02                     push     2
0042d463  8d 45 e4                  lea      eax, [ebp - 0x1c]
0042d466  50                        push     eax
0042d467  e8 f8 b0 00 00            call     0x438564
0042d46c  83 c4 08                  add      esp, 8
0042d46f  66 c7 45 c0 74 00         mov      word ptr [ebp - 0x40], 0x74
0042d475  83 45 cc 02               add      dword ptr [ebp - 0x34], 2
0042d479  83 45 cc 03               add      dword ptr [ebp - 0x34], 3
0042d47d  8d 55 e0                  lea      edx, [ebp - 0x20]
0042d480  52                        push     edx
0042d481  68 88 3b 40 00            push     0x403b88
0042d486  e8 1f b0 00 00            call     0x4384aa
0042d48b  83 c4 24                  add      esp, 0x24
0042d48e  66 c7 45 c0 68 00         mov      word ptr [ebp - 0x40], 0x68
0042d494  8b 4d dc                  mov      ecx, dword ptr [ebp - 0x24]
0042d497  eb 03                     jmp      0x42d49c
0042d499  8b 4d dc                  mov      ecx, dword ptr [ebp - 0x24]
0042d49c  89 0d a8 6a 44 00         mov      dword ptr [0x446aa8], ecx
0042d4a2  8b 07                     mov      eax, dword ptr [edi]
0042d4a4  a3 f0 a9 44 00            mov      dword ptr [0x44a9f0], eax
0042d4a9  8b 55 b0                  mov      edx, dword ptr [ebp - 0x50]
0042d4ac  64 89 15 00 00 00 00      mov      dword ptr fs:[0], edx
0042d4b3  8b 07                     mov      eax, dword ptr [edi]
0042d4b5  5f                        pop      edi
0042d4b6  5e                        pop      esi
0042d4b7  5b                        pop      ebx
0042d4b8  8b e5                     mov      esp, ebp
0042d4ba  5d                        pop      ebp
0042d4bb  c3                        ret      
0042d4bc  55                        push     ebp
0042d4bd  8b ec                     mov      ebp, esp
0042d4bf  83 c4 dc                  add      esp, -0x24
0042d4c2  53                        push     ebx
0042d4c3  8b 5d 0c                  mov      ebx, dword ptr [ebp + 0xc]
0042d4c6  b8 b0 ab 44 00            mov      eax, 0x44abb0
0042d4cb  e8 48 57 fd ff            call     0x402c18
0042d4d0  c7 45 f8 1e 00 00 00      mov      dword ptr [ebp - 8], 0x1e
0042d4d7  83 7d 08 00               cmp      dword ptr [ebp + 8], 0
0042d4db  0f 84 ec 00 00 00         je       0x42d5cd
0042d4e1  66 c7 45 ec 08 00         mov      word ptr [ebp - 0x14], 8
0042d4e7  8b 55 08                  mov      edx, dword ptr [ebp + 8]
0042d4ea  c7 42 08 6c d1 44 00      mov      dword ptr [edx + 8], 0x44d16c
0042d4f1  8b 4d 08                  mov      ecx, dword ptr [ebp + 8]
0042d4f4  8b 01                     mov      eax, dword ptr [ecx]
0042d4f6  c7 00 fc d1 44 00         mov      dword ptr [eax], 0x44d1fc
0042d4fc  8b 55 08                  mov      edx, dword ptr [ebp + 8]
0042d4ff  8b 4a 04                  mov      ecx, dword ptr [edx + 4]
0042d502  c7 01 08 d2 44 00         mov      dword ptr [ecx], 0x44d208
0042d508  33 c0                     xor      eax, eax
0042d50a  a3 f0 a9 44 00            mov      dword ptr [0x44a9f0], eax
0042d50f  6a 00                     push     0
0042d511  8b 55 08                  mov      edx, dword ptr [ebp + 8]
0042d514  52                        push     edx
0042d515  8b 4a 08                  mov      ecx, dword ptr [edx + 8]
0042d518  ff 51 10                  call     dword ptr [ecx + 0x10]
0042d51b  83 c4 08                  add      esp, 8
0042d51e  ff 4d f8                  dec      dword ptr [ebp - 8]
0042d521  6a 02                     push     2
0042d523  8b 45 08                  mov      eax, dword ptr [ebp + 8]
0042d526  05 9d 01 00 00            add      eax, 0x19d
0042d52b  50                        push     eax
0042d52c  e8 8c f4 ff ff            call     0x42c9bd
0042d531  83 c4 08                  add      esp, 8
0042d534  83 6d f8 08               sub      dword ptr [ebp - 8], 8
0042d538  6a 02                     push     2
0042d53a  8b 55 08                  mov      edx, dword ptr [ebp + 8]
0042d53d  81 c2 7c 01 00 00         add      edx, 0x17c
0042d543  52                        push     edx
0042d544  e8 d0 01 ff ff            call     0x41d719
0042d549  83 c4 08                  add      esp, 8
0042d54c  83 6d f8 12               sub      dword ptr [ebp - 8], 0x12
0042d550  6a 02                     push     2
0042d552  8b 4d 08                  mov      ecx, dword ptr [ebp + 8]
0042d555  81 c1 b6 00 00 00         add      ecx, 0xb6
0042d55b  51                        push     ecx
0042d55c  e8 37 16 ff ff            call     0x41eb98
0042d561  83 c4 08                  add      esp, 8
0042d564  ff 4d f8                  dec      dword ptr [ebp - 8]
0042d567  6a 02                     push     2
0042d569  8b 45 08                  mov      eax, dword ptr [ebp + 8]
0042d56c  05 8e 00 00 00            add      eax, 0x8e
0042d571  50                        push     eax
0042d572  e8 c1 7e 00 00            call     0x435438
0042d577  83 c4 08                  add      esp, 8
0042d57a  8b 55 08                  mov      edx, dword ptr [ebp + 8]
0042d57d  8b 0a                     mov      ecx, dword ptr [edx]
0042d57f  81 69 fc 23 01 00 00      sub      dword ptr [ecx - 4], 0x123
0042d586  83 6d f8 02               sub      dword ptr [ebp - 8], 2
0042d58a  6a 00                     push     0
0042d58c  ff 75 08                  push     dword ptr [ebp + 8]
0042d58f  e8 78 b6 00 00            call     0x438c0c
0042d594  83 c4 08                  add      esp, 8
0042d597  8b 45 08                  mov      eax, dword ptr [ebp + 8]
0042d59a  8b 10                     mov      edx, dword ptr [eax]
0042d59c  81 42 fc 23 01 00 00      add      dword ptr [edx - 4], 0x123
0042d5a3  f6 c3 02                  test     bl, 2
0042d5a6  74 17                     je       0x42d5bf
0042d5a8  ff 4d f8                  dec      dword ptr [ebp - 8]
0042d5ab  6a 00                     push     0
0042d5ad  8b 4d 08                  mov      ecx, dword ptr [ebp + 8]
0042d5b0  81 c1 b1 01 00 00         add      ecx, 0x1b1
0042d5b6  51                        push     ecx
0042d5b7  e8 10 b1 00 00            call     0x4386cc
0042d5bc  83 c4 08                  add      esp, 8
0042d5bf  f6 c3 01                  test     bl, 1
0042d5c2  74 09                     je       0x42d5cd
0042d5c4  ff 75 08                  push     dword ptr [ebp + 8]
0042d5c7  e8 4a af 00 00            call     0x438516
0042d5cc  59                        pop      ecx
0042d5cd  8b 45 dc                  mov      eax, dword ptr [ebp - 0x24]
0042d5d0  64 a3 00 00 00 00         mov      dword ptr fs:[0], eax
0042d5d6  5b                        pop      ebx
0042d5d7  8b e5                     mov      esp, ebp
0042d5d9  5d                        pop      ebp
0042d5da  c3                        ret      
0042d5db  55                        push     ebp
0042d5dc  8b ec                     mov      ebp, esp
0042d5de  83 c4 b8                  add      esp, -0x48
0042d5e1  53                        push     ebx
0042d5e2  56                        push     esi
0042d5e3  57                        push     edi
0042d5e4  8b 5d 08                  mov      ebx, dword ptr [ebp + 8]
0042d5e7  8d 75 c0                  lea      esi, [ebp - 0x40]
0042d5ea  b8 6c ac 44 00            mov      eax, 0x44ac6c
0042d5ef  e8 24 56 fd ff            call     0x402c18
0042d5f4  53                        push     ebx
0042d5f5  e8 3e b4 00 00            call     0x438a38
0042d5fa  59                        pop      ecx
0042d5fb  6a 23                     push     0x23
0042d5fd  e8 ea ae 00 00            call     0x4384ec
0042d602  59                        pop      ecx
0042d603  89 45 fc                  mov      dword ptr [ebp - 4], eax
0042d606  85 c0                     test     eax, eax
0042d608  74 1d                     je       0x42d627
0042d60a  66 c7 46 10 14 00         mov      word ptr [esi + 0x10], 0x14
0042d610  53                        push     ebx
0042d611  ff 75 fc                  push     dword ptr [ebp - 4]
0042d614  e8 76 d3 fe ff            call     0x41a98f
0042d619  83 c4 08                  add      esp, 8
0042d61c  66 c7 46 10 08 00         mov      word ptr [esi + 0x10], 8
0042d622  8b 55 fc                  mov      edx, dword ptr [ebp - 4]
0042d625  eb 03                     jmp      0x42d62a
0042d627  8b 55 fc                  mov      edx, dword ptr [ebp - 4]
0042d62a  89 93 9e 00 00 00         mov      dword ptr [ebx + 0x9e], edx
0042d630  6a 1f                     push     0x1f
0042d632  e8 b5 ae 00 00            call     0x4384ec
0042d637  59                        pop      ecx
0042d638  89 45 f8                  mov      dword ptr [ebp - 8], eax
0042d63b  85 c0                     test     eax, eax
0042d63d  74 1d                     je       0x42d65c
0042d63f  66 c7 46 10 2c 00         mov      word ptr [esi + 0x10], 0x2c
0042d645  53                        push     ebx
0042d646  ff 75 f8                  push     dword ptr [ebp - 8]
0042d649  e8 87 d7 fe ff            call     0x41add5
0042d64e  83 c4 08                  add      esp, 8
0042d651  66 c7 46 10 20 00         mov      word ptr [esi + 0x10], 0x20
0042d657  8b 4d f8                  mov      ecx, dword ptr [ebp - 8]
0042d65a  eb 03                     jmp      0x42d65f
0042d65c  8b 4d f8                  mov      ecx, dword ptr [ebp - 8]
0042d65f  89 8b a2 00 00 00         mov      dword ptr [ebx + 0xa2], ecx
0042d665  6a 1f                     push     0x1f
0042d667  e8 80 ae 00 00            call     0x4384ec
0042d66c  59                        pop      ecx
0042d66d  89 45 f0                  mov      dword ptr [ebp - 0x10], eax
0042d670  85 c0                     test     eax, eax
0042d672  74 6e                     je       0x42d6e2
0042d674  66 c7 46 10 44 00         mov      word ptr [esi + 0x10], 0x44
0042d67a  8b fb                     mov      edi, ebx
0042d67c  68 b3 c5 44 00            push     0x44c5b3
0042d681  8d 55 f4                  lea      edx, [ebp - 0xc]
0042d684  52                        push     edx
0042d685  e8 e4 ad 00 00            call     0x43846e
0042d68a  83 c4 08                  add      esp, 8
0042d68d  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0042d690  8d 45 f4                  lea      eax, [ebp - 0xc]
0042d693  50                        push     eax
0042d694  57                        push     edi
0042d695  ff 75 f0                  push     dword ptr [ebp - 0x10]
0042d698  e8 9b cc fe ff            call     0x41a338
0042d69d  83 c4 0c                  add      esp, 0xc
0042d6a0  83 46 1c 03               add      dword ptr [esi + 0x1c], 3
0042d6a4  8b 55 f0                  mov      edx, dword ptr [ebp - 0x10]
0042d6a7  c7 02 c8 40 44 00         mov      dword ptr [edx], 0x4440c8
0042d6ad  83 46 1c 04               add      dword ptr [esi + 0x1c], 4
0042d6b1  66 c7 46 10 50 00         mov      word ptr [esi + 0x10], 0x50
0042d6b7  ff 4e 1c                  dec      dword ptr [esi + 0x1c]
0042d6ba  6a 02                     push     2
0042d6bc  8d 4d f4                  lea      ecx, [ebp - 0xc]
0042d6bf  51                        push     ecx
0042d6c0  e8 9f ae 00 00            call     0x438564
0042d6c5  83 c4 08                  add      esp, 8
0042d6c8  66 c7 46 10 44 00         mov      word ptr [esi + 0x10], 0x44
0042d6ce  8b 45 f0                  mov      eax, dword ptr [ebp - 0x10]
0042d6d1  c7 00 f0 d0 44 00         mov      dword ptr [eax], 0x44d0f0
0042d6d7  66 c7 46 10 38 00         mov      word ptr [esi + 0x10], 0x38
0042d6dd  8b 55 f0                  mov      edx, dword ptr [ebp - 0x10]
0042d6e0  eb 03                     jmp      0x42d6e5
0042d6e2  8b 55 f0                  mov      edx, dword ptr [ebp - 0x10]
0042d6e5  89 93 a6 00 00 00         mov      dword ptr [ebx + 0xa6], edx
0042d6eb  68 c5 00 00 00            push     0xc5
0042d6f0  e8 f7 ad 00 00            call     0x4384ec
0042d6f5  59                        pop      ecx
0042d6f6  89 45 e8                  mov      dword ptr [ebp - 0x18], eax
0042d6f9  85 c0                     test     eax, eax
0042d6fb  0f 84 da 00 00 00         je       0x42d7db
0042d701  66 c7 46 10 68 00         mov      word ptr [esi + 0x10], 0x68
0042d707  89 5d bc                  mov      dword ptr [ebp - 0x44], ebx
0042d70a  8b 4d e8                  mov      ecx, dword ptr [ebp - 0x18]
0042d70d  81 c1 bd 00 00 00         add      ecx, 0xbd
0042d713  8b 45 e8                  mov      eax, dword ptr [ebp - 0x18]
0042d716  89 48 1f                  mov      dword ptr [eax + 0x1f], ecx
0042d719  8b 55 e8                  mov      edx, dword ptr [ebp - 0x18]
0042d71c  81 c2 c1 00 00 00         add      edx, 0xc1
0042d722  8b 4d e8                  mov      ecx, dword ptr [ebp - 0x18]
0042d725  89 51 23                  mov      dword ptr [ecx + 0x23], edx
0042d728  8b 45 e8                  mov      eax, dword ptr [ebp - 0x18]
0042d72b  33 d2                     xor      edx, edx
0042d72d  89 90 b9 00 00 00         mov      dword ptr [eax + 0xb9], edx
0042d733  8b 7d e8                  mov      edi, dword ptr [ebp - 0x18]
0042d736  81 c7 bd 00 00 00         add      edi, 0xbd
0042d73c  c7 07 30 40 44 00         mov      dword ptr [edi], 0x444030
0042d742  8b 45 e8                  mov      eax, dword ptr [ebp - 0x18]
0042d745  05 c1 00 00 00            add      eax, 0xc1
0042d74a  89 45 b8                  mov      dword ptr [ebp - 0x48], eax
0042d74d  8b 55 b8                  mov      edx, dword ptr [ebp - 0x48]
0042d750  c7 02 20 40 44 00         mov      dword ptr [edx], 0x444020
0042d756  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0042d759  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0042d75c  68 bb c5 44 00            push     0x44c5bb
0042d761  8d 4d ec                  lea      ecx, [ebp - 0x14]
0042d764  51                        push     ecx
0042d765  e8 04 ad 00 00            call     0x43846e
0042d76a  83 c4 08                  add      esp, 8
0042d76d  ff 46 1c                  inc      dword ptr [esi + 0x1c]
0042d770  8d 45 ec                  lea      eax, [ebp - 0x14]
0042d773  50                        push     eax
0042d774  ff 75 bc                  push     dword ptr [ebp - 0x44]
0042d777  6a 01                     push     1
0042d779  ff 75 e8                  push     dword ptr [ebp - 0x18]
0042d77c  e8 d6 d8 fe ff            call     0x41b057
0042d781  83 c4 10                  add      esp, 0x10
0042d784  83 46 1c 05               add      dword ptr [esi + 0x1c], 5
0042d788  66 c7 46 10 74 00         mov      word ptr [esi + 0x10], 0x74
0042d78e  ff 4e 1c                  dec      dword ptr [esi + 0x1c]
0042d791  6a 02                     push     2
0042d793  8d 55 ec                  lea      edx, [ebp - 0x14]
0042d796  52                        push     edx
0042d797  e8 c8 ad 00 00            call     0x438564
0042d79c  83 c4 08                  add      esp, 8
0042d79f  66 c7 46 10 68 00         mov      word ptr [esi + 0x10], 0x68
0042d7a5  8b 4d e8                  mov      ecx, dword ptr [ebp - 0x18]
0042d7a8  c7 01 0c d0 44 00         mov      dword ptr [ecx], 0x44d00c
0042d7ae  8b 45 e8                  mov      eax, dword ptr [ebp - 0x18]
0042d7b1  c7 40 27 50 d0 44 00      mov      dword ptr [eax + 0x27], 0x44d050
0042d7b8  8b 55 e8                  mov      edx, dword ptr [ebp - 0x18]
0042d7bb  8b 4a 1f                  mov      ecx, dword ptr [edx + 0x1f]
0042d7be  c7 01 d4 d0 44 00         mov      dword ptr [ecx], 0x44d0d4
0042d7c4  8b 45 e8                  mov      eax, dword ptr [ebp - 0x18]
0042d7c7  8b 50 23                  mov      edx, dword ptr [eax + 0x23]
0042d7ca  c7 02 e0 d0 44 00         mov      dword ptr [edx], 0x44d0e0
0042d7d0  66 c7 46 10 5c 00         mov      word ptr [esi + 0x10], 0x5c
0042d7d6  8b 4d e8                  mov      ecx, dword ptr [ebp - 0x18]
0042d7d9  eb 03                     jmp      0x42d7de
0042d7db  8b 4d e8                  mov      ecx, dword ptr [ebp - 0x18]
0042d7de  89 8b aa 00 00 00         mov      dword ptr [ebx + 0xaa], ecx
0042d7e4  8b 83 aa 00 00 00         mov      eax, dword ptr [ebx + 0xaa]
0042d7ea  83 c0 1f                  add      eax, 0x1f
0042d7ed  50                        push     eax
0042d7ee  8b 93 aa 00 00 00         mov      edx, dword ptr [ebx + 0xaa]
0042d7f4  8b 42 27                  mov      eax, dword ptr [edx + 0x27]
0042d7f7  ff 50 08                  call     dword ptr [eax + 8]
0042d7fa  59                        pop      ecx
0042d7fb  8b 93 9e 00 00 00         mov      edx, dword ptr [ebx + 0x9e]
0042d801  52                        push     edx
0042d802  8b 0a                     mov      ecx, dword ptr [edx]
0042d804  ff 51 04                  call     dword ptr [ecx + 4]
0042d807  59                        pop      ecx
0042d808  84 c0                     test     al, al
0042d80a  74 0a                     je       0x42d816
0042d80c  a1 44 ec 44 00            mov      eax, dword ptr [0x44ec44]
0042d811  83 c8 01                  or       eax, 1
0042d814  eb 08                     jmp      0x42d81e
0042d816  a1 44 ec 44 00            mov      eax, dword ptr [0x44ec44]
0042d81b  83 e0 fe                  and      eax, 0xfffffffe
0042d81e  a3 44 ec 44 00            mov      dword ptr [0x44ec44], eax
0042d823  8b 93 a2 00 00 00         mov      edx, dword ptr [ebx + 0xa2]
0042d829  52                        push     edx
0042d82a  8b 0a                     mov      ecx, dword ptr [edx]
0042d82c  ff 51 04                  call     dword ptr [ecx + 4]
0042d82f  59                        pop      ecx
0042d830  84 c0                     test     al, al
0042d832  74 0a                     je       0x42d83e
0042d834  a1 44 ec 44 00            mov      eax, dword ptr [0x44ec44]
0042d839  83 c8 02                  or       eax, 2
0042d83c  eb 08                     jmp      0x42d846
0042d83e  a1 44 ec 44 00            mov      eax, dword ptr [0x44ec44]
0042d843  83 e0 fd                  and      eax, 0xfffffffd
0042d846  a3 44 ec 44 00            mov      dword ptr [0x44ec44], eax
0042d84b  8b 93 aa 00 00 00         mov      edx, dword ptr [ebx + 0xaa]
0042d851  52                        push     edx
0042d852  8b 0a                     mov      ecx, dword ptr [edx]
0042d854  ff 51 04                  call     dword ptr [ecx + 4]
0042d857  59                        pop      ecx
0042d858  84 c0                     test     al, al
0042d85a  74 0a                     je       0x42d866
0042d85c  a1 44 ec 44 00            mov      eax, dword ptr [0x44ec44]
0042d861  83 c8 04                  or       eax, 4
0042d864  eb 08                     jmp      0x42d86e
0042d866  a1 44 ec 44 00            mov      eax, dword ptr [0x44ec44]
0042d86b  83 e0 fb                  and      eax, 0xfffffffb
0042d86e  a3 44 ec 44 00            mov      dword ptr [0x44ec44], eax
0042d873  6a 21                     push     0x21
0042d875  e8 72 ac 00 00            call     0x4384ec
0042d87a  59                        pop      ecx
0042d87b  89 45 e4                  mov      dword ptr [ebp - 0x1c], eax
0042d87e  85 c0                     test     eax, eax
0042d880  74 1f                     je       0x42d8a1
0042d882  66 c7 46 10 8c 00         mov      word ptr [esi + 0x10], 0x8c
0042d888  ff 73 0c                  push     dword ptr [ebx + 0xc]
0042d88b  ff 75 e4                  push     dword ptr [ebp - 0x1c]
0042d88e  e8 95 b2 00 00            call     0x438b28
0042d893  83 c4 08                  add      esp, 8
0042d896  66 c7 46 10 80 00         mov      word ptr [esi + 0x10], 0x80
0042d89c  8b 55 e4                  mov      edx, dword ptr [ebp - 0x1c]
0042d89f  eb 03                     jmp      0x42d8a4
0042d8a1  8b 55 e4                  mov      edx, dword ptr [ebp - 0x1c]
0042d8a4  89 93 86 00 00 00         mov      dword ptr [ebx + 0x86], edx
0042d8aa  8b 06                     mov      eax, dword ptr [esi]
0042d8ac  64 a3 00 00 00 00         mov      dword ptr fs:[0], eax
0042d8b2  5f                        pop      edi
0042d8b3  5e                        pop      esi
0042d8b4  5b                        pop      ebx
0042d8b5  8b e5                     mov      esp, ebp
0042d8b7  5d                        pop      ebp
0042d8b8  c3                        ret      
0042d8b9  55                        push     ebp
0042d8ba  8b ec                     mov      ebp, esp
0042d8bc  53                        push     ebx
0042d8bd  56                        push     esi
0042d8be  57                        push     edi
0042d8bf  8b 5d 0c                  mov      ebx, dword ptr [ebp + 0xc]
0042d8c2  8b 75 08                  mov      esi, dword ptr [ebp + 8]
0042d8c5  83 3b 00                  cmp      dword ptr [ebx], 0
0042d8c8  74 17                     je       0x42d8e1
0042d8ca  8b 3b                     mov      edi, dword ptr [ebx]
0042d8cc  57                        push     edi
0042d8cd  ff 76 0c                  push     dword ptr [esi + 0xc]
0042d8d0  e8 6b af 00 00            call     0x438840
0042d8d5  85 c0                     test     eax, eax
0042d8d7  0f 95 c0                  setne    al
0042d8da  83 e0 01                  and      eax, 1
0042d8dd  33 d2                     xor      edx, edx
0042d8df  89 13                     mov      dword ptr [ebx], edx
0042d8e1  5f                        pop      edi
0042d8e2  5e                        pop      esi
0042d8e3  5b                        pop      ebx
0042d8e4  5d                        pop      ebp
0042d8e5  c3                        ret      
0042d8e6  55                        push     ebp
0042d8e7  8b ec                     mov      ebp, esp
0042d8e9  83 c4 d4                  add      esp, -0x2c
0042d8ec  53                        push     ebx
0042d8ed  8b 5d 08                  mov      ebx, dword ptr [ebp + 8]
0042d8f0  b8 24 ad 44 00            mov      eax, 0x44ad24
0042d8f5  e8 1e 53 fd ff            call     0x402c18
0042d8fa  8d 93 78 01 00 00         lea      edx, [ebx + 0x178]
0042d900  52                        push     edx
0042d901  53                        push     ebx
0042d902  e8 b2 ff ff ff            call     0x42d8b9
0042d907  83 c4 08                  add      esp, 8
0042d90a  8b 8b 00 01 00 00         mov      ecx, dword ptr [ebx + 0x100]
0042d910  89 4d fc                  mov      dword ptr [ebp - 4], ecx
0042d913  83 7d fc 00               cmp      dword ptr [ebp - 4], 0
0042d917  74 19                     je       0x42d932
0042d919  66 c7 45 e4 14 00         mov      word ptr [ebp - 0x1c], 0x14
0042d91f  6a 03                     push     3
0042d921  8b 45 fc                  mov      eax, dword ptr [ebp - 4]
0042d924  50                        push     eax
0042d925  8b 10                     mov      edx, dword ptr [eax]
0042d927  ff 12                     call     dword ptr [edx]
0042d929  83 c4 08                  add      esp, 8
0042d92c  66 c7 45 e4 08 00         mov      word ptr [ebp - 0x1c], 8
0042d932  33 c9                     xor      ecx, ecx
0042d934  89 8b 00 01 00 00         mov      dword ptr [ebx + 0x100], ecx
0042d93a  8b 83 04 01 00 00         mov      eax, dword ptr [ebx + 0x104]
0042d940  89 45 f8                  mov      dword ptr [ebp - 8], eax
0042d943  83 7d f8 00               cmp      dword ptr [ebp - 8], 0
0042d947  74 19                     je       0x42d962
0042d949  66 c7 45 e4 2c 00         mov      word ptr [ebp - 0x1c], 0x2c
0042d94f  6a 03                     push     3
0042d951  8b 55 f8                  mov      edx, dword ptr [ebp - 8]
0042d954  52                        push     edx
0042d955  8b 0a                     mov      ecx, dword ptr [edx]
0042d957  ff 11                     call     dword ptr [ecx]
0042d959  83 c4 08                  add      esp, 8
0042d95c  66 c7 45 e4 20 00         mov      word ptr [ebp - 0x1c], 0x20
0042d962  33 c0                     xor      eax, eax
0042d964  89 83 04 01 00 00         mov      dword ptr [ebx + 0x104], eax
0042d96a  8b 55 d4                  mov      edx, dword ptr [ebp - 0x2c]
0042d96d  64 89 15 00 00 00 00      mov      dword ptr fs:[0], edx
0042d974  5b                        pop      ebx
0042d975  8b e5                     mov      esp, ebp
0042d977  5d                        pop      ebp
0042d978  c3                        ret      
0042d979  55                        push     ebp
0042d97a  8b ec                     mov      ebp, esp
0042d97c  53                        push     ebx
0042d97d  8b 5d 08                  mov      ebx, dword ptr [ebp + 8]
0042d980  83 bb 9e 00 00 00 00      cmp      dword ptr [ebx + 0x9e], 0
0042d987  74 0d                     je       0x42d996
0042d989  8b 83 9e 00 00 00         mov      eax, dword ptr [ebx + 0x9e]
0042d98f  50                        push     eax
0042d990  8b 10                     mov      edx, dword ptr [eax]
0042d992  ff 52 30                  call     dword ptr [edx + 0x30]
0042d995  59                        pop      ecx
0042d996  83 bb a2 00 00 00 00      cmp      dword ptr [ebx + 0xa2], 0
0042d99d  74 0d                     je       0x42d9ac
0042d99f  8b 8b a2 00 00 00         mov      ecx, dword ptr [ebx + 0xa2]
0042d9a5  51                        push     ecx
0042d9a6  8b 01                     mov      eax, dword ptr [ecx]
0042d9a8  ff 50 30                  call     dword ptr [eax + 0x30]
0042d9ab  59                        pop      ecx
0042d9ac  83 bb a6 00 00 00 00      cmp      dword ptr [ebx + 0xa6], 0
0042d9b3  74 0d                     je       0x42d9c2
0042d9b5  8b 93 a6 00 00 00         mov      edx, dword ptr [ebx + 0xa6]
0042d9bb  52                        push     edx
0042d9bc  8b 0a                     mov      ecx, dword ptr [edx]
0042d9be  ff 51 30                  call     dword ptr [ecx + 0x30]
0042d9c1  59                        pop      ecx
0042d9c2  83 bb aa 00 00 00 00      cmp      dword ptr [ebx + 0xaa], 0
0042d9c9  74 0d                     je       0x42d9d8
0042d9cb  8b 83 aa 00 00 00         mov      eax, dword ptr [ebx + 0xaa]
0042d9d1  50                        push     eax
0042d9d2  8b 10                     mov      edx, dword ptr [eax]
0042d9d4  ff 52 30                  call     dword ptr [edx + 0x30]
0042d9d7  59                        pop      ecx
0042d9d8  5b                        pop      ebx
0042d9d9  5d                        pop      ebp
0042d9da  c3                        ret      
0042d9db  55                        push     ebp
0042d9dc  8b ec                     mov      ebp, esp
0042d9de  83 c4 d0                  add      esp, -0x30
0042d9e1  53                        push     ebx
0042d9e2  8b 5d 08                  mov      ebx, dword ptr [ebp + 8]
0042d9e5  b8 8c ad 44 00            mov      eax, 0x44ad8c
0042d9ea  e8 29 52 fd ff            call     0x402c18
0042d9ef  53                        push     ebx
0042d9f0  e8 84 ff ff ff            call     0x42d979
0042d9f5  59                        pop      ecx
0042d9f6  53                        push     ebx
0042d9f7  e8 59 5b 00 00            call     0x433555
0042d9fc  59                        pop      ecx
0042d9fd  8b 93 ae 00 00 00         mov      edx, dword ptr [ebx + 0xae]
0042da03  89 55 fc                  mov      dword ptr [ebp - 4], edx
0042da06  83 7d fc 00               cmp      dword ptr [ebp - 4], 0
0042da0a  74 1a                     je       0x42da26
0042da0c  66 c7 45 e0 14 00         mov      word ptr [ebp - 0x20], 0x14
0042da12  6a 03                     push     3
0042da14  8b 4d fc                  mov      ecx, dword ptr [ebp - 4]
0042da17  51                        push     ecx
0042da18  8b 41 05                  mov      eax, dword ptr [ecx + 5]
0042da1b  ff 10                     call     dword ptr [eax]
0042da1d  83 c4 08                  add      esp, 8
0042da20  66 c7 45 e0 08 00         mov      word ptr [ebp - 0x20], 8
0042da26  33 d2                     xor      edx, edx
0042da28  89 93 ae 00 00 00         mov      dword ptr [ebx + 0xae], edx
0042da2e  8b 8b b2 00 00 00         mov      ecx, dword ptr [ebx + 0xb2]
0042da34  89 4d f8                  mov      dword ptr [ebp - 8], ecx
0042da37  83 7d f8 00               cmp      dword ptr [ebp - 8], 0
0042da3b  74 1a                     je       0x42da57
0042da3d  66 c7 45 e0 2c 00         mov      word ptr [ebp - 0x20], 0x2c
0042da43  6a 03                     push     3
0042da45  8b 45 f8                  mov      eax, dword ptr [ebp - 8]
0042da48  50                        push     eax
0042da49  8b 50 05                  mov      edx, dword ptr [eax + 5]
0042da4c  ff 12                     call     dword ptr [edx]
0042da4e  83 c4 08                  add      esp, 8
0042da51  66 c7 45 e0 20 00         mov      word ptr [ebp - 0x20], 0x20
0042da57  33 c9                     xor      ecx, ecx
0042da59  89 8b b2 00 00 00         mov      dword ptr [ebx + 0xb2], ecx
0042da5f  8b 83 fc 00 00 00         mov      eax, dword ptr [ebx + 0xfc]
0042da65  89 45 f4                  mov      dword ptr [ebp - 0xc], eax
0042da68  83 7d f4 00               cmp      dword ptr [ebp - 0xc], 0
0042da6c  74 19                     je       0x42da87
0042da6e  66 c7 45 e0 44 00         mov      word ptr [ebp - 0x20], 0x44
0042da74  6a 03                     push     3
0042da76  8b 55 f4                  mov      edx, dword ptr [ebp - 0xc]
0042da79  52                        push     edx
0042da7a  8b 0a                     mov      ecx, dword ptr [edx]
0042da7c  ff 11                     call     dword ptr [ecx]
0042da7e  83 c4 08                  add      esp, 8
0042da81  66 c7 45 e0 38 00         mov      word ptr [ebp - 0x20], 0x38
0042da87  33 c0                     xor      eax, eax
0042da89  89 83 fc 00 00 00         mov      dword ptr [ebx + 0xfc], eax
0042da8f  8b 55 d0                  mov      edx, dword ptr [ebp - 0x30]
0042da92  64 89 15 00 00 00 00      mov      dword ptr fs:[0], edx
0042da99  5b                        pop      ebx
0042da9a  8b e5                     mov      esp, ebp
0042da9c  5d                        pop      ebp
0042da9d  c3                        ret      
```

### String References

- `0042d7b1` → `0x0044d050`: "xception"

### Function Calls

**Other Calls**:

- `0042d3d4` → `sub_41CAF4`
- `0042d43a` → `sub_438510`
- `0042d44d` → `sub_4383E4`
- `0042d467` → `sub_438564`
- `0042d486` → `sub_4384AA`
- `0042d4cb` → `sub_402C18`
- `0042d52c` → `sub_42C9BD`
- `0042d544` → `sub_41D719`
- `0042d55c` → `sub_41EB98`
- `0042d572` → `sub_435438`
- `0042d58f` → `sub_438C0C`
- `0042d5b7` → `sub_4386CC`
- `0042d5c7` → `sub_438516`
- `0042d5ef` → `sub_402C18`
- `0042d5f5` → `sub_438A38`
- `0042d5fd` → `sub_4384EC`
- `0042d614` → `sub_41A98F`
- `0042d632` → `sub_4384EC`
- `0042d649` → `sub_41ADD5`
- `0042d667` → `sub_4384EC`
- ... and 15 more

---

## Method [1]: 0x00480001

**Address**: 0x00480001
**Index in vtable**: 1

**Size**: ~500 bytes

### Assembly Code

```assembly
00480001  f2 f3 f5                  cmc      
00480004  f4                        hlt      
00480005  f4                        hlt      
00480006  f4                        hlt      
00480007  f4                        hlt      
```

---

