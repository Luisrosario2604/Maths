/*
** EPITECH PROJECT, 2017
** 105torus
** File description:
** Main function
*/

#include "function.h"

int error(int ac,char **av)
{
        if (ac != 8)
                exit(84);
        if(av[1][0] != '1' && av[1][0] != '2' && av[1][0] != '3')
                exit(84);
	return (0);
}

int main(int ac,char *av[])
{
        error(ac,av);
        if(av[1][0] == '1')
                method_bisection(av);
        if(av[1][0] == '2')
                method_newton(av);
        if(av[1][0] == '3')
                method_secant(av);
        return(0);
}
