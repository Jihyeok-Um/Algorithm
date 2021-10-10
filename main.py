def solution(sizes):
    garo = [0 for i in range(len(sizes))]
    sero = [0 for i in range(len(sizes))]
    for i in range(len(sizes)):
        if (sizes[i][0] < sizes[i][1]):
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        garo[i] = sizes[i][0]
        sero[i] = sizes[i][1]

    result = max(garo) * max(sero)
    return result
