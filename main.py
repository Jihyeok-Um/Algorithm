
def getNextArray(array):
    i = len(array)-1
    while (i > 0 and array[i-1] >= array[i]):
        i -= 1
    if (i == 0):
        return 0

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
        print(array[i], end=' ')

    print()
    return array

def main():
    arraySize = int(input())
    array = [i for i in range(1,arraySize+1)]
    for i in range(len(array)):
        print(array[i], end=' ')
    print()
    while(array != 0):
        array = getNextArray(array)

main()