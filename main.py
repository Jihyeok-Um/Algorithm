n = int(input())
d = [[[0 for i in range(2)] for i in range(3)] for i in range(n+1)]
a = [0]
for i in range(n):
    a.append(int(input()))

d[1][1] = [a[1],0]

for i in range(2, n+1):
    d[i][2][0] = max(d[i-1][1]) + a[i]
    d[i][1][0] = max(d[i-1][0]) + a[i]
    d[i][0][1] = max(d[i-1][2])
    d[i][0][0] = max(d[i-1][1])

print(max(max(d[n][1]),max(d[n][2])))