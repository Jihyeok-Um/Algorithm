from collections import deque

n,m,v = map(int,input().split())
matrix = [[] for i in range(n+1)]
check = [False for i in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    matrix[x].append(y)
    matrix[y].append(x)

def dfs(v):
    check[v] = True
    print(v,end=' ')
    matrix[v].sort()
    for i in matrix[v]:
        if(check[i] == False):
            dfs(i)

def bfs(v):
    check = [False for i in range(n + 1)]
    q = deque()
    q.append(v)
    check[v] = True
    while(q):
        x = q.popleft()
        print(x,end=' ')
        for i in matrix[x]:
            if(check[i] == False):
                check[i] = True
                q.append(i)


dfs(v)
print()
bfs(v)