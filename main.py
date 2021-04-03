node = int(input())
edge = int(input())
count = 0
matrix = [[0]*(node+1) for i in range(node+1)]
for i in range(edge):
    a,b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
visitList = [0 for i in range(node+1)]

def dfs(vertex):
    global count
    visitList[vertex] = 1
    for i in range(1, node+1):
        if (visitList[i] == 0 and matrix[vertex][i] == 1):
            count += 1
            dfs(i)

dfs(1)
print(count)