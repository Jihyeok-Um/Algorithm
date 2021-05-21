n = int(input())
red = [0]
green = [0]
blue = [0]
d = [[0 for i in range(3)] for i in range(n+1)]
temp1 = temp2 = temp3 = 0
for i in range(n):
    temp1,temp2,temp3 = map(int, input().split())
    red.append(temp1)
    green.append(temp2)
    blue.append(temp3)

i = 1
while(i <= n):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + red[i]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + green[i]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + blue[i]
    i += 1

print(min(d[n][0],d[n][1],d[n][2]))