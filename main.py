def solution(s):
    ans = ""
    if (len(s) % 2 == 0):
        ans += s[int(len(s) / 2) - 1]
        ans += s[int(len(s) / 2)]
    else:
        ans += s[int(len(s) / 2)]

    return ans