t = int(input())
for i in range(t):
    isNo = False
    n = int(input())
    num = []
    for j in range(n):
        num.append((input()))
    num.sort()
    for j in range(len(num) - 1):
        if (num[j] == num[j + 1][0:len(num[j])]):
            print("NO")
            isNo = True
            break
    if (isNo == False):
        print("YES")