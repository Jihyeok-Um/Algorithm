import sys
input = sys.stdin.readline

fullStr = list(input().rstrip())
exStr = list(input().rstrip())
stack = []
for i in range(len(fullStr)):
    stack.append(fullStr[i])
    if len(stack) >= len(exStr) and stack[-1] == exStr[-1]:
        if stack[-len(exStr):] == exStr:
            for j in range(len(exStr)):
                stack.pop()


if stack:
    print("".join(stack))
else:
    print("FRULA")
