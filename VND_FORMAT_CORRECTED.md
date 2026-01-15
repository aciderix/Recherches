# Format VND - Analyse Corrigée

## ⚠️ Correction importante

L'analyse automatique initiale a mal interprété la structure. Voici la **vraie** structure après analyse manuelle.

---

## 📐 Structure Réelle du Fichier

```
┌─────────────────────────────────────────┐
│ ZONE 1: HEADER                          │
│ 0x0000 - 0x0086 (134 bytes)             │
├─────────────────────────────────────────┤
│ ZONE 2: TABLE DE VARIABLES              │
│ 0x0086 - 0x1154 (3,278 bytes)           │
│ 281 variables                           │
├─────────────────────────────────────────┤
│ ZONE 3: PADDING                         │
│ 0x1154 - 0x115C (8 bytes nulls)         │
├─────────────────────────────────────────┤
│ ZONE 4: DONNÉES DE SCÈNE                │
│ 0x115C - EOF                            │
│ Entrées de scène variables              │
└─────────────────────────────────────────┘
```

---

## 🔍 Zone 1: Header (0x0000 - 0x0086)

### Structure exacte:

```c
struct VNDHeader {
    // Magic
    uint32_t magic;              // 0x00: 0x3A010100
    uint8_t  reserved;           // 0x04: 0x00

    // Strings avec format [uint32 len][ASCII string]
    // (voir détails ci-dessous)

    // Après les strings:
    uint64_t reserved2;          // 0x46: 00 00 00 00 00 00 00 00

    // Paramètres graphiques
    uint32_t width;              // 0x4E: 640
    uint32_t height;             // 0x52: 480
    uint32_t bits_per_pixel;     // 0x56: 16
    uint32_t unknown1;           // 0x5A: 1
    uint32_t unknown2;           // 0x5E: 1
    uint32_t unknown3;           // 0x62: 31
    uint32_t unknown4;           // 0x66: 0

    // DLL path
    uint32_t dll_path_len;       // 0x6A: 24
    char     dll_path[24];       // 0x6E: "..\VnStudio\vnresmod.dll"
};
```

### Strings du header:

| Offset | Length | Contenu            | Description        |
|--------|--------|--------------------|--------------------|
| 0x05   | 6      | "VNFILE"           | Signature du format|
| 0x0F   | 4      | "2.13"             | Version (partielle)|
| 0x17   | (pad)  | "6\0\0\0"          | Suite version      |
| 0x1B   | 7      | "Europeo"          | Région             |
| 0x26   | 16     | "Sopra Multimedia" | Éditeur            |
| 0x3A   | 8      | "5D51F233"         | ID projet          |

---

## 📋 Zone 2: Table de Variables (0x0086 - 0x1154)

### Format:

```
0x0086: uint32 = 280 (0x118) - Taille partielle de la section

Puis pour chaque variable:
[uint32 length][ASCII name][uint32 padding=0x00000000]
```

### Exemples de variables:

```
SACADOS, JEU, BIDON, MILLEEURO, CALC, TELEPHONE, ACTIVE, FRANCS,
DELPHITEST1, DELPHITEST2, CPAYS, CMENU1, CMENU2, CMENU3,
COMPTEUR1, COMPTEUR2, COMPTEUR3, RAQUETTE, REPONSEM, AFFICHEM,
PIECE, DICO, BEETHOVEN, PHOTO, SCOTCH, QUESTION, REPONSE,
... (281 variables au total)
```

**Interprétation**: Ce sont des **flags/variables du moteur de jeu** utilisées pour:
- Compteurs de score
- États du jeu
- Flags de progression
- Valeurs temporaires

---

## 🎬 Zone 4: Données de Scène (0x115C - EOF)

### ⚠️ Structure COMPLEXE et VARIABLE

**Erreur de l'analyse initiale**: Ce n'est PAS un format bloc uniforme `[separator][length][type][payload]`.

**Vraie structure**: Séquence d'entrées de scène de types et tailles variables.

### Marqueur d'entrée:

Chaque entrée commence par: `01 00 00 00`

Mais ensuite, **la structure varie** selon le type d'entrée.

---

## 🎭 Types d'Entrées Identifiées

### Type 1: Entrée Vidéo/Image

**Exemple** (0x115C):
```
01 00 00 00          → Marqueur
00 00 00 00          → Type ou ID
00 00 00 00          → Flags?
08 00 00 00          → Paramètre 1
09 00 00 00          → Paramètre 2
"music.wav"          → Fichier audio
...
"euroland\face.bmp"  → Fichier image
```

**Contenu**: Chemin de fichier (BMP, AVI) + paramètres d'affichage

---

### Type 2: Entrée Texte

**Exemple** (0x11DE):
```
01 00 00 00                    → Marqueur
09 00 00 00                    → Longueur texte?
18 00 00 00                    → 24 (taille police?)
"euroland\bibliobis.avi 1"     → Fond vidéo
"18 0 #000000 Comic sans MS"   → Format texte:
                                  • 18 = taille
                                  • 0 = style?
                                  • #000000 = couleur (noir)
                                  • Police
"57 60 125 365 0 La biblioth..." → Position + texte:
                                  • 57, 60 = X, Y
                                  • 125, 365 = largeur, hauteur?
                                  • Texte: "La biblioth..."
```

**Contenu**: Paramètres de texte (police, couleur, position) + contenu

---

### Type 3: Entrée Données Numériques

**Exemple** (0x1631, 0x1639):
```
01 00 00 00          → Marqueur
06 00 00 00          → 6
01 00 00 00          → 1
33 69 00 00          → 26931 (ID ressource? coordonnée?)
00 0d 00 00          → 3328
...
```

**Contenu**: Suite de valeurs uint32

**Interprétation possible**:
- Coordonnées de zones cliquables
- IDs de ressources
- Données de collision
- Paramètres de mini-jeux

---

## ❌ Erreurs de l'Analyse Initiale

### 1. Mauvaise interprétation des "blocs"

**Pensé**: Format uniforme `[01][uint32 length][uint32 type][payload]`

**Réalité**: Séquence d'entrées avec structures variables selon le contexte

### 2. "Tailles énormes"

**Pensé**: `length=26931` → payload de 26931 bytes

**Réalité**: 26931 est une **valeur de donnée** (coordonnée? ID?), pas une taille

### 3. Chevauchements

**Problème détecté**: Les "blocs" se chevauchaient

**Cause**: Mauvaise interprétation de la structure

---

## ✅ Structure Correcte

### Format variable par contexte:

```
Entrée Vidéo:
  [01 00 00 00][params][chemin.avi]

Entrée Texte:
  [01 00 00 00][longueur][taille_police]
  [chemin_fond][format_texte][position + texte]

Entrée Données:
  [01 00 00 00][valeur1][valeur2]...[valeurN]
```

### Pas de format fixe!

La structure **change dynamiquement** selon:
- Le type de commande de scène
- Le contexte (affichage, logique, ressources)
- Les paramètres spécifiques à chaque entrée

---

## 🔧 Implications pour le Désassembleur

### Approche nécessaire:

1. **Parser contexte-aware**:
   - Détecter le type d'entrée par pattern matching
   - Parser selon le type détecté
   - Pas de structure fixe possible

2. **Heuristiques**:
   - Strings → chemins de fichiers
   - "#RRGGBB" → couleurs
   - "Comic sans MS" → polices
   - Petits entiers (< 1000) → paramètres
   - Gros entiers → coordonnées/IDs

3. **État interne**:
   - Le parser doit maintenir un état
   - Contexte de la scène courante
   - Type d'entrée en cours

---

## 🎯 Prochaines Étapes

### Pour créer un désassembleur fonctionnel:

1. **Identifier tous les types d'entrées**
   - Cataloguer les patterns
   - Documenter chaque type
   - Créer des parsers spécialisés

2. **Extraire les ressources**
   - Lister tous les chemins de fichiers
   - Extraire les textes
   - Documenter les paramètres

3. **Comprendre la logique**
   - Ordre des entrées = ordre d'exécution?
   - Relations entre entrées
   - Conditions et branchements

4. **Reverse engineer le runtime**
   - Analyser `vnresmod.dll`
   - Comprendre l'interpréteur
   - Documenter les commandes

---

## 📚 Outils Disponibles

### Scripts Python créés:

1. **analyze_vnd.py** - Analyse automatique (limitée)
2. **analyze_vnd_manual.py** - Analyse manuelle (correcte)
3. **parse_vnd_blocks.py** - Parser de blocs (incorrect)
4. **extract_vnd_blocks.py** - Extracteur (limité)

### Outils système:

- **xxd** - Inspection hex manuelle ✓ (recommandé)
- **hexedit** - Édition interactive ✓ (recommandé)
- **Ghidra** - Analyse du DLL ✓ (prochain step)
- **radare2** - Analyse binaire ✓

---

## 🧠 Leçons Apprises

### Erreurs à éviter:

1. ❌ Ne pas assumer un format uniforme
2. ❌ Ne pas parser aveuglément sans regarder manuellement
3. ❌ Ne pas ignorer les anomalies (chevauchements, tailles énormes)

### Bonnes pratiques:

1. ✅ Toujours vérifier manuellement avec xxd
2. ✅ Analyser plusieurs exemples avant de généraliser
3. ✅ Suivre les anomalies jusqu'à les comprendre
4. ✅ Parser contexte-aware pour formats variables

---

## 📊 Statistiques Finales

- **Fichier**: couleurs1.vnd (76,174 bytes)
- **Header**: 134 bytes
- **Variables**: 281 entrées, 3,278 bytes
- **Données scène**: ~72,500 bytes
- **Entrées détectées**: 800+ (non toutes parsées correctement encore)

---

**Status**: ⚠️ Partiellement compris
**Prochaine étape**: Reverse engineer vnresmod.dll avec Ghidra
**Difficulté**: Élevée (format variable, contexte-dépendant)

---

**Date**: 2026-01-15
**Auteur**: Analyse manuelle corrigée
**Outils**: xxd, hexedit, Python, observation directe
