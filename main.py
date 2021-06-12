def solution(n):
    temp = []
    while (n > 0):
        temp.append(n % 3)
        n = n // 3

    count = 1
    for i in range(len(temp) - 1):
        count *= 10

    num = 0
    for i in range(len(temp)):
        num += temp[i] * count
        count = count // 10

    return int(str(num), 3)