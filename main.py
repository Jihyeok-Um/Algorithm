from collections import deque
d = deque()
ans = []
n,k = map(int, input().split())
for i in range(1,n+1):
    d.append(i)

while(d):
    d.rotate(-(k-1))
    ans.append(d.popleft())

print("<", end="")
for i in ans:
    if (i == ans[-1]):
        print(i, end="")
    else:
        print(i, end=", ")
print(">")