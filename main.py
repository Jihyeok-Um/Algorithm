matrix = []
max_ = 0
sero,garo = map(int,input().split())
for i in range(sero):
    matrix.append(list(map(int,input().split())))

def getScore(sero, garo, matrix):
    temp = 0
    global max_
    for i in range(0, sero):
        for j in range(0, garo):
            if (sero-1 >= i and garo-1 >= j+3):#1
                temp = matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i][j+3]
                max_ = max(temp, max_)
            if (sero-1 >= i+3 and garo-1 >= j):#2
                temp = matrix[i][j]+matrix[i+1][j]+matrix[i+2][j]+matrix[i+3][j]
                max_ = max(temp, max_)
            if (sero-1 >= i+1 and garo-1 >= j+1):#3
                temp = matrix[i][j]+matrix[i+1][j]+matrix[i][j+1]+matrix[i+1][j+1]
                max_ = max(temp, max_)
            if (sero-1 >= i+1 and garo-1 >= j+2):#4
                temp = matrix[i][j]+matrix[i+1][j]+matrix[i][j+1]+matrix[i][j+2]
                max_ = max(temp, max_)
            if (sero-1 >= i+1 and garo-1 >= j+2):#5
                temp = matrix[i][j]+matrix[i+1][j]+matrix[i+1][j+1]+matrix[i+1][j+2]
                max_ = max(temp, max_)
            if (sero-1 >= i+1 and garo-1 >= j+2):#6
                temp = matrix[i+1][j]+matrix[i+1][j+1]+matrix[i+1][j+2]+matrix[i][j+2]
                max_ = max(temp, max_)
            if (sero-1 >= i+1 and garo-1 >= j+2):#7
                temp = matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i+1][j+2]
                max_ = max(temp, max_)
            if (sero-1 >= i+2 and garo-1 >= j+1):#15
                temp = matrix[i][j]+matrix[i+1][j]+matrix[i+1][j+1]+matrix[i+2][j+1]
                max_ = max(temp, max_)
            if (sero-1 >= i+2 and garo-1 >= j+1):#16
                temp = matrix[i+1][j]+matrix[i+1][j+1]+matrix[i+2][j]+matrix[i][j+1]
                max_ = max(temp, max_)
            if (sero-1 >= i+1 and garo-1 >= j+2):#17
                temp = matrix[i+1][j]+matrix[i+1][j+1]+matrix[i][j+1]+matrix[i][j+2]
                max_ = max(temp, max_)
            if (sero-1 >= i+1 and garo-1 >= j+2):#8
                temp = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j+2]
                max_ = max(temp, max_)
            if (sero-1 >= i+2 and garo-1 >= j+1):#9
                temp = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1]
                max_ = max(temp, max_)
            if (sero-1 >= i+2 and garo-1 >= j+1):#18
                temp = matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+1][j+1] + matrix[i][j+1]
                max_ = max(temp, max_)
            if (sero-1 >= i+2 and garo-1 >= j+1):#10
                temp = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i][j+1]
                max_ = max(temp, max_)
            if (sero-1 >= i+2 and garo-1 >= j+1):#19
                temp = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1]
                max_ = max(temp, max_)
            if (sero-1 >= i+1 and garo-1 >= j+2):#11
                temp = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i][j+2]
                max_ = max(temp, max_)
            if (sero-1 >= i+1 and garo-1 >= j+2):#12
                temp = matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i][j+1]
                max_ = max(temp, max_)
            if (sero-1 >= i+2 and garo-1 >= j+1):#13
                temp = matrix[i+1][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1]
                max_ = max(temp, max_)
            if (sero-1 >= i+2 and garo-1 >= j+1):#14
                temp = matrix[i][j] + matrix[i+1][j+1] + matrix[i+1][j] + matrix[i+2][j]
                max_ = max(temp, max_)

getScore(sero, garo, matrix)
print(max_)