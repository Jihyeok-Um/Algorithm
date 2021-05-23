n = int(input())
arr = [0]
d = [[0 for i in range(3)] for i in range(n+1)]
for i in range(n):
    arr.append(int(input()))

d[1][1] = arr[1]
if (n >= 2):
    d[2][2] = arr[1]+arr[2]

if (n >= 3):
    for i in range(3,n+1):
        d[i][0] = max(d[i-1]) #0번
        d[i][1] = max(d[i-2])+arr[i] #1번
        d[i][2] = max(d[i-3])+arr[i-1]+arr[i] #2번

print(max(d[n]))