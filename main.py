def solution(n):
    i = 0
    ans = count = 0
    re = 1
    while (i <= n):
        i += 1
        ans += i
        if (ans == n):
            count += 1
            i = re
            re += 1
        elif (ans > n):
            ans = 0
            i = re
            re += 1

    return count