from collections import deque
q = deque()
dx = [1,0,-1,0]
dy = [0,-1,0,1]
ans = 0

m,n = map(int,input().split())
matrix = []
days = [[-1 for i in range(m)] for i in range(n)]
for i in range(n):
    matrix.append(list(map(int,input().split())))

for y in range(n):
    for x in range(m):
        if(matrix[y][x] == 1):
            q.append([x,y])
            days[y][x] = 0
        elif(matrix[y][x] == -1):
            days[y][x] = -2

while(q):
    temp = q.popleft()
    for i in range(0,4):
        if(temp[0]+dx[i] >= 0 and temp[0]+dx[i] < m and temp[1]+dy[i] >=0 and temp[1]+dy[i] < n and days[temp[1]+dy[i]][temp[0]+dx[i]] == -1):
            if(matrix[temp[1]+dy[i]][temp[0]+dx[i]] != -1):
                ans = days[temp[1]+dy[i]][temp[0]+dx[i]] = days[temp[1]][temp[0]]+1
                q.append([temp[0]+dx[i],temp[1]+dy[i]])

check = 0

for y in range(n):
    for x in range(m):
        if(days[y][x] == -1):
            check = -1
            break
        else:
            ans = max(ans,days[y][x])

if (check == -1):
    print(check)
else:
    print(ans)