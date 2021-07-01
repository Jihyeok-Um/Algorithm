def solution(n, t, m, p):
    arr = ["F", 0]
    stack = []
    i = count = 1
    while (len(arr) < p + m * t):
        i = count
        count += 1
        while (i != 0):
            stack.append((i % n))
            i = i // n

        for k in range(len(stack)):
            temp = stack.pop()
            if (temp == 10):
                temp = 'A'
            elif (temp == 11):
                temp = 'B'
            elif (temp == 12):
                temp = 'C'
            elif (temp == 13):
                temp = 'D'
            elif (temp == 14):
                temp = 'E'
            elif (temp == 15):
                temp = 'F'
            arr.append(temp)

    ans = ""
    for i in range(t):
        ans += str(arr[p + m * i])
    return ans

