from collections import deque


def solution(cacheSize, cities):
    q = deque()
    time = 0
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if (cities[i] in q):
            time += 1
        else:
            time += 5

        if cities[i] in q:
            q.remove(cities[i])
        else:
            if (len(q) == cacheSize and cacheSize != 0):
                q.popleft()
        if (cacheSize != 0):
            q.append(cities[i])

    return time