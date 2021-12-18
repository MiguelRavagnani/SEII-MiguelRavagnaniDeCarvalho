# @author Miguel Ravagnani de Carvalho

CC = gcc
CFLAGS = -I ./
INCLUDE = byte_operations.h byte_swap.h
OBJ = main.o byte_operations.o byte_swap.o

%.o: %.c $(INCLUDE)
	$(CC) -c -o $@ $< $(CFLAGS)

atv2.o: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

clean:
	rm -f atv2.o