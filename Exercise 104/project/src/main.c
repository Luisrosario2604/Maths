/*
** EPITECH PROJECT, 2017
** 104intersection
** File description:
** Main function
*/

#include "function.h"

int is_number(char *str)
{
	int i = 0;
	while (str[i] != '\0') {
		if (str[i] < '0' || str[i] > '9') {
			if (str[i] != '-')
				return (1);
		}
		i++;
	}
	return (0);
}

void calcul(char *av[])
{
	int xp = atoi(av[2]);
	int yp = atoi(av[3]);
	int zp = atoi(av[4]);
	int xv = atoi(av[5]);
	int yv = atoi(av[6]);
	int zv = atoi(av[7]);
	float Rayon = atoi(av[8]);
	float a = 0;
	float b = 0;
	float c = 0;

	if (av[1][0] == '1') {
		a = (xv * xv) + (yv * yv) + (zv * zv);
		b = (2 * xp * xv) + (2 * yp * yv) + (2 * zp * zv);
		c = (xp * xp) + (yp * yp) + (zp * zp) - (Rayon * Rayon);
	} else if (av[1][0] == '2') {
		a = (xv * xv) + (yv * yv);
		b = (2 * xp * xv) + (2 * yp * yv);
		c = (xp * xp) + (yp * yp) - (Rayon * Rayon);
	} else if (av[1][0] == '3') {
		float Angle = ((atoi(av[8])) * (M_PI/ 180));
		a = (xv * xv) + (yv * yv) - (zv * zv) * (tan(Angle) * tan(Angle));
		b = (2 * xp * xv) + (2 * yp * yv) - (2 * zp * zv) * (tan(Angle) * tan(Angle));
		c = (xp * xp) + (yp * yp) - (zp * zp) * (tan(Angle) * tan(Angle));
	}
	float delta = (b * b) - (4 * a * c);
	float answer1 = 0;
	float answer2 = 0;
	float answer1_1 = 0;
	float answer1_2 = 0;
	float answer1_3 = 0;
	float answer2_1 = 0;
	float answer2_2 = 0;
	float answer2_3 = 0;
	if (delta == 0) {
		answer1 = (-1 * b) / (2 * a);
		answer1_1 = xp + (answer1 * xv);
		answer1_2 = yp + (answer1 * yv);
		answer1_3 = zp + (answer1 * zv);
		printf("1 intersection point :\n(%.3f, %.3f, %.3f)\n", answer1_1, answer1_2, answer1_3);

	} else if (delta < 0) {
		printf("No intersection point.\n");
	} else {
		answer1 = ((-b) - sqrt(delta)) / (2 * a);
		answer2 = ((-b) + sqrt(delta)) / (2 * a);
		answer1_1 = xp + (answer1 * xv);
		answer1_2 = yp + (answer1 * yv);
		answer1_3 =  zp + (answer1 * zv);
		answer2_1 = xp + (answer2 * xv);
		answer2_2 = yp + (answer2 * yv);
		answer2_3 =  zp + (answer2 * zv);
		printf("2 intersection points :\n(%.3f, %.3f, %.3f)\n", answer2_1, answer2_2, answer2_3);
		printf("(%.3f, %.3f, %.3f)\n", answer1_1, answer1_2, answer1_3);

	}
}

int display_lines(char *av[])
{
	int i = 1;
	while (i != 9) {
		if (is_number(av[i]) == 1) {
			printf("Not a number");
			return (84);
		}
		i++;
	}
	if (av[1][0] == '1')
		printf("sphere of radius %s", av[8]);
	else if (av[1][0] == '2')
		printf("cylinder of radius %s", av[8]);
	else if (av[1][0] == '3')
		printf("cone of %s degree angle", av[8]);
	printf("\nstraight line going through the (%s,%s,%s) point and of direction vector (%s,%s,%s)\n", av[2], av[3], av[4], av[5], av[6], av[7]);
	calcul(av);
	return (0);
}

int main(int ac, char *av[])
{
	if (ac == 9) {
		int a = 0;
		a = display_lines(av);
		return (a);
	}
	else {
		printf("Invalid number of arguments");
		return (84);
	}
}
