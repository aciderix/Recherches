# VND Records Avancés - Types 50-100+

**Version**: 1.0
**Date**: 2026-01-17
**Source**: Analyse de 16 977 records sur 19 fichiers VND

---

## 📊 Vue d'ensemble

**Records analysés** : 16 977 total
**Types identifiés** : 100+ types uniques
**Types rares (≤5 occurrences)** : 27 types

Ce document se concentre sur les **types de records avancés** (types 50-100+) qui sont peu utilisés mais présents dans le format VND.

---

## 🔍 Types de Records par Fréquence

### Types Fréquents (>100 occurrences)

| Type | Occurrences | % | Description | Échantillon |
|------|-------------|---|-------------|-------------|
| **28** | 1630 | 9.6% | inc_var operations | `bouee = 2 then inc_var non 1` |
| **32** | 1352 | 8.0% | partition operations | `partition = 2 then inc_var non 1` |
| **29** | 1333 | 7.9% | ciseau operations | `ciseau = 2 then inc_var non 1` |
| **31** | 1264 | 7.4% | clerouge operations | `clerouge = 2 then inc_var non 1` |
| **30** | 1205 | 7.1% | ballon operations | `ballon1 = 2 then inc_var non 1` |
| **0** | 1061 | 6.2% | Scènes (Type 0) | Audio + Images + Scripts |
| **34** | 903 | 5.3% | castagnette operations | `castagnette = 2 then inc_var non 1` |
| **35** | 718 | 4.2% | taillepierre operations | `taillepierre = 2 then inc_var non 1` |
| **36** | 577 | 3.4% | fiolefinlande operations | `fiolefinlande = 2 then inc_var non 1` |
| **1** | 562 | 3.3% | Référence scène + conditions | `score < 0 then runprj ...` |
| **26** | 536 | 3.2% | bus operations | `bus = 2 then inc_var non 1` |
| **33** | 520 | 3.1% | papiercado operations | `papiercado = 2 then inc_var non 1` |
| **2** | 508 | 3.0% | Hotspots rectangulaires | Coordonnées + texte |
| **27** | 432 | 2.5% | pain operations | `pain = 2 then inc_var non 1` |
| **38** | 318 | 1.9% | fioleangleterre operations | `fioleangleterre = 2 then inc_var non 1` |
| **9** | 305 | 1.8% | Audio/Vidéo | `Avion.wav` + `.avi` files |
| **8** | 285 | 1.7% | Questions | `question = ...` |
| **6** | 183 | 1.1% | Punk/non operations | Conditions punk/non |
| **23** | 170 | 1.0% | closewav + orgue | `punk = 1 then closewav` |
| **10** | 152 | 0.9% | WAV audio | `bras.wav 2` |
| **5** | 149 | 0.9% | État variables | `non 0` + conditions |

---

## 🔎 Types Moyennement Utilisés (10-100 occurrences)

| Type | Occ. | Description | Échantillon |
|------|------|-------------|-------------|
| **37** | 137 | Bonus + cartoon | `bonus8 = 1 then playwav cartoon.wav 1` |
| **42** | 123 | pier_berlin operations | `pier_berlin = 0 then set_var...` |
| **3** | 121 | Scripts/valeurs | `justeprixreponse = 5 then...` |
| **55** | 115 | Bonus audio | `bonus15 = 1 then playwav...` |
| **40** | 109 | calc + rundll | `calc = 1 then rundll ..\barre\euro32.dll` |
| **11** | 105 | Orgue WAV | `Orgue.wav 2` |
| **51** | 102 | playavi aviateur | `non = 0 then playavi aviateur1.avi` |
| **45** | 102 | fioleirlande dec_var | `fioleirlande = 2 then dec_var...` |
| **24** | 101 | Bonus scène | `bonus16 = 1 then scene 1` |
| **43** | 101 | fiolegrece2 dec_var | `fiolegrece2 = 2 then dec_var...` |
| **52** | 100 | playavi aviateur99 | `non = 1 then playavi aviateur99.avi` |
| **47** | 92 | justeprixreponse set_var | `justeprixreponse = 5 then set_var...` |
| **7** | 85 | Score operations | `score 5` + opcode |
| **25** | 84 | Bonus scène variant | `bonus16 = 1 then scene 9` |
| **44** | 83 | taillepierre dec_var | `taillepierre = 2 then dec_var...` |
| **50** | 82 | playavi punk2 | `non = 0 then playavi punk2.avi 1` |
| **41** | 79 | fiolegrece dec_var | `fiolegrece = 2 then dec_var...` |
| **73** | 51 | bonus16 playavi | `bonus16 = 1 then playavi...` |
| **48** | 59 | justeprix cartoon | `justeprixquestion = 2 then playwav cartoon` |
| **49** | 61 | playavi orgue1 | `non = 0 then playavi orgue1.avi` |
| **53** | 61 | playavi brasse4 | `biereok = 3 then playavi brasse4.avi` |
| **57** | 53 | trans playavi | `trans = 1 then playavi...` |
| **54** | 50 | playavi brasse1 | `biereok != 3 then playavi brasse1.avi` |
| **39** | 64 | partition set_var -1 | `partition = 2 then set_var partition -1` |
| **12** | 33 | Cochon WAV | `Cochon.wav 1` |
| **13** | 34 | corbeau WAV | `corbeau.wav 2` + conditions |

---

## 🔬 Types Rares (1-10 occurrences)

### Types 60-69

| Type | Occ. | Fichier | Échantillon |
|------|------|---------|-------------|
| **64** | 15 | couleurs1 | `bonus16 = 0 then playwav...` |
| **61** | 26 | Multiple | `pier_berlin = -1 then addbmp taille2` |
| **62** | 19 | biblio | `mauvaisenote = 1 then playwav...` |
| **63** | 29 | biblio | `mauvaisenote = 2 then playwav...` |
| **65** | 7 | couleurs1 | `telephone = 0 then playavi euroland\biblio...` |
| **66** | 7 | couleurs1 | `justeprixquestion = 0 then addbmp question` |
| **68** | 2 | couleurs1 | `painok != 1 then playtext 35 50 125 365` |
| **69** | 4 | Multiple | `cpays = <numpays> then playwav cling.wav` |

### Types 70-79

| Type | Occ. | Fichier | Échantillon |
|------|------|---------|-------------|
| **70** | 2 | couleurs1 | `clejaune = 0 then playtext 1540 210 1700 230 0` |
| **71** | 4 | couleurs1 | `clejaune = 0 then playtext 1540 190 1700 210 0` |
| **72** | 2 | belge | `numpaysscore = 1 then addtext quest2 6 420 380 64` |
| **73** | 34 | Multiple | `bonus8 = 1 then playavi...` |
| **74** | 51 | Multiple | `bonus16 = 1 then playavi...` |
| **75** | 5 | couleurs1 | `clejaune = 0 then addbmp clejaune euroland\rollover` |
| **76** | 8 | Multiple | `photo = 2 then playtext 350 90 1 1 0 OUI !` |
| **77** | 6 | Multiple | `NUMERO = 3 then playtext 350 90 1 1 0 OUI` |
| **78** | 1 | belge | Police Comic sans MS (white) |

### Types 80-99

| Type | Occ. | Fichier | Échantillon |
|------|------|---------|-------------|
| **80** | 1 | belge | `ques1 6 12 420 351 115 0 Si tu as 10 bonnes r` |
| **81** | 10 | Multiple | `..\VnStudio\vnresmod.dll` |
| **82** | 4 | italie | `capitale = 10 then playtext 100 170 1 1 0 OUI !` |
| **83** | 1 | angleterre | `X...22i` (données binaires) |
| **84** | 2 | italie | `clerouge = 2 then playtext 240 120 125 365 0 Non` |
| **86** | 2 | danem | `tulipejaune != 2 then if jeugagne = -1 then addbmp` |
| **88** | 1 | ecosse | `colomb = 1 then playtext 10 355 365 120 0 Tu as d` |
| **89** | 3 | couleurs1 | `sacados = 0 then playtext 20 350 105 365 0 Il te f` |
| **90** | 2 | couleurs1 | `allumette = 0 then playtext 20 370 125 365 0 Il te` |
| **91** | 1 | allem | `justeprixreponse = 5 then playwav applaud.wav 1` |

### Types 100+

| Type | Occ. | Fichier | Échantillon |
|------|------|---------|-------------|
| **100** | 1 | holl | Données binaires |
| **108** | 10 | Multiple | `capitale = 0 then playwav...` |
| **109** | 5 | france | Données avec `7` + marker |
| **110** | 1 | allem | Données binaires |
| **111** | 2 | biblio | `max.wav 1` + cphoto |
| **117** | 1 | holl | Données binaires (lettres) |
| **122** | 1 | espa | Données binaires |
| **129** | 1 | ecosse | Police Comic sans MS (white) |
| **132** | 1 | italie | Police Comic sans MS (white) |
| **140** | 1 | italie | Données + police Comic sans MS |
| **174** | 1 | ecosse | Police Comic sans MS (white) |
| **175** | 1 | grece | Police Comic sans MS (black) |
| **184** | 1 | italie | Données + police Comic sans MS |

---

## 🎯 Patterns Détectés dans Records Avancés

### Pattern 1 : Opérations Conditionnelles sur Variables

**Types** : 28-36, 38, 41-45

**Format** :
```
<variable> = <valeur> then <opération> <variable> <increment>
```

**Exemples** :
- `bouee = 2 then inc_var non 1`
- `partition = 2 then inc_var non 1`
- `fiolegrece = 2 then dec_var fiolegrece 1`
- `taillepierre = 2 then set_var taillepierre -1`

**Rôle** : Gestion d'inventaire et variables du jeu

---

### Pattern 2 : Multimédia Conditionnel

**Types** : 37, 48-54, 64-65, 73-74, 91, 108

**Format** :
```
<condition> then play<type> <fichier> <params>
```

**Exemples** :
- `bonus8 = 1 then playwav cartoon.wav 1`
- `non = 0 then playavi aviateur1.avi 1`
- `biereok = 3 then playavi brasse4.avi 1`
- `bonus16 = 0 then playwav...`
- `capitale = 0 then playwav...`

**Types de média** :
- `playwav` : Audio WAV
- `playavi` : Vidéo AVI

**Rôle** : Déclenchement audio/vidéo basé sur état du jeu

---

### Pattern 3 : Affichage Texte Conditionnel

**Types** : 68, 70-72, 76-77, 82, 84, 88-90

**Format** :
```
<condition> then playtext <x> <y> <w> <h> <flags> <texte>
```

**Exemples** :
- `painok != 1 then playtext 35 50 125 365 0 ...`
- `clejaune = 0 then playtext 1540 210 1700 230 0 ...`
- `photo = 2 then playtext 350 90 1 1 0 OUI !`
- `capitale = 10 then playtext 100 170 1 1 0 OUI !`

**Paramètres** :
- `x, y` : Position à l'écran
- `w, h` : Largeur/hauteur zone de texte
- `flags` : Options d'affichage (0 = standard)
- `texte` : Message à afficher

**Rôle** : Affichage messages conditionnels (feedback joueur)

---

### Pattern 4 : Gestion Images Conditionnelle

**Types** : 55-56, 59, 61, 66, 75

**Format** :
```
<condition> then addbmp <nom> <fichier> <x> <y>
```

**Exemples** :
- `occupe10 = 1 then addbmp f10 rollover\b9...`
- `non = 0 then addbmp beet infobeet.bmp 0...`
- `pier_berlin = -1 then addbmp taille2 rol...`
- `clejaune = 0 then addbmp clejaune euroland\rollover...`

**Rôle** : Ajout dynamique d'images selon état du jeu

---

### Pattern 5 : Polices et Formatage

**Types** : 78, 129, 132, 140, 174, 175, 184

**Format** :
```
<taille> <style> #<couleur> <police>
```

**Exemples** :
- `18 0 #ffffff Comic sans MS` (blanc)
- `18 0 #000000 Comic sans MS` (noir)
- `22 0 #ffffff Comic sans MS`

**Couleurs détectées** :
- `#ffffff` : Blanc
- `#000000` : Noir
- `#ff0000` : Rouge

**Rôle** : Configuration affichage texte

---

### Pattern 6 : Intégration DLL

**Type** : 40, 81

**Format** :
```
<condition> then rundll <chemin_dll>
```

**Exemple** :
- `calc = 1 then rundll ..\barre\euro32.dll`

**Chemin DLL standard** :
- `..\VnStudio\vnresmod.dll`
- `..\barre\euro32.dll`

**Rôle** : Appel fonctions externes (calculatrice Euro, ressources)

---

## 📈 Statistiques par Catégorie

| Catégorie | Nombre de Types | Occurrences Totales | % |
|-----------|-----------------|---------------------|---|
| **Variables (inc/dec/set)** | 20+ | ~8500 | 50% |
| **Multimédia (audio/vidéo)** | 15+ | ~2000 | 12% |
| **Scènes (Type 0)** | 1 | 1061 | 6% |
| **Conditions générales** | 10+ | ~1500 | 9% |
| **Affichage texte** | 10+ | ~500 | 3% |
| **Gestion images** | 10+ | ~800 | 5% |
| **Polices/formatage** | 7+ | ~20 | <1% |
| **Autres/rares** | 30+ | ~100 | <1% |

---

## 🔍 Types Non Documentés (Données Binaires)

Certains types contiennent des données binaires non textuelles :

| Type | Occurrences | Note |
|------|-------------|------|
| 100 | 1 | Données binaires pures |
| 109 | 5 | Contient marqueur `7` |
| 110 | 1 | Données binaires |
| 117 | 1 | Séquence de lettres |
| 122 | 1 | Données binaires |

**Hypothèse** : Structures de données compilées, configurations binaires, ou métadonnées compressées.

---

## 📝 Conclusion

**Types documentés** : 100+
**Patterns identifiés** : 6 majeurs
**Compréhension** : ~90% des records

Les types 50-100+ sont principalement :
1. **Opérations avancées sur variables** (gestion inventaire complexe)
2. **Multimédia conditionnel** (audio/vidéo basé sur état)
3. **Affichage dynamique** (texte et images conditionnels)
4. **Configuration UI** (polices, couleurs)
5. **Intégration externe** (DLL calls)

La majorité des types rares suivent les **mêmes patterns** que les types fréquents, avec des conditions plus spécifiques.
