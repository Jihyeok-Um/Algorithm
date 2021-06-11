def solution(arr):
    i = 0
    arr2 = []
    for i in range(1, len(arr)):
        if (arr[i] == arr[i - 1] and arr[i] != -1):
            arr[i - 1] = -1

    for i in range(len(arr)):
        if (arr[i] != -1):
            arr2.append(arr[i])

    return arr2