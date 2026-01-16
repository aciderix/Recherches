# Système d'Opcodes VND Europeo - Documentation Complète

## Vue d'ensemble

Le moteur Europeo utilise un système d'opcodes alphabétiques ('a'-'z') pour exécuter des commandes dans les fichiers VND. Les opcodes sont extraits par un mécanisme de parsing qui utilise `atol()` pour consommer les nombres, puis interprète le caractère suivant comme un opcode.

## Mécanisme de Parsing (sub_407FE5)

### Principe
1. **Extraction des paramètres**: `atol()` lit les chiffres un par un
2. **Point de rupture**: `atol()` s'arrête au premier caractère NON numérique
3. **Exécution**: Le caractère suivant est immédiatement interprété comme un **opcode**

### Exemples
- `54h` → paramètre=54, opcode='h' (Tooltip)
- `euroj` → texte="euro", opcode='j' (playbmp)
- `5i` → paramètre=5, opcode='i' (Images)

### Conversion Index
```
index = caractère - 'a' + 1
'a' → 1, 'b' → 2, ..., 'z' → 26
```

## Dispatcher (sub_43177D)

Switch table @ **0x004317D5** avec 43 entrées (indices 0x00-0x2A)

Mécanisme: `jmp dword ptr [ecx*4 + 0x4317d5]`

## Opcodes d'Action Principaux

| Opcode | Index | Handler @ | Fonction | Description |
|--------|-------|-----------|----------|-------------|
| **'f'** | 6 | 0x0043198B | sub_4268F8 | **Navigation/changement de scène** |
| **'h'** | 8 | 0x00431B70 | sub_426D33 | **Tooltip** (bulle d'aide) |
| **'i'** | 9 | 0x004321B6 | sub_42703A | **Images** (chargement AVI/BMP) |
| **'j'** | 10 | 0x00432201 | sub_4275F6 | **Bitmaps** (transparence, palettes) |
| **'k'** | 11 | 0x0043224C | sub_427B56 | **Audio WAV** |
| **'l'** | 12 | 0x00432297 | sub_427C42 | **Musique MIDI** |
| **'u'** | 21 | 0x00431A7C | sub_428373 | **Logic if/then/else** (conditions) |

## Suffixes de Navigation

Certaines lettres après un nombre sont des **SUFFIXES** pour la commande `scene` (opcode 'f'), pas des opcodes standalone:

### Suffixe 'i' (INDEX)
- **Calcul**: `destination = INDEX_ID + n`
- **Exemple**: `5i` → va à la scène `INDEX_ID + 5`
- **INDEX_ID**: Lu à l'offset 65 du fichier VND ou dans le fichier INI

### Suffixe 'd' (DIRECT)
- **Calcul**: `destination = n` (absolu)
- **Exemple**: `13d` → va directement à la scène 13

### Suffixe '+' ou '-' (RELATIF)
- **Calcul**: `destination = scène_actuelle ± n`
- **Exemple**: `+1` → scène suivante, `-2` → 2 scènes avant

### Sans Suffixe
- Par défaut, traité comme DIRECT

## Statistiques couleurs1.vnd

Extraction de 108 séquences nombre+lettre:

| Opcode | Occurrences | Type |
|--------|-------------|------|
| 'i' | 46 | Images / INDEX suffix |
| 'd' | 35 | DIRECT suffix |
| 'h' | 10 | Tooltip |
| 'j' | 8 | Bitmaps |
| 'f' | 3 | Navigation |
| 'l' | 3 | MIDI |
| 'k' | 1 | Audio WAV |

## Exemples Réels (couleurs1.vnd)

### Navigation
```
scene 16l     @ 0x0027CC  → scène 16 + MIDI
scene 54f     @ 0x002551  → navigation vers scène 54
scene 54i     @ 0x003C3E  → scène INDEX_ID+54
scene 54d     @ 0x0068B1  → scène directe 54
scene 15d     @ 0x007CCA  → scène directe 15
```

### Actions
```
54h  @ 0x001B6C  → runprj couleurs1.vnp scène 54, puis Tooltip
22j  @ 0x001D06  → playbmp bitmap 22 (Bouteille d'encre noire)
59j  @ 0x002C99  → playbmp bitmap 59 (après runprj angleterre.vnp)
2l   @ 0x003DCC  → play MIDI music.wav
35k  @ 0x005840  → play WAV (bonus2 = 1 then scene 35k)
```

### Conditions
```
score < 0 then runprj     @ 0x00126C  → opcode 'u' (logic)
espagne = 1 then dec_var  @ 0x0012C1  → condition if/then
sacados = 1 then if       @ 0x0076B0  → condition imbriquée
```

## Commandes Textuelles

Le VND contient aussi des **commandes textuelles** qui sont parsées:

- `addbmp` - Ajouter bitmap
- `if ... then ...` - Conditions
- `else` - Branche alternative
- `inc_var` - Incrémenter variable
- `dec_var` - Décrémenter variable
- `set_var` - Définir variable
- `runprj` - Lancer projet/scène
- `scene` - Changer de scène

Ces commandes sont suivies de leurs paramètres et opcodes.

## Structure Record Type 0 (Scène)

Format observé:
```
[SEPARATOR: 01 00 00 00]
[LENGTH: 4 bytes]
[TYPE: 00 00 00 00]
[Métadonnées scène:]
  - Fichier audio (music.wav, etc.)
  - Fichier image (euroland\face.bmp, etc.)
  - Fichier vidéo (euroland\bibliobis.avi, etc.)
  - Coordonnées, couleurs, fonts
  - Script avec commandes textuelles
  - Opcodes d'exécution
```

Le champ LENGTH ne représente **PAS** la longueur totale du record Type 0. La structure est plus complexe avec plusieurs sections de métadonnées.

## Prochaines Étapes

1. ✅ Extrait opcodes de couleurs1.vnd (108 séquences)
2. ✅ Documenté système opcodes + suffixes
3. ⏳ Analyser handlers 'i', 'j', 'k', 'l', 'h' dans IDA
4. ⏳ Créer parser VND v3 avec parsing complet des opcodes
5. ⏳ Mapper types de records → opcodes utilisés
6. ⏳ Dumper table variables @ 0x44ECCE

## Outils Créés

- `extract_opcodes_from_vnd.py` - Extraction basique (3517 candidats)
- `extract_opcodes_from_vnd_v2.py` - Extraction précise nombre+lettre (108 séquences)
- `vnd_parser.py` - Parser VND initial
- `vnd_parser_v2.py` - Parser VND amélioré avec auto-détection
