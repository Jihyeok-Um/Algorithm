def solution(arr):
    if (len(arr) == 1):
        num2 = [-1]
        return num2
    else:
        arr.remove(min(arr))

    if (len(arr) == 0):
        num2 = [-1]
        return num2
    return arr