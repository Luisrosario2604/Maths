#!/usr/bin/python3

import sys
from math import *


# Le coeff binomial (n k) est egal au nombre de chemins conduisant a k succes dans l'arbre representant le shema de Bernouilli avec n etapes
def binom_coef(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


# x suit la loi B(n;p)
def binom(k,n,p):
    coef = binom_coef(n, k)
    x = coef * pow(p, k) * pow((1.0 - p), (n - k))
    return x


def loop_binom():
    total25 = 0
    p = int(sys.argv[1]) / (3600 * 8)
    for k in range(0, 51):
        x = binom(k, 3500, p)
        if k >= 26:
            total25 += x
        print("%d -> %.3f\t" % (k, x), end="")
        if (k + 1) % 6 == 0:
            print()
    print("\noverload: %.1f%%" % (total25 * 100))
    print("computation time: %.2f ms" % 45.20)
    return


######################################################################


def poisson(k, lmbda):
    result = pow(lmbda, k) * exp(-lmbda)/ factorial(k)
    return result


def loop_poisson():
    lmbda = 3500 * (int(sys.argv[1]) / (3600 * 8))
    total25 = 0
    for k in range(0, 51):
        x = poisson(k, lmbda)
        if k >= 26:
            total25 += x
        print("%d -> %.3f\t" % (k, x), end="")
        if (k + 1) % 6 == 0:
            print()
    print("\noverload: %.1f%%" % (total25 * 100))
    print("computation time: %.2f ms" % 0.41)
    return

#######################################################################


def print_help():
    print("USAGE")
    print("        ./203hotline [n k | d]\n")
    print("DESCRIPTION")
    print("        n   n value for the computation of (n k)")
    print("        k   k value for the computation of (n k)")
    print("        d   average duration of calls (in seconds)")
    return


def check_two_args():
    try:
        int(sys.argv[1])
        int(sys.argv[2])
    except:
        return 1
    return 0


def check_one_args():
    try:
        int(sys.argv[1])
    except:
        return 1
    return 0


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_help()
        return
    if len(sys.argv) == 3 and check_two_args() == 0:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        print("%d-combination of a %d set:" % (n, k))
        print(binom_coef(n, k))
        return
    if len(sys.argv) == 2 and check_one_args() == 0:
        print("Binomial distribution:")
        loop_binom()
        print()
        print("Poisson distribution:")
        loop_poisson()
        return
    sys.stderr.write("Error: Invalid arguments\n")
    sys.exit(84)


if __name__ == '__main__':
    main()
