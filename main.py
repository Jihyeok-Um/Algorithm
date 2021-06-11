def solution(s):
    answer = 0
    count = 1
    isNeg = False
    for i in range(len(s)):
        count *= 10
    count = count // 10
    if (s[0] == '+' or s[0] == '-'):
        count = count // 10
        if (s[0] == '-'):
            isNeg = True
        for i in range(1, len(s)):
            answer += count * int(s[i])
            count = count // 10
    else:
        for i in range(0, len(s)):
            answer += count * int(s[i])
            count = count // 10

    if (isNeg == True):
        answer = -answer

    return answer