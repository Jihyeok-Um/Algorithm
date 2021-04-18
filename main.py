testCase = int(input())
for i in range(testCase):
    M,N,x,y = map(int,input().split())
    x -= 1
    y -= 1
    temp = x
    while temp < N*M:
        if temp % N == y:
            print(temp+1)
            break
        temp += M
    else:
        print(-1)

