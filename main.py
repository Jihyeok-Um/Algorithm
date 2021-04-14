max = 1

def swapCandy(array):
    global num
    for i in range(0, num):
        for j in range(0, num-1):
            array[i][j], array[i][j+1] = array[i][j+1], array[i][j]
            checkCandy(array)
            array[i][j], array[i][j+1] = array[i][j+1], array[i][j]

    for i in range(0, num):
        for j in range(0, num-1):
            array[j][i], array[j+1][i] = array[j+1][i], array[j][i]
            checkCandy(array)
            array[j][i], array[j+1][i] = array[j+1][i], array[j][i]

def checkCandy(array):
    global max
    current = 1
    for i in range(0, num):
        current = 1
        for j in range(0, num-1):
            if (array[i][j] == array[i][j+1]):
                current += 1
                if (current > max):
                    max = current
            else:
                current = 1

    for i in range(0, num):
        current = 1
        for j in range(0, num-1):
            if (array[j][i] == array[j+1][i]):
                current += 1
                if (current > max):
                    max = current
            else:
                current = 1


num = int(input())
outerArray = []
for i in range(num):
    outerArray.append(list(input()))

swapCandy(outerArray)
print(max)