/*
** EPITECH PROJECT, 2017
** my_strcpy.c
** File description:
** Function that copies a string into another
*/

#include "function.h"

char *my_strcpy(char *dest, char const *src)
{
	int i = 0;

	for (i = 0; src[i] != '\n' && src[i] != '\0'; i += 1) {
		dest[i] = src[i];
	}
	dest[i] = '\0';
	return (dest);
}
