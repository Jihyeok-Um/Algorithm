from collections import deque

def solution(maps):
    n = len(maps[0])
    m = len(maps)

    check = [[0 for i in range(n)] for i in range(m)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    q.append([0, 0])
    check[0][0] = 1
    while (q):
        c = q.popleft()
        for i in range(4):
            x = c[1] + dx[i]
            y = c[0] + dy[i]
            if (x >= 0 and x < n and y >= 0 and y < m and maps[y][x] == 1 and check[y][x] == 0):
                q.append([y, x])
                check[y][x] = check[c[0]][c[1]] + 1

    for i in range(len(maps)):
        print(check[i])

    if (check[m - 1][n - 1] != 0):
        return check[m - 1][n - 1]
    else:
        return -1