/*
** EPITECH PROJECT, 2017
** 107transfer
** File description:
** Main function
*/

#include "function.h"

void help(void)
{
	printf("USAGE\n           ./107transfer [num den]*\n");
	printf("\nDESCRIPTION\n           num    ");
	printf("polynomial numerator defined by its coeficients\n");
	printf("           den    ");
	printf("polynomial denominator defined by its coeficients\n");
}

int main(int ac,char *av[])
{
	int a = 0;
	if (ac == 2 && av[1][0] == '-' && av[1][1] == 'h') {
		help();
		return (0);
	} else if (ac >= 3 && ac % 2 == 1) {
		a = main_calc(av, ac);
		if (a == 1) {
			printf("No div by 0\n");
			return (84);
		} else {
			return (0);
		}
	} else {
		printf ("Error : ./107transfer -h");
	}
        return(0);
}
