/*
** EPITECH PROJECT, 2017
** 103cipher
** File description:
** Main function
*/

#include "function.h"

void print_key2(int l, char *key[], char *Key_array, int w)
{
	int a = 0;
	int i = my_strlen(key[2]);
	int h = l * l;
	int s = h - i;
	while (i != h) {
		if (i + 1 == h || i + 1 == h - l) {
			printf("0");
		} else {
			printf("0          ");
		}
		i++;
		s = h - i;
		if (s == l)
			printf("\n");
		a = 1;
		Key_array[w] = 0;
		w++;
	}
	if (a == 1)
		printf("\n");
	printf("\nEncrypted message :\n");
	Encrypted_mess(Key_array, l, key);
}

int know_the_size(char *key[])
{
	int j = my_strlen(key[2]);
	float i = j;
	int k = i;
	int l = 0;
	if (i == 1)
		return(1);
	while (i > l) {
		l++;
		i = k;
		i = (i / l);
	}
	return (l);
}

void print_key(char *key[], char *Key_array)
{
	int i = 0;
	int a = 0;
	int z = 0;
	int temp = 0;
	int l = know_the_size(key);
	printf("Key matrix :\n");
	while (key[2][i] != '\0') {
		temp = key[2][i];
		printf("%d", temp);
		Key_array[i] = (key[2][i]);
		z = key[2][i];
		a++;
		if (a != l) {
			if (my_counter_number(z) == 2)
				printf("         ");
			else
				printf("        ");
		}
		else {
			printf("\n");
			a = 0;
		}
		i++;
	}
	print_key2(l, key, Key_array, i);
}

int main(int ac, char *av[])
{
	if (ac != 4) {
		printf("ERROR");
		return (84);
	}
	else if (ac == 4 && av[3][0] == '0') {
		char *Key_array = malloc(2 * my_strlen(av[1]));
		print_key(av, Key_array);
		return (0);
	} else if (ac == 4 && av[3][0] == '1') {
		char *matrix_key = malloc(sizeof(char *) * my_strlen(av[2]));
	        decrypted(av, matrix_key);
		return (0);
	} else {
		printf("ERROR");
		return (84);
	}
}
