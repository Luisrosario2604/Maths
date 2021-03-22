/*
** EPITECH PROJECT, 2017
** my_strdup.c
** File description:
** Duplicate a string
*/

#include "function.h"

char *my_strdup(char const *src)
{
	char *str;
	int len = my_strlen(src);

	str = malloc(sizeof(char) * len + 1);
	if (!str)
		return (NULL);
	my_strcpy(str, src);
	return (str);
}
