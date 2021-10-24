from collections import deque
q = deque()
n = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1]
matrix = []
sharkSize = 2
eaten = time = 0
for i in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if (matrix[i][j] == 9):
            q.append([j,i,0])
            matrix[i][j] = 0
            break

def bfs():
    temp = 1e9
    while(q):
        p = q.popleft()
        visit[p[1]][p[0]] = True
        if (temp < p[2]):
            break
        for i in range(4):
            ny = p[1]+dy[i]
            nx = p[0]+dx[i]
            if(nx>=0 and nx<n and ny>=0 and ny<n):
                if (matrix[ny][nx] < sharkSize and visit[ny][nx] == False):
                    if(matrix[ny][nx] != 0 and [ny,nx,p[2]+1] not in fish):
                        fish.append([ny,nx,p[2]+1])
                        temp = p[2]
                    if([nx,ny,p[2]+1] not in q):
                        q.append([nx,ny,p[2]+1])
                elif (matrix[ny][nx] == sharkSize and visit[ny][nx] == False and [nx,ny,p[2]+1] not in q):
                    q.append([nx, ny, p[2]+1])
    print(q)


while(True):
    fish = []
    visit = [[False for i in range(n)] for i in range(n)]
    bfs()
    q.clear()
    if len(fish) > 0:
        fish.sort()
        y,x,move = fish[0][0], fish[0][1], fish[0][2]
        time += move
        eaten += 1
        matrix[y][x] = 0
        if eaten == sharkSize:
            sharkSize += 1
            eaten = 0
        q.append([x,y,0])
    else:
        break

print(time)