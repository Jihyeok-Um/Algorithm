testCase = int(input())
mod = 1000000009
d = [0]*1000001
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(testCase):
    n = int(input())
    if(n >= 4):
        for i in range(4, n+1):
            d[i] = d[i-1]+d[i-2]+d[i-3]
            d[i] %= mod
    print(d[n] % mod)