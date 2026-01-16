# Complete TVN Methods Extraction

Comprehensive extraction of all vtables and methods from TVN structures.

**Binary**: DOCS/europeo.exe
**Date**: 2026-01-16

---

## Summary

| Structure | Vtable Address | Methods Count |
|-----------|----------------|---------------|
| TVNCommand                     | 0x0040EDC9 |   1 |
| TVNHtmlParms                   | 0x0040EC57 |   1 |
| TVNProjectParms                | 0x0040EC02 |   1 |

**Total**: 3 structures, 3 methods

---

## Detailed Methods

### TVNCommand

**Vtable**: 0x0040EDC9
**Methods**: 1

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x0043F0BE | Virtual[0] - Likely Destructor |

```cpp
struct TVNCommand_vtable {
    void* method0 - Likely Destructor; // +0x00 @ 0x0043F0BE
};
```

---

### TVNHtmlParms

**Vtable**: 0x0040EC57
**Methods**: 1

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x0040FD32 | Virtual[0] - Likely Destructor |

```cpp
struct TVNHtmlParms_vtable {
    void* method0 - Likely Destructor; // +0x00 @ 0x0040FD32
};
```

---

### TVNProjectParms

**Vtable**: 0x0040EC02
**Methods**: 1

| Offset | Address | Role |
|--------|---------|------|
| +0x00 | 0x0044013C | Virtual[0] - Likely Destructor |

```cpp
struct TVNProjectParms_vtable {
    void* method0 - Likely Destructor; // +0x00 @ 0x0044013C
};
```

---

