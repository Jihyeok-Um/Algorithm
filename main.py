import sys
n,m = map(int,input().split())

c = [False]*(n+1)
a = [0]*m

def go(index, n, m):
    if index == m:
        for i in range(index):
            if(i>=1 and a[i] < a[i-1]):
                return
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(1, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, n, m)
        c[i] = False

go(0,n,m)

# 다음 순열로 넘어갈 때, 앞에 숫자 하나씩 못 쓰게 하기.