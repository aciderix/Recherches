# VND Scripting Language - Documentation

## 📚 Vue d'ensemble

Le format VND contient un **langage de script intégré** utilisé pour contrôler le flux du Visual Novel, gérer les ressources multimédia, et implémenter la logique de jeu.

Cette documentation est basée sur l'analyse de `couleurs1.vnd`.

---

## 🎮 Variables du Jeu

### Variables identifiées (281 au total)

Le fichier contient 281 variables utilisées pour gérer l'état du jeu:

```
SACADOS, JEU, BIDON, MILLEEURO, CALC, TELEPHONE, ACTIVE, FRANCS,
DELPHITEST1, DELPHITEST2, CPAYS, CMENU1, CMENU2, CMENU3,
COMPTEUR1, COMPTEUR2, COMPTEUR3, RAQUETTE, REPONSEM, AFFICHEM,
PIECE, DICO, BEETHOVEN, PHOTO, SCOTCH, QUESTION, REPONSE,
... (254 autres)
```

### Variables utilisées dans le script

```
milleeuro    - Compteur d'euros (jeu éducatif sur l'Euro)
bonus3       - Flag de bonus
telephone    - État du téléphone (0/1)
score        - Score du joueur
```

---

## 📝 Syntaxe du Langage

### Structure générale

```
<condition> then <action> [else <action>]
```

### Opérateurs de comparaison

```
=          Égal
<          Inférieur
>          Supérieur
>=         Supérieur ou égal
<=         Inférieur ou égal (probable)
!=         Différent (probable)
```

---

## 🎬 Commandes Multimédia

### 1. playavi - Jouer une vidéo

**Syntaxe**:
```
playavi <fichier> <loop> [x y largeur hauteur]
```

**Paramètres**:
- `fichier`: Chemin du fichier .avi
- `loop`: 1 = boucle, 0 = une fois
- `x, y`: Position (optionnel)
- `largeur, hauteur`: Dimensions (optionnel)

**Exemples**:
```
playavi euroland\bibliobis.avi 1
playavi euroland\banq41.avi 1 168 122 344 374
milleeuro = 0 then playavi euroland\banq3.avi 1 168 122 344 374
```

---

### 2. playwav - Jouer un son

**Syntaxe**:
```
playwav <fichier> <loop>
```

**Paramètres**:
- `fichier`: Chemin du fichier .wav
- `loop`: 1 = boucle, 0 = une fois

**Exemples**:
```
playwav music.wav 1
playwav bruit\boing.wav 1
bonus3 = 0 then playwav bruit\boing.wav 1
```

---

### 3. addbmp - Ajouter une image

**Syntaxe**:
```
addbmp <nom> <fichier> <layer> <x> <y>
```

**Paramètres**:
- `nom`: Identifiant de l'image (pour manipulation ultérieure)
- `fichier`: Chemin du fichier .bmp
- `layer`: Couche d'affichage (z-order)
- `x, y`: Position à l'écran

**Exemples**:
```
addbmp coffre euroland\rollover\coffre.bmp 0 0 203
addbmp tt euroland\rollover\maintel.bmp 0 732 240
telephone = 1 then addbmp tt euroland\rollover\maintel.bmp 0 732 240
```

---

### 4. delbmp - Supprimer une image

**Syntaxe**:
```
delbmp <nom>
```

**Paramètres**:
- `nom`: Identifiant de l'image à supprimer

**Exemples**:
```
delbmp coffre
milleeuro >= 1 then addbmp coffre euroland\rollover\coffre.bmp 0 0 203 else delbmp coffre
```

---

### 5. runprj - Exécuter un projet/scène

**Syntaxe**:
```
runprj <fichier_projet> <scène>
```

**Paramètres**:
- `fichier_projet`: Chemin du fichier .vnp (VN Project)
- `scène`: Numéro de la scène à charger

**Exemples**:
```
runprj ..\couleurs1\couleurs1.vnp 54
score < 0 then runprj ..\couleurs1\couleurs1.vnp 54
```

---

## 🎨 Affichage de Texte

### Format de texte

Les textes sont affichés avec les paramètres suivants:

**Structure**:
```
<taille> <style> <couleur> <police>
<x> <y> <largeur> <hauteur> <flags> <texte>
```

**Exemple**:
```
18 0 #000000 Comic sans MS
57 60 125 365 0 La bibliothèque
```

### Paramètres de texte

| Paramètre | Type | Description |
|-----------|------|-------------|
| Taille | int | Taille de police (18, 24, 32, etc.) |
| Style | int | 0 = normal, autres styles non identifiés |
| Couleur | hex | Format #RRGGBB (#000000, #ffffff) |
| Police | string | Nom de police ("Comic sans MS", etc.) |
| X, Y | int | Position du texte à l'écran |
| Largeur, Hauteur | int | Dimensions de la zone de texte |
| Flags | int | Drapeaux (0 par défaut) |
| Texte | string | Contenu du texte |

---

## 🔀 Logique Conditionnelle

### Structure if-then-else

**Syntaxe**:
```
<variable> <opérateur> <valeur> then <action> [else <action>]
```

### Exemples réels extraits

```
milleeuro = 0 then playavi euroland\banq41.avi 1 168 122 344 374
```
→ Si milleeuro vaut 0, jouer la vidéo banq41.avi

```
milleeuro >= 1 then addbmp coffre euroland\rollover\coffre.bmp 0 0 203 else delbmp coffre
```
→ Si milleeuro ≥ 1, afficher le coffre, sinon le supprimer

```
bonus3 = 0 then playwav bruit\boing.wav 1
```
→ Si bonus3 vaut 0, jouer le son boing.wav

```
telephone = 1 then addbmp tt euroland\rollover\maintel.bmp 0 732 240
```
→ Si telephone vaut 1, afficher l'image du téléphone

```
score < 0 then runprj ..\couleurs1\couleurs1.vnp 54
```
→ Si score < 0, charger la scène 54

---

## 📂 Structure des Ressources

### Chemins de fichiers

Tous les chemins sont relatifs au répertoire du projet:

```
euroland\
  ├─ face.bmp
  ├─ bibliobis.avi
  ├─ bankbis.avi
  ├─ home2.avi
  ├─ profbis.avi
  ├─ musee.avi
  ├─ fontaine.avi
  ├─ bureaubanquier.bmp
  ├─ banque.bmp
  ├─ banq2.avi
  ├─ banq3.avi
  ├─ banq41.avi
  ├─ biblio.bmp
  ├─ biblio1.avi
  └─ rollover\
      ├─ coffre.bmp
      └─ maintel.bmp

bruit\
  └─ boing.wav

music.wav (à la racine)
```

---

## 🎯 Entrées de Scène

### Types d'entrées identifiés

Le fichier VND contient trois types d'entrées:

#### 1. Entrée VIDEO (37 entrées)
- Chargement de ressources multimédia (.avi, .bmp, .wav)
- Paramètres d'affichage
- Commandes de lecture

#### 2. Entrée TEXT (62 entrées)
- Texte à afficher (dialogues, narration)
- Formatage (police, couleur, taille)
- Position et dimensions

#### 3. Entrée DATA (1 entrée)
- Valeurs numériques brutes
- Probablement des paramètres ou coordonnées

---

## 📊 Statistiques du Fichier Analysé

**Fichier**: `couleurs1.vnd` (76,174 bytes)

### Contenu:
- **Variables**: 281
- **Entrées de scène**: 100+ (limité dans l'analyse)
  - VIDEO: 37
  - TEXT: 62
  - DATA: 1

### Ressources multimédia:
- **Vidéos (.avi)**: 15+ fichiers
- **Images (.bmp)**: 10+ fichiers
- **Sons (.wav)**: 2+ fichiers

---

## 🔍 Exemples Complets

### Exemple 1: Gestion d'un objet conditionnel (coffre)

```
milleeuro >= 1 then addbmp coffre euroland\rollover\coffre.bmp 0 0 203 else delbmp coffre
```

**Logique**:
1. Si le joueur a au moins 1 euro
2. Afficher le coffre à la position (0, 203) sur la couche 0
3. Sinon, supprimer le coffre de l'écran

---

### Exemple 2: Animation conditionnelle

```
milleeuro = 0 then playavi euroland\banq41.avi 1 168 122 344 374
```

**Logique**:
1. Si le joueur a 0 euros
2. Jouer la vidéo banq41.avi en boucle
3. Dans la zone (168, 122) de dimensions 344×374

---

### Exemple 3: Texte avec formatage

```
Entrée TEXT:
  Fond: euroland\banque.bmp
  Format: 18 0 #000000 Comic sans MS
  Position: (160, 350) - 125×365
  Texte: Le banquier d'Euroland
```

**Résultat**:
- Afficher l'image de fond banque.bmp
- Texte en Comic Sans MS, taille 18, noir
- Positionné à (160, 350)
- Zone de texte: 125 pixels de large, 365 de haut

---

## 🧩 Commandes Non Documentées

Ces patterns ont été observés mais leur fonction exacte est incertaine:

```
<nombre1> <nombre2> ...
```
Exemple: `6 1 50`, `0 0 0 0`, `248 0 4 0 39 26`

**Hypothèses**:
- Coordonnées de zones cliquables
- Paramètres de mini-jeux
- Données de collision
- Configuration de l'interface

---

## 🎓 Contexte du Jeu

### Thème: Éducation sur l'Euro

Basé sur les noms de variables et textes extraits:

- **MILLEEURO**: Compteur d'argent
- **CPAYS**: Pays sélectionné
- **Textes**: "La bibliothèque", "Le banquier d'Euroland", "Le bureau du banquier"
- **Ressources**: Scènes de banque, bibliothèque, musée, fontaine

### Type de jeu:
Visual Novel / Jeu éducatif point-and-click sur l'économie européenne et l'Euro

---

## 🔧 Interpréteur

### DLL du runtime

```
..\VnStudio\vnresmod.dll
```

Cette DLL contient l'interpréteur qui:
1. Parse le fichier VND
2. Exécute les commandes de script
3. Gère l'affichage multimédia
4. Maintient l'état des variables

**Note**: Pour une compréhension complète du langage, l'analyse de cette DLL avec Ghidra serait nécessaire.

---

## 📚 Références

### Outils d'analyse créés:
- `vnd_disasm.py` - Désassembleur complet
- `analyze_vnd_manual.py` - Analyseur manuel
- `parse_vnd_blocks.py` - Parser de blocs
- `extract_vnd_blocks.py` - Extracteur

### Documentation:
- `VND_FORMAT_ANALYSIS.md` - Analyse initiale
- `VND_FORMAT_CORRECTED.md` - Corrections après analyse manuelle
- `VND_SCRIPTING_LANGUAGE.md` - Ce document

---

## ✅ Commandes Confirmées

| Commande | Fonction | Statut |
|----------|----------|--------|
| `playavi` | Jouer vidéo | ✅ Confirmé |
| `playwav` | Jouer audio | ✅ Confirmé |
| `addbmp` | Ajouter image | ✅ Confirmé |
| `delbmp` | Supprimer image | ✅ Confirmé |
| `runprj` | Charger scène | ✅ Confirmé |
| `if-then-else` | Logique conditionnelle | ✅ Confirmé |

---

## 🚧 À Confirmer

- Opérateurs `!=`, `<=` (non observés mais probables)
- Commandes de manipulation de variables (set, add, sub, etc.)
- Commandes de boucle (for, while?)
- Commandes d'input utilisateur
- Gestion des événements (onclick, onhover?)

---

**Date**: 2026-01-15
**Auteur**: Analyse par désassemblage de couleurs1.vnd
**Outils**: Python, xxd, analyse manuelle
**Status**: ✅ Langage partiellement documenté

---

## 🎯 Prochaine Étape

Pour compléter cette documentation:
1. **Analyser vnresmod.dll avec Ghidra**
2. Identifier toutes les commandes du langage
3. Documenter le cycle de vie de l'interpréteur
4. Comprendre le format exact des entrées DATA
5. Créer un assembleur VND complet
