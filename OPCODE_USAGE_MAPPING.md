# Mapping Opcodes → Usage dans couleurs1.vnd

## Vue d'Ensemble

Analyse des 108 séquences opcode extraites de `couleurs1.vnd` (75KB).

## Distribution des Opcodes

| Opcode | Index | Handler | Occurrences | % |
|--------|-------|---------|-------------|---|
| **'i'** | 9 | Images/INDEX | 46 | 42.6% |
| **'d'** | 4 | DIRECT suffix | 35 | 32.4% |
| **'h'** | 8 | Tooltip | 10 | 9.3% |
| **'j'** | 10 | Bitmaps | 8 | 7.4% |
| **'f'** | 6 | Navigation | 3 | 2.8% |
| **'l'** | 12 | MIDI Music | 3 | 2.8% |
| **'k'** | 11 | Audio WAV | 1 | 0.9% |
| **'e'** | 5 | ? | 1 | 0.9% |
| **'a'** | 1 | ? | 1 | 0.9% |
| **Total** | | | 108 | 100% |

## Analyse par Opcode

### Opcode 'i' (INDEX Navigation / Images) - 46 occurrences

**Usage dual**:
1. **Suffixe INDEX** pour navigation: `destination = INDEX_ID + n`
2. **Handler Images** (standalone): Chargement AVI/BMP

**Exemples**:
```
1i   @ 0x001579  Context: "suede = 1  then dec_var suede 1i"
3i   @ 0x00163D  Context: "land\bankbis.avi 1............3i"
5i   @ 0x00172E  Context: "roland\home2.avi 1............5i"
6i   @ 0x0017F1  Context: "land\profbis.avi 1............6i"
39i  @ 0x0019E3  Context: ".avi 1...$..................39i"
54i  @ 0x003C3E  Context: "rj ..\couleurs1\couleurs1.vnp 54i"
318i @ 0x00650A  Context: "yavi sirene.avi 2 118 214 510 318i"
```

**Patterns**:
- Après `dec_var variable`: Probablement suffixe navigation
- Après chemin `.avi` ou `.vnp`: Chargement vidéo/projet
- Après coordonnées: Positionnement image

---

### Opcode 'd' (DIRECT Navigation) - 35 occurrences

**Usage**: Suffixe DIRECT pour navigation: `destination = n` (absolu)

**Exemples**:
```
177d @ 0x005CB0  Context: "oland\rollover\sac2.bmp  0 52 177d"
54d  @ 0x0068B1  Context: "rj ..\couleurs1\couleurs1.vnp 54d"
69d  @ 0x0069C1  Context: "..\angl\angleterre.vnp 69d"
6d   @ 0x006A6D  Context: "bruit\boing.wav 1..............6d"
63d  @ 0x006AF3  Context: "rollover\fr.bmp 0 27 63d"
13d  @ 0x006BEF  Context: "..\espa\espa.vnp 13d"
33d  @ 0x006CAF  Context: "..\ecosse\ecosse.vnp 33d"
12d  @ 0x006D45  Context: "..\portu\portu.vnp 12d"
19d  @ 0x006DDB  Context: "..\belge\belge.vnp 19d"
11d  @ 0x006E73  Context: "..\finlan\finlan.vnp 11d"
14d  @ 0x006F4B  Context: "..\irland\irland.vnp 14d"
12d  @ 0x006FEE  Context: "..\autr\autr.vnp 12d"
10d  @ 0x0070AB  Context: "..\danem\danem.vnp 10d"
12d  @ 0x007141  Context: "..\suede\suede.vnp 12d"
28d  @ 0x007209  Context: "..\italie\italie.vnp 28d"
10d  @ 0x0072C5  Context: "..\holl\holl.vnp 10d"
7d   @ 0x007363  Context: "..\grece\grece.vnp 7d"
15d  @ 0x007CCA  Context: "1\couleurs1.vnp 54 else scene 15d"
87d  @ 0x0084F5  Context: "rollover\rotvoi.bmp 0 100 87d"
3d   @ 0x0092A6  Context: "..\frontal\start.vnp 3d"
```

**Pattern clair**:
- Toujours après un chemin `.vnp` (projet) ou `.bmp`
- Navigation vers scène spécifique dans un pays/projet
- Exemples: "angleterre.vnp 69d" → va à scène 69 d'Angleterre

---

### Opcode 'h' (Tooltip) - 10 occurrences

**Usage**: Affichage bulle d'aide/info-bulle

**Exemples**:
```
54h @ 0x001B6C  Context: "rj ..\couleurs1\couleurs1.vnp 54h"
54h @ 0x001F5D  Context: "rj ..\couleurs1\couleurs1.vnp 54h"
7h  @ 0x0065B7  Context: "SORTIE...$..................7h"
54h @ 0x00B377  Context: "rj ..\couleurs1\couleurs1.vnp 54h"
```

**Pattern**:
- Souvent après `runprj couleurs1.vnp` avec numéro de scène
- Exemple: "54h" = charge scène 54, puis affiche tooltip

---

### Opcode 'j' (Bitmaps) - 8 occurrences

**Usage**: Gestion technique bitmaps (transparence, palettes)

**Exemples**:
```
22j @ 0x001D06  Context: "outeille d'encre noire..........22j"
59j @ 0x002C99  Context: "runprj ..\angl\angleterre.vnp 59j"
27j @ 0x002E42  Context: "n runprj ..\france\france.vnp 27j"
15j @ 0x003897  Context: "n runprj ..\france\france.vnp 15j"
5j  @ 0x003A2E  Context: "hen runprj ..\allem\allem.vnp 5j"
57j @ 0x003AE5  Context: "runprj ..\angl\angleterre.vnp 57j"
51j @ 0x003EBA  Context: "n de choses dessus..........51j"
```

**Pattern**:
- Après description d'objet ("bouteille d'encre")
- Ou après `runprj` vers pays → charge bitmap spécifique
- Exemple: "angleterre.vnp 59j" = charge projet + bitmap 59

---

### Opcode 'f' (Navigation) - 3 occurrences

**Usage**: Changement de scène (handler principal navigation)

**Exemples**:
```
54f @ 0x002551  Context: "rj ..\couleurs1\couleurs1.vnp 54f"
54f @ 0x004B19  Context: "rj ..\couleurs1\couleurs1.vnp 54f"
54f @ 0x00533F  Context: "rj ..\couleurs1\couleurs1.vnp 54f"
```

**Pattern**:
- Toujours "54f" après `runprj couleurs1.vnp`
- Navigation vers scène 54 du projet couleurs1

---

### Opcode 'l' (MIDI Music) - 3 occurrences

**Usage**: Lecture musique MIDI

**Exemples**:
```
16l @ 0x0027CC  Context: "telephone = 0 then scene 16l"
2l  @ 0x003DCC  Context: " 420 400.........music.wav 2l"
6l  @ 0x004D6E  Context: " 771 286.........music.wav 6l"
```

**Pattern**:
- Après condition + `scene` : "scene 16l" = va scène 16 + joue MIDI
- Ou après coordonnées + `music.wav`

---

### Opcode 'k' (Audio WAV) - 1 occurrence

**Usage**: Lecture audio WAV

**Exemple**:
```
35k @ 0x005840  Context: "bonus2 = 1 then scene 35k"
```

**Pattern**:
- Condition "bonus2 = 1 then scene 35k" = si bonus actif, va scène 35 + joue son

---

### Opcodes Rares - 1 occurrence chaque

**'e' (5)**:
```
1e @ 0x003D0A  Context: ".Ý..,................1e"
```

**'a' (1)**:
```
1a @ 0x004D40  Context: "..	..$...euroland\pro1a.avi 1 659 166 771 286"
```

Probablement:
- 'e': Opcode 5 (État du jeu?)
- 'a': Dans nom de fichier "pro1a.avi" (faux positif?)

---

## Commandes Textuelles Associées

Les opcodes apparaissent dans le contexte de commandes scriptes:

### Conditions
```
if variable = valeur then opcode
variable = valeur then dec_var variable opcode
bonus2 = 1 then scene opcode
```

### Navigation
```
runprj chemin.vnp opcode
scene nombre+opcode
```

### Médias
```
chemin.avi coordonnées opcode
music.wav coordonnées opcode
chemin.bmp coordonnées opcode
```

---

## Mapping Handlers Analysés → Usage Réel

| Handler | Adresse | Usage dans couleurs1.vnd |
|---------|---------|--------------------------|
| **'f'** (6) @ 0x0043198B | Navigation | 3× - Navigation vers scène 54 |
| **'h'** (8) @ 0x00431B70 | Tooltip | 10× - Bulles d'aide après runprj |
| **'i'** (9) @ 0x004321B6 | Images/INDEX | 46× - Chargement vidéos + navigation INDEX |
| **'j'** (10) @ 0x00432201 | Bitmaps | 8× - Objets (bouteille, sac) + bitmaps pays |
| **'k'** (11) @ 0x0043224C | Audio WAV | 1× - Son bonus |
| **'l'** (12) @ 0x00432297 | MIDI | 3× - Musique de fond scènes |
| **'u'** (21) @ 0x00431A7C | Logic if/then | 0× (conditions parsées autrement?) |

**Note**: Handler 'u' (logic) n'apparaît pas directement car les conditions `if ... then` sont probablement gérées par le dispatcher avant d'atteindre les handlers d'action.

---

## Conclusions

1. **'i' et 'd' dominent** (78% des opcodes):
   - Usage dual navigation (suffixes) + handlers
   - 'i' = INDEX relatif (INDEX_ID+n)
   - 'd' = DIRECT absolu (scène n)

2. **Pattern géographique fort**:
   - Navigation entre pays européens: `pays.vnp XXd`
   - Chaque pays a un numéro de scène spécifique
   - Exemples: angleterre=69, espagne=13, ecosse=33

3. **Média handlers secondaires**:
   - 'j' pour objets (bouteille, sac)
   - 'l' pour ambiance musicale
   - 'k' rare (1 bonus audio)

4. **Tooltip omniprésent après runprj**:
   - Pattern: `runprj projet.vnp 54h`
   - Charge projet, puis affiche aide

5. **Type 0 contient TOUT**:
   - Le grand record Type 0 de couleurs1.vnd contient:
     - Métadonnées scène (audio, images de fond)
     - Scripts conditionnels
     - Commandes navigation
     - Tous les opcodes d'exécution

---

## Prochaines Analyses

1. ✅ Opcodes extraits et mappés (108 séquences)
2. ⏳ Comprendre structure exacte Type 0 (métadonnées + scripts)
3. ⏳ Analyser handlers restants (a, e, et 35 autres)
4. ⏳ Parser conditions `if ... then` (interaction avec handler 'u')
5. ⏳ Dumper table variables @ 0x44ECCE pour voir INDEX_ID

---

**Document**: OPCODE_USAGE_MAPPING.md
**Source**: couleurs1.vnd (108 opcodes via extract_opcodes_from_vnd_v2.py)
**Date**: 2026-01-16
