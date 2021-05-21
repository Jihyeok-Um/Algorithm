n = int(input())
mod = 10007
d = [[0 for i in range(10)] for i in range(n)]
for i in range(0,10):
    d[0][i] = 1

for i in range(1,n):
    for j in range(0,10):
        k = 0
        while(k <= j):
            d[i][j] += d[i-1][k]
            k += 1
            d[i][j] %= 10007


print((sum(d[n-1])) % 10007)