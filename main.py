def solution(board):
    for y in range(len(board) - 1):
        for x in range(len(board[y]) - 1):
            if (board[y + 1][x + 1] != 0):
                board[y + 1][x + 1] = min(board[y][x], board[y + 1][x], board[y][x + 1]) + 1

    ans = 0
    for y in range(len(board)):
        ans = max(ans, max(board[y]))

    return ans * ans