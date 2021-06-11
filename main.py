def solution(x):
    count = 10
    a = x
    sum_ = 0
    while (int(x / count) != 0):
        count *= 10
    count /= 10

    while (count != 1):
        sum_ += int(x / count)
        x = int(x % count)
        count /= 10
    sum_ += x

    if (a % sum_ == 0):
        return True
    else:
        return False
