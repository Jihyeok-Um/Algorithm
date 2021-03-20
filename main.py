import sys
pa = 0

def getSmallArray(howManyNum, array, currentSum, goalSum, count, add):
    if (count == howManyNum):
        if (currentSum == goalSum and add > 0):
            global pa
            pa += 1
        return 0

    sys.setrecursionlimit(200000)
    getSmallArray(howManyNum, array, currentSum+array[count], goalSum, count+1, add+1)
    getSmallArray(howManyNum, array, currentSum, goalSum, count+1, add)

def main():
    temp = list(map(int, input().split()))
    howManyNum = temp[0]
    goalSum = temp[1]
    array = list(map(int, input().split()))
    currentSum = 0
    count = 0
    add = 0
    getSmallArray(howManyNum, array, currentSum, goalSum, count, add)
    print(pa)

main()