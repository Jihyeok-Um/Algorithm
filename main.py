n,m,r = map(int,input().split())
matrix = [list(map(int,input().split())) for i in range(n)]
matrix2 = [[0 for i in range(m)] for i in range(n)]
a = []
a = map(int,input().split())

for i in a:
    if (i == 1):
        for y in range(n):
            for x in range(m):
                matrix2[n-y-1][x] = matrix[y][x]
    elif (i == 2):
        for y in range(n):
            for x in range(m):
                matrix2[y][m-x-1] = matrix[y][x]
    elif (i == 3):
        matrix2 = [[0 for i in range(n)] for i in range(m)]
        n,m = m,n
        for y in range(n):
            for x in range(m):
                matrix2[y][x] = matrix[m-x-1][y]
    elif (i == 4):
        matrix2 = [[0 for i in range(n)] for i in range(m)]
        n,m = m,n
        for y in range(n):
            for x in range(m):
                matrix2[y][x] = matrix[x][n-y-1]
    elif (i == 5):
        for y in range(n):
            for x in range(m):
                if (y < int(n/2) and x < int(m/2)): # 1사분면
                    matrix2[y][x+int(m/2)] = matrix[y][x]
                elif (y < int(n/2) and x >= int(m/2)): # 2사분면
                    matrix2[y+int(n/2)][x] = matrix[y][x]
                elif (y >= int(n/2) and x < int(m/2)): # 4사분면
                    matrix2[y-int(n/2)][x] = matrix[y][x]
                elif (y >= int(n/2) and x >= int(m/2)): # 3사분면
                    matrix2[y][x-int(m/2)] = matrix[y][x]
    elif (i == 6):
        for y in range(n):
            for x in range(m):
                if (y < int(n/2) and x < int(m/2)): # 1사분면
                    matrix2[y+int(n/2)][x] = matrix[y][x]
                elif (y < int(n/2) and x >= int(m/2)): # 2사분면
                    matrix2[y][x-int(m/2)] = matrix[y][x]
                elif (y >= int(n/2) and x < int(m/2)): # 4사분면
                    matrix2[y][x+int(m/2)] = matrix[y][x]
                elif (y >= n/2 and x >= m/2): # 3사분면
                    matrix2[y-int(n/2)][x] = matrix[y][x]

    matrix = []
    for y in range(len(matrix2)):
        matrix.append(list(matrix2[y]))

for y in range(len(matrix2)):
    for x in range(len(matrix2[0])):
        print(matrix2[y][x],end=' ')
    print()