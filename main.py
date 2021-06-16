def solution(L, x):
    start = 0
    last = len(L) - 1

    while (start <= last):
        mid = (start + last) // 2
        if (L[mid] > x):
            last = mid - 1
        elif (L[mid] < x):
            start = mid + 1
        elif (L[mid] == x):
            return mid
    return -1