from collections import deque


def solution(priorities, location):
    q = deque()
    for i in priorities:
        q.append(i)

    count = 0
    location += 1
    while (q):
        temp = q.popleft()
        if (location > 0):
            location -= 1

        if (len(q) >= 1 and temp >= max(q)):
            count += 1
            if (location == 0):
                print(count)
                return
        elif (len(q) == 0):
            count += 1
            if (location == 0):
                print(count)
                return
        else:
            q.append(temp)
            if (location == 0):
                location = len(q)

t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    k = list(map(int, input().split()))
    solution(k,m)
