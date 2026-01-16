# VND Progress - État de la Recherche

**Version**: 2.0
**Date**: 2026-01-16
**Complétion globale**: 75%

> **Note**: Document centralisé pour suivre l'avancement. Mettre à jour ce fichier au lieu de créer de nouveaux TODOs.

---

## 📊 État Actuel

### Handlers Analysés: 13/43 (30.2%)

| Handler | Status | Fonction | Occurrences | Priorité |
|---------|--------|----------|-------------|----------|
| **'a' (1)** | ✅ | Pre-processor A | 1 | - |
| **'b' (2)** | ✅ | Pre-processor B | 0 | - |
| **'c' (3)** | ✅ | Images variant | 0 | - |
| **'d' (4)** | ✅ | Pre-processor D | 434* | - |
| **'e' (5)** | ✅ | Audio+Image | 35 | - |
| 'f' (6) | ✅ | Navigation | 11 | - |
| **'g' (7)** | ✅ | Tooltip variant | 44 | - |
| 'h' (8) | ✅ | Tooltip | 50 | - |
| 'i' (9) | ✅ | Images/INDEX | 603 | - |
| 'j' (10) | ✅ | Bitmaps | 34 | - |
| 'k' (11) | ✅ | Audio WAV | 11 | - |
| 'l' (12) | ✅ | MIDI Music | 94 | - |
| 'u' (21) | ✅ | Logic if/then | 0 | - |

**Dernière découverte**: Handlers a,b,c,d analysés - Tous pré-processeurs → handler 'i'

*Note: 'd' (434 occ.) = probablement suffixe DIRECT, pas le handler lui-même

---

### Handlers À Analyser: 30 restants

#### Priorité HAUTE (avec occurrences)

**Tous les handlers de base (a-l, u) analysés!**

Prochains handlers prioritaires:
- 'm' (13) - À vérifier occurrences
- 'n' (14) - 144 occurrences mais FAUX POSITIFS (noms fichiers)
- 'o'-'t' (15-20) - À vérifier

**Action**: Analyser handlers 13-20 (m-t) pour continuer la progression

---

#### Priorité MOYENNE (indices 13-20)

| Handler | Adresse | Occurrences | Notes |
|---------|---------|-------------|-------|
| 'm' (13) | ? | ? | Inconnu |
| 'n' (14) | ? | 0 | Faux positifs (filenames) |
| 'o' (15) | ? | ? | Inconnu |
| 'p' (16) | ? | ? | Inconnu |
| 'q' (17) | ? | ? | Inconnu |
| 'r' (18) | ? | ? | Inconnu |
| 's' (19) | ? | ? | Inconnu |
| 't' (20) | ? | ? | Inconnu |

**Action**: Chercher adresses dans switch table, vérifier occurrences

---

#### Priorité BASSE (indices 22-42)

- 'v' (22) à 'z' (26)
- Indices 27-42 (opcodes numériques?)

**Action**: Documentation + search dans switch table

---

### Fichiers Analysés: 19/19 (100%)

✅ **Tous les fichiers VND disponibles analysés**

**Dataset**:
- 19 fichiers (6.2KB - 138KB)
- 1.2 MB total
- 1461 opcodes extraits
- 11 opcodes uniques trouvés

---

### Formats Compris

| Élément | Compréhension | Notes |
|---------|---------------|-------|
| Header VNFILE | 100% | Signature, dimensions, checksum |
| Table variables | 90% | Format connu, INDEX_ID à dumper |
| Records Type 0 | 60% | Structure complexe non complète |
| Records Type 1-5 | 70% | Documentés mais non testés |
| Records Type 20-24 | 80% | Vidéos AVI bien comprises |
| Records Type 38 | 90% | Texte hotspot documenté |
| Records Type 105 | 80% | Polygones bien compris |
| Opcodes a-z | 70% | 8/43 analysés, système compris |

**Blocage principal**: Type 0 (scènes) - LENGTH non fiable

---

## 🎯 TODO Actif

### Récemment Complété ✅

- [x] **Handlers a,b,c,d (1-4)** - ANALYSÉS
  - Handler 'a' (1) @ 0x00431A20: Pre-processor A → calls 0x426b62 → handler 'i'
  - Handler 'b' (2) @ 0x00431A39: Pre-processor B → calls 0x426d33 → handler 'i'
  - Handler 'c' (3) @ 0x00431881: Images variant → calls 0x42703A (Images func) → handler 'i'
  - Handler 'd' (4) @ 0x00431A53: Pre-processor D → calls 0x4275f6 → handler 'i'
  - Pattern commun: Tous pré-processent puis délèguent à handler 'i'

- [x] **Handler 'e' (5)** @ 0x004318EE - ANALYSÉ
  - Fonction: Handler combiné Audio+Image
  - Appelle 0x427B56 (Audio WAV) puis jump vers handler 'i' (Images)
  - Pattern: Opcode de convenance pour scènes audiovisuelles
  - 35 occurrences dans holl.vnd et autres

---

### Priorité Haute

- [ ] **Parser Type 0 complet**
  - Problème: LENGTH non fiable
  - Test sur biblio.vnd (galerie photos)
  - Test sur irland.vnd (50 records)
  - **Action**: Analyser structure empirique
  - **Output**: Ajouter à VND_MASTER_REFERENCE.md section "Type 0"

- [ ] **Dumper table variables @ 0x44ECCE**
  - Voir INDEX_ID runtime
  - Comprendre storage variables
  - **Action**: Utiliser debugger (x32dbg/OllyDbg)
  - **Output**: Ajouter à VND_MASTER_REFERENCE.md section "Table Variables"

- [ ] **Analyser handlers 1-4 (a,b,c,d)**
  - Trouver adresses dans switch table
  - Vérifier occurrences réelles
  - Désassembler si utilisés
  - **Output**: Mettre à jour VND_MASTER_REFERENCE.md

---

### Priorité Moyenne

- [ ] **Améliorer extraction opcodes**
  - Filtrer faux positifs (noms fichiers: "5n1.bmp")
  - Détecter path separators (\ /) avant nombre+lettre
  - Valider contexte (après runprj, scene, etc.)
  - **Action**: Modifier extract_opcodes_from_vnd_v2.py
  - **Output**: Mettre à jour VND_TOOLS_GUIDE.md

- [ ] **Analyser handlers 13-20 (m-t)**
  - Switch table → adresses
  - Vérifier si appelés
  - Désassembler si utilisés
  - **Output**: Mettre à jour VND_MASTER_REFERENCE.md

- [ ] **Créer VND parser v3**
  - Parser complet Type 0
  - Extraction opcodes inline
  - Export human-readable
  - **Action**: Nouveau script parser_v3.py
  - **Output**: Ajouter à VND_TOOLS_GUIDE.md

---

### Priorité Basse

- [ ] **Documenter records 2,3,21,38,105**
  - Tester parsing sur fichiers réels
  - Valider structures documentées
  - **Output**: Mettre à jour VND_MASTER_REFERENCE.md section "Records"

- [ ] **Analyser handlers 22-42**
  - Switch table → adresses
  - Identifier usage
  - **Output**: Mettre à jour VND_MASTER_REFERENCE.md

- [ ] **Créer VND decompiler**
  - VND → script lisible
  - Extraction complète médias
  - **Action**: Nouveau projet séparé
  - **Output**: Nouveau dossier tools/

---

## 🚧 Blocages Actuels

### 1. Type 0 Structure ⚠️

**Problème**: Champ LENGTH ne représente pas taille réelle

**Impact**: Parser ne peut pas lire records séquentiellement

**Solution possible**:
- Chercher prochain séparateur (01 00 00 00)
- Parsing empirique des métadonnées
- Analyse manuelle biblio.vnd et irland.vnd

**Priorité**: HAUTE

---

### 2. Handlers Non Utilisés 🤔

**Problème**: Beaucoup de handlers (1-4, 13-20, 22-42) semblent non utilisés

**Possibilités**:
- Deprecated (anciennes versions)
- Debug commands
- Features rares
- Switch table incomplet

**Action**: Vérifier switch table, chercher dans tous VND

**Priorité**: MOYENNE

---

### 3. Variable INDEX_ID Inconnue 📍

**Problème**: INDEX_ID nécessaire pour navigation INDEX ('i' suffix)

**Impact**: Ne peut pas calculer destinations exactes

**Solution**: Dump mémoire @ 0x44ECCE avec debugger

**Priorité**: HAUTE

---

## 📈 Métriques de Progrès

### Complétion par Catégorie

| Catégorie | Progression | Détails |
|-----------|-------------|---------|
| **Format VND** | ████████░░ 80% | Header/variables OK, Type 0 partiel |
| **Opcodes** | ███████░░░ 70% | Système compris, 13/43 analysés |
| **Handlers** | ███░░░░░░░ 30% | 13 analysés, 30 restants |
| **Records** | ██████░░░░ 60% | Types documentés, parsing partiel |
| **Navigation** | █████████░ 90% | Système géographique compris |
| **Médias** | ████████░░ 80% | Images/audio/vidéo bien compris |
| **Logic** | ███████░░░ 70% | if/then compris, handler analysé |
| **Tools** | ████████░░ 80% | Parsers OK, batch OK, amélioration possible |

**Global**: ████████░░ 75%

---

### Historique Progression

#### 2026-01-16 AM (Phase 1)
- ✅ VND parser v2 créé
- ✅ Système opcodes décodé (atol parsing)
- ✅ 108 opcodes extraits (couleurs1.vnd)
- ✅ 7 handlers analysés (f,u,h,i,j,k,l)
- ✅ Navigation géographique identifiée
- **Progression**: 0% → 50%

#### 2026-01-16 PM (Phase 2)
- ✅ 19 fichiers VND récupérés
- ✅ Batch analysis (1461 opcodes total)
- ✅ Handler 'g' découvert (nouveau!)
- ✅ False positive 'n' identifié
- ✅ Patterns validés sur dataset complet
- ✅ Documentation centralisée (3 docs)
- **Progression**: 50% → 70%

---

## 🎓 Leçons Apprises

### 1. Éviter Fragmentation Documentation ✅

**Problème initial**: 20+ documents séparés créés

**Solution**: 3 documents centralisés:
- VND_MASTER_REFERENCE.md (référence complète)
- VND_TOOLS_GUIDE.md (guide outils)
- VND_PROGRESS.md (ce fichier - état/todo)

**Règle**: **Mettre à jour documents existants, pas créer nouveaux**

---

### 2. Batch Analysis Essentiel 📊

**Single file** (couleurs1.vnd): Patterns identifiés

**Batch files** (19 VND): Patterns **validés**

**Résultat**: Confiance que patterns sont systémiques

**Leçon**: Toujours valider sur dataset complet

---

### 3. False Positives dans Regex ⚠️

**Pattern**: `\d+[a-z]` trouve opcodes

**Problème**: Aussi noms fichiers ("5n1.bmp")

**Leçon**: Toujours vérifier contexte, pas juste pattern

**Solution future**: Améliorer heuristiques extraction

---

### 4. C++ Polymorphism Partout 🎯

**Handlers** → Pas de calls directs

**Tout via vtables**: `call dword ptr [ecx+offset]`

**Leçon**: Fonctions documentées ≠ appels visibles

**Implication**: Analyse statique limitée, besoin runtime

---

## 🔄 Workflow Recommandé

### Découverte Nouveau Handler

1. **Trouver occurrences**
   ```bash
   python3 batch_extract_opcodes.py | grep "'X'"
   ```

2. **Trouver adresse**
   ```bash
   python3 extract_opcode_table.py | grep "'X'"
   ```

3. **Analyser contextes**
   ```bash
   python3 extract_opcodes_from_vnd_v2.py fichier.vnd | grep "X ("
   ```

4. **Désassembler**
   - Copier analyze_handler_g.py
   - Modifier adresse
   - Exécuter

5. **Documenter**
   - **Mettre à jour VND_MASTER_REFERENCE.md**
   - Section "Handlers Analysés"
   - **NE PAS** créer nouveau doc

---

### Analyse Nouveau Fichier VND

1. **Parser**
   ```bash
   python3 vnd_parser_v2.py nouveau.vnd
   ```

2. **Extraire opcodes**
   ```bash
   python3 extract_opcodes_from_vnd_v2.py nouveau.vnd
   ```

3. **Comparer**
   - Nouveaux opcodes?
   - Patterns différents?

4. **Documenter SI nouveauté**
   - **Mettre à jour VND_MASTER_REFERENCE.md**
   - Section "Fichiers VND Analysés"

---

## 🎯 Objectifs Session Suivante

### Objectif 1: Compléter Handler 'e'

- [ ] Désassembler @ 0x004318EE
- [ ] Identifier fonction
- [ ] Tester avec holl.vnd (4 occurrences)
- [ ] Documenter dans VND_MASTER_REFERENCE.md

**Temps estimé**: 30 min

---

### Objectif 2: Parser Type 0 Complet

- [ ] Analyser biblio.vnd structure
- [ ] Identifier sections métadonnées
- [ ] Parser audio/images/scripts
- [ ] Documenter format

**Temps estimé**: 2 heures

---

### Objectif 3: Analyser Handlers 1-4

- [ ] Switch table → adresses
- [ ] Chercher occurrences
- [ ] Désassembler si utilisés
- [ ] Documenter

**Temps estimé**: 1 heure

---

## 📝 Notes

### Fichiers À Nettoyer (Optionnel)

**Documents obsolètes** (remplacés par 3 centraux):
- SESSION_SUMMARY.md
- OPCODE_USAGE_MAPPING.md
- OPCODES_SYSTEM_COMPLETE.md
- BATCH_VND_ANALYSIS_RESULTS.md
- FINAL_SESSION_SUMMARY_EXTENDED.md

**Action**: Garder pour historique OU supprimer après review

**Priorité**: BASSE

---

### Branches Git

**Branche actuelle**: claude/setup-reverse-engineering-tools-qRw7d

**État**: Clean, tous commits pushed

**Fichiers centraux**:
- ✅ VND_MASTER_REFERENCE.md
- ✅ VND_TOOLS_GUIDE.md
- ✅ VND_PROGRESS.md

---

## ✅ Checklist Avant Nouvelle Session

- [ ] Lire VND_PROGRESS.md (ce fichier)
- [ ] Review VND_MASTER_REFERENCE.md (derniers handlers)
- [ ] Check TODOs actifs ci-dessus
- [ ] git pull (nouveaux fichiers?)
- [ ] Priorité: Handler 'e' (5)

---

**Maintenu par**: Claude Code Analysis
**Dernière mise à jour**: 2026-01-16
**Prochaine session**: Continuer avec handler 'e' + Type 0

> ⚠️ **RAPPEL**: Mettre à jour CE FICHIER pour todo/progress, pas créer nouveau!
