def solution(N, stages):
    answer = {}
    for i in range(1, N + 1):
        clearCount = count = 0
        for j in range(len(stages)):
            if (i < stages[j]):
                clearCount += 1
                count += 1
            elif (i == stages[j]):
                count += 1
        if (count == 0):
            answer[i] = 0.0
        else:
            answer[i] = (count - clearCount) / count

    print(answer)
    answer = sorted(answer, key=lambda x: answer[x], reverse=True)
    print(answer)
    return answer