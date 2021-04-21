import sys
limit_number = 150000
sys.setrecursionlimit(limit_number)

n,m,z = map(int,input().split())
matrix = []
check = [[False for _ in range(m)] for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
max_ = -100000000
for i in range(n):
    matrix.append(list(map(int, input().split())))

def getScore(startX, startY, index, temp):
    global max_
    if (index == z):
        print(check)
        max_ = max(max_,temp)
        return

    for i in range(startX,n):
        for j in range(startY if i == startX else 0,m):
            if (check[i][j]):
                continue
            ok = True
            for k in range(0, 4):
                if (0 <= i + dx[k] < n and 0 <= j + dy[k] < m):
                    if (check[i + dx[k]][j + dy[k]]):
                        ok = False
            if ok:
                check[i][j] = True
                getScore(i,j, index+1,temp+matrix[i][j])
                check[i][j] = False

getScore(0,0,0,0)
print(max_)