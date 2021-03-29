node,edge,vertex = map(int, input().split())
matrix = [ [] for i in range(node+1)]
for i in range(edge):
    a,b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
visitList = [0] * (node+1)

def dfs(vertex):
    visitList[vertex]=1
    print(vertex, end=' ')
    for i in range(1, node+1):
        if(visitList[i]==0):
            for j in range(0, len(matrix[vertex])):
                if (matrix[vertex][j] == i):
                    dfs(i)


def bfs(vertex):
    queue=[vertex]
    visitList[vertex]=1
    while queue:
        vertex=queue.pop(0)
        print(vertex, end=' ')
        for i in range(1, node+1):
            if(visitList[i]==0):
                for j in range(0, len(matrix[vertex])):
                    if (matrix[vertex][j] == i):
                        queue.append(i)
                        visitList[i]=1

dfs(vertex)
visitList = [0] * (node+1)
print()
bfs(vertex)