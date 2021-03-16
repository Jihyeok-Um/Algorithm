def getNextPermutations(array):
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

    return array


def getTSP(cities, count, cost):
    sum = 0
    for i in range(0, cities-1):
        if cost[count[i]][count[i+1]] != 0:
            sum += cost[count[i]][count[i+1]]
        else:
            return -1

    if cost[count[i+1]][count[0]] != 0:
        sum += cost[count[i+1]][count[0]]
    else:
        return -1

    return sum

def main():
    cities = int(input())
    count = [i for i in range(cities)]
    cost = []
    result = 10000000
    for i in range(cities):
        cost.append(list(map(int, input().split())))

    while(True):
        temp = getTSP(cities, count, cost)
        if temp != -1:
            result = min(temp,result)
        count = getNextPermutations(count)
        if (count == 0):
            break

    print(result)

main()