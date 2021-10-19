n,m,y,x,k = map(int, input().split())
d = [0,2,3,1,4,5]
dice = [0,0,0,0,0,0]
order = []
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
order = list(map(int, input().split()))

def rollDice():
    if (matrix[y][x] == 0):
        matrix[y][x] = dice[d[5]]
    else:
        dice[d[5]] = matrix[y][x]
        matrix[y][x] = 0
    print(dice[d[0]])

for k in order:
    if (k == 1 and x <= m-2):
        x += 1
        d = [d[1],d[5],d[0],d[3],d[4],d[2]]
        rollDice()
    elif (k == 2 and x >= 1):
        x -= 1
        d = [d[2],d[0],d[5],d[3],d[4],d[1]]
        rollDice()
    elif (k == 3 and y >= 1):
        y -= 1
        d = [d[4],d[1],d[2],d[0],d[5],d[3]]
        rollDice()
    elif (k == 4 and y <= n-2):
        y += 1
        d = [d[3],d[1],d[2],d[5],d[0],d[4]]
        rollDice()
