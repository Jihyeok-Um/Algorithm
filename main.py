n, k = map(int, input().split())
d = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(0, n+1):
    for j in range(0, i + 1):
        if (j == 0):
            d[i][j] = 1
        elif (j == i):
            d[i][j] = 1
        elif (j != 0 and j != i):
            d[i][j] = d[i-1][j-1] + d[i-1][j]

print(d[n][k] % 10007)