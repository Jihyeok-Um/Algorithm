import sys
s = 0
count = int(input())

def add(num):
    num = int(num[0]) - 1
    global s
    s = (s | (1 << num))

def remove(num):
    num = int(num[0]) - 1
    global s
    s = (s & ~(1 << num))

def check(num):
    num = int(num[0]) - 1
    global s
    if (s & (1<<num)):
        print(1)
    else:
        print(0)

def toggle(num):
    num = int(num[0]) - 1
    global s
    s = (s ^ (1<<num))

def all_():
    global s
    s = (1 << 20) - 1

def empty():
    global s
    s = 0

while(count != 0):
    count -= 1
    func, *num = sys.stdin.readline().split()
    if (func == "add"):
        add(num)
    if (func == "remove"):
        remove(num)
    if (func == "check"):
        check(num)
    if (func == "toggle"):
        toggle(num)
    if (func == "all"):
        all_()
    if (func == "empty"):
        empty()
