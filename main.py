def solution(land):
    s = [[0 for i in range(4)] for i in range(len(land))]
    for i in range(len(land[0])):
        s[0][i] = land[0][i]

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            for k in range(len(land[0])):
                if (j != k):
                    if (s[i][j] < s[i - 1][k]):
                        s[i][j] = s[i - 1][k]
            s[i][j] += land[i][j]

    return max(s[len(land) - 1])