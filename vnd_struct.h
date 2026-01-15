// Structure hypothétique du format VND
// Basé sur l'analyse hex

#include <stdint.h>

// Header principal du fichier
struct VNDHeader {
    uint32_t magic;           // 0x00: 0x3A010100 ?
    uint8_t  unknown1;        // 0x04: 0x00

    // Strings avec longueur
    uint32_t vnfile_len;      // 0x05: 6
    char     vnfile[6];       // 0x09: "VNFILE"

    uint32_t version_len;     // 0x0F: 4
    char     version[5];      // 0x13: "2.136" (mais len=4?)
    uint8_t  padding[3];      // 0x18: 00 00 00

    uint32_t region_len;      // 0x1B: 7
    char     region[7];       // 0x1F: "Europeo"

    uint32_t company_len;     // 0x26: 16
    char     company[16];     // 0x2A: "Sopra Multimedia"

    uint32_t id_len;          // 0x3A: 8
    char     id[8];           // 0x3E: "5D51F233"

    uint32_t unknown2[2];     // 0x46: 00 00 00 00 00 00 00 00

    // Paramètres graphiques
    uint32_t width;           // 0x4E: 640 (0x280)
    uint32_t height;          // 0x52: 480 (0x1E0)
    uint32_t bits_per_pixel;  // 0x56: 16
    uint32_t unknown3;        // 0x5A: 1
    uint32_t unknown4;        // 0x5E: 1
    uint32_t unknown5;        // 0x62: 31 (0x1F)
    uint32_t unknown6;        // 0x66: 0
    uint32_t dll_path_len;    // 0x6A: 24
    // char dll_path[24];     // "..\VnStudio\vnresmod.dll"
};

// Bloc générique - apparaît 869 fois dans le fichier
struct VNDBlock {
    uint32_t separator;       // 0x01 0x00 0x00 0x00 (marqueur)
    uint32_t length;          // Taille du bloc en bytes
    uint32_t type;            // Type de bloc
    uint8_t  payload[];       // Données variables
};

// Types de blocs possibles (à déterminer)
#define VND_BLOCK_TYPE_TEXT     0x00
#define VND_BLOCK_TYPE_IMAGE    0x01
#define VND_BLOCK_TYPE_SCRIPT   0x02
#define VND_BLOCK_TYPE_AUDIO    0x03
// ... autres types à identifier
