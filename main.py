from collections import deque
q = deque()
ans = 0

m,n,h = map(int,input().split())
matrix = []
small = []
dx = [1,0,-1,0,0,0]
dy = [0,-1,0,1,0,0]
dz = [0,0,0,0,1,-1]
days = [[[-1 for i in range(m)] for i in range(n)] for i in range(h)]
for j in range(h):
    for i in range(n):
        small.append(list(map(int,input().split())))
    matrix.append(small)
    small = []

for z in range(h):
    for y in range(n):
        for x in range(m):
            if(matrix[z][y][x] == 1):
                q.append([x,y,z])
                days[z][y][x] = 0
            elif(matrix[z][y][x] == -1):
                days[z][y][x] = -2

while(q):
    temp = q.popleft()
    for i in range(0,6):
        x = temp[0] + dx[i]
        y = temp[1] + dy[i]
        z = temp[2] + dz[i]
        if (x >= 0 and x < m and y >= 0 and y < n and z >= 0 and z < h and days[z][y][x] == -1):
            if(matrix[z][y][x] != -1):
                ans = days[z][y][x] = days[temp[2]][temp[1]][temp[0]]+1
                q.append([x,y,z])

check = 0

for z in range(h):
    for y in range(n):
        for x in range(m):
            if(days[z][y][x] == -1):
                check = -1
                break
            else:
                ans = max(ans,days[z][y][x])

if (check == -1):
    print(check)
else:
    print(ans)