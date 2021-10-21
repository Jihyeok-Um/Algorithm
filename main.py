import sys
import copy
sys.setrecursionlimit(10000)

from collections import deque
q = deque()
n,m = map(int, input().split())
check = [[0 for i in range(m)] for i in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
direction = []
matrix = []
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

def dfs(matrix, direction, depth, red, blue):
    global result
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


    for i in range(4):
        if (i != direction):
            dfs(copy.deepcopy(matrix), i, depth+1, copy.deepcopy(red), copy.deepcopy(blue))


for i in range(4):
    dfs(copy.deepcopy(matrix),i,1,copy.deepcopy(red),copy.deepcopy(blue))

if(result <= 10):
    print(1)
else:
    print(0)