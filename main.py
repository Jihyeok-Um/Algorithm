testCase = int(input())
d = [[0]*4 for _ in range(100001)]
d[1][1] = d[2][2] = d[3][1] = d[3][2] = d[3][3] = 1

for i in range(4,100001):
    d[i][1] = d[i-1][2] + d[i-1][3]
    d[i][2] = d[i-2][1] + d[i-2][3]
    d[i][3] = d[i-3][1] + d[i-3][2]

for i in range(testCase):
    n = int(input())
    print(sum(d[n])%1000000009)