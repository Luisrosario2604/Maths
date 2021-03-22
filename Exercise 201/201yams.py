#!/usr/bin/python3

import sys
import math


def calcFull(three, pair):
    occurenceThree = getGoods(three)
    occurencePair = getGoods(pair)
    if occurencePair > 2:
        occurencePair = 2
    if occurenceThree > 3:
        occurenceThree = 3
    totalOccurence = 5.0 - occurencePair - occurenceThree - 1
    if totalOccurence < 0:
        totalOccurence = 0
    roll = 5 - occurenceThree - occurencePair
    result = ((calcThree(getGoods(three), roll) / 100.0) * (calcPair(getGoods(pair), roll)) / 100.0) / pow(6.0, totalOccurence)
    return result * 100


def calcThree(good, toThrow):
    total = 0
    if good > 2:
        return 100
    toFind = 3 - good

    while toFind <= toThrow:
        total += (math.factorial(toThrow) / (math.factorial(toFind) * math.factorial(toThrow - toFind))) * (math.pow(1.0 / 6.0, toFind)) * (math.pow(5.0 / 6.0, toThrow - toFind))
        toFind += 1

    return total * 100


def calcPair(good, toThrow):
    total = 0
    if good >= 2:
        return 100
    toFind = 2 - good

    while toFind <= toThrow:
        total += (math.factorial(toThrow) / (math.factorial(toFind) * math.factorial(toThrow - toFind))) * (math.pow(1.0 / 6.0, toFind)) * (math.pow(5.0 / 6.0, toThrow - toFind))
        toFind += 1

    return total * 100


def getStraightGoods(nbr):
    one = int(sys.argv[1])
    two = int(sys.argv[2])
    three = int(sys.argv[3])
    four = int(sys.argv[4])
    five = int(sys.argv[5])
    good = 0
    nbr = int(nbr)

    if one == nbr - 4 or two == nbr - 4 or three == nbr - 4 or four == nbr - 4 or five == nbr - 4:
        good += 1
    if one == nbr - 3 or two == nbr - 3 or three == nbr - 3 or four == nbr - 3 or five == nbr - 3:
        good += 1
    if one == nbr - 2 or two == nbr - 2 or three == nbr - 2 or four == nbr - 2 or five == nbr - 2:
        good += 1
    if one == nbr - 1 or two == nbr - 1 or three == nbr - 1 or four == nbr - 1 or five == nbr - 1:
        good += 1
    if one == nbr or two == nbr or three == nbr or four == nbr or five == nbr:
        good += 1
    return good


def calcStraight(nbr):
    good = getStraightGoods(nbr)
    percent = 1.0
    if good == 5:
        return 100
    good = 5 - good
    while good > 0:
        percent *= good / 6.0
        good -= 1
    return percent * 100


def getGoods(nbr):
    good = 0
    if sys.argv[1] == nbr:
        good += 1
    if sys.argv[2] == nbr:
        good += 1
    if sys.argv[3] == nbr:
        good += 1
    if sys.argv[4] == nbr:
        good += 1
    if sys.argv[5] == nbr:
        good += 1
    return good


def calcYams(nbr):
    result = 1.0
    good = getGoods(nbr)
    if good == 5:
        return 100
    while good < 5:
        result /= 6
        good += 1
    return result * 100


def calcFour(nbr):
    result = 0.0
    good = getGoods(nbr)
    if good == 4 or good == 5:
        return 100
    good = 5 - good
    result += (good * 5)
    result += 1
    result /= pow(6, good)
    return result * 100


def parserCombinaison():
    if "pair_" in sys.argv[6]:
        if int(sys.argv[6][5]) > 6 or int(sys.argv[6][5]) < 0:
            return 84
        good = getGoods(sys.argv[6][5])
        result = calcPair(good, 5 - good)
        print("chances to get a %c pair:  %.2f%%" % (sys.argv[6][5], result))
        return 0
    if "three_" in sys.argv[6]:
        if int(sys.argv[6][6]) > 6 or int(sys.argv[6][6]) < 0:
            return 84
        good = getGoods(sys.argv[6][6])
        result = calcThree(good, 5 - good)
        print("chances to get a %c three-of-a-kind:  %.2f%%" % (sys.argv[6][6], result))
        return 0
    if "four_" in sys.argv[6]:
        if int(sys.argv[6][5]) > 6 or int(sys.argv[6][5]) < 0:
            return 84
        result = calcFour(sys.argv[6][5])
        print("chances to get a %c four-of-a-kind:  %.2f%%" % (sys.argv[6][5], result))
        return 0
    if "straight_" in sys.argv[6]:
        if int(sys.argv[6][9]) > 6 or int(sys.argv[6][9]) < 5:
            return 84
        result = calcStraight(sys.argv[6][9])
        print("chances to get a %c straight:  %.2f%%" % (sys.argv[6][9], result))
        return 0
    if "yams_" in sys.argv[6]:
        if int(sys.argv[6][5]) > 6 or int(sys.argv[6][5]) < 0:
            return 84
        result = calcYams(sys.argv[6][5])
        print("chances to get a %c yams:  %.2f%%" % (sys.argv[6][5], result))
        return 0
    if "full_" in sys.argv[6]:
        if int(sys.argv[6][5]) > 6 or int(sys.argv[6][5]) < 0:
            return 84
        if int(sys.argv[6][7]) > 6 or int(sys.argv[6][7]) < 0:
            return 84
        result = calcFull(sys.argv[6][5], sys.argv[6][7])
        print("chances to get a %c full of %c:  %.2f%%" % (sys.argv[6][5], sys.argv[6][7], result))
        return 0
    return 84


def checkDiceValue():
    if int(sys.argv[1]) > 6 or int(sys.argv[1]) < 0:
        return 84
    if int(sys.argv[2]) > 6 or int(sys.argv[2]) < 0:
        return 84
    if int(sys.argv[3]) > 6 or int(sys.argv[3]) < 0:
        return 84
    if int(sys.argv[4]) > 6 or int(sys.argv[4]) < 0:
        return 84
    if int(sys.argv[5]) > 6 or int(sys.argv[5]) < 0:
        return 84
    return 0


def printMyH():
    print("USAGE\n\t./201yams d1 d2 d3 d4 d5 c\n")
    print("DESCRIPTION\n\td1\tvalue of the first die (0 if not thrown)")
    print("\td2\tvalue of the second die (0 if not thrown)")
    print("\td3\tvalue of the third die (0 if not thrown)")
    print("\td4\tvalue of the fourth die (0 if not thrown)")
    print("\td5\tvalue of the fifth die (0 if not thrown)")
    print("\tc\texpected combination")
    return


def main():
    global period
    if len(sys.argv) != 7:
        sys.stderr.write("Error: Invalid arguments\n")
        sys.exit(84)
    if sys.argv[1] == '-h' and len(sys.argv) == 2:
        printMyH()
        return 0
    if checkDiceValue() != 0:
        sys.stderr.write("Error: Invalid arguments\n")
        sys.exit(84)
    if parserCombinaison() == 84:
        sys.stderr.write("Error: Invalid arguments\n")
        sys.exit(84)
    return 0


if __name__ == '__main__':
    main()
