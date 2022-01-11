#include <stdio.h>
#include <stdint.h>
#include "byte_swap.h"
#include "byte_operations.h"

/**
 * @author Miguel Ravagnani de Carvalho
 */

void PrintBits (uint16_t param_word){
    uint16_t mask = 0;
    uint16_t mask_handler = 0;
    int i = 0;

    for (i = 15; i >= 0; i--){
        mask = 1 << i;
        mask_handler = param_word & mask;
        mask_handler == 0 ? printf ("0") : printf ("1");
    }
    return;
}

int main(){

    uint16_t word = 32773;
    uint16_t word_swap_bits = 0x00;
    uint16_t word_swap_endian = 0x00;

    byteOperation SwapBitsPtr;
    byteOperation SwapEndiansPtr;

    SwapBitsPtr = SwapBits;
    SwapEndiansPtr = SwapEndians;

    printf("Word before conversion\nHex: %X | Binary ", word);
    PrintBits(word);

    word_swap_bits = SwapOperation(SwapBitsPtr, word);
    word_swap_endian = SwapOperation(SwapEndiansPtr, word);

    printf("\nWord after bits conversion\nHex: %X | Binary ", word_swap_bits);
    PrintBits(word_swap_bits);

    printf("\nWord after endian conversion\nHex: %X | Binary ", word_swap_endian);
    PrintBits(word_swap_endian);
    printf("\n");

    return 0;
}