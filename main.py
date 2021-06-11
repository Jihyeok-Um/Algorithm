def solution(n, m):
    a = [n, m]
    while m != 0:
        remainder = n % m
        n = m
        m = remainder

    num = [n, int((a[0] * a[1]) / n)]
    return num