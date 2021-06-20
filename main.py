def solution(clothes):
    for i in range(len(clothes)):
        clothes[i][0], clothes[i][1] = clothes[i][1], clothes[i][0]
    clothes.sort()
    temp = []
    ans = {}
    for i in range(len(clothes)):
        if (clothes[i][0] not in temp):
            temp.append(clothes[i][0])
            ans[clothes[i][0]] = 1
        else:
            ans[clothes[i][0]] = ans[clothes[i][0]] + 1

    answer = 1
    for i in range(len(ans)):
        answer *= (ans.get(temp[i]) + 1)

    return answer - 1