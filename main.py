import sys
import copy
string = list(sys.stdin.readline().rstrip())
bracketNum = 0
bracketNum2 = 0
temp = 0
bracket = [[0,0] for i in range(10)]
for i in range(len(string)):
    if string[i] == '(':
        bracket[bracketNum2][0] = i
        bracketNum += 1
        bracketNum2 += 1
        temp += 1
    elif string[i] == ')':
        bracketNum2 -= 1
        if ()
        bracket[bracketNum][1] = i
combi = []
for i in range(len(bracket)):
    if (bracket[i] == [0,0]):
        continue
    combi.append(bracket[i])

ans = []
depth = 0
print(bracket)
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
    s[bracket[depth][0]] = "!"
    s[bracket[depth][1]] = "!"
    delBracket(copy.deepcopy(s), depth+1)

delBracket(copy.deepcopy(string), 0)
for i in range(1,len(ans)):
    print(ans[i])