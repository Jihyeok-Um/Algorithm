def solution(d, budget):
    d.sort()
    result = 0
    i = 0
    for i in range(len(d)):
        if (d[i] <= budget):
            result += 1
            budget -= d[i]
        else:
            break

    return result