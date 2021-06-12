# 시저 암호

def solution(s, n):
    result = [i for i in s]

    for i in range(len(s)):
        for j in range(26):
            if (ord(s[i]) == ord('a') + j):
                if (chr(ord('a') + j + n) > 'z'):
                    result[i] = chr(ord('a') + j + n - 26)
                else:
                    result[i] = chr(ord('a') + j + n)

            elif (ord(s[i]) == ord('A') + j):
                if (chr(ord('A') + j + n) > 'Z'):
                    result[i] = chr(ord('A') + j + n - 26)
                else:
                    result[i] = chr(ord('A') + j + n)

    ans = ""
    for i in range(len(result)):
        ans += result[i]

    return ans
