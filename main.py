from itertools import permutations


def getSik(expression):
    op = ['*', '-', '+', ')']
    expression += ")"
    s = ""
    sik = []
    for i in expression:
        if (i not in op):
            s += i
        elif (i in op and i != ')'):
            sik.append(int(s))
            s = ""
            sik.append(i)
        elif (i == ")"):
            sik.append(int(s))
    return sik


def solution(expression):
    sik = getSik(expression)
    print(sik)
    o = []
    for i in range(len(sik)):
        if (sik[i] not in o and (sik[i] == '+' or sik[i] == '*' or sik[i] == '-')):
            o.append(sik[i])
    op = list(map(''.join, permutations(o)))
    ans = 0

    for i in range(len(op)):
        sik2 = list(sik)
        for j in range(len(op[i])):
            k = 0
            stack = []
            while (k != len(sik2)):
                print(stack)
                stack.append(sik2[k])
                if (stack[-1] == op[i][j] and op[i][j] == '*'):
                    stack.pop()
                    stack[-1] = stack[-1] * sik2[k + 1]
                    k += 1
                elif (stack[-1] == op[i][j] and op[i][j] == '-'):
                    stack.pop()
                    stack[-1] = stack[-1] - sik2[k + 1]
                    k += 1
                elif (stack[-1] == op[i][j] and op[i][j] == '+'):
                    stack.pop()
                    stack[-1] = stack[-1] + sik2[k + 1]
                    k += 1
                k += 1

            print(stack)
            sik2 = list(stack)
        ans = max(ans, abs(stack[0]))

    return ans
