import sys
sys.setrecursionlimit(100000)

node, edge = map(int, input().split())
count = 1
matrix = [[0]*(node+1) for i in range(node+1)]
for i in range(edge):
    a,b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
visitList = [0 for i in range(node+1)]

def bfs(vertex):
    visitList[vertex] = 1
    for i in range(1, node+1):
        if (visitList[i] == 0 and matrix[vertex][i] == 1):
            bfs(i)

bfs(1)
for i in range(1, len(visitList)):
    if (visitList[i] == 0):
        count += 1
        bfs(i)
        i = 1
print(count)