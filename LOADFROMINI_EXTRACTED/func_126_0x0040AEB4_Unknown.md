# LoadFromINI Function Analysis

**Function Address**: 0x0040AEB4
**Rank**: #126
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 312

```assembly
0040AEB4  push     ebp
0040AEB5  mov      ebp, esp
0040AEB7  add      esp, -0x58
0040AEBA  push     ebx
0040AEBB  push     esi
0040AEBC  push     edi
0040AEBD  lea      ebx, [ebp - 0x54]
0040AEC0  lea      edi, [ebp + 8]
0040AEC3  mov      eax, 0x43da9d
0040AEC8  call     0x403618
0040AECD  mov      word ptr [ebx + 0x10], 8
0040AED3  mov      edx, dword ptr [edi]
0040AED5  mov      dword ptr [edx], 0x440458
0040AEDB  mov      ecx, dword ptr [edi]
0040AEDD  mov      dword ptr [ecx], 0x4402ac
0040AEE3  push     0x43fa2f
0040AEE8  mov      eax, dword ptr [edi]
0040AEEA  add      eax, 4
0040AEED  push     eax
0040AEEE  call     0x438e6e
0040AEF3  add      esp, 8
0040AEF6  inc      dword ptr [ebx + 0x1c]
0040AEF9  add      dword ptr [ebx + 0x1c], 2
0040AEFD  mov      edx, dword ptr [edi]
0040AEFF  mov      dword ptr [edx], 0x440298
0040AF05  mov      eax, dword ptr [edi]
0040AF07  add      eax, 8
0040AF0A  xor      edx, edx
0040AF0C  mov      dword ptr [eax], edx
0040AF0E  xor      ecx, ecx
0040AF10  mov      dword ptr [eax + 4], ecx
0040AF13  xor      edx, edx
0040AF15  mov      dword ptr [eax + 8], edx
0040AF18  xor      ecx, ecx
0040AF1A  mov      dword ptr [eax + 0xc], ecx
0040AF1D  mov      eax, dword ptr [edi]
0040AF1F  mov      word ptr [eax + 0x18], 0
0040AF25  add      dword ptr [ebx + 0x1c], 3
0040AF29  mov      eax, dword ptr [edi]
0040AF2B  mov      dword ptr [eax], 0x440284
0040AF31  mov      edx, dword ptr [edi]
0040AF33  add      edx, 0x1a
0040AF36  push     edx
0040AF37  call     0x438ec2
0040AF3C  pop      ecx
0040AF3D  inc      dword ptr [ebx + 0x1c]
0040AF40  push     0
0040AF42  mov      ecx, dword ptr [ebp + 0xc]
0040AF45  mov      eax, dword ptr [ecx]
0040AF47  push     dword ptr [eax + 2]
0040AF4A  call     0x439168
0040AF4F  add      esp, 8
0040AF52  mov      esi, eax
0040AF54  mov      word ptr [ebx + 0x10], 0x14
0040AF5A  push     0x43f76a
0040AF5F  lea      eax, [ebp - 4]
0040AF62  push     eax
0040AF63  call     0x438e6e
0040AF68  add      esp, 8
0040AF6B  inc      dword ptr [ebx + 0x1c]
0040AF6E  lea      edx, [ebp - 4]
0040AF71  push     edx
0040AF72  push     0
0040AF74  push     esi
0040AF75  call     0x407ed3
0040AF7A  add      esp, 8
0040AF7D  push     eax
0040AF7E  lea      ecx, [ebp - 8]
0040AF81  push     ecx
0040AF82  call     0x438e6e
0040AF87  add      esp, 8
0040AF8A  inc      dword ptr [ebx + 0x1c]
0040AF8D  lea      eax, [ebp - 8]
0040AF90  push     eax
0040AF91  lea      edx, [ebp - 0xc]
0040AF94  push     edx
0040AF95  call     0x40804e
0040AF9A  add      esp, 0xc
0040AF9D  lea      eax, [ebp - 0xc]
0040AFA0  inc      dword ptr [ebx + 0x1c]
0040AFA3  push     -1
0040AFA5  push     0
0040AFA7  push     eax
0040AFA8  mov      edx, dword ptr [edi]
0040AFAA  add      edx, 0x1a
0040AFAD  push     edx
0040AFAE  call     0x438f04
0040AFB3  add      esp, 0x10
0040AFB6  dec      dword ptr [ebx + 0x1c]
0040AFB9  push     2
0040AFBB  lea      ecx, [ebp - 0xc]
0040AFBE  push     ecx
0040AFBF  call     0x438f64
0040AFC4  add      esp, 8
0040AFC7  dec      dword ptr [ebx + 0x1c]
0040AFCA  push     2
0040AFCC  lea      eax, [ebp - 8]
0040AFCF  push     eax
0040AFD0  call     0x438f64
0040AFD5  add      esp, 8
0040AFD8  dec      dword ptr [ebx + 0x1c]
0040AFDB  push     2
0040AFDD  lea      edx, [ebp - 4]
0040AFE0  push     edx
0040AFE1  call     0x438f64
0040AFE6  add      esp, 8
0040AFE9  push     0
0040AFEB  mov      word ptr [ebx + 0x10], 0x20
0040AFF1  push     0
0040AFF3  push     0
0040AFF5  call     0x407ed3
0040AFFA  add      esp, 8
0040AFFD  push     eax
0040AFFE  lea      ecx, [ebp - 0x10]
0040B001  push     ecx
0040B002  call     0x438e6e
0040B007  add      esp, 8
0040B00A  inc      dword ptr [ebx + 0x1c]
0040B00D  lea      eax, [ebp - 0x10]
0040B010  push     eax
0040B011  call     0x407fe5
0040B016  add      esp, 8
0040B019  mov      edx, dword ptr [edi]
0040B01B  mov      dword ptr [edx + 0x1e], eax
0040B01E  dec      dword ptr [ebx + 0x1c]
0040B021  push     2
0040B023  lea      ecx, [ebp - 0x10]
0040B026  push     ecx
0040B027  call     0x438f64
0040B02C  add      esp, 8
0040B02F  push     0
0040B031  mov      word ptr [ebx + 0x10], 0x2c
0040B037  push     0
0040B039  push     0
0040B03B  call     0x407ed3
0040B040  add      esp, 8
0040B043  push     eax
0040B044  lea      eax, [ebp - 0x14]
0040B047  push     eax
0040B048  call     0x438e6e
0040B04D  add      esp, 8
0040B050  inc      dword ptr [ebx + 0x1c]
0040B053  lea      edx, [ebp - 0x14]
0040B056  push     edx
0040B057  call     0x407fe5
0040B05C  add      esp, 8
0040B05F  mov      ecx, dword ptr [edi]
0040B061  mov      dword ptr [ecx + 8], eax
0040B064  dec      dword ptr [ebx + 0x1c]
0040B067  push     2
0040B069  lea      eax, [ebp - 0x14]
0040B06C  push     eax
0040B06D  call     0x438f64
0040B072  add      esp, 8
0040B075  push     0
0040B077  mov      word ptr [ebx + 0x10], 0x38
0040B07D  push     0
0040B07F  push     0
0040B081  call     0x407ed3
0040B086  add      esp, 8
0040B089  push     eax
0040B08A  lea      edx, [ebp - 0x18]
0040B08D  push     edx
0040B08E  call     0x438e6e
0040B093  add      esp, 8
0040B096  inc      dword ptr [ebx + 0x1c]
0040B099  lea      ecx, [ebp - 0x18]
0040B09C  push     ecx
0040B09D  call     0x407fe5
0040B0A2  add      esp, 8
0040B0A5  mov      edx, dword ptr [edi]
0040B0A7  mov      dword ptr [edx + 0xc], eax
0040B0AA  dec      dword ptr [ebx + 0x1c]
0040B0AD  push     2
0040B0AF  lea      eax, [ebp - 0x18]
0040B0B2  push     eax
0040B0B3  call     0x438f64
0040B0B8  add      esp, 8
0040B0BB  push     0
0040B0BD  mov      word ptr [ebx + 0x10], 0x44
0040B0C3  push     0
0040B0C5  push     0
0040B0C7  call     0x407ed3
0040B0CC  add      esp, 8
0040B0CF  push     eax
0040B0D0  lea      ecx, [ebp - 0x1c]
0040B0D3  push     ecx
0040B0D4  call     0x438e6e
0040B0D9  add      esp, 8
0040B0DC  inc      dword ptr [ebx + 0x1c]
0040B0DF  lea      eax, [ebp - 0x1c]
0040B0E2  push     eax
0040B0E3  call     0x407fe5
0040B0E8  add      esp, 8
0040B0EB  mov      edx, dword ptr [edi]
0040B0ED  mov      dword ptr [edx + 0x10], eax
0040B0F0  dec      dword ptr [ebx + 0x1c]
0040B0F3  push     2
0040B0F5  lea      ecx, [ebp - 0x1c]
0040B0F8  push     ecx
0040B0F9  call     0x438f64
0040B0FE  add      esp, 8
0040B101  push     0
0040B103  mov      word ptr [ebx + 0x10], 0x50
0040B109  push     0
0040B10B  push     0
0040B10D  call     0x407ed3
0040B112  add      esp, 8
0040B115  push     eax
0040B116  lea      eax, [ebp - 0x20]
0040B119  push     eax
0040B11A  call     0x438e6e
0040B11F  add      esp, 8
0040B122  inc      dword ptr [ebx + 0x1c]
0040B125  lea      edx, [ebp - 0x20]
0040B128  push     edx
0040B129  call     0x407fe5
0040B12E  add      esp, 8
0040B131  mov      ecx, dword ptr [edi]
0040B133  mov      dword ptr [ecx + 0x14], eax
0040B136  dec      dword ptr [ebx + 0x1c]
0040B139  push     2
0040B13B  lea      eax, [ebp - 0x20]
0040B13E  push     eax
0040B13F  call     0x438f64
0040B144  add      esp, 8
0040B147  push     0
0040B149  mov      word ptr [ebx + 0x10], 0x5c
0040B14F  lea      edx, [ebp - 0x58]
0040B152  push     edx
0040B153  push     0
0040B155  call     0x407ed3
0040B15A  add      esp, 8
0040B15D  push     eax
0040B15E  lea      ecx, [ebp - 0x24]
0040B161  push     ecx
0040B162  call     0x438e6e
0040B167  add      esp, 8
0040B16A  inc      dword ptr [ebx + 0x1c]
0040B16D  lea      eax, [ebp - 0x24]
0040B170  push     eax
0040B171  call     0x407fe5
0040B176  add      esp, 8
0040B179  mov      edx, dword ptr [edi]
0040B17B  mov      word ptr [edx + 0x18], ax
0040B17F  dec      dword ptr [ebx + 0x1c]
0040B182  push     2
0040B184  lea      ecx, [ebp - 0x24]
0040B187  push     ecx
0040B188  call     0x438f64
0040B18D  add      esp, 8
0040B190  mov      word ptr [ebx + 0x10], 0x68
0040B196  push     0x43f76a
0040B19B  lea      eax, [ebp - 0x28]
0040B19E  push     eax
0040B19F  call     0x438e6e
0040B1A4  add      esp, 8
0040B1A7  inc      dword ptr [ebx + 0x1c]
0040B1AA  lea      edx, [ebp - 0x28]
0040B1AD  push     edx
0040B1AE  push     dword ptr [ebp - 0x58]
0040B1B1  lea      ecx, [ebp - 0x2c]
0040B1B4  push     ecx
0040B1B5  call     0x438e6e
0040B1BA  add      esp, 8
0040B1BD  inc      dword ptr [ebx + 0x1c]
0040B1C0  lea      eax, [ebp - 0x2c]
0040B1C3  push     eax
0040B1C4  lea      edx, [ebp - 0x30]
0040B1C7  push     edx
0040B1C8  call     0x40804e
0040B1CD  add      esp, 0xc
0040B1D0  lea      eax, [ebp - 0x30]
0040B1D3  inc      dword ptr [ebx + 0x1c]
0040B1D6  push     -1
0040B1D8  push     0
0040B1DA  push     eax
0040B1DB  mov      edx, dword ptr [edi]
0040B1DD  add      edx, 4
0040B1E0  push     edx
0040B1E1  call     0x438f04
0040B1E6  add      esp, 0x10
0040B1E9  dec      dword ptr [ebx + 0x1c]
0040B1EC  push     2
0040B1EE  lea      ecx, [ebp - 0x30]
0040B1F1  push     ecx
0040B1F2  call     0x438f64
0040B1F7  add      esp, 8
0040B1FA  dec      dword ptr [ebx + 0x1c]
0040B1FD  push     2
0040B1FF  lea      eax, [ebp - 0x2c]
0040B202  push     eax
0040B203  call     0x438f64
0040B208  add      esp, 8
0040B20B  dec      dword ptr [ebx + 0x1c]
0040B20E  push     2
0040B210  lea      edx, [ebp - 0x28]
0040B213  push     edx
0040B214  call     0x438f64
0040B219  add      esp, 8
0040B21C  push     esi
0040B21D  call     0x438f82
0040B222  pop      ecx
0040B223  mov      ecx, dword ptr [ebx]
0040B225  mov      dword ptr fs:[0], ecx
0040B22C  mov      eax, dword ptr [edi]
0040B22E  pop      edi
0040B22F  pop      esi
0040B230  pop      ebx
0040B231  mov      esp, ebp
0040B233  pop      ebp
0040B234  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438E6E
- 0x00438EC2
- 0x00439168
- 0x00438E6E
- 0x00407ED3
- 0x00438E6E
- 0x0040804E
- 0x00438F04
- 0x00438F64
- 0x00438F64
- 0x00438F64
- 0x00407ED3
- 0x00438E6E
- 0x00407FE5
- 0x00438F64
- 0x00407ED3
- 0x00438E6E
- 0x00407FE5
- 0x00438F64
- 0x00407ED3
- 0x00438E6E
- 0x00407FE5
- 0x00438F64
- 0x00407ED3
- 0x00438E6E
- 0x00407FE5
- 0x00438F64
- 0x00407ED3
- 0x00438E6E
- 0x00407FE5
- 0x00438F64
- 0x00407ED3
- 0x00438E6E
- 0x00407FE5
- 0x00438F64
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
