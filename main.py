from collections import deque
n,k = map(int,input().split())
matrix = [-1 for i in range(200001)]
q = deque()
ok = 0

q.append(n)
matrix[n] = 0
while(q):
    x = q.popleft()
    if(x == k):
        ok += 1
    if (x-1 >= 0 and (matrix[x-1] == -1 or matrix[x-1]>=matrix[x]+1)):
        q.append(x-1)
        matrix[x-1] = matrix[x] + 1
    if (x+1 < 200000 and (matrix[x+1] == -1 or matrix[x+1]>=matrix[x]+1)):
        q.append(x+1)
        matrix[x+1] = matrix[x] + 1
    if (x*2 < 200000 and (matrix[x*2] == -1 or matrix[x*2]>=matrix[x]+1)):
        q.append(x*2)
        matrix[x*2] = matrix[x] + 1

print(matrix[k])
print(ok)