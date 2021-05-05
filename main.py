n = int(input())

matrix = []
for i in range(n):
    matrix.append([False for i in range(n)])

def queen(count, y,x):
    if (matrix[y][x] == True):
        if (x < n-1):
            queen(count,y,x+1)
            return
        elif (y < n-1):
            queen(count,y+1,0)
            return
        else:
            print(count)
            return

    for i in range (n):
        if (matrix[y][i] == True):
            return
        matrix[y][i] = True
    matrix[y][x] = False
    for i in range (n):
        if (matrix[i][x] == True):
            return
        matrix[i][x] = True

    a=b=c=d = False
    donePoint = 0
    i = 0
    while(donePoint != 4):
        i += 1
        if(x-i > 0 and y-i > 0 and a == False):
            if(matrix[y-i][x-i] == True):
                return
            matrix[y-i][x-i] = True
        else:
            if (a == False):
                donePoint += 1
                a = True

        if (x+i <= n-1 and y-i > 0 and b == False):
            if (matrix[y-i][x+i] == True):
                return
            matrix[y-i][x+i] = True
        else:
            if (b == False):
                donePoint += 1
                b = True

        if (x-i > 0 and y+i <= n-1 and c == False):
            if (matrix[y+i][x-i] == True):
                return
            matrix[y+i][x-i] = True
        else:
            if (c == False):
                donePoint += 1
                c = True

        if (x+i <= n-1 and y+i <= n-1 and d == False):
            if (matrix[y+i][x+i] == True):
                return
            matrix[y+i][x+i] = True
        else:
            if (d == False):
                donePoint += 1
                d = True

    if (x < n-1):
        queen(count+1, y, x + 1)
    elif (y < n-1):
        queen(count+1, y + 1, 0)
    else:
        print(count+1)
        return

queen(0,0,0)