/*
** EPITECH PROJECT, 2017
** my_strlen
** File description:
** 06
*/

int my_counter_number(int j)
{
	int i = 0;
	while (j != 0) {
		j = j / 10;
		i++;
	}
	return (i);
}
