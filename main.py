n = int(input())
d = [100000 for i in range(n+1)]
d[0] = 0
d[1] = 1

for i in range(1,n+1):
    j = 1
    while (j*j <= i):
        if (d[i] > d[i-(j*j)]+1):
            d[i] = d[i-(j*j)]+1
        j += 1

print(d[n])