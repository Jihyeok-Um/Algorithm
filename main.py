def solution(s):
    isFirst = True
    s = s.lower()
    arr = []
    for i in range(len(s)):
        arr.append(s[i])
    for i in range(len(s)):
        if (isFirst == True):
            if (s[i] == " "):
                continue
            isFirst = False
            for j in range(26):
                if (ord(s[i]) == ord('a') + j):
                    arr[i] = chr(ord('A') + j)
        else:
            if (s[i] == " "):
                isFirst = True

    ans = ""
    for i in range(len(arr)):
        ans += arr[i]

    return ans