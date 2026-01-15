# Outils de Rétro-ingénierie Installés

Ce document liste tous les outils de rétro-ingénierie (reverse engineering) installés sur ce système.

## 📋 Table des matières

1. [Outils principaux](#outils-principaux)
2. [Outils d'analyse binaire](#outils-danalyse-binaire)
3. [Débogueurs](#débogueurs)
4. [Outils Python](#outils-python)
5. [Utilisation rapide](#utilisation-rapide)

---

## 🔧 Outils principaux

### Radare2 (r2)
**Version**: 5.5.0
**Description**: Framework open-source complet pour l'analyse binaire et la rétro-ingénierie
**Commandes utiles**:
```bash
r2 <binary>           # Ouvrir un binaire
r2 -A <binary>        # Analyse automatique
r2 -d <binary>        # Mode débogage
```

**Commandes internes importantes**:
- `aa` - Analyse basique
- `aaa` - Analyse approfondie
- `afl` - Lister les fonctions
- `pdf @ main` - Désassembler la fonction main
- `V` - Mode visuel
- `VV` - Mode graphique
- `s <addr>` - Seek vers une adresse
- `px 100` - Afficher 100 bytes en hex

### Ghidra
**Version**: 12.0.1
**Description**: Suite d'analyse de logiciels de la NSA avec décompilateur avancé
**Installation**: `/opt/ghidra`

**Commandes utiles**:
```bash
ghidra                        # Lancer l'interface graphique
analyzeHeadless <project_dir> <project_name> -import <binary> -analyze
analyzeHeadless <project_dir> <project_name> -process <binary> -postScript <script.py>
```

**Interface graphique**:
- **CodeBrowser**: Interface principale pour analyser les binaires
- **Decompiler**: Décompilateur C/C++ très puissant
- **Function Graph**: Vue graphique du flux d'exécution
- **Listing**: Vue désassemblée avec annotations
- **Symbol Tree**: Arbre des symboles et fonctions
- **Data Type Manager**: Gestion des types de données

**Fonctionnalités clés**:
- Décompilation en C pseudo-code de haute qualité
- Support de nombreuses architectures (x86, ARM, MIPS, PowerPC, etc.)
- Analyse automatique des fonctions et du flux de contrôle
- Scripting en Python et Java
- Comparaison de binaires (diff)
- Analyse de firmware
- Extension via plugins

**Mode headless (CLI)**:
```bash
# Analyser un binaire automatiquement
analyzeHeadless /tmp/ghidra_projects MyProject -import binary.exe -analyze

# Exécuter un script Python sur un binaire
analyzeHeadless /tmp/ghidra_projects MyProject -process binary.exe \
  -postScript analyze.py

# Exporter les fonctions décompilées
analyzeHeadless /tmp/ghidra_projects MyProject -process binary.exe \
  -postScript DecompileAllScript.java /tmp/output
```

**Scripting Python dans Ghidra**:
```python
# Script Ghidra Python (exécuté dans le contexte Ghidra)
# Obtenir le programme actuel
prog = getCurrentProgram()

# Lister toutes les fonctions
fm = prog.getFunctionManager()
for func in fm.getFunctions(True):
    print("Function: {} at {}".format(func.getName(), func.getEntryPoint()))

# Obtenir la décompilation d'une fonction
from ghidra.app.decompiler import DecompInterface
decomp = DecompInterface()
decomp.openProgram(prog)

func = getFirstFunction()  # Obtenir la première fonction
if func:
    result = decomp.decompileFunction(func, 30, monitor)
    if result.decompileCompleted():
        print(result.getDecompiledFunction().getC())
```

### GDB (GNU Debugger)
**Version**: 15.0.50
**Description**: Débogueur standard pour Linux
**Extensions**: GEF (GDB Enhanced Features) installé

**Commandes utiles**:
```bash
gdb <binary>          # Lancer GDB
gdb -p <pid>          # Attacher à un processus
gdb-multiarch         # GDB multi-architecture
```

**Commandes GDB importantes**:
- `break main` - Point d'arrêt sur main
- `run` - Lancer le programme
- `continue` - Continuer l'exécution
- `step` - Exécuter ligne par ligne
- `info registers` - Afficher les registres
- `x/20x $rsp` - Examiner la stack
- `disassemble main` - Désassembler une fonction

**Commandes GEF**:
- `vmmap` - Carte mémoire du processus
- `checksec` - Vérifier les protections
- `elf-info` - Informations sur l'ELF
- `heap` - Analyse du heap
- `pattern create 200` - Créer un pattern
- `pattern search` - Chercher un pattern
- `rop` - Recherche de gadgets ROP

---

## 🔍 Outils d'analyse binaire

### binutils
Collection d'outils pour manipuler les binaires:

**objdump** - Désassembleur
```bash
objdump -d <binary>           # Désassembler
objdump -M intel -d <binary>  # Syntaxe Intel
objdump -s <binary>           # Dump hexadécimal
objdump -t <binary>           # Table des symboles
```

**readelf** - Analyse de fichiers ELF
```bash
readelf -h <binary>           # Header ELF
readelf -l <binary>           # Program headers
readelf -S <binary>           # Sections
readelf -s <binary>           # Symboles
readelf -r <binary>           # Relocations
```

**strings** - Extraire les chaînes de caractères
```bash
strings <binary>              # Toutes les chaînes
strings -n 10 <binary>        # Chaînes de 10+ caractères
strings -e l <binary>         # Little-endian unicode
```

**nm** - Lister les symboles
```bash
nm <binary>                   # Tous les symboles
nm -D <binary>                # Symboles dynamiques
nm -C <binary>                # Démangle C++
```

### hexedit
Éditeur hexadécimal interactif
```bash
hexedit <file>                # Ouvrir un fichier
```

### xxd
Dump hexadécimal
```bash
xxd <file>                    # Dump hex
xxd -r <hexfile> <outfile>    # Reverse (hex vers binaire)
xxd -p <file>                 # Dump continu sans formatage
```

### file
Identification de type de fichier
```bash
file <binary>                 # Type de fichier
file -L <link>                # Suivre les liens symboliques
```

### binwalk
Analyse et extraction de firmware
```bash
binwalk <firmware>            # Analyser
binwalk -e <firmware>         # Extraire
binwalk -E <file>             # Analyse d'entropie
```

### foremost
Récupération de fichiers (file carving)
```bash
foremost -i <image> -o output/  # Extraire fichiers
```

### elfutils
Outils avancés pour ELF
```bash
eu-readelf -a <binary>        # Analyse complète
eu-objdump -d <binary>        # Désassembler
```

### patchelf
Modification de binaires ELF
```bash
patchelf --set-interpreter <interp> <binary>
patchelf --set-rpath <path> <binary>
patchelf --remove-needed <lib> <binary>
```

---

## 🐛 Débogueurs

### strace
Traçage des appels système
```bash
strace <program>              # Tracer les syscalls
strace -f <program>           # Suivre les forks
strace -e open <program>      # Tracer seulement open
strace -c <program>           # Statistiques
```

### ltrace
Traçage des appels de bibliothèques
```bash
ltrace <program>              # Tracer les calls
ltrace -f <program>           # Suivre les forks
ltrace -c <program>           # Statistiques
```

---

## 🐍 Outils Python

### pwntools
Framework complet pour l'exploitation et la rétro-ingénierie
```python
from pwn import *

# Connexion
p = process('./binary')
p = remote('host', port)

# Manipulation de données
payload = p32(0xdeadbeef)     # Pack en 32-bit
payload = p64(0xdeadbeef)     # Pack en 64-bit
data = u32(p.recv(4))         # Unpack 32-bit

# ELF manipulation
elf = ELF('./binary')
print(elf.symbols['main'])
print(elf.got['puts'])
print(elf.plt['system'])

# ROP
rop = ROP(elf)
rop.call('system', ['/bin/sh'])
print(rop.dump())

# Shellcode
shellcode = asm(shellcraft.sh())

# Recherche
libc = ELF('./libc.so.6')
system = libc.symbols['system']
```

### capstone
Désassembleur multi-architecture
```python
from capstone import *

md = Cs(CS_ARCH_X86, CS_MODE_64)
code = b"\x55\x48\x8b\x05\xb8\x13\x00\x00"

for i in md.disasm(code, 0x1000):
    print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
```

Architectures supportées:
- x86/x64
- ARM/ARM64
- MIPS
- PowerPC
- SPARC
- SystemZ
- M68K
- TMS320C64x
- M680X
- EVM

### keystone
Assembleur multi-architecture
```python
from keystone import *

ks = Ks(KS_ARCH_X86, KS_MODE_64)
encoding, count = ks.asm("mov rax, 0x60; ret")
print("Encoded: %s" % encoding.hex())
```

### unicorn
Framework d'émulation CPU
```python
from unicorn import *
from unicorn.x86_const import *

# Initialiser émulateur x86-64
mu = Uc(UC_ARCH_X86, UC_MODE_64)

# Mapper mémoire
ADDRESS = 0x1000000
mu.mem_map(ADDRESS, 2 * 1024 * 1024)

# Écrire code machine
code = b"\x48\xb8\x01\x00\x00\x00\x00\x00\x00\x00"  # mov rax, 1
mu.mem_write(ADDRESS, code)

# Émuler
mu.emu_start(ADDRESS, ADDRESS + len(code))

# Lire registre
rax = mu.reg_read(UC_X86_REG_RAX)
print("RAX = 0x%x" % rax)
```

### pyelftools
Parsing de fichiers ELF
```python
from elftools.elf.elffile import ELFFile

with open('binary', 'rb') as f:
    elf = ELFFile(f)

    # Lire les sections
    for section in elf.iter_sections():
        print(section.name, hex(section['sh_addr']))

    # Lire les symboles
    symtab = elf.get_section_by_name('.symtab')
    for symbol in symtab.iter_symbols():
        print(symbol.name, hex(symbol['st_value']))
```

### ROPgadget
Recherche de gadgets ROP
```bash
ROPgadget --binary <binary>
ROPgadget --binary <binary> --only "pop|ret"
ROPgadget --binary <binary> --ropchain
```

```python
# Utilisation en Python
from ropgadget.args import Args
from ropgadget.core import Core

args = Args().getArgs()
core = Core(args)
core.analyze()
```

---

## 🚀 Utilisation rapide

### Workflow typique d'analyse

1. **Identification initiale**
```bash
file binary
strings binary | less
```

2. **Analyse statique**
```bash
checksec binary              # Avec pwntools
readelf -a binary | less
objdump -M intel -d binary | less
```

3. **Analyse avec radare2**
```bash
r2 -A binary
# Dans r2:
aaa          # Analyse complète
afl          # Liste des fonctions
s main       # Aller à main
VV           # Vue graphique
```

4. **Analyse avec Ghidra (décompilation)**
```bash
ghidra                    # Lancer l'interface graphique
# 1. Create New Project
# 2. Import File -> sélectionner le binaire
# 3. Double-cliquer sur le fichier importé
# 4. Analyze -> Oui (analyse automatique)
# 5. Naviguer dans le code décompilé

# Ou en mode headless:
analyzeHeadless /tmp/ghidra_proj MyProj -import binary -analyze
```

5. **Débogage avec GDB + GEF**
```bash
gdb binary
# Dans GDB:
checksec
break main
run
vmmap
disassemble
```

6. **Analyse dynamique**
```bash
strace ./binary 2>&1 | less
ltrace ./binary 2>&1 | less
```

### Exemples pratiques

**Trouver des gadgets ROP:**
```bash
ROPgadget --binary binary --only "pop|ret" > gadgets.txt
```

**Extraire et analyser des strings:**
```bash
strings -n 8 binary | grep -i "password\|key\|flag"
```

**Patcher un binaire:**
```bash
# Changer l'interpréteur
patchelf --set-interpreter /lib64/ld-linux-x86-64.so.2 binary

# Ajouter une bibliothèque
patchelf --add-needed libcustom.so binary
```

**Script Python pour exploitation:**
```python
#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

# Configuration
binary = './vuln'
elf = ELF(binary)

# Lancer le processus
p = process(binary)
# ou remote
# p = remote('target.com', 1337)

# Exploitation
payload = b'A' * 64
payload += p64(elf.symbols['win'])

p.sendline(payload)
p.interactive()
```

---

## 📚 Ressources supplémentaires

### Documentation officielle
- Ghidra: https://ghidra-sre.org/ et https://github.com/NationalSecurityAgency/ghidra
- Radare2: https://book.rada.re/
- GDB: https://sourceware.org/gdb/documentation/
- GEF: https://hugsy.github.io/gef/
- pwntools: https://docs.pwntools.com/

### Tutoriels et références
- Binary exploitation: https://exploit.education/
- CTF challenges: https://ctftime.org/
- Reverse engineering: https://crackmes.one/

---

## 🧪 Test de l'installation

Pour vérifier que tous les outils sont correctement installés, exécutez:

```bash
bash test_reverse_tools.sh
```

Ce script vérifiera la présence et le fonctionnement de tous les outils installés.

---

**Dernière mise à jour**: 2026-01-15
**Système**: Ubuntu 24.04 LTS
