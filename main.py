def solution(n, words):
    num = 2
    count = 1
    a = {}
    a[words[0]] = 1
    for i in range(1, len(words)):
        if (words[i] not in a):
            a[words[i]] = 1
        else:
            a[words[i]] = a[words[i]] + 1

        if (a[words[i]] > 1 or words[i - 1][len(words[i - 1]) - 1] != words[i][0]):
            return [num, count]

        if (num == n):
            num = 1
            count += 1
        else:
            num += 1

    return [0, 0]