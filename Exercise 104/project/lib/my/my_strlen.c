/*
** EPITECH PROJECT, 2018
** CPE_getnextline_2017
** File description:
** Function that returns a read line from a file descriptor
*/

#include "function.h"

int my_strlen(char const *str)
{
	int nbr;

	if (!str)
		return (0);
	for (nbr = 0; str[nbr] != '\n' && str[nbr] != '\0'; nbr += 1);
	return (nbr);
}
