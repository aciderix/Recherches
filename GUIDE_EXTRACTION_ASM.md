# Guide - Extraction Automatique du Code Assembleur TVN

Ce guide explique comment extraire automatiquement le code assembleur de toutes les méthodes des 35 structures TVN.

---

## 🎯 Objectif

Reproduire automatiquement le travail manuel que tu as fait pour TVNSceneParms, mais pour **TOUTES** les 35 structures TVN.

**Résultat**: Un fichier markdown par structure TVN contenant:
- Le code assembleur complet de chaque méthode
- Les références aux chaînes de caractères
- Les appels de fonctions (avec mise en évidence des appels importants comme `TProfile::GetString`)
- Les commentaires et annotations

---

## 🛠️ Méthode Recommandée: IDA Python

**Script**: `extract_all_tvn_ida_simple.py`

### Pourquoi IDA ?

✅ **Avantages**:
- Tu l'as déjà utilisé avec succès manuellement
- Meilleure analyse des fonctions
- Désassemblage de qualité supérieure
- Identification automatique des chaînes et appels

❌ **Inconvénient**:
- Nécessite IDA Pro (pas headless pour IDA Free)
- Doit être lancé interactivement

### Comment Utiliser

#### Étape 1: Ouvrir europeo.exe dans IDA

```
1. Lance IDA Pro (ou IDA Free)
2. File -> Open -> DOCS/europeo.exe
3. Accepte les options par défaut
4. Attends que l'analyse se termine (barre en bas)
```

#### Étape 2: Exécuter le Script

```
1. File -> Script file... (ou Alt+F7)
2. Sélectionne: extract_all_tvn_ida_simple.py
3. Clique Open
```

#### Étape 3: Attendre l'Extraction

Le script va:
```
[1/7] Extraction TVNCommand...
  Found 2 methods
  [0] Extracting destructor @ 0x0043BA0C...
  [1] Extracting LoadFromINI @ 0x00440090...
  ✓ Saved to TVNCommand_COMPLETE.md

[2/7] SKIPPING TVNDigitParms (shared vtable)
...
[7/7] Extraction TVNTimer...
  ✓ Saved to TVNTimer_COMPLETE.md

DONE! Check TVN_IDA_EXTRACTS/ folder
```

#### Étape 4: Vérifier les Résultats

```bash
cd TVN_IDA_EXTRACTS/
ls -lh

# Tu devrais voir :
TVNCommand_COMPLETE.md
TVNFrame_1_COMPLETE.md
TVNFrame_2_COMPLETE.md
TVNHotspot_COMPLETE.md
TVNImageObject_1_COMPLETE.md
TVNImageObject_2_COMPLETE.md
TVNTimer_COMPLETE.md
```

---

## 📋 Format des Fichiers Générés

Chaque fichier `.md` contient:

```markdown
# TVNCommand - Complete Assembly Extraction

**Vtable Address**: 0x0040E1E0
**Binary**: europeo.exe
**Tool**: IDA Pro

---

## Methods Summary

| Index | Address | Name |
|-------|---------|------|
|  0 | 0x0043BA0C | `destructor` |
|  1 | 0x00440090 | `LoadFromINI` |

---

## Method [0]: destructor

**Address**: 0x0043BA0C
**Index in vtable**: 0

### Assembly Code

```assembly
0043BA0C  55                      push    ebp
0043BA0D  8BEC                    mov     ebp, esp
0043BA0F  51                      push    ecx
0043BA10  894DFC                  mov     [ebp+var_4], ecx
...
```

### String References

- 0x0043BA20 → 0x00450123: `TVNCommand`

### Function Calls

**Important Calls** (TProfile, GetString, etc.):

- ⭐ 0x0043BA30 → `TProfile::GetString` @ 0x00401234

**Other Calls**:

- 0x0043BA40 → `operator_delete`
- 0x0043BA50 → `_free`

---

## Method [1]: LoadFromINI

...
```

---

## 🔄 Méthodes Alternatives

### Option 2: Ghidra (Headless)

**Script**: `ExtractAllTVNMethodsASM.java`

Si tu veux utiliser Ghidra en mode automatique:

```bash
/opt/ghidra/support/analyzeHeadless \
    /tmp TVN_Project \
    -import DOCS/europeo.exe \
    -postScript ExtractAllTVNMethodsASM.java \
    -scriptPath /home/user/Recherches \
    -deleteProject
```

**Note**: Peut avoir des problèmes avec Ghidra headless.

### Option 3: radare2

**Script**: `extract_all_tvn_asm.py`

```bash
python3 extract_all_tvn_asm.py DOCS/europeo.exe TVN_ASM_EXTRACTS
```

**Note**: radare2 en mode batch ne fonctionne pas toujours bien.

### Option 4: objdump

**Script**: `extract_all_tvn_asm_objdump.py`

```bash
python3 extract_all_tvn_asm_objdump.py DOCS/europeo.exe TVN_ASM_COMPLETE
```

**Note**: objdump ne trouve pas toujours les fonctions aux adresses calculées.

---

## 📊 Structures à Extraire

### 7 Vtables Uniques

Le script extrait **7 vtables uniques** (les autres partagent la même vtable):

1. **TVNCommand** (`0x0040E1E0`) - Base class
   - Partagée par 16 structures *Parms

2. **TVNFrame_1** (`0x00435B50`)

3. **TVNFrame_2** (`0x00435DD4`)

4. **TVNHotspot** (`0x00413514`)

5. **TVNImageObject_1** (`0x00429980`)

6. **TVNImageObject_2** (`0x004299D0`)

7. **TVNTimer** (`0x004394D4`)

### Structures Partageant la Vtable de Base

Ces 16 structures partagent `0x0040E1E0`:
```
TVNCommand         TVNDigitParms      TVNExecParms       TVNFontParms
TVNHtmlParms       TVNIfParms         TVNImageParms      TVNImgObjParms
TVNImgSeqParms     TVNMidiParms       TVNProjectParms    TVNSceneParms
TVNSetVarParms     TVNStringParms     TVNTextObjParms    TVNTextParms
```

---

## 🎯 Ce Que le Script Extrait

Pour chaque méthode de chaque vtable:

### 1. Code Assembleur Complet
```assembly
0043BA0C  push    ebp
0043BA0D  mov     ebp, esp
0043BA0F  push    ecx
...
```

### 2. Références aux Chaînes
```
- 0x0043BA20 → "NAME"
- 0x0043BA30 → "BKCOLOR"
- 0x0043BA40 → "CAPS"
```

### 3. Appels de Fonctions
**Important** (⭐):
```
- TProfile::GetString
- TProfile::GetInt
- LoadFromINI
- ParseData
```

**Autres**:
```
- operator_new
- operator_delete
- memcpy
- sprintf
```

---

## 🔍 Recherche d'Appels Importants

Le script met en évidence automatiquement les appels à:

- `TProfile::GetString` / `GetInt` - Lecture INI
- `LoadFromINI` - Chargement
- `Parse*` - Parsing
- `*Profile*` - Gestion profil

Ces appels sont marqués ⭐ dans la section "Important Calls".

---

## ✅ Vérification des Résultats

### Vérification 1: Nombre de Fichiers

```bash
ls TVN_IDA_EXTRACTS/ | wc -l
# Devrait afficher: 7
```

### Vérification 2: Contenu d'un Fichier

```bash
head -50 TVN_IDA_EXTRACTS/TVNCommand_COMPLETE.md
```

Tu devrais voir:
- Header avec infos vtable
- Tableau récapitulatif des méthodes
- Code assembleur pour chaque méthode

### Vérification 3: Appels Importants

```bash
grep -r "⭐" TVN_IDA_EXTRACTS/
```

Tu devrais voir les appels à `TProfile`, `GetString`, etc.

---

## 🐛 Résolution de Problèmes

### Problème: "Script error"

**Solution**: Vérifie que tu es bien dans IDA (pas headless).

### Problème: "No methods found"

**Solution**: Vérifie que l'analyse IDA est complète (barre en bas = 100%).

### Problème: "Permission denied"

**Solution**:
```bash
chmod +x extract_all_tvn_ida_simple.py
```

### Problème: Fichiers vides

**Solution**: Relance l'analyse IDA:
```
Options -> General -> Analysis -> Reanalyze program
```

---

## 📚 Comparaison avec Extraction Manuelle

### Ce Que Tu As Fait Manuellement (TVNSceneParms)

1. Trouvé la chaîne "TVNSceneParms"
2. Suivi les références
3. Identifié la vtable
4. Pour chaque méthode:
   - Copié le code assembleur
   - Identifié les appels importants
   - Sauvegardé dans un fichier
5. Répété pour les fonctions appelées

### Ce Que le Script Fait (Automatique)

1. ✅ Utilise les adresses de vtables connues
2. ✅ Lit automatiquement les pointeurs de méthodes
3. ✅ Pour chaque méthode:
   - ✅ Extrait le code assembleur
   - ✅ Identifie les chaînes
   - ✅ Identifie les appels de fonctions
   - ✅ Met en évidence les appels importants
   - ✅ Sauvegarde dans un fichier markdown
4. ✅ Fait ça pour toutes les structures TVN
5. ✅ Extrait même les fonctions appelées (profondeur 1)

**Gain de temps**: ~40h de travail manuel → ~5 minutes automatique

---

## 🚀 Après l'Extraction

Une fois les fichiers générés:

### 1. Analyse

Ouvre les fichiers `.md` et cherche:
- Patterns communs entre structures
- Appels à `TProfile::GetString` avec les noms de clés INI
- Logique de parsing spécifique

### 2. Documentation

Utilise les résultats pour:
- Documenter chaque méthode
- Comprendre le flow d'exécution
- Identifier les clés INI utilisées

### 3. Commit

```bash
git add TVN_IDA_EXTRACTS/
git commit -m "Add complete assembly extraction for all 7 TVN vtables

Extracted assembly code for all unique vtables:
- TVNCommand (base, shared by 16 structures)
- TVNFrame_1, TVNFrame_2
- TVNHotspot
- TVNImageObject_1, TVNImageObject_2
- TVNTimer

Each file contains:
- Complete assembly code
- String references
- Function calls (with important calls highlighted)

Total: 7 structures, ~14 methods documented"

git push
```

---

## 📖 Ressources

### Scripts Créés

1. **`extract_all_tvn_ida_simple.py`** ⭐ **RECOMMANDÉ**
   - IDA Python interactif
   - Meilleure qualité
   - Plus fiable

2. `ExtractAllTVNMethodsASM.java`
   - Ghidra headless
   - Automatique mais moins fiable

3. `extract_all_tvn_asm.py`
   - radare2
   - Alternative

4. `extract_all_tvn_asm_objdump.py`
   - objdump
   - Simple mais limité

### Documentation Existante

- `TVN_SCENE_LOADER_ANALYSIS.md` - Exemple d'analyse manuelle
- `VND_COMPLETE_COMMAND_REFERENCE.md` - Toutes les commandes
- `FINAL_TVN_VTABLES_REPORT.md` - Rapport complet vtables

---

## ✨ Résumé

**Pour extraire tout le code assembleur automatiquement**:

```
1. Ouvre DOCS/europeo.exe dans IDA Pro
2. File -> Script file... -> extract_all_tvn_ida_simple.py
3. Attends 2-5 minutes
4. Check TVN_IDA_EXTRACTS/ → 7 fichiers .md créés
5. Profite! 🎉
```

**Temps estimé**: 5 minutes (vs 40h manuellement)

**Résultat**: Code assembleur complet de toutes les méthodes TVN, formaté et annoté.

---

Bon courage avec l'extraction! 🚀
