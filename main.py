# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    for i in range(len(strings) - 1, 0, -1):
        for j in range(i):
            if (strings[j][n] > strings[j + 1][n]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]

            elif (strings[j][n] == strings[j + 1][n]):
                len_ = min(len(strings[j]), len(strings[j + 1]))
                isBig = False
                isChange = False
                for k in range(len_):
                    if (strings[j][k] > strings[j + 1][k]):
                        strings[j], strings[j + 1] = strings[j + 1], strings[j]
                        isChange = True
                        break
                    elif (strings[j][k] < strings[j + 1][k]):
                        isBig = True
                        break
                if (len(strings[j]) > len(strings[j + 1]) and isBig == False and isChange == False):
                    strings[j], strings[j + 1] = strings[j + 1], strings[j]

    return strings