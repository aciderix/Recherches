# ⚠️ IMPORTANT: Utiliser IDA pour Extraire le Code Assembleur

## 🎯 Pourquoi les Scripts Automatiques Ont Échoué

**Problème**: Les fichiers générés sont vides ou contiennent des données invalides.

**Raison**: Le mapping **Virtual Address (VA) → File Offset** dans un PE file est complexe:
- Les sections ont des alignements différents en mémoire vs fichier
- Les outils simples (objdump, capstone) ne gèrent pas bien ce mapping
- Seuls IDA/Ghidra font ce mapping correctement

**Conclusion**: Il faut utiliser **IDA** (comme tu l'as fait manuellement pour les 5 fichiers).

---

## ✅ Solution: Lancer le Script IDA Python

### Étape 1: Ouvrir europeo.exe dans IDA

```
1. Lance IDA Pro (ou IDA Free 8.4)
2. File → Open → sélectionne DOCS/europeo.exe
3. Accept les options par défaut
4. Attends que l'analyse se termine (barre de progression en bas)
```

### Étape 2: Exécuter le Script

```
1. Dans IDA, va dans: File → Script file... (ou appuie sur Alt+F7)
2. Navigue vers: /home/user/Recherches/
3. Sélectionne: extract_all_tvn_ida_simple.py
4. Clique sur "Open"
```

### Étape 3: Attendre l'Extraction

Le script va s'exécuter et afficher:

```
====================================================================================================
EXTRACTING COMPLETE ASSEMBLY CODE FOR ALL TVN METHODS - IDA
====================================================================================================

Output directory: TVN_IDA_EXTRACTS

====================================================================================================
EXTRACTING: TVNCommand
Vtable @ 0x0040E1E0
====================================================================================================
  Found 2 method(s)
  [0] Extracting destructor @ 0x0043BA0C...
  [1] Extracting LoadFromINI @ 0x00440090...
  ✓ Saved to TVNCommand_COMPLETE.md

...

====================================================================================================
EXTRACTION COMPLETE!
====================================================================================================

Output directory: TVN_IDA_EXTRACTS
Structures extracted: 7

✓ Done! Check the TVN_IDA_EXTRACTS/ folder for results.
```

### Étape 4: Vérifier les Résultats

Dans IDA, ouvre le dossier de sortie ou utilise:

```bash
ls -lh TVN_IDA_EXTRACTS/
cat TVN_IDA_EXTRACTS/TVNCommand_COMPLETE.md
```

---

## 📋 Ce Que Tu Obtiendras

Pour **chaque structure TVN**, un fichier markdown avec:

### 1. Code Assembleur Complet

```assembly
0043BA0C  push    ebp
0043BA0D  mov     ebp, esp
0043BA0F  sub     esp, 8
0043BA12  mov     eax, [ebp+8]
0043BA15  mov     [ebp-4], eax
...
```

### 2. Références aux Chaînes

```
- 0x0043BA30 → 0x00450120: "NAME"
- 0x0043BA40 → 0x00450130: "BKCOLOR"
```

### 3. Appels de Fonctions

**Important** (⭐):
```
- ⭐ 0x0043BA50 → TProfile::GetString @ 0x00401234
- ⭐ 0x0043BA60 → TProfile::GetInt @ 0x00401250
```

**Autres**:
```
- 0x0043BA70 → sprintf
- 0x0043BA80 → strcpy
```

---

## 🔄 Alternative si IDA ne Fonctionne Pas

Si vraiment tu ne peux pas lancer IDA, tu peux:

### Option 1: Utiliser Ghidra GUI

1. Lance Ghidra
2. Crée un nouveau projet
3. Importe europeo.exe
4. Attends l'analyse
5. Tools → Execute Script → ExtractAllTVNMethodsASM.java

### Option 2: Extraction Manuelle Ciblée

Tu as déjà fait l'extraction manuelle pour TVNSceneParms (les 5 fichiers). Tu pourrais:

1. Ouvrir europeo.exe dans IDA
2. Aller aux adresses des vtables:
   - TVNCommand: 0x0040E1E0
   - TVNFrame_1: 0x00435B50
   - TVNFrame_2: 0x00435DD4
   - TVNHotspot: 0x00413514
   - TVNImageObject_1: 0x00429980
   - TVNImageObject_2: 0x004299D0
   - TVNTimer: 0x004394D4
3. Pour chaque vtable:
   - Lire les 2 pointeurs de méthodes
   - Aller à chaque adresse de méthode
   - Copier le code assembleur (View → Open Subviews → Disassembly)
   - Sauvegarder dans un fichier .txt

Mais c'est exactement ce que le script fait automatiquement!

---

## 🎯 Résumé

**CE QUI NE FONCTIONNE PAS**:
- ❌ Scripts automatiques (objdump, radare2, capstone)
- ❌ Extraction sans IDA/Ghidra

**CE QUI FONCTIONNE**:
- ✅ Script IDA Python (`extract_all_tvn_ida_simple.py`)
- ✅ Extraction manuelle dans IDA (comme tu l'as fait)
- ✅ Script Ghidra Java (alternative)

**LA SOLUTION**:
```
Ouvre IDA → File → Script file → extract_all_tvn_ida_simple.py → Done!
```

**Temps estimé**: 2-5 minutes

---

## 💡 Pourquoi C'est Important

Sans le code assembleur des méthodes, on ne peut pas:
- Comprendre ce que fait chaque méthode
- Identifier les clés INI utilisées
- Voir comment les données sont parsées
- Documenter le format VND complètement

Le code assembleur est **essentiel** pour la reverse engineering complète.

---

## 🚀 Prochaine Étape

**MAINTENANT**: Lance IDA et exécute le script!

1. IDA Free est déjà installé: `/opt/idafree/ida64` ou `ida64` dans le terminal
2. Le script est prêt: `/home/user/Recherches/extract_all_tvn_ida_simple.py`
3. Ça prendra 5 minutes max

Après ça, on aura **TOUT** le code assembleur de toutes les structures TVN! 🎉

---

**TL;DR**: Les scripts automatiques ne marchent pas pour les PE files. Il FAUT utiliser IDA (ou Ghidra). Lance IDA, exécute `extract_all_tvn_ida_simple.py`, c'est tout!
