# 다트 게임
def solution(dartResult):
    i = 0
    dart = []
    while (i <= len(dartResult) - 2):
        result = ""
        if (len(dartResult) - 1 >= i + 2):
            result += dartResult[i]
            result += dartResult[i + 1]
            if (dartResult[i + 2] == "*"):
                result += dartResult[i + 2]
                i += 1
            elif (dartResult[i + 2] == "#"):
                result += dartResult[i + 2]
                i += 1
            elif (dartResult[i + 2] == "S" or dartResult[i + 2] == "D" or dartResult[i + 2] == "T"):
                result += dartResult[i + 2]
                i += 1
            i += 2
        else:
            result += dartResult[i]
            result += dartResult[i + 1]
            i += 2

        dart.append(result)

    score = [0, 0, 0]
    for i in range(len(dart)):
        if (len(dart[i]) == 3 and i == 0):
            if (dart[i][1] == "S"):
                score[i] += int(dart[i][0])
            elif (dart[i][1] == "D"):
                score[i] += int(dart[i][0]) * int(dart[i][0])
            elif (dart[i][1] == "T"):
                score[i] += int(dart[i][0]) * int(dart[i][0]) * int(dart[i][0])
            else:
                score[i] += int(dart[i][0]) * 10 + int(dart[i][1])

            if (dart[i][2] == "*"):
                score[i] *= 2
            elif (dart[i][2] == "#"):
                score[i] *= -1
            elif (dart[i][2] == "S"):
                score[i] = score[i]
            elif (dart[i][2] == "D"):
                score[i] = score[i] * score[i]
            elif (dart[i][2] == "T"):
                score[i] = score[i] * score[i] * score[i]

        elif (len(dart[i]) == 3):
            if (dart[i][1] == "S"):
                score[i] += int(dart[i][0])
            elif (dart[i][1] == "D"):
                score[i] += int(dart[i][0]) * int(dart[i][0])
            elif (dart[i][1] == "T"):
                score[i] += int(dart[i][0]) * int(dart[i][0]) * int(dart[i][0])
            else:
                score[i] += int(dart[i][0]) * 10 + int(dart[i][1])

            if (dart[i][2] == "*"):
                score[i] *= 2
                score[i - 1] *= 2
            elif (dart[i][2] == "#"):
                score[i] *= -1
            elif (dart[i][2] == "S"):
                score[i] = score[i]
            elif (dart[i][2] == "D"):
                score[i] = score[i] * score[i]
            elif (dart[i][2] == "T"):
                score[i] = score[i] * score[i] * score[i]

        elif (len(dart[i]) == 2):
            if (dart[i][1] == "S"):
                score[i] += int(dart[i][0])
            elif (dart[i][1] == "D"):
                score[i] += int(dart[i][0]) * int(dart[i][0])
            else:
                score[i] += int(dart[i][0]) * int(dart[i][0]) * int(dart[i][0])

        elif (len(dart[i] == 4 and i == 0)):
            if (dart[i][2] == "S"):
                score[i] += dart[i][0] * 10 + dart[i][1]
            elif (dart[i][2] == "D"):
                score[i] += (dart[i][0] * 10 + dart[i][1]) * (dart[i][0] * 10 + dart[i][1])
            elif (dart[i][3] == "T"):
                score[i] += (dart[i][0] * 10 + dart[i][1]) * (dart[i][0] * 10 + dart[i][1]) * (
                            dart[i][0] * 10 + dart[i][1])

            if (dart[i][3] == "*"):
                score[i] *= 2
            elif (dart[i][3] == "#"):
                score[i] *= -1

        elif (len(dart[i] == 4)):
            if (dart[i][2] == "S"):
                score[i] += dart[i][0] * 10 + dart[i][1]
            elif (dart[i][2] == "D"):
                score[i] += (dart[i][0] * 10 + dart[i][1]) * (dart[i][0] * 10 + dart[i][1])
            elif (dart[i][3] == "T"):
                score[i] += (dart[i][0] * 10 + dart[i][1]) * (dart[i][0] * 10 + dart[i][1]) * (
                            dart[i][0] * 10 + dart[i][1])

            if (dart[i][3] == "*"):
                score[i] *= 2
                score[i - 1] *= 2
            elif (dart[i][3] == "#"):
                score[i] *= -1

        ans = 0
    for i in range(len(score)):
        ans += score[i]

    return ans