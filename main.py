n = int(input())
mod = 1000000000
d = [[0]*10 for i in range(n+1)]
d[1][1] = d[1][2] = d[1][3] = d[1][4] = d[1][5] = d[1][6] = d[1][7] = d[1][8] = d[1][9] = 1

for i in range(2,n+1):
    for j in range(0,10):
        if (j != 0 and j != 9):
            d[i][j] = d[i-1][j+1] + d[i-1][j-1]
        elif (j == 0):
            d[i][j] = d[i-1][j+1]
        elif (j == 9):
            d[i][j] = d[i-1][j-1]

print(sum(d[n]) % 1000000000)