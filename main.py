def solution(n):
    one = getOne(n)
    while(True):
        n += 1
        if(one == getOne(n)):
            return n

def getOne(n):
    arr = []
    while(n > 0):
        arr.append(n % 2)
        n = n // 2
    return arr.count(1)