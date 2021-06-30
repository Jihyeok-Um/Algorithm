alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def solution(str1, str2):
    no = deno = 0
    arr1 = []
    arr2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1) - 1):
        if (str1[i] in alpha and str1[i + 1] in alpha):
            arr1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if (str2[i] in alpha and str2[i + 1] in alpha):
            arr2.append(str2[i:i + 2])

    if (len(arr1) == 0 and len(arr2) == 0):
        return int(1 * 65536)
    else:

        val = []
        arr1.sort()
        arr2.sort()
        for i in range(len(arr1)):
            if (arr1[i] in arr2 and arr1[i] not in val):
                no += min(arr1.count(arr1[i]), arr2.count(arr1[i]))
                val.append(arr1[i])

        dic = {}
        for i in range(len(arr1)):
            if (arr1[i] not in dic):
                dic[arr1[i]] = arr1.count(arr1[i])

        for i in range(len(arr2)):
            if (arr2[i] not in dic):
                dic[arr2[i]] = arr2.count(arr2[i])
            else:
                dic[arr2[i]] = max(dic[arr2[i]], arr2.count(arr2[i]))

        ans = list(dic.values())
        for i in ans:
            deno += i

        return int((no / deno) * 65536)
