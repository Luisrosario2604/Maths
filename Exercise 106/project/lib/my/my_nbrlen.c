/*
** EPITECH PROJECT, 2018
** CPE_corewar_2018
** File description:
** Function that return number's lenght
*/

#include "function.h"

int my_nbrlen(int nb)
{
	int len = 0;

	if (nb == 0)
		len = 1;
	else {
		while (nb != 0) {
			nb = nb / 10;
			len = len + 1;
		}
	}
	return (len);
}
