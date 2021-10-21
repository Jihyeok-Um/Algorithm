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

for i in range(n):
    for j in range(m):
        if (matrix[i][j] == "R"):
            q.append([j, i, -1])
            start = [j, i]
            red = [j,i]
        elif (matrix[i][j] == "O"):
            end = [j,i]
        elif (matrix[i][j] == "B"):
            blue = [j,i]
while(q):
    c = q.popleft()
    if([c[0],c[1]] == end):
        break
    for i in range(4):
        if (c[0]+dx[i] >= 0 and c[0]+dx[i] < m and c[1]+dy[i] >= 0 and c[1]+dy[i] < n and matrix[c[1]+dy[i]][c[0]+dx[i]] != '#' and ([c[0]+dx[i],c[1]+dy[i]] != start)):
            if ((check[c[1]+dy[i]][c[0]+dx[i]]) == 0 or (check[c[1]][c[0]] < check[c[1]+dy[i]][c[0]+dx[i]])):
                for j in range(len(direction)):
                    if (direction[j][0] == [c[0],c[1]]):
                        direction[j][0] = [c[0]+dx[i],c[1]+dy[i]]
                        if (direction[j][1][-1] != str(i)):
                            direction[j][1] += str(i)
                if (c[2] == i):
                    check[c[1]+dy[i]][c[0]+dx[i]] = check[c[1]][c[0]]
                else:
                    check[c[1]+dy[i]][c[0]+dx[i]] = check[c[1]][c[0]] + 1
                    X = False
                    for j in range(len(direction)):
                        if (direction[j][0] == [c[0]+dx[i],c[1]+dy[i]]):
                            X = True
                    if(X == False):
                     direction.append([[c[0]+dx[i],c[1]+dy[i]],str(i)])
                q.append([c[0]+dx[i],c[1]+dy[i],i])

for i in range(len(check)):
    print(check[i])
print()

result = ""
for i in range(len(direction)):
    if (direction[i][0] == end):
        result = direction[i][1]

redO = False
blueO = False
for i in result:
    if(i == "0"):
        while(True):
            if (matrix[red[1]-1][red[0]] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]-1][red[0]] = "R"
                red = [red[0],red[1]-1]
            elif (matrix[red[1]-1][red[0]] == "O"):
                redO = True
                matrix[red[1]][red[0]] = "."
                break
            else:
                break
        while (True):
            if (matrix[blue[1]-1][blue[0]] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1]-1][blue[0]] = "B"
                blue = [blue[0],blue[1]-1]
            elif (matrix[blue[1]-1][blue[0]] == "O"):
                blueO = True
                matrix[blue[1]][blue[0]] = "."
                break
            else:
                break
        while (True):
            if (matrix[red[1] - 1][red[0]] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1] - 1][red[0]] = "R"
                red = [red[0],red[1]-1]
            elif (matrix[red[1] - 1][red[0]] == "O"):
                redO = True
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
                blueO = True
                matrix[blue[1]][blue[0]] = "."
                break
            else:
                break
    elif(i == "1"):
        while (True):
            if (matrix[red[1]+1][red[0]] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]+1][red[0]] = "R"
                red = [red[0],red[1]+1]
            elif (matrix[red[1]+1][red[0]] == "O"):
                redO = True
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
                blueO = True
                matrix[blue[1]][blue[0]] = "."
                break
            else:
                break
        while (True):
            if (matrix[red[1]+1][red[0]] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]+1][red[0]] = "R"
                red = [red[0],red[1]+1]
            elif (matrix[red[1]+1][red[0]] == "O"):
                redO = True
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
                blueO = True
                matrix[blue[1]][blue[0]] = "."
                break
            else:
                break
    elif(i == "2"):
        while (True):
            if (matrix[red[1]][red[0]-1] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]][red[0]-1] = "R"
                red = [red[0]-1,red[1]]
            elif (matrix[red[1]][red[0]-1] == "O"):
                redO = True
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
                blueO = True
                matrix[blue[1]][blue[0]] = "."
                break
            else:
                break
        while (True):
            if (matrix[red[1]][red[0]-1] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]][red[0]-1] = "R"
                red = [red[0]-1,red[1]]
            elif (matrix[red[1]][red[0]-1] == "O"):
                redO = True
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
                matrix[blue[1]][blue[0]] = "."
                blueO = True
                break
            else:
                break
    elif(i == "3"):
        while (True):
            if (matrix[red[1]][red[0]+1] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]][red[0]+1] = "R"
                red = [red[0]+1,red[1]]
            elif (matrix[red[1]][red[0]+1] == "O"):
                redO = True
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
                matrix[blue[1]][blue[0]] = "."
                blueO = True
                break
            else:
                break
        while (True):
            if (matrix[red[1]][red[0]+1] == "."):
                matrix[red[1]][red[0]] = "."
                matrix[red[1]][red[0]+1] = "R"
                red = [red[0]+1,red[1]]
            elif (matrix[red[1]][red[0]+1] == "O"):
                matrix[red[1]][red[0]] = "."
                redO = True
                break
            else:
                break
        while (True):
            if (matrix[blue[1]][blue[0]+1] == "."):
                matrix[blue[1]][blue[0]] = "."
                matrix[blue[1]][blue[0]+1] = "B"
                blue = [blue[0]+1, blue[1]]
            elif (matrix[blue[1]][blue[0]+1] == "O"):
                matrix[blue[1]][blue[0]] = "."
                blueO = True
                break
            else:
                break
    for i in range(n):
        print(matrix[i])
    print()

if(redO == True and blueO == False and check[end[1]][end[0]] < 10):
    print(1)
else:
    print(0)

print(result)