import sys
sys.setrecursionlimit(10000)

from collections import deque
q = deque()
n,m = map(int, input().split())
check = [[0 for i in range(m)] for i in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
direction = []
matrix = start = end = []
for i in range(n):
    matrix.append(list(input()))
result = 100
blue = red = []

for i in range(n):
    for j in range(m):
        if (matrix[i][j] == "B"):
            blue = [j,i]
        elif (matrix[i][j] == "R"):
            red = [j,i]

def dfs(matrix, direction, depth):
    global result
    global blue
    global red
    if (depth > 10 or depth > result):
        return
    if(direction == 0):
        while (True):
            if (matrix[blue[1]-1][blue[0]] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1]-1][blue[0]] = "B"
                blue = [blue[0],blue[1]-1]
            elif (matrix[blue[1]-1][blue[0]] == "O"):
                return
            else:
                break
        while (True):
            if (matrix[red[1] - 1][red[0]] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1] - 1][red[0]] = "R"
                red = [red[0], red[1] - 1]
            elif (matrix[red[1] - 1][red[0]] == "O"):
                matrix[red[1]][red[0]] = "."
                break
            else:
                break
        while (True):
            if (matrix[blue[1] - 1][blue[0]] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1] - 1][blue[0]] = "B"
                blue = [blue[0],blue[1]-1]
            elif (matrix[blue[1] - 1][blue[0]] == "O"):
                return
            else:
                break
        while (True):
            if (matrix[red[1] - 1][red[0]] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1] - 1][red[0]] = "R"
                red = [red[0],red[1]-1]
            elif (matrix[red[1] - 1][red[0]] == "O"):
                matrix[red[1]][red[0]] = "."
                if (depth < result):
                    result = depth
                return
            else:
                break
    elif(direction == 1):
        while (True):
            if (matrix[blue[1]+1][blue[0]] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1]+1][blue[0]] = "B"
                blue = [blue[0],blue[1]+1]
            elif (matrix[blue[1]+1][blue[0]] == "O"):
                return
            else:
                break
        while (True):
            if (matrix[red[1]+1][red[0]] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]+1][red[0]] = "R"
                red = [red[0],red[1]+1]
            elif (matrix[red[1]+1][red[0]] == "O"):
                matrix[red[1]][red[0]] = "."
                break
            else:
                break
        while (True):
            if (matrix[blue[1]+1][blue[0]] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1]+1][blue[0]] = "B"
                blue = [blue[0],blue[1]+1]
            elif (matrix[blue[1]+1][blue[0]] == "O"):
                return
            else:
                break
        while (True):
            if (matrix[red[1]+1][red[0]] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]+1][red[0]] = "R"
                red = [red[0],red[1]+1]
            elif (matrix[red[1]+1][red[0]] == "O"):
                if (depth < result):
                    result = depth
                return
            else:
                break
    elif(direction == 2):
        while (True):
            if (matrix[blue[1]][blue[0]-1] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1]][blue[0]-1] = "B"
                blue = [blue[0]-1,blue[1]]
            elif (matrix[blue[1]][blue[0]-1] == "O"):
                return
            else:
                break
        while (True):
            if (matrix[red[1]][red[0]-1] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]][red[0]-1] = "R"
                red = [red[0]-1,red[1]]
            elif (matrix[red[1]][red[0]-1] == "O"):
                matrix[red[1]][red[0]] = "."
                break
            else:
                break
        while (True):
            if (matrix[blue[1]][blue[0]-1] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1]][blue[0]-1] = "B"
                blue = [blue[0]-1,blue[1]]
            elif (matrix[blue[1]][blue[0]-1] == "O"):
                return
            else:
                break
        while (True):
            if (matrix[red[1]][red[0]-1] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]][red[0]-1] = "R"
                red = [red[0]-1,red[1]]
            elif (matrix[red[1]][red[0]-1] == "O"):
                if (depth < result):
                    result = depth
                return
            else:
                break
    elif(direction == 3):
        while (True):
            if (matrix[blue[1]][blue[0]+1] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1]][blue[0]+1] = "B"
                blue = [blue[0]+1, blue[1]]
            elif (matrix[blue[1]][blue[0]+1] == "O"):
                return
            else:
                break
        while (True):
            if (matrix[red[1]][red[0]+1] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]][red[0]+1] = "R"
                red = [red[0]+1,red[1]]
            elif (matrix[red[1]][red[0]+1] == "O"):
                matrix[red[1]][red[0]] = "."
                break
            else:
                break
        while (True):
            if (matrix[blue[1]][blue[0]+1] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1]][blue[0]+1] = "B"
                blue = [blue[0]+1,blue[1]]
            elif (matrix[blue[1]][blue[0]+1] == "O"):
                return
            else:
                break
        while (True):
            if (matrix[red[1]][red[0]+1] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]][red[0]+1] = "R"
                red = [red[0]+1,red[1]]
            elif (matrix[red[1]][red[0]+1] == "O"):
                if (depth < result):
                    result = depth
                return
            else:
                break

    for i in range(n):
        print(matrix[i])
    print(depth)
    print()

    for i in range(4):
        if (i != direction):
            dfs(list(matrix), i, depth+1)

matrix2 = list(matrix)
matrix3 = list(matrix)
matrix4 = list(matrix)
dfs(matrix,0,1)
dfs(matrix2,1,1)
dfs(matrix3,2,1)
dfs(matrix4,3,1)

print(result)