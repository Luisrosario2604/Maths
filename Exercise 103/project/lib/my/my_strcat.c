/*
** EPITECH PROJECT, 2018
** CPE_getnextline_2017
** File description:
** Function that returns a read line from a file descriptor
*/

#include "function.h"

char *my_strcat(char *dest, char const *src)
{
	int i;

	for (i = 0; dest[i] != '\0'; i += 1);
	for (int j = 0; src[j] != '\0'; j += 1, i += 1)
		dest[i] = src[j];
	dest[i] = '\0';
	return (dest);
}
