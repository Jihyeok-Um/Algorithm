def solution(scores):
    self = [0 for i in range((len(scores)))]
    isExcept = [False for i in range(len(scores))]
    isBig = [0 for i in range(len(scores))]
    isSmall = [0 for i in range(len(scores))]
    sumScore = [0 for i in range(len(scores))]
    result = ""

    for i in range(len(scores)):
        for j in range(len(scores)):
            sumScore[i] += scores[j][i]
            if (i == j):
                self[i] = scores[j][i]

    for i in range(len(scores)):
        for j in range(len(scores)):
            if (self[i] > scores[j][i]):
                isBig[i] += 1
            if (self[i] < scores[j][i]):
                isSmall[i] += 1

    for i in range(len(isExcept)):
        if (isBig[i] == len(isExcept) - 1 or isSmall[i] == len(isExcept) - 1):
            isExcept[i] = True

    print(sumScore)

    for i in range(len(sumScore)):
        if (isExcept[i] == True):
            sumScore[i] -= self[i]
            sumScore[i] = int(sumScore[i] / (len(sumScore) - 1))
        else:
            sumScore[i] = int(sumScore[i] / len(sumScore))

    print(isExcept)
    print(sumScore)

    for i in range(len(sumScore)):
        if (sumScore[i] >= 90):
            result += "A"
        elif (sumScore[i] >= 80):
            result += "B"
        elif (sumScore[i] >= 70):
            result += "C"
        elif (sumScore[i] >= 50):
            result += "D"
        else:
            result += "F"

    return result