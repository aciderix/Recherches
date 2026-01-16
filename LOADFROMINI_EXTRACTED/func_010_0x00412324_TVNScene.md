# LoadFromINI Function Analysis

**Function Address**: 0x00412324
**Rank**: #10
**INI String Count**: 13
**Identified Structure**: TVNScene
**Confidence Score**: 1

---

## Assembly Code

**Instructions**: 1003

```assembly
00412324  push     ebp
00412325  mov      ebp, esp
00412327  add      esp, 0xfffffccc
0041232D  push     ebx
0041232E  push     esi
0041232F  push     edi
00412330  mov      ebx, dword ptr [ebp + 8]
00412333  lea      esi, [ebp - 0xec]
00412339  mov      eax, 0x440800
0041233E  call     0x403618
00412343  push     ebx
00412344  mov      edx, dword ptr [ebx]
00412346  call     dword ptr [edx + 0xc]
00412349  pop      ecx
0041234A  mov      word ptr [esi + 0x10], 8
00412350  push     dword ptr [ebp + 0x14]
00412353  push     dword ptr [ebp + 0xc]
00412356  lea      ecx, [ebp - 8]
00412359  push     ecx
0041235A  call     0x4390c0
0041235F  add      esp, 0xc
00412362  inc      dword ptr [esi + 0x1c]
00412365  mov      word ptr [esi + 0x10], 0x14
0041236B  mov      dword ptr [ebx + 0x2d], 0xffffffff
00412372  push     dword ptr [ebp + 0x10]
00412375  push     0x4412ec
0041237A  lea      eax, [ebp - 0x224]
00412380  push     eax
00412381  call     0x43929a
00412386  add      esp, 0xc
00412389  push     0x4412f5
0041238E  push     0x100
00412393  lea      edx, [ebp - 0x324]
00412399  push     edx
0041239A  lea      ecx, [ebp - 0x224]
004123A0  push     ecx
004123A1  lea      eax, [ebp - 8]
004123A4  push     eax
004123A5  call     0x4390a2
004123AA  add      esp, 0x14
004123AD  test     al, al
004123AF  je       0x4123ca
004123B1  push     0
004123B3  lea      edx, [ebp - 0x324]
004123B9  push     edx
004123BA  push     0x440460
004123BF  call     0x403a55
004123C4  add      esp, 0xc
004123C7  mov      dword ptr [ebx + 0x2d], eax
004123CA  cmp      dword ptr [ebx + 0x2d], 0
004123CE  jge      0x4123d9
004123D0  mov      dword ptr [ebx + 0x2d], 0x64
004123D7  jmp      0x4123dd
004123D9  add      dword ptr [ebx + 0x2d], 0x64
004123DD  push     dword ptr [ebp + 0x10]
004123E0  push     0x4412f6
004123E5  lea      ecx, [ebp - 0x224]
004123EB  push     ecx
004123EC  call     0x43929a
004123F1  add      esp, 0xc
004123F4  push     0x4412ff
004123F9  push     0x100
004123FE  lea      eax, [ebp - 0x324]
00412404  push     eax
00412405  lea      edx, [ebp - 0x224]
0041240B  push     edx
0041240C  lea      ecx, [ebp - 8]
0041240F  push     ecx
00412410  call     0x4390a2
00412415  add      esp, 0x14
00412418  cmp      byte ptr [ebp - 0x324], 0
0041241F  je       0x412745
00412425  push     0x441300
0041242A  lea      eax, [ebp - 0x324]
00412430  push     eax
00412431  call     0x438e74
00412436  add      esp, 8
00412439  mov      edi, eax
0041243B  test     edi, edi
0041243D  jne      0x4124c5
00412443  push     esi
00412444  push     0
00412446  push     0
00412448  push     0
0041244A  push     1
0041244C  push     0x40690f
00412451  push     0
00412453  mov      word ptr [esi + 0x10], 0x20
00412459  push     0xd1
0041245E  push     0x44130e
00412463  push     0x441302
00412468  push     0x44131a
0041246D  lea      eax, [ebp - 0xc]
00412470  push     eax
00412471  call     0x438f10
00412476  add      esp, 0x14
00412479  lea      edx, [ebp - 0xc]
0041247C  push     edx
0041247D  inc      dword ptr [esi + 0x1c]
00412480  lea      ecx, [ebp - 0x10]
00412483  push     ecx
00412484  call     0x438de4
00412489  add      esp, 8
0041248C  inc      dword ptr [esi + 0x1c]
0041248F  mov      word ptr [esi + 0x10], 0x2c
00412495  dec      dword ptr [esi + 0x1c]
00412498  push     2
0041249A  lea      eax, [ebp - 0xc]
0041249D  push     eax
0041249E  call     0x438f64
004124A3  add      esp, 8
004124A6  mov      word ptr [esi + 0x10], 0x20
004124AC  add      dword ptr [esi + 0x1c], 2
004124B0  add      dword ptr [esi + 0x1c], 3
004124B4  lea      edx, [ebp - 0x10]
004124B7  push     edx
004124B8  push     0x4068bf
004124BD  call     0x438eaa
004124C2  add      esp, 0x24
004124C5  mov      dword ptr [ebp - 0xf4], edi
004124CB  push     dword ptr [ebp - 0xf4]
004124D1  call     0x438eb0
004124D6  pop      ecx
004124D7  mov      dword ptr [ebx + 0x35], eax
004124DA  cmp      dword ptr [ebx + 0x35], 1
004124DE  jbe      0x412740
004124E4  cmp      dword ptr [ebx + 0x39], 0
004124E8  je       0x412570
004124EE  push     esi
004124EF  push     0
004124F1  push     0
004124F3  push     0
004124F5  push     1
004124F7  push     0x40690f
004124FC  push     0
004124FE  mov      word ptr [esi + 0x10], 0x38
00412504  push     0xd4
00412509  push     0x44132f
0041250E  push     0x441320
00412513  push     0x44133b
00412518  lea      ecx, [ebp - 0x14]
0041251B  push     ecx
0041251C  call     0x438f10
00412521  add      esp, 0x14
00412524  lea      eax, [ebp - 0x14]
00412527  push     eax
00412528  inc      dword ptr [esi + 0x1c]
0041252B  lea      edx, [ebp - 0x18]
0041252E  push     edx
0041252F  call     0x438de4
00412534  add      esp, 8
00412537  inc      dword ptr [esi + 0x1c]
0041253A  mov      word ptr [esi + 0x10], 0x44
00412540  dec      dword ptr [esi + 0x1c]
00412543  push     2
00412545  lea      ecx, [ebp - 0x14]
00412548  push     ecx
00412549  call     0x438f64
0041254E  add      esp, 8
00412551  mov      word ptr [esi + 0x10], 0x38
00412557  add      dword ptr [esi + 0x1c], 2
0041255B  add      dword ptr [esi + 0x1c], 3
0041255F  lea      eax, [ebp - 0x18]
00412562  push     eax
00412563  push     0x4068bf
00412568  call     0x438eaa
0041256D  add      esp, 0x24
00412570  push     0
00412572  push     0
00412574  push     0x413fc9
00412579  push     1
0041257B  push     dword ptr [ebx + 0x35]
0041257E  push     8
00412580  push     0
00412582  call     0x4037e0
00412587  add      esp, 0x1c
0041258A  mov      dword ptr [ebx + 0x39], eax
0041258D  mov      word ptr [esi + 0x10], 0x14
00412593  xor      edx, edx
00412595  mov      dword ptr [ebp - 0xf0], edx
0041259B  jmp      0x412728
004125A0  push     0x441341
004125A5  push     0
004125A7  call     0x438e74
004125AC  add      esp, 8
004125AF  mov      edi, eax
004125B1  test     edi, edi
004125B3  jne      0x41263b
004125B9  push     esi
004125BA  push     0
004125BC  push     0
004125BE  push     0
004125C0  push     1
004125C2  push     0x40690f
004125C7  push     0
004125C9  mov      word ptr [esi + 0x10], 0x50
004125CF  push     0xd9
004125D4  push     0x44134f
004125D9  push     0x441343
004125DE  push     0x44135b
004125E3  lea      eax, [ebp - 0x1c]
004125E6  push     eax
004125E7  call     0x438f10
004125EC  add      esp, 0x14
004125EF  lea      edx, [ebp - 0x1c]
004125F2  push     edx
004125F3  inc      dword ptr [esi + 0x1c]
004125F6  lea      ecx, [ebp - 0x20]
004125F9  push     ecx
004125FA  call     0x438de4
004125FF  add      esp, 8
00412602  inc      dword ptr [esi + 0x1c]
00412605  mov      word ptr [esi + 0x10], 0x5c
0041260B  dec      dword ptr [esi + 0x1c]
0041260E  push     2
00412610  lea      eax, [ebp - 0x1c]
00412613  push     eax
00412614  call     0x438f64
00412619  add      esp, 8
0041261C  mov      word ptr [esi + 0x10], 0x50
00412622  add      dword ptr [esi + 0x1c], 2
00412626  add      dword ptr [esi + 0x1c], 3
0041262A  lea      edx, [ebp - 0x20]
0041262D  push     edx
0041262E  push     0x4068bf
00412633  call     0x438eaa
00412638  add      esp, 0x24
0041263B  mov      dword ptr [ebp - 0x100], edi
00412641  push     dword ptr [ebp - 0x100]
00412647  call     0x438eb0
0041264C  pop      ecx
0041264D  mov      dword ptr [ebp - 0xfc], eax
00412653  push     0x441361
00412658  push     0
0041265A  call     0x438e74
0041265F  add      esp, 8
00412662  mov      edi, eax
00412664  test     edi, edi
00412666  jne      0x4126ee
0041266C  push     esi
0041266D  push     0
0041266F  push     0
00412671  push     0
00412673  push     1
00412675  push     0x40690f
0041267A  push     0
0041267C  mov      word ptr [esi + 0x10], 0x68
00412682  push     0xdc
00412687  push     0x44136f
0041268C  push     0x441363
00412691  push     0x44137b
00412696  lea      eax, [ebp - 0x24]
00412699  push     eax
0041269A  call     0x438f10
0041269F  add      esp, 0x14
004126A2  lea      edx, [ebp - 0x24]
004126A5  push     edx
004126A6  inc      dword ptr [esi + 0x1c]
004126A9  lea      ecx, [ebp - 0x28]
004126AC  push     ecx
004126AD  call     0x438de4
004126B2  add      esp, 8
004126B5  inc      dword ptr [esi + 0x1c]
004126B8  mov      word ptr [esi + 0x10], 0x74
004126BE  dec      dword ptr [esi + 0x1c]
004126C1  push     2
004126C3  lea      eax, [ebp - 0x24]
004126C6  push     eax
004126C7  call     0x438f64
004126CC  add      esp, 8
004126CF  mov      word ptr [esi + 0x10], 0x68
004126D5  add      dword ptr [esi + 0x1c], 2
004126D9  add      dword ptr [esi + 0x1c], 3
004126DD  lea      edx, [ebp - 0x28]
004126E0  push     edx
004126E1  push     0x4068bf
004126E6  call     0x438eaa
004126EB  add      esp, 0x24
004126EE  mov      dword ptr [ebp - 0x104], edi
004126F4  push     dword ptr [ebp - 0x104]
004126FA  call     0x438eb0
004126FF  pop      ecx
00412700  mov      dword ptr [ebp - 0xf8], eax
00412706  mov      ecx, dword ptr [ebx + 0x39]
00412709  mov      eax, dword ptr [ebp - 0xf0]
0041270F  mov      edx, dword ptr [ebp - 0xfc]
00412715  mov      dword ptr [ecx + eax*8], edx
00412718  mov      edx, dword ptr [ebp - 0xf8]
0041271E  mov      dword ptr [ecx + eax*8 + 4], edx
00412722  inc      dword ptr [ebp - 0xf0]
00412728  mov      ecx, dword ptr [ebp - 0xf0]
0041272E  cmp      ecx, dword ptr [ebx + 0x35]
00412731  jb       0x4125a0
00412737  push     ebx
00412738  call     0x412168
0041273D  pop      ecx
0041273E  jmp      0x412745
00412740  xor      eax, eax
00412742  mov      dword ptr [ebx + 0x35], eax
00412745  push     dword ptr [ebp + 0x10]
00412748  push     0x441381
0041274D  lea      edx, [ebp - 0x224]
00412753  push     edx
00412754  call     0x43929a
00412759  add      esp, 0xc
0041275C  push     dword ptr [ebp + 0x14]
0041275F  lea      ecx, [ebp - 0x224]
00412765  push     ecx
00412766  push     dword ptr [ebp + 0xc]
00412769  lea      eax, [ebx + 8]
0041276C  push     eax
0041276D  call     0x40e6fc
00412772  add      esp, 0x10
00412775  push     dword ptr [ebp + 0x10]
00412778  push     0x44138a
0041277D  lea      edx, [ebp - 0x224]
00412783  push     edx
00412784  call     0x43929a
00412789  add      esp, 0xc
0041278C  mov      dword ptr [ebp - 0x108], 0xffffffff
00412796  mov      word ptr [esi + 0x10], 0x14
0041279C  push     0x441395
004127A1  push     0x100
004127A6  lea      ecx, [ebp - 0x324]
004127AC  push     ecx
004127AD  lea      eax, [ebp - 0x224]
004127B3  push     eax
004127B4  lea      edx, [ebp - 8]
004127B7  push     edx
004127B8  call     0x4390a2
004127BD  add      esp, 0x14
004127C0  test     al, al
004127C2  je       0x412bcc
004127C8  push     0x441396
004127CD  lea      ecx, [ebp - 0x324]
004127D3  push     ecx
004127D4  call     0x438e74
004127D9  add      esp, 8
004127DC  mov      edi, eax
004127DE  test     edi, edi
004127E0  jne      0x412868
004127E6  push     esi
004127E7  push     0
004127E9  push     0
004127EB  push     0
004127ED  push     1
004127EF  push     0x40690f
004127F4  push     0
004127F6  mov      word ptr [esi + 0x10], 0x80
004127FC  push     0xee
00412801  push     0x4413a4
00412806  push     0x441398
0041280B  push     0x4413b0
00412810  lea      eax, [ebp - 0x30]
00412813  push     eax
00412814  call     0x438f10
00412819  add      esp, 0x14
0041281C  lea      edx, [ebp - 0x30]
0041281F  push     edx
00412820  inc      dword ptr [esi + 0x1c]
00412823  lea      ecx, [ebp - 0x34]
00412826  push     ecx
00412827  call     0x438de4
0041282C  add      esp, 8
0041282F  inc      dword ptr [esi + 0x1c]
00412832  mov      word ptr [esi + 0x10], 0x8c
00412838  dec      dword ptr [esi + 0x1c]
0041283B  push     2
0041283D  lea      eax, [ebp - 0x30]
00412840  push     eax
00412841  call     0x438f64
00412846  add      esp, 8
00412849  mov      word ptr [esi + 0x10], 0x80
0041284F  add      dword ptr [esi + 0x1c], 2
00412853  add      dword ptr [esi + 0x1c], 3
00412857  lea      edx, [ebp - 0x34]
0041285A  push     edx
0041285B  push     0x4068bf
00412860  call     0x438eaa
00412865  add      esp, 0x24
00412868  mov      dword ptr [ebp - 0x10c], edi
0041286E  push     dword ptr [ebp - 0x10c]
00412874  call     0x438eb0
00412879  pop      ecx
0041287A  mov      dword ptr [ebp - 0x108], eax
00412880  push     0x4413b6
00412885  push     0
00412887  call     0x438e74
0041288C  add      esp, 8
0041288F  mov      edi, eax
00412891  test     edi, edi
00412893  jne      0x41291b
00412899  push     esi
0041289A  push     0
0041289C  push     0
0041289E  push     0
004128A0  push     1
004128A2  push     0x40690f
004128A7  push     0
004128A9  mov      word ptr [esi + 0x10], 0x98
004128AF  push     0xf1
004128B4  push     0x4413c4
004128B9  push     0x4413b8
004128BE  push     0x4413d0
004128C3  lea      eax, [ebp - 0x38]
004128C6  push     eax
004128C7  call     0x438f10
004128CC  add      esp, 0x14
004128CF  lea      edx, [ebp - 0x38]
004128D2  push     edx
004128D3  inc      dword ptr [esi + 0x1c]
004128D6  lea      ecx, [ebp - 0x3c]
004128D9  push     ecx
004128DA  call     0x438de4
004128DF  add      esp, 8
004128E2  inc      dword ptr [esi + 0x1c]
004128E5  mov      word ptr [esi + 0x10], 0xa4
004128EB  dec      dword ptr [esi + 0x1c]
004128EE  push     2
004128F0  lea      eax, [ebp - 0x38]
004128F3  push     eax
004128F4  call     0x438f64
004128F9  add      esp, 8
004128FC  mov      word ptr [esi + 0x10], 0x98
00412902  add      dword ptr [esi + 0x1c], 2
00412906  add      dword ptr [esi + 0x1c], 3
0041290A  lea      edx, [ebp - 0x3c]
0041290D  push     edx
0041290E  push     0x4068bf
00412913  call     0x438eaa
00412918  add      esp, 0x24
0041291B  mov      dword ptr [ebp - 0x110], edi
00412921  push     dword ptr [ebp - 0x110]
00412927  call     0x438eb0
0041292C  pop      ecx
0041292D  add      eax, 0x64
00412930  mov      dword ptr [ebx + 0x2d], eax
00412933  push     0x4413d6
00412938  push     0
0041293A  call     0x438e74
0041293F  add      esp, 8
00412942  mov      edi, eax
00412944  test     edi, edi
00412946  jne      0x4129ce
0041294C  push     esi
0041294D  push     0
0041294F  push     0
00412951  push     0
00412953  push     1
00412955  push     0x40690f
0041295A  push     0
0041295C  mov      word ptr [esi + 0x10], 0xb0
00412962  push     0xf4
00412967  push     0x4413e4
0041296C  push     0x4413d8
00412971  push     0x4413f0
00412976  lea      eax, [ebp - 0x40]
00412979  push     eax
0041297A  call     0x438f10
0041297F  add      esp, 0x14
00412982  lea      edx, [ebp - 0x40]
00412985  push     edx
00412986  inc      dword ptr [esi + 0x1c]
00412989  lea      ecx, [ebp - 0x44]
0041298C  push     ecx
0041298D  call     0x438de4
00412992  add      esp, 8
00412995  inc      dword ptr [esi + 0x1c]
00412998  mov      word ptr [esi + 0x10], 0xbc
0041299E  dec      dword ptr [esi + 0x1c]
004129A1  push     2
004129A3  lea      eax, [ebp - 0x40]
004129A6  push     eax
004129A7  call     0x438f64
004129AC  add      esp, 8
004129AF  mov      word ptr [esi + 0x10], 0xb0
004129B5  add      dword ptr [esi + 0x1c], 2
004129B9  add      dword ptr [esi + 0x1c], 3
004129BD  lea      edx, [ebp - 0x44]
004129C0  push     edx
004129C1  push     0x4068bf
004129C6  call     0x438eaa
004129CB  add      esp, 0x24
004129CE  mov      dword ptr [ebp - 0x114], edi
004129D4  push     dword ptr [ebp - 0x114]
004129DA  call     0x438eb0
004129DF  pop      ecx
004129E0  mov      dword ptr [ebx + 0x35], eax
004129E3  cmp      dword ptr [ebx + 0x35], 0
004129E7  je       0x412bcc
004129ED  cmp      dword ptr [ebx + 0x35], 1
004129F1  jbe      0x412bc7
004129F7  push     0
004129F9  push     0
004129FB  push     0x413fc9
00412A00  push     1
00412A02  push     dword ptr [ebx + 0x35]
00412A05  push     8
00412A07  push     0
00412A09  call     0x4037e0
... (503 more instructions)
```

## Strings Referenced

**Total unique strings**: 40

- `"str && *str"` @ 0x0043A0D9
- `"lib\strarray.cpp"` @ 0x0043A0E5
- `"Precondition"` @ 0x0043A0F6
- `"HSCUR_%u"` @ 0x004412EC
- `"HSRGN_%u"` @ 0x004412F6
- `"ptr != NULL"` @ 0x00441302
- `"hotspot.cpp"` @ 0x0044130E
- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B
- `"ptr != NULL"` @ 0x00441343
- `"hotspot.cpp"` @ 0x0044134F
- `"Check"` @ 0x0044135B
- `"ptr != NULL"` @ 0x00441363
- `"hotspot.cpp"` @ 0x0044136F
- `"Check"` @ 0x0044137B
- `"HSCMD_%u"` @ 0x00441381
- `"HOTSPOT_%u"` @ 0x0044138A
- `"ptr != NULL"` @ 0x00441398
- `"hotspot.cpp"` @ 0x004413A4
- `"Check"` @ 0x004413B0
- `"ptr != NULL"` @ 0x004413B8
- `"hotspot.cpp"` @ 0x004413C4
- `"Check"` @ 0x004413D0
- `"ptr != NULL"` @ 0x004413D8
- `"hotspot.cpp"` @ 0x004413E4
- `"Check"` @ 0x004413F0
- `"ptr != NULL"` @ 0x004413F8
- `"hotspot.cpp"` @ 0x00441404
- `"Check"` @ 0x00441410
- `"ptr != NULL"` @ 0x00441418
- `"hotspot.cpp"` @ 0x00441424
- `"Check"` @ 0x00441430
- `"HSVIDEO_%u"` @ 0x00441436
- `"HSVIDEOFLAGS_%u"` @ 0x00441442
- `"HSVIDEORECT_%u"` @ 0x00441452
- `"0,0,0,0"` @ 0x00441461
- `"%i,%i,%i,%i"` @ 0x00441469
- `" %u %i %i %i %i"` @ 0x00441475

## DATA Context

**Context around 0x00441381**:

- `"ptr != NULL"` @ 0x00441302
- `"hotspot.cpp"` @ 0x0044130E
- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B
- `"ptr != NULL"` @ 0x00441343
- `"hotspot.cpp"` @ 0x0044134F
- `"Check"` @ 0x0044135B
- `"ptr != NULL"` @ 0x00441363
- `"hotspot.cpp"` @ 0x0044136F
- `"Check"` @ 0x0044137B
- `"HSCMD_%u"` @ 0x00441381
- `"HOTSPOT_%u"` @ 0x0044138A
- `"ptr != NULL"` @ 0x00441398
- `"hotspot.cpp"` @ 0x004413A4
- `"Check"` @ 0x004413B0
- `"ptr != NULL"` @ 0x004413B8
- `"hotspot.cpp"` @ 0x004413C4
- `"Check"` @ 0x004413D0

**Context around 0x00441302**:

- `"vectimp.h"` @ 0x00441282
- `"Precondition"` @ 0x0044128C
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441299
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF
- `"HSCUR_%u"` @ 0x004412EC
- `"HSRGN_%u"` @ 0x004412F6
- `"ptr != NULL"` @ 0x00441302
- `"hotspot.cpp"` @ 0x0044130E
- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B
- `"ptr != NULL"` @ 0x00441343
- `"hotspot.cpp"` @ 0x0044134F
- `"Check"` @ 0x0044135B
- `"ptr != NULL"` @ 0x00441363
- `"hotspot.cpp"` @ 0x0044136F
- `"Check"` @ 0x0044137B
- `"HSCMD_%u"` @ 0x00441381

**Context around 0x00441404**:

- `"MD_%u"` @ 0x00441384
- `"HOTSPOT_%u"` @ 0x0044138A
- `"ptr != NULL"` @ 0x00441398
- `"hotspot.cpp"` @ 0x004413A4
- `"Check"` @ 0x004413B0
- `"ptr != NULL"` @ 0x004413B8
- `"hotspot.cpp"` @ 0x004413C4
- `"Check"` @ 0x004413D0
- `"ptr != NULL"` @ 0x004413D8
- `"hotspot.cpp"` @ 0x004413E4
- `"Check"` @ 0x004413F0
- `"ptr != NULL"` @ 0x004413F8
- `"hotspot.cpp"` @ 0x00441404
- `"Check"` @ 0x00441410
- `"ptr != NULL"` @ 0x00441418
- `"hotspot.cpp"` @ 0x00441424
- `"Check"` @ 0x00441430
- `"HSVIDEO_%u"` @ 0x00441436
- `"HSVIDEOFLAGS_%u"` @ 0x00441442
- `"HSVIDEORECT_%u"` @ 0x00441452

**Context around 0x0044138A**:

- `"ULL"` @ 0x0044130A
- `"hotspot.cpp"` @ 0x0044130E
- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B
- `"ptr != NULL"` @ 0x00441343
- `"hotspot.cpp"` @ 0x0044134F
- `"Check"` @ 0x0044135B
- `"ptr != NULL"` @ 0x00441363
- `"hotspot.cpp"` @ 0x0044136F
- `"Check"` @ 0x0044137B
- `"HSCMD_%u"` @ 0x00441381
- `"HOTSPOT_%u"` @ 0x0044138A
- `"ptr != NULL"` @ 0x00441398
- `"hotspot.cpp"` @ 0x004413A4
- `"Check"` @ 0x004413B0
- `"ptr != NULL"` @ 0x004413B8
- `"hotspot.cpp"` @ 0x004413C4
- `"Check"` @ 0x004413D0

**Context around 0x0044130E**:

- `"econdition"` @ 0x0044128E
- `"Lim > 0 && Data != 0 && index < Lim"` @ 0x00441299
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF
- `"HSCUR_%u"` @ 0x004412EC
- `"HSRGN_%u"` @ 0x004412F6
- `"ptr != NULL"` @ 0x00441302
- `"hotspot.cpp"` @ 0x0044130E
- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B
- `"ptr != NULL"` @ 0x00441343
- `"hotspot.cpp"` @ 0x0044134F
- `"Check"` @ 0x0044135B
- `"ptr != NULL"` @ 0x00441363
- `"hotspot.cpp"` @ 0x0044136F
- `"Check"` @ 0x0044137B
- `"HSCMD_%u"` @ 0x00441381
- `"HOTSPOT_%u"` @ 0x0044138A

**Context around 0x00441410**:

- `"T_%u"` @ 0x00441390
- `"ptr != NULL"` @ 0x00441398
- `"hotspot.cpp"` @ 0x004413A4
- `"Check"` @ 0x004413B0
- `"ptr != NULL"` @ 0x004413B8
- `"hotspot.cpp"` @ 0x004413C4
- `"Check"` @ 0x004413D0
- `"ptr != NULL"` @ 0x004413D8
- `"hotspot.cpp"` @ 0x004413E4
- `"Check"` @ 0x004413F0
- `"ptr != NULL"` @ 0x004413F8
- `"hotspot.cpp"` @ 0x00441404
- `"Check"` @ 0x00441410
- `"ptr != NULL"` @ 0x00441418
- `"hotspot.cpp"` @ 0x00441424
- `"Check"` @ 0x00441430
- `"HSVIDEO_%u"` @ 0x00441436
- `"HSVIDEOFLAGS_%u"` @ 0x00441442
- `"HSVIDEORECT_%u"` @ 0x00441452
- `"0,0,0,0"` @ 0x00441461

**Context around 0x00441398**:

- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B
- `"ptr != NULL"` @ 0x00441343
- `"hotspot.cpp"` @ 0x0044134F
- `"Check"` @ 0x0044135B
- `"ptr != NULL"` @ 0x00441363
- `"hotspot.cpp"` @ 0x0044136F
- `"Check"` @ 0x0044137B
- `"HSCMD_%u"` @ 0x00441381
- `"HOTSPOT_%u"` @ 0x0044138A
- `"ptr != NULL"` @ 0x00441398
- `"hotspot.cpp"` @ 0x004413A4
- `"Check"` @ 0x004413B0
- `"ptr != NULL"` @ 0x004413B8
- `"hotspot.cpp"` @ 0x004413C4
- `"Check"` @ 0x004413D0
- `"ptr != NULL"` @ 0x004413D8
- `"hotspot.cpp"` @ 0x004413E4

**Context around 0x00441418**:

- `"ptr != NULL"` @ 0x00441398
- `"hotspot.cpp"` @ 0x004413A4
- `"Check"` @ 0x004413B0
- `"ptr != NULL"` @ 0x004413B8
- `"hotspot.cpp"` @ 0x004413C4
- `"Check"` @ 0x004413D0
- `"ptr != NULL"` @ 0x004413D8
- `"hotspot.cpp"` @ 0x004413E4
- `"Check"` @ 0x004413F0
- `"ptr != NULL"` @ 0x004413F8
- `"hotspot.cpp"` @ 0x00441404
- `"Check"` @ 0x00441410
- `"ptr != NULL"` @ 0x00441418
- `"hotspot.cpp"` @ 0x00441424
- `"Check"` @ 0x00441430
- `"HSVIDEO_%u"` @ 0x00441436
- `"HSVIDEOFLAGS_%u"` @ 0x00441442
- `"HSVIDEORECT_%u"` @ 0x00441452
- `"0,0,0,0"` @ 0x00441461
- `"%i,%i,%i,%i"` @ 0x00441469

**Context around 0x0044131A**:

- `"im > 0 && Data != 0 && index < Lim"` @ 0x0044129A
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF
- `"HSCUR_%u"` @ 0x004412EC
- `"HSRGN_%u"` @ 0x004412F6
- `"ptr != NULL"` @ 0x00441302
- `"hotspot.cpp"` @ 0x0044130E
- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B
- `"ptr != NULL"` @ 0x00441343
- `"hotspot.cpp"` @ 0x0044134F
- `"Check"` @ 0x0044135B
- `"ptr != NULL"` @ 0x00441363
- `"hotspot.cpp"` @ 0x0044136F
- `"Check"` @ 0x0044137B
- `"HSCMD_%u"` @ 0x00441381
- `"HOTSPOT_%u"` @ 0x0044138A
- `"ptr != NULL"` @ 0x00441398

**Context around 0x00441320**:

- `" && Data != 0 && index < Lim"` @ 0x004412A0
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004412BD
- `"Precondition"` @ 0x004412DF
- `"HSCUR_%u"` @ 0x004412EC
- `"HSRGN_%u"` @ 0x004412F6
- `"ptr != NULL"` @ 0x00441302
- `"hotspot.cpp"` @ 0x0044130E
- `"Check"` @ 0x0044131A
- `"Points == NULL"` @ 0x00441320
- `"hotspot.cpp"` @ 0x0044132F
- `"Check"` @ 0x0044133B
- `"ptr != NULL"` @ 0x00441343
- `"hotspot.cpp"` @ 0x0044134F
- `"Check"` @ 0x0044135B
- `"ptr != NULL"` @ 0x00441363
- `"hotspot.cpp"` @ 0x0044136F
- `"Check"` @ 0x0044137B
- `"HSCMD_%u"` @ 0x00441381
- `"HOTSPOT_%u"` @ 0x0044138A
- `"ptr != NULL"` @ 0x00441398

## Functions Called

- 0x00403618
- 0x004390C0
- 0x0043929A
- 0x004390A2
- 0x00403A55
- 0x0043929A
- 0x004390A2
- 0x00438E74
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438EB0
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x004037E0
- 0x00438E74
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438EB0
- 0x00438E74
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438EB0
- 0x00412168
- 0x0043929A
- 0x0040E6FC
- 0x0043929A
- 0x004390A2
- 0x00438E74
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438EB0
- 0x00438E74
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x00438EB0
- 0x00438E74
- 0x00438F10
- 0x00438DE4

... and 58 more calls

---

*Extracted with recursive CALL following and DATA context*
