/*
** EPITECH PROJECT, 2017
** 107transfer
** File description:
** Main function
*/

#include "function.h"

double part_nbr(char *nbr)
{
	int j = 0;
	static int i = 0;
	char *last = malloc(sizeof(char) * my_strlen(nbr));
	while (nbr[i] != '*' && nbr[i] != '\0') {
		last[j] = nbr[i];
		j++;
		i++;
	}
	if (nbr[i] == '\0')
		i = -1;
	i++;
	last[j] = '\0';
	double x = atof(last);
	free(last);
	return (x);
}

double get_my_nbr(char *nbr, double i)
{
	int k = 0;
	int power = 1;
	double x = part_nbr(nbr);
	double y = 0;
	while (nbr[k] != '\0') {
		if (nbr[k] == '*') {
			y = part_nbr(nbr);
			x += y * pow(i, power);
			power++;
		}
		k++;
	}
	return (x);
}
	
int calc(char *av[], double i, int ac)
{
	int k = 1;
	double a = 0;
	double b = 0;
	double result = 1;
	while (k != ac) {
		a = get_my_nbr(av[k], i);
		b = get_my_nbr(av[k + 1], i);
		if (b == 0)
			return (1);
		result = result * (a / b);
		k += 2;
	}
	printf("%.5f", result);
	return (0);
}

int main_calc(char *av[], int ac)
{
        double i = 0;
	int a = 0;
	while (i <= 1.001) {
		display(i, 4);
		printf(" ");
		a = calc(av, i, ac);
		if (a == 1)
			return (1);
		printf("\n");
		i += 0.001;
	}
	return (0);
}
