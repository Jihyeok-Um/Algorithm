def numOne(p):
    if (len(p) == 0):
        return True

def numTwo(p):
    u = ""
    v = ""
    inCount = outCount = 0
    for i in p:
        if (inCount != outCount or inCount == outCount == 0):
            if (i == '('):
                inCount += 1
                u += i
            else:
                outCount += 1
                u += i
        elif (inCount == outCount):
            v += i
    return u, v

def numThree(p):
    stack = []
    for i in p:
        if (i == '('):
            stack.append(i)
        elif (i == ')' and len(stack) > 0 and stack[-1] == '('):
            stack.pop()
        else:
            stack.append(i)

    if (len(stack) == 0):
        return True

def getNewU(u):
    newU = ""
    for i in range(len(u)):
        if (i == 0 or i == len(u) - 1):
            pass
        else:
            if (u[i] == '('):
                newU += ')'
            elif (u[i] == ')'):
                newU += '('

    return newU

def sol(p):
    if (numOne(p)):
        return ""
    u, v = map(str, numTwo(p))
    if (numThree(u)):
        return u + sol(v)
    else:
        return "(" + sol(v) + ")" + getNewU(u)


def solution(p):
    if (numOne(p)):
        return ""
    if (numThree(p)):
        return p
    else:
        return sol(p)




