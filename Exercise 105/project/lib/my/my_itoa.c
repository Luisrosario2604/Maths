/*
** EPITECH PROJECT, 2018
** my_itoa.c
** File description:
** Convert a numbre into a string
*/

#include "function.h"

char *my_itoa(long int nbr)
{
	int len = my_nbrlen(nbr);
	char *str = malloc(sizeof(*str) * (len + 1));

	if (str == NULL)
		return (NULL);
	for (int i = 0; i < len; i += 1) {
		str[i] = (nbr % 10) + 48;
		nbr = nbr / 10;
	}
	str[len] = '\0';
	str = my_revstr(str);
	return (str);
}
