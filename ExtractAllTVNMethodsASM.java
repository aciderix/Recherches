// Extract complete assembly code for ALL TVN methods (all 35 structures)
// One markdown file per TVN structure
//@category TVN.Analysis

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.*;
import ghidra.program.model.mem.*;
import ghidra.program.model.symbol.*;
import ghidra.program.model.scalar.Scalar;
import java.io.*;
import java.util.*;

public class ExtractAllTVNMethodsASM extends GhidraScript {

    // All 35 TVN structures with their vtable addresses
    private static final Map<String, Long> TVN_VTABLES = new LinkedHashMap<>();
    static {
        // From previous extraction
        TVN_VTABLES.put("TVNCommand", 0x0040E1E0L);
        TVN_VTABLES.put("TVNDigitParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNExecParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNFontParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNHtmlParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNIfParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNImageParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNImgObjParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNImgSeqParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNMidiParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNProjectParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNSceneParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNSetVarParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNStringParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNTextObjParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNTextParms", 0x0040E1E0L);
        TVN_VTABLES.put("TVNFrame_1", 0x00435B50L);
        TVN_VTABLES.put("TVNFrame_2", 0x00435DD4L);
        TVN_VTABLES.put("TVNHotspot", 0x00413514L);
        TVN_VTABLES.put("TVNImageObject_1", 0x00429980L);
        TVN_VTABLES.put("TVNImageObject_2", 0x004299D0L);
        TVN_VTABLES.put("TVNTimer", 0x004394D4L);
    }

    private PrintWriter currentWriter;
    private Set<Address> analyzedFunctions = new HashSet<>();

    public void run() throws Exception {
        println("="*100);
        println("EXTRACTING COMPLETE ASSEMBLY CODE FOR ALL TVN METHODS");
        println("="*100);
        println();

        // Wait for auto-analysis
        println("Waiting for analysis...");
        analyzeAll(currentProgram);
        println("Analysis complete.\n");

        // Create output directory
        File outputDir = new File("/home/user/Recherches/TVN_ASM_EXTRACTS");
        if (!outputDir.exists()) {
            outputDir.mkdirs();
            println("Created output directory: " + outputDir.getAbsolutePath());
        }

        // Extract each TVN structure
        for (Map.Entry<String, Long> entry : TVN_VTABLES.entrySet()) {
            String structName = entry.getKey();
            long vtableAddr = entry.getValue();

            extractTVNStructure(structName, vtableAddr, outputDir);
        }

        println("\n" + "=".repeat(100));
        println("EXTRACTION COMPLETE");
        println("="*100);
        println("\nOutput directory: " + outputDir.getAbsolutePath());
    }

    private void extractTVNStructure(String structName, long vtableAddr, File outputDir) throws Exception {
        println("\n" + "=".repeat(100));
        println("EXTRACTING: " + structName);
        println("Vtable @ 0x" + String.format("%08X", vtableAddr));
        println("=".repeat(100));

        File outputFile = new File(outputDir, structName + "_COMPLETE.md");
        currentWriter = new PrintWriter(new FileWriter(outputFile));

        // Write header
        writeHeader(structName, vtableAddr);

        // Extract all methods from vtable
        List<MethodInfo> methods = extractVtableMethods(vtableAddr);

        if (methods.isEmpty()) {
            currentWriter.println("\n⚠️ **No methods found in vtable**\n");
            currentWriter.close();
            println("  No methods found");
            return;
        }

        // Write summary
        writeSummary(methods);

        // Extract each method with full assembly
        for (int i = 0; i < methods.size(); i++) {
            MethodInfo method = methods.get(i);
            println("  [" + i + "] Extracting " + method.name + " @ 0x" +
                   String.format("%08X", method.address));

            extractMethodComplete(method, i);
        }

        currentWriter.close();
        println("  ✓ Saved to " + outputFile.getName());
    }

    private void writeHeader(String structName, long vtableAddr) {
        currentWriter.println("# " + structName + " - Complete Assembly Extraction");
        currentWriter.println();
        currentWriter.println("**Vtable Address**: 0x" + String.format("%08X", vtableAddr));
        currentWriter.println("**Binary**: europeo.exe");
        currentWriter.println("**Tool**: Ghidra 12.0.1");
        currentWriter.println("**Date**: 2026-01-16");
        currentWriter.println();
        currentWriter.println("---");
        currentWriter.println();
    }

    private void writeSummary(List<MethodInfo> methods) {
        currentWriter.println("## Methods Summary");
        currentWriter.println();
        currentWriter.println("| Index | Address | Name | Size |");
        currentWriter.println("|-------|---------|------|------|");

        for (int i = 0; i < methods.size(); i++) {
            MethodInfo method = methods.get(i);
            currentWriter.println(String.format("| %2d | 0x%08X | %s | %d bytes |",
                i, method.address, method.name, method.size));
        }

        currentWriter.println();
        currentWriter.println("---");
        currentWriter.println();
    }

    private List<MethodInfo> extractVtableMethods(long vtableAddr) throws MemoryAccessException {
        List<MethodInfo> methods = new ArrayList<>();
        Address addr = toAddr(vtableAddr);

        for (int offset = 0; offset < 0x40; offset += 4) {
            Address ptrAddr = addr.add(offset);
            int methodAddr = getInt(ptrAddr);

            if (methodAddr == 0) {
                break;
            }

            Address methodAddress = toAddr(methodAddr);
            if (!isValidCodePointer(methodAddress)) {
                if (offset == 0) {
                    break;
                }
                break;
            }

            Function func = getFunctionAt(methodAddress);
            String name = (func != null) ? func.getName() : "sub_" + String.format("%X", methodAddr);
            int size = (func != null) ? (int) func.getBody().getNumAddresses() : 0;

            methods.add(new MethodInfo(offset / 4, methodAddr, name, size));
        }

        return methods;
    }

    private void extractMethodComplete(MethodInfo method, int methodIndex) throws Exception {
        Address methodAddr = toAddr(method.address);
        Function func = getFunctionAt(methodAddr);

        currentWriter.println("## Method [" + methodIndex + "]: " + method.name);
        currentWriter.println();
        currentWriter.println("**Address**: 0x" + String.format("%08X", method.address));
        currentWriter.println("**Size**: " + method.size + " bytes");
        currentWriter.println();

        if (func == null) {
            currentWriter.println("⚠️ **Function not recognized by Ghidra**");
            currentWriter.println();
            return;
        }

        // Write function signature
        currentWriter.println("### Signature");
        currentWriter.println();
        currentWriter.println("```cpp");
        currentWriter.println(func.getSignature().getPrototypeString());
        currentWriter.println("```");
        currentWriter.println();

        // Extract complete assembly
        currentWriter.println("### Assembly Code");
        currentWriter.println();
        currentWriter.println("```assembly");

        InstructionIterator instructions = currentProgram.getListing().getInstructions(func.getBody(), true);
        List<String> asmLines = new ArrayList<>();
        Map<Address, String> comments = new HashMap<>();
        List<String> stringRefs = new ArrayList<>();
        List<String> functionCalls = new ArrayList<>();

        while (instructions.hasNext()) {
            Instruction instr = instructions.next();
            Address instrAddr = instr.getAddress();

            // Format: address  bytes  mnemonic operands
            String addrStr = String.format("%08X", instrAddr.getOffset());
            String instrStr = instr.toString();

            asmLines.add(addrStr + "  " + instrStr);

            // Extract string references
            for (int i = 0; i < instr.getNumOperands(); i++) {
                Reference[] refs = instr.getOperandReferences(i);
                for (Reference ref : refs) {
                    Address refAddr = ref.getToAddress();

                    // Check for string
                    Data data = getDataAt(refAddr);
                    if (data != null && data.hasStringValue()) {
                        String str = data.getDefaultValueRepresentation();
                        stringRefs.add(addrStr + " → " + str);
                        comments.put(instrAddr, "String: " + str);
                    }

                    // Check for function call
                    Function calledFunc = getFunctionAt(refAddr);
                    if (calledFunc != null) {
                        String callName = calledFunc.getName();
                        functionCalls.add(addrStr + " → " + callName);

                        // Highlight important calls
                        if (callName.contains("GetString") || callName.contains("GetInt") ||
                            callName.contains("Profile") || callName.contains("TProfile")) {
                            comments.put(instrAddr, "⚠️ IMPORTANT: " + callName);
                        }
                    }
                }
            }
        }

        // Write assembly with comments
        for (String line : asmLines) {
            Address lineAddr = toAddr(Long.parseLong(line.substring(0, 8), 16));
            currentWriter.print(line);

            if (comments.containsKey(lineAddr)) {
                currentWriter.print("    ; " + comments.get(lineAddr));
            }

            currentWriter.println();
        }

        currentWriter.println("```");
        currentWriter.println();

        // Write string references section
        if (!stringRefs.isEmpty()) {
            currentWriter.println("### String References");
            currentWriter.println();
            for (String ref : stringRefs) {
                currentWriter.println("- `" + ref + "`");
            }
            currentWriter.println();
        }

        // Write function calls section
        if (!functionCalls.isEmpty()) {
            currentWriter.println("### Function Calls");
            currentWriter.println();

            // Group by importance
            List<String> importantCalls = new ArrayList<>();
            List<String> otherCalls = new ArrayList<>();

            for (String call : functionCalls) {
                if (call.contains("GetString") || call.contains("GetInt") ||
                    call.contains("Profile")) {
                    importantCalls.add(call);
                } else {
                    otherCalls.add(call);
                }
            }

            if (!importantCalls.isEmpty()) {
                currentWriter.println("**Important Calls** (TProfile, GetString, etc.):");
                currentWriter.println();
                for (String call : importantCalls) {
                    currentWriter.println("- ⭐ `" + call + "`");
                }
                currentWriter.println();
            }

            if (!otherCalls.isEmpty()) {
                currentWriter.println("**Other Calls**:");
                currentWriter.println();
                for (String call : otherCalls) {
                    currentWriter.println("- `" + call + "`");
                }
                currentWriter.println();
            }
        }

        // Extract called functions recursively (depth 1)
        if (!functionCalls.isEmpty()) {
            currentWriter.println("### Called Functions Details");
            currentWriter.println();

            Set<Address> processed = new HashSet<>();

            for (String call : functionCalls) {
                if (call.contains("GetString") || call.contains("GetInt") || call.contains("Profile")) {
                    String funcName = call.split(" → ")[1];
                    Function calledFunc = getFunction(funcName);

                    if (calledFunc != null && !processed.contains(calledFunc.getEntryPoint())) {
                        processed.add(calledFunc.getEntryPoint());
                        extractCalledFunctionSummary(calledFunc);
                    }
                }
            }
        }

        currentWriter.println("---");
        currentWriter.println();
    }

    private void extractCalledFunctionSummary(Function func) {
        currentWriter.println("#### " + func.getName());
        currentWriter.println();
        currentWriter.println("**Address**: 0x" + String.format("%08X", func.getEntryPoint().getOffset()));
        currentWriter.println();
        currentWriter.println("```assembly");

        InstructionIterator instructions = currentProgram.getListing().getInstructions(func.getBody(), true);
        int lineCount = 0;

        while (instructions.hasNext() && lineCount < 50) {  // Limit to 50 lines
            Instruction instr = instructions.next();
            currentWriter.println(String.format("%08X  %s",
                instr.getAddress().getOffset(), instr.toString()));
            lineCount++;
        }

        if (instructions.hasNext()) {
            currentWriter.println("... (truncated)");
        }

        currentWriter.println("```");
        currentWriter.println();
    }

    private boolean isValidCodePointer(Address addr) {
        if (addr == null) return false;
        long offset = addr.getOffset();
        if (offset < 0x00401000L || offset > 0x00500000L) return false;

        Function func = getFunctionAt(addr);
        if (func != null) return true;

        Instruction instr = getInstructionAt(addr);
        return instr != null;
    }

    private static class MethodInfo {
        int index;
        int address;
        String name;
        int size;

        MethodInfo(int index, int address, String name, int size) {
            this.index = index;
            this.address = address;
            this.name = name;
            this.size = size;
        }
    }
}
