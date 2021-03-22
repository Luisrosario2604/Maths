/*
** EPITECH PROJECT, 2017
** functions.h
** File description:
** all functions
*/

#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include "include.h"

/* LIB FCT */
#include "get_next_line.h"

char *my_itoa(long int);
char *my_revstr(char *);
char *my_strcat(char *, char const *);
char *my_strcpy(char *, char const *);
char *my_strdup(char const *);
char **seg_line(char *);
int my_getnbr(char const *);
int my_nbrlen(int);
int my_strcmp(char const *, char const *);
int my_strlen(char const *);
void my_putchar(char);
void my_putstr(char const *);
char *get_next_line(int);
int my_putnbr(int);
int my_counter_number(int);

/* MAIN FUNCTION */
int main(int, char **);
int my_strlen(char const *);
int my_counter_3(int);
int my_counter_number(int);
void print_key(char **, char *);
void print_key2(int, char **, char *, int);
int know_the_size(char **);
void Encrypted_mess(char *, int, char **);
int counter_diff(int, int);
void calcul(char *, char *, int);
void calcul(char *, char *, int);
void decrypted(char **, char *);
int comatrix(char *);
void message(char *, float *, int);
void calc_disp(int *, float *, int, char *);
void matrix_inverse2(char **, char *, int);
void matrix_inverse1(char **, char *, int);

#endif
