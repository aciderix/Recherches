// Extract ALL vtables and methods from ALL 35 TVN structures
//@category TVN.Analysis

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.*;
import ghidra.program.model.mem.*;
import java.io.*;
import java.util.*;

public class ExtractTVNVtables extends GhidraScript {

    // All 35 TVN structures with their known vtable offsets
    private static final Map<String, Long> TVN_VTABLES = new LinkedHashMap<>();
    static {
        // From VND_CRITICAL_NOTES.md
        TVN_VTABLES.put("TVNProjectParms", 0x0040EC02L);
        TVN_VTABLES.put("TVNMidiParms", 0x0040EC20L);
        TVN_VTABLES.put("TVNDigitParms", 0x0040EC3BL);
        TVN_VTABLES.put("TVNHtmlParms", 0x0040EC57L);
        TVN_VTABLES.put("TVNImageParms", 0x0040EC72L);
        TVN_VTABLES.put("TVNImgObjParms", 0x0040EC8EL);
        TVN_VTABLES.put("TVNImgSeqParms", 0x0040ECABL);
        TVN_VTABLES.put("TVNExecParms", 0x0040ECC8L);
        TVN_VTABLES.put("TVNSetVarParms", 0x0040ECE3L);
        TVN_VTABLES.put("TVNIfParms", 0x0040ED00L);
        TVN_VTABLES.put("TVNTextParms", 0x0040ED75L);
        TVN_VTABLES.put("TVNTextObjParms", 0x0040ED90L);
        TVN_VTABLES.put("TVNFontParms", 0x0040EDAEL);
        TVN_VTABLES.put("TVNCommand", 0x0040EDC9L);
        TVN_VTABLES.put("TVNSceneParms", 0x0040EDFEL);
        TVN_VTABLES.put("TVNStringParms", 0x0040EE1AL);
    }

    // Additional structures - need to search for vtables
    private static final String[] TVN_STRINGS = {
        "TVNFileNameParms",
        "TVNEventCommand",
        "TVNVariable",
        "TVNScene",
        "TVNHotspot",
        "TVNTimer",
        "TVNWaveMedia",
        "TVNMidiMedia",
        "TVNBitmap",
        "TVNGdiObject",
        "TVNHtmlText",
        "TVNImageObject",
        "TVNTextObject",
        "TVNBmpImg",
        "TVNToolBar",
        "TVNWindow",
        "TVNCDAMedia",
        "TVNAviMedia",
        "TVNFrame",
        "TVNApplication"
    };

    private Map<String, StructureInfo> results = new TreeMap<>();

    public void run() throws Exception {
        println("="*100);
        println("EXTRACTING ALL TVN VTABLES AND METHODS - GHIDRA ANALYSIS");
        println("="*100);
        println("");

        // Phase 1: Extract known vtables
        println("\n" + "=".repeat(100));
        println("PHASE 1: Known Vtable Offsets");
        println("=".repeat(100));

        for (Map.Entry<String, Long> entry : TVN_VTABLES.entrySet()) {
            String structName = entry.getKey();
            long vtableAddr = entry.getValue();

            StructureInfo info = extractVtableAtOffset(vtableAddr, structName);
            if (info != null) {
                results.put(structName, info);
            }
        }

        // Phase 2: Search for additional vtables
        println("\n" + "=".repeat(100));
        println("PHASE 2: Searching for Additional Vtables");
        println("=".repeat(100));

        for (String structName : TVN_STRINGS) {
            println("\nSearching for " + structName + "...");
            Long vtableAddr = findVtableNearString(structName);

            if (vtableAddr != null) {
                StructureInfo info = extractVtableAtOffset(vtableAddr, structName);
                if (info != null) {
                    results.put(structName, info);
                }
            } else {
                println("  Could not locate vtable for " + structName);
            }
        }

        // Save results
        saveResultsToMarkdown();

        println("\n" + "=".repeat(100));
        println("EXTRACTION COMPLETE");
        println("=".repeat(100));
        println("\nExtracted " + results.size() + " structures");
        int totalMethods = 0;
        for (StructureInfo info : results.values()) {
            totalMethods += info.methods.size();
        }
        println("Total methods: " + totalMethods);
    }

    private boolean isValidCodePointer(Address addr) {
        if (addr == null) {
            return false;
        }

        long offset = addr.getOffset();

        // Check if in valid code range for europeo.exe
        if (offset < 0x00401000L || offset > 0x00500000L) {
            return false;
        }

        // Check if it's a function
        Function func = getFunctionAt(addr);
        if (func != null) {
            return true;
        }

        // Check if there's an instruction
        Instruction instr = getInstructionAt(addr);
        if (instr != null) {
            return true;
        }

        return false;
    }

    private StructureInfo extractVtableAtOffset(long vtableAddr, String structName) {
        println("\n" + "=".repeat(100));
        println(String.format("Extracting vtable for %s @ 0x%08X", structName, vtableAddr));
        println("=".repeat(100));

        Address addr = toAddr(vtableAddr);
        List<MethodInfo> methods = new ArrayList<>();
        int offset = 0;

        while (offset < 0x100) {  // Max 64 methods
            Address methodPtrAddr = addr.add(offset);

            int methodPtrValue;
            try {
                methodPtrValue = getInt(methodPtrAddr);
            } catch (MemoryAccessException e) {
                println(String.format("  [0x%02X] Memory access error, ending", offset));
                break;
            }

            if (methodPtrValue == 0) {
                println(String.format("  [0x%02X] NULL - end of vtable", offset));
                break;
            }

            Address methodAddr = toAddr(methodPtrValue);

            if (!isValidCodePointer(methodAddr)) {
                if (offset == 0) {
                    println("  ERROR: First entry is not a valid code pointer!");
                    return null;
                } else {
                    println(String.format("  [0x%02X] 0x%08X - invalid, ending", offset, methodPtrValue));
                    break;
                }
            }

            // Get function info
            Function func = getFunctionAt(methodAddr);
            String funcName;
            int funcSize = 0;
            String role;

            if (func != null) {
                funcName = func.getName();
                funcSize = (int) func.getBody().getNumAddresses();
                role = identifyMethodRole(funcName, offset / 4, funcSize);
            } else {
                funcName = String.format("sub_%X", methodPtrValue);
                role = "Unknown";
            }

            println(String.format("  [0x%02X] 0x%08X  %-30s  %-25s  size=%d",
                offset, methodPtrValue, funcName, role, funcSize));

            methods.add(new MethodInfo(offset, methodPtrValue, funcName, role, funcSize));
            offset += 4;
        }

        println("\nTotal methods found: " + methods.size());

        if (methods.isEmpty()) {
            return null;
        }

        return new StructureInfo(structName, vtableAddr, methods);
    }

    private String identifyMethodRole(String funcName, int methodIndex, int funcSize) {
        String nameLower = funcName.toLowerCase();

        // Name-based detection
        if (nameLower.contains("destructor") || nameLower.contains("dtor")) {
            return "Destructor";
        }
        if (nameLower.contains("constructor") || nameLower.contains("ctor")) {
            return "Constructor";
        }
        if (nameLower.contains("load")) {
            return "Load/Parse";
        }
        if (nameLower.contains("save")) {
            return "Save/Serialize";
        }
        if (nameLower.contains("execute") || nameLower.contains("exec")) {
            return "Execute";
        }
        if (nameLower.contains("release") || nameLower.contains("free")) {
            return "Release/Cleanup";
        }
        if (nameLower.contains("init")) {
            return "Initialize";
        }
        if (nameLower.contains("parse")) {
            return "Parse";
        }
        if (nameLower.contains("clone") || nameLower.contains("copy")) {
            return "Clone/Copy";
        }

        // Index-based detection
        if (methodIndex == 0) {
            return "Virtual[0] - Likely Destructor";
        } else if (methodIndex == 1) {
            return "Virtual[1]";
        }

        // Size-based detection
        if (funcSize > 0) {
            if (funcSize < 10) {
                return "Getter/Setter";
            } else if (funcSize > 500) {
                return "Complex Logic";
            }
        }

        return String.format("Method[%d]", methodIndex);
    }

    private Long findVtableNearString(String structName) {
        String searchStr = structName + " *";

        // Search for string
        Address foundAddr = find(searchStr);

        if (foundAddr == null) {
            println("  Warning: String '" + searchStr + "' not found for " + structName);
            return null;
        }

        println(String.format("  Found type string at 0x%08X", foundAddr.getOffset()));

        // Search backwards for vtable (up to 0x200 bytes)
        for (int i = 0; i < 0x200; i += 4) {
            Address checkAddr = foundAddr.subtract(i);

            int firstPtrValue;
            try {
                firstPtrValue = getInt(checkAddr);
            } catch (MemoryAccessException e) {
                continue;
            }

            Address firstPtr = toAddr(firstPtrValue);

            if (isValidCodePointer(firstPtr)) {
                // Check for consecutive code pointers
                int consecutive = 1;
                for (int j = 1; j < 10; j++) {
                    Address nextAddr = checkAddr.add(j * 4);
                    int nextPtrValue;
                    try {
                        nextPtrValue = getInt(nextAddr);
                    } catch (MemoryAccessException e) {
                        break;
                    }

                    Address nextPtr = toAddr(nextPtrValue);
                    if (isValidCodePointer(nextPtr)) {
                        consecutive++;
                    } else {
                        break;
                    }
                }

                if (consecutive >= 3) {
                    long vtableOffset = checkAddr.getOffset();
                    println(String.format("  Possible vtable found at 0x%08X (%d methods)",
                        vtableOffset, consecutive));
                    return vtableOffset;
                }
            }
        }

        return null;
    }

    private void saveResultsToMarkdown() throws IOException {
        File outputFile = new File("/home/user/Recherches/TVN_ALL_METHODS_GHIDRA.md");

        try (PrintWriter writer = new PrintWriter(new FileWriter(outputFile))) {
            writer.println("# Complete TVN Methods Extraction - Ghidra Analysis\n");
            writer.println("Comprehensive extraction of all vtables and methods from 35 TVN structures.\n");
            writer.println("**Tool**: Ghidra 12.0.1 Headless Analyzer");
            writer.println("**Binary**: DOCS/europeo.exe");
            writer.println("**Date**: 2026-01-16\n");
            writer.println("---\n");

            // Summary
            writer.println("## Summary\n");
            writer.println("| Structure | Vtable Address | Methods Count |");
            writer.println("|-----------|----------------|---------------|");

            int totalMethods = 0;
            for (StructureInfo info : results.values()) {
                int methodCount = info.methods.size();
                totalMethods += methodCount;
                writer.println(String.format("| %-30s | 0x%08X | %3d |",
                    info.name, info.vtableAddress, methodCount));
            }

            writer.println(String.format("\n**Total**: %d structures, %d methods\n",
                results.size(), totalMethods));
            writer.println("---\n");

            // Detailed methods
            writer.println("## Detailed Methods\n");

            for (StructureInfo info : results.values()) {
                writer.println("### " + info.name + "\n");
                writer.println(String.format("**Vtable**: 0x%08X", info.vtableAddress));
                writer.println(String.format("**Methods**: %d\n", info.methods.size()));

                writer.println("| Offset | Address | Function | Role | Size |");
                writer.println("|--------|---------|----------|------|------|");

                for (MethodInfo method : info.methods) {
                    writer.println(String.format("| +0x%02X | 0x%08X | %-30s | %-25s | %5d |",
                        method.offset, method.address, method.name, method.role, method.size));
                }

                writer.println("\n---\n");
            }
        }

        println("\n✓ Results saved to " + outputFile.getAbsolutePath());
    }

    // Helper classes
    private static class StructureInfo {
        String name;
        long vtableAddress;
        List<MethodInfo> methods;

        StructureInfo(String name, long vtableAddress, List<MethodInfo> methods) {
            this.name = name;
            this.vtableAddress = vtableAddress;
            this.methods = methods;
        }
    }

    private static class MethodInfo {
        int offset;
        int address;
        String name;
        String role;
        int size;

        MethodInfo(int offset, int address, String name, String role, int size) {
            this.offset = offset;
            this.address = address;
            this.name = name;
            this.role = role;
            this.size = size;
        }
    }
}
