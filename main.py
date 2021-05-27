n = int(input())
d = list(map(int, input().split()))
s = [0 for i in range(n)]
s2 = [0 for i in range(n)]
ans = -1001
for i in range(0,n):
    if i == 0:
        s[i] = d[i]
    else:
        s[i] = max(d[i],s[i-1]+d[i])

for i in range(n-1, -1, -1):
    if i == n-1:
        s2[i] = d[i]
    else:
        s2[i] = max(d[i],s2[i+1]+d[i])

for i in range(1,n-1):
    if (s[i-1] + s2[i+1] > ans):
        ans = s[i-1] + s2[i+1]

print(max(ans,max(s2),max(s)))