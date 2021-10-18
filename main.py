h,w = map(int,input().split())
matrix = [[0 for i in range(w)] for i in range(h)]
block = list(map(int,input().split()))
count = 0

for i in range(len(block)):
    n = block[i]
    for j in range(n):
        matrix[(h-1)-j][i] = 1

for i in range(h):
    start = False
    st = fi = 0
    for j in range(w):
        if (matrix[i][j] == 1 and start == False):
            st = j
            start = True
        elif (matrix[i][j] == 1 and start == True):
            fi = j

    for j in range(st,fi):
        if (matrix[i][j] == 0):
            count += 1
            matrix[i][j] = 2

print(count)