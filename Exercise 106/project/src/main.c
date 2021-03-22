/*
** EPITECH PROJECT, 2017
** 106bombyx
** File description:
** Main function
*/

#include "function.h"

void help(void)
{
	printf("USAGE\n           ./106bombyx n[k|i0 i1]\n");
	printf("\nDESCRIPTION\n           n    number of fir");
	printf("st generation individuals\n           k    growth");
	printf("rate from 1 to 4\n           i0   initial generation");
	printf("(included)\n           i1   final generation (included)\n");
}

int main(int ac,char *av[])
{
	int i = 0;
	if (ac == 2 && av[1][0] == '-' && av[1][1] == 'h') {
		help();
		return (0);
	}
	if (ac == 3) {
		i = growth_method(av);
		return (i);
	} else if (ac == 4) {
		i = generation_method(av);
		return (i);
	} else {
		printf("Invalid arguments : ./106bombyx -h");
		return (84);
	}
        return(0);
}
