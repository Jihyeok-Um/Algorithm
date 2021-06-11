def solution(board, moves):
    store = []
    for i in range(len(moves)):
        for j in range(len(board)):
            if (board[j][moves[i] - 1] != 0):
                store.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break

    i = 1
    result = 0
    if (len(store) < 2):
        return result
    while (i < len(store)):
        if (store[i] == store[i - 1]):
            result += 2
            del store[i]
            del store[i - 1]
            i = 0
        i += 1

    return result