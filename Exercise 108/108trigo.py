#!/usr/bin/python3

import sys


def help():
	print("USAGE")
	print("\t./108trigo fun a0 a1 a2....\n")
	print("DESCRIPTION")
	print("\tfun function to be applied, among at least \"EXP\", \"COS\", \"SIN\", \"COSH\" and \"SINH\"")
	print("\tai  coeficients of the matrix")


def print_matrix(Matrix):

	stop = 0
	while (stop * stop) < len(Matrix):
		stop = stop + 1

	i = 0
	j = 0
	while i < len(Matrix):
		j = 0
		while j < len(Matrix):
			if j == len(Matrix) - 1:
				print("{0:.2f}".format(Matrix[i][j]), end='')
			else:
				print("{0:.2f}".format(Matrix[i][j]), end='\t')
			j = j + 1
		print()
		i = i + 1


def create_matrix(av):
	size = len(av) - 2
	i = 1
	while (i * i) < size:
		i = i + 1
	matrix = [[int(0)] * i for _ in range(i)]
	j = 0
	n = 2
	while j < i:
		k = 0
		while (k < i) and (n < size + 2):
			matrix[j][k] = int(av[n])
			n += 1
			k += 1
		j += 1
	return matrix


def multiply_matrix(matrix, matrix2):
	tmp = []
	for i in range(len(matrix)):
		tmp2 = []
		for j in range(len(matrix2[0])):
			elem = 0
			for k in range(len(matrix2)):
				elem += (matrix[i][k] * matrix2[k][j])
			tmp2.append(elem)
		tmp.append(tmp2)
	return tmp


def division_matrix(matrix, div):
	i = 0
	while i != len(matrix):
		for j in range(len(matrix[0])):
			matrix[i][j] /= div
		i += 1
	return matrix


def addition_matrix(matrix, matrix2):
	tmp = []
	for i in range(len(matrix)):
		save = []
		for j in range(len(matrix[0])):
			save.append(matrix[i][j] + matrix2[i][j])
		tmp.append(save)
	return tmp


def soustraction_matrix(matrix, matrix2):
	save = []
	for i in range(len(matrix)):
		tmp = []
		for j in range(len(matrix[0])):
			tmp.append(matrix[i][j] - matrix2[i][j])
		save.append(tmp)
	return save


def matrix_power(matrix, nb):
	tmp = matrix
	i = 0
	while i != (nb - 1):
		tmp = multiply_matrix(matrix, tmp)
		i += 1
	return tmp


def factorial_nb(nb):
	if nb < 2:
		return 1
	return nb * factorial_nb(nb - 1)


def cosCalc(matrix):
	matrix1 = []
	for i in range(len(matrix)):
		tmp = []
		for j in range(len(matrix[0])):
			if i == j:
				tmp.append(1)
			else:
				tmp.append(0)
		matrix1.append(tmp)

	save = matrix1
	for i in range(1, 100):
		if i % 2 == 0:
			save = addition_matrix(save, division_matrix(matrix_power(matrix, 2 * i), factorial_nb(2 * i)))
		else:
			save = soustraction_matrix(save, division_matrix(matrix_power(matrix, 2 * i), factorial_nb(2 * i)))
	return save


def sinCalc(Matrix):
	tmp = Matrix
	for i in range(1, 100):
		if i % 2 == 0:
			tmp = addition_matrix(tmp, division_matrix(matrix_power(Matrix, 2 * i + 1), factorial_nb(2 * i + 1)))
		else:
			tmp = soustraction_matrix(tmp, division_matrix(matrix_power(Matrix, 2 * i + 1), factorial_nb(2 * i + 1)))
	return tmp


def expCalc(matrix):
	matrix_save = []
	for i in range(len(matrix)):
		tmp = []
		for j in range(len(matrix[0])):
			if i == j:
				tmp.append(1)
			else:
				tmp.append(0)
		matrix_save.append(tmp)

	save = matrix_save
	for i in range(1, 100):
		save = addition_matrix(save, division_matrix(matrix_power(matrix, i), factorial_nb(i)))
	return save


def coshCalc(matrix):
	matrix_save = []
	for i in range(len(matrix)):
		tmp = []
		for j in range(len(matrix[0])):
			if i == j:
				tmp.append(1)
			else:
				tmp.append(0)
		matrix_save.append(tmp)

	save = matrix_save
	for k in range(1, 100):
		save = addition_matrix(save, division_matrix(matrix_power(matrix, 2 * k), factorial_nb(2 * k)))
	return res


def sinhCalc(matrix):
	tmp = matrix
	for k in range(1, 100):
		tmp = addition_matrix(tmp, division_matrix(matrix_power(matrix, 2 * k + 1), factorial_nb(2 * k + 1)))
	return tmp


def chooseOperator(av):
	matrix = create_matrix(av)
	if av[1] == "COS":
		matrix = cosCalc(matrix)
	if av[1] == "SIN":
		matrix = sinCalc(matrix)
	if av[1] == "COSH":
		matrix = coshCalc(matrix)
	if av[1] == "EXP":
		matrix = expCalc(matrix)
	if av[1] == "SINH":
		matrix = sinhCalc(matrix)
	print_matrix(matrix)


def error(arg):

	if len(arg) < 2:
		exit(84)

	if len(arg) == 2:
		if arg[1] == "-h":
			help()
			exit(0)
		else:
			exit(84)

	if (arg[1] != "COS" and arg[1] != "SIN" and arg[1] != "COSH" and
	arg[1] != "EXP" and arg[1] != "SINH"):
		exit(84)

	i = 2
	while i != len(arg):
		try:
			float(arg[i])
		except:
			exit(84)
		i = i + 1


def main():
	error(sys.argv)
	chooseOperator(sys.argv)
	return 0
main()
