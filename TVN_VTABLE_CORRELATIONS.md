# Vtable Correlation Results

Vtables correlated to missing TVN structures via reference proximity.

---

## Summary

| Structure | Vtable Address | Methods | Distance |
|-----------|----------------|---------|----------|
| TVNTimer             | 0x004394D4 |  2 |   371 bytes |

**Total**: 1 structures matched

---

## Detailed Correlations

### TVNTimer

- **Vtable**: 0x004394D4
- **Reference**: 0x00019d52 (distance: 371 bytes)
- **Methods**: 2

| Index | Address |
|-------|----------|
|  0 | 0x0043A49C |
|  1 | 0x00405181 |

```cpp
struct TVNTimer_vtable {
    void* method_0; // @ 0x0043A49C
    void* method_1; // @ 0x00405181
};
```

---

