from collections import deque
n,k = map(int,input().split())
matrix = [-1 for i in range(200000)]
q = deque()

q.append(n)
matrix[n] = 0
while(q):
    x = q.popleft()
    if(x == k):
        print(matrix[x])
        break
    if (x-1 >= 0 and matrix[x-1] == -1):
        q.append(x-1)
        matrix[x-1] = matrix[x] + 1
    if (x+1 < 200000 and matrix[x+1] == -1):
        q.append(x+1)
        matrix[x+1] = matrix[x] + 1
    if (x*2 < 200000 and matrix[x*2] == -1):
        q.append(x*2)
        matrix[x*2] = matrix[x] + 1