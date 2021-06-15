from math import gcd

def solution(arr):
    ans = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        ans = lcm(ans, arr[i])
    return ans


def lcm(x, y):
    return x * y // gcd(x, y)
