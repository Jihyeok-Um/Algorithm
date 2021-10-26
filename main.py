import sys
from collections import deque
import copy
stack = []
string = list(sys.stdin.readline().rstrip())
bracketNum = 0
bracketNum2 = 0
temp = 0
bracket = [[0,0] for i in range(10)]
for i in range(len(string)):
    if string[i] == '(':
        stack.append(['(',i])
    elif string[i] == ')':
        b1 = stack.pop()
        bracket[temp] = [b1[1],i]
        temp += 1

combi = []
for i in range(len(bracket)):
    if (bracket[i] == [0,0]):
        continue
    combi.append(bracket[i])
ans = []
depth = 0
combi.sort()

def delBracket(s,depth):
    global string
    result = ""
    if (depth == temp):
        for i in range(len(s)):
            if (s[i] != '!'):
                result += s[i]
        if (result not in ans):
            ans.append(result)
        return

    delBracket(copy.deepcopy(s), depth+1)
    s[combi[depth][0]] = "!"
    s[combi[depth][1]] = "!"
    delBracket(copy.deepcopy(s), depth+1)

delBracket(copy.deepcopy(string), 0)
ans.sort()
for i in range(1,len(ans)):
    print(ans[i])