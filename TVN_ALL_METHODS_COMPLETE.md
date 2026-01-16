# Complete TVN Methods Extraction

Comprehensive extraction of all vtables and methods from 35 TVN structures.

**Binary**: DOCS/europeo.exe
**Date**: 2026-01-16
**Method**: Type string proximity search

---

## Summary

| Structure | Vtables Found | Total Methods |
|-----------|---------------|---------------|
| ✗ TVNApplication                 |  0 |   0 |
| ✗ TVNAviMedia                    |  0 |   0 |
| ✗ TVNBitmap                      |  0 |   0 |
| ✗ TVNBmpImg                      |  0 |   0 |
| ✗ TVNCDAMedia                    |  0 |   0 |
| ✓ TVNCommand                     |  1 |   2 |
| ✓ TVNDigitParms                  |  1 |   2 |
| ✗ TVNEventCommand                |  0 |   0 |
| ✓ TVNExecParms                   |  1 |   2 |
| ✗ TVNFileNameParms               |  0 |   0 |
| ✓ TVNFontParms                   |  1 |   2 |
| ✓ TVNFrame                       |  2 |   4 |
| ✗ TVNGdiObject                   |  0 |   0 |
| ✓ TVNHotspot                     |  1 |   2 |
| ✓ TVNHtmlParms                   |  1 |   2 |
| ✗ TVNHtmlText                    |  0 |   0 |
| ✓ TVNIfParms                     |  1 |   2 |
| ✓ TVNImageObject                 |  2 |   4 |
| ✓ TVNImageParms                  |  1 |   2 |
| ✓ TVNImgObjParms                 |  1 |   2 |
| ✓ TVNImgSeqParms                 |  1 |   2 |
| ✗ TVNMidiMedia                   |  0 |   0 |
| ✓ TVNMidiParms                   |  1 |   2 |
| ✓ TVNProjectParms                |  1 |   2 |
| ✗ TVNScene                       |  0 |   0 |
| ✓ TVNSceneParms                  |  1 |   2 |
| ✓ TVNSetVarParms                 |  1 |   2 |
| ✓ TVNStringParms                 |  1 |   2 |
| ✓ TVNTextObjParms                |  1 |   2 |
| ✓ TVNTextObject                  |  2 |   4 |
| ✓ TVNTextParms                   |  1 |   2 |
| ✗ TVNTimer                       |  0 |   0 |
| ✗ TVNToolBar                     |  0 |   0 |
| ✗ TVNVariable                    |  0 |   0 |
| ✗ TVNWaveMedia                   |  0 |   0 |
| ✗ TVNWindow                      |  0 |   0 |

**Total**: 23 vtables, 46 methods

---

## Detailed Methods

### TVNCommand

**Type String Offset**: 0x0000e3d5

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNCommand_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNDigitParms

**Type String Offset**: 0x0000e247

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNDigitParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNExecParms

**Type String Offset**: 0x0000e2d4

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNExecParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNFontParms

**Type String Offset**: 0x0000e3ba

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNFontParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNFrame

**Type String Offset**: 0x0003603c

#### Vtable #1

- **File Offset**: 0x00035b50
- **Virtual Address**: 0x00435b50
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0042d471 | Virtual[0] - Destructor |
|  1 | 0x00440001 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNFrame_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0042d471
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440001
};
```

#### Vtable #2

- **File Offset**: 0x00035dd4
- **Virtual Address**: 0x00435dd4
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0042d3bd | Virtual[0] - Destructor |
|  1 | 0x00480001 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNFrame_vtable_2 {
    void* method0_Destructor; // [ 0] @ 0x0042d3bd
    void* method1_Load_Parse_Init; // [ 1] @ 0x00480001
};
```

---

### TVNHotspot

**Type String Offset**: 0x000135bc

#### Vtable #1

- **File Offset**: 0x00013514
- **Virtual Address**: 0x00413514
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x00440460 | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNHotspot_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x00440460
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNHtmlParms

**Type String Offset**: 0x0000e263

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNHtmlParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNIfParms

**Type String Offset**: 0x0000e30c

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNIfParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNImageObject

**Type String Offset**: 0x00029a17

#### Vtable #1

- **File Offset**: 0x00029980
- **Virtual Address**: 0x00429980
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0042a738 | Virtual[0] - Destructor |
|  1 | 0x00440001 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNImageObject_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0042a738
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440001
};
```

#### Vtable #2

- **File Offset**: 0x000299d0
- **Virtual Address**: 0x004299d0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x00439612 | Virtual[0] - Destructor |
|  1 | 0x004c0001 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNImageObject_vtable_2 {
    void* method0_Destructor; // [ 0] @ 0x00439612
    void* method1_Load_Parse_Init; // [ 1] @ 0x004c0001
};
```

---

### TVNImageParms

**Type String Offset**: 0x0000e27e

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNImageParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNImgObjParms

**Type String Offset**: 0x0000e29a

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNImgObjParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNImgSeqParms

**Type String Offset**: 0x0000e2b7

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNImgSeqParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNMidiParms

**Type String Offset**: 0x0000e22c

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNMidiParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNProjectParms

**Type String Offset**: 0x0000e20e

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNProjectParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNSceneParms

**Type String Offset**: 0x0000e3ee

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNSceneParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNSetVarParms

**Type String Offset**: 0x0000e2ef

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNSetVarParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNStringParms

**Type String Offset**: 0x0000e40a

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNStringParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNTextObjParms

**Type String Offset**: 0x0000e39c

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNTextObjParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

### TVNTextObject

**Type String Offset**: 0x00029a54

#### Vtable #1

- **File Offset**: 0x00029980
- **Virtual Address**: 0x00429980
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0042a738 | Virtual[0] - Destructor |
|  1 | 0x00440001 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNTextObject_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0042a738
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440001
};
```

#### Vtable #2

- **File Offset**: 0x000299d0
- **Virtual Address**: 0x004299d0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x00439612 | Virtual[0] - Destructor |
|  1 | 0x004c0001 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNTextObject_vtable_2 {
    void* method0_Destructor; // [ 0] @ 0x00439612
    void* method1_Load_Parse_Init; // [ 1] @ 0x004c0001
};
```

---

### TVNTextParms

**Type String Offset**: 0x0000e381

#### Vtable #1

- **File Offset**: 0x0000e1e0
- **Virtual Address**: 0x0040e1e0
- **Methods**: 2

| Index | Address | Role |
|-------|---------|------|
|  0 | 0x0043ba0c | Virtual[0] - Destructor |
|  1 | 0x00440090 | Virtual[1] - Load/Parse/Init |

```cpp
struct TVNTextParms_vtable_1 {
    void* method0_Destructor; // [ 0] @ 0x0043ba0c
    void* method1_Load_Parse_Init; // [ 1] @ 0x00440090
};
```

---

