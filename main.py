n = int(input())
matrix = [[0 for i in range(101)] for i in range(101)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
ans = 0
for i in range(n):
    x, y, d, g = map(int, input().split())
    matrix[y][x] = 1
    temp = [d]
    q = [d]
    for j in range(g + 1):
        for k in q:
            x += dx[k]
            y += dy[k]
            matrix[y][x] = 1
        q = [(i + 1) % 4 for i in temp]
        q.reverse()
        temp = temp + q

for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i][j + 1] and matrix[i + 1][j] and matrix[i + 1][j + 1]:
            ans += 1
print(ans)
