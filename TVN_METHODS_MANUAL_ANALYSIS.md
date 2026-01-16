# TVN Methods - Analyse Manuelle

## 📋 Vue d'ensemble

Pour extraire **toutes les méthodes** de **toutes les structures TVN**, nous avons besoin d'analyser europeo.exe avec IDA Pro/Free.

Cette documentation compile ce que nous avons **déjà trouvé** et propose une **méthodologie** pour extraire le reste.

---

## ✅ Ce que Nous Avons Déjà Extrait

### TVNSceneParms - COMPLET (5 extraits analysés)

#### Vtables Identifiées

| Vtable | Offset | Associée à |
|--------|--------|------------|
| `off_442DA4` | 0x00442DA4 | TVNSceneParms (principale) |
| `off_442D64` | 0x00442D64 | TVNSceneParms (alternative) |
| `off_442D80` | 0x00442D80 | Sous-objet 1 |
| `off_442D90` | 0x00442D90 | Sous-objet 2 |
| `off_4417C0` | 0x004417C0 | Structure interne 1 |
| `off_4417D0` | 0x004417D0 | Structure interne 2 |
| `off_4417A0` | 0x004417A0 | Structure interne 3 |
| `off_441800` | 0x00441800 | Array interne |

#### Méthodes Identifiées

##### Méthode Virtuelle [0] - Load from INI
**Fonction**: `sub_414B2A` @ 0x00414B2A

**Rôle**: Charger les paramètres d'une AREA depuis le fichier .INI

**Pseudo-code**:
```cpp
void TVNSceneParms::LoadFromINI(int area_number, char* ini_filename)
{
    TProfile ini;
    char section_name[256];
    char buffer[256];

    sprintf(section_name, "AREA_%u", area_number);
    ini.TProfile(section_name, ini_filename);

    // Lire NAME
    ini.GetString("NAME", buffer, 0x100, "");
    this->name = buffer;  // +0x08

    // Lire BKCOLOR (format "R,G,B")
    ini.GetString("BKCOLOR", buffer, 0x100, "0,0,0");
    unsigned char r, g, b;
    sscanf(buffer, "%u,%u,%u", &r, &g, &b);
    this->background_color = (b << 16) | (g << 8) | r;  // +0x10

    // Lire autres paramètres
    this->caps = ini.GetInt("CAPS", 0);                    // +0x14
    this->default_cursor = ini.GetInt("DEFCURSOR", 0);    // +0x0C
    this->background_texture = ini.GetInt("BKTEXTURE", 0); // +0x04
}
```

**Paramètres lus**:
- NAME → +0x08 (string)
- BKCOLOR → +0x10 (RGB packed)
- CAPS → +0x14 (int)
- DEFCURSOR → +0x0C (int)
- BKTEXTURE → +0x04 (int)

##### Constructeur - sub_415093
**Fonction**: `sub_415093` @ 0x00415093

**Rôle**: Construire l'objet TVNSceneParms (153 bytes)

**Pseudo-code**:
```cpp
TVNSceneParms::TVNSceneParms()
{
    // Initialiser vtable principale
    this->vtable = &off_442DA4;

    // Initialiser strings (7 strings)
    new (&this->name) string();           // +0x08
    new (&this->field_20) string();       // +0x20
    new (&this->field_24) string();       // +0x24
    new (&this->field_28) string();       // +0x28
    new (&this->field_2C) string();       // +0x2C
    new (&this->field_30) string();       // +0x30
    new (&this->field_34) string();       // +0x34

    // Initialiser vtables des sous-objets
    this->sub_obj1_vtable = &off_442D80;  // +0x18
    this->sub_obj2_vtable = &off_442D90;  // +0x1C

    // Initialiser structure complexe à +0x68
    this->complex.count = 1;
    this->complex.vtable = &off_43B500;

    // Allouer array interne
    void* array = operator new[](4);
    this->complex.array = _vector_new_ldtc_(array, 1, 1, 4, &sub_417940, 1, 0);

    // Finaliser vtables
    this->complex.vtable = &off_441800;
    this->complex.sub_vtable1 = &off_4417C0;
    this->complex.sub_vtable2 = &off_4417D0;
    this->complex.sub_vtable3 = &off_4417A0;

    // Configuration supplémentaire
    sub_415560(this);

    // Appeler méthode virtuelle Load
    this->vtable->Load(this, area_number, ini_filename);
}
```

##### Autres Fonctions Auxiliaires

| Fonction | Offset | Rôle |
|----------|--------|------|
| `sub_416FCD` | ? | Initialisation préalable de scene_obj |
| `sub_404711` | ? | Extraction du nom de fichier |
| `sub_406954` | ? | Redimensionnement de liste dynamique |
| `sub_426399` | ? | Ajout d'élément à liste |
| `sub_414A70` | ? | Initialisation supplémentaire AREA |
| `sub_415560` | ? | Configuration AREA |
| `sub_417940` | ? | Callback pour _vector_new_ldtc_ |

---

## 📊 Méthodologie d'Extraction Complète

### Approche Recommandée: IDA Pro/Free

Pour extraire **toutes les méthodes** de **toutes les 35 structures TVN**, voici la procédure:

#### Étape 1: Ouvrir avec IDA

```bash
# GUI (nécessite X11)
ida64 DOCS/europeo.exe

# Mode texte (headless)
idat64 DOCS/europeo.exe
```

#### Étape 2: Localiser les Vtables

Dans IDA, chercher les symboles:

**Pour les *Parms structures**:
```
Goto → 0x0040EC02  (TVNProjectParms vtable)
Goto → 0x0040EC20  (TVNMidiParms vtable)
Goto → 0x0040EC3B  (TVNDigitParms vtable)
Goto → 0x0040EC57  (TVNHtmlParms vtable)
Goto → 0x0040EC72  (TVNImageParms vtable)
Goto → 0x0040EC8E  (TVNImgObjParms vtable)
Goto → 0x0040ECAB  (TVNImgSeqParms vtable)
Goto → 0x0040ECC8  (TVNExecParms vtable)
Goto → 0x0040ECE3  (TVNSetVarParms vtable)
Goto → 0x0040ED00  (TVNIfParms vtable)
Goto → 0x0040ED75  (TVNTextParms vtable)
Goto → 0x0040ED90  (TVNTextObjParms vtable)
Goto → 0x0040EDAE  (TVNFontParms vtable)
Goto → 0x0040EDC9  (TVNCommand vtable)
Goto → 0x0040EDE2  (TVNSceneParms vtable)
Goto → 0x0040EDFE  (TVNStringParms vtable)
```

**Note**: Ces offsets proviennent de vos extraits initiaux.

#### Étape 3: Extraire les Méthodes de Chaque Vtable

Pour chaque vtable trouvée:

1. **Identifier le nombre de méthodes**
   - Les vtables sont des tableaux de pointeurs de fonction
   - Format: `dd offset method1, offset method2, offset method3, ...`

2. **Pour chaque méthode**:
   - Noter l'offset de la fonction
   - Désassembler la fonction (touche F5 dans IDA pour décompiler)
   - Identifier le rôle de la méthode

3. **Documenter**:
   ```
   TVNImageParms @ 0x0040EC72:
     [00] Load      @ 0x00412ABC  - Charger image/vidéo
     [04] Execute   @ 0x00413456  - Exécuter (playavi/playbmp)
     [08] Stop      @ 0x00414789  - Arrêter lecture
     [0C] Release   @ 0x004158BC  - Libérer ressources
     ...
   ```

#### Étape 4: Scripter l'Extraction (IDC ou Python)

Script IDA Python pour automatiser:

```python
import ida_bytes
import ida_name

# Liste des vtables connues
vtables = {
    0x0040EC02: "TVNProjectParms",
    0x0040EC20: "TVNMidiParms",
    0x0040EC3B: "TVNDigitParms",
    # ... toutes les vtables
}

for vtable_addr, struct_name in vtables.items():
    print(f"\n=== {struct_name} @ 0x{vtable_addr:08X} ===")

    # Lire les pointeurs de méthodes
    offset = 0
    while True:
        method_ptr = ida_bytes.get_dword(vtable_addr + offset)

        # Vérifier si c'est un pointeur de code valide
        if method_ptr < 0x00400000 or method_ptr > 0x00500000:
            break

        # Obtenir le nom de la fonction (si disponible)
        func_name = ida_name.get_name(method_ptr)
        if not func_name:
            func_name = f"sub_{method_ptr:X}"

        print(f"  [{offset:02X}] 0x{method_ptr:08X}  {func_name}")

        offset += 4

        if offset > 0x100:  # Sécurité
            break
```

---

## 🔍 Structures TVN Prioritaires

Voici les structures à analyser **en priorité** pour comprendre le moteur:

### 1. TVNCommand (Classe de Base)

**Priorité**: ⭐⭐⭐⭐⭐ CRITIQUE

**Raison**: Toutes les commandes héritent de TVNCommand

**Vtable**: `0x0040EDC9` (selon vos extraits)

**Méthodes attendues**:
- `Execute()` - Exécuter la commande
- `Parse()` - Parser les paramètres
- `Validate()` - Valider
- `Clone()` - Dupliquer
- `Release()` - Libérer

### 2. TVNImageParms (Multimédia)

**Priorité**: ⭐⭐⭐⭐ HAUTE

**Commandes**: playavi, playbmp, closeavi

**Vtable**: `0x0040EC72`

**Méthodes attendues**:
- `Load(filename)` - Charger fichier
- `Play(x, y, w, h)` - Jouer
- `Stop()` - Arrêter
- `SetLoop(loop)` - Définir boucle

### 3. TVNSetVarParms (Variables)

**Priorité**: ⭐⭐⭐⭐ HAUTE

**Commandes**: set_var

**Vtable**: `0x0040ECE3`

**Méthodes attendues**:
- `SetVariable(name, value)` - Définir variable
- `GetVariable(name)` - Obtenir valeur

### 4. TVNIfParms (Conditions)

**Priorité**: ⭐⭐⭐⭐ HAUTE

**Commandes**: if-then-else

**Vtable**: `0x0040ED00`

**Méthodes attendues**:
- `Evaluate()` - Évaluer condition
- `ExecuteThen()` - Branche then
- `ExecuteElse()` - Branche else

### 5. TVNTextParms (Texte)

**Priorité**: ⭐⭐⭐ MOYENNE

**Commandes**: playtext

**Vtable**: `0x0040ED75`

### 6. TVNExecParms (Système)

**Priorité**: ⭐⭐⭐ MOYENNE

**Commandes**: exec, rundll

**Vtable**: `0x0040ECC8`

---

## 🛠️ Outils Disponibles

### 1. IDA Free 8.4 (Installé)

**Avantages**:
- Décompilateur intégré (F5)
- Navigation graphique des vtables
- Scripts Python/IDC

**Utilisation**:
```bash
# Lancer IDA sur europeo.exe
ida64 DOCS/europeo.exe
```

### 2. Radare2 5.5.0 (Installé)

**Avantages**:
- Scriptable
- Analyse automatique

**Utilisation**:
```bash
# Analyser les vtables
r2 -A DOCS/europeo.exe
# Dans r2:
aaa  # Analyser tout
afl  # Lister fonctions
s 0x0040EC72  # Goto vtable
pd 20  # Disassemble
```

### 3. Ghidra 12.0.1 (Installé)

**Avantages**:
- Décompilateur gratuit
- Analyse de structures

**Utilisation**:
```bash
ghidra
# Puis: File → Import → europeo.exe → Analyze
```

---

## 📝 Template de Documentation

Pour chaque structure TVN, documenter selon ce template:

```markdown
### TVN[NomStructure]

**Type**: Parms / Class
**Vtable**: 0x[offset]
**Taille**: [bytes]
**Commandes associées**: [liste]

#### Vtable

| Offset | Adresse | Méthode | Rôle |
|--------|---------|---------|------|
| +0x00 | 0x[addr] | [nom] | [description] |
| +0x04 | 0x[addr] | [nom] | [description] |
| ... | ... | ... | ... |

#### Structure Mémoire

```cpp
struct TVN[NomStructure] {
    void* vtable;           // +0x00
    [type] [champ];         // +0x[offset]
    ...
};
```

#### Méthodes Détaillées

##### Méthode[0] - [Nom]

**Fonction**: `sub_[addr]` @ 0x[addr]

**Pseudo-code**:
```cpp
[code]
```

**Paramètres**:
- [param1]: [description]
- [param2]: [description]

**Retour**: [type et description]

---

## 🎯 Plan d'Action

### Phase 1: Structures Critiques (PRIORITÉ)

1. ✅ **TVNSceneParms** - FAIT (5 extraits analysés)
2. ⬜ **TVNCommand** - Base de toutes les commandes
3. ⬜ **TVNImageParms** - Multimédia vidéo/image
4. ⬜ **TVNSetVarParms** - Variables
5. ⬜ **TVNIfParms** - Conditions

**Temps estimé**: 2-3 heures avec IDA

### Phase 2: Structures Média

6. ⬜ **TVNDigitParms** - Audio WAV
7. ⬜ **TVNMidiParms** - Audio MIDI
8. ⬜ **TVNTextParms** - Texte

**Temps estimé**: 1-2 heures

### Phase 3: Structures Avancées

9. ⬜ **TVNExecParms** - Exécution système
10. ⬜ **TVNFontParms** - Polices
11. ⬜ **Autres structures** (25 restantes)

**Temps estimé**: 3-4 heures

---

## 💡 Approche Alternative: Analyse Dynamique

Si l'analyse statique est trop complexe, on peut:

1. **Exécuter europeo.exe**
2. **Attacher un débogueur** (x32dbg, OllyDbg)
3. **Mettre des breakpoints** sur les vtables connues
4. **Observer** les appels de méthodes en temps réel
5. **Logger** les paramètres et comportements

---

## 📊 Statistiques Actuelles

| Catégorie | Total | Analysé | Reste |
|-----------|-------|---------|-------|
| **Structures TVN** | 35 | 1 (TVNSceneParms) | 34 |
| **Vtables identifiées** | ~35+ | 8 (TVNSceneParms) | ~27+ |
| **Méthodes extraites** | ~200+ | 4 (TVNSceneParms) | ~196+ |
| **Commandes documentées** | 46 | 46 (noms) | 0 (implémentation) |

---

## 🚀 Prochaine Étape Recommandée

**Option A**: Utilisez IDA directement
```bash
ida64 DOCS/europeo.exe
# Naviguez vers 0x0040EC72 (TVNImageParms)
# Extrayez les méthodes
```

**Option B**: Fournissez plus d'extraits IDA
```
Comme vous l'avez fait pour TVNSceneParms, extrayez:
- TVNCommand @ 0x0040EDC9
- TVNImageParms @ 0x0040EC72
- TVNSetVarParms @ 0x0040ECE3
- TVNIfParms @ 0x0040ED00
```

**Option C**: J'utilise Ghidra en mode headless
```bash
# Script automatisé d'extraction
analyzeHeadless /tmp VND -import DOCS/europeo.exe -postScript extract_vtables.py
```

**Quelle option préférez-vous ?**

---

**Date**: 2026-01-16
**Status**: 1/35 structures complètement analysées
**Prochaine cible**: TVNCommand (classe de base)
