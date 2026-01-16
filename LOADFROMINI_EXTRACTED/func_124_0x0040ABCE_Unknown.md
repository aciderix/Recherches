# LoadFromINI Function Analysis

**Function Address**: 0x0040ABCE
**Rank**: #124
**INI String Count**: 3
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 211

```assembly
0040ABCE  push     ebp
0040ABCF  mov      ebp, esp
0040ABD1  add      esp, -0x48
0040ABD4  push     ebx
0040ABD5  push     esi
0040ABD6  lea      ebx, [ebp - 0x44]
0040ABD9  mov      eax, 0x43d95d
0040ABDE  call     0x403618
0040ABE3  mov      word ptr [ebx + 0x10], 8
0040ABE9  mov      edx, dword ptr [ebp + 8]
0040ABEC  mov      dword ptr [edx], 0x440458
0040ABF2  mov      ecx, dword ptr [ebp + 8]
0040ABF5  mov      dword ptr [ecx], 0x4402ac
0040ABFB  push     0x43fa1c
0040AC00  mov      eax, dword ptr [ebp + 8]
0040AC03  add      eax, 4
0040AC06  push     eax
0040AC07  call     0x438e6e
0040AC0C  add      esp, 8
0040AC0F  inc      dword ptr [ebx + 0x1c]
0040AC12  add      dword ptr [ebx + 0x1c], 2
0040AC16  mov      edx, dword ptr [ebp + 8]
0040AC19  mov      dword ptr [edx], 0x440298
0040AC1F  push     0
0040AC21  mov      ecx, dword ptr [ebp + 0xc]
0040AC24  mov      eax, dword ptr [ecx]
0040AC26  push     dword ptr [eax + 2]
0040AC29  call     0x439168
0040AC2E  add      esp, 8
0040AC31  mov      esi, eax
0040AC33  push     0
0040AC35  mov      word ptr [ebx + 0x10], 0x14
0040AC3B  push     0
0040AC3D  push     esi
0040AC3E  call     0x407ed3
0040AC43  add      esp, 8
0040AC46  push     eax
0040AC47  lea      eax, [ebp - 4]
0040AC4A  push     eax
0040AC4B  call     0x438e6e
0040AC50  add      esp, 8
0040AC53  inc      dword ptr [ebx + 0x1c]
0040AC56  lea      edx, [ebp - 4]
0040AC59  push     edx
0040AC5A  call     0x407fe5
0040AC5F  add      esp, 8
0040AC62  mov      ecx, dword ptr [ebp + 8]
0040AC65  mov      dword ptr [ecx + 8], eax
0040AC68  dec      dword ptr [ebx + 0x1c]
0040AC6B  push     2
0040AC6D  lea      eax, [ebp - 4]
0040AC70  push     eax
0040AC71  call     0x438f64
0040AC76  add      esp, 8
0040AC79  push     0
0040AC7B  mov      word ptr [ebx + 0x10], 0x20
0040AC81  push     0
0040AC83  push     0
0040AC85  call     0x407ed3
0040AC8A  add      esp, 8
0040AC8D  push     eax
0040AC8E  lea      edx, [ebp - 8]
0040AC91  push     edx
0040AC92  call     0x438e6e
0040AC97  add      esp, 8
0040AC9A  inc      dword ptr [ebx + 0x1c]
0040AC9D  lea      ecx, [ebp - 8]
0040ACA0  push     ecx
0040ACA1  call     0x407fe5
0040ACA6  add      esp, 8
0040ACA9  mov      edx, dword ptr [ebp + 8]
0040ACAC  mov      dword ptr [edx + 0xc], eax
0040ACAF  dec      dword ptr [ebx + 0x1c]
0040ACB2  push     2
0040ACB4  lea      eax, [ebp - 8]
0040ACB7  push     eax
0040ACB8  call     0x438f64
0040ACBD  add      esp, 8
0040ACC0  push     0
0040ACC2  mov      word ptr [ebx + 0x10], 0x2c
0040ACC8  push     0
0040ACCA  push     0
0040ACCC  call     0x407ed3
0040ACD1  add      esp, 8
0040ACD4  push     eax
0040ACD5  lea      ecx, [ebp - 0xc]
0040ACD8  push     ecx
0040ACD9  call     0x438e6e
0040ACDE  add      esp, 8
0040ACE1  inc      dword ptr [ebx + 0x1c]
0040ACE4  lea      eax, [ebp - 0xc]
0040ACE7  push     eax
0040ACE8  call     0x407fe5
0040ACED  add      esp, 8
0040ACF0  mov      edx, dword ptr [ebp + 8]
0040ACF3  mov      dword ptr [edx + 0x10], eax
0040ACF6  dec      dword ptr [ebx + 0x1c]
0040ACF9  push     2
0040ACFB  lea      ecx, [ebp - 0xc]
0040ACFE  push     ecx
0040ACFF  call     0x438f64
0040AD04  add      esp, 8
0040AD07  push     0
0040AD09  mov      word ptr [ebx + 0x10], 0x38
0040AD0F  push     0
0040AD11  push     0
0040AD13  call     0x407ed3
0040AD18  add      esp, 8
0040AD1B  push     eax
0040AD1C  lea      eax, [ebp - 0x10]
0040AD1F  push     eax
0040AD20  call     0x438e6e
0040AD25  add      esp, 8
0040AD28  inc      dword ptr [ebx + 0x1c]
0040AD2B  lea      edx, [ebp - 0x10]
0040AD2E  push     edx
0040AD2F  call     0x407fe5
0040AD34  add      esp, 8
0040AD37  mov      ecx, dword ptr [ebp + 8]
0040AD3A  mov      dword ptr [ecx + 0x14], eax
0040AD3D  dec      dword ptr [ebx + 0x1c]
0040AD40  push     2
0040AD42  lea      eax, [ebp - 0x10]
0040AD45  push     eax
0040AD46  call     0x438f64
0040AD4B  add      esp, 8
0040AD4E  push     0
0040AD50  mov      word ptr [ebx + 0x10], 0x44
0040AD56  lea      edx, [ebp - 0x48]
0040AD59  push     edx
0040AD5A  push     0
0040AD5C  call     0x407ed3
0040AD61  add      esp, 8
0040AD64  push     eax
0040AD65  lea      ecx, [ebp - 0x14]
0040AD68  push     ecx
0040AD69  call     0x438e6e
0040AD6E  add      esp, 8
0040AD71  inc      dword ptr [ebx + 0x1c]
0040AD74  lea      eax, [ebp - 0x14]
0040AD77  push     eax
0040AD78  call     0x407fe5
0040AD7D  add      esp, 8
0040AD80  mov      edx, dword ptr [ebp + 8]
0040AD83  mov      word ptr [edx + 0x18], ax
0040AD87  dec      dword ptr [ebx + 0x1c]
0040AD8A  push     2
0040AD8C  lea      ecx, [ebp - 0x14]
0040AD8F  push     ecx
0040AD90  call     0x438f64
0040AD95  add      esp, 8
0040AD98  mov      word ptr [ebx + 0x10], 0x50
0040AD9E  push     0x43f76a
0040ADA3  lea      eax, [ebp - 0x18]
0040ADA6  push     eax
0040ADA7  call     0x438e6e
0040ADAC  add      esp, 8
0040ADAF  inc      dword ptr [ebx + 0x1c]
0040ADB2  lea      edx, [ebp - 0x18]
0040ADB5  push     edx
0040ADB6  push     dword ptr [ebp - 0x48]
0040ADB9  lea      ecx, [ebp - 0x1c]
0040ADBC  push     ecx
0040ADBD  call     0x438e6e
0040ADC2  add      esp, 8
0040ADC5  inc      dword ptr [ebx + 0x1c]
0040ADC8  lea      eax, [ebp - 0x1c]
0040ADCB  push     eax
0040ADCC  lea      edx, [ebp - 0x20]
0040ADCF  push     edx
0040ADD0  call     0x40804e
0040ADD5  add      esp, 0xc
0040ADD8  lea      eax, [ebp - 0x20]
0040ADDB  inc      dword ptr [ebx + 0x1c]
0040ADDE  push     -1
0040ADE0  push     0
0040ADE2  push     eax
0040ADE3  mov      edx, dword ptr [ebp + 8]
0040ADE6  add      edx, 4
0040ADE9  push     edx
0040ADEA  call     0x438f04
0040ADEF  add      esp, 0x10
0040ADF2  dec      dword ptr [ebx + 0x1c]
0040ADF5  push     2
0040ADF7  lea      ecx, [ebp - 0x20]
0040ADFA  push     ecx
0040ADFB  call     0x438f64
0040AE00  add      esp, 8
0040AE03  dec      dword ptr [ebx + 0x1c]
0040AE06  push     2
0040AE08  lea      eax, [ebp - 0x1c]
0040AE0B  push     eax
0040AE0C  call     0x438f64
0040AE11  add      esp, 8
0040AE14  dec      dword ptr [ebx + 0x1c]
0040AE17  push     2
0040AE19  lea      edx, [ebp - 0x18]
0040AE1C  push     edx
0040AE1D  call     0x438f64
0040AE22  add      esp, 8
0040AE25  push     esi
0040AE26  call     0x438f82
0040AE2B  pop      ecx
0040AE2C  mov      ecx, dword ptr [ebx]
0040AE2E  mov      dword ptr fs:[0], ecx
0040AE35  mov      eax, dword ptr [ebp + 8]
0040AE38  pop      esi
0040AE39  pop      ebx
0040AE3A  mov      esp, ebp
0040AE3C  pop      ebp
0040AE3D  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00438E6E
- 0x00439168
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
