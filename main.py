def solution(citations):
    h = 0
    for i in range(0, 1001):
        count = 0
        for j in range(len(citations)):
            if (citations[j] >= i):
                count += 1
        if (count >= i):
            h = i

    return h