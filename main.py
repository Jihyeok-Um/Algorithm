def solution(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    matrix[0][0] = 1
    count = 1
    x = y = where = 0
    num = n

    while (n != 1):
        if (count == n):
            count = 0
            n -= 1
            where += 1

        if (where % 3 == 0):
            matrix[y + 1][x] = matrix[y][x] + 1
            y = y + 1
            count += 1

        elif (where % 3 == 1):
            matrix[y][x + 1] = matrix[y][x] + 1
            x = x + 1
            count += 1

        elif (where % 3 == 2):
            matrix[y - 1][x - 1] = matrix[y][x] + 1
            y = y - 1
            x = x - 1
            count += 1

    ans = []
    for y in range(num):
        for x in range(num):
            if (matrix[y][x] != 0):
                ans.append(matrix[y][x])

    return ans