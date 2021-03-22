/*
** EPITECH PROJECT, 2017
** my_putchar
** File description:
** Display characters
*/

#include "function.h"

void my_putchar(char c)
{
	write(1, &c, 1);
}
