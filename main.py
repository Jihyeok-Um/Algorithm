from collections import deque
import copy
q = deque()

n = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1]
matrix = []
check = [[0 for i in range(n)] for i in range(n)]
bfsCheck = [[0 for i in range(n)] for i in range(n)]
visit = [[False for i in range(n)] for i in range(n)]
fish = [0 for i in range(400)]
sharkSize = 2
eaten = 0
time = 0
for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if(matrix[i][j] == 9):
            bfsCheck[i][j] = 9
            q.append([j,i])
        elif(matrix[i][j] >= 1 and matrix[i][j] <= 6):
            fish[matrix[i][j]] += 1
            if (matrix[i][j] < sharkSize):
                bfsCheck[i][j] = matrix[i][j]
            elif (matrix[i][j] > sharkSize):
                bfsCheck[i][j] = -1
                check[i][j] = -1

def bfs():
    while(q):
        p = q.popleft()
        visit[p[1]][p[0]] = True
        for i in range(4):
            if(p[0]+dx[i]>=0 and p[0]+dx[i]<n and p[1]+dy[i]>=0 and p[1]+dy[i]<n and check[p[1]+dy[i]][p[0]+dx[i]] != -1 and visit[p[1]+dy[i]][p[0]+dx[i]] == False):
                check[p[1]+dy[i]][p[0]+dx[i]] = check[p[1]][p[0]] + 1
                q.append([p[0]+dx[i],p[1]+dy[i]])


while(True):
    total = 0
    for i in range(sharkSize):
        total += fish[i]
    if (total == 0):
        break
    eaten += 1
    if (eaten == sharkSize):
        eaten = 0
        sharkSize += 1
    eatFish = [0]
    shortest = n*n
    bfs()
    for i in range(n):
        print(matrix[i])
    print()
    for i in range(n):
        print(check[i])
    print()
    print(sharkSize, eaten)
    print(time)
    print()
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if (check[i][j] <= shortest and bfsCheck[i][j] != 9 and bfsCheck[i][j] != 0 and check[i][j] != -1 and (sharkSize > matrix[i][j])):
                shortest = check[i][j]
                eatFish[0] = [j,i]
            elif (bfsCheck[i][j] == 9):
                bfsCheck[i][j] = 0
                matrix[i][j] = 0

            check[i][j] = 0
            if (matrix[i][j] >= 1 and matrix[i][j] <= 6):
                if (matrix[i][j] < sharkSize):
                    bfsCheck[i][j] = matrix[i][j]
                elif (matrix[i][j] > sharkSize):
                    check[i][j] = -1
    visit = [[False for i in range(n)] for i in range(n)]
    fish[matrix[eatFish[0][1]][eatFish[0][0]]] -= 1
    bfsCheck[eatFish[0][1]][eatFish[0][0]] = 9
    matrix[eatFish[0][1]][eatFish[0][0]] = 9
    q.append([eatFish[0][0],eatFish[0][1]])
    time += shortest

print(time)