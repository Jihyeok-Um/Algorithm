def solution(msg):
    ans = []
    dic = [chr(ord('A') + i) for i in range(26)]
    i = 0
    while (i < len(msg)):
        j = i + 1
        while (j < len(msg) + 1):
            if (msg[i:j] in dic):
                if (msg[i:j + 1] not in dic):
                    ans.append(dic.index(msg[i:j]) + 1)
                elif (msg[i:j] == msg[i:j + 1]):
                    ans.append(dic.index(msg[i:j]) + 1)
                    return ans

            elif (msg[i:j] not in dic):
                dic.append(msg[i:j])
                i = j - 2
                break
            j += 1
        i += 1