#!/usr/bin/python
# -*- coding utf-8 -8-

import sys
import math


def multiplication(matriceCalcul, matriceCalculTmp):

	matriceResult = [0, 0, 0, 0, 0, 0, 0, 0, 0]

	matriceResult[0] = matriceCalcul[0] * matriceCalculTmp[0] + matriceCalcul[1] * matriceCalculTmp[3] + matriceCalcul[2] * matriceCalculTmp[6]
	matriceResult[1] = matriceCalcul[0] * matriceCalculTmp[1] + matriceCalcul[1] * matriceCalculTmp[4] + matriceCalcul[2] * matriceCalculTmp[7]
	matriceResult[2] = matriceCalcul[0] * matriceCalculTmp[2] + matriceCalcul[1] * matriceCalculTmp[5] + matriceCalcul[2] * matriceCalculTmp[8]

	matriceResult[3] = matriceCalcul[3] * matriceCalculTmp[0] + matriceCalcul[4] * matriceCalculTmp[3] + matriceCalcul[5] * matriceCalculTmp[6]
	matriceResult[4] = matriceCalcul[3] * matriceCalculTmp[1] + matriceCalcul[4] * matriceCalculTmp[4] + matriceCalcul[5] * matriceCalculTmp[7]
	matriceResult[5] = matriceCalcul[3] * matriceCalculTmp[2] + matriceCalcul[4] * matriceCalculTmp[5] + matriceCalcul[5] * matriceCalculTmp[8]

	matriceResult[6] = matriceCalcul[6] * matriceCalculTmp[0] + matriceCalcul[7] * matriceCalculTmp[3] + matriceCalcul[8] * matriceCalculTmp[6]
	matriceResult[7] = matriceCalcul[6] * matriceCalculTmp[1] + matriceCalcul[7] * matriceCalculTmp[4] + matriceCalcul[8] * matriceCalculTmp[7]
	matriceResult[8] = matriceCalcul[6] * matriceCalculTmp[2] + matriceCalcul[7] * matriceCalculTmp[5] + matriceCalcul[8] * matriceCalculTmp[8]

	return matriceResult


def main():
	matriceCalcul = [1, 0, 0, 0, 1, 0, 0, 0, 1]
	x = float (sys.argv[1])
	y = float (sys.argv[2])

	argc = len(sys.argv)
	counter = 0
	
	if len(sys.argv) < 3:
				error()

	while (counter + 3) < argc:

		if (sys.argv[3 + counter]) == '-t':
			i = float (sys.argv[4 + counter])
			j = float (sys.argv[5 + counter])
			print ("Translation by the vector (%.f, %.f)") % (i, j)
			counter += 3
			matriceCalcul[2] = i
			matriceCalcul[5] = j

		elif (sys.argv[3 + counter]) == '-h':
			m = float(sys.argv[4 + counter])
			n = float(sys.argv[5 + counter])
			print("Homothety by the ratios %.f and %.f") % (m, n)
			counter += 3
			matriceCalcul[0] = m
			matriceCalcul[4] = n

		elif (sys.argv[3 + counter]) == '-r' :
			degree = float (sys.argv[4 + counter])
			print("Rotation at a %.f degree angle") % (degree)
			counter += 2
			angle = (math.pi / 180) * degree
			matriceCalculTmp = [math.cos(angle), math.sin(angle) * -1, 0, math.sin(angle), math.cos(angle), 0, 0, 0, 1]

			matriceCalcul = multiplication(matriceCalculTmp, matriceCalcul)

		elif (sys.argv[3 + counter]) == '-s':
			degree = float (sys.argv[4 + counter])
			print("Symmetry about an axis inclined with an angle of %.f degrees" % degree)
			counter += 2

			angle = (math.pi / 180) * degree
			matriceCalculTmp = [math.cos(angle * 2), math.sin(angle * 2), 0, math.sin(angle * 2), (math.cos(angle * 2) * -1), 0, 0, 0, 1]

			matriceCalcul = multiplication(matriceCalculTmp, matriceCalcul)

		elif (sys.argv[3 + counter]) == '-z':
			axis_x = float (sys.argv[4 + counter])
			axis_y = float (sys.argv[5 + counter])
			print("Scaling by factors %.f and %.f") % (axis_x, axis_y)
			counter += 3
			matriceCalculTmp = [axis_x, 0, 0, 0, axis_y, 0, 0, 0, 1]

			matriceCalcul = multiplication(matriceCalculTmp, matriceCalcul)

	result = [0, 0, 0]
	point = [x, y, 1.0]
	matrix = [[matriceCalcul[0], matriceCalcul[1], matriceCalcul[2]], [matriceCalcul[3], matriceCalcul[4], matriceCalcul[5]], [matriceCalcul[6], matriceCalcul[7], matriceCalcul[8]]]
	for i in range(3):
		for k in range(3):
			result[i] += matrix[i][k] * point[k]

	print("%.2f     %.2f     %.2f\n%.2f     %.2f     %.2f\n%.2f     %.2f     %.2f") % (matriceCalcul[0], matriceCalcul[1], matriceCalcul[2], matriceCalcul[3], matriceCalcul[4], matriceCalcul[5], matriceCalcul[6], matriceCalcul[7], matriceCalcul[8])
	print("(%.2f, %.2f) => (%.2f, %.2f)") % (x, y, result[0], result[1])
	return 0


def error():
			print("Syntax Error : Usage ./102architect x y transfo1 arg11 [arg12] [transfor2 arg12 [arg22]] ..\n")
			return 84


main()
