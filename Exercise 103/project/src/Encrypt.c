/*
** EPITECH PROJECT, 2017
** 103cipher
** File description:
** Main function
*/

#include "function.h"

int spaces(char *Msg, char *Key, int l)
{
        int counter1 = 0;
	int counter2 = 0;
	int sortie = 0;
	int sortie2 = 0;
	int i = 0;
	int f = 0;
	int number = 0;
	int counter_spaces = 0;
	while (sortie2 < my_strlen(Msg)) {
		while (i < l) {
			while (f < l) {
				number += Msg[f + counter1] * Key[i + counter2];
				f++;
				counter2 = counter2 + l;
				counter_spaces++;
			}
			number = 0;
			f = 0;
			counter2 = 0;
			sortie++;
			sortie2++;
			i++;
		}
		counter1 += l;
		sortie = 0;
		i = 0;
	}
	return (counter_spaces);

}

void calcul(char *Msg, char *Key, int l)
{
	int counter1 = 0;
	int counter2 = 0;
	int sortie = 0;
	int sortie2 = 0;
	int i = 0;
	int f = 0;
	int number = 0;
	int counter_spaces = spaces(Msg, Key, l);
	int counter_space = 0;
	while (sortie2 < my_strlen(Msg)) {
		while (i < l) {
			while (f < l) {
				number += Msg[f + counter1] * Key[i + counter2];
				f++;
				counter2 = counter2 + l;
				counter_space++;
			}
			printf("%d", number);
			if (counter_space < counter_spaces)
				printf(" ");
			number = 0;
			f = 0;
			counter2 = 0;
			sortie++;
			sortie2++;
			i++;
		}
		counter1 += l;
		sortie = 0;
		i = 0;
	}
}

int counter_diff(int l, int i)
{
	int difference = 0;
	while (i < l)
		i = i + l;
	while (i > l)
		i = i - l;
	while (i != l) {
		i++;
		difference++;
	}
	return (difference);
}

void Encrypted_mess(char *Key_array, int l, char *av[])
{
	int i = my_strlen(av[1]);
	int counter = 0;
	char *Message = malloc(2 * my_strlen(av[1]));
	while (av[1][counter] != '\0') {
		Message[counter] = av[1][counter];
		counter++;
	}
	int difference = counter_diff(l, i);
	while (difference != 0) {
		Message[counter] = 0;
		difference--;
		counter++;
	}
	Message[counter] = '\0';
	calcul(Message, Key_array, l);
}
