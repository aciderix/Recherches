# VND Décompilateur - Documentation

**Date**: 2026-01-17
**Version finale**: V4

---

## 🎯 Problème Résolu

Le champ `LENGTH` dans les records VND **n'est pas fiable**, surtout pour le Type 0 (scènes):

- Record avec LENGTH=0, vraie taille=4520 bytes (**4520% d'erreur!**)
- Record avec LENGTH=3, vraie taille=886 bytes (**99% d'erreur!**)

**Source**: `VND_MASTER_REFERENCE.md` ligne 66-77

---

## ✅ Solution: Désassembleur V4

### Principe

**Lire jusqu'au prochain séparateur** `01 00 00 00` et **filtrer intelligemment** les caractères binaires.

### Fonctionnement

1. **Détection des séparateurs**: Cherche tous les `01 00 00 00` dans le fichier
2. **Lecture des données**: Lit du offset+12 jusqu'au prochain séparateur
3. **Filtrage binaire**:
   - Garde les caractères imprimables ASCII + accents français
   - Remplace les zones binaires par des espaces
   - S'arrête après 30 caractères binaires consécutifs (pour éviter les gros blocs)
4. **Détection de patterns**:
   - Fichiers: `.bmp`, `.wav`, `.avi`
   - Commandes: `runprj`, `playavi`, `addbmp`, etc.
   - Conditions: `var = val then action`
   - Polices: `SIZE STYLE #COLOR FONT`
   - Terminateurs: lettres isolées en fin de ligne (`i`, `d`, `h`, etc.)

### Exemple de Sortie

```
────────────────────────────────────────────────────────────────────────────────
SCÈNE #2 @ 0x0000115C
────────────────────────────────────────────────────────────────────────────────
🔊 Audio: music.wav
🖼️  Fond: euroland\face.bmp

euroland\bibliobis.avi 1

[HOTSPOT #1]
18 0 #000000 Comic sans MS
57 60 125 365 0 La bibliothèque
387 351 125 365 0 La banque
score < 0 then runprj ..\couleurs1\couleurs1.vnp 54
runprj ..\couleurs1\couleurs1.vnp 54
dec_var espagne 1
[Polygone 7 points]
```

---

## 📁 Fichiers

- **vnd_decompiler_v4.py**: Désassembleur final recommandé
- **couleurs1_v4_final.txt**: Sortie complète de couleurs1.vnd
- **vnd_decompiler_v5.py**: Tentative de parsing binaire par type (abandonné - trop complexe)

---

## 🔍 Structure VND Découverte

### Records VND

Format: `[SÉPARATEUR:01000000][LENGTH:4][TYPE:4][DATA]`

⚠️ **Le champ LENGTH n'est PAS fiable!** Utiliser distance au prochain séparateur.

### Types de Records

| Type | Description | Contenu |
|------|-------------|---------|
| **0** | Scène | Audio, images, scripts, conditions, polices |
| **1** | Condition/Action | `if var op val then command` + opcodes |
| **2** | Hotspot | Polygone + texte (OPCODE + Points + Texte) |
| **38** | Texte hotspot | `X Y W H layer text` |
| **105** | Polygone pur | Count + points (x,y) binaires |
| **7, 26, 39** | Police | `SIZE STYLE #COLOR FONT` |
| **20-24** | Vidéo AVI | Chemins `.avi` + params |
| **8-12** | Audio WAV | Chemins `.wav` |
| **28-90+** | Commandes variées | Conditions + actions textuelles |

### Hotspots

Un hotspot = **séquence de plusieurs records**:

1. Type 38: Texte et position d'affichage
2. Type 2 ou 105: Zone cliquable (polygone)
3. Type 1: Destination/action
4. Type 3/21: Logique/scripts

**Source**: `VND_SCENE_STRUCTURE_EXPLAINED.md` lignes 1-150

### Opcodes

Les lettres en fin de données (`54i`, `39h`, etc.) sont des **opcodes séparés** lus par le moteur:

- **'i'** (41%): Images/INDEX
- **'d'** (30%): DIRECT navigation
- **'h'** (3%): Tooltip
- **'l'** (6%): MIDI Music
- **'f'** (1%): Navigation

**Source**: `VND_MASTER_REFERENCE.md` lignes 105-143

---

## 🚀 Utilisation

```bash
python3 vnd_decompiler_v4.py Vnd-vnp/couleurs1.vnd > output.txt
```

---

## 📊 Statistiques

- **Total records**: 739 (couleurs1.vnd)
- **Total polygones**: 34
- **Types de records identifiés**: 100+
- **Fichiers analysés**: 19 fichiers VND du projet Europeo

---

## 🔗 Références

- `VND_MASTER_REFERENCE.md`: Documentation centralisée complète
- `VND_SCENE_STRUCTURE_EXPLAINED.md`: Structure hiérarchique des scènes
- `VND_RECORDS_ADVANCED.md`: Types 50-100+ et patterns
- `DOCS/`: Documentation technique complète du format VND
