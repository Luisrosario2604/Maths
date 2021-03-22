#!/usr/bin/python3

import sys


def proba(x, y):
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    result = 0.0 + (a - x) * (b - y)
    result = result / ((5 * a - 150) * (5 * b - 150))

    return result


def line():
    print("------------------------------------------------------")


def start_calc():
    total_y_10 = proba(10, 10) + proba(20, 10) + proba(30, 10) + proba(40, 10) + proba(50, 10)
    total_y_20 = proba(10, 20) + proba(20, 20) + proba(30, 20) + proba(40, 20) + proba(50, 20)
    total_y_30 = proba(10, 30) + proba(20, 30) + proba(30, 30) + proba(40, 30) + proba(50, 30)
    total_y_40 = proba(10, 40) + proba(20, 40) + proba(30, 40) + proba(40, 40) + proba(50, 40)
    total_y_50 = proba(10, 50) + proba(20, 50) + proba(30, 50) + proba(40, 50) + proba(50, 50)
    total_x_10 = proba(10, 10) + proba(10, 20) + proba(10, 30) + proba(10, 40) + proba(10, 50)
    total_x_20 = proba(20, 10) + proba(20, 20) + proba(20, 30) + proba(20, 40) + proba(20, 50)
    total_x_30 = proba(30, 10) + proba(30, 20) + proba(30, 30) + proba(30, 40) + proba(30, 50)
    total_x_40 = proba(40, 10) + proba(40, 20) + proba(40, 30) + proba(40, 40) + proba(40, 50)
    total_x_50 = proba(50, 10) + proba(50, 20) + proba(50, 30) + proba(50, 40) + proba(50, 50)

    t_20 = (total_x_10 * total_y_10)
    t_30 = (total_x_10 * total_y_20) + (total_x_20 * total_y_10)
    t_40 = (total_x_20 * total_y_20) + (total_x_30 * total_y_10) + (total_x_10 * total_y_30)
    t_50 = (total_x_30 * total_y_20) + (total_x_20 * total_y_30) + (total_x_40 * total_y_10) + (total_x_10 * total_y_40)
    t_60 = (total_x_30 * total_y_30) + (total_x_40 * total_y_20) + (total_x_20 * total_y_40) + (total_x_10 * total_y_50) + (total_x_50 * total_y_10)
    t_70 = (total_x_40 * total_y_30) + (total_x_30 * total_y_40) + (total_x_50 * total_y_20) + (total_x_20 * total_y_50)
    t_80 = (total_x_40 * total_y_40) + (total_x_30 * total_y_50) + (total_x_50 * total_y_30)
    t_90 = (total_x_40 * total_y_50) + (total_x_50 * total_y_40)
    t_100 = (total_x_50 * total_y_50)

    espe_x = (total_x_10 * 10) + (total_x_20 * 20) + (total_x_30 * 30) + (total_x_40 * 40) + (total_x_50 * 50)
    espe_y = (total_y_10 * 10) + (total_y_20 * 20) + (total_y_30 * 30) + (total_y_40 * 40) + (total_y_50 * 50)
    espe_z = (t_20 * 20) + (t_30 * 30) + (t_40 * 40) + (t_50 * 50) + (t_60 * 60) + (t_70 * 70) + (t_80 * 80) + (t_90 * 90) + (t_100 * 100)

    var_x = total_x_10 * (pow(10 - espe_x, 2)) + total_x_20 * (pow(20 - espe_x, 2)) + total_x_30 * (pow(30 - espe_x, 2)) + total_x_40 * (pow(40 - espe_x, 2)) + total_x_50 * (pow(50 - espe_x, 2))
    var_y = total_y_10 * (pow(10 - espe_y, 2)) + total_y_20 * (pow(20 - espe_y, 2)) + total_y_30 * (pow(30 - espe_y, 2)) + total_y_40 * (pow(40 - espe_y, 2)) + total_y_50 * (pow(50 - espe_y, 2))
    var_z = t_20 * (pow(20 - espe_z, 2)) + t_30 * (pow(30 - espe_z, 2)) + t_40 * (pow(40 - espe_z, 2)) + t_50 * (pow(50 - espe_z, 2)) + t_60 * (pow(60 - espe_z, 2)) + t_70 * (pow(70 - espe_z, 2)) + t_80 * (pow(80 - espe_z, 2)) + t_90 * (pow(90 - espe_z, 2)) + t_100 * (pow(100 - espe_z, 2))

    line()

    print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")

    print("Y=10\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" % (proba(10, 10), proba(20, 10), proba(30, 10), proba(40, 10), proba(50, 10), total_y_10))
    print("Y=20\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" % (proba(10, 20), proba(20, 20), proba(30, 20), proba(40, 20), proba(50, 20), total_y_20))
    print("Y=30\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" % (proba(10, 30), proba(20, 30), proba(30, 30), proba(40, 30), proba(50, 30), total_y_30))
    print("Y=40\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" % (proba(10, 40), proba(20, 40), proba(30, 40), proba(40, 40), proba(50, 40), total_y_40))
    print("Y=50\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" % (proba(10, 50), proba(20, 50), proba(30, 50), proba(40, 50), proba(50, 50), total_y_50))
    print("X law\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%d" % (total_x_10, total_x_20, total_x_30, total_x_40, total_x_50, 1))
    line()

    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100\ttotal")
    print("p(Z=z)\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t1" % (t_20, t_30, t_40, t_50, t_60, t_70, t_80, t_90, t_100))

    line()

    print("expected value of X:\t%.01f" % espe_x)
    print("variance of X:\t\t%.01f" % var_x)
    print("expected value of Y:\t%.01f" % espe_y)
    print("variance of Y:\t\t%.01f" % var_y)
    print("expected value of Z:\t%.01f" % espe_z)
    print("variance of Z:\t\t%.01f" % var_z)

    line()

    return


def check_two_args():
    try:
        int(sys.argv[1])
        int(sys.argv[2])
    except:
        return 1
    if int(sys.argv[1]) > 50 and int(sys.argv[2]) > 50:
        return 0
    return 1


def print_help():
    print("USAGE\n\t./202unsold a b\n")
    print("DESCRIPTION\n\t\ta\tconstant computed from the past results")
    print("\t\tb\tconstant computed from the past results")
    return


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_help()
        return 0
    if len(sys.argv) != 3 or check_two_args() != 0:
        sys.stderr.write("Error: Invalid arguments\n")
        sys.exit(84)
    start_calc()
    return 0


if __name__ == '__main__':
    main()
