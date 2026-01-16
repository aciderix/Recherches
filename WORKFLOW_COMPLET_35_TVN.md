# 🎯 Workflow Complet: Extraction des 35 Structures TVN

## 📋 Vue d'Ensemble

Ce guide explique comment extraire **automatiquement** le code assembleur et les sections DATA pour **toutes les 35 structures TVN** d'europeo.exe.

---

## ✅ Ce Qui a Été Créé

### 1. Script Principal: `extract_all_35_tvn_complete.py`

**Objectif**: Extraire le code assembleur + DATA sections pour les 35 structures TVN

**Caractéristiques**:
- ✅ Extraction complète de l'assembleur (comme tu l'as fait manuellement)
- ✅ Sections DATA au format IDA (`DATA:0044295A db 41h ; A`)
- ✅ Toutes les chaînes ("AREA_%u", "NAME", "BKCOLOR", "0,0,0", etc.)
- ✅ Appels de fonctions identifiés (⭐ pour les importants)
- ✅ Un fichier markdown par structure

**État actuel**:
- ✅ 22 structures avec vtables connues → Extraction complète possible
- ⚠️ 13 structures avec vtables inconnues → Marquées TODO

### 2. Script de Recherche: `find_missing_vtables.py`

**Objectif**: Trouver automatiquement les vtables des 13 structures TODO

**Stratégies de recherche**:
1. **Proximité de type string**: Cherche "TVNStructName *" puis scanne ±500 bytes
2. **Analyse de constructeur**: Trouve les fonctions contenant `mov [reg], offset vtable`
3. **Analyse des xrefs**: Suit toutes les références aux type strings
4. **Validation**: Vérifie que c'est bien une vtable (2+ pointeurs de code valides)

**Output**: `MISSING_VTABLES_FOUND.md` avec:
- Table résumé des vtables trouvées
- Analyse détaillée par structure
- Code prêt à copier-coller dans le script principal

### 3. Documentation

- **EXTRACTION_COMPLETE_35_TVN.md**: Guide complet d'utilisation
- **UTILISER_IDA_MAINTENANT.md**: Pourquoi IDA est nécessaire (PE file mapping)
- **WORKFLOW_COMPLET_35_TVN.md**: Ce fichier - workflow complet

---

## 🚀 Workflow Étape par Étape

### Étape 1: Trouver les Vtables Manquantes ⏱️ 5-10 minutes

```
1. Ouvre IDA Pro/Free
2. File → Open → DOCS/europeo.exe
3. Attends l'analyse complète (barre de progression)
4. File → Script file... (Alt+F7)
5. Sélectionne: find_missing_vtables.py
6. Attends l'exécution (5-10 min)
```

**Sortie console attendue**:
```
====================================================================================================
FINDING MISSING TVN VTABLES
====================================================================================================

Structures to search: 17

====================================================================================================
SEARCHING: TVNFileNameParms
====================================================================================================
  Step 1: Finding type string...
  Found type string 'TVNFileNameParms *' @ 0x00450120
  Step 2: Searching for vtables near type string...
  ✓ Found 2 vtable candidate(s) near string
    #1: 0x0044FFC0 - 3 methods - 100 bytes before
    #2: 0x00450000 - 2 methods - 50 bytes before
  Step 3: Finding constructor functions...
  ✓ Found 1 constructor candidate(s)
    - sub_414200 @ 0x00414200
      → Found 1 vtable(s) in constructor

  ✅ FOUND 2 unique vtable(s):
     0x0044FFC0 - 3 methods
     0x00450000 - 2 methods

[... répété pour chaque structure ...]

====================================================================================================
SEARCH COMPLETE
====================================================================================================

Structures searched: 17
Structures with vtables found: 15
Total vtables found: 18

✓ Results saved to MISSING_VTABLES_FOUND.md
```

**Résultat**: Fichier `MISSING_VTABLES_FOUND.md` créé dans le répertoire IDA

### Étape 2: Mettre à Jour le Script Principal ⏱️ 2 minutes

```
1. Ouvre MISSING_VTABLES_FOUND.md
2. Va à la section "Code for Main Script" en bas
3. Copie le code Python généré
4. Ouvre extract_all_35_tvn_complete.py
5. Remplace les lignes "None" par les adresses trouvées
```

**Exemple de code à copier** (généré automatiquement):
```python
    "TVNFileNameParms": 0x0044FFC0,
    "TVNEventCommand": 0x00450200,
    "TVNVariable": 0x00450300,
    "TVNScene": 0x00450400,
    # ... etc.
```

**Avant**:
```python
TVN_STRUCTURES = {
    # ... structures with vtables ...

    # Missing structures - need to find their vtables
    "TVNFileNameParms": None,
    "TVNEventCommand": None,
    # ...
}
```

**Après**:
```python
TVN_STRUCTURES = {
    # ... structures with vtables ...

    # Previously missing - now found!
    "TVNFileNameParms": 0x0044FFC0,
    "TVNEventCommand": 0x00450200,
    # ...
}
```

### Étape 3: Extraire Toutes les 35 Structures ⏱️ 10-15 minutes

```
1. Dans IDA (europeo.exe toujours ouvert)
2. File → Script file... (Alt+F7)
3. Sélectionne: extract_all_35_tvn_complete.py
4. Attends l'exécution (10-15 min)
```

**Sortie console attendue**:
```
====================================================================================================
EXTRACTING ALL 35 TVN STRUCTURES WITH COMPLETE DATA SECTIONS
====================================================================================================

Output directory: TVN_COMPLETE_35_STRUCTURES
Total structures: 35

====================================================================================================
EXTRACTING: TVNProjectParms
Vtable @ 0x0040E1E0
====================================================================================================
  Found 2 method(s)
  [0] Extracting destructor @ 0x0043BA0C...
  [1] Extracting LoadFromINI @ 0x00440090...
  ✓ Saved to TVNProjectParms_COMPLETE.md

====================================================================================================
EXTRACTING: TVNMidiParms
Vtable @ 0x0040E1E0
====================================================================================================
  Found 2 method(s)
  [0] Extracting destructor @ 0x0043BA0C...
  [1] Extracting LoadFromINI @ 0x00414D80...
  ✓ Saved to TVNMidiParms_COMPLETE.md

[... répété 35 fois ...]

====================================================================================================
EXTRACTION COMPLETE!
====================================================================================================

Total structures: 35
With vtable: 35
Without vtable (TODO): 0

Output directory: TVN_COMPLETE_35_STRUCTURES

✓ Done! Files include complete DATA sections like IDA format.
✓ Check files for strings like 'AREA_%u', 'NAME', 'BKCOLOR', etc.
```

**Résultat**: 35 fichiers markdown dans `TVN_COMPLETE_35_STRUCTURES/`

### Étape 4: Vérification des Résultats ⏱️ 2 minutes

Dans le terminal (hors IDA):

```bash
cd TVN_COMPLETE_35_STRUCTURES/

# Combien de fichiers?
ls *.md | wc -l
# Devrait afficher: 35

# Vérifier qu'il n'y a plus de TODO
grep -l "TODO" *.md | wc -l
# Devrait afficher: 0

# Vérifier le contenu d'un fichier
cat TVNSceneParms_COMPLETE.md | head -100
```

**Ce que tu dois voir** dans chaque fichier:

```markdown
# TVNSceneParms - Complete Extraction

**Structure**: TVNSceneParms
**Vtable Address**: 0x0040E1E0
**Binary**: europeo.exe
**Tool**: IDA Pro

---

## Methods Summary

| Index | Address | Name |
|-------|---------|------|
|  0 | 0x0043BA0C | `destructor` |
|  1 | 0x00414B2A | `LoadFromINI` |

---

## Method [0]: destructor

**Address**: 0x0043BA0C
**Index in vtable**: 0
**Name**: `destructor`

### Assembly Code

```assembly
0043BA0C  push    ebp
0043BA0D  mov     ebp, esp
0043BA0F  sub     esp, 8
...
```

### DATA Section References

Complete DATA section like IDA (strings, constants, etc.):

```
DATA:0044295A ; "AREA_%u"
DATA:0044295A ; Referenced from 0x00414B50
DATA:0044295A                 db    0
DATA:0044295B                 db  41h ; A
DATA:0044295C                 db  52h ; R
DATA:0044295D                 db  45h ; E
DATA:0044295E                 db  41h ; A
DATA:0044295F                 db  5Fh ; _
DATA:00442960                 db  25h ; %
DATA:00442961                 db  75h ; u
DATA:00442962                 db    0

DATA:00442963 ; "NAME"
DATA:00442963 ; Referenced from 0x00414B60
DATA:00442963                 db  4Eh ; N
DATA:00442964                 db  41h ; A
DATA:00442965                 db  4Dh ; M
DATA:00442966                 db  45h ; E
DATA:00442967                 db    0
...
```

**Strings Found**:

- `"AREA_%u"` @ 0x0044295A
- `"NAME"` @ 0x00442963
- `"BKCOLOR"` @ 0x00442969
- `"0,0,0"` @ 0x00442971
...

### Function Calls

**Important Calls** (TProfile, GetString, etc.):

- ⭐ 0x00414B60 → `TProfile::GetString` @ 0x00401234
- ⭐ 0x00414B80 → `TProfile::GetInt` @ 0x00401250

**Other Calls**:

- 0x00414B90 → `sprintf`
- 0x00414BA0 → `strcpy`
...
```

---

## 📊 Les 35 Structures TVN

### Avec Vtable Partagée 0x0040E1E0 (16 structures)

1. TVNProjectParms
2. TVNMidiParms
3. TVNDigitParms
4. TVNHtmlParms
5. TVNImageParms
6. TVNImgObjParms
7. TVNImgSeqParms
8. TVNExecParms
9. TVNSetVarParms
10. TVNIfParms
11. TVNTextParms
12. TVNTextObjParms
13. TVNFontParms
14. TVNCommand
15. TVNSceneParms
16. TVNStringParms

### Avec Vtables Uniques (6 structures)

17. TVNFrame_1 → `0x00435B50`
18. TVNFrame_2 → `0x00435DD4`
19. TVNHotspot → `0x00413514`
20. TVNImageObject_1 → `0x00429980`
21. TVNImageObject_2 → `0x004299D0`
22. TVNTimer → `0x004394D4`

### Vtables à Trouver (13+ structures) ⚠️

23. TVNFileNameParms
24. TVNEventCommand
25. TVNVariable
26. TVNScene
27. TVNToolBar
28. TVNWindow
29. TVNApplication
30. TVNAviMedia
31. TVNWaveMedia
32. TVNMidiMedia
33. TVNCDAMedia
34. TVNBitmap
35. TVNGdiObject

**Plus**:
- TVNHtmlText
- TVNImageObject
- TVNTextObject
- TVNBmpImg

**Total**: 17 structures à chercher

---

## 🎯 Cas d'Usage des Résultats

### 1. Reconstruction du Format INI

Les chaînes extraites révèlent **exactement** quelles clés INI sont lues:

**TVNSceneParms** utilise:
- `"AREA_%u"` → Nom de section
- `"NAME"` → Nom de la scène
- `"BKCOLOR"` → Couleur de fond (format: `"0,0,0"`)
- `"%u,%u,%u"` → Format RGB
- `"BKTEXTURE"` → Texture de fond
- `"DEFCURSOR"` → Curseur par défaut
- `"CAPS"` → Capacités

**Fichier INI reconstruit**:
```ini
[AREA_1]
NAME=Scene1
BKCOLOR=255,128,0
BKTEXTURE=background.bmp
DEFCURSOR=arrow
CAPS=1
```

### 2. Compréhension de la Logique

Le code assembleur montre **comment** les données sont parsées:

```assembly
; Lecture de BKCOLOR
call    TProfile::GetString  ; Lit "255,128,0"
call    sscanf               ; Parse avec "%u,%u,%u"
mov     [area.r], eax        ; Stocke R
mov     [area.g], ebx        ; Stocke G
mov     [area.b], ecx        ; Stocke B
```

### 3. Documentation Complète

Chaque fichier markdown devient une documentation technique complète:
- Code assembleur complet
- Toutes les données référencées
- Appels de fonctions importants
- Format des paramètres INI

---

## ⚠️ Problèmes Potentiels et Solutions

### Problème 1: "Type string not found" pour certaines structures

**Cause**: La structure n'utilise pas de type string classique

**Solution**: Recherche manuelle dans IDA:
1. Cherche les références au nom de la structure (Alt+T)
2. Analyse les constructeurs trouvés
3. Cherche `mov [reg], offset vtable` dans le constructeur

### Problème 2: Plusieurs vtables candidates trouvées

**Cause**: Plusieurs adresses ressemblent à des vtables

**Solution**: Validation manuelle:
1. Regarde `MISSING_VTABLES_FOUND.md` section détaillée
2. Choisis la vtable avec le plus de méthodes
3. Ou celle la plus proche du type string
4. Vérifie dans IDA que les méthodes sont cohérentes

### Problème 3: IDA plante pendant l'extraction

**Cause**: Script trop long, IDA manque de mémoire

**Solution**: Extraction par batch:
1. Divise `TVN_STRUCTURES` en 3 groupes de ~12 structures
2. Lance le script 3 fois avec chaque groupe
3. Combine les résultats à la fin

---

## 📝 Checklist Complète

### Phase 1: Préparation
- [ ] IDA Pro/Free installé et fonctionnel
- [ ] europeo.exe disponible dans DOCS/
- [ ] Scripts Python à jour (git pull)

### Phase 2: Recherche des Vtables
- [ ] Ouvrir europeo.exe dans IDA
- [ ] Lancer find_missing_vtables.py
- [ ] Vérifier MISSING_VTABLES_FOUND.md créé
- [ ] Lire le résumé: combien de vtables trouvées?

### Phase 3: Mise à Jour
- [ ] Copier les adresses de vtable trouvées
- [ ] Mettre à jour extract_all_35_tvn_complete.py
- [ ] Vérifier qu'il ne reste plus de "None"

### Phase 4: Extraction Complète
- [ ] Lancer extract_all_35_tvn_complete.py dans IDA
- [ ] Attendre la fin (10-15 min)
- [ ] Vérifier TVN_COMPLETE_35_STRUCTURES/ créé

### Phase 5: Vérification
- [ ] 35 fichiers .md générés
- [ ] Aucun fichier marqué TODO
- [ ] Chaque fichier contient:
  - [ ] Code assembleur complet
  - [ ] Sections DATA formatées
  - [ ] Chaînes extraites
  - [ ] Appels de fonctions

---

## 🎉 Résultat Final

Après avoir suivi ce workflow, tu auras:

✅ **35 fichiers markdown** avec extraction complète
✅ **Code assembleur** de toutes les méthodes
✅ **Sections DATA** au format IDA (db 41h ; A, etc.)
✅ **Toutes les chaînes** ("AREA_%u", "NAME", "BKCOLOR", etc.)
✅ **Appels de fonctions** identifiés et catégorisés
✅ **Format INI** reconstruit pour chaque structure
✅ **Documentation technique** complète pour le reverse engineering

**Temps total estimé**: 20-30 minutes

---

## 🔗 Fichiers Importants

- `find_missing_vtables.py` - Cherche les vtables manquantes
- `extract_all_35_tvn_complete.py` - Script principal d'extraction
- `EXTRACTION_COMPLETE_35_TVN.md` - Guide détaillé d'utilisation
- `UTILISER_IDA_MAINTENANT.md` - Pourquoi IDA est nécessaire
- `WORKFLOW_COMPLET_35_TVN.md` - Ce fichier (workflow complet)

---

**TL;DR**:
1. Lance `find_missing_vtables.py` dans IDA → trouve les vtables
2. Copie les adresses dans `extract_all_35_tvn_complete.py`
3. Lance `extract_all_35_tvn_complete.py` dans IDA → extraction complète
4. Vérifie les 35 fichiers .md générés ✓
