import sys
sys.setrecursionlimit(200000)
max = 0

def getBiggestMoney(T, P, sum, day, i):
    global max
    if (day == len(T)+1):
        if (sum > max):
            max = sum
        return 0
    elif (day > len(T)+1):
        return 0

    getBiggestMoney(T, P, sum+P[i], day+T[i], i+T[i])
    getBiggestMoney(T, P, sum, day+1, i+1)

def main():
    num = int(input())
    T = []
    P = []
    sum = 0
    day = 1
    j = 0

    for i in range(num):
        temp = list(map(int, input().split()))
        T.append(temp[0])
        P.append(temp[1])
        temp = []

    getBiggestMoney(T, P, sum, day, j)
    print(max)

main()