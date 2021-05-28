import sys
input = sys.stdin.readline
queue = [0 for i in range(10000)]
start = 0
end = 0

def push(num):
    global end
    queue[end] = int(num)
    end += 1

def pop():
    global start
    if(queue[start] == 0):
        print(-1)
    else:
        print(queue[start])
        queue[start] = 0
        start += 1

def size():
    print(end - start)

def empty():
    if(start == end):
        print(1)
    else:
        print(0)

def front():
    if(start == end):
        print(-1)
    else:
        print(queue[start])

def back():
    if(start == end):
        print(-1)
    else:
        print(queue[end-1])

n = int(input())

for i in range(n):
    d = list(map(str,input().split()))
    if(d[0] == 'push'):
        push(d[1])
    elif(d[0] == 'pop'):
        pop()
    elif(d[0] == 'size'):
        size()
    elif(d[0] == 'empty'):
        empty()
    elif(d[0] == 'front'):
        front()
    elif(d[0] == 'back'):
        back()
    d = []