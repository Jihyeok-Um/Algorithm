def postfixEval(tokenList):
    prec = {
        '*': 1,
        '/': 2,
        '+': 3,
        '-': 4,
    }
    pStack = ArrayStack()
    for i in range(len(tokenList)):
        if (tokenList[i] in prec):
            a = pStack.pop()
            b = pStack.pop()
            if (tokenList[i] == '*'):
                pStack.push(a * b)
            elif (tokenList[i] == '/'):
                pStack.push(b / a)
            elif (tokenList[i] == '+'):
                pStack.push(a + b)
            else:
                pStack.push(b - a)
        else:
            pStack.push(tokenList[i])

    return pStack.pop()