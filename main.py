from collections import deque

def solution(progresses, speeds):
    q = deque()
    speed = deque()
    for i in range(len(progresses)):
        q.append(progresses[i])
        speed.append(speeds[i])

    ans = []
    while (q):
        for i in range(len(q)):
            q[i] += speed[i]

        count = 0
        while (q):
            if (q[0] >= 100):
                q.popleft()
                speed.popleft()
                count += 1
            else:
                break
        if (count != 0):
            ans.append(count)
    return ans