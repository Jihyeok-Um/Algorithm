a = 0

def solution(num):
    collatz(num, 0)
    return a

def collatz(num, count):
    global a
    if (count == 500):
        a = -1
        return -1
    if (num == 1):
        a = count
        return

    if (num % 2 == 0):
        collatz(num // 2, count + 1)
    elif (num % 2 == 1):
        collatz(num * 3 + 1, count + 1)
