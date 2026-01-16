# LoadFromINI Function Analysis

**Function Address**: 0x0041DB36
**Rank**: #147
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 283

```assembly
0041DB36  push     ebp
0041DB37  mov      ebp, esp
0041DB39  add      esp, 0xffffff44
0041DB3F  push     ebx
0041DB40  push     esi
0041DB41  push     edi
0041DB42  mov      edi, dword ptr [ebp + 0x18]
0041DB45  mov      ebx, dword ptr [ebp + 8]
0041DB48  mov      eax, 0x4445ec
0041DB4D  call     0x403618
0041DB52  push     0x21
0041DB54  call     0x438eec
0041DB59  pop      ecx
0041DB5A  mov      dword ptr [ebp - 4], eax
0041DB5D  test     eax, eax
0041DB5F  je       0x41db80
0041DB61  mov      word ptr [ebp - 0x1c], 0x14
0041DB67  push     dword ptr [ebp + 0xc]
0041DB6A  push     dword ptr [ebp - 4]
0041DB6D  call     0x439798
0041DB72  add      esp, 8
0041DB75  mov      word ptr [ebp - 0x1c], 8
0041DB7B  mov      esi, dword ptr [ebp - 4]
0041DB7E  jmp      0x41db83
0041DB80  mov      esi, dword ptr [ebp - 4]
0041DB83  cmp      dword ptr [ebx + 8], 0
0041DB87  je       0x41dd66
0041DB8D  mov      eax, dword ptr [ebx + 4]
0041DB90  push     eax
0041DB91  mov      edx, dword ptr [eax + 5]
0041DB94  call     dword ptr [edx + 4]
0041DB97  pop      ecx
0041DB98  cmp      edi, eax
0041DB9A  jne      0x41dc5f
0041DBA0  mov      ecx, dword ptr [ebx + 4]
0041DBA3  push     ecx
0041DBA4  mov      eax, dword ptr [ecx + 5]
0041DBA7  call     dword ptr [eax + 8]
0041DBAA  pop      ecx
0041DBAB  cmp      eax, dword ptr [ebp + 0x1c]
0041DBAE  jne      0x41dc5f
0041DBB4  push     dword ptr [ebx + 8]
0041DBB7  push     esi
0041DBB8  call     0x43977a
0041DBBD  add      esp, 8
0041DBC0  mov      dword ptr [ebp - 0x34], esi
0041DBC3  mov      edx, dword ptr [ebp + 0x1c]
0041DBC6  mov      dword ptr [ebp - 0x38], edx
0041DBC9  mov      dword ptr [ebp - 0x3c], edi
0041DBCC  mov      ecx, dword ptr [ebp + 0x14]
0041DBCF  mov      dword ptr [ebp - 0x40], ecx
0041DBD2  mov      eax, dword ptr [ebp + 0x10]
0041DBD5  mov      dword ptr [ebp - 0x44], eax
0041DBD8  push     0x8800c6
0041DBDD  push     0
0041DBDF  push     0
0041DBE1  mov      edx, dword ptr [ebp - 0x34]
0041DBE4  push     dword ptr [edx]
0041DBE6  push     dword ptr [ebp - 0x38]
0041DBE9  push     dword ptr [ebp - 0x3c]
0041DBEC  push     dword ptr [ebp - 0x40]
0041DBEF  push     dword ptr [ebp - 0x44]
0041DBF2  mov      ecx, dword ptr [ebp + 0xc]
0041DBF5  push     dword ptr [ecx]
0041DBF7  call     0x43982e
0041DBFC  test     eax, eax
0041DBFE  setne    al
0041DC01  and      eax, 1
0041DC04  mov      byte ptr [ebp - 0x2d], al
0041DC07  push     dword ptr [ebx + 4]
0041DC0A  push     esi
0041DC0B  call     0x43977a
0041DC10  add      esp, 8
0041DC13  mov      dword ptr [ebp - 0x48], esi
0041DC16  mov      edx, dword ptr [ebp + 0x1c]
0041DC19  mov      dword ptr [ebp - 0x4c], edx
0041DC1C  mov      dword ptr [ebp - 0x50], edi
0041DC1F  mov      ecx, dword ptr [ebp + 0x14]
0041DC22  mov      dword ptr [ebp - 0x54], ecx
0041DC25  mov      eax, dword ptr [ebp + 0x10]
0041DC28  mov      dword ptr [ebp - 0x58], eax
0041DC2B  push     0xee0086
0041DC30  push     0
0041DC32  push     0
0041DC34  mov      edx, dword ptr [ebp - 0x48]
0041DC37  push     dword ptr [edx]
0041DC39  push     dword ptr [ebp - 0x4c]
0041DC3C  push     dword ptr [ebp - 0x50]
0041DC3F  push     dword ptr [ebp - 0x54]
0041DC42  push     dword ptr [ebp - 0x58]
0041DC45  mov      ecx, dword ptr [ebp + 0xc]
0041DC48  push     dword ptr [ecx]
0041DC4A  call     0x43982e
0041DC4F  test     eax, eax
0041DC51  setne    al
0041DC54  and      eax, 1
0041DC57  or       byte ptr [ebp - 0x2d], al
0041DC5A  jmp      0x41de84
0041DC5F  push     dword ptr [ebx + 8]
0041DC62  push     esi
0041DC63  call     0x43977a
0041DC68  add      esp, 8
0041DC6B  mov      edx, dword ptr [ebx + 4]
0041DC6E  push     edx
0041DC6F  mov      ecx, dword ptr [edx + 5]
0041DC72  call     dword ptr [ecx + 8]
0041DC75  pop      ecx
0041DC76  mov      dword ptr [ebp - 0x5c], eax
0041DC79  mov      eax, dword ptr [ebx + 4]
0041DC7C  push     eax
0041DC7D  mov      edx, dword ptr [eax + 5]
0041DC80  call     dword ptr [edx + 4]
0041DC83  pop      ecx
0041DC84  mov      dword ptr [ebp - 0x60], eax
0041DC87  mov      dword ptr [ebp - 0x64], esi
0041DC8A  mov      ecx, dword ptr [ebp + 0x1c]
0041DC8D  mov      dword ptr [ebp - 0x68], ecx
0041DC90  mov      dword ptr [ebp - 0x6c], edi
0041DC93  mov      eax, dword ptr [ebp + 0x14]
0041DC96  mov      dword ptr [ebp - 0x70], eax
0041DC99  mov      edx, dword ptr [ebp + 0x10]
0041DC9C  mov      dword ptr [ebp - 0x74], edx
0041DC9F  push     0x8800c6
0041DCA4  push     dword ptr [ebp - 0x5c]
0041DCA7  push     dword ptr [ebp - 0x60]
0041DCAA  push     0
0041DCAC  push     0
0041DCAE  mov      ecx, dword ptr [ebp - 0x64]
0041DCB1  push     dword ptr [ecx]
0041DCB3  push     dword ptr [ebp - 0x68]
0041DCB6  push     dword ptr [ebp - 0x6c]
0041DCB9  push     dword ptr [ebp - 0x70]
0041DCBC  push     dword ptr [ebp - 0x74]
0041DCBF  mov      eax, dword ptr [ebp + 0xc]
0041DCC2  push     dword ptr [eax]
0041DCC4  call     0x4397b0
0041DCC9  test     eax, eax
0041DCCB  setne    dl
0041DCCE  and      edx, 1
0041DCD1  mov      byte ptr [ebp - 0x2d], dl
0041DCD4  push     dword ptr [ebx + 4]
0041DCD7  push     esi
0041DCD8  call     0x43977a
0041DCDD  add      esp, 8
0041DCE0  mov      ecx, dword ptr [ebx + 4]
0041DCE3  push     ecx
0041DCE4  mov      eax, dword ptr [ecx + 5]
0041DCE7  call     dword ptr [eax + 8]
0041DCEA  pop      ecx
0041DCEB  mov      dword ptr [ebp - 0x78], eax
0041DCEE  mov      edx, dword ptr [ebx + 4]
0041DCF1  push     edx
0041DCF2  mov      ecx, dword ptr [edx + 5]
0041DCF5  call     dword ptr [ecx + 4]
0041DCF8  pop      ecx
0041DCF9  mov      dword ptr [ebp - 0x7c], eax
0041DCFC  mov      dword ptr [ebp - 0x80], esi
0041DCFF  mov      eax, dword ptr [ebp + 0x1c]
0041DD02  mov      dword ptr [ebp - 0x84], eax
0041DD08  mov      dword ptr [ebp - 0x88], edi
0041DD0E  mov      edx, dword ptr [ebp + 0x14]
0041DD11  mov      dword ptr [ebp - 0x8c], edx
0041DD17  mov      ecx, dword ptr [ebp + 0x10]
0041DD1A  mov      dword ptr [ebp - 0x90], ecx
0041DD20  push     0xee0086
0041DD25  push     dword ptr [ebp - 0x78]
0041DD28  push     dword ptr [ebp - 0x7c]
0041DD2B  push     0
0041DD2D  push     0
0041DD2F  mov      eax, dword ptr [ebp - 0x80]
0041DD32  push     dword ptr [eax]
0041DD34  push     dword ptr [ebp - 0x84]
0041DD3A  push     dword ptr [ebp - 0x88]
0041DD40  push     dword ptr [ebp - 0x8c]
0041DD46  push     dword ptr [ebp - 0x90]
0041DD4C  mov      edx, dword ptr [ebp + 0xc]
0041DD4F  push     dword ptr [edx]
0041DD51  call     0x4397b0
0041DD56  test     eax, eax
0041DD58  setne    cl
0041DD5B  and      ecx, 1
0041DD5E  or       byte ptr [ebp - 0x2d], cl
0041DD61  jmp      0x41de84
0041DD66  push     dword ptr [ebx + 4]
0041DD69  push     esi
0041DD6A  call     0x43977a
0041DD6F  add      esp, 8
0041DD72  mov      eax, dword ptr [ebx + 4]
0041DD75  push     eax
0041DD76  mov      edx, dword ptr [eax + 5]
0041DD79  call     dword ptr [edx + 4]
0041DD7C  pop      ecx
0041DD7D  cmp      edi, eax
0041DD7F  jne      0x41ddf1
0041DD81  mov      ecx, dword ptr [ebx + 4]
0041DD84  push     ecx
0041DD85  mov      eax, dword ptr [ecx + 5]
0041DD88  call     dword ptr [eax + 8]
0041DD8B  pop      ecx
0041DD8C  cmp      eax, dword ptr [ebp + 0x1c]
0041DD8F  jne      0x41ddf1
0041DD91  mov      ebx, esi
0041DD93  mov      edx, dword ptr [ebp + 0x1c]
0041DD96  mov      dword ptr [ebp - 0x94], edx
0041DD9C  mov      dword ptr [ebp - 0x98], edi
0041DDA2  mov      ecx, dword ptr [ebp + 0x14]
0041DDA5  mov      dword ptr [ebp - 0x9c], ecx
0041DDAB  mov      eax, dword ptr [ebp + 0x10]
0041DDAE  mov      dword ptr [ebp - 0xa0], eax
0041DDB4  push     0xcc0020
0041DDB9  push     0
0041DDBB  push     0
0041DDBD  push     dword ptr [ebx]
0041DDBF  push     dword ptr [ebp - 0x94]
0041DDC5  push     dword ptr [ebp - 0x98]
0041DDCB  push     dword ptr [ebp - 0x9c]
0041DDD1  push     dword ptr [ebp - 0xa0]
0041DDD7  mov      edx, dword ptr [ebp + 0xc]
0041DDDA  push     dword ptr [edx]
0041DDDC  call     0x43982e
0041DDE1  test     eax, eax
0041DDE3  setne    cl
0041DDE6  and      ecx, 1
0041DDE9  mov      byte ptr [ebp - 0x2d], cl
0041DDEC  jmp      0x41de84
0041DDF1  mov      eax, dword ptr [ebx + 4]
0041DDF4  push     eax
0041DDF5  mov      edx, dword ptr [eax + 5]
0041DDF8  call     dword ptr [edx + 8]
0041DDFB  pop      ecx
0041DDFC  mov      dword ptr [ebp - 0xa4], eax
0041DE02  mov      ecx, dword ptr [ebx + 4]
0041DE05  push     ecx
0041DE06  mov      eax, dword ptr [ecx + 5]
0041DE09  call     dword ptr [eax + 4]
0041DE0C  pop      ecx
0041DE0D  mov      dword ptr [ebp - 0xa8], eax
0041DE13  mov      dword ptr [ebp - 0xac], esi
0041DE19  mov      edx, dword ptr [ebp + 0x1c]
0041DE1C  mov      dword ptr [ebp - 0xb0], edx
0041DE22  mov      dword ptr [ebp - 0xb4], edi
0041DE28  mov      ecx, dword ptr [ebp + 0x14]
0041DE2B  mov      dword ptr [ebp - 0xb8], ecx
0041DE31  mov      eax, dword ptr [ebp + 0x10]
0041DE34  mov      dword ptr [ebp - 0xbc], eax
0041DE3A  push     0xcc0020
0041DE3F  push     dword ptr [ebp - 0xa4]
0041DE45  push     dword ptr [ebp - 0xa8]
0041DE4B  push     0
0041DE4D  push     0
0041DE4F  mov      edx, dword ptr [ebp - 0xac]
0041DE55  push     dword ptr [edx]
0041DE57  push     dword ptr [ebp - 0xb0]
0041DE5D  push     dword ptr [ebp - 0xb4]
0041DE63  push     dword ptr [ebp - 0xb8]
0041DE69  push     dword ptr [ebp - 0xbc]
0041DE6F  mov      ecx, dword ptr [ebp + 0xc]
0041DE72  push     dword ptr [ecx]
0041DE74  call     0x4397b0
0041DE79  test     eax, eax
0041DE7B  setne    al
0041DE7E  and      eax, 1
0041DE81  mov      byte ptr [ebp - 0x2d], al
0041DE84  mov      dword ptr [ebp - 8], esi
0041DE87  cmp      dword ptr [ebp - 8], 0
0041DE8B  je       0x41dea7
0041DE8D  mov      word ptr [ebp - 0x1c], 0x2c
0041DE93  push     3
0041DE95  mov      edx, dword ptr [ebp - 8]
0041DE98  push     edx
0041DE99  mov      ecx, dword ptr [edx + 5]
0041DE9C  call     dword ptr [ecx]
0041DE9E  add      esp, 8
0041DEA1  mov      word ptr [ebp - 0x1c], 0x20
0041DEA7  mov      al, byte ptr [ebp - 0x2d]
0041DEAA  mov      edx, dword ptr [ebp - 0x2c]
0041DEAD  mov      dword ptr fs:[0], edx
0041DEB4  pop      edi
0041DEB5  pop      esi
0041DEB6  pop      ebx
0041DEB7  mov      esp, ebp
0041DEB9  pop      ebp
0041DEBA  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438EEC
- 0x00439798
- 0x0043977A
- 0x0043982E
- 0x0043977A
- 0x0043982E
- 0x0043977A
- 0x004397B0
- 0x0043977A
- 0x004397B0
- 0x0043977A
- 0x0043982E
- 0x004397B0

---

*Extracted with recursive CALL following and DATA context*
