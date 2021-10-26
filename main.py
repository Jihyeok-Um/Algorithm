from collections import deque
stack = deque()
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1, ')': 1,
}
s = input()
ans = []
bracket = 0
for i in range(len(s)):
    if (s[i] in prec):
        while (len(stack) != 0 and prec[stack[-1]] >= prec[s[i]]):
            if (s[i] == '('):
                break
            elif(s[i] == ')'):
                if (stack[-1] != '('):
                    ans += stack.pop()
                else:
                    stack.pop()
                    break
            else:
                ans += stack.pop()
        if(s[i] != ')'):
            stack.append(s[i])
    else:
        ans += s[i]
while(len(stack) != 0):
    if(stack[-1] != '(' and stack[-1] != ')'):
        ans += stack.pop()
    else:
        stack.pop()

for i in ans:
    print(i,end="")
