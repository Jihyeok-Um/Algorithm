import sys
n,m = map(int,input().split())

c = [0]*(n+1)
a = [0]*m

def go(index, n, m):
    if index == m:
        for i in range(1, index):
            if (a[i] < a[i-1]):
                return
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(1, n+1):
        if c[i] == m:
            continue
        c[i] += 1
        a[index] = i
        go(index+1, n, m)
        c[i] = 0

go(0,n,m)
