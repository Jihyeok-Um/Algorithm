def getNextPermutations(array, cost):
    i = len(array) - 1
    while (i > 0 and array[i - 1] >= array[i]):
        i -= 1
    if (i == 0):
        return 0

    j = len(array) - 1
    while (array[j] <= array[i - 1]):
        j -= 1
    array[j], array[i - 1] = array[i - 1], array[j]

    j = len(array) - 1
    while (i <= j):
        array[j], array[i] = array[i], array[j]
        i += 1
        j -= 1

    getCombination(array, cost)
    return array

def getCombination(array, cost):
    result = []
    for i in range(0, len(array)):
        if array[i] == 0:
            result.append(cost[i])

    for i in range(len(result)):
        print(result[i], end=' ')
    print("")


def main():
    while(True):
        cost = list(map(int, input().split()))
        if cost[0] == 0:
            break
        array2 = []
        for i in range(0, cost[0]):
            if i < 6:
                array2.append(0)
            else:
                array2.append(1)

        cost.remove(cost[0])
        cost.sort()
        array2.sort()
        getCombination(array2, cost)
        while(True):
            count = getNextPermutations(array2, cost)
            if (count == 0):
                print("")
                break

main()