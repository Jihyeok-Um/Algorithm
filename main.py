from collections import deque
n,m = map(int,input().split())
matrix = [list(map(int,list(input()))) for i in range(m)]
check = [[-1 for i in range(n)] for i in range(m)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
q = deque()
q2 = deque()
q.append([0,0])
check[0][0] = 0
while(q or q2):
    if (q):
        a = 1 #의미없음
    elif (q2):
        q = deque(q2)
        q2.clear()
    t = q.popleft()
    for i in range(4):
        x = t[0] + dx[i]
        y = t[1] + dy[i]
        if (x>=0 and x<n and y>=0 and y<m and matrix[y][x] == 1 and check[y][x] == -1):
            check[y][x] = check[t[1]][t[0]] + 1
            q2.append([x,y])
        if (x>=0 and x<n and y>=0 and y<m and matrix[y][x] == 0 and check[y][x] == -1):
            check[y][x] = check[t[1]][t[0]]
            q.append([x,y])

for i in range(m):
    print(check[i])

print(check[m-1][n-1])