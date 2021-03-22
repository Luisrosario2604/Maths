/*
** EPITECH PROJECT, 2017
** 106bombyx
** File description:
** Method of growth
*/

#include "function.h"

int growth_method(char *av[])
{
	float x0 = atof(av[1]);
	float k = atof(av[2]);
	float x1;
	int counter = 1;
	if (k < 1 || k > 4) {
		printf("Error : k must be : 1 < k < 4\n");
		return (84);
	}
	while (counter <= 100) {
		printf("%d %.2f\n",counter, x0);
		x1 = x0 * k * ((1000 - x0) / 1000);
		x0 = x1;
		counter++;
	}
	return (0);
}
