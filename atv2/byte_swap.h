#ifndef _BYTE_SWAP_
#define _BYTE_SWAP_

/**
 * @author Miguel Ravagnani de Carvalho
 */

#include <stdint.h>

typedef uint16_t (*byteOperation) (uint16_t);

uint16_t SwapOperation(byteOperation param_function, uint16_t param_byte);

#endif // _BYTE_SWAP_