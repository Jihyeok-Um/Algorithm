def solution(n, results):
    matrix = [[] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(len(result)):
            matrix[result[i][0]].append(result[i][1])

    cmt = [0 for i in range(n + 1)]
    for i in range(n + 1):
        cmt[i] += len(matrix[i])
        for j in range(len(matrix[i]):
            cmt[matrix[i][j]] -= 1