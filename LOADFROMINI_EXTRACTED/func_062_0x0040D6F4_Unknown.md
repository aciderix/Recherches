# LoadFromINI Function Analysis

**Function Address**: 0x0040D6F4
**Rank**: #62
**INI String Count**: 5
**Identified Structure**: Unknown
**Confidence Score**: 0

---

## Assembly Code

**Instructions**: 55

```assembly
0040D6F4  push     ebp
0040D6F5  mov      ebp, esp
0040D6F7  add      esp, -0x28
0040D6FA  push     ebx
0040D6FB  push     esi
0040D6FC  push     edi
0040D6FD  mov      ebx, dword ptr [ebp + 8]
0040D700  mov      eax, 0x43e932
0040D705  call     0x403618
0040D70A  lea      edx, [ebx + 0xc]
0040D70D  push     edx
0040D70E  lea      edi, [ebx + 8]
0040D711  mov      esi, dword ptr [ebp + 0xc]
0040D714  push     esi
0040D715  call     0x439186
0040D71A  pop      ecx
0040D71B  mov      dword ptr [edi], eax
0040D71D  push     esi
0040D71E  call     0x439138
0040D723  add      esp, 8
0040D726  lea      eax, [ebx + 0xc]
0040D729  push     eax
0040D72A  call     0x404c08
0040D72F  pop      ecx
0040D730  cmp      dword ptr [ebx + 8], 6
0040D734  jge      0x40d775
0040D736  mov      word ptr [ebp - 0x18], 8
0040D73C  push     0x43fbc7
0040D741  lea      edx, [ebp - 4]
0040D744  push     edx
0040D745  call     0x438e6e
0040D74A  add      esp, 8
0040D74D  inc      dword ptr [ebp - 0xc]
0040D750  push     -1
0040D752  push     0
0040D754  lea      ecx, [ebp - 4]
0040D757  push     ecx
0040D758  add      ebx, 0xc
0040D75B  push     ebx
0040D75C  call     0x438f04
0040D761  add      esp, 0x10
0040D764  dec      dword ptr [ebp - 0xc]
0040D767  push     2
0040D769  lea      eax, [ebp - 4]
0040D76C  push     eax
0040D76D  call     0x438f64
0040D772  add      esp, 8
0040D775  mov      edx, dword ptr [ebp - 0x28]
0040D778  mov      dword ptr fs:[0], edx
0040D77F  pop      edi
0040D780  pop      esi
0040D781  pop      ebx
0040D782  mov      esp, ebp
0040D784  pop      ebp
0040D785  ret      
```

## Strings Referenced

**Total unique strings**: 0


## Functions Called

- 0x00403618
- 0x00439186
- 0x00439138
- 0x00404C08
- 0x00438E6E
- 0x00438F04
- 0x00438F64

---

*Extracted with recursive CALL following and DATA context*
