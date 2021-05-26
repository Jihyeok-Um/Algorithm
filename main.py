n = int(input())
d = list(map(int,input().split()))
length = [1 for i in range(n)]
ans = 0

for i in range(1, len(d)):
    for j in range(0, i):
        if(d[i] > d[j] and length[i] <= length[j]+1):
            length[i] = length[j]+1

copy = list(length)

for i in range(0, len(d)):
    for j in range(i, len(d)):
        if(d[i] > d[j] and copy[j] <= copy[i]+1):
            copy[j] = copy[i]+1

ans = max(copy)

print(max(max(length),ans))

