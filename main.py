from collections import deque

dy = [0,-1,0,1]
dx = [1,0,-1,0]
n,m = map(int,input().split())
matrix = []
check = [[-1 for i in range(m)] for i in range(n)]
for i in range(n):
    temp = input()
    small = []
    for i in range(0,m):
        small.append(int(temp[i]))
    matrix.append(small)

def bfs(x,y):
    q = deque()
    v = [x,y]
    q.append(v)
    check[y][x] = 1
    while(q):
        temp = q.popleft()
        for i in range(0,4):
            if (temp[0]+dy[i] >= 0 and temp[0]+dy[i] < n and temp[1]+dx[i] >=0 and temp[1]+dx[i] < m):
                if (matrix[temp[0]+dy[i]][temp[1]+dx[i]] == 1 and check[temp[0]+dy[i]][temp[1]+dx[i]] == -1):
                    q.append([temp[0]+dy[i],temp[1]+dx[i]])
                    check[temp[0] + dy[i]][temp[1] + dx[i]] = check[temp[0]][temp[1]]+1

bfs(0,0)
print(check[n-1][m-1])