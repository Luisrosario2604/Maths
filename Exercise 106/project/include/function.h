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

/* MAIN FUNCTION */
int main(int, char **);
int generation_method(char **);
int growth_method(char **);
void help(void);


#endif
