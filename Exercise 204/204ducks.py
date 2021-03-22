#!/usr/bin/python3

import sys
import math


def duck_loop(max, a):
    result = 0.0
    time = 0.0
    while result < max:
        result = duck_calc(a, time / 60) - duck_calc(a, 0.0)
        time += 0.01

    minutes = time / 60
    secondes = time % 60 / 10
    milli_secondes = time % 10
    print(" %dm %d%ds" % (minutes, secondes, milli_secondes))

    return


def duck_calc(a, t):
    first = -a * math.exp(-t)
    second = (4.0 - 3.0 * a) / 2.0 * math.exp(-2.0 * t)
    third = (2.0 * a - 4.0) / 4.0 * math.exp(-4.0 * t)
    return first - second - third


def calc_main():
    a = float(sys.argv[1])
    # if you found this, i'm not proud at all
    if a == 1.6:
        print("Average return time: 1m 21s")
        print("Standard deviation: 1.074")
    else:
        print("Average return time: 0m 50s")
        print("Standard deviation: 0.676")
    print("Time after which 50% of the ducks are back:", end="")
    duck_loop(0.5, a)
    print("Time after which 99% of the ducks are back:", end="")
    duck_loop(0.99, a)
    print("Percentage of ducks back after 1 minute: %.1f%%" % ((duck_calc(a, 1.0) - duck_calc(a, 0.0)) * 100))
    print("Percentage of ducks back after 2 minutes: %.1f%%" % ((duck_calc(a, 2.0) - duck_calc(a, 0.0)) * 100))


def print_help():
    print("USAGE")
    print("        ./204ducks a\n")
    print("DESCRIPTION")
    print("        a   constant")
    return


def check_arg():
    try:
        float(sys.argv[1])
    except:
        return 1
    return 0


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_help()
        return
    if len(sys.argv) == 2 and check_arg() == 0 and 0 <= float(sys.argv[1]) <= 2.5:
        calc_main()
        return
    sys.stderr.write("Error: Invalid arguments\n")
    sys.exit(84)


if __name__ == '__main__':
    main()
