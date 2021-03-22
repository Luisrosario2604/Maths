##
## EPITECH PROJECT, 2017
## Makefile
## File description:
## Makefile to compile library
##

SRC	=	get_next_line.c		\
		my_getnbr.c			\
		my_itoa.c			\
		my_nbrlen.c			\
		my_putchar.c			\
		my_putstr.c			\
		my_str_to_words_array.c	\
		my_strcat.c			\
		my_strcmp.c			\
		my_strcpy.c			\
		my_strdup.c			\
		my_strlen.c			\
		my_putnbr.c			\
		my_counter_number.c

CFLAGS	=	-I../../include/ -W -Wextra

OBJ	=	$(SRC:.c=.o)

NAME	=	libmy.a

all:	$(NAME)

$(NAME):	$(OBJ)
	ar rc $(NAME) $(OBJ)

clean:
	rm -f $(OBJ)

fclean:	clean
	rm -f $(NAME)

re:	fclean all
