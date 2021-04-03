import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global a, b
    visitList[x][y] = 1
    if (x - 1 >= 0 and visitList[x - 1][y] == 0 and matrix[x - 1][y] == 1):
        dfs(x - 1, y)
    if (x + 1 < a and visitList[x + 1][y] == 0 and matrix[x + 1][y] == 1):
        dfs(x + 1, y)
    if (y - 1 >= 0 and visitList[x][y - 1] == 0 and matrix[x][y - 1] == 1):
        dfs(x, y - 1)
    if (y + 1 < b and visitList[x][y + 1] == 0 and matrix[x][y + 1] == 1):
        dfs(x, y + 1)

num = int(input())
for i in range(num):
    a,b,node = map(int,input().split())
    matrix = [[0]*(b) for i in range(a)]
    visitList = [ [0]*(b) for i in range(a)]
    count = 0

    for i in range(node):
        x,y = map(int,input().split())
        matrix[x][y] = 1

    for i in range(a):
        for j in range(b):
            if (matrix[i][j] == 1 and visitList[i][j] == 0):
                dfs(i,j)
                count += 1

    print(count)