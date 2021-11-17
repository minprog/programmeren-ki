# Makefile for Tiles game

tiles: tiles.c helpers.o
	clang -ggdb3 -O0 -std=c11 -Wall -Werror -o tiles tiles.c helpers.o -lcs50 -lm

helpers.o: helpers.c
	clang -ggdb3 -O0 -std=c11 -Wall -Werror -c -o helpers.o helpers.c

clean:
	rm -f *.o a.out core tiles log.txt
