def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cmt = [0, 0, 0]
    for i in range(0, len(answers)):
        if (answers[i] == num1[i % 5]):
            cmt[0] += 1
        if (answers[i] == num2[i % 8]):
            cmt[1] += 1
        if (answers[i] == num3[i % 10]):
            cmt[2] += 1

    temp = max(cmt)
    ans = []
    for i in range(len(cmt)):
        if (cmt[i] == temp):
            ans.append(i + 1)

    return ans