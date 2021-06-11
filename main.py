def solution(n):
    count = 1
    num = []
    while (n // count != 0):
        count *= 10
    count = count // 10
    temp = count

    while (count != 1):
        num.append(n // count)
        n %= count
        count = count // 10
    num.append(n)
    num.sort(reverse=True)
    num2 = 0
    for i in num:
        num2 += i * temp
        temp = temp // 10

    return num2


