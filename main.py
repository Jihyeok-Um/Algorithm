from collections import deque
n,k = map(int,input().split())
matrix = [-1 for i in range(200000)]
trace = [-1 for i in range(200000)]
ans = []
q = deque()

q.append(n)
matrix[n] = 0
trace[n] = -2
while(q):
    x = q.popleft()
    if(x == k):
        print(matrix[x])
        break
    if (x-1 >= 0 and matrix[x-1] == -1):
        q.append(x-1)
        matrix[x-1] = matrix[x] + 1
        trace[x-1] = x
    if (x+1 < 200000 and matrix[x+1] == -1):
        q.append(x+1)
        matrix[x+1] = matrix[x] + 1
        trace[x+1] = x
    if (x*2 < 200000 and matrix[x*2] == -1):
        q.append(x*2)
        matrix[x*2] = matrix[x] + 1
        trace[x*2] = x

while(True):
    if(trace[x] == -2):
        ans.append(x)
        break
    else:
        ans.append(x)
        x = trace[x]

for i in range(len(ans)-1,-1,-1):
    print(ans[i],end=' ')
