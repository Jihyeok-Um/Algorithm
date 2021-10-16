s,n = map(int,input().split())
n = str(n)
num = [["" for i in range(2*s+3)] for i in range(10)]


def makeOne(s):
    for i in range(2*s+3):
        if (i == 0 or i == s+1 or i == 2*s+2):
            for j in range(s+2):
                num[1][i] += " "
        else:
            for j in range(s+1):
                num[1][i] += " "
            num[1][i] += "|"

def makeTwo(s):
    for i in range(2*s+3):
        if (i == 0 or i == s+1 or i == 2*s+2):
            for j in range(s+2):
                if (j == 0 or j == s+1):
                    num[2][i] += " "
                else:
                    num[2][i] += "-"
        elif (i > 0 and i <= s):
            for j in range(s+1):
                num[2][i] += " "
            num[2][i] += "|"
        else:
            num[2][i] += "|"
            for j in range(s+1):
                num[2][i] += " "

def makeThree(s):
    for i in range(2 * s + 3):
        if (i == 0 or i == s + 1 or i == 2 * s + 2):
            for j in range(s + 2):
                if (j == 0 or j == s + 1):
                    num[3][i] += " "
                else:
                    num[3][i] += "-"
        else:
            for j in range(s + 1):
                num[3][i] += " "
            num[3][i] += "|"

def makeFour(s):
    for i in range(2*s+3):
        if (i == 0 or i == 2*s+2):
            for j in range(s+2):
                num[4][i] += " "
        elif (i == s+1):
            for j in range(s + 2):
                if (j == 0 or j == s + 1):
                    num[4][i] += " "
                else:
                    num[4][i] += "-"
        elif (i > 0 and i <= s):
            num[4][i] += "|"
            for j in range(s):
                num[4][i] += " "
            num[4][i] += "|"
        else:
            for j in range(s+1):
                num[4][i] += " "
            num[4][i] += "|"

def makeFive(s):
    for i in range(2 * s + 3):
        if (i == 0 or i == s + 1 or i == 2 * s + 2):
            for j in range(s + 2):
                if (j == 0 or j == s + 1):
                    num[5][i] += " "
                else:
                    num[5][i] += "-"
        elif (i > s+1 and i < 2*s+2):
            for j in range(s + 1):
                num[5][i] += " "
            num[5][i] += "|"
        else:
            num[5][i] += "|"
            for j in range(s + 1):
                num[5][i] += " "

def makeSix(s):
    for i in range(2 * s + 3):
        if (i == 0 or i == s + 1 or i == 2 * s + 2):
            for j in range(s + 2):
                if (j == 0 or j == s + 1):
                    num[6][i] += " "
                else:
                    num[6][i] += "-"
        elif (i > s+1 and i < 2*s+2):
            num[6][i] += "|"
            for j in range(s):
                num[6][i] += " "
            num[6][i] += "|"
        else:
            num[6][i] += "|"
            for j in range(s + 1):
                num[6][i] += " "

def makeSeven(s):
    for i in range(2 * s + 3):
        if (i == 0):
            for j in range(s + 2):
                if (j == 0 or j == s + 1):
                    num[7][i] += " "
                else:
                    num[7][i] += "-"
        elif(i == s + 1 or i == 2 * s + 2):
            for j in range(s+2):
                num[7][i] += " "
        else:
            for j in range(s+1):
                num[7][i] += " "
            num[7][i] += "|"

def makeEight(s):
    for i in range(2 * s + 3):
        if (i == 0 or i == s + 1 or i == 2 * s + 2):
            for j in range(s + 2):
                if (j == 0 or j == s + 1):
                    num[8][i] += " "
                else:
                    num[8][i] += "-"
        else:
            num[8][i] += "|"
            for j in range(s):
                num[8][i] += " "
            num[8][i] += "|"

def makeNine(s):
    for i in range(2 * s + 3):
        if (i == 0 or i == s + 1 or i == 2 * s + 2):
            for j in range(s + 2):
                if (j == 0 or j == s + 1):
                    num[9][i] += " "
                else:
                    num[9][i] += "-"
        elif(i > 0 and i <= s):
            num[9][i] += "|"
            for j in range(s):
                num[9][i] += " "
            num[9][i] += "|"
        else:
            for j in range(s+1):
                num[9][i] += " "
            num[9][i] += "|"

def makeZero(s):
    for i in range(2 * s + 3):
        if (i == 0 or i == 2 * s + 2):
            for j in range(s + 2):
                if (j == 0 or j == s + 1):
                    num[0][i] += " "
                else:
                    num[0][i] += "-"
        elif (i == s+1):
            for j in range(s+2):
                num[0][i] += " "
        else:
            num[0][i] += "|"
            for j in range(s):
                num[0][i] += " "
            num[0][i] += "|"

makeOne(s)
makeTwo(s)
makeThree(s)
makeFour(s)
makeFive(s)
makeSix(s)
makeSeven(s)
makeEight(s)
makeNine(s)
makeZero(s)

for i in range(len(num[0])):
    for j in range(len(n)):
        print(num[int(n[j])][i], end=' ')
    print()