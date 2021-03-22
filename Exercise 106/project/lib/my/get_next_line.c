/*
** EPITECH PROJECT, 2018
** get_next_line
** File description:
** The 5 functions get_next_line.
*/

#include "function.h"

static unsigned int scan(char *buffer)
{
	unsigned int count = 0;

	while (buffer[count] != '\0') {
		if (buffer[count] == '\n')
			return (0);
		count = count + 1;
	}
	return (1);
}

static unsigned int my_line_lenght(char *line, const int choice)
{
	unsigned int count = 0;

	while (line[count] != '\0' && line[count] != '\n' && choice == 1) {
		count = count + 1;
	}
	while (line[count] != '\0' && choice == 2) {
		count = count + 1;
	}
	return (count);
}

static void my_strcpy_tmp(char *destination, char *source, const int choice)
{
	unsigned int size = 0;
	unsigned int count = 0;
	unsigned int count_source = 0;

	if (source[0] == '\n')
		source++;
	if (choice == 1) {
		size = my_line_lenght(destination, 1) + READ_SIZE;
		count = size - READ_SIZE;
	}
	choice == 2 ? size = my_line_lenght(source, 1) : 0;
	choice == 3 ? size = my_line_lenght(source, 2) : 0;
	while (count < size && choice != 3 ? source[count_source] != '\n' :
	source[count_source]) {
		destination[count] = source[count_source];
		count = count + 1;
		count_source = count_source + 1;
	}
	choice != 4 ? destination[count] = '\0' : 0;
}

static char *my_re_alloc_string(char *old_string, const int to_add)
{
	unsigned int lenght_old_string = my_line_lenght(old_string, 1);
	char *new_string = malloc(sizeof(char) * lenght_old_string +
	to_add + 1);

	old_string[lenght_old_string] = '\0';
	if (new_string == NULL)
		return (NULL);
	for (unsigned int i = 0; i < lenght_old_string + to_add; i++)
		new_string[i] = 0;
	my_strcpy_tmp(new_string, old_string, 2);
	new_string[lenght_old_string + to_add] = '\0';
	free(old_string);
	return (new_string);
}

char *get_next_line(int fd)
{
	static char buf[READ_SIZE];
	char *line = NULL;
	int check = 1;
	const int size = READ_SIZE;

	if (!(line = malloc(sizeof(char) * size + size)) || !size)
		return (NULL);
	line[0] = '\0';
	buf[0] != '\n' ? my_strcpy_tmp(line, buf, 1) : 0;
	if (scan(buf)) {
		while ((check = read(fd, buf, size)) == size &&
		scan(buf) && line) {
			my_strcpy_tmp(line, buf, 1);
			line = my_re_alloc_string(line, size);
		}
		check > 0 && *buf != '\n' ? my_strcpy_tmp(line, buf, 1) : 1;
		check < size ? buf[check - 1] = '\0' : 0;
	}
	my_strcpy_tmp(buf, buf + my_line_lenght(buf, 1), 3);
	return (check <= 0 && buf[0] == '\0' && line[0] == '\0' ? NULL : line);
}
