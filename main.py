import sys
sys.setrecursionlimit(200000)
max = -2000000000
min = 2000000000

def getResult(nArray, oArray, op1, op2, op3, op4, op, current, i):
    if (i == 0):
        if op == 0:
            current = nArray[i] + nArray[i + 1]
            op1 += 1
        elif op == 1:
            current = nArray[i] - nArray[i + 1]
            op2 += 1
        elif op == 2:
            current = nArray[i] * nArray[i + 1]
            op3 += 1
        elif op == 3:
            current = int(nArray[i] / nArray[i + 1])
            op4 += 1
            if (nArray[i] < 0 and nArray[i+1] > 0):
                current = int(((-1*nArray[i]) / nArray[i + 1])*-1)
    else:
        if op == 0:
            current = current + nArray[i + 1]
            op1 += 1
        elif op == 1:
            current = current - nArray[i + 1]
            op2 += 1
        elif op == 2:
            current = current * nArray[i + 1]
            op3 += 1
        elif op == 3:
            current = int(current / nArray[i + 1])
            op4 += 1
            if (current < 0 and nArray[i+1] > 0):
                current = int(((-1*current) / nArray[i + 1])*-1)

    global max
    global min

    if (i == len(nArray)-2 and oArray[0] == op1 and oArray[1] == op2 and oArray[2] == op3 and oArray[3] == op4):
        if current > max:
            max = current
        if current < min:
            min = current
        return 0
    elif (i == len(nArray)-2):
        return 0

    getResult(nArray, oArray, op1, op2, op3, op4, 0, current, i + 1)
    getResult(nArray, oArray, op1, op2, op3, op4, 1, current, i + 1)
    getResult(nArray, oArray, op1, op2, op3, op4, 2, current, i + 1)
    getResult(nArray, oArray, op1, op2, op3, op4, 3, current, i + 1)


def main():
    num = int(input())
    nArray = list(map(int, input().split()))
    oArray = list(map(int, input().split()))
    i = 0
    current = 0
    op1 = op2 = op3 = op4 = 0
    getResult(nArray, oArray, op1, op2, op3, op4, 0, current, i)
    getResult(nArray, oArray, op1, op2, op3, op4, 1, current, i)
    getResult(nArray, oArray, op1, op2, op3, op4, 2, current, i)
    getResult(nArray, oArray, op1, op2, op3, op4, 3, current, i)

    print(max)
    print(min)

main()