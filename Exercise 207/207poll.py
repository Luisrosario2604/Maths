#!/usr/bin/python3

import sys
from math import *


def variance(N, n, p):
    b = p * (1 - p)
    var = b / n
    var = var * ((N - n) / (N - 1))
    return var


def print_args():
    pSize = int(sys.argv[1])
    sSize = int(sys.argv[2])
    if pSize < 0:
        error(1)
    if sSize < 0:
        error(1)
    p = float(sys.argv[3]) / 100
    var = variance(pSize, sSize, p)
    p1 = (2 * 1.96 * sqrt(var)) / 2 * 100
    p2 = (2 * 2.58 * sqrt(var)) / 2 * 100
    c1min = p * 100 - p1
    c1max = p * 100 + p1
    c2min = p * 100 - p2
    c2max = p * 100 + p2
    if c1max > 100:
        c1max = 100
    if c1max < 0:
        c1max = 0
    if c2max > 100:
        c2max = 100
    if c2max < 0:
        c2max = 0
    if c1min > 100:
        c1min = 100
    if c1min < 0:
        c1min = 0
    if c2min > 100:
        c2min = 100
    if c2min < 0:
        c2min = 0
    print("Population size:\t\t%d" % pSize)
    print("Sample size:\t\t\t%d" % sSize)
    print("Voting intentions:\t\t%.2f%%" % (p * 100))
    print("Variance:\t\t\t%.6f" % var)
    print("95%% confidence interval:\t[%.2f%%; %.2f%%]" % (c1min, c1max))
    print("99%% confidence interval:\t[%.2f%%; %.2f%%]" % (c2min, c2max))


def error(i):
    if i == 1:
        sys.stderr.write("Error: Invalid arguments\n")
    elif i == 2:
        sys.stderr.write("Error: All Ox must be equal to 100\n")
    else:
        sys.stderr.write("Error\n")
    sys.exit(84)


def print_help():
    print("USAGE")
    print("\t./207poll pSize sSize p\n")
    print("DESCRIPTION")
    print("\tpSize\tsize of the population")
    print("\tsSize\tsize of the sample (supposed to be representative)")
    print("\tp\tpercentage of voting intentions for a specific candidate")
    return


def check_country(country, data):
    for row in data:
        if country == row[1]:
            return 0
    return 1


def check_float_arg(testing):
    try:
        float(testing)
    except:
        return 1
    return 0


def check_int_arg(testing):
    try:
        int(testing)
    except:
        return 1
    return 0


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_help()
        return
    if len(sys.argv) != 4:
        error(1)
    if check_int_arg(sys.argv[1]) != 0:
        error(1)
    if check_int_arg(sys.argv[2]) != 0:
        error(1)
    if check_float_arg(sys.argv[3]) != 0 or float(sys.argv[3]) > 100 or float(sys.argv[3]) < 0:
        error(1)
    print_args()
    return


if __name__ == '__main__':
    main()
