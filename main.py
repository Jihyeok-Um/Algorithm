def getNextArray(array):
    max = 0
    while(True):
        i = len(array)-1
        while (i > 0 and array[i-1] >= array[i]):
            i -= 1
        if (i == 0):
            break

        j = len(array)-1
        while (array[j] <= array[i-1]):
            j -= 1
        array[j], array[i-1] = array[i-1], array[j]

        j = len(array) - 1
        while (i <= j):
            array[j], array[i] = array[i], array[j]
            i += 1
            j -= 1

        sum = 0
        for k in range(0, len(array)-1):
            if (array[k]-array[k+1] < 0):
                sum += (array[k] - array[k + 1]) * -1
            else:
                sum += (array[k] - array[k+1])

        if (sum > max):
            max = sum

    return max

def main():
    arraySize = int(input())
    array = list(map(int,input().split()))
    array.sort()
    print(getNextArray(array))

main()