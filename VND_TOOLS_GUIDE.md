# VND Tools Guide - Documentation Outils

**Version**: 1.0
**Date**: 2026-01-16

> **Note**: Guide d'utilisation de TOUS les outils VND créés. Centralise la documentation des scripts.

---

## Table des Matières

1. [Parsers VND](#parsers-vnd)
2. [Extracteurs d'Opcodes](#extracteurs-dopcodes)
3. [Analyseurs de Handlers](#analyseurs-de-handlers)
4. [Outils d'Analyse Batch](#outils-danalyse-batch)
5. [Outils Utilitaires](#outils-utilitaires)

---

## Parsers VND

### vnd_parser_v2.py ⭐ RECOMMANDÉ

**Description**: Parser VND complet avec auto-détection

**Usage**:
```bash
python3 vnd_parser_v2.py fichier.vnd
```

**Fonctionnalités**:
- ✅ Détection automatique signature VNFILE
- ✅ Parsing table variables
- ✅ Détection records (séparateur 01 00 00 00)
- ✅ Résumé par type de record

**Sortie**:
```
✓ Signature VNFILE trouvée @ 0x0009
✓ Premier record trouvé @ 0x115C
✓ Parsed 3 records

RECORDS BY TYPE:
  Type 0 (0x00): 1 records
  Type 24: 1 records

✓ Found 4 potential variables
```

**Limitations**: Type 0 non complètement parsé (structure complexe)

---

### vnd_parser.py

**Description**: Version initiale (moins robuste)

**Usage**:
```bash
python3 vnd_parser.py fichier.vnd
```

**Note**: Utiliser vnd_parser_v2.py à la place

---

## Extracteurs d'Opcodes

### extract_opcodes_from_vnd_v2.py ⭐ RECOMMANDÉ

**Description**: Extraction précise opcodes (pattern nombre+lettre)

**Usage**:
```bash
python3 extract_opcodes_from_vnd_v2.py fichier.vnd
```

**Fonctionnalités**:
- ✅ Regex `\d+[a-z]` pour trouver opcodes
- ✅ Filtrage faux positifs (lettres dans texte)
- ✅ Affichage contexte (30 chars avant/après)
- ✅ Top 20 opcodes
- ✅ Statistiques

**Sortie**:
```
✓ Trouvé 108 séquences nombre+lettre

TOP 20 OPCODES LES PLUS FRÉQUENTS:
  'i' (index 9): 46 occurrences
  'd' (index 4): 35 occurrences
  'h' (index 8): 10 occurrences

PREMIERS 100 OPCODES AVEC CONTEXTE:
@ 0x001579  1i (opcode idx 9)
  Context: ...suede = 1 then dec_var suede 1i...
```

**Note**: Peut avoir quelques faux positifs (noms fichiers comme "5n1.bmp")

---

### extract_opcodes_from_vnd.py

**Description**: Version initiale (plus de faux positifs)

**Usage**:
```bash
python3 extract_opcodes_from_vnd.py fichier.vnd
```

**Note**: Utiliser v2 à la place

---

## Analyseurs de Handlers

### analyze_handler_f_navigation.py

**Description**: Analyse handler 'f' (6) - Navigation

**Usage**:
```bash
python3 analyze_handler_f_navigation.py
```

**Sortie**:
- Désassemblage 100+ instructions
- Function calls détectés
- Pattern wrapper identifié
- Call principal: 0x4268F8

---

### analyze_handler_u_logic.py

**Description**: Analyse handler 'u' (21) - Logic if/then

**Usage**:
```bash
python3 analyze_handler_u_logic.py
```

**Sortie**:
- 35 function calls
- 23 comparisons
- Pattern conditionnel identifié
- Call principal: 0x428373

---

### analyze_handler_i_images_v2.py

**Description**: Analyse handler 'i' (9) - Images

**Usage**:
```bash
python3 analyze_handler_i_images_v2.py
```

**Note**: Utilise parsing correct des sections PE

---

### analyze_all_media_handlers.py

**Description**: Analyse batch handlers 'h','i','j','k','l'

**Usage**:
```bash
python3 analyze_all_media_handlers.py
```

**Sortie**:
- 5 handlers analysés en parallèle
- Appels de fonction pour chaque handler
- Comparaison entre handlers

**Résultat clé**: Aucun call direct aux fonctions documentées (tous via vtables)

---

### analyze_handler_g.py

**Description**: Analyse handler 'g' (7) - Tooltip variant (NOUVEAU)

**Usage**:
```bash
python3 analyze_handler_g.py
```

**Sortie**:
- Désassemblage
- Calls identiques à handler 'h'
- Confirmation: variante tooltip

---

## Outils d'Analyse Batch

### test_batch_vnd_parser.py

**Description**: Test rapide de tous les fichiers VND

**Usage**:
```bash
python3 test_batch_vnd_parser.py
```

**Sortie**:
```
✓ Trouvé 19 fichiers VND

✓ allem.vnd        62.9 KB  Sig @ 0x0009  Records: 17
✓ angleterre.vnd   85.0 KB  Sig @ 0x0009  Records:  4
...

STATISTIQUES:
Fichiers valides: 19/19
Taille moyenne: 64.9 KB
Records moyen: 7.2
```

**Utilité**: Vue d'ensemble rapide du dataset

---

### batch_extract_opcodes.py ⭐ RECOMMANDÉ

**Description**: Extraction opcodes de tous les fichiers + comparaison

**Usage**:
```bash
python3 batch_extract_opcodes.py
```

**Sortie**:
```
allemand.vnd         49 opcodes   6 unique  Top: 'd': 23, 'i': 11, 'l': 8
angleterre.vnd      132 opcodes   9 unique  Top: 'i': 84, 'd': 13, 'l': 10
...

ANALYSE GLOBALE:
Total opcodes extraits: 1461
Opcodes uniques: 11

TOP 20 OPCODES (tous fichiers):
  'i' (idx 9 - Images/INDEX): 603 (41.3%)
  'd' (idx 4 - DIRECT suffix): 434 (29.7%)
  ...

NOUVEAUX OPCODES (non vus dans couleurs1.vnd):
  'g' (idx 7 - Unknown-g): 44 occurrences
  'n' (idx 14 - Unknown-n): 144 occurrences
```

**Utilité**:
- Découvrir nouveaux opcodes
- Valider patterns
- Comparer fichiers

---

## Outils Utilitaires

### extract_opcode_table.py

**Description**: Extrait la switch table du dispatcher

**Usage**:
```bash
python3 extract_opcode_table.py
```

**Sortie**:
```
OPCODE SWITCH TABLE @ 0x004317D5

| Index | Hex  | Handler Addr  | Description |
|-------|------|---------------|-------------|
|     1 | 0x01 | 0x00431844    | 'a' = Unknown
|     2 | 0x02 | 0x00431854    | 'b' = Unknown
...
|     6 | 0x06 | 0x0043198B    | 'f' = Navigation
|     7 | 0x07 | 0x00431B2B    | 'g' = Unknown
|     8 | 0x08 | 0x00431B70    | 'h' = Tooltip
|     9 | 0x09 | 0x004321B6    | 'i' = Images (AVI/BMP)
...
```

**Utilité**: Trouver adresses des handlers inconnus

---

### map_records_to_opcodes.py

**Description**: Parse records et extrait leurs opcodes

**Usage**:
```bash
python3 map_records_to_opcodes.py fichier.vnd
```

**Sortie**:
- Records parsés avec type
- Opcodes trouvés dans chaque record
- Analyse par type de record

**Note**: Détection limitée pour Type 0 complexe

---

### analyze_dispatcher.py

**Description**: Analyse le dispatcher @ 0x43177D

**Usage**:
```bash
python3 analyze_dispatcher.py
```

**Sortie**:
- Confirmation switch table @ 0x4317D5
- 43 entrées documentées
- Mécanisme de saut analysé

---

## Workflow Recommandé

### 1. Analyse Rapide Fichier Unique

```bash
# 1. Vue d'ensemble
python3 test_batch_vnd_parser.py

# 2. Parser le fichier
python3 vnd_parser_v2.py fichier.vnd

# 3. Extraire opcodes
python3 extract_opcodes_from_vnd_v2.py fichier.vnd
```

---

### 2. Analyse Batch (Tous Fichiers)

```bash
# 1. Statistiques globales
python3 test_batch_vnd_parser.py

# 2. Opcodes de tous les fichiers
python3 batch_extract_opcodes.py

# 3. Comparer patterns
# (Analyser sortie batch_extract_opcodes.py)
```

---

### 3. Analyse Handler

```bash
# 1. Trouver adresse dans switch table
python3 extract_opcode_table.py | grep "'X'"

# 2. Créer script d'analyse
# (Copier analyze_handler_g.py et adapter)

# 3. Analyser
python3 analyze_handler_X.py
```

---

### 4. Découverte Nouveaux Opcodes

```bash
# 1. Batch extract
python3 batch_extract_opcodes.py

# 2. Chercher section "NOUVEAUX OPCODES"
# (Opcodes non vus dans couleurs1.vnd)

# 3. Analyser contextes
python3 extract_opcodes_from_vnd_v2.py fichier_avec_nouveau.vnd | grep "opcode ('X')"
```

---

## Dépendances

### Python (3.x)

**Modules requis**:
```bash
pip install capstone  # Pour désassemblage
```

**Modules standard**:
- struct (manipulation binaire)
- re (regex pour opcodes)
- collections (Counter, defaultdict)
- os, sys (système fichiers)

---

### Fichiers Requis

**Binaire**:
- `DOCS/europeo.exe` (pour analyse handlers)

**VND**:
- `Vnd-vnp/*.vnd` (19 fichiers pour batch)
- `couleurs1.vnd` (référence)

---

## FAQ

### Q: Quel parser utiliser?

**A**: `vnd_parser_v2.py` - version améliorée avec auto-détection

---

### Q: Comment trouver tous les opcodes d'un fichier?

**A**: `python3 extract_opcodes_from_vnd_v2.py fichier.vnd`

---

### Q: Comment analyser tous les fichiers d'un coup?

**A**: `python3 batch_extract_opcodes.py`

---

### Q: J'ai trouvé un nouveau opcode, que faire?

**A**:
1. Vérifier qu'il n'est pas dans un nom de fichier (faux positif)
2. Chercher adresse: `python3 extract_opcode_table.py | grep "'X'"`
3. Analyser handler avec capstone
4. **Mettre à jour VND_MASTER_REFERENCE.md** (pas nouveau doc!)

---

### Q: Pourquoi certains handlers n'appellent pas les fonctions documentées?

**A**: Tous les handlers utilisent **vtables** (appels indirects):
```asm
call dword ptr [ecx + offset]  ; Pas d'adresse directe
```

Les fonctions documentées sont appelées via polymorphisme C++.

---

### Q: Opcode 'n' a 144 occurrences mais n'est pas dans les handlers?

**A**: FAUX POSITIF! C'est dans les noms de fichiers:
```
addbmp photos\5n1.bmp
              ^^^ nom fichier, pas opcode
```

---

## Maintenance

### Ajouter Nouveau Handler

1. Copier `analyze_handler_g.py`
2. Modifier `HANDLER_X_ADDR` avec adresse de switch table
3. Exécuter
4. **Mettre à jour VND_MASTER_REFERENCE.md** avec résultats

**Ne PAS créer nouveau document séparé!**

---

### Ajouter Nouveau Fichier VND

1. Copier dans `Vnd-vnp/`
2. Tester: `python3 test_batch_vnd_parser.py`
3. Extraire: `python3 batch_extract_opcodes.py`
4. **Mettre à jour VND_MASTER_REFERENCE.md** si patterns nouveaux

---

**Maintenu par**: Claude Code Analysis
**Dernière mise à jour**: 2026-01-16

> ⚠️ **IMPORTANT**: Ce guide centralise TOUS les outils. Ne créez pas de nouveaux guides séparés.
