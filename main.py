n = int(input())
d = list(map(int,input().split()))
length = [1 for i in range(n)]
trace = [-1 for i in range(n)]
ans = []
lastNum = 0

for i in range(1, len(d)):
    for j in range(0, i):
        if(d[i] > d[j] and length[i] <= length[j]+1):
            length[i] = length[j]+1
            trace[i] = j

for i in range(1, len(length)):
    if (max(length) == length[i]):
        lastNum = i

def go(p):
    if (trace[p] == -1):
        return
    ans.append(d[trace[p]])
    go(trace[p])


print(max(length))
ans.append(d[lastNum])
go(lastNum)
ans.reverse()
for i in ans:
    print(i, end=' ')
