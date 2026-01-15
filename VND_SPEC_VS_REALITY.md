# VND Format - Spécification vs Réalité

## ⚠️ DÉCOUVERTE IMPORTANTE

La spécification fournie **NE CORRESPOND PAS** au fichier `couleurs1.vnd`.

Ce document compare ce qui était attendu vs ce qui a été trouvé.

---

## 📋 Comparaison des Types de Records

### Types documentés dans la spec

| Type | Spec dit | couleurs1.vnd | Status |
|------|----------|---------------|--------|
| 2 | Hotspot RECTANGLE (16 bytes: X1,Y1,X2,Y2) | 8 occurrences, 6 bytes, binaire | ❌ Différent |
| 6 | Navigation / scène (ASCII chiffres+lettre) | 3 occurrences, 1 byte, binaire | ⚠️ Partiellement |
| 21 (0x15) | Script / condition (avec "then") | **0 occurrence** | ❌ Absent |
| 38 (0x26) | Tooltip (X Y W H layer texte) | 13 occurrences, scripts conditionnels | ❌ Différent |
| 39 (0x27) | Police (SIZE STYLE #RRGGBB FONT) | 6 occurrences, scripts conditionnels | ❌ Différent |
| 105 (0x69) | Hotspot POLYGONE (count + points) | **0 occurrence** | ❌ Absent |
| 257 (0x101) | Signature interne | **0 occurrence** | ❌ Absent |
| 1634296933 | Checksum | **0 occurrence** | ❌ Absent |

### Verdict

**❌ La spécification décrit un format VND différent**

---

## 🔍 Ce qui a été réellement trouvé

### Structure générale confirmée ✅

```
01 00 00 00        ← séparateur (uint32 = 1) ✅ CORRECT
LL LL LL LL        ← longueur du payload ✅ CORRECT
TT TT TT TT        ← type de record ✅ CORRECT
DD DD DD ...       ← données (payload) ✅ CORRECT
```

### Types réels dans couleurs1.vnd

#### Scripts conditionnels (la majorité)

**Types 20-65**: Presque tous sont des **scripts conditionnels** avec `then`

| Type | Occurrences | Pattern |
|------|-------------|---------|
| 32 (0x20) | 91 | `variable = valeur then commande` |
| 37 (0x25) | 28 | Scripts avec `playwav` |
| 45 (0x2d) | 21 | Scripts avec `runprj` |
| 51 (0x33) | 17 | Scripts avec `playavi` |
| 30 (0x1e) | 16 | Scripts avec `dec_var` |
| 35 (0x23) | 15 | Scripts variés |
| 43 (0x2b) | 15 | Scripts avec `runprj` |
| 23 (0x17) | 14 | Scripts avec `scene` |
| 38 (0x26) | 13 | Scripts avec `dec_var` |
| ...et 36 autres types | ... | ... |

**Total: 46 types différents, dont ~40 sont des scripts**

#### Gros blocs binaires

| Type | Taille | Contenu |
|------|--------|---------|
| 3328 (0x0d00) | 26,931 bytes | Données binaires (coordonnées?) |
| 5376 (0x1500) | 822 bytes | Mixte ASCII/binaire |
| 9984 (0x2700) | 53 bytes | Binaire |

---

## 🧩 Découverte Majeure: Commandes en Chunks

### Observation

Les commandes **ne sont PAS tronquées** - elles sont **divisées en chunks** !

### Exemple réel

```hex
Offset 0x00899f:
01 00 00 00              ← séparateur
15 00 00 00              ← longueur = 21 bytes
20 00 00 00              ← type = 32
"bonus4 = 1 then dec_"   ← chunk 1 (21 bytes)

Texte suivant (entre les records):
"var score 10"           ← chunk 2 (continuation)

Prochain record:
01 00 00 00              ← nouveau séparateur
```

**Commande complète**: `bonus4 = 1 then dec_var score 10`

### Implication

Le parser doit **reconstituer** les commandes en lisant:
1. Le payload du record
2. Le texte entre ce record et le suivant
3. Combiner les deux pour obtenir la commande complète

---

## 📊 Statistiques couleurs1.vnd

### Fichier

- **Taille**: 76,174 bytes
- **Records totaux**: 389
- **Types différents**: 46

### Contenu

| Zone | Offset | Taille | Description |
|------|--------|--------|-------------|
| Header | 0x0000 - 0x0086 | 134 bytes | Métadonnées (VNFILE, version, résolution) |
| Variables | 0x0086 - 0x1154 | 3,278 bytes | 281 variables de jeu |
| Padding | 0x1154 - 0x115C | 8 bytes | Zeros |
| Scene Data | 0x115C - EOF | ~72 KB | 389 records de commandes/données |

### Types de records

| Catégorie | Count | Exemples |
|-----------|-------|----------|
| Scripts conditionnels | ~300 | `bonus3 = 1 then playavi ...` |
| Binaires petits | ~50 | Type 1, 2, 3: données courtes |
| Gros blocs | 3 | Type 3328, 5376, 9984 |
| Texte mixte | ~36 | Types variés avec ASCII partiel |

---

## 🎮 Commandes Identifiées

### Commandes multimédia

```
playavi <fichier> <loop> [x y w h]
playwav <fichier> <loop>
addbmp <nom> <fichier> <layer> <x> <y>
delbmp <nom>
closewav
```

### Commandes de navigation

```
runprj <projet.vnp> <scene>
scene <numéro>
```

### Commandes de variables

```
set_var <variable> <valeur>
dec_var <variable> [montant]
inc_var <variable> [montant]
```

### Syntaxe conditionnelle

```
<variable> <op> <valeur> then <commande>

Opérateurs: =, !=, <, >, >=, <=
```

### Exemples réels

```
bonus3 = 0 then playwav bruit\boing.wav 1
bonus3 = 0 then set_var bonus3 1
telephone = 0 then closewav
telephone = 0 then playavi euroland\biblio1.avi 1 754 217 873 325
milleeuro = 0 then playavi euroland\banq41.avi 1 168 122 344 374
jeu = 1 then runprj ..\biblio\biblio.vnp 2
```

---

## 🤔 Hypothèses

### Pourquoi la spec ne correspond pas?

1. **Version différente**: couleurs1.vnd utilise une version plus ancienne/récente du format
2. **Sous-format spécifique**: Ce jeu utilise un variant du format VND
3. **Compilateur différent**: Différent éditeur VnStudio = différent format
4. **Spec d'un autre jeu**: La spec décrit peut-être un autre moteur Visual Novel

### Types calculés vs fixes

Dans couleurs1.vnd, le **type semble être calculé** plutôt qu'être une catégorie fixe:

- Type 32: scripts avec `dec_var`
- Type 37: scripts avec `playwav`
- Type 45: scripts avec `runprj`
- Type 51: scripts avec `playavi`

**Hypothèse**: Le type = hash ou dérivé du contenu de la commande ?

---

## ✅ Ce qui a été confirmé

### Structure de base ✓

- Séparateur `01 00 00 00` ✓
- Format `[separator][length][type][payload]` ✓
- Lecture séquentielle (pas d'index) ✓
- Little-endian ✓

### Header ✓

- Magic: `0x3A010100` ✓
- Signature: "VNFILE" ✓
- Version: "2.136" ✓
- Résolution: 640x480x16 ✓
- DLL: `vnresmod.dll` ✓

### Variables ✓

- 281 variables de jeu ✓
- Format: `[uint32 len][ASCII name][padding]` ✓

---

## 🔧 Outils Créés

### Pour l'analyse de couleurs1.vnd

1. **`verify_vnd_types.py`**: Compare types réels vs spec
2. **`analyze_real_types.py`**: Analyse patterns sans présupposés
3. **`parse_complete_commands.py`**: Reconstitue commandes complètes
4. **`vnd_disasm.py`**: Désassembleur context-aware
5. **`analyze_vnd_manual.py`**: Analyse manuelle corrigée

### Extraction

- **`couleurs1_resources/files.txt`**: Liste des fichiers référencés
- **`couleurs1_resources/texts.txt`**: Textes extraits
- **`couleurs1_resources/variables.txt`**: 281 variables

---

## 🎯 Prochaines Étapes

### Pour comprendre complètement le format

1. **Analyser d'autres fichiers VND**
   - Vérifier si la spec correspond à d'autres jeux
   - Identifier les variations du format
   - Documenter les différentes versions

2. **Reverse engineer vnresmod.dll**
   - Analyser avec Ghidra
   - Identifier l'interpréteur de commandes
   - Comprendre le calcul des types
   - Documenter toutes les commandes

3. **Tester avec d'autres jeux VnStudio**
   - Voir si les types varient entre jeux
   - Identifier les constantes du format

4. **Créer un parser universel**
   - Détecter la version du format
   - Parser selon les règles appropriées
   - Gérer les différents variants

---

## 📚 Documentation

### Fichiers créés

- `VND_FORMAT_ANALYSIS.md` - Analyse initiale (partiellement incorrecte)
- `VND_FORMAT_CORRECTED.md` - Corrections après analyse manuelle
- `VND_SCRIPTING_LANGUAGE.md` - Documentation du langage de script
- `VND_SPEC_VS_REALITY.md` - Ce document (comparaison spec vs réalité)

---

## 💡 Conclusion

### Ce qui est sûr

1. ✅ La structure de base `[01][length][type][payload]` est correcte
2. ✅ Le format est linéaire, séquentiel
3. ✅ Le header et les variables sont bien compris
4. ✅ Les commandes de script existent et fonctionnent
5. ✅ Le langage de script a été partiellement documenté

### Ce qui reste incertain

1. ❓ Pourquoi la spec ne correspond pas
2. ❓ Comment les types sont calculés
3. ❓ Signification exacte de chaque type
4. ❓ Format précis des gros blocs binaires
5. ❓ Toutes les commandes possibles du langage

### Recommandation

**Ne pas utiliser aveuglément la spec fournie pour ce fichier.**

À la place:
- Utiliser les outils créés qui analysent la structure réelle
- Parser de manière adaptive selon le contenu
- Tester sur d'autres fichiers VND pour valider

---

**Date**: 2026-01-15
**Fichier analysé**: couleurs1.vnd (76,174 bytes)
**Records parsés**: 389
**Types identifiés**: 46
**Commandes trouvées**: ~300 scripts + données

**Status**: ✅ Format réel documenté, différent de la spec fournie
