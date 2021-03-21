import sys
sys.setrecursionlimit(200000)
max1 = -1000000000
min1 = 1000000000

def getResult(nArray, op1, op2, op3, op4, current, i):
    global max1, min1
    if i == len(nArray):
        max1 = max(current, max1)
        min1 = min(current, min1)
        return 0
    else:
        if op1:
            getResult(nArray, op1-1, op2, op3, op4, current+nArray[i], i+1)
        if op2:
            getResult(nArray, op1, op2-1, op3, op4, current-nArray[i], i+1)
        if op3:
            getResult(nArray, op1, op2, op3-1, op4, current*nArray[i], i+1)
        if op4:
            getResult(nArray, op1, op2, op3, op4-1, int(current/nArray[i]), i+1)

def main():
    num = int(input())
    nArray = list(map(int, input().split()))
    op1, op2, op3, op4 = list(map(int, input().split()))

    getResult(nArray, op1, op2, op3, op4, nArray[0], 1)
    print(max1)
    print(min1)

main()