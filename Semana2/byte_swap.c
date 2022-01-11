#include "byte_swap.h"

uint16_t SwapOperation(byteOperation param_function, uint16_t param_byte){
    return param_function(param_byte);
}