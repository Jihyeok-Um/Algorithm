from collections import deque
q = deque()
t = int(input())
dy = [2,1,-1,-2,-2,-1,1,2]
dx = [1,2,2,1,-1,-2,-2,-1]

for i in range(t):
    ans = 0
    l = int(input())
    startX, startY = map(int,input().split())
    finishX, finishY = map(int,input().split())
    if(startX == finishX and startY == finishY):
        print(ans)
        continue
    matrix = [[-1 for i in range(l)] for i in range(l)]

    q.append([startX,startY])
    matrix[startY][startX] = 0
    while(q):
        temp = q.popleft()
        for i in range(len(dx)):
            x = temp[0]+dx[i]
            y = temp[1]+dy[i]
            if (x >= 0 and x < l and y >= 0 and y < l and matrix[y][x] == -1):
                if (x == finishX and y == finishY):
                    ans = matrix[temp[1]][temp[0]]+1
                    q.clear()
                    break
                else:
                    q.append([x,y])
                    matrix[y][x] = matrix[temp[1]][temp[0]] + 1
    print(ans)