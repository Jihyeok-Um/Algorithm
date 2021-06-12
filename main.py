# 이상한 문자 만들기

def solution(s):
    index = 0
    result = [0 for i in range(len(s))]
    for i in range(len(s)):
        if (s[i] == " "):
            index = 0
            result[i] = " "
            continue
        else:
            for j in range(26):
                if (index % 2 == 0):
                    if (ord(s[i]) == ord('a') + j or ord(s[i]) == ord('A') + j):
                        result[i] = chr(ord('A') + j)
                elif (index % 2 == 1):
                    if (ord(s[i]) == ord('A') + j or ord(s[i]) == ord('a') + j):
                        result[i] = chr(ord('a') + j)
        index += 1

    ans = ""
    for i in range(len(result)):
        ans += result[i]

    return ans