def solution(n, arr1, arr2):
    result = []
    for i in range(len(arr1)):
        a1 = []
        a2 = []
        while (arr1[i] != 0):
            a1.append(arr1[i] % 2)
            arr1[i] = arr1[i] // 2
        while (arr2[i] != 0):
            a2.append(arr2[i] % 2)
            arr2[i] = arr2[i] // 2

        while (len(a1) < len(arr1)):
            a1.append(0)
        while (len(a2) < len(arr2)):
            a2.append(0)

        a1.reverse()
        a2.reverse()
        temp = ""
        for j in range(len(a1)):
            if (a1[j] == 1 or a2[j] == 1):
                temp += '#'
            else:
                temp += ' '
        result.append(temp)

    return result