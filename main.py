node,edge,vertex = map(int, input().split())
matrix = [[0]*node for i in range(node)]
for i in range(edge):
    a,b = map(int, input().split())
    matrix[a-1][b-1] = matrix[b-1][a-1] = 1
visitList = [0] * (node)

def dfs(vertex):
    visitList[vertex]=1
    print(vertex+1, end=' ')
    for i in range(0, node):
        if(visitList[i]==0 and matrix[vertex][i]==1):
            dfs(i)


def bfs(vertex):
    queue=[vertex]
    visitList[vertex]=0
    while queue:
        vertex=queue.pop(0)
        print(vertex+1, end=' ')
        for i in range(0, node):
            if(visitList[i]==1 and matrix[vertex][i]==1):
                queue.append(i)
                visitList[i]=0

dfs(vertex - 1)
print()
bfs(vertex - 1)