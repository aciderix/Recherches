# VND Reverse Engineering - Documentation Centralisée

**Projet**: Analyse format VND (Visual Novel Europeo)
**Status**: 75% complété
**Date**: 2026-01-16

---

## 📚 Documentation Principale (3 fichiers)

### 1. [VND_MASTER_REFERENCE.md](./VND_MASTER_REFERENCE.md) ⭐

**Référence technique complète**:
- Format VND (header, variables, records)
- Système d'opcodes (a-z)
- Handlers analysés (13/43)
- Patterns d'usage
- Fichiers analysés (19 VND)
- Références techniques

**Quand utiliser**: Pour comprendre le format, chercher info handler, voir patterns

---

### 2. [VND_TOOLS_GUIDE.md](./VND_TOOLS_GUIDE.md) 🛠️

**Guide d'utilisation des outils**:
- Parsers VND (vnd_parser_v2.py, etc.)
- Extracteurs opcodes (batch, single file)
- Analyseurs handlers
- Workflows recommandés
- FAQ

**Quand utiliser**: Pour utiliser les scripts, chercher comment parser un fichier

---

### 3. [VND_PROGRESS.md](./VND_PROGRESS.md) 📊

**État de la recherche**:
- Handlers analysés vs restants (13/43)
- TODO actif (priorités)
- Blocages actuels
- Métriques progression
- Historique

**Quand utiliser**: Pour savoir où on en est, quoi faire ensuite, voir blocages

---

## 🚀 Quick Start

### Analyser un fichier VND

```bash
# 1. Parser le fichier
python3 vnd_parser_v2.py fichier.vnd

# 2. Extraire opcodes
python3 extract_opcodes_from_vnd_v2.py fichier.vnd
```

### Analyser tous les fichiers (batch)

```bash
# Statistiques globales
python3 test_batch_vnd_parser.py

# Opcodes de tous fichiers + comparaison
python3 batch_extract_opcodes.py
```

### Analyser un handler

```bash
# 1. Trouver adresse
python3 extract_opcode_table.py | grep "'X'"

# 2. Analyser (adapter script existant)
python3 analyze_handler_X.py
```

---

## 📁 Structure Projet

```
/home/user/Recherches/
├── README_VND.md                    ← CE FICHIER
├── VND_MASTER_REFERENCE.md          ← Documentation technique
├── VND_TOOLS_GUIDE.md               ← Guide outils
├── VND_PROGRESS.md                  ← État/TODO
│
├── Vnd-vnp/                         ← 19 fichiers VND
│   ├── angleterre.vnd (85KB)
│   ├── france.vnd (98KB)
│   ├── biblio.vnd (138KB)
│   └── ... (16 autres)
│
├── DOCS/                            ← Documentation extraite
│   ├── europeo.exe                  ← Binaire analysé
│   └── documentation_VND_Europeo.zip
│
├── vnd_parser_v2.py                 ← Parser VND (recommandé)
├── extract_opcodes_from_vnd_v2.py   ← Extraction opcodes
├── batch_extract_opcodes.py         ← Batch analysis
├── test_batch_vnd_parser.py         ← Test rapide
│
├── analyze_handler_*.py             ← Analyseurs handlers
├── extract_opcode_table.py          ← Switch table
│
└── (autres fichiers...)
```

---

## 🎯 État Actuel

### Complété ✅

- ✅ Format VND compris (header, variables, records)
- ✅ Système opcodes décodé (atol parsing, dispatcher)
- ✅ 19 fichiers analysés (1.2MB, 1461 opcodes)
- ✅ 13 handlers analysés (a, b, c, d, e, f, g, h, i, j, k, l, u)
- ✅ Navigation géographique identifiée
- ✅ Patterns validés sur dataset complet
- ✅ Tools créés (parsers, extracteurs, analyseurs)
- ✅ Documentation centralisée (3 docs)

### En Cours ⏳

- ⏳ Type 0 parsing complet (structure complexe)
- ⏳ 30 handlers restants (13-20, 22-42)

### Blocages ⚠️

- ⚠️ Type 0 LENGTH non fiable (chercher séparateur)
- ⚠️ INDEX_ID variable inconnue (dump mémoire requis)
- ⚠️ Handlers inconnus (switch table à analyser)

---

## 🎓 Découvertes Majeures

### 1. Système atol() Parsing

**Clé du système**:
```c
number = atol(string);  // Lit chiffres
opcode = next_char;     // Lettre = opcode
```

Exemple: `"54h"` → number=54, opcode='h' (tooltip)

---

### 2. Handler 'g' Découvert

**Nouveau handler** trouvé via batch analysis (19 fichiers)

- 44 occurrences
- Pattern: `runprj couleurs1.vnp 54g`
- Appels identiques à handler 'h' (tooltip)
- **Hypothèse**: Variante tooltip

---

### 3. False Positive 'n'

**144 occurrences** mais **pas un vrai opcode**!

Réalité: Noms de fichiers
```
addbmp photos\5n1.bmp
              ^^^ filename, not opcode
```

Leçon: Vérifier contexte, pas juste pattern

---

### 4. Navigation Géographique

**19 pays européens** avec navigation:
```
angleterre.vnp 69d  → England scene 69
france.vnp 27j      → France + bitmap 27
ecosse.vnp 33d      → Scotland scene 33
```

Système éducatif sur géographie européenne

---

## 📊 Métriques

| Métrique | Valeur |
|----------|--------|
| **Fichiers VND** | 19 (1.2 MB) |
| **Opcodes extraits** | 1461 total |
| **Opcodes uniques** | 11 |
| **Handlers analysés** | 13/43 (30.2%) |
| **Formats compris** | 75% |
| **Tools créés** | 20+ scripts |
| **Documentation** | 3 docs centraux |
| **Complétion globale** | 75% |

---

## 🔗 Liens Rapides

**Chercher info handler**:
→ [VND_MASTER_REFERENCE.md#handlers-analysés](./VND_MASTER_REFERENCE.md#handlers-analysés)

**Utiliser parser**:
→ [VND_TOOLS_GUIDE.md#parsers-vnd](./VND_TOOLS_GUIDE.md#parsers-vnd)

**Voir TODO**:
→ [VND_PROGRESS.md#todo-actif](./VND_PROGRESS.md#todo-actif)

**Workflow analyse**:
→ [VND_TOOLS_GUIDE.md#workflow-recommandé](./VND_TOOLS_GUIDE.md#workflow-recommandé)

**Progression**:
→ [VND_PROGRESS.md#métriques-de-progrès](./VND_PROGRESS.md#métriques-de-progrès)

---

## ⚠️ Règles Importantes

### 1. Documentation Centralisée

**✅ FAIRE**: Mettre à jour un des 3 docs principaux

**❌ NE PAS**: Créer nouveau document séparé

**Exception**: Tools nouveaux → ajouter à VND_TOOLS_GUIDE.md

---

### 2. Découverte Nouveau Handler

**Workflow**:
1. Identifier dans batch_extract_opcodes.py
2. Vérifier switch table (extract_opcode_table.py)
3. Analyser (copier analyze_handler_g.py)
4. **Mettre à jour VND_MASTER_REFERENCE.md**

**PAS de nouveau fichier HANDLER_X_ANALYSIS.md !**

---

### 3. TODO Management

**✅ FAIRE**: Mettre à jour VND_PROGRESS.md

**❌ NE PAS**: Créer TODO_SESSION_X.md

---

## 🛠️ Dépendances

**Python 3.x** + capstone:
```bash
pip install capstone
```

**Fichiers requis**:
- DOCS/europeo.exe (binaire)
- Vnd-vnp/*.vnd (19 fichiers)

---

## 📝 Maintenance

**Mettre à jour documentation**:
1. Nouvelle découverte → VND_MASTER_REFERENCE.md
2. Nouvel outil → VND_TOOLS_GUIDE.md
3. Nouveau TODO → VND_PROGRESS.md

**Git workflow**:
```bash
# Après modification docs
git add VND_*.md README_VND.md
git commit -m "DOC: Brief description"
git push
```

---

## 🎯 Prochaines Étapes

**Voir**: [VND_PROGRESS.md#todo-actif](./VND_PROGRESS.md#todo-actif)

**Priorités**:
1. Handler 'e' (5) - 35 occurrences
2. Type 0 parsing complet
3. Dump table variables @ 0x44ECCE
4. Handlers 1-4 (a,b,c,d)

---

**Projet**: VND Reverse Engineering
**Maintenu par**: Claude Code Analysis
**Branche**: claude/setup-reverse-engineering-tools-qRw7d
**Status**: ✅ Clean, committed, pushed

> 📚 Commencez par lire [VND_MASTER_REFERENCE.md](./VND_MASTER_REFERENCE.md) pour la référence complète!
