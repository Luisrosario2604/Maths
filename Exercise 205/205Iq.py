#!/usr/bin/python3

import sys
from math import *


def calc(u, a, i):
    first = 1 / (a * sqrt(2 * pi))
    second = exp(- (pow(i - u, 2) / (2 * pow(a, 2))))
    return first * second


def error():
    sys.stderr.write("Error: Invalid arguments\n")
    sys.exit(84)


def print_help():
    print("USAGE")
    print("\t./205IQ u s [IQ1] [IQ2]\n")
    print("DESCRIPTION")
    print("\tu\tmean")
    print("\ts\tstandar deviation")
    print("\tIQ1\tminimum IQ")
    print("\tIQ2\tmaximum IQ")
    return


def check_arg(testing):
    try:
        int(testing)
    except:
        return 1
    return 0


def three_param():
    u = int(sys.argv[1])
    a = int(sys.argv[2])
    for i in range(0, 201):
        print("%d %.5f" % (i, calc(u, a, i)))
    return


def four_param():
    u = int(sys.argv[1])
    a = int(sys.argv[2])
    q1 = int(sys.argv[3])
    result = 0.0
    i = 0.00
    while i <= 200:
        if q1 > i:
            result += calc(u, a, i)
        if q1 == i:
            result += calc(u, a, i) / 2
        i += 0.01
    print("%.1f%% of people have an IQ inferior to %i" % (result, q1))
    return


def five_param():
    u = int(sys.argv[1])
    a = int(sys.argv[2])
    q1 = int(sys.argv[3])
    q2 = int(sys.argv[4])
    result = 0.0
    i = 0.00
    while i <= 200:
        if q2 > i >= q1:
            result += calc(u, a, i)
        i += 0.01
    print("%.1f%% of people have an IQ between %d and %d" % (result, q1, q2))
    return


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_help()
        return
    if len(sys.argv) > 5:
        error()
    if len(sys.argv) < 3:
        error()
    if len(sys.argv) == 3:
        if check_arg(sys.argv[1]) == 1 or check_arg(sys.argv[2]) == 1 or int(sys.argv[1]) > 200 or int(sys.argv[1]) < 0:
            error()
        three_param()
        return
    if check_arg(sys.argv[1]) == 1 or check_arg(sys.argv[2]) == 1 or int(sys.argv[1]) > 200 or int(sys.argv[1]) < 0:
        error()
    if len(sys.argv) == 4:
        if check_arg(sys.argv[3]) == 1:
            error()
        four_param()
        return
    if check_arg(sys.argv[3]) == 1:
        error()
    if len(sys.argv) == 5:
        if check_arg(sys.argv[4]) == 1:
            error()
        five_param()
        return
    error()


if __name__ == '__main__':
    main()
