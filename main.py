n = int(input())
dice = []
opposite = [5,3,4,1,2,0]
for i in range(n):
    dice.append(list(map(int, input().split())))

sum = [0 for i in range(6)]
for i in range(6):
    m = 0
    up = dice[0][opposite[i]]
    for j in range(6):
        if (j != i and j != opposite[i]):
            if (dice[0][j] > m):
                m = dice[0][j]
    sum[i] += m
    for j in range(1, n):
        s = dice[j].index(up)
        up = dice[j][opposite[dice[j].index(up)]]
        m = 0
        for k in range(6):
            if (k != s and k != opposite[s]):
                if (dice[j][k] > m):
                    m = dice[j][k]
        sum[i] += m
print(max(sum))