variable = list(map(str, input().split()))
result = [variable[0] for i in range(len(variable)-1)]
type = ['[',']','&','*',',',';']
rever = []
varName = []
varDone = 0

for i in range(1, len(variable)):
    for j in range(len(variable[i])):
        if (variable[i][j] not in type):
            varDone = j
    varName.append(variable[i][0:varDone+1])
    rever.append(variable[i][varDone+1:-1])

for i in range(len(rever)):
    for j in range(len(rever[i])-1, -1 ,-1):
        if(rever[i][j] == ']'):
            result[i] += '[]'
        elif(rever[i][j] == '['):
            continue
        else:
            result[i] += rever[i][j]
    result[i] += " "
    result[i] += varName[i]
    result[i] += ";"

for i in range(len(result)):
    print(result[i])