# VND Master Reference - Documentation Centralisée

**Version**: 2.0
**Date**: 2026-01-16
**Status**: 70% complété

> **Note**: Ce document centralise TOUTE la documentation VND. Ne créez plus de nouveaux documents séparés - mettez à jour celui-ci.

---

## Table des Matières

1. [Format VND](#format-vnd)
2. [Système d'Opcodes](#système-dopcodes)
3. [Handlers Analysés](#handlers-analysés)
4. [Patterns d'Usage](#patterns-dusage)
5. [Fichiers VND Analysés](#fichiers-vnd-analysés)
6. [Références Techniques](#références-techniques)

---

## Format VND

### Structure Générale

```
[HEADER]
  - Signature: "VNFILE" @ offset 0x09
  - Version, projet, créateur
  - Dimensions écran (640x480)
  - Checksum @ 0x4C
  - DLL path (..\VnStudio\vnresmod.dll)

[TABLE VARIABLES] @ ~0x88
  Format: [LENGTH:4][NAME:ASCII][00][VALUE:4]
  Variables: SACADOS, SCORE, FIOLE, CPAYS, etc.

[RECORDS] @ variable (chercher séparateur 01 00 00 00)
  Format: [SEPARATOR:01000000][LENGTH:4][TYPE:4][DATA]
```

### Types de Records Documentés

| Type | Description | Structure |
|------|-------------|-----------|
| **0** | Scène (métadonnées complexes) | Audio + images + scripts + opcodes |
| **1** | Référence scène primaire | ID scène |
| **2** | Hotspot rectangulaire | Coordonnées XYWH |
| **3** | Scripts/valeurs | Conditions, scores |
| **5** | État du jeu | Variables globales |
| **8-12** | Audio | WAV/MIDI |
| **17** | Chemins audio | Dossiers sons |
| **20-24** | Vidéos AVI | Cinématiques |
| **21** | Conditionnels | if/then/else |
| **26, 39** | Polices | Taille/style/couleur |
| **27-31** | Actions | addbmp, delbmp, runprj |
| **38** | Texte hotspot | Format "X Y W H 0 Nom" |
| **105** | Polygone cliquable | Point count + coords |

**Note Type 0**: Le champ LENGTH n'est PAS fiable - chercher prochain séparateur

---

## Système d'Opcodes

### Mécanisme de Parsing (sub_407FE5)

```c
// Parsing des commandes VND
char* ptr = command_string;
int number = atol(ptr);     // Lit chiffres jusqu'à non-digit
char opcode = *ptr;         // Caractère suivant = opcode
int index = opcode - 'a' + 1;  // Conversion en index

// Dispatcher @ 0x43177D
switch_table[index]();      // Saute vers handler via table @ 0x4317D5
```

**Exemples**:
- `"54h"` → number=54, opcode='h' (index 8)
- `"euroj"` → texte="euro", opcode='j' (index 10)
- `"5i"` → number=5, opcode='i' (index 9)

### Distribution Globale (1461 opcodes sur 19 fichiers)

| Opcode | Idx | Handler @ | Fonction | Count | % | Status |
|--------|-----|-----------|----------|-------|---|--------|
| **'i'** | 9 | 0x004321B6 | Images/INDEX | 603 | 41.3% | ✓ |
| **'d'** | 4 | ? | DIRECT suffix | 434 | 29.7% | Suffixe |
| **'l'** | 12 | 0x00432297 | MIDI Music | 94 | 6.4% | ✓ |
| **'h'** | 8 | 0x00431B70 | Tooltip | 50 | 3.4% | ✓ |
| **'g'** | 7 | 0x00431B2B | Tooltip variant | 44 | 3.0% | ✓ |
| **'e'** | 5 | 0x004318EE | Audio+Image | 35 | 2.4% | ✓ |
| **'j'** | 10 | 0x00432201 | Bitmaps | 34 | 2.3% | ✓ |
| **'k'** | 11 | 0x0043224C | Audio WAV | 11 | 0.8% | ✓ |
| **'f'** | 6 | 0x0043198B | Navigation | 11 | 0.8% | ✓ |
| **'u'** | 21 | 0x00431A7C | Logic if/then | 0 | 0% | ✓ |
| **'a'** | 1 | ? | Unknown | 1 | 0.1% | Rare |

**Note**: 'n' (144 occ.) = FAUX POSITIF (noms fichiers: "5n1.bmp")

---

## Handlers Analysés

### Handlers Analysés (9 sur 43 - 20.9%)

#### 'f' (6) - Navigation @ 0x0043198B

**Pattern wrapper**:
```asm
test esi, esi           ; Check params
je   skip
push [esi+...]          ; 6 params
call 0x4268F8           ; sub_4268F8 = vraie fonction
```

**Usage**: 11 occurrences
- `runprj couleurs1.vnp 54f`
- Changement de scène

**Suffixes navigation** (utilisent ce handler):
- **'i'** = INDEX: `dest = INDEX_ID + n`
- **'d'** = DIRECT: `dest = n` (absolu)
- **'+'/'−'** = RELATIF: `dest = scène_actuelle ± n`

---

#### 'g' (7) - Tooltip Variant @ 0x00431B2B ⭐ NOUVEAU

**Découvert**: Analyse batch 19 fichiers

**Appels identiques à 'h'**:
```asm
call 0x427D34    ; Call principal
call 0x427FAE    ; ← Même que handler 'h'
call 0x4280EA    ; ← Même que handler 'h'
```

**Usage**: 44 occurrences
- `runprj couleurs1.vnp 54g`
- Variante tooltip ou fonction UI apparentée

**Fichiers**: danem, ecosse, autres pays

---

#### 'h' (8) - Tooltip @ 0x00431B70

**Appels de fonction**:
```asm
call 0x427FAE
call 0x4280EA
call [eax+8]     ; Vtable
```

**Usage**: 50 occurrences
- `runprj couleurs1.vnp 54h`
- Affichage bulle d'aide après chargement projet

---

#### 'i' (9) - Images @ 0x004321B6

**DUAL PURPOSE**:
1. **Handler Images**: Chargement AVI/BMP
2. **Suffixe INDEX**: Navigation INDEX_ID+n

**Usage**: 603 occurrences (41.3% - DOMINANT)

**Appels**: Vtable indirects
```asm
call dword ptr [ecx + 0xc]
```

**Exemples**:
- `euroland\bibliobis.avi 3i` → Charge vidéo
- `scene 5i` → Va scène INDEX_ID+5
- `dec_var suede 1i` → Décrémente + navigation

---

#### 'j' (10) - Bitmaps @ 0x00432201

**Fonction**: Gestion transparence/palettes bitmaps

**Usage**: 34 occurrences
- `runprj angleterre.vnp 59j` → Charge bitmap pays
- Après description objet: `Bouteille d'encre noire 22j`

**Appels**: Vtable

---

#### 'k' (11) - Audio WAV @ 0x0043224C

**Fonction**: Lecture sons WAV

**Usage**: 11 occurrences
- `bonus2 = 1 then scene 35k` → Son si bonus actif

**Appels**: Vtable + 0x4330F1

---

#### 'l' (12) - MIDI Music @ 0x00432297

**Fonction**: Musique de fond MIDI

**Usage**: 94 occurrences (6.4%)
- `telephone = 0 then scene 16l` → Scène + musique
- `music.wav coords 2l` → Musique positionnée

**Appels**: Vtable

---

#### 'u' (21) - Logic if/then @ 0x00431A7C

**Fonction**: Évaluation conditions

**Complexité**:
- 35 function calls
- 23 comparisons
- 35 conditional jumps

**Usage**: 0 occurrence directe (conditionsimplicites)

**Pattern**: `if variable op valeur then commande`

**Appels**:
```asm
push 6 params from [esi+...]
call 0x428373    ; sub_428373 = moteur logique
```

---

#### 'e' (5) - Audio+Image @ 0x004318EE ✅ ANALYSÉ

**Fonction**: Handler combiné multimédia (Audio + Image)

**Mécanisme découvert**:
```asm
push [esi+8]
push esi
push ebx
call 0x427b56           ; ← sub_427B56 = Audio WAV (handler 'k')
...
jmp  0x4321b6           ; ← Handler 'i' (Images)
```

**Rôle**: Pré-processeur multimédia
1. Charge/joue audio via 0x427B56 (fonction WAV handler 'k')
2. Délègue à handler 'i' pour affichage image

**Usage**: 35 occurrences (2.4%)
- `runprj couleurs1.vnp 54e`
- Scènes avec audio + visuel

**Fichiers**: holl.vnd (4×), autres pays

**Pattern**: Opcode de convenance pour scènes audiovisuelles

---

### Handlers À Analyser

**TODO**: Désassembler et identifier fonction

---

### Handlers Inconnus (35 restants)

**Avec occurrences**:
- 'a' (1) @ ? - 1 occurrence (rare)
- 'b' (2) @ ?
- 'c' (3) @ ?
- 'm' (13-20) @ ?
- Autres (22-26, 27+)

**Sans occurrences détectées**: À investiguer dans switch table

---

## Patterns d'Usage

### Pattern Post-Load Actions

**Après `runprj projet.vnp XX`**, différents opcodes exécutent des actions:

```
runprj couleurs1.vnp 54f  → Navigation scene 54
runprj couleurs1.vnp 54g  → Tooltip variant
runprj couleurs1.vnp 54h  → Tooltip
runprj couleurs1.vnp 54e  → Unknown (UI?)
```

**Tous partagent**: Chargement projet + scène + action spécifique

---

### Pattern Navigation Géographique

**Système de navigation européenne** (19 pays):

```
angleterre.vnp 69d  → Angleterre, scène 69
espagne.vnp 13d     → Espagne, scène 13
ecosse.vnp 33d      → Écosse, scène 33
france.vnp 27j      → France + bitmap 27
allem.vnp 5j        → Allemagne + bitmap 5
danem.vnp 4g        → Danemark + tooltip variant
```

**Pattern**: `pays.vnp XXopcode`

**Pays disponibles**: 19 fichiers VND (angleterre, france, espagne, ecosse, allem, autr, belge, danem, finlan, grece, holl, irland, italie, portu, suede)

---

### Pattern Conditions

```
if variable = valeur then opcode
variable = valeur then dec_var variable opcode
bonus = 1 then scene XXopcode
```

**Exemples**:
- `score < 0 then runprj ...`
- `telephone = 0 then scene 16l`
- `sacados = 1 then if annule = 0 then ...`

---

### Pattern Médias

```
chemin.avi coords opcode      → Vidéo
music.wav coords opcode       → Audio
chemin.bmp coords opcode      → Image
addbmp image chemin coords    → Ajouter bitmap
```

---

## Fichiers VND Analysés

### Dataset Complet (19 fichiers, 1.2 MB)

| Fichier | Taille | Records | Opcodes | Caractéristique |
|---------|--------|---------|---------|-----------------|
| biblio.vnd | 138KB | 9 | 329 | Galerie photos (répétitif) |
| france.vnd | 98KB | 0 | 65 | France |
| angleterre.vnd | 85KB | 4 | 132 | Angleterre (beaucoup 'i') |
| couleurs1.vnd | 74KB | 3 | 108 | Référence principale |
| belge.vnd | 74KB | 16 | 64 | Belgique |
| autr.vnd | 73KB | 1 | 54 | Autriche |
| italie.vnd | 73KB | 0 | 60 | Italie |
| portu.vnd | 73KB | 0 | 36 | Portugal |
| espa.vnd | 73KB | 0 | 64 | Espagne |
| ecosse.vnd | 70KB | 0 | 137 | Écosse (beaucoup 'd') |
| allem.vnd | 63KB | 17 | 49 | Allemagne |
| irland.vnd | 61KB | 50 | 127 | Irlande (MAX records!) |
| grece.vnd | 55KB | 3 | 45 | Grèce |
| holl.vnd | 55KB | 3 | 46 | Hollande |
| suede.vnd | 51KB | 2 | 36 | Suède |
| finlan.vnd | 44KB | 0 | 51 | Finlande |
| danem.vnd | 41KB | 4 | 42 | Danemark |
| barre.vnd | 28KB | 25 | 12 | Barre navigation (100% 'd') |
| start.vnd | 6KB | 0 | 4 | Écran démarrage |

**Total**: 1461 opcodes, 11 types uniques

---

### Fichiers Remarquables

#### biblio.vnd (138KB) - Galerie Photos

**Structure**:
```
addbmp image photos\5n1.bmp 0 0
addbmp image photos\11n1.bmp 0 0
addbmp image photos\2n1.bmp 0 0
```

**Note**: "5n", "11n" → noms de fichiers, PAS des opcodes!

**Opcodes**: 329 total, 3 types seulement
- 'i': 157 (Images)
- 'n': 144 (FAUX POSITIFS - filenames)
- 'd': 28 (Navigation)

---

#### irland.vnd (61KB) - Structure Dense

**50 records détectés** (maximum!)

**Opcodes**: 127 total, 'd' dominant (64.6%)

**Caractéristique**: Navigation directe intensive entre scènes

---

#### barre.vnd (28KB) - Menu Navigation

**25 records** pour petit fichier

**Opcodes**: 12 total, 100% 'd' (DIRECT)

**Fonction**: Barre de navigation ou menu

---

## Références Techniques

### Dispatcher

**Adresse**: sub_43177D @ 0x0043177D

**Switch Table**: @ 0x004317D5 (43 entrées)

**Mécanisme**:
```asm
; ecx = opcode index (1-43)
jmp dword ptr [ecx*4 + 0x4317d5]
```

**Formule index**: `index = caractère - 'a' + 1`

---

### Polymorphisme C++

**Tous les handlers** utilisent des vtables:
```asm
call dword ptr [ecx + offset]  ; Appel indirect via vtable
call dword ptr [eax + 8]
```

**Pas d'appels directs** aux fonctions documentées trouvés

**Exemple**:
```asm
; Handler 'i' (Images)
mov ecx, [context]
call dword ptr [ecx + 0xc]  ; Vtable call
```

---

### Table Variables

**Adresse runtime**: @ 0x44ECCE (dword_44ECCE)

**Format en mémoire**: À dumper avec débogueur

**Variables connues**: SACADOS, SCORE, FIOLE, CPAYS, INDEX_ID

**INDEX_ID**: Variable clé pour navigation INDEX (suffixe 'i')

---

### Fonctions Clés

| Fonction | Adresse | Usage |
|----------|---------|-------|
| Dispatcher | 0x0043177D | Répartiteur principal |
| atol parser | 0x00407FE5 | Extraction nombres |
| Navigation | 0x004268F8 | Handler 'f' appelle |
| Logic engine | 0x00428373 | Handler 'u' appelle |
| Tooltip | 0x00427FAE | Handlers 'g'+'h' appellent |
| Tooltip 2 | 0x004280EA | Handlers 'g'+'h' appellent |
| Images | 0x0042703A | Handler 'i' (doc, pas confirmé) |
| Bitmaps | 0x004275F6 | Handler 'j' (doc, pas confirmé) |
| WAV | 0x00427B56 | Handler 'k' (doc, pas confirmé) |
| MIDI | 0x00427C42 | Handler 'l' (doc, pas confirmé) |

---

## Changelog

### v2.0 - 2026-01-16
- ✅ Consolidation de tous les documents en un seul
- ✅ Ajout handler 'g' (nouveau découvert)
- ✅ Analyse batch 19 fichiers
- ✅ 1461 opcodes totaux documentés
- ✅ False positive 'n' identifié

### v1.0 - 2026-01-16
- ✅ Format VND documenté
- ✅ Système opcodes décodé
- ✅ 7 handlers analysés (f,u,h,i,j,k,l)
- ✅ couleurs1.vnd analysé (108 opcodes)
- ✅ Navigation géographique identifiée

---

**Maintenu par**: Claude Code Analysis
**Dernière mise à jour**: 2026-01-16
**État**: 70% complété (8/43 handlers, format compris, 19 fichiers analysés)

> ⚠️ **IMPORTANT**: Pour toute nouvelle découverte, METTRE À JOUR CE DOCUMENT au lieu de créer un nouveau fichier.
