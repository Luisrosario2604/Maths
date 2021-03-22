/*
** EPITECH PROJECT, 2017
** my_getnbr.c
** File description:
** get a number in a string
*/

#include "function.h"

int my_getnbr(char const *str)
{
	int i;
	int e = 1;
	int neg = 0;
	long int result = 0;

	for (i = 0; (str[i] < 48 || str[i] > 58) && str[i] != '\0'; i++);
	if (i != 0)
		if (*(str + i - 1) == 45)
			neg = 1;
	for (; *(str + i) > 47 && *(str + i) < 58; i++) {
		result += *(str + i) - 48;
		if (*(str + i + 1) > 47 && *(str + i + 1) < 58)
			result *= 10;
		e += 1;
		if ((result > 2147483647 && neg != 1) || result > 2147483648)
			return (0);
	}
	if (neg == 1)
		return (result * -1);
	return (result);
}
