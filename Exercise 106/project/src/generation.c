/*
** EPITECH PROJECT, 2017
** 106bombyx
** File description:
** Method of generation
*/

#include "function.h"

int generation_method(char *av[])
{
	double x0 = atof(av[1]);
	double k = 1;
	double i0 = atof(av[2]);
	double i1 = atof(av[3]);
	double i = 1;
	while (k <= 4.00) {
		while (i < i0) {
			x0 = x0 * k * ((1000 - x0) / 1000);
			i++;
		}
		while (i <= i1) {
			printf("%.2f %.2f\n", k, x0);
			x0 = x0 * k * ((1000 - x0) / 1000);
			i++;
		}
		i = 1;
		k += 0.01;
		x0 = atof(av[1]);
	}
	return (0);
}
