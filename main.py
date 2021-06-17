class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    ans = ""
    for i in range(len(S)):
        if (S[i] in prec):
            if (S[i] != '('):
                while (not opStack.isEmpty() and prec[opStack.peek()] >= prec[S[i]]):
                    ans += opStack.pop()
            opStack.push(S[i])
        elif (S[i] == ')'):
            while (prec[opStack.peek()] != 1):
                ans += opStack.pop()
            opStack.pop()
        else:
            ans += S[i]

    while (not opStack.isEmpty()):
        ans += opStack.pop()

    return ans