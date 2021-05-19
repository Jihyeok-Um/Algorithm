arr = list(map(int, input().split()))
ans = [0 for i in range(101)]
output = []

for i in range(len(arr)):
    ans[arr[i]] = arr.count(arr[i])

for i in range(len(ans)):
    if (ans[i] != 0 and ans[i] != 1):
        output.append(ans[i])

print(output)