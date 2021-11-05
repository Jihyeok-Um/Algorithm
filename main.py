from collections import deque
import sys
import copy

q = deque()
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
last = n*m
matrix = []
matrix2 = [[0 for i in range(m)] for j in range(n)]
visit = [[False for i in range(m)] for j in range(n)]
for i in range(n):
    matrix.append(list(sys.stdin.readline().rstrip()))
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '*':
            visit[i][j] = True
            matrix2[i][j] = -1
        else:
            q.append([i, j, -1])


def dfs(matrix, t, depth):
    if depth >= last:
        return
    for i in range(4):
        if i == t[2]:
            continue
        ny = t[0] + dy[i]
        nx = t[1] + dx[i]
        if ny >= n or ny < 0 or nx >= m or nx < 0:
            continue
        while n > ny > 0 and m > nx > 0 and not visit[ny][nx]:
            matrix[ny][nx] = matrix[t[0]][t[1]] + 1
            visit[ny][nx] = True
            ny = ny + dy[i]
            nx = nx + dx[i]

        for i in range(n):
            print(matrix[i])
        print()
        nt = [ny, nx, i]
        dfs(copy.deepcopy(matrix), nt, depth+1)


while q:
    nt = q.popleft()
    dfs(copy.deepcopy(matrix2), nt, 1)
    print(matrix2)
