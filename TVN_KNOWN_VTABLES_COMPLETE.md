# All TVN Vtables - Known Addresses

Extraction of all methods from known vtable addresses.

**Source**: TVN_SCENE_LOADER_ANALYSIS.md + find_and_extract_vtables.py results
**Binary**: DOCS/europeo.exe
**Date**: 2026-01-16

---

## Summary

| Vtable Name | Virtual Address | Methods |
|-------------|-----------------|----------|
| TVNCommand_or_Base                       | 0x0040E1E0 |   2 |
| TVNFrame_1                               | 0x00435B50 |   2 |
| TVNFrame_2                               | 0x00435DD4 |   2 |
| TVNHotspot                               | 0x00413514 |   2 |
| TVNImageObject_1                         | 0x00429980 |   2 |
| TVNImageObject_2                         | 0x004299D0 |   2 |
| TVNSceneParms_array                      | 0x00441800 |   1 |
| TVNSceneParms_internal2                  | 0x004417D0 |   1 |
| TVNSceneParms_internal3                  | 0x004417A0 |   2 |

**Total**: 9 vtables, 16 methods

---

## Detailed Methods

### TVNCommand_or_Base

**Virtual Address**: 0x0040E1E0
**Methods**: 2

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x0043BA0C | Virtual[0] - Destructor |
| +0x04 | 0x00440090 | Virtual[1] - LoadFromINI/Parse |

```cpp
struct TVNCommand_or_Base_vtable {
    void* method0_Destructor; // +0x00 @ 0x0043BA0C
    void* method1_LoadFromINI_Parse; // +0x04 @ 0x00440090
};
```

---

### TVNFrame_1

**Virtual Address**: 0x00435B50
**Methods**: 2

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x0042D471 | Virtual[0] - Destructor |
| +0x04 | 0x00440001 | Virtual[1] - LoadFromINI/Parse |

```cpp
struct TVNFrame_1_vtable {
    void* method0_Destructor; // +0x00 @ 0x0042D471
    void* method1_LoadFromINI_Parse; // +0x04 @ 0x00440001
};
```

---

### TVNFrame_2

**Virtual Address**: 0x00435DD4
**Methods**: 2

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x0042D3BD | Virtual[0] - Destructor |
| +0x04 | 0x00480001 | Virtual[1] - LoadFromINI/Parse |

```cpp
struct TVNFrame_2_vtable {
    void* method0_Destructor; // +0x00 @ 0x0042D3BD
    void* method1_LoadFromINI_Parse; // +0x04 @ 0x00480001
};
```

---

### TVNHotspot

**Virtual Address**: 0x00413514
**Methods**: 2

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x00440460 | Virtual[0] - Destructor |
| +0x04 | 0x00440090 | Virtual[1] - LoadFromINI/Parse |

```cpp
struct TVNHotspot_vtable {
    void* method0_Destructor; // +0x00 @ 0x00440460
    void* method1_LoadFromINI_Parse; // +0x04 @ 0x00440090
};
```

---

### TVNImageObject_1

**Virtual Address**: 0x00429980
**Methods**: 2

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x0042A738 | Virtual[0] - Destructor |
| +0x04 | 0x00440001 | Virtual[1] - LoadFromINI/Parse |

```cpp
struct TVNImageObject_1_vtable {
    void* method0_Destructor; // +0x00 @ 0x0042A738
    void* method1_LoadFromINI_Parse; // +0x04 @ 0x00440001
};
```

---

### TVNImageObject_2

**Virtual Address**: 0x004299D0
**Methods**: 2

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x00439612 | Virtual[0] - Destructor |
| +0x04 | 0x004C0001 | Virtual[1] - LoadFromINI/Parse |

```cpp
struct TVNImageObject_2_vtable {
    void* method0_Destructor; // +0x00 @ 0x00439612
    void* method1_LoadFromINI_Parse; // +0x04 @ 0x004C0001
};
```

---

### TVNSceneParms_array

**Virtual Address**: 0x00441800
**Methods**: 1

| Offset | Address | Role |
|--------|---------|------|
| +0x04 | 0x004427E4 | Virtual[1] - LoadFromINI/Parse |

```cpp
struct TVNSceneParms_array_vtable {
    void* method1_LoadFromINI_Parse; // +0x04 @ 0x004427E4
};
```

---

### TVNSceneParms_internal2

**Virtual Address**: 0x004417D0
**Methods**: 1

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x004427A4 | Virtual[0] - Destructor |

```cpp
struct TVNSceneParms_internal2_vtable {
    void* method0_Destructor; // +0x00 @ 0x004427A4
};
```

---

### TVNSceneParms_internal3

**Virtual Address**: 0x004417A0
**Methods**: 2

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x00442774 | Virtual[0] - Destructor |
| +0x04 | 0x0040F500 | Virtual[1] - LoadFromINI/Parse |

```cpp
struct TVNSceneParms_internal3_vtable {
    void* method0_Destructor; // +0x00 @ 0x00442774
    void* method1_LoadFromINI_Parse; // +0x04 @ 0x0040F500
};
```

---

