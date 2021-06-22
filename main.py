def binary(s):
    num = bin(s)
    return num


def solution(s):
    zero = 0
    binCount = 0
    while (s != "0b1"):
        ss = ""
        for i in range(len(s)):
            if (s[i] == "1"):
                ss += s[i]
            elif (s[i] == "0"):
                zero += 1
        zero -= 1
        s = str(binary(len(ss)))
        binCount += 1

    return [binCount, zero + 1]