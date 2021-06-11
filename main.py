def solution(n):
    count = 1
    while (n / count != 0):
        count *= 10
    count = count // 10

    result = 0
    while (count != 1):
        result += n // count
        n = n % count
        count = count // 10
    result += n
    return result