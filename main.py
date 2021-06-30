def isRight(s):
    stack = []
    for i in s:
        if (i == '[' or i == '{' or i == '('):
            stack.append(i)
        elif ((i == ']' or i == '}' or i == ')') and len(stack) > 0):
            if (stack[-1] == '[' and i == ']' or stack[-1] == '{' and i == '}' or stack[-1] == '(' and i == ')'):
                stack.pop()
        else:
            stack.append(i)

    if (len(stack) == 0):
        return True
    else:
        return False


def sRotate(s):
    f = ""
    newS = ""
    for i in range(len(s)):
        if (i == 0):
            f += s[i]
        else:
            newS += s[i]

    return newS + f


def solution(s):
    ans = 0
    for i in range(len(s)):
        if (isRight(s)):
            ans += 1
        s = sRotate(s)

    return ans
