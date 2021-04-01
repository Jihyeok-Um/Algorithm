import sys
sys.setrecursionlimit(10000)
vertexList = []

def dfs(vertex, c):
    visitList[vertex] = 1
    color[vertex] = c
    vertexList.append(vertex)
    for i in range(1, node+1):
        if(visitList[i]==0):
            for j in range(0, len(matrix[vertex])):
                if (matrix[vertex][j] == i):
                    dfs(i, 3-c)

num = int(input())

for i in range(num):
    node, edge = map(int, input().split())
    matrix = [[] for i in range(node + 1)]
    check = True
    for i in range(edge):
        a, b = map(int, input().split())
        matrix[a].append(b)
        matrix[b].append(a)
    visitList = [0 for i in range(node+1)]
    color = [0 for i in range(node+1)]

    dfs(1, 1)
    if (check):
        print("YES")
    else:
        print("NO")