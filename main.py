import sys
sys.setrecursionlimit(100000)
d = [0 for i in range(10001)]
n = [[0,0] for i in range(41)]
n[0] = [1,0]
n[1] = [0,1]

def fibonaci(num):
    if (num == 0):
        return 0
    if (num == 1):
        d[num] = 1
        return d[num]
    if (d[num] != 0):
        return d[num]
    else:
        d[num] = fibonaci(num-1) + fibonaci(num-2)
        for i in range(0,2):
            n[num][i] = n[num-1][i] + n[num-2][i]
        return d[num]

t = int(input())
fibonaci(40)

for i in range(t):
    num = int(input())
    for j in range(0,2):
        print(n[num][j], end=' ')