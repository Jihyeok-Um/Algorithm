n = int(input())
d = list(map(int,input().split()))
sum = list(d)

for i in range(1, len(d)):
    for j in range(0, i):
        if(d[i] > d[j] and sum[j]+d[i] > sum[i]):
            sum[i] = sum[j]+d[i]

print(max(sum))