def solution(s):
    countP = 0
    countY = 0

    for i in range(len(s)):
        if (s[i] == "p" or s[i] == "P"):
            countP += 1
        elif (s[i] == "y" or s[i] == "Y"):
            countY += 1
    if (countP == countY):
        return True
    else:
        return False