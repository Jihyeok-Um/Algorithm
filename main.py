n,m = map(int, input().split())
r,c,d = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
isclean = [[0 for j in range(m)] for i in range(n)]
result = 0

while(True):
    if (isclean[r][c] == 0):
        isclean[r][c] = 1
        result += 1
    isTurn = 0
    for i in range(4):
        if (d == 0):
            d = 3
            if (matrix[r][c-1] != 1 and isclean[r][c-1] == 0):
                c = c-1
                isTurn = 1
                break
        elif (d == 1):
            d = 0
            if (matrix[r-1][c] != 1 and isclean[r-1][c] == 0):
                r = r-1
                isTurn = 1
                break
        elif (d == 2):
            d = 1
            if (matrix[r][c+1] != 1 and isclean[r][c+1] == 0):
                c = c+1
                isTurn = 1
                break
        elif (d == 3):
            d = 2
            if (matrix[r+1][c] != 1 and isclean[r+1][c] == 0):
                r = r+1
                isTurn = 1
                break
    if (isTurn == 0):
        if (d == 0):
            if (matrix[r+1][c] != 1):
                r = r+1
            else:
                break
        elif (d == 1):
            if (matrix[r][c-1] != 1):
                c = c-1
            else:
                break
        elif (d == 2):
            if (matrix[r-1][c] != 1):
                r = r-1
            else:
                break
        elif (d == 3):
            if (matrix[r][c+1] != 1):
                c = c+1
            else:
                break

print(result)