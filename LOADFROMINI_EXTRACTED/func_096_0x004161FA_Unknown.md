# LoadFromINI Function Analysis

**Function Address**: 0x004161FA
**Rank**: #96
**INI String Count**: 4
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 298

```assembly
004161FA  push     ebp
004161FB  mov      ebp, esp
004161FD  add      esp, 0xffffff74
00416203  push     ebx
00416204  push     esi
00416205  push     edi
00416206  mov      edi, dword ptr [ebp + 0x10]
00416209  mov      esi, dword ptr [ebp + 0xc]
0041620C  mov      ebx, dword ptr [ebp + 8]
0041620F  mov      eax, 0x441ca0
00416214  call     0x403618
00416219  push     ebx
0041621A  call     0x4159c4
0041621F  pop      ecx
00416220  cmp      dword ptr [edi + 4], 0x20000
00416227  sete     dl
0041622A  and      edx, 1
0041622D  test     dl, dl
0041622F  je       0x416240
00416231  push     esi
00416232  push     ebx
00416233  mov      ecx, dword ptr [ebx]
00416235  call     dword ptr [ecx + 0x10]
00416238  add      esp, 8
0041623B  jmp      0x4165b7
00416240  cmp      dword ptr [edi + 4], 0x2000a
00416247  setae    al
0041624A  and      eax, 1
0041624D  test     al, al
0041624F  je       0x4165b7
00416255  push     edi
00416256  push     esi
00416257  push     ebx
00416258  call     0x414ca1
0041625D  add      esp, 0xc
00416260  lea      edx, [ebx + 0x50]
00416263  mov      dword ptr [ebp - 0x34], edx
00416266  lea      ecx, [ebx + 0x40]
00416269  push     ecx
0041626A  lea      eax, [ebx + 0x64]
0041626D  mov      dword ptr [ebp - 0x3c], eax
00416270  lea      edx, [ebx + 0x34]
00416273  push     edx
00416274  lea      ecx, [ebx + 0x60]
00416277  mov      dword ptr [ebp - 0x44], ecx
0041627A  lea      eax, [ebx + 0x30]
0041627D  push     eax
0041627E  lea      edx, [ebx + 0x5c]
00416281  mov      dword ptr [ebp - 0x4c], edx
00416284  lea      ecx, [ebx + 0x2c]
00416287  push     ecx
00416288  lea      eax, [ebx + 0x58]
0041628B  mov      dword ptr [ebp - 0x54], eax
0041628E  lea      edx, [ebx + 0x28]
00416291  push     edx
00416292  lea      ecx, [ebx + 0x54]
00416295  mov      dword ptr [ebp - 0x5c], ecx
00416298  lea      eax, [ebx + 0x20]
0041629B  push     eax
0041629C  lea      edx, [ebx + 0x24]
0041629F  push     edx
004162A0  push     esi
004162A1  call     0x439138
004162A6  add      esp, 8
004162A9  push     eax
004162AA  call     0x439138
004162AF  add      esp, 8
004162B2  mov      dword ptr [ebp - 0x60], eax
004162B5  push     dword ptr [ebp - 0x60]
004162B8  call     0x439186
004162BD  pop      ecx
004162BE  mov      ecx, dword ptr [ebp - 0x5c]
004162C1  mov      dword ptr [ecx], eax
004162C3  mov      eax, dword ptr [ebp - 0x60]
004162C6  push     eax
004162C7  call     0x439138
004162CC  add      esp, 8
004162CF  mov      dword ptr [ebp - 0x58], eax
004162D2  push     dword ptr [ebp - 0x58]
004162D5  call     0x439186
004162DA  pop      ecx
004162DB  mov      edx, dword ptr [ebp - 0x54]
004162DE  mov      dword ptr [edx], eax
004162E0  mov      ecx, dword ptr [ebp - 0x58]
004162E3  push     ecx
004162E4  call     0x439138
004162E9  add      esp, 8
004162EC  mov      dword ptr [ebp - 0x50], eax
004162EF  push     dword ptr [ebp - 0x50]
004162F2  call     0x439186
004162F7  pop      ecx
004162F8  mov      edx, dword ptr [ebp - 0x4c]
004162FB  mov      dword ptr [edx], eax
004162FD  mov      eax, dword ptr [ebp - 0x50]
00416300  push     eax
00416301  call     0x439138
00416306  add      esp, 8
00416309  mov      dword ptr [ebp - 0x48], eax
0041630C  push     dword ptr [ebp - 0x48]
0041630F  call     0x439186
00416314  pop      ecx
00416315  mov      ecx, dword ptr [ebp - 0x44]
00416318  mov      dword ptr [ecx], eax
0041631A  mov      eax, dword ptr [ebp - 0x48]
0041631D  push     eax
0041631E  call     0x439138
00416323  add      esp, 8
00416326  mov      dword ptr [ebp - 0x40], eax
00416329  push     dword ptr [ebp - 0x40]
0041632C  call     0x439186
00416331  pop      ecx
00416332  mov      edx, dword ptr [ebp - 0x3c]
00416335  mov      dword ptr [edx], eax
00416337  mov      ecx, dword ptr [ebp - 0x40]
0041633A  push     ecx
0041633B  call     0x43913e
00416340  add      esp, 8
00416343  mov      dword ptr [ebp - 0x38], eax
00416346  push     dword ptr [ebp - 0x38]
00416349  call     0x439186
0041634E  pop      ecx
0041634F  mov      edx, dword ptr [ebp - 0x34]
00416352  mov      dword ptr [edx], eax
00416354  mov      dword ptr [ebp - 0x64], esi
00416357  push     dword ptr [ebp - 0x64]
0041635A  call     0x439180
0041635F  pop      ecx
00416360  test     eax, eax
00416362  setne    al
00416365  and      eax, 1
00416368  test     al, al
0041636A  je       0x4164e8
00416370  push     0x29
00416372  call     0x438eec
00416377  pop      ecx
00416378  mov      dword ptr [ebp - 4], eax
0041637B  test     eax, eax
0041637D  je       0x4164df
00416383  mov      word ptr [ebp - 0x20], 0x14
00416389  mov      dword ptr [ebp - 0x68], edi
0041638C  mov      dword ptr [ebp - 0x6c], esi
0041638F  mov      edx, dword ptr [ebp - 4]
00416392  xor      ecx, ecx
00416394  mov      dword ptr [edx], ecx
00416396  mov      eax, dword ptr [ebp - 4]
00416399  add      eax, 4
0041639C  mov      dword ptr [ebp - 0x70], eax
0041639F  mov      edx, dword ptr [ebp - 0x70]
004163A2  mov      dword ptr [edx + 1], 0x4401ac
004163A9  push     0x14
004163AB  call     0x438e50
004163B0  pop      ecx
004163B1  mov      dword ptr [ebp - 8], eax
004163B4  cmp      dword ptr [ebp - 8], 0
004163B8  je       0x4163e8
004163BA  mov      word ptr [ebp - 0x20], 0x20
004163C0  push     0x40f471
004163C5  push     1
004163C7  push     0x40f3ed
004163CC  push     0x211
004163D1  push     1
004163D3  push     0x10
004163D5  push     dword ptr [ebp - 8]
004163D8  call     0x4037e0
004163DD  add      esp, 0x1c
004163E0  mov      word ptr [ebp - 0x20], 0x14
004163E6  jmp      0x4163eb
004163E8  mov      eax, dword ptr [ebp - 8]
004163EB  mov      edx, dword ptr [ebp - 0x70]
004163EE  mov      dword ptr [edx + 5], eax
004163F1  mov      ecx, dword ptr [ebp - 0x70]
004163F4  mov      dword ptr [ecx + 9], 1
004163FB  inc      dword ptr [ebp - 0x14]
004163FE  mov      eax, dword ptr [ebp - 0x70]
00416401  mov      dword ptr [eax + 1], 0x4401c8
00416408  add      dword ptr [ebp - 0x14], 2
0041640C  mov      edx, dword ptr [ebp - 0x70]
0041640F  mov      dword ptr [edx + 1], 0x4401e4
00416416  mov      ecx, dword ptr [ebp - 0x70]
00416419  xor      eax, eax
0041641B  mov      dword ptr [ecx + 0xd], eax
0041641E  mov      edx, dword ptr [ebp - 0x70]
00416421  mov      dword ptr [edx + 0x11], 1
00416428  add      dword ptr [ebp - 0x14], 3
0041642C  add      dword ptr [ebp - 0x14], 4
00416430  add      dword ptr [ebp - 0x14], 5
00416434  add      dword ptr [ebp - 0x14], 6
00416438  add      dword ptr [ebp - 0x14], 7
0041643C  add      dword ptr [ebp - 0x14], 8
00416440  mov      ecx, dword ptr [ebp - 4]
00416443  add      ecx, 0x19
00416446  mov      dword ptr [ebp - 0x74], ecx
00416449  mov      eax, dword ptr [ebp - 0x74]
0041644C  mov      dword ptr [eax], 0x4402d4
00416452  inc      dword ptr [ebp - 0x14]
00416455  mov      edx, dword ptr [ebp - 0x74]
00416458  add      edx, 4
0041645B  mov      dword ptr [ebp - 0x78], edx
0041645E  mov      ecx, dword ptr [ebp - 0x78]
00416461  mov      dword ptr [ecx], 0x4402c0
00416467  inc      dword ptr [ebp - 0x14]
0041646A  mov      eax, dword ptr [ebp - 0x74]
0041646D  mov      dword ptr [eax], 0x4402e8
00416473  mov      edx, dword ptr [ebp - 0x74]
00416476  mov      dword ptr [edx + 4], 0x4402f8
0041647D  add      dword ptr [ebp - 0x14], 3
00416481  mov      ecx, dword ptr [ebp - 4]
00416484  mov      dword ptr [ecx + 0x21], 0x44016c
0041648B  mov      eax, dword ptr [ebp - 4]
0041648E  mov      dword ptr [eax + 0x19], 0x440188
00416495  mov      edx, dword ptr [ebp - 4]
00416498  mov      dword ptr [edx + 0x1d], 0x440198
0041649F  add      dword ptr [ebp - 0x14], 0xc
004164A3  mov      ecx, dword ptr [ebp - 4]
004164A6  mov      dword ptr [ecx + 0x21], 0x442db8
004164AD  mov      eax, dword ptr [ebp - 4]
004164B0  mov      dword ptr [eax + 0x19], 0x442dd4
004164B7  mov      edx, dword ptr [ebp - 4]
004164BA  mov      dword ptr [edx + 0x1d], 0x442de4
004164C1  push     dword ptr [ebp - 0x68]
004164C4  push     dword ptr [ebp - 0x6c]
004164C7  mov      ecx, dword ptr [ebp - 4]
004164CA  push     ecx
004164CB  mov      eax, dword ptr [ecx + 0x21]
004164CE  call     dword ptr [eax + 0x10]
004164D1  add      esp, 0xc
004164D4  mov      word ptr [ebp - 0x20], 8
004164DA  mov      edx, dword ptr [ebp - 4]
004164DD  jmp      0x4164e2
004164DF  mov      edx, dword ptr [ebp - 4]
004164E2  mov      dword ptr [ebx + 0x91], edx
004164E8  mov      dword ptr [ebp - 0x80], esi
004164EB  push     dword ptr [ebp - 0x80]
004164EE  call     0x439186
004164F3  pop      ecx
004164F4  mov      dword ptr [ebp - 0x7c], eax
004164F7  cmp      dword ptr [ebp - 0x7c], 0
004164FB  je       0x4165b7
00416501  push     0x20
00416503  call     0x438eec
00416508  pop      ecx
00416509  mov      dword ptr [ebp - 0xc], eax
0041650C  test     eax, eax
0041650E  je       0x41659a
00416514  mov      word ptr [ebp - 0x20], 0x38
0041651A  mov      dword ptr [ebp - 0x84], edi
00416520  mov      dword ptr [ebp - 0x88], esi
00416526  mov      ecx, dword ptr [ebp - 0xc]
00416529  mov      dword ptr [ecx], 0x4402d4
0041652F  inc      dword ptr [ebp - 0x14]
00416532  mov      eax, dword ptr [ebp - 0xc]
00416535  add      eax, 4
00416538  mov      dword ptr [ebp - 0x8c], eax
0041653E  mov      edx, dword ptr [ebp - 0x8c]
00416544  mov      dword ptr [edx], 0x4402c0
0041654A  inc      dword ptr [ebp - 0x14]
0041654D  mov      ecx, dword ptr [ebp - 0xc]
00416550  mov      dword ptr [ecx], 0x4402e8
00416556  mov      eax, dword ptr [ebp - 0xc]
00416559  mov      dword ptr [eax + 4], 0x4402f8
00416560  add      dword ptr [ebp - 0x14], 3
00416564  mov      edx, dword ptr [ebp - 0xc]
00416567  mov      dword ptr [edx], 0x442df8
0041656D  mov      ecx, dword ptr [ebp - 0xc]
00416570  mov      dword ptr [ecx + 4], 0x442e0c
00416577  push     dword ptr [ebp - 0x84]
0041657D  push     dword ptr [ebp - 0x88]
00416583  mov      eax, dword ptr [ebp - 0xc]
00416586  push     eax
00416587  mov      edx, dword ptr [eax]
00416589  call     dword ptr [edx + 8]
0041658C  add      esp, 0xc
0041658F  mov      word ptr [ebp - 0x20], 0x2c
00416595  mov      ecx, dword ptr [ebp - 0xc]
00416598  jmp      0x41659d
0041659A  mov      ecx, dword ptr [ebp - 0xc]
0041659D  mov      dword ptr [ebx + 0x95], ecx
004165A3  cmp      dword ptr [ebp - 0x7c], 0
004165A7  jge      0x4165b7
004165A9  mov      eax, dword ptr [ebp - 0x7c]
004165AC  neg      eax
004165AE  mov      edx, dword ptr [ebx + 0x95]
004165B4  mov      dword ptr [edx + 8], eax
004165B7  push     edi
004165B8  push     esi
004165B9  lea      eax, [ebx + 0x68]
004165BC  push     eax
004165BD  mov      edx, dword ptr [ebx + 0x8d]
004165C3  call     dword ptr [edx + 0x14]
004165C6  add      esp, 0xc
004165C9  mov      ecx, dword ptr [ebp - 0x30]
004165CC  mov      dword ptr fs:[0], ecx
004165D3  pop      edi
004165D4  pop      esi
004165D5  pop      ebx
004165D6  mov      esp, ebp
004165D8  pop      ebp
004165D9  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x004159C4
- 0x00414CA1
- 0x00439138
- 0x00439138
- 0x00439186
- 0x00439138
- 0x00439186
- 0x00439138
- 0x00439186
- 0x00439138
- 0x00439186
- 0x00439138
- 0x00439186
- 0x0043913E
- 0x00439186
- 0x00439180
- 0x00438EEC
- 0x00438E50
- 0x004037E0
- 0x00439186
- 0x00438EEC

---

*Extracted with recursive CALL following and DATA context*
