N,M,V=map(int,input().split())
matrix=[[0]*(N) for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    matrix[a-1][b-1]=matrix[b-1][a-1]=1
visit_list=[0]*(N)

def dfs(V):
    visit_list[V]=1
    print(V+1, end=' ')
    for i in range(0,N):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue=[V]
    visit_list[V]=0
    while queue:
        V=queue.pop(0)
        print(V+1, end=' ')
        for i in range(0, N):
            if(visit_list[i]==1 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i]=0

dfs(V-1)
print()
bfs(V-1)