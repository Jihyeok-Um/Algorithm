import sys

def getNextArray(array):
    i = len(array)-1
    while (i > 0 and array[i-1] >= array[i]):
        i -= 1
    if (i == 0):
        for i in range(len(array)):
            print(array[i], end='')
        print()
        return

    j = len(array)-1
    while (array[j] <= array[i-1]):
        j -= 1
    array[j], array[i-1] = array[i-1], array[j]

    j = len(array) - 1
    while (i <= j):
        array[j], array[i] = array[i], array[j]
        i += 1
        j -= 1

    for i in range(len(array)):
        print(array[i], end='')
    print()

    return

def main():
    t = int(input())
    for i in range(t):
        array = list(sys.stdin.readline().rstrip())
        getNextArray(array)

main()