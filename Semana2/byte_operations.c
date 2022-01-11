#include "byte_operations.h"

uint16_t SwapEndians(uint16_t param_byte){
    return (param_byte >> 8 | param_byte << 8);
}

uint16_t SwapBits(uint16_t param_byte){

    uint16_t swapped_bytes_left = 0;
    uint16_t swapped_bytes_right = 0;

    swapped_bytes_left = (param_byte & 0xF0) >> 4 | (param_byte & 0x0F) << 4;
    swapped_bytes_left = (swapped_bytes_left & 0xCC) >> 2 | (swapped_bytes_left & 0x33) << 2;
    swapped_bytes_left = (swapped_bytes_left & 0xAA) >> 1 | (swapped_bytes_left & 0x55) << 1;
    swapped_bytes_left = swapped_bytes_left << 8;

    swapped_bytes_right = param_byte >> 8;
    swapped_bytes_right = (swapped_bytes_right & 0xF0) >> 4 | (swapped_bytes_right & 0x0F) << 4;
    swapped_bytes_right = (swapped_bytes_right & 0xCC) >> 2 | (swapped_bytes_right & 0x33) << 2;
    swapped_bytes_right = (swapped_bytes_right & 0xAA) >> 1 | (swapped_bytes_right & 0x55) << 1;

    return swapped_bytes_left | swapped_bytes_right;
}