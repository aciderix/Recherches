# TVNCommand - Complete Extraction

**Structure**: TVNCommand
**TYPEINFO Address**: 0x0040EDC9
**Class Name**: TVNCommand *
**Destructor**: 0x0040ED19

---

## Destructor Analysis

**Function**: 0x0040ED19
**Instructions**: 132
**Size**: 256 bytes

### Assembly Code

```assembly
0040ED19  adc      byte ptr [eax], al
0040ED1B  add      byte ptr [eax], al
0040ED1D  add      eax, dword ptr [eax]
0040ED1F  xor      byte ptr [eax], al
0040ED21  add      byte ptr [eax], al
0040ED23  add      byte ptr [eax], al
0040ED25  ja       0x40ed27
0040ED27  add      byte ptr [eax], al
0040ED29  cmp      al, 0
0040ED2B  dec      esp
0040ED2C  add      byte ptr [eax], al
0040ED2E  add      byte ptr [eax], al
0040ED30  add      byte ptr [eax], al
0040ED32  add      byte ptr [eax], al
0040ED34  add      byte ptr [eax], al
0040ED36  add      byte ptr [eax], al
0040ED38  add      byte ptr [0x5000000], al
0040ED3E  add      byte ptr [eax], al
0040ED40  add      byte ptr [ecx - 0xc], dh
0040ED43  inc      eax
0040ED44  add      byte ptr [ecx], al
0040ED46  add      byte ptr [eax], dl
0040ED49  push     esp
0040ED4A  push     esi
0040ED4B  dec      esi
0040ED4C  inc      ebx
0040ED4D  outsd    dx, dword ptr [esi]
0040ED4E  insd     dword ptr es:[edi], dx
0040ED4F  insd     dword ptr es:[edi], dx
0040ED50  popal    
0040ED51  outsb    dx, byte ptr [esi]
0040ED52  add      byte ptr fs:[eax], al
0040ED55  jnp      0x40ed5b
0040ED57  inc      ecx
0040ED58  add      byte ptr [eax], al
0040ED5A  add      byte ptr [eax], al
0040ED5C  add      byte ptr [ebx], al
0040ED5E  add      byte ptr [eax], al
0040ED60  add      byte ptr [eax], al
0040ED62  add      byte ptr [eax], al
0040ED64  add      byte ptr [eax], al
0040ED66  add      byte ptr [eax], al
0040ED68  add      byte ptr [0xc00403c], ah
0040ED6E  add      byte ptr [eax], al
0040ED70  add      byte ptr [eax], al
0040ED72  add      byte ptr [eax], al
0040ED74  add      byte ptr [eax + eax], al
0040ED77  add      byte ptr [eax], al
0040ED79  nop      
0040ED7A  add      byte ptr [eax + eax], cl
0040ED7D  push     ss
0040ED7E  inc      eax
0040ED80  add      byte ptr [esi + edx*2 + 0x4e], dl
0040ED84  push     esp
0040ED85  js       0x40edfc
0040ED88  push     eax
0040ED89  popal    
0040ED8A  jb       0x40edf9
0040ED8C  jae      0x40edae
0040ED8E  sub      al, byte ptr [eax]
0040ED90  add      al, 0
0040ED92  add      byte ptr [eax], al
0040ED94  nop      
0040ED95  add      byte ptr [eax + eax], cl
0040ED98  jbe      0x40ed89
0040ED9A  inc      eax
0040ED9B  add      byte ptr [esi + edx*2 + 0x4e], dl
0040ED9F  push     esp
0040EDA0  js       0x40ee17
0040EDA3  dec      edi
0040EDA4  bound    ebp, qword ptr [edx + 0x50]
0040EDA7  popal    
0040EDA8  jb       0x40ee17
0040EDAA  jae      0x40edcc
0040EDAC  sub      al, byte ptr [eax]
0040EDAE  add      al, 0
0040EDB0  add      byte ptr [eax], al
0040EDB2  nop      
0040EDB3  add      byte ptr [eax + eax], cl
0040EDB6  outsb    dx, byte ptr [esi]
0040EDB7  inc      eax
0040EDB9  add      byte ptr [esi + edx*2 + 0x4e], dl
0040EDBD  inc      esi
0040EDBE  outsd    dx, dword ptr [esi]
0040EDBF  outsb    dx, byte ptr [esi]
0040EDC0  je       0x40ee12
0040EDC2  popal    
0040EDC3  jb       0x40ee32
0040EDC5  jae      0x40ede7
0040EDC7  sub      al, byte ptr [eax]
0040EDC9  add      al, 0
0040EDCB  add      byte ptr [eax], al
0040EDCD  nop      
0040EDCE  add      byte ptr [eax + eax], cl
0040EDD1  sbb      ebp, ebp
0040EDD3  inc      eax
0040EDD4  add      byte ptr [esi + edx*2 + 0x4e], dl
0040EDD8  inc      ebx
0040EDD9  outsd    dx, dword ptr [esi]
0040EDDA  insd     dword ptr es:[edi], dx
... (32 more instructions)
```

### Strings Referenced

- `"ms *"` @ 0x0040EDF9
- `"arms *"` @ 0x0040ED89
- `"tringParms"` @ 0x0040EE32

### DATA Context (Neighbor Strings)

**Context 0x0040ED79 - 0x0040EE79**:

- `"TVNTextParms *"` @ 0x0040ED81
- `"TVNTextObjParms *"` @ 0x0040ED9C
- `"TVNFontParms *"` @ 0x0040EDBA
- `"TVNCommand *"` @ 0x0040EDD5
- `"TVNSceneParms *"` @ 0x0040EDEE
- `"TVNStringParms"` @ 0x0040EE2E
- `"%<@"` @ 0x0040EE52

**Context 0x0040ED09 - 0x0040EE09**:

- `"TVNIfParms *"` @ 0x0040ED0C
- `"TVNCommand"` @ 0x0040ED49
- `"%<@"` @ 0x0040ED69
- `"TVNTextParms *"` @ 0x0040ED81
- `"TVNTextObjParms *"` @ 0x0040ED9C
- `"TVNFontParms *"` @ 0x0040EDBA
- `"TVNCommand *"` @ 0x0040EDD5
- `"TVNSceneParms *"` @ 0x0040EDEE

**Context 0x0040EDB2 - 0x0040EEB2**:

- `"TVNFontParms *"` @ 0x0040EDBA
- `"TVNCommand *"` @ 0x0040EDD5
- `"TVNSceneParms *"` @ 0x0040EDEE
- `"TVNStringParms"` @ 0x0040EE2E
- `"%<@"` @ 0x0040EE52
- `"TVNHtmlParms"` @ 0x0040EE8E

---

*Extracted with all expert fixes (#1-#6)*
