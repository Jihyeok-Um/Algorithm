n = int(input())
d = list(map(int, input().split()))
s = [0 for i in range(n)]

for i in range(0,n):
    if i == 0:
        s[i] = d[i]
    else:
        s[i] = max(d[i],s[i-1]+d[i])

print(max(s))