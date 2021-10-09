def solution(weights, head2head):
    verse = [[0, 0, weights[i], i] for i in range(len(weights))]
    n = [0 for i in range(len(weights))]
    for i in range(len(weights)):
        for j in range(len(weights)):
            if (head2head[i][j] == "W"):
                verse[i][0] += 1
                if (weights[j] > weights[i]):
                    verse[i][1] += 1
            elif (head2head[i][j] == "N"):
                n[i] += 1
    for i in range(len(verse)):
        print(verse[i][0], len(verse) - n[i])
        if (len(verse) - n[i] != 0):
            verse[i][0] = float(verse[i][0]) / float(len(verse) - n[i])
        print(verse[i][0])

    result = sorted(verse, key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    print(result)
    ans = [1 for i in range(len(weights))]
    for i in range(len(verse)):
        ans[i] += result[i][3]
    return ans