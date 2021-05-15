testCase = int(input())
last = 101
d = [0 for i in range(last)]
d[1] = d[2] = d[3] = 1
d[4] = d[5] = 2

for i in range(6,last):
    d[i] = d[i-1] + d[i-5]

for i in range(testCase):
    temp = int(input())
    print(d[temp])
