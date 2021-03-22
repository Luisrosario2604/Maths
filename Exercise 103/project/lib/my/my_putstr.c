/*
** EPITECH PROJECT, 2017
** my_putstr
** File description:
** Display string's characters
*/

#include "function.h"

void my_putstr(char const *str)
{
	int i = 0;

	while (str[i] != '\0') {
		my_putchar(str[i]);
		i += 1;
	}
}
