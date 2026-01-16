# Missing TVN Vtables - Search Results

Automated search for vtables of missing TVN structures.

**Tool**: Standalone Python vtable finder
**Binary**: europeo.exe

---

## Summary

| Structure | Vtables Found | Type String |
|-----------|---------------|-------------|
| TVNFileNameParms     |  0 | ✓ |
| TVNEventCommand      |  0 | ✓ |
| TVNVariable          |  0 | ✓ |
| TVNScene             |  0 | ✓ |
| TVNToolBar           |  0 | ✓ |
| TVNWindow            |  0 | ✓ |
| TVNApplication       |  0 | ✓ |
| TVNAviMedia          |  0 | ✓ |
| TVNWaveMedia         |  0 | ✓ |
| TVNMidiMedia         |  0 | ✓ |
| TVNCDAMedia          |  0 | ✓ |
| TVNBitmap            |  0 | ✓ |
| TVNGdiObject         |  0 | ✓ |
| TVNHtmlText          |  0 | ✓ |
| TVNImageObject       |  1 | ✓ |
| TVNTextObject        |  2 | ✓ |
| TVNBmpImg            |  0 | ✓ |

---

## Detailed Results

### TVNFileNameParms

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNEventCommand

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNVariable

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNScene

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNToolBar

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNWindow

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNApplication

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNAviMedia

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNWaveMedia

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNMidiMedia

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNCDAMedia

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNBitmap

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNGdiObject

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNHtmlText

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

### TVNImageObject

**Type String**: ✓ Found

**Vtables Found**: 1

#### Vtable @ 0x0042A517

- **Virtual Address**: 0x0042A517
- **File Offset**: 0x29B17
- **Methods**: 2
- **Distance from string**: 256 bytes after

**Method Pointers**:

- [0] 0x0042AA5F
- [1] 0x004C0001

---

### TVNTextObject

**Type String**: ✓ Found

**Vtables Found**: 2

#### Vtable @ 0x0042A380

- **Virtual Address**: 0x0042A380
- **File Offset**: 0x29980
- **Methods**: 2
- **Distance from string**: 212 bytes before

**Method Pointers**:

- [0] 0x0042A738
- [1] 0x00440001

#### Vtable @ 0x0042A3D0

- **Virtual Address**: 0x0042A3D0
- **File Offset**: 0x299D0
- **Methods**: 2
- **Distance from string**: 132 bytes before

**Method Pointers**:

- [0] 0x00439612
- [1] 0x004C0001

---

### TVNBmpImg

**Type String**: ✓ Found

**Vtables Found**: ❌ None

---

## Code for Main Script

Add these vtables to `extract_all_35_tvn_complete.py`:

```python
    "TVNFileNameParms": None,  # TODO - Not found
    "TVNEventCommand": None,  # TODO - Not found
    "TVNVariable": None,  # TODO - Not found
    "TVNScene": None,  # TODO - Not found
    "TVNToolBar": None,  # TODO - Not found
    "TVNWindow": None,  # TODO - Not found
    "TVNApplication": None,  # TODO - Not found
    "TVNAviMedia": None,  # TODO - Not found
    "TVNWaveMedia": None,  # TODO - Not found
    "TVNMidiMedia": None,  # TODO - Not found
    "TVNCDAMedia": None,  # TODO - Not found
    "TVNBitmap": None,  # TODO - Not found
    "TVNGdiObject": None,  # TODO - Not found
    "TVNHtmlText": None,  # TODO - Not found
    "TVNImageObject": 0x0042A517,
    "TVNTextObject": 0x0042A3D0,
    "TVNBmpImg": None,  # TODO - Not found
```

