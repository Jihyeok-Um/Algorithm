from itertools import permutations

prime = [False for i in range(10000001)]


def isPrime():
    prime[0] = prime[1] = True
    for i in range(2, 10000000):
        if (prime[i] == False):
            j = i * i
            while (j <= 10000000):
                prime[j] = True
                j += i


def solution(numbers):
    isPrime()
    count = 0
    primeStore = []
    for i in range(len(numbers)):
        num = list(permutations(numbers, i + 1))
        for j in range(len(num)):
            temp = ""
            for k in range(len(num[j])):
                temp += num[j][k]
            if (prime[int(temp)] == False and int(temp) not in primeStore):
                primeStore.append(int(temp))
                count += 1

    return count

