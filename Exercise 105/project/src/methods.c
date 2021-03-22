/*
** EPITECH PROJECT, 2017
** 105torus
** File description:
** Methods file
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
	printf("x = %.*f\n", n - exit , x);
}

double derived(double x, char *av[])
{
	double a1 = atoi(av[3]);
	double a2 = atoi(av[4]);
	double a3 = atoi(av[5]);
	double a4 = atoi(av[6]);
	double result = ((4 * a4 * pow(x, 3)) + (3 * a3 * pow(x, 2))
			 + (2 * a2 * x) + a1);
	return (result);
}

double function(double x, char *av[])
{
	double a0 = atoi(av[2]);
	double a1 = atoi(av[3]);
	double a2 = atoi(av[4]);
	double a3 = atoi(av[5]);
	double a4 = atoi(av[6]);
	double result = ((a4 * pow(x, 4)) + (a3 * pow(x, 3))
			 + (a2 * pow(x, 2)) + (a1 * x) + a0);
	return (result);
}

void method_bisection(char *av[])
{
	int n = atoi(av[7]);
	double e = pow(10, -(atoi(av[7])));
	double x1 = 0;
	double x2 = 1;
	double xm = (x1 + x2) / 2;
	while ((fabs(x1 - x2)) / 2 * fabs(xm) > e) {
		xm = (x1 + x2) / 2;
		if ((function(x1, av) * function(xm, av)) < 0)
			x2 = xm;
		else
			x1 = xm;
	        display(xm, n);
	}
	xm = (x1 + x2) / 2;
	if ((function(x1, av) * function(xm, av)) < 0)
		x2 = xm;
	else
		x1 = xm;
        display(xm, n);
	xm = (x1 + x2) / 2;
	if ((function(x1, av) * function(xm, av)) < 0)
		x2 = xm;
	else
		x1 = xm;
        display(xm, n);
}

void method_newton(char *av[])
{
	int n = atoi(av[7]);
	double e = pow(10, -(atoi(av[7])));
	double xn_1 = 0.5;
	double xn_2 = xn_1 - ((function(xn_1, av) / (derived(xn_1, av))));
	while ((fabs(xn_2 - xn_1) / fabs(xn_2)) > e) {
	        display(xn_1, n);
		xn_1 = xn_2;
	        xn_2 = xn_1 - ((function(xn_1, av) / (derived(xn_1, av))));
	}
	display(xn_1, n);
}

void method_secant(char *av[])
{
	int n = atoi(av[7]);
	double e = pow(10, -(atoi(av[7])));
	double xn_0 = 0;
	double xn_1 = 1;
	double xn_2 = xn_1 - ((function(xn_1, av) * (xn_1 - xn_0))
			      / (function(xn_1, av) - function(xn_0, av)));
	while ((fabs(xn_2 - xn_1) / fabs(xn_2)) > e) {
	        display(xn_2, n);
		xn_0 = xn_1;
		xn_1 = xn_2;
		xn_2 = xn_1 - ((function(xn_1, av) * (xn_1 - xn_0))
			       / (function(xn_1, av) - function(xn_0, av)));
	}
	display(xn_2, n);
}
