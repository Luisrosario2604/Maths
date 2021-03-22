/*
** EPITECH PROJECT, 2017
** 107transfer
** File description:
** Main function
*/

#include "function.h"

void display(double x, int n)
{
	int a = 0;
	int z = x;
	int e = 10;
	int count = 1;
	int exit = 0;

	while (count != 9) {
		z = x * e;
		a = z % 10;
		e = e * 10;
		if (a == 0) {
			if (count <= n)
				exit++;
		} else
			exit = 0;
		count++;
	}
	printf("%.*f ->", n - exit , x);
}
