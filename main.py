

S = input()
T = input()
isGet = False

def getT(T):
    global isGet
    if T == S:
        print(1)
        isGet = True
        return
    if len(T) <= len(S):
        return

    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
    getT(T)
getT(T)
if isGet == False:
    print(0)