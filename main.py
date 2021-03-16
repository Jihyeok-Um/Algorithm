def main():
    arraySize = int(input())
    array = list(map(int, input().split()))

    i = arraySize-1
    while (i > 0 and array[i-1] > array[i]):
        i -= 1

    if (i == 0):
        print(-1)
        return 0

    j = arraySize-1
    while (array[j] < array[i-1]):
        j -= 1
    array[j], array[i-1] = array[i-1], array[j]

    j = arraySize - 1
    while (i <= j):
        array[j], array[i] = array[i], array[j]
        i += 1
        j -= 1

    for i in range(len(array)):
        print(array[i], end=' ')

main()