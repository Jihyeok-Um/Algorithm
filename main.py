def solution(n):
    count = 10
    answer = 0
    while(int(n / count) != 0):
        count *= 10
    count /= 10

    while(count != 0):
        answer += int(n / count)
        n = int(n % count)
        count = int(count / 10)

    return answer