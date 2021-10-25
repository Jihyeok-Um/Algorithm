import sys
from collections import deque
t = int(input())
d = deque()
ans = []
ans2 = deque()
numList = ['0','1','2','3','4','5','6','7','8','9']

for i in range(t):
    errer = False
    func = input()
    n = int(input())
    num = sys.stdin.readline().rstrip()
    ans = ["" for i in range(len(num))]
    j = 0
    k = -1
    r = 0
    while num[j] != ']':
        if num[j] in numList:
            ans[k] += str(num[j])
            j += 1
        else:
            k += 1
            j += 1
    ans2.clear()
    for k in range(len(ans)):
        if ans[k] != '':
            ans2.append(int(ans[k]))

    for k in func:
        if k == 'R':
            r += 1
        elif k == 'D':
            if (len(ans2) == 0):
                errer = True
                break
            else:
                if r % 2 == 0:
                    ans2.popleft()
                if r % 2 == 1:
                    ans2.pop()

    if(errer == True):
        print("error")
    else:
        if r % 2 == 1:
            ans2.reverse()
            ans3 = list(ans2)
            if(len(ans3) == 0):
                print("[]")
            else:
                print("[", end="")
            for i in range(len(ans3)):
                if(i == len(ans3)-1):
                    print(ans3[i],end="]")
                    print()
                else:
                    print(ans3[i], end=",")
        elif r % 2 == 0:
            ans3 = list(ans2)
            if (len(ans3) == 0):
                print("[]")
            else:
                print("[", end="")
            for i in range(len(ans3)):
                if (i == len(ans3) - 1):
                    print(ans3[i], end="]")
                    print()
                else:
                    print(ans3[i], end=",")

