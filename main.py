import sys
sys.setrecursionlimit(1000000)

f = [-1 for i in range(1000000)]
def solution(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        if (f[n] != -1):
            return f[n] % 1234567
        else:
            f[n] = solution(n-1)+solution(n-2)
            return f[n] % 1234567