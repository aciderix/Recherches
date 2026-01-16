# LoadFromINI Function Analysis

**Function Address**: 0x004200CF
**Rank**: #86
**INI String Count**: 5
**Identified Structure**: TVNTextObject
**Confidence Score**: 2

---

## Assembly Code

**Instructions**: 1898

```assembly
004200CF  push     ebp
004200D0  mov      ebp, esp
004200D2  add      esp, 0xfffffd74
004200D8  push     ebx
004200D9  push     esi
004200DA  push     edi
004200DB  mov      ebx, dword ptr [ebp + 8]
004200DE  lea      edi, [ebp - 0xcc]
004200E4  mov      eax, 0x445324
004200E9  call     0x403618
004200EE  mov      edx, dword ptr [ebx + 0x36]
004200F1  cmp      dword ptr [edx + 6], 0
004200F5  jne      0x42017d
004200FB  push     edi
004200FC  push     0
004200FE  push     0
00420100  push     0
00420102  push     1
00420104  push     0x403be0
00420109  push     0
0042010B  mov      word ptr [edi + 0x10], 8
00420111  push     0x129
00420116  push     0x4464b4
0042011B  push     0x4464a6
00420120  push     0x4464c1
00420125  lea      ecx, [ebp - 0xc]
00420128  push     ecx
00420129  call     0x438f10
0042012E  add      esp, 0x14
00420131  lea      eax, [ebp - 0xc]
00420134  push     eax
00420135  inc      dword ptr [edi + 0x1c]
00420138  lea      edx, [ebp - 0x10]
0042013B  push     edx
0042013C  call     0x438de4
00420141  add      esp, 8
00420144  inc      dword ptr [edi + 0x1c]
00420147  mov      word ptr [edi + 0x10], 0x14
0042014D  dec      dword ptr [edi + 0x1c]
00420150  push     2
00420152  lea      ecx, [ebp - 0xc]
00420155  push     ecx
00420156  call     0x438f64
0042015B  add      esp, 8
0042015E  mov      word ptr [edi + 0x10], 8
00420164  add      dword ptr [edi + 0x1c], 2
00420168  add      dword ptr [edi + 0x1c], 3
0042016C  lea      eax, [ebp - 0x10]
0042016F  push     eax
00420170  push     0x403b88
00420175  call     0x438eaa
0042017A  add      esp, 0x24
0042017D  push     0x5a
0042017F  mov      edx, dword ptr [ebp + 0xc]
00420182  push     edx
00420183  mov      ecx, dword ptr [edx + 5]
00420186  call     dword ptr [ecx + 0xc]
00420189  add      esp, 8
0042018C  mov      dword ptr [0x444a34], eax
00420191  lea      eax, [ebx + 8]
00420194  push     eax
00420195  mov      edx, dword ptr [ebx + 9]
00420198  call     dword ptr [edx + 4]
0042019B  pop      ecx
0042019C  test     eax, eax
0042019E  jne      0x4201c5
004201A0  lea      ecx, [ebp - 0x224]
004201A6  push     ecx
004201A7  call     0x41f121
004201AC  pop      ecx
004201AD  mov      dword ptr [ebp - 0xd0], eax
004201B3  push     dword ptr [ebp - 0xd0]
004201B9  lea      eax, [ebx + 8]
004201BC  push     eax
004201BD  call     0x42320a
004201C2  add      esp, 8
004201C5  mov      edx, dword ptr [ebx + 0x3e]
004201C8  mov      dword ptr [ebp - 0xd4], edx
004201CE  lea      esi, [ebx + 4]
004201D1  mov      eax, dword ptr [ebp - 0xd4]
004201D7  inc      eax
004201D8  mov      dword ptr [ebp - 0xd8], eax
004201DE  mov      edx, dword ptr [esi]
004201E0  cmp      edx, dword ptr [ebp - 0xd8]
004201E6  jle      0x42020f
004201E8  mov      ecx, dword ptr [ebp - 0xd8]
004201EE  sub      ecx, dword ptr [esi]
004201F0  add      ecx, dword ptr [esi + 0xd]
004201F3  mov      dword ptr [ebp - 0xdc], ecx
004201F9  push     0
004201FB  push     dword ptr [ebp - 0xdc]
00420201  lea      eax, [esi + 4]
00420204  push     eax
00420205  call     0x4232bc
0042020A  add      esp, 0xc
0042020D  jmp      0x42025a
0042020F  mov      edx, dword ptr [esi + 0xd]
00420212  mov      dword ptr [ebp - 0xe0], edx
00420218  cmp      dword ptr [ebp - 0xe0], -1
0042021F  jne      0x420228
00420221  mov      ecx, 0x7fffffff
00420226  jmp      0x420230
00420228  mov      ecx, dword ptr [esi]
0042022A  add      ecx, dword ptr [ebp - 0xe0]
00420230  cmp      ecx, dword ptr [ebp - 0xd8]
00420236  jg       0x42025a
00420238  mov      eax, dword ptr [ebp - 0xd8]
0042023E  sub      eax, dword ptr [esi]
00420240  mov      dword ptr [ebp - 0xe4], eax
00420246  push     0
00420248  push     dword ptr [ebp - 0xe4]
0042024E  lea      edx, [esi + 4]
00420251  push     edx
00420252  call     0x4232bc
00420257  add      esp, 0xc
0042025A  mov      eax, dword ptr [ebp - 0xd4]
00420260  sub      eax, dword ptr [esi]
00420262  mov      dword ptr [ebp - 0xe8], eax
00420268  add      esi, 4
0042026B  mov      dword ptr [ebp - 0xec], esi
00420271  mov      eax, dword ptr [ebp - 0xec]
00420277  cmp      dword ptr [eax + 9], 0
0042027B  je       0x420324
00420281  mov      edx, dword ptr [ebp - 0xec]
00420287  cmp      dword ptr [edx + 5], 0
0042028B  je       0x4202a2
0042028D  mov      ecx, dword ptr [ebp - 0xec]
00420293  mov      eax, dword ptr [ecx + 9]
00420296  cmp      eax, dword ptr [ebp - 0xe8]
0042029C  ja       0x420324
004202A2  push     edi
004202A3  push     0
004202A5  push     0
004202A7  push     0
004202A9  push     1
004202AB  push     0x403be0
004202B0  push     0
004202B2  mov      word ptr [edi + 0x10], 0x20
004202B8  push     0xc1
004202BD  push     0x4464f3
004202C2  push     0x4464ce
004202C7  push     0x446515
004202CC  lea      edx, [ebp - 0x14]
004202CF  push     edx
004202D0  call     0x438f10
004202D5  add      esp, 0x14
004202D8  lea      ecx, [ebp - 0x14]
004202DB  push     ecx
004202DC  inc      dword ptr [edi + 0x1c]
004202DF  lea      eax, [ebp - 0x18]
004202E2  push     eax
004202E3  call     0x438de4
004202E8  add      esp, 8
004202EB  inc      dword ptr [edi + 0x1c]
004202EE  mov      word ptr [edi + 0x10], 0x2c
004202F4  dec      dword ptr [edi + 0x1c]
004202F7  push     2
004202F9  lea      edx, [ebp - 0x14]
004202FC  push     edx
004202FD  call     0x438f64
00420302  add      esp, 8
00420305  mov      word ptr [edi + 0x10], 0x20
0042030B  add      dword ptr [edi + 0x1c], 2
0042030F  add      dword ptr [edi + 0x1c], 3
00420313  lea      ecx, [ebp - 0x18]
00420316  push     ecx
00420317  push     0x403b88
0042031C  call     0x438eaa
00420321  add      esp, 0x24
00420324  mov      eax, dword ptr [ebp - 0xec]
0042032A  mov      edx, dword ptr [eax + 5]
0042032D  imul     ecx, dword ptr [ebp - 0xe8], 0x52
00420334  add      edx, ecx
00420336  push     edx
00420337  lea      eax, [ebp - 0x278]
0042033D  push     eax
0042033E  call     0x41f1cf
00420343  add      esp, 8
00420346  mov      dword ptr [ebp - 0x28c], 0xffffffff
00420350  xor      edx, edx
00420352  mov      dword ptr [ebp - 0x288], edx
00420358  xor      ecx, ecx
0042035A  mov      dword ptr [ebp - 0x284], ecx
00420360  xor      eax, eax
00420362  mov      dword ptr [ebp - 0x280], eax
00420368  xor      edx, edx
0042036A  mov      dword ptr [ebp - 0x27c], edx
00420370  lea      ecx, [ebx + 0x21]
00420373  mov      dword ptr [ebp - 0xf0], ecx
00420379  mov      eax, dword ptr [ebp - 0xf0]
0042037F  xor      edx, edx
00420381  mov      dword ptr [eax + 0xd], edx
00420384  mov      word ptr [edi + 0x10], 0x38
0042038A  lea      ecx, [ebp - 4]
0042038D  push     ecx
0042038E  call     0x438ec2
00420393  pop      ecx
00420394  inc      dword ptr [edi + 0x1c]
00420397  mov      word ptr [edi + 0x10], 0x44
0042039D  mov      word ptr [edi + 0x10], 0x50
004203A3  lea      eax, [ebp - 8]
004203A6  push     eax
004203A7  call     0x438ec2
004203AC  pop      ecx
004203AD  inc      dword ptr [edi + 0x1c]
004203B0  mov      word ptr [edi + 0x10], 0x44
004203B6  xor      edx, edx
004203B8  mov      dword ptr [ebp - 0xf8], edx
004203BE  xor      ecx, ecx
004203C0  mov      dword ptr [ebp - 0xf4], ecx
004203C6  mov      esi, dword ptr [ebp - 0x278]
004203CC  mov      dword ptr [ebp - 0xfc], esi
004203D2  mov      eax, dword ptr [ebp + 0x10]
004203D5  mov      dword ptr [ebp - 0x108], eax
004203DB  mov      edx, dword ptr [ebp - 0x108]
004203E1  mov      ecx, dword ptr [edx]
004203E3  mov      dword ptr [ebp - 0x104], ecx
004203E9  mov      eax, dword ptr [ebp - 0x108]
004203EF  mov      edx, dword ptr [eax + 4]
004203F2  mov      dword ptr [ebp - 0x100], edx
004203F8  mov      ecx, dword ptr [ebp - 0x230]
004203FE  add      dword ptr [ebp - 0x104], ecx
00420404  xor      eax, eax
00420406  mov      dword ptr [ebp - 0x110], eax
0042040C  xor      edx, edx
0042040E  mov      dword ptr [ebp - 0x10c], edx
00420414  xor      ecx, ecx
00420416  mov      dword ptr [ebp - 0x114], ecx
0042041C  mov      eax, dword ptr [ebp + 0xc]
0042041F  push     eax
00420420  mov      edx, dword ptr [eax + 5]
00420423  call     dword ptr [edx + 0x58]
00420426  pop      ecx
00420427  mov      ecx, dword ptr [ebp + 0xc]
0042042A  cmp      eax, dword ptr [ecx]
0042042C  je       0x42043a
0042042E  push     0x18
00420430  mov      eax, dword ptr [ebp + 0xc]
00420433  push     dword ptr [eax]
00420435  call     0x4397bc
0042043A  push     0x18
0042043C  mov      edx, dword ptr [ebp + 0xc]
0042043F  push     edx
00420440  mov      ecx, dword ptr [edx + 5]
00420443  call     dword ptr [ecx + 0x58]
00420446  pop      ecx
00420447  push     eax
00420448  call     0x4397bc
0042044D  push     0
0042044F  push     0
00420451  mov      eax, dword ptr [ebp + 0xc]
00420454  push     eax
00420455  mov      edx, dword ptr [eax + 5]
00420458  call     dword ptr [edx + 0x58]
0042045B  pop      ecx
0042045C  push     eax
0042045D  call     0x4397b6
00420462  test     eax, eax
00420464  setne    cl
00420467  and      ecx, 1
0042046A  mov      word ptr [edi + 0x10], 0x5c
00420470  lea      eax, [ebp - 0x274]
00420476  push     eax
00420477  lea      edx, [ebp - 0x20]
0042047A  push     edx
0042047B  call     0x43946e
00420480  add      esp, 8
00420483  add      dword ptr [edi + 0x1c], 2
00420487  push     eax
00420488  mov      ecx, dword ptr [ebp + 0xc]
0042048B  push     ecx
0042048C  mov      eax, dword ptr [ecx + 5]
0042048F  call     dword ptr [eax + 0x14]
00420492  add      esp, 8
00420495  sub      dword ptr [edi + 0x1c], 2
00420499  add      dword ptr [edi + 0x1c], 2
0042049D  dec      dword ptr [edi + 0x1c]
004204A0  push     0
004204A2  lea      edx, [ebp - 0x20]
004204A5  push     edx
004204A6  call     0x4392b8
004204AB  add      esp, 8
004204AE  jmp      0x421835
004204B3  mov      dword ptr [ebp - 0x118], esi
004204B9  push     dword ptr [ebp - 0x118]
004204BF  lea      ecx, [ebx + 0x36]
004204C2  push     ecx
004204C3  call     0x438ee0
004204C8  add      esp, 8
004204CB  movsx    eax, byte ptr [eax]
004204CE  cmp      eax, 0x3c
004204D1  jne      0x42118f
004204D7  push     esi
004204D8  lea      edx, [ebp - 8]
004204DB  push     edx
004204DC  push     ebx
004204DD  call     0x41f790
004204E2  add      esp, 0xc
004204E5  mov      esi, eax
004204E7  mov      byte ptr [ebp - 0x119], 1
004204EE  mov      word ptr [edi + 0x10], 0x44
004204F4  mov      ecx, dword ptr [ebp - 8]
004204F7  cmp      dword ptr [ecx + 6], 0
004204FB  je       0x42118f
00420501  lea      eax, [ebp - 8]
00420504  push     eax
00420505  call     0x438e26
0042050A  pop      ecx
0042050B  mov      word ptr [edi + 0x10], 0x68
00420511  push     0x446522
00420516  lea      edx, [ebp - 0x24]
00420519  push     edx
0042051A  call     0x438e6e
0042051F  add      esp, 8
00420522  inc      dword ptr [edi + 0x1c]
00420525  lea      ecx, [ebp - 0x24]
00420528  push     ecx
00420529  lea      eax, [ebp - 8]
0042052C  push     eax
0042052D  call     0x438ec8
00420532  add      esp, 8
00420535  test     eax, eax
00420537  sete     dl
0042053A  and      edx, 1
0042053D  push     edx
0042053E  dec      dword ptr [edi + 0x1c]
00420541  push     2
00420543  lea      ecx, [ebp - 0x24]
00420546  push     ecx
00420547  call     0x438f64
0042054C  add      esp, 8
0042054F  pop      eax
00420550  test     eax, eax
00420552  je       0x42056a
00420554  mov      dword ptr [ebp - 0x114], 1
0042055E  mov      byte ptr [ebp - 0x119], 0
00420565  jmp      0x42112e
0042056A  mov      word ptr [edi + 0x10], 0x74
00420570  push     0x446525
00420575  lea      edx, [ebp - 0x28]
00420578  push     edx
00420579  call     0x438e6e
0042057E  add      esp, 8
00420581  inc      dword ptr [edi + 0x1c]
00420584  lea      ecx, [ebp - 0x28]
00420587  push     ecx
00420588  lea      eax, [ebp - 8]
0042058B  push     eax
0042058C  call     0x438ec8
00420591  add      esp, 8
00420594  test     eax, eax
00420596  sete     dl
00420599  and      edx, 1
0042059C  push     edx
0042059D  dec      dword ptr [edi + 0x1c]
004205A0  push     2
004205A2  lea      ecx, [ebp - 0x28]
004205A5  push     ecx
004205A6  call     0x438f64
004205AB  add      esp, 8
004205AE  pop      eax
004205AF  test     eax, eax
004205B1  jne      0x4205fa
004205B3  push     -1
004205B5  push     0
004205B7  push     0x446528
004205BC  lea      edx, [ebp - 0x2c]
004205BF  push     edx
004205C0  call     0x438e6e
004205C5  add      esp, 8
004205C8  inc      dword ptr [edi + 0x1c]
004205CB  lea      ecx, [ebp - 0x2c]
004205CE  push     ecx
004205CF  lea      eax, [ebp - 8]
004205D2  push     eax
004205D3  call     0x438dfc
004205D8  add      esp, 0x10
004205DB  test     eax, eax
004205DD  sete     dl
004205E0  and      edx, 1
004205E3  push     edx
004205E4  dec      dword ptr [edi + 0x1c]
004205E7  push     2
004205E9  lea      ecx, [ebp - 0x2c]
004205EC  push     ecx
004205ED  call     0x438f64
004205F2  add      esp, 8
004205F5  pop      eax
004205F6  test     eax, eax
004205F8  je       0x42062d
004205FA  add      dword ptr [ebp - 0x230], 0x28
00420601  mov      byte ptr [ebp - 0x227], 1
00420608  cmp      dword ptr [ebp - 0x22c], 0
0042060F  jne      0x42061b
00420611  mov      dword ptr [ebp - 0x114], 2
0042061B  inc      dword ptr [ebp - 0x22c]
00420621  mov      byte ptr [ebp - 0x119], 0
00420628  jmp      0x42112e
0042062D  mov      word ptr [edi + 0x10], 0x80
00420633  push     0x44652c
00420638  lea      edx, [ebp - 0x30]
0042063B  push     edx
0042063C  call     0x438e6e
00420641  add      esp, 8
00420644  inc      dword ptr [edi + 0x1c]
00420647  lea      ecx, [ebp - 0x30]
0042064A  push     ecx
0042064B  lea      eax, [ebp - 8]
0042064E  push     eax
0042064F  call     0x438ec8
00420654  add      esp, 8
00420657  test     eax, eax
00420659  sete     dl
0042065C  and      edx, 1
0042065F  push     edx
00420660  dec      dword ptr [edi + 0x1c]
00420663  push     2
00420665  lea      ecx, [ebp - 0x30]
00420668  push     ecx
00420669  call     0x438f64
0042066E  add      esp, 8
00420671  pop      eax
00420672  test     eax, eax
00420674  je       0x4206ca
00420676  mov      edx, dword ptr [ebp + 0x10]
00420679  mov      ecx, dword ptr [edx + 4]
0042067C  cmp      ecx, dword ptr [ebp - 0x100]
00420682  je       0x4206ca
00420684  cmp      dword ptr [ebp - 0x230], 0x28
0042068B  jle      0x420696
0042068D  sub      dword ptr [ebp - 0x230], 0x28
00420694  jmp      0x42069e
00420696  xor      eax, eax
00420698  mov      dword ptr [ebp - 0x230], eax
0042069E  mov      byte ptr [ebp - 0x227], 0
004206A5  dec      dword ptr [ebp - 0x22c]
004206AB  cmp      dword ptr [ebp - 0x22c], 0
004206B2  jne      0x4206be
004206B4  mov      dword ptr [ebp - 0x114], 2
004206BE  mov      byte ptr [ebp - 0x119], 0
004206C5  jmp      0x42112e
004206CA  mov      word ptr [edi + 0x10], 0x8c
004206D0  push     0x446530
004206D5  lea      edx, [ebp - 0x34]
004206D8  push     edx
004206D9  call     0x438e6e
004206DE  add      esp, 8
004206E1  inc      dword ptr [edi + 0x1c]
004206E4  lea      ecx, [ebp - 0x34]
004206E7  push     ecx
004206E8  lea      eax, [ebp - 8]
004206EB  push     eax
004206EC  call     0x438ec8
004206F1  add      esp, 8
004206F4  test     eax, eax
004206F6  sete     dl
004206F9  and      edx, 1
004206FC  push     edx
004206FD  dec      dword ptr [edi + 0x1c]
00420700  push     2
00420702  lea      ecx, [ebp - 0x34]
00420705  push     ecx
00420706  call     0x438f64
0042070B  add      esp, 8
0042070E  pop      eax
0042070F  test     eax, eax
00420711  jne      0x42075a
00420713  push     -1
00420715  push     0
00420717  push     0x446533
0042071C  lea      edx, [ebp - 0x38]
0042071F  push     edx
00420720  call     0x438e6e
00420725  add      esp, 8
00420728  inc      dword ptr [edi + 0x1c]
0042072B  lea      ecx, [ebp - 0x38]
0042072E  push     ecx
0042072F  lea      eax, [ebp - 8]
00420732  push     eax
00420733  call     0x438dfc
00420738  add      esp, 0x10
0042073B  test     eax, eax
0042073D  sete     dl
00420740  and      edx, 1
00420743  push     edx
00420744  dec      dword ptr [edi + 0x1c]
00420747  push     2
00420749  lea      ecx, [ebp - 0x38]
0042074C  push     ecx
0042074D  call     0x438f64
00420752  add      esp, 8
00420755  pop      eax
00420756  test     eax, eax
00420758  je       0x42078d
0042075A  add      dword ptr [ebp - 0x230], 0x28
00420761  mov      byte ptr [ebp - 0x227], 0
00420768  cmp      dword ptr [ebp - 0x22c], 0
0042076F  jne      0x42077b
00420771  mov      dword ptr [ebp - 0x114], 2
0042077B  inc      dword ptr [ebp - 0x22c]
... (1398 more instructions)
```

## Strings Referenced

**Total unique strings**: 22

- `"Text.length()"` @ 0x004464A6
- `"htmldata.cpp"` @ 0x004464B4
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3
- `"Precondition"` @ 0x00446515
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C
- `"UL "` @ 0x00446533
- `"/UL"` @ 0x00446537
- `"/TR"` @ 0x0044653E
- `"/H1"` @ 0x0044655C
- `"/H6"` @ 0x00446560
- `"PRE"` @ 0x00446564
- `"Courier New"` @ 0x00446568
- `"/PRE"` @ 0x00446574
- `"Times New Roman"` @ 0x00446579
- `"FONT"` @ 0x00446589
- `"/FONT"` @ 0x0044658E
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044659E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004465C3
- `"Precondition"` @ 0x004465E5

## DATA Context

**Context around 0x00446589**:

- `"b/vectimp.h"` @ 0x00446509
- `"Precondition"` @ 0x00446515
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C
- `"UL "` @ 0x00446533
- `"/UL"` @ 0x00446537
- `"/TR"` @ 0x0044653E
- `"/H1"` @ 0x0044655C
- `"/H6"` @ 0x00446560
- `"PRE"` @ 0x00446564
- `"Courier New"` @ 0x00446568
- `"/PRE"` @ 0x00446574
- `"Times New Roman"` @ 0x00446579
- `"FONT"` @ 0x00446589
- `"/FONT"` @ 0x0044658E
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044659E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004465C3
- `"Precondition"` @ 0x004465E5
- `"Cur < Upper"` @ 0x004465F3
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004465FF

**Context around 0x0044658E**:

- `"timp.h"` @ 0x0044650E
- `"Precondition"` @ 0x00446515
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C
- `"UL "` @ 0x00446533
- `"/UL"` @ 0x00446537
- `"/TR"` @ 0x0044653E
- `"/H1"` @ 0x0044655C
- `"/H6"` @ 0x00446560
- `"PRE"` @ 0x00446564
- `"Courier New"` @ 0x00446568
- `"/PRE"` @ 0x00446574
- `"Times New Roman"` @ 0x00446579
- `"FONT"` @ 0x00446589
- `"/FONT"` @ 0x0044658E
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044659E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004465C3
- `"Precondition"` @ 0x004465E5
- `"Cur < Upper"` @ 0x004465F3
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004465FF

**Context around 0x00446515**:

- `"LOR="#%lX""` @ 0x00446495
- `"%u."` @ 0x004464A0
- `"Text.length()"` @ 0x004464A6
- `"htmldata.cpp"` @ 0x004464B4
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3
- `"Precondition"` @ 0x00446515
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C
- `"UL "` @ 0x00446533
- `"/UL"` @ 0x00446537
- `"/TR"` @ 0x0044653E
- `"/H1"` @ 0x0044655C
- `"/H6"` @ 0x00446560
- `"PRE"` @ 0x00446564
- `"Courier New"` @ 0x00446568
- `"/PRE"` @ 0x00446574
- `"Times New Roman"` @ 0x00446579
- `"FONT"` @ 0x00446589

**Context around 0x0044659E**:

- `"ion"` @ 0x0044651E
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C
- `"UL "` @ 0x00446533
- `"/UL"` @ 0x00446537
- `"/TR"` @ 0x0044653E
- `"/H1"` @ 0x0044655C
- `"/H6"` @ 0x00446560
- `"PRE"` @ 0x00446564
- `"Courier New"` @ 0x00446568
- `"/PRE"` @ 0x00446574
- `"Times New Roman"` @ 0x00446579
- `"FONT"` @ 0x00446589
- `"/FONT"` @ 0x0044658E
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044659E
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004465C3
- `"Precondition"` @ 0x004465E5
- `"Cur < Upper"` @ 0x004465F3
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004465FF

**Context around 0x004464A6**:

- `"Roman"` @ 0x00446426
- `"Text[start] == '<'"` @ 0x0044642D
- `"htmldata.cpp"` @ 0x00446440
- `"Precondition"` @ 0x0044644D
- `"HREF"` @ 0x00446461
- `"."'"` @ 0x00446469
- `"SIZE"` @ 0x0044646D
- `"SIZE="%i""` @ 0x00446472
- `"SIZE=%i"` @ 0x0044647C
- `"FACE"` @ 0x00446484
- `"COLOR"` @ 0x0044648D
- `"COLOR="#%lX""` @ 0x00446493
- `"%u."` @ 0x004464A0
- `"Text.length()"` @ 0x004464A6
- `"htmldata.cpp"` @ 0x004464B4
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3
- `"Precondition"` @ 0x00446515

**Context around 0x00446528**:

- `"xt.length()"` @ 0x004464A8
- `"htmldata.cpp"` @ 0x004464B4
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3
- `"Precondition"` @ 0x00446515
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C
- `"UL "` @ 0x00446533
- `"/UL"` @ 0x00446537
- `"/TR"` @ 0x0044653E
- `"/H1"` @ 0x0044655C
- `"/H6"` @ 0x00446560
- `"PRE"` @ 0x00446564
- `"Courier New"` @ 0x00446568
- `"/PRE"` @ 0x00446574
- `"Times New Roman"` @ 0x00446579
- `"FONT"` @ 0x00446589
- `"/FONT"` @ 0x0044658E
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044659E

**Context around 0x0044652C**:

- `"ength()"` @ 0x004464AC
- `"htmldata.cpp"` @ 0x004464B4
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3
- `"Precondition"` @ 0x00446515
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C
- `"UL "` @ 0x00446533
- `"/UL"` @ 0x00446537
- `"/TR"` @ 0x0044653E
- `"/H1"` @ 0x0044655C
- `"/H6"` @ 0x00446560
- `"PRE"` @ 0x00446564
- `"Courier New"` @ 0x00446568
- `"/PRE"` @ 0x00446574
- `"Times New Roman"` @ 0x00446579
- `"FONT"` @ 0x00446589
- `"/FONT"` @ 0x0044658E
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044659E

**Context around 0x00446533**:

- `"htmldata.cpp"` @ 0x004464B4
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3
- `"Precondition"` @ 0x00446515
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C
- `"UL "` @ 0x00446533
- `"/UL"` @ 0x00446537
- `"/TR"` @ 0x0044653E
- `"/H1"` @ 0x0044655C
- `"/H6"` @ 0x00446560
- `"PRE"` @ 0x00446564
- `"Courier New"` @ 0x00446568
- `"/PRE"` @ 0x00446574
- `"Times New Roman"` @ 0x00446579
- `"FONT"` @ 0x00446589
- `"/FONT"` @ 0x0044658E
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044659E

**Context around 0x004464B4**:

- `"art] == '<'"` @ 0x00446434
- `"htmldata.cpp"` @ 0x00446440
- `"Precondition"` @ 0x0044644D
- `"HREF"` @ 0x00446461
- `"."'"` @ 0x00446469
- `"SIZE"` @ 0x0044646D
- `"SIZE="%i""` @ 0x00446472
- `"SIZE=%i"` @ 0x0044647C
- `"FACE"` @ 0x00446484
- `"COLOR"` @ 0x0044648D
- `"COLOR="#%lX""` @ 0x00446493
- `"%u."` @ 0x004464A0
- `"Text.length()"` @ 0x004464A6
- `"htmldata.cpp"` @ 0x004464B4
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3
- `"Precondition"` @ 0x00446515
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C

**Context around 0x00446537**:

- `"ldata.cpp"` @ 0x004464B7
- `"Precondition"` @ 0x004464C1
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x004464CE
- `"C:\BC5\INCLUDE\classlib/vectimp.h"` @ 0x004464F3
- `"Precondition"` @ 0x00446515
- `"OL "` @ 0x00446528
- `"/OL"` @ 0x0044652C
- `"UL "` @ 0x00446533
- `"/UL"` @ 0x00446537
- `"/TR"` @ 0x0044653E
- `"/H1"` @ 0x0044655C
- `"/H6"` @ 0x00446560
- `"PRE"` @ 0x00446564
- `"Courier New"` @ 0x00446568
- `"/PRE"` @ 0x00446574
- `"Times New Roman"` @ 0x00446579
- `"FONT"` @ 0x00446589
- `"/FONT"` @ 0x0044658E
- `"Lim == 0 || Data != 0 && index < Lim"` @ 0x0044659E

## Functions Called

- 0x00403618
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x0041F121
- 0x0042320A
- 0x004232BC
- 0x004232BC
- 0x00438F10
- 0x00438DE4
- 0x00438F64
- 0x00438EAA
- 0x0041F1CF
- 0x00438EC2
- 0x00438EC2
- 0x004397BC
- 0x004397BC
- 0x004397B6
- 0x0043946E
- 0x004392B8
- 0x00438EE0
- 0x0041F790
- 0x00438E26
- 0x00438E6E
- 0x00438EC8
- 0x00438F64
- 0x00438E6E
- 0x00438EC8
- 0x00438F64
- 0x00438E6E
- 0x00438DFC
- 0x00438F64
- 0x00438E6E
- 0x00438EC8
- 0x00438F64
- 0x00438E6E
- 0x00438EC8
- 0x00438F64
- 0x00438E6E
- 0x00438DFC
- 0x00438F64
- 0x00438E6E
- 0x00438EC8
- 0x00438F64
- 0x00438E6E
- 0x00438EC8
- 0x00438F64
- 0x00438E6E
- 0x00438EC8

... and 98 more calls

---

*Extracted with recursive CALL following and DATA context*
