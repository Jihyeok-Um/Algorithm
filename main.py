def solution(s):
    minlen = 1000
    for i in range(len(s) // 2):
        j = 0
        count = 1
        arr = ""
        spl = []
        while (j < len(s)):
            spl.append(s[j:j + (i + 1)])
            j += i + 1

        for j in range(len(spl) - 1):
            if (spl[j] == spl[j + 1]):
                count += 1
            elif (spl[j] != spl[j + 1]):
                if (count != 1):
                    arr += str(count)
                arr += spl[j]
                count = 1

        if (count != 1):
            arr += str(count)
        arr += spl[j + 1]

        minlen = min(len(arr), minlen)

    if (len(s) == 1):
        return 1
    return minlen