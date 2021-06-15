def solution(s):
    srr = ""
    arr = []
    for i in range(len(s)):
        if (s[i] != " "):
            srr += s[i]
        elif (s[i] == " "):
            arr.append(srr)
            srr = ""
    arr.append(srr)
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    ans = ""
    ans += str(min(arr))
    ans += " "
    ans += str(max(arr))
    return ans