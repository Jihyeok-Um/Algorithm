import sys

sys.setrecursionlimit(100000)

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
three = ["one", "two", "six"]
four = ["zero", "four", "five", "nine"]
five = ["three", "seven", "eight"]


def solution(s):
    result = ""
    for i in range(50):
        if (s[:1] in num):
            result += s[:1]
            s = s[1:]
        elif (s[:3] in three):
            ss = s[:3]
            if (ss == three[0]):
                result += "1"
            elif (ss == three[1]):
                result += "2"
            elif (ss == three[2]):
                result += "6"
            s = s[3:]
        elif (s[:4] in four):
            ss = s[:4]
            if (ss == four[0]):
                result += "0"
            elif (ss == four[1]):
                result += "4"
            elif (ss == four[2]):
                result += "5"
            elif (ss == four[3]):
                result += "9"
            s = s[4:]
        elif (s[:5] in five):
            ss = s[:5]
            if (ss == five[0]):
                result += "3"
            elif (ss == five[1]):
                result += "7"
            elif (ss == five[2]):
                result += "8"
            s = s[5:]

    return int(result)