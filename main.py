n = int(input())
d = [0 for i in range(1000001)]
d[1] = 1
d[2] = 2
for i in range(3,1000001):
    d[i] = d[i-1] + d[i-2]
    d[i] %= 15746
print(d[n])