# ⚠️ NOTES IMPORTANTES - Structures TVN du Moteur VND

## 🎯 CRITICAL: Structures de Commandes VND

Ces structures proviennent du désassemblage de **vnresmod.dll** et définissent **tous les types de commandes** du moteur Visual Novel.

### 📋 Liste des Structures TVN Identifiées

| Structure | Offset | Description Probable |
|-----------|--------|----------------------|
| `TVNProjectParms *` | `0x0040EC02` | Paramètres de projet (.vnp) |
| `TVNMidiParms *` | `0x0040EC20` | Commandes MIDI audio |
| `TVNDigitParms *` | `0x0040EC3B` | Paramètres numériques/digits |
| `TVNHtmlParms *` | `0x0040EC57` | Contenu HTML (?) |
| `TVNImageParms *` | `0x0040EC72` | **Images (playavi, addbmp)** |
| `TVNImgObjParms *` | `0x0040EC8E` | Objets images |
| `TVNImgSeqParms *` | `0x0040ECAB` | Séquences d'images |
| `TVNExecParms *` | `0x0040ECC8` | **Exécution (runprj)** |
| `TVNSetVarParms *` | `0x0040ECE3` | **set_var, inc_var, dec_var** |
| `TVNIfParms *` | `0x0040ED00` | **Conditions if-then-else** |
| `TVNCommand *` | `0x0040EDC9` | Commande générique (parent) |
| `TVNTextParms *` | `0x0040ED75` | **Affichage texte** |
| `TVNTextObjParms *` | `0x0040ED90` | Objets texte |
| `TVNFontParms *` | `0x0040EDAE` | **Paramètres police** |
| `TVNSceneParms *` | `0x0040EDE2` | **Navigation scènes** |
| `TVNStringParms *` | `0x0040EDFE` | Paramètres chaînes |

---

## 🔗 Correspondance avec l'Analyse VND

### Structures Confirmées par l'Analyse

| Structure TVN | Commandes Trouvées | Fichier Référence |
|---------------|-------------------|-------------------|
| `TVNImageParms` | `playavi`, `addbmp`, `delbmp` | `VND_SCRIPTING_LANGUAGE.md` |
| `TVNSetVarParms` | `set_var`, `inc_var`, `dec_var` | `parse_complete_commands.py` |
| `TVNIfParms` | `variable = val then action` | 300+ dans couleurs1.vnd |
| `TVNExecParms` | `runprj <projet.vnp> <scene>` | Multiples occurrences |
| `TVNTextParms` | Affichage texte avec coords | `couleurs1_resources/texts.txt` |
| `TVNFontParms` | Format: `SIZE STYLE #COLOR FONT` | Type 39 records |
| `TVNSceneParms` | `scene <numéro>` | Navigation inter-scènes |

### Structures Non Encore Observées

| Structure TVN | À Rechercher |
|---------------|--------------|
| `TVNMidiParms` | Commandes MIDI/musique |
| `TVNDigitParms` | Entrées numériques utilisateur ? |
| `TVNHtmlParms` | Affichage HTML ? (peu probable) |
| `TVNImgObjParms` | Objets images interactifs ? |
| `TVNImgSeqParms` | Animations/séquences ? |
| `TVNTextObjParms` | Objets texte avancés ? |

---

## 📊 Corrélation Types de Records vs Structures TVN

### Hypothèse: Types Calculés par Structure

Les types de records trouvés dans `couleurs1.vnd` pourraient correspondre à des **hash** ou **IDs dérivés** de ces structures TVN:

| Type Record | Count | Structure TVN Probable |
|-------------|-------|------------------------|
| 32 (0x20) | 91 | `TVNSetVarParms` (set_var) |
| 37 (0x25) | 28 | `TVNImageParms` (playwav) |
| 45 (0x2d) | 21 | `TVNExecParms` (runprj) |
| 51 (0x33) | 17 | `TVNImageParms` (playavi) |
| 38 (0x26) | 13 | `TVNSetVarParms` (dec_var) |
| 39 (0x27) | 6 | `TVNFontParms` (police) |
| 27 (0x1b) | 3 | `TVNSceneParms` (scene) |

**NOTE**: Cette corrélation est spéculative et doit être confirmée par analyse de vnresmod.dll.

---

## 🔬 Prochaines Étapes de Reverse Engineering

### 1. Analyser vnresmod.dll avec IDA Pro/Ghidra

**Objectifs**:
- Trouver les définitions complètes des structures TVN
- Identifier les vtables et méthodes associées
- Comprendre le parsing des records VND
- Documenter l'algorithme de calcul des types

**Commandes**:
```bash
# Avec IDA Free
ida64 vnresmod.dll

# Ou avec Ghidra (déjà installé)
analyzeHeadless /tmp VnResmod -import vnresmod.dll -analyze
```

### 2. Rechercher les Patterns dans vnresmod.dll

**Patterns à chercher**:
```c
// Structures potentielles
struct TVNImageParms {
    uint32_t type;
    char* filename;
    int x, y, w, h;
    int loop;
};

struct TVNSetVarParms {
    uint32_t type;
    char* varname;
    int value;
    int operation;  // set, inc, dec
};

struct TVNIfParms {
    uint32_t type;
    char* condition;
    TVNCommand* then_cmd;
    TVNCommand* else_cmd;
};
```

### 3. Identifier le Parser VND

**Rechercher dans vnresmod.dll**:
- Fonction `LoadVND()` ou `ParseVND()`
- Lecture du séparateur `0x01000000`
- Switch/case sur le type de record
- Allocation des structures TVN*

### 4. Mapper Complètement le Format

**Créer une table de correspondance**:
```
Type Record → Structure TVN → Fonction de parsing → Commande de jeu
```

---

## 📁 Fichiers à Analyser

### DLL Principale
- `vnresmod.dll` - **Moteur principal du Visual Novel**
  - Contient toutes les structures TVN
  - Parser VND
  - Interpréteur de commandes
  - Gestionnaire de scènes

### Fichiers VND Additionnels (si disponibles)
- `*.vnd` - Autres fichiers de scène
- `*.vnp` - Fichiers projet
- Comparer les variations entre jeux/versions

---

## 🛠️ Outils Installés pour l'Analyse

### Reverse Engineering
- ✅ **IDA Free 8.4** (`/opt/idafree/`)
  - `ida64` - Interface graphique
  - `idat64` - Mode texte
- ✅ **Ghidra 12.0.1** (`/opt/ghidra/`)
- ✅ **radare2 5.5.0**
- ✅ **GDB + GEF**

### Analyse Binaire
- ✅ binutils (objdump, nm, strings)
- ✅ hexedit, xxd
- ✅ binwalk, foremost
- ✅ elfutils, patchelf

### Python Tools
- ✅ pwntools, capstone, keystone, unicorn
- ✅ ROPgadget

---

## 💡 Insights Importants

### 1. Architecture Orientée Objet

Les structures `TVN*Parms` suivent un pattern orienté objet avec:
- **Parent commun**: `TVNCommand`
- **Polymorphisme**: via vtables
- **Taille fixe**: 4 bytes (pointeur)
- **Allocation dynamique**: structures créées au runtime

### 2. Format VND = Sérialisation

Le format VND est probablement une **sérialisation** de ces structures:
```
[type_id] → identifie la structure TVN* à créer
[length] → taille des données sérialisées
[data] → données à copier dans la structure
```

### 3. Types Variables

Les types de records (20-65) sont probablement:
- **Calculés** à partir du nom de commande
- **Dépendants** du contenu
- **Non fixes** entre versions

Ceci explique pourquoi la spécification fournie ne correspondait pas à `couleurs1.vnd`.

---

## 🎯 Actions Prioritaires

### IMMÉDIAT
1. ✅ Installer IDA Free
2. ⬜ Obtenir vnresmod.dll
3. ⬜ Charger vnresmod.dll dans IDA/Ghidra
4. ⬜ Rechercher les offsets des structures TVN

### COURT TERME
1. ⬜ Définir complètement chaque structure TVN*
2. ⬜ Identifier le parser VND
3. ⬜ Comprendre l'algorithme de type_id
4. ⬜ Créer un décodeur universel

### LONG TERME
1. ⬜ Parser universel VND multi-versions
2. ⬜ Éditeur VND graphique
3. ⬜ Recompilateur VND
4. ⬜ Documentation complète du moteur

---

## 📝 Références Croisées

### Documents Créés
- `VND_FORMAT_ANALYSIS.md` - Analyse initiale
- `VND_FORMAT_CORRECTED.md` - Corrections post-analyse manuelle
- `VND_SCRIPTING_LANGUAGE.md` - Langage de script documenté
- `VND_SPEC_VS_REALITY.md` - Comparaison spec vs réalité
- `VND_CRITICAL_NOTES.md` - **CE FICHIER**

### Scripts Créés
- `vnd_disasm.py` - Désassembleur VND
- `verify_vnd_types.py` - Vérification types
- `analyze_real_types.py` - Analyse patterns
- `parse_complete_commands.py` - Reconstitution commandes

### Données Extraites
- `couleurs1_resources/` - Fichiers, textes, variables
- `couleurs1_blocks/` - Blocs binaires extraits

---

## ⚠️ CRITICAL REMINDER

**Ces structures TVN sont la CLÉ du format VND.**

Sans elles, on ne peut que deviner. Avec elles, on peut:
- ✅ Comprendre chaque type de record
- ✅ Parser n'importe quel fichier VND
- ✅ Créer/modifier des fichiers VND
- ✅ Comprendre le moteur Visual Novel

**Next Step**: Analyser vnresmod.dll pour extraire les définitions complètes.

---

**Date**: 2026-01-15
**Status**: 🔴 STRUCTURES IDENTIFIÉES - ANALYSE DLL REQUISE
**Priorité**: ⭐⭐⭐⭐⭐ CRITIQUE
