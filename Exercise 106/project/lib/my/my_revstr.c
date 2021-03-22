/*
** EPITECH PROJECT, 2017
** my_revstr.c
** File description:
** Function that reverses a string
*/

#include "function.h"

char *my_revstr(char *str)
{
	int i = 0;
	int j = 0;
	char temp;

	while (str[i] != '\0') {
		i += 1;
	}
	while (j < i ) {
		temp = str[j];
		str[j] = str[i - 1];
		str[i - 1] = temp;
		j += 1;
		i -= 1;
	}
	return (str);
}
