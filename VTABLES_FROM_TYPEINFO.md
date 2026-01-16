# TVN Vtables - Found Using TYPEINFO Addresses

Search strategy: Look for vtables ±2000 bytes from TYPEINFO addresses.

**Tool**: find_vtables_from_typeinfo.py
**Binary**: europeo.exe

---

## Summary

| Structure | TYPEINFO | Vtables Found |
|-----------|----------|---------------|
| TVNFileNameParms     | 0x0040F3CE |  0 |
| TVNEventCommand      | 0x0040F51E |  0 |
| TVNVariable          | 0x004067B8 |  0 |
| TVNScene             | 0x004179AE |  1 |
| TVNToolBar           | 0x00435901 |  0 |
| TVNWindow            | 0x00435921 |  0 |
| TVNApplication       | 0x00438A7A |  0 |
| TVNAviMedia          | 0x00435953 |  0 |
| TVNWaveMedia         | 0x0041C51D |  0 |
| TVNMidiMedia         | 0x0041C590 |  0 |
| TVNCDAMedia          | 0x00435939 |  0 |
| TVNBitmap            | 0x0041E5FC |  0 |
| TVNGdiObject         | 0x0041E673 |  0 |
| TVNHtmlText          | 0x004231F0 |  0 |
| TVNBmpImg            | 0x004358CF |  0 |
| TVNImageObject       | 0x0042A40B |  1 |
| TVNTextObject        | 0x0042A448 |  2 |

---

## Detailed Results

### TVNFileNameParms

**TYPEINFO Address**: 0x0040F3CE

**Vtables Found**: ❌ None

---

### TVNEventCommand

**TYPEINFO Address**: 0x0040F51E

**Vtables Found**: ❌ None

---

### TVNVariable

**TYPEINFO Address**: 0x004067B8

**Vtables Found**: ❌ None

---

### TVNScene

**TYPEINFO Address**: 0x004179AE

**Vtables Found**: 1

#### Vtable @ 0x00417B52

- **Virtual Address**: 0x00417B52
- **File Offset**: 0x17152
- **Methods**: 2
- **Distance from TYPEINFO**: 420 bytes after

**Method Pointers**:

- [0] 0x00417FA2
- [1] 0x004C0001

---

### TVNToolBar

**TYPEINFO Address**: 0x00435901

**Vtables Found**: ❌ None

---

### TVNWindow

**TYPEINFO Address**: 0x00435921

**Vtables Found**: ❌ None

---

### TVNApplication

**TYPEINFO Address**: 0x00438A7A

**Vtables Found**: ❌ None

---

### TVNAviMedia

**TYPEINFO Address**: 0x00435953

**Vtables Found**: ❌ None

---

### TVNWaveMedia

**TYPEINFO Address**: 0x0041C51D

**Vtables Found**: ❌ None

---

### TVNMidiMedia

**TYPEINFO Address**: 0x0041C590

**Vtables Found**: ❌ None

---

### TVNCDAMedia

**TYPEINFO Address**: 0x00435939

**Vtables Found**: ❌ None

---

### TVNBitmap

**TYPEINFO Address**: 0x0041E5FC

**Vtables Found**: ❌ None

---

### TVNGdiObject

**TYPEINFO Address**: 0x0041E673

**Vtables Found**: ❌ None

---

### TVNHtmlText

**TYPEINFO Address**: 0x004231F0

**Vtables Found**: ❌ None

---

### TVNBmpImg

**TYPEINFO Address**: 0x004358CF

**Vtables Found**: ❌ None

---

### TVNImageObject

**TYPEINFO Address**: 0x0042A40B

**Vtables Found**: 1

#### Vtable @ 0x0042A517

- **Virtual Address**: 0x0042A517
- **File Offset**: 0x29B17
- **Methods**: 2
- **Distance from TYPEINFO**: 268 bytes after

**Method Pointers**:

- [0] 0x0042AA5F
- [1] 0x004C0001

---

### TVNTextObject

**TYPEINFO Address**: 0x0042A448

**Vtables Found**: 2

#### Vtable @ 0x0042A380

- **Virtual Address**: 0x0042A380
- **File Offset**: 0x29980
- **Methods**: 2
- **Distance from TYPEINFO**: 200 bytes before

**Method Pointers**:

- [0] 0x0042A738
- [1] 0x00440001

#### Vtable @ 0x0042A3D0

- **Virtual Address**: 0x0042A3D0
- **File Offset**: 0x299D0
- **Methods**: 2
- **Distance from TYPEINFO**: 120 bytes before

**Method Pointers**:

- [0] 0x00439612
- [1] 0x004C0001

---

## Code for Main Script

Add these vtables to `extract_all_35_tvn_complete.py`:

```python
    "TVNFileNameParms": None,  # TODO - Not found
    "TVNEventCommand": None,  # TODO - Not found
    "TVNVariable": None,  # TODO - Not found
    "TVNScene": 0x00417B52,
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
    "TVNBmpImg": None,  # TODO - Not found
    "TVNImageObject": 0x0042A517,
    "TVNTextObject": 0x0042A3D0,
```

