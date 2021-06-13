from itertools import combinations

array = [False for i in range(10001)]


def solution(nums):
    get_prime(1, 10000)
    store = list(combinations(nums, 3))
    for i in range(len(store)):
        store[i] = store[i][0] + store[i][1] + store[i][2]

    count = 0
    for i in range(len(store)):
        if (array[store[i]] == False):
            count += 1

    return count


def get_prime(min, max):
    for i in range(2, max + 1):
        if (array[i] == False):
            j = i * i
        while (j <= max):
            array[j] = True
            j += i