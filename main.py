import sys
sys.setrecursionlimit(15000)
num = int(input())
array = list(map(str, input().split()))
numChar = ['0','1','2','3','4','5','6','7','8','9']
numCheck = [False for i in range(10)]
count = last = 0
min_ = max_ = 0

def go(numArray):
    global count
    global min_, max_
    if(len(numArray) == len(array)+1):
        for i in range(0, len(array)):
            if (array[i] == '>'):
                if (numArray[i] < numArray[i+1]):
                    return
            elif (array[i] == '<'):
                if (numArray[i] > numArray[i+1]):
                    return

        ans = ""
        for i in range(len(numArray)):
            ans += str(numArray[i])
        if (count == 0):
            min_ = ans
        count += 1
        if (last < count):
            max_ = ans
        return

    for i in range(0, 10):
        if (numCheck[i] == True):
            continue
        numCheck[i] = True
        go(numArray+[i])
        numCheck[i] = False

go([])
print(max_)
print(min_)