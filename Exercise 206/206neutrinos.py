#!/usr/bin/python3

import sys
from math import *


def average(x, y, n):
    result = 0.0
    result += x * n + y
    result = result / (n + 1)
    return result


def error(i):
    if i == 1:
        sys.stderr.write("Error: Invalid arguments\n")
    elif i == 2:
        sys.stderr.write("Error: Bad input\n")
    else:
        sys.stderr.write("Error\n")
    sys.exit(84)


def truncate(f, n):
    return floor(f * 10 ** n) / 10 ** n


def print_help():
    print("USAGE")
    print("\t./206neutrinos n a h sd\n")
    print("DESCRIPTION")
    print("\tn\tnumber of values")
    print("\ta\tarithmetic mean")
    print("\th\tharmonic mean")
    print("\tsd\tstrandard deviation")
    return


def check_arg(testing):
    try:
        int(testing)
    except:
        return 1
    if int(testing) < 0:
        return 1
    return 0


def average_trunked(n, input_user, h):
    result = 0.0
    result += (n - 1) / h
    result += 1 / input_user
    result = n / result
    return result


def get_standard_devi(pow_sd_a_n, input_user, n, a):
    result = 0.0
    result += (pow_sd_a_n + input_user ** 2) / n
    result = result - a ** 2
    return sqrt(result)


def get_root_mean(pow_sd_a_n, input_user, n):
    result = 0.0
    result += pow_sd_a_n + input_user ** 2
    return sqrt(result / n)


def loop(n, a, h, sd):
    input_user = ""
    while input_user != 'END':
        print("Enter next value: ", end='')
        try:
            input_user = input()
            if check_arg(input_user) == 0:
                input_user = float(input_user)
                pow_sd_a_n = (sd ** 2 + a ** 2) * (n - 1)
                a = average(a, input_user, n)
                sd = get_standard_devi(pow_sd_a_n, input_user, n, a)
                rms = get_root_mean(pow_sd_a_n, input_user, n)
                h = average_trunked(n, input_user, h)
                print("\tNumber of values:\t%d" % n)
                print("\tStandard deviation:\t%.2f" % sd)
                print("\tArithmetic mean:\t%.2f" % a)
                print("\tRoot mean square:\t%.2f" % rms)
                print("\tHarmonic mean:\t\t%.2f\n" % h)
                n += 1
            elif input_user == 'END':
                return
            else:
                error(2)
        except KeyboardInterrupt:
            error(2)
        except EOFError:
            error(2)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_help()
        return
    if len(sys.argv) != 5:
        error(1)
    if check_arg(sys.argv[1]) != 0:
        error(1)
    if check_arg(sys.argv[2]) != 0:
        error(1)
    if check_arg(sys.argv[3]) != 0:
        error(1)
    if check_arg(sys.argv[4]) != 0:
        error(1)
    loop(int(sys.argv[1]) + 1, int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))


if __name__ == '__main__':
    main()
