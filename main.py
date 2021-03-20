import sys
sys.setrecursionlimit(200000)

def check(current):
    ja = 0
    mo = 0
    for i in current:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            mo += 1
        else:
            ja += 1

    if (mo >= 1 and ja >= 2):
        return True
    else:
        return False


def getPassword(alpha,current,numOfAlpha, count):
    if (len(current) == numOfAlpha[0]):
        if check(current):
            print(current)
        return 0

    if (count >= len(alpha)):
        return 0
    getPassword(alpha, current+alpha[count], numOfAlpha, count + 1)
    getPassword(alpha, current, numOfAlpha, count + 1)

def main():
    count = 0
    current = ""
    numOfAlpha = list(map(int,input().split()))
    alpha = list(map(str,input().split()))
    alpha.sort()
    getPassword(alpha,current, numOfAlpha, count)

main()