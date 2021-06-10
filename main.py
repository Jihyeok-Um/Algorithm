from collections import deque

def solution(n, computers):
    check = [False for i in range(n)]
    count = net = 1
    q = deque()
    q.append(0)
    check[0] = True

    while (count < n):
        if (q):
            a = 1
        else:
            for i in range(len(check)):
                if (check[i] == False):
                    check[i] = True
                    q.append(i)
                    net += 1
                    count += 1
                    break

        x = q.popleft()
        for i in range(len(computers[x])):
            if (computers[x][i] == 1 and check[i] == False):
                count += 1
                q.append(i)
                check[i] = True

    return net