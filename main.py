import sys

def getSum(num, current, addNum):
    current = current + addNum

    if num < current:
        return 0
    elif num == current:
        return 1

    count = 0
    for i in range(1,4):
        sys.setrecursionlimit(200000)
        count += getSum(num, current, i)

    return count


def main():
    testCase = int(input())

    for i in range(testCase):
        num = int(input())
        print(getSum(num, 0, 0))

main()