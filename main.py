n = int(input())
d = list(map(int,input().split()))
length = [1 for i in range(n)]

for i in range(1, len(d)):
    for j in range(0, i):
        if(d[i] > d[j] and length[i] <= length[j]+1):
            length[i] = length[j]+1

print(max(length))