# Priorités de Recherche VND - Orientées Décodage

**Date**: 2026-01-16
**Objectif**: Décoder le format VND pour recréer un moteur Visual Novel

---

## 🎯 FONCTIONS CRITIQUES À ANALYSER

Basé sur la documentation VND, voici les fonctions **prioritaires** identifiées dans europeo.exe:

### 🔴 PRIORITÉ CRITIQUE (À faire maintenant)

#### 1. **sub_43177D** - Répartiteur de Commandes (LE CŒUR!)
**Rôle**: Moteur d'exécution central qui parse les opcodes VND
**Localisation**: Mentionné dans la doc comme le dispatcher principal
**Ce qu'il fait**:
- Lit le flux VND octet par octet
- Convertit les lettres a-z en indices 1-26
- Dispatch vers les handlers spécifiques (scene, playavi, set_var, etc.)
- Table de 49 entrées de commandes

**Opcodes clés**:
| Lettre | Index | Fonction | Rôle |
|--------|-------|----------|------|
| f | 6 | sub_4268F8 | **Navigation scène** |
| h | 8 | sub_426D33 | Tooltip |
| i | 9 | sub_42703A | **Images (AVI/BMP)** |
| j | 10 | sub_4275F6 | **Bitmaps (palette)** |
| k | 11 | sub_427B56 | **Audio (WAV)** |
| u | 21 | sub_431721 | **Logic (if/then)** |

**ACTION IMMÉDIATE**:
```
1. Désassembler sub_43177D dans IDA
2. Identifier la switch table de 49 entrées
3. Extraire tous les handlers d'opcodes
4. Documenter le format exact du parsing
```

---

#### 2. **sub_407FE5** - Extracteur d'Arguments
**Rôle**: Parse les paramètres numériques avant les opcodes
**Ce qu'il fait**:
- Utilise `atol()` pour convertir ASCII → nombre
- S'arrête au premier caractère non-numérique
- Le caractère suivant = opcode immédiat

**Exemple de parsing**:
```
Flux: "54h"
→ atol() lit "54" → valeur = 54
→ Pointeur sur 'h' → Opcode 8 (tooltip) exécuté immédiatement
```

**Dans nos résultats précédents**:
- **Path parser appelé 6x** par le coordinateur 0x0040AEB4
- Probablement la fonction mentionnée dans la doc!

**ACTION**:
```
Désassembler 0x407FE5 pour confirmer le mécanisme atol()
```

---

#### 3. **dword_44ECCE** - Table Globale des Variables
**Rôle**: Tableau en mémoire contenant toutes les variables du jeu
**Variables critiques**:
- `SCORE` - Points du joueur
- `FIOLE` - Progression (0-12)
- `SACADOS` - Inventaire activé
- `CPAYS` - Pays actuel
- `FRANCS` - Mode monétaire

**Structure dans VND**:
```
[LENGTH:uint32] [NAME:ASCII] [VALUE:uint32]
Exemple:
07 00 00 00 "SACADOS" 00 01 00 00 00
```

**ACTION**:
```
1. Dumper la mémoire @ 0x44ECCE pendant l'exécution
2. Identifier le format exact du tableau
3. Mapper les offsets de chaque variable
```

---

### 🟡 PRIORITÉ HAUTE (Après le dispatcher)

#### 4. **sub_4268F8** - Navigation Scène (Opcode 'f')
**Rôle**: Gère les transitions entre scènes
**Ce qu'il fait**:
- Charge nouvelle scène par ID
- Libère ressources de l'ancienne scène
- Initialise contexte graphique

**Lien avec classe**:
- Probablement méthode de **TVNScene** (TYPEINFO @ 0x004179AE)
- Distance: Calculer offset depuis TYPEINFO

**ACTION**:
```
Analyser sub_4268F8 pour comprendre:
- Comment l'ID de scène est extrait
- Quelles ressources sont chargées (BMP, AVI, WAV)
- Mécanisme de transition
```

---

#### 5. **sub_42703A** - Chargement Images (Opcode 'i')
**Rôle**: Charge AVI/BMP selon le contexte
**Types de records associés**:
- Type 20-24 (0x14-0x18): Vidéos AVI
- Type 0 (0x00): Images de fond BMP

**ACTION**:
```
Comprendre comment il détermine AVI vs BMP
```

---

#### 6. **sub_431721** - Logique Conditionnelle (Opcode 'u')
**Rôle**: Évalue les conditions if/then
**Format**:
```
if VARIABLE OPERATOR VALUE then COMMAND
```

**Opérateurs supportés**:
- `==` - Égal
- `!=` - Différent
- `>` - Supérieur
- `<` - Inférieur
- `>=` - Supérieur ou égal
- `<=` - Inférieur ou égal

**Interaction avec dword_44ECCE**: Lit/écrit directement dans le tableau de variables

**ACTION**:
```
Analyser la logique de comparaison et branchement
```

---

### 🟢 PRIORITÉ MOYENNE (Pour compréhension complète)

#### 7. **sub_41721D** - Chargement Fichier VND
**Rôle**: Lit et valide le header VND
**Validation**:
- Vérifie signature "VNFILE" @ offset 0x09
- Lit dimensions écran (640x480)
- Parse checksum

**ACTION**:
```
Analyser pour créer un parser VND complet
```

---

#### 8. **sub_410AF6** - Validation Scène (TVNScene)
**Rôle**: Vérifie qu'une scène existe avant transition
**Classe**: TVNScene @ 0x004179AE

**ACTION**:
```
Comprendre les checks de validité
```

---

## 📋 STRUCTURE DU FORMAT VND

### Header (Offset 0x00)
```
0x00: Magic [9 bytes]      = 3a 01 01 00 00 06 00 00 00
0x09: Signature [6 bytes]  = "VNFILE"
0x0F: Version Length [4]
0x13: Version [variable]   = "2.136"
...   Project Name
...   Creator               = "Sopra Multimedia"
0x48: Checksum Length [4]
0x4C: Checksum [8]         = "5D51F233"
0x5C: Width [4]            = 640
0x60: Height [4]           = 480
0x64: Color Depth [4]      = 16
...   Flags [12]
0x7C: DLL Path Length [4]
0x80: DLL Path             = "..\VnStudio\vnresmod.dll"
```

### Table des Variables (Après Header)
```
Structure par variable:
[LENGTH:4] [NAME:ASCII] [00] [VALUE:4]

Exemple:
07 00 00 00 "SACADOS" 00 01 00 00 00
05 00 00 00 "SCORE" 00 00 00 00 00
```

### Records (Corps du fichier)
```
Structure standard:
[SEPARATOR:4] [LENGTH:4] [TYPE:4] [DATA:variable]

SEPARATOR = 01 00 00 00 (toujours)
TYPE = Type ID (voir table ci-dessous)
```

### Types de Records Critiques

| Type | Hex | Nom | Données | Rôle |
|------|-----|-----|---------|------|
| 0 | 0x00 | Scène | Chemin BMP fond | **Définit une scène** |
| 1 | 0x01 | Scene ID | Numéro court | ID de destination |
| 2 | 0x02 | Hotspot Rect | X Y W H | **Zone cliquable rectangulaire** |
| 3 | 0x03 | Script | Commandes | Scripts conditionnels |
| 8,11,12 | 0x08,0x0B,0x0C | Audio | Chemin WAV | Sons |
| 20-24 | 0x14-0x18 | Vidéo | Chemin AVI | Cinématiques |
| 21 | 0x15 | Condition | if/then | **Logique conditionnelle** |
| 22 | 0x16 | set_var | var=val | Assignation variable |
| 23 | 0x17 | inc_var | var++ | Incrémentation |
| 24 | 0x18 | dec_var | var-- | Décrémentation |
| 27 | 0x1B | addbmp | Params | Ajout bitmap |
| 28 | 0x1C | delbmp | Params | Suppression bitmap |
| 31 | 0x1F | runprj | Chemin | Lancement projet |
| 38 | 0x26 | Hotspot Text | "X Y W H 0 Name" | Texte survol |
| 105 | 0x69 | Polygone | Points[x,y] | **Zone cliquable polygonale** |

---

## 🔍 CORRÉLATION AVEC NOS DÉCOUVERTES

### Coordinateur @ 0x0040AEB4 (312 instr, 44 calls)
**Hypothèse révisée**: Pas le dispatcher principal, mais probablement **TVNCommand constructor**

**Relation avec sub_43177D**:
- Le coordinateur initialise les commandes
- sub_43177D les exécute
- Lien: VTable 0x004402AC

**Prochaine action**:
```
Chercher sub_43177D dans le binaire pour confirmer qu'il existe
```

### Path Parser @ 0x407FE5
**Confirmé**: C'est bien l'extracteur d'arguments mentionné dans la doc!

**Fonction exacte**: Convertit les strings ASCII en nombres via atol()

---

## 🎯 PLAN D'ACTION IMMÉDIAT

### Étape 1: Localiser sub_43177D
```bash
# Chercher la fonction dans le binaire
objdump -d europeo.exe | grep -A 50 "43177d:"
```

### Étape 2: Analyser la Switch Table
```
1. Identifier les 49 entrées
2. Extraire toutes les adresses de handlers
3. Mapper opcodes → fonctions
```

### Étape 3: Dumper la Table de Variables
```
1. Lancer europeo.exe dans un débogueur
2. Breakpoint @ 0x44ECCE
3. Dumper la structure en mémoire
```

### Étape 4: Parser un Fichier VND
```python
# Créer un parser Python basé sur la spec
1. Lire header avec signature VNFILE
2. Parser table de variables
3. Lire records séquentiels
4. Afficher la structure
```

---

## 📊 FONCTIONS IDENTIFIÉES vs DOC

| Doc | Adresse | Status | Priorité |
|-----|---------|--------|----------|
| sub_43177D (dispatcher) | ❓ | **À TROUVER** | 🔴 CRITIQUE |
| sub_407FE5 (atol parser) | 0x407FE5 | ✅ TROUVÉE | 🔴 CRITIQUE |
| dword_44ECCE (var table) | 0x44ECCE | ✅ ADRESSE CONNUE | 🔴 CRITIQUE |
| sub_4268F8 (scene nav) | 0x4268F8 | ✅ ADRESSE CONNUE | 🟡 HAUTE |
| sub_42703A (images) | 0x42703A | ✅ ADRESSE CONNUE | 🟡 HAUTE |
| sub_4275F6 (bitmaps) | 0x4275F6 | ✅ ADRESSE CONNUE | 🟡 HAUTE |
| sub_427B56 (audio) | 0x427B56 | ✅ ADRESSE CONNUE | 🟡 HAUTE |
| sub_431721 (logic) | 0x431721 | ✅ ADRESSE CONNUE | 🟡 HAUTE |
| sub_41721D (load VND) | 0x41721D | ✅ ADRESSE CONNUE | 🟢 MOYENNE |
| sub_410AF6 (validate) | 0x410AF6 | ✅ ADRESSE CONNUE | 🟢 MOYENNE |
| TVNScene TYPEINFO | 0x004179AE | ✅ TROUVÉE | ✅ |

---

## 🚀 PROCHAINES ACTIONS

### 1. Analyser sub_43177D (LE PLUS IMPORTANT!)
```
objdump -d DOCS/europeo.exe -M intel --start-address=0x43177d --stop-address=0x432000
```

### 2. Extraire la Switch Table des Opcodes
```
Identifier toutes les 49 entrées
Créer la table complète: opcode → handler
```

### 3. Analyser les Handlers Critiques
```
sub_4268F8 - Navigation
sub_42703A - Images
sub_431721 - Logic
```

### 4. Dumper la Table de Variables @ 0x44ECCE
```
Utiliser un débogueur pour voir la structure en mémoire
```

### 5. Créer un Parser VND
```python
# Parser basé sur la spec documentée
- Header avec VNFILE
- Table de variables
- Records séquentiels
```

---

## ❌ CE QUI N'EST PLUS PRIORITAIRE

- ~~Analyse graphique (SetPaletteEntries, BitBlt)~~ → Délégué au moteur maison
- ~~115 vtables à réassigner~~ → Pas critique pour VND
- ~~TVNBitmap détails~~ → Géré par le nouveau moteur
- ~~Path replacement/modding~~ → Feature secondaire

**Focus 100% sur**: Comprendre comment le VND est parsé et exécuté!

---

## 📝 NOTES IMPORTANTES

### Artefacts de Parsing (À IGNORER)
La doc mentionne des Type IDs erronés:
- Type 257 = Mauvaise lecture de "VNFILE"
- Type 1634296933 = Mauvaise lecture du Checksum
- Type 280 = Mauvaise lecture de "SACADOS"

→ Ces types n'existent PAS réellement dans le format!

### Format des Suffixes
Les lettres après les nombres (ex: `54h`, `13d`) ne sont PAS des types de records, mais des **opcodes immédiats** exécutés après le parsing du nombre.

---

**Fichier généré**: Pour guider l'analyse vers le décodage VND
**Prochaine étape**: Analyser sub_43177D (dispatcher)
