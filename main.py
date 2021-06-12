# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    arr.sort()
    result = []
    for i in range(len(arr)):
        if (arr[i] % divisor == 0):
            result.append(arr[i])
    if (len(result) == 0):
        result.append(-1)

    return result
