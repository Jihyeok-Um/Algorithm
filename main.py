import copy


def solution(y, x, board):
    check = [[False for i in range(x)] for i in range(y)]
    arr = [list(map(str, board[i])) for i in range(y)]
    ans = 0

    while (True):
        count = 0
        for i in range(y - 1):
            for j in range(x - 1):
                if (arr[i][j] == arr[i][j + 1] == arr[i + 1][j] == arr[i + 1][j + 1] != 'X'):
                    check[i][j] = check[i][j + 1] = check[i + 1][j] = check[i + 1][j + 1] = True
                    count += 1

        if (count == 0):
            return ans

        for i in range(y):
            for j in range(x):
                if (check[i][j] == True):
                    arr[i][j] = "X"
                    check[i][j] = False
                    ans += 1

        for i in range(y - 1, -1, -1):
            for j in range(x):
                if (arr[i][j] == 'X'):
                    k = i
                    while (arr[k][j] == 'X'):
                        if (k == 0):
                            break
                        k -= 1
                    arr[i][j] = arr[k][j]
                    arr[k][j] = 'X'