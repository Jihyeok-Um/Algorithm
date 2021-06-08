from collections import deque

def solution(n, edge):
    q = deque()
    matrix = [[] for i in range(n + 1)]
    check = [-1 for i in range(n + 1)]
    for i in range(len(edge)):
        matrix[edge[i][0]].append(edge[i][1])
        matrix[edge[i][1]].append(edge[i][0])

    q.append(1)
    check[1] = 0
    while (q):
        vertex = q.popleft()
        for j in range(0,len(matrix[vertex])):
            if (check[matrix[vertex][j]] == -1):
                check[matrix[vertex][j]] = check[vertex]+1
                q.append(matrix[vertex][j])

    temp = max(check)
    ans = 0
    for i in range(len(check)):
        if (check[i] == temp):
            ans += 1

    return ans
