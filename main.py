# 정수 제곱근 판별

import math

def solution(n):
    num = math.sqrt(float(n))
    if (num == int(num)):
        return (num + 1) * (num + 1)
    else:
        return -1

