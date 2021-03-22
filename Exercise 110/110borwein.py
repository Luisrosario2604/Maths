#!/usr/bin/python3

import sys
import math


def help():
	print('USAGE')
	print('\t\t ./110borwiein n')
	print('\nDESCRIPTION')
	print('\n\tn  constant defining the integral to be computed')


def loop(k, n, i):
	ret = 1

	while k <= n:
		if i != 0:
			ret = ret * (math.sin((i) / (2 * k + 1)) / ((i) / (2 * k + 1)))
		k = k + 1
	return ret


def trap(n):
	i = 1
	k = 0
	result = 0
	while i < 10000:
		ret = loop(k, n, i * 0.5)
		result = result + ret
		i = i + 1
	result2 = ((result * 2) + loop(k, n, 0) + loop(k, n, 5000)) * 0.25
	diff = result2 - (math.pi / 2)
	print('Trapezoides:')
	print('I%d =  %.10f' % (n, result2))
	print('diff = %.10f' % abs(diff))


def rectangle(n):
	i = 0
	k = 0
	result = 0

	while i < 10000:
		ret = loop(k, n, i * 0.5)
		result = result + ret
		i = i + 1
	result = result * 0.5
	diff = result - (math.pi/2)
	print('Rectangles:')
	print('I%d =  %.10f' % (n, result))
	print('diff = %.10f' % abs(diff))


def simpson(n):
	i = 1
	k = 0
	result = 0
	result2 = 0
	while i < 10000:
		result = result + loop(k, n, i * 0.5)
		i = i + 1
	i = 0
	k = 0
	while i < 10000:
		result2 = result2 + loop(k, n, (i * 0.5) + 0.25)
		i = i + 1
	result3 = ((result * 2) + (result2 * 4) + loop(k, n, 0) + loop(k, n, 5000)) * (5/6) / 10
	diff = result3 - (math.pi / 2)
	print('Simpson:')
	print('I%d =  %.10f' % (n, result3))
	print('diff = %.10f' % abs(diff))


def decide(av):
	rectangle(float(av[1]))
	print()
	trap(float(av[1]))
	print()
	simpson(float(av[1]))


def error(av):
	if len(av) > 2:
		exit(84)
	if len(av) == 2:
		if av[1] == "-h":
			help()
			exit(0)

	try:
		float(av[1])
	except ValueError:
		exit(84)


def main(av):
	error(av)
	decide(av)


main(sys.argv)
