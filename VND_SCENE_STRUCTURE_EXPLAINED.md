# Structure des Scènes VND - Explication Complète

**Date**: 2026-01-17
**Contexte**: Réponse aux questions sur Type 0, hotspots, et navigation

---

## 🎯 Question Centrale

**Comment un fichier VND organise une scène interactive?**

Un fichier VND n'est PAS juste une liste plate de records. C'est une **hiérarchie** où chaque scène (Type 0) contient ou référence d'autres éléments.

---

## 📊 Structure Hiérarchique

### Niveau 1: Fichier VND

```
┌─────────────────────────────────────┐
│ VNFILE Header                       │
│ ├─ Signature: "VNFILE"             │
│ ├─ Dimensions écran                │
│ └─ Checksum                        │
├─────────────────────────────────────┤
│ Table Variables (140+)              │
│ ├─ SACADOS = 50331648              │
│ ├─ JEU = ...                       │
│ └─ CALC = ...                      │
├─────────────────────────────────────┤
│ Records (séquence)                  │
│ ├─ Type 0 (Scène #1)               │
│ ├─ Type 2 (Hotspot)                │
│ ├─ Type 1 (Condition)              │
│ ├─ Type 0 (Scène #2)               │
│ └─ ...                             │
└─────────────────────────────────────┘
```

### Niveau 2: Une Scène (Type 0)

**Type 0 = MÉTADONNÉES DE SCÈNE**

Contenu typique d'un Type 0:

1. **Fichiers à charger**:
   - DLL à initialiser (`..\VnStudio\vnresmod.dll`)
   - Images de fond (`.bmp`)
   - Musique de fond (`.wav`)
   - Vidéos (`.avi`)

2. **Configuration**:
   - Variables utilisées dans cette scène
   - Polices et formatage texte
   - Coordonnées de zones de texte

3. **Référence implicite aux records suivants**:
   - Les records qui suivent un Type 0 appartiennent à cette scène
   - Jusqu'au prochain Type 0 = nouvelle scène

---

## 🖼️ Exemple Concret: Scène #2 de couleurs1.vnd

### Structure trouvée:

```
@ 0x0000115C: Type 0 (Scène #2)
  ├─ music.wav              ← Musique de fond
  ├─ euroland\face.bmp      ← Image de fond
  │
  └─ Records enfants (juste après):
      ├─ Type 24 @ 0x000011DE
      ├─ Type 1  @ 0x00001202  ← Conditions
      ├─ Type 22 @ 0x00001631
      ├─ Type 1  @ 0x00001631  ← Autres conditions
      └─ Type 20 @ 0x00001702
```

**Interprétation**:
- Le Type 0 dit: "Charge music.wav en boucle + affiche face.bmp"
- Les Type 1 suivants définissent les **conditions de navigation** (si score < 0 alors...)
- Les autres types définissent **hotspots** et **actions**

---

## 🔍 Type 2: Hotspots (Points Cliquables)

### Analyse Binaire d'un Type 2 Réel

**Dump brut du premier Type 2 @ 0x000019D7**:

```
Offset   Hex                                           ASCII
------   -------------------------------------------   ----------------
+0000:   33 39 69 00 00 00                             "39i\0\0\0"
+0006:   08 00 00 00                                   8
+0010:   15 01 00 00                                   277 (0x115)
+0014:   3c 01 00 00                                   316 (0x13C)
+0018:   e8 00 00 00                                   232 (0xE8)
+0022:   3c 01 00 00                                   316 (0x13C)
+0026:   d5 00 00 00                                   213 (0xD5)
+0030:   30 01 00 00                                   304 (0x130)
+0034:   e4 00 00 00                                   228 (0xE4)
+0038:   21 01 00 00                                   289 (0x121)
+0042:   e5 00 00 00                                   229 (0xE5)
+0046:   00 00 00 00                                   0
+0050:   08 01 00 00                                   264 (0x108)
...
+0082:   4c 65 20 62 75 72 65 61 75 20 64 75 20 62    "Le bureau du b"
+0096:   61 6e 71 75 69 65 72                          "anquier"
```

### Structure Identifiée:

```
Type 2 Format:
┌──────────────────────────────────────────┐
│ OPCODE (null-terminated string)         │  "39i\0"
├──────────────────────────────────────────┤
│ Nombre de points (uint32)               │  8 points
├──────────────────────────────────────────┤
│ Points (paires x,y) × N                  │
│   Point 1: x=277, y=316                  │
│   Point 2: x=232, y=316                  │
│   Point 3: x=213, y=304                  │
│   Point 4: x=228, y=289                  │
│   Point 5: x=229, y=0                    │
│   Point 6: x=264, y=0                    │
│   Point 7: x=264, y=289                  │
│   Point 8: x=280, y=303                  │
├──────────────────────────────────────────┤
│ Padding (00 00 00 00)                    │
├──────────────────────────────────────────┤
│ Longueur texte (uint32)                  │  21 bytes
├──────────────────────────────────────────┤
│ Texte (ASCII null-terminated)            │  "Le bureau du banquier"
└──────────────────────────────────────────┘
```

**C'est un POLYGONE, pas un rectangle!**

---

## 🎮 Navigation: Comment Ça Marche?

### 1. Moteur de Jeu Charge la Scène

1. Lit Type 0 → charge music.wav + face.bmp
2. Affiche l'image de fond
3. Lance la musique en boucle

### 2. Moteur Construit les Zones Cliquables

1. Lit tous les Type 2 qui suivent
2. Pour chaque Type 2:
   - Extrait l'opcode (ex: "39i")
   - Extrait les points du polygone
   - Crée une zone cliquable avec ces coordonnées
   - Associe le texte tooltip "Le bureau du banquier"

### 3. Joueur Clique sur l'Écran

1. **Détection de collision**:
   ```python
   for hotspot in hotspots:
       if point_in_polygon(mouse_x, mouse_y, hotspot.points):
           # Clic détecté!
           execute_opcode(hotspot.opcode)  # "39i"
   ```

2. **Exécution de l'opcode**:
   - "39i" = Opcode 39 + suffix 'i' (INDEX)
   - Le moteur appelle `handler 39` avec INDEX
   - Handler 39 → Pre-processor → Handler 'i' (Images)
   - Handler 'i' charge la scène INDEX #39

### 4. Navigation Géographique

**Exemple d'opcode de navigation**:

- `13i` → Scène INDEX 13 (peut-être "Espagne")
- `54d` → Scène DIRECT 54 (condition spéciale)
- `7h` → Tooltip/info #7

**Fichiers VND par pays** (découverts):
```
espa.vnp       → Espagne
angl.vnp       → Angleterre
grece.vnp      → Grèce
allem.vnp      → Allemagne
france.vnp     → France
italie.vnp     → Italie
```

**Navigation entre pays**:
- Un Type 2 dans `couleurs1.vnd` (menu principal)
- Opcode: `..\espa\espa.vnp 13`
- Clic → Charge `espa.vnp` scène 13

---

## 📏 Extraction des Coordonnées

### Format Général Type 2

```c
struct Type2_Hotspot {
    char opcode[variable];     // Null-terminated: "39i", "13i", etc.
    uint8_t padding[align_4];  // Alignement sur 4 bytes
    uint32_t num_points;       // Nombre de points
    struct {
        uint32_t x;
        uint32_t y;
    } points[num_points];      // Coordonnées des points
    uint32_t padding2;         // 00 00 00 00
    uint32_t text_length;      // Longueur du texte
    char text[text_length];    // Texte tooltip
};
```

### Algorithme d'Extraction

```python
def parse_type2_hotspot(data):
    pos = 0

    # 1. Opcode
    opcode_end = data.find(b'\x00')
    opcode = data[:opcode_end].decode('ascii')
    pos = opcode_end + 1

    # 2. Alignement sur 4 bytes
    while pos % 4 != 0:
        pos += 1

    # 3. Nombre de points
    num_points = struct.unpack('<I', data[pos:pos+4])[0]
    pos += 4

    # 4. Points (x, y)
    points = []
    for i in range(num_points):
        x = struct.unpack('<I', data[pos:pos+4])[0]
        y = struct.unpack('<I', data[pos+4:pos+8])[0]
        points.append((x, y))
        pos += 8

    # 5. Skip padding
    pos += 4

    # 6. Texte
    text_len = struct.unpack('<I', data[pos:pos+4])[0]
    pos += 4
    text = data[pos:pos+text_len].decode('ascii', errors='ignore')

    return {
        'opcode': opcode,
        'points': points,
        'text': text
    }
```

---

## 🧩 Réponses aux Questions Précises

### Q: "Type 0 je comprends pas"

**Réponse**: Type 0 n'est PAS une simple liste de fichiers.

**C'est une SCÈNE COMPLÈTE** qui définit:
1. **Environnement**: Background image, musique, vidéos
2. **Variables actives**: Quelles variables du jeu sont utilisées ici
3. **Formatage UI**: Polices, couleurs, zones de texte
4. **Contexte**: DLL à charger, ressources nécessaires

**Analogie**: Type 0 = Le "fichier de niveau" dans un jeu vidéo
- Super Mario: chaque niveau a son fond, sa musique, ses ennemis
- VND: chaque scène Type 0 a son fond, sa musique, ses hotspots

### Q: "vnresmod.dll, SACADOS, JEU - des variables techniques?"

**Réponse**:

1. **vnresmod.dll**: DLL externe pour ressources/modules
   - Chargée au démarrage de la scène
   - Fournit probablement des fonctions helper

2. **SACADOS, JEU, BIDON, etc.**: VARIABLES DE JEU
   - Définies dans la table de variables (début du fichier)
   - Valeurs initiales définies (ex: SACADOS = 50331648)
   - Utilisées dans les conditions if/then

**Exemple d'utilisation**:
```
Type 1: if SACADOS = 0 then playtext "Il te faut un sac à dos"
Type 1: if SACADOS = 1 then addbmp sacados.bmp
```

### Q: "face.bmp = Type 0?"

**Oui ET non**:
- `face.bmp` est **mentionné DANS** le Type 0
- C'est une **référence** à un fichier externe
- Le moteur lit Type 0 → voit "euroland\face.bmp" → charge ce fichier

**Pas de données d'image dans le VND!**
- Les fichiers VND ne contiennent QUE la logique/structure
- Les ressources (BMP, WAV, AVI) sont externes

### Q: "Comment sont définies la navigation?"

**Réponse**: Via les **opcodes dans les hotspots**

**Mécanisme complet**:

1. **Type 2 définit zone cliquable**:
   - Polygone avec coordonnées
   - Opcode associé: "13i"

2. **Joueur clique**:
   - Moteur détecte collision avec polygone
   - Récupère opcode "13i"

3. **Exécution**:
   - Parse "13i" → handler 13, suffix 'i'
   - Appelle `handler[13](suffix='i', index=13)`
   - Handler 13 → Pre-processor → Handler 'i'
   - Handler 'i' charge scène INDEX #13

4. **Navigation géographique**:
   - Certains opcodes référencent d'autres fichiers `.vnp`
   - Ex: `..\espa\espa.vnp 13d`
   - Charge fichier externe, scène spécifique

### Q: "Hotspot rectangle, polygone, image - différences?"

**Réponse**:

| Type | Format | Coordonnées | Utilisation |
|------|--------|-------------|-------------|
| **Type 2** | Polygone | N points (x,y) | Zones cliquables irrégulières |
| **Rectangle** | Probablement un Type 2 avec 4 points | 4 coins | Boutons rectangulaires |
| **Image hotspot** | Type inconnu (Type 10?) | Position + taille image | Images cliquables |

**Tous utilisent le même système**: Coordonnées + Opcode

### Q: "Est-ce que tu extrais bien les coordonnées de polygones?"

**Actuellement**: **NON, pas complètement**

**Problème identifié**:
- Mon parser V2 n'extrait pas correctement les points du polygone
- J'ai identifié la structure mais pas encore codé le parser final

**Solution nécessaire**:
- Créer `vnd_decompiler_v3.py` avec extraction complète des hotspots
- Parser Type 2 selon le format documenté ci-dessus
- Afficher: `Hotspot "39i": Polygone [(277,316), (232,316), ...] → "Le bureau du banquier"`

---

## 🛠️ Prochaines Étapes

### Pour Décompilation Complète

1. **Parser Type 2 correctement**:
   - Implémenter l'algorithme d'extraction ci-dessus
   - Vérifier sur tous les Type 2 de couleurs1.vnd

2. **Créer visualisation**:
   - Générer image avec polygones dessinés
   - Overlay sur l'image de fond
   - Voir les zones cliquables

3. **Décompilateur V3**:
   - Améliorer extraction hotspots
   - Afficher hiérarchie scène → hotspots → actions
   - Format pseudo-code lisible:
   ```
   SCÈNE 2: Menu Principal
     Background: euroland/face.bmp
     Music: music.wav

     HOTSPOT "Le bureau du banquier" (opcode 39i)
       Polygone: [(277,316), (232,316), (213,304), ...]
       Action: → Charge scène INDEX 39
   ```

---

## 📝 Conclusion

**Format VND = Hiérarchie de Scènes Interactives**

```
Fichier VND
  └─ Scène (Type 0)
      ├─ Ressources (images, sons)
      ├─ Variables actives
      └─ Enfants (records suivants)
          ├─ Hotspots (Type 2) → Navigation
          ├─ Conditions (Type 1) → Logique
          └─ Actions (autres types) → Effets
```

**Navigation** = Hotspots polygonaux avec opcodes

**Coordonnées** = Identifiées dans structure binaire Type 2

**Manquant** = Parser complet pour extraction automatique

---

**Maintenu par**: Claude Code Analysis
**Dernière mise à jour**: 2026-01-17
