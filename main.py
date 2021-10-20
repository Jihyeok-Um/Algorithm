from collections import deque

q = deque()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ans = 0
c = 0
n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if (matrix[i][j]) == 1:
            c += 1

ans = 0
while (c):
    q.append([0, 0])
    while (q):
        temp = q.popleft()
        for i in range(0, 4):
            if (temp[0] + dx[i] >= 0 and temp[0] + dx[i] < m and temp[1] + dy[i] >= 0 and temp[1] + dy[i] < n and matrix[temp[1] + dy[i]][temp[0] + dx[i]] == 0):
                if (matrix[temp[1] + dy[i]][temp[0] + dx[i]] != 1):
                    matrix[temp[1] + dy[i]][temp[0] + dx[i]] = 2
                    q.append([temp[0] + dx[i], temp[1] + dy[i]])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 1):
                count = 0
                for k in range(4):
                    if (i + dy[k] >= 0 and i + dy[k] < n and j + dx[k] >= 0 and j + dx[k] < m and matrix[i + dy[k]][j + dx[k]] == 2):
                        count += 1
                if (count >= 2):
                    matrix[i][j] = 3
                    c -= 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 2 or matrix[i][j] == 3):
                matrix[i][j] = 0

    ans += 1

print(ans)
