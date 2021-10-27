import sys
final = False
t = int(input())
for i in range(t):
    array = list(sys.stdin.readline().rstrip())
    for k in range(len(array)):
        array[k] = ord(array[k])

    i = len(array)-1
    while (i > 0 and array[i-1] > array[i]):
        i -= 1

    if (i == 0):
        for k in array:
            print(chr(k),end='')
        print()
        final = True

    j = len(array)-1
    while (array[j] < array[i-1]):
        j -= 1
    array[j], array[i-1] = array[i-1], array[j]

    j = len(array) - 1
    while (i <= j):
        array[j], array[i] = array[i], array[j]
        i += 1
        j -= 1

    if final == False:
        for k in array:
            print(chr(k), end='')
        print()
