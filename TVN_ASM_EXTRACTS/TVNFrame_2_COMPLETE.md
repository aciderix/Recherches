# TVNFrame_2 - Complete Assembly Extraction

**Vtable Address**: 0x00435DD4
**Binary**: europeo.exe
**Tool**: radare2 5.5.0
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

### Assembly Code

```assembly
            [31m[31m; CALL XREF from fcn.0042d8b6 @ [31m+0x676[31m[0m
[36m┌[0m 101: [31mfcn.0042d3bd[0m (int32_t arg_8h, int32_t arg_ch);
[36m│[0m           [37m; [37mvar [34mint32_t var_28h [36m@ ebp-0x28[0m
[36m│[0m           [37m; [37mvar [34mint32_t var_18h [36m@ ebp-0x18[0m
[36m│[0m           [37m; [37mvar [34muint32_t var_4h [36m@ ebp-0x4[0m
[36m│[0m           [37m; [37marg [34mint32_t arg_8h [36m@ ebp+0x8[0m
[36m│[0m           [37m; [37marg [34mint32_t arg_ch [36m@ ebp+0xc[0m
[36m│[0m           [32m0x0042d3bd[0m      [33m55[0m             [35mpush[36m ebp[0m[0m[0m
[36m│[0m           [32m0x0042d3be[0m      [37m8b[37mec[0m           [37mmov[36m ebp[0m,[36m[36m esp[0m[0m[0m
[36m│[0m           [32m0x0042d3c0[0m      [37m83[37mc4[37md8[0m         [33madd[36m esp[0m,[36m[36m [33m0xffffffd8[0m[0m[0m
[36m│[0m           [32m0x0042d3c3[0m      [33m53[0m             [35mpush[36m ebx[0m[0m[0m
[36m│[0m           [32m0x0042d3c4[0m      [37m8b[33m5d[37m08[0m         [37mmov[36m ebx[0m,[36m dword[36m [0m[[34marg_8h[0m][36m[0m[0m[0m
[36m│[0m           [32m0x0042d3c7[0m      [37mb8[37m84[37ma4[33m44[32m00[0m     [37mmov[36m eax[0m,[36m[36m [33m0x44a484[0m[0m[0m
[36m│[0m           [32m0x0042d3cc[0m      [37me8[33m47[33m62[37mfd[31mff[0m     [1;92mcall fcn.00403618[0m[0m
[36m│[0m           [32m0x0042d3d1[0m      [37m85[37mdb[0m           [33mtest[36m ebx[0m,[36m[36m ebx[0m[0m[0m
[36m│[0m       [36m┌[0m[36m─[0m[36m<[0m [32m0x0042d3d3[0m      [33m74[33m3e[0m           [32mje 0x42d413[0m[0m
[36m│[0m       [36m│[0m   [32m0x0042d3d5[0m      [37m8b[33m53[37m04[0m         [37mmov[36m edx[0m,[36m dword [0m[[36mebx [0m+[36m[36m [33m4[0m][36m[0m[0m[0m
[36m│[0m       [36m│[0m   [32m0x0042d3d8[0m      [37m89[33m55[37mfc[0m         [37mmov dword[36m [0m[[34mvar_4h[0m][36m[0m,[36m[36m edx[0m[0m[0m
[36m│[0m       [36m│[0m   [32m0x0042d3db[0m      [37m83[33m7d[37mfc[32m00[0m       [33mcmp dword[36m [0m[[34mvar_4h[0m][36m[0m,[36m[36m [36m0[0m[0m[0m
[36m│[0m      [36m┌[0m[36m─[0m[36m─[0m[36m<[0m [32m0x0042d3df[0m      [33m74[37m19[0m           [32mje 0x42d3fa[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d3e1[0m      [33m66[37mc7[33m45[37me8[37m14[32m00[0m   [37mmov word[36m [0m[[34mvar_18h[0m][36m[0m,[36m[36m [33m0x14[0m[0m[31m    [31m; 20[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d3e7[0m      [33m6a[37m03[0m           [35mpush[36m [33m3[0m[0m[31m                      [31m; 3[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d3e9[0m      [37m8b[33m4d[37mfc[0m         [37mmov[36m ecx[0m,[36m dword[36m [0m[[34mvar_4h[0m][36m[0m[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d3ec[0m      [33m51[0m             [35mpush[36m ecx[0m[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d3ed[0m      [37m8b[37m01[0m           [37mmov[36m eax[0m,[36m dword[36m [0m[[36mecx[0m][36m[0m[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d3ef[0m      [31mff[37m10[0m           [32mcall dword [eax][0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d3f1[0m      [37m83[37mc4[37m08[0m         [33madd[36m esp[0m,[36m[36m [33m8[0m[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d3f4[0m      [33m66[37mc7[33m45[37me8[37m08[32m00[0m   [37mmov word[36m [0m[[34mvar_18h[0m][36m[0m,[36m[36m [33m8[0m[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [31m[31m; CODE XREF from fcn.0042d3bd @ [31m0x42d3df[31m[0m
[36m│[0m      [36m└[0m[36m─[0m[36m─[0m[36m>[0m [32m0x0042d3fa[0m      [33m33[37md2[0m           [33mxor[36m edx[0m,[36m[36m edx[0m[0m[0m
[36m│[0m       [36m│[0m   [32m0x0042d3fc[0m      [37m89[33m53[37m04[0m         [37mmov dword [0m[[36mebx [0m+[36m[36m [33m4[0m][36m[0m,[36m[36m edx[0m[0m[0m
[36m│[0m       [36m│[0m   [32m0x0042d3ff[0m      [33m53[0m             [35mpush[36m ebx[0m[0m[0m
[36m│[0m       [36m│[0m   [32m0x0042d400[0m      [37me8[37m86[37ma8[37mfd[31mff[0m     [1;92mcall fcn.00407c8b[0m[0m
[36m│[0m       [36m│[0m   [32m0x0042d405[0m      [33m59[0m             [35mpop[36m ecx[0m[0m[0m
[36m│[0m       [36m│[0m   [32m0x0042d406[0m      [37mf6[33m45[37m0c[37m01[0m       [33mtest byte[36m [0m[[34marg_ch[0m][36m[0m,[36m[36m [33m1[0m[0m[0m
[36m│[0m      [36m┌[0m[36m─[0m[36m─[0m[36m<[0m [32m0x0042d40a[0m      [33m74[37m07[0m           [32mje 0x42d413[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d40c[0m      [33m53[0m             [35mpush[36m ebx[0m[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d40d[0m      [37me8[37m04[37mbb[32m00[32m00[0m     [1;92mcall sub.cw3230mt.DLL___bdele_qpv[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [32m0x0042d412[0m      [33m59[0m             [35mpop[36m ecx[0m[0m[0m
[36m│[0m      [36m│[0m[36m│[0m   [31m[31m; CODE XREFS from fcn.0042d3bd @ [31m0x42d3d3[31m, 0x42d40a[31m[0m
[36m│[0m      [36m└[0m[36m└[0m[36m─[0m[36m>[0m [32m0x0042d413[0m      [37m8b[33m4d[37md8[0m         [37mmov[36m ecx[0m,[36m dword[36m [0m[[34mvar_28h[0m][36m[0m[0m[0m
[36m│[0m           [32m0x0042d416[0m      [33m64[37m89[37m0d[32m00[32m00[32m00[37m.[0m  [37mmov dword[36m fs:[0m[[36m[36m0[0m][36m[0m,[36m[36m ecx[0m[0m[0m
[36m│[0m           [32m0x0042d41d[0m      [33m5b[0m             [35mpop[36m ebx[0m[0m[0m
[36m│[0m           [32m0x0042d41e[0m      [37m8b[37me5[0m           [37mmov[36m esp[0m,[36m[36m ebp[0m[0m[0m
[36m│[0m           [32m0x0042d420[0m      [33m5d[0m             [35mpop[36m ebp[0m[0m[0m
[36m└[0m           [32m0x0042d421[0m      [37mc3[0m             [31mret[0m[0m[0m
```

### Function Calls

**Other Calls**:

- `X`
- `fcn.00403618`
- `d`
- `fcn.00407c8b`

---

## Method [1]: 0x00480001

**Address**: 0x00480001
**Index in vtable**: 1

### Assembly Code

```assembly
```

---

