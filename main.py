def solution(s):
    s = s[1:-1]
    ans = []
    i = 0
    while (i < len(s)):
        if (s[i] == '{'):
            i += 1
            temp = ""
            small = []
            while (s[i] != '}'):
                if (s[i] != ','):
                    temp += s[i]
                else:
                    small.append(int(temp))
                    temp = ""
                i += 1
            small.append(int(temp))
            ans.append(small)
        i += 1

    answer = []
    ans.sort(key=len)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if (ans[i][j] not in answer):
                answer.append(ans[i][j])

    return answer

