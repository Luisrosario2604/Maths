/*
** EPITECH PROJECT, 2017
** 103cipher
** File description:
** Main function
*/

#include "function.h"

void calc_disp(int *calc_final, float *Key, int l, char *Message)
{
	int count1 = 0;
	int count2 = 0;
	int count3 = 0;
	int count4 = 0;
	double temp = 0;
	int temp1 = 0;
	int strlen = 0;
	char temp4;
	int counter = 0;
	double temp2 = 0;
	while (calc_final[strlen] != NULL)
		strlen++;
	while (counter < strlen) {
		while (count4 < l) {
			while (count1 < l) {
				temp = temp + (calc_final[count1 + count2] * Key[count3 + count4]);
				count1++;
				count3 += l;
			}
			temp1 = temp;
			temp2 = temp1 + 0.5;
			temp4 = temp1;
			if (temp - temp1 == 0)
				printf("%c", temp4);
			else if (temp2 > temp)
				printf("%c", temp4);
			else
				printf("%c", temp4 + 1);
			temp = 0;
			count3 = 0;
			count4++;
			count1 = 0;
			counter++;
		}
		count2 += l;
		count4 = 0;
	}

}

void message(char *Message, float *Key, int l)
{
	int calc = 0;
	int i = 0;
	int h = 1;
	int a = 0;
	int g = 0;
	int q = 0;
	int *calc_final = malloc(sizeof(int *) * my_strlen(Message));
	int j = my_strlen(Message);
	while (g < j) {
		i = 0;
		while (Message[i + q] != ' ')
			i++;
		q += i + 1;
		while (i != 0) {
			h = h * 10;
			i--;
		}
		h = h / 10;
		while (Message[g] != ' ') {
			calc += (Message[g] - 48) * h;
			g++;
			h = h / 10;
		} 
		calc_final[a] = calc;
		a++;
		g++;
		h = 1;
		calc = 0;
	}
	h = a;
	while (a > l)
		a = a - l;
	while (a > 0) {
		calc_final[h] = 0;
		a--;
	}
        calc_disp(calc_final, Key, l, Message);
}

int comatrix(char *m)
{
	int i = -((m[2] * m[4] * m[6])+(m[0] * m[5] * m[7])+(m[1] * m[3] * m[8]))+((m[0] * m[4] * m[8])+(m[1] * m[5] * m[6])+(m[2] * m[3] * m[7]));
	return (i);
}

void matrix_inverse2(char *key[], char *m, int l)
{
	float matrix_inverse[4] = {0, 0, 0, 0};
	float a = (m[0] * m[3] - m[1] * m[2]);
	matrix_inverse[0] = (m[3]) * 1/a;
	matrix_inverse[1] = (m[1]) * -1/a;
	matrix_inverse[2] = (m[2]) * -1/a;
	matrix_inverse[3] = (m[0]) * 1/a;
	int i = 0;
	int b = 0;
	while (i != 4) {
		while (1) {
		if (matrix_inverse[i] == 0)
			printf("0.0   ");
	        else
			printf("%.4f", matrix_inverse[i]);
		break;
		}
		if (i == 1)
			printf("\n");
		else
			printf("  ");
		i++;
	}
	while (key[1][b] != '\0')
		b++;
	key[1][b] = ' ';
	key[1][b + 1] = '0';
	key[1][b + 2] = ' ';
	key[1][b + 3] = '0';
	printf("\n\nDecrypted message :\n");
	message(key[1], matrix_inverse, l);
}

void matrix_inverse1(char *key[], char *m, int l)
{
	int b = 0;
	while (key[1][b] != '\0')
		b++;
	key[1][b] = ' ';
	key[1][b + 1] = '0';
	key[1][b + 2] = ' ';
	key[1][b + 3] = '0';
	float matrix_inverse[1] = {0};
	float a = 1;
	matrix_inverse[0] = a / m[0];
	printf("%.4f", matrix_inverse[0]);
	printf("\n\nDecrypted message :\n");
	message(key[1], matrix_inverse, l);
}

void matrix_inverse(char *key[], char *m, int l)
{
	float matrix_inverse[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
	float a = comatrix(m);
	matrix_inverse[0] = ((m[4] * m[8]) - (m[7] * m[5])) * 1/a;
	matrix_inverse[1] = ((m[2] * m[7]) - (m[1] * m[8])) * 1/a;
	matrix_inverse[2] = ((m[1] * m[5]) - (m[4] * m[2])) * 1/a;
	matrix_inverse[3] = ((m[5] * m[6]) - (m[3] * m[8])) * 1/a;
	matrix_inverse[4] = ((m[0] * m[8]) - (m[2] * m[6])) * 1/a;
	matrix_inverse[5] = ((m[2] * m[3]) - (m[5] * m[0])) * 1/a;
	matrix_inverse[6] = ((m[3] * m[7]) - (m[4] * m[6])) * 1/a;
	matrix_inverse[7] = ((m[1] * m[6]) - (m[0] * m[7])) * 1/a;
	matrix_inverse[8] = ((m[4] * m[0]) - (m[3] * m[1])) * 1/a;
	int i = 0;
	int j = 0;
	int b = 0;
	while (j < 9) {
		while (i != 3) {
			if (matrix_inverse[i + j] == 0)
				printf("0.0     ");
			else if (i == 2) {
				printf("%.3f", matrix_inverse[i + j]);
				b = 1;
			}
			else
				printf("%.3f  ", matrix_inverse[i + j]);
			if (matrix_inverse[i + j] >= 0 && b == 0)
				printf(" ");
			i++;
			b = 0;
		}
		i = 0;
		j += 3;
		printf("\n");
	}
	b = 0;
	while (key[1][b] != '\0')
		b++;
	key[1][b] = ' ';
	key[1][b + 1] = '0';
	key[1][b + 2] = ' ';
	key[1][b + 3] = '0';
	printf("\nDecrypted message :\n");
	message(key[1], matrix_inverse, l);
}

void decrypted(char *key[], char *matrix_key)
{
	int a = 0;
	int b = 0;
	int l = know_the_size(key);
	while (a < l * l) {
		if (key[2][b] != NULL)
			matrix_key[a] = key[2][b];
		else {
			matrix_key[a] = 0;
			b--;
		}
		b++;
		a++;
	}
	printf("Key matrix :\n");
	if (l == 3)
		matrix_inverse(key, matrix_key, l);
	else if (l == 2)
		matrix_inverse2(key, matrix_key, l);
	else
		matrix_inverse1(key, matrix_key, l);
}
