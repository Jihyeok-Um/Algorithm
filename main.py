def solution(x, n):
    answer = []
    for i in range(n):
        if (i != 0):
            answer.append(x + (x * i))
        else:
            answer.append(x)

    return answer