# Makefile

all: sort generate

sort: sort.c helpers.c helpers.h
	clang -ggdb3 -O0 -std=c11 -Wall -Werror -o sort sort.c helpers.c -lcs50 -lm

generate: generate.c
	clang -ggdb3 -O0 -std=c11 -Wall -Werror -o generate generate.c

clean:
	rm -f *.o a.out core find generate
