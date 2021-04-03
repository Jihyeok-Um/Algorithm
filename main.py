node = int(input())
matrix = []
array = []
countList = []
count = 0
for i in range(node):
     array = input()
     matrix.append(array)
visitList = [ [0]*(node) for i in range(node)]

def dfs(x,y):
    global count
    count += 1
    visitList[x][y] = 1
    if (x-1 >= 0 and visitList[x-1][y] == 0 and matrix[x-1][y] == '1'):
        dfs(x-1,y)
    if (x+1 < node and visitList[x+1][y] == 0 and matrix[x+1][y] == '1'):
        dfs(x+1,y)
    if (y-1 >= 0 and visitList[x][y-1] == 0 and matrix[x][y-1] == '1'):
        dfs(x,y-1)
    if (y+1 < node and visitList[x][y+1] == 0 and matrix[x][y+1] == '1'):
        dfs(x,y+1)

for i in range(0,node):
    for j in range(0,node):
        if (matrix[i][j] != '0' and visitList[i][j] != 1):
            dfs(i,j)
        if (count != 0):
            countList.append(count)
        count = 0

print(len(countList))
countList.sort()
for i in countList:
    print(i)