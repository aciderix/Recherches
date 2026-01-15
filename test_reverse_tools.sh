#!/bin/bash

# Script de test pour vérifier l'installation des outils de rétro-ingénierie
# Test Reverse Engineering Tools Installation

echo "=========================================="
echo "Test des outils de rétro-ingénierie"
echo "=========================================="
echo ""

# Couleurs pour l'affichage
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

test_command() {
    local cmd=$1
    local name=$2

    if command -v "$cmd" &> /dev/null; then
        echo -e "${GREEN}✓${NC} $name: $(which $cmd)"
        $cmd --version 2>&1 | head -1 || $cmd -v 2>&1 | head -1 || echo "  Version info not available"
    else
        echo -e "${RED}✗${NC} $name: Not found"
    fi
    echo ""
}

test_python_module() {
    local module=$1
    local name=$2

    if python3 -c "import $module" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} Python: $name"
        python3 -c "import $module; print('  Version:', getattr($module, '__version__', 'N/A'))" 2>/dev/null || echo "  Installed"
    else
        echo -e "${RED}✗${NC} Python: $name - Not found"
    fi
    echo ""
}

echo "=== Outils principaux ==="
test_command "r2" "Radare2"
test_command "gdb" "GDB"
test_command "gdb-multiarch" "GDB Multiarch"

echo "=== Outils d'analyse binaire ==="
test_command "objdump" "objdump (binutils)"
test_command "readelf" "readelf (binutils)"
test_command "strings" "strings"
test_command "nm" "nm"
test_command "hexedit" "hexedit"
test_command "xxd" "xxd"
test_command "file" "file"
test_command "binwalk" "binwalk"
test_command "foremost" "foremost"

echo "=== Outils de traçage ==="
test_command "strace" "strace"
test_command "ltrace" "ltrace"

echo "=== Outils ELF ==="
test_command "eu-readelf" "elfutils readelf"
test_command "patchelf" "patchelf"

echo "=== Outils Python ==="
test_python_module "pwn" "pwntools"
test_python_module "capstone" "capstone"
test_python_module "keystone" "keystone"
test_python_module "unicorn" "unicorn"
test_python_module "elftools" "pyelftools"
test_python_module "ropgadget" "ROPgadget"

echo "=== Test GEF pour GDB ==="
if [ -f ~/.gdbinit-gef.py ]; then
    echo -e "${GREEN}✓${NC} GEF installé: ~/.gdbinit-gef.py"
    echo "  Taille: $(stat -c%s ~/.gdbinit-gef.py) bytes"
else
    echo -e "${RED}✗${NC} GEF: Not found"
fi
echo ""

echo "=========================================="
echo "Test terminé!"
echo "=========================================="
