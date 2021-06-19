from collections import deque

def solution(bridge_length, weight, truck_weights):
    q2 = deque()
    q1 = deque(0 for i in range(bridge_length))
    q = deque(truck_weights)
    time = zeroCount = numTruck = 0

    while (len(q2) < len(truck_weights)):
        if (len(q) > 0 and sum(q1) + q[0] <= weight and numTruck + 1 <= bridge_length):
            t = q.popleft()
            q1.append(t)
            numTruck += 1
            zeroCount = 0
        else:
            if (len(q1) < bridge_length):
                q1.append(0)

        t2 = q1.popleft()
        if (t2 != 0):
            q2.append(t2)
            numTruck -= 1
            if (len(q) > 0 and sum(q1) + q[0] <= weight and numTruck + 1 <= bridge_length):
                t = q.popleft()
                q1.append(t)
                numTruck += 1

        time += 1
    return time