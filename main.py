n = int(input())
matrix = []
check = [[0 for i in range(n)] for i in range(n)]
dy = [0,1,0,-1]
dx = [-1,0,1,0]
t = [int(n/2), int(n/2)]
for i in range(n):
    matrix.append(list(map(int, input().split())))
check[t[0]][t[1]] = 0
def tornado():
    count = 1
    while(t != [0,0]):
        for i in range(0,2):
            for j in range(count):
                if (t[0]+dx[i] >= 0 and t[0]+dx[i] < n and t[1]+dy[i] >= 0 and t[1]+dy[i] < n):
                    check[t[1]+dy[i]][t[0]+dx[i]] = check[t[1]][t[0]] + 1
                    t[0] = t[0]+dx[i]
                    t[1] = t[1]+dy[i]
                    sand(i)
                    if(t == [0,0]):
                        return
        count += 1
        for i in range(2,4):
            for j in range(count):
                if (t[0]+dx[i] >= 0 and t[0]+dx[i] < n and t[1]+dy[i] >= 0 and t[1]+dy[i] < n):
                    check[t[1] + dy[i]][t[0] + dx[i]] = check[t[1]][t[0]] + 1
                    t[0] = t[0]+dx[i]
                    t[1] = t[1]+dy[i]
                    sand(i)
                    if (t == [0, 0]):
                        return
        count += 1

ans = 0
def sand(d):
    global ans
    if(d == 1):
        if (t[1]+1 >= 0 and t[1]+1 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]+1][t[0]]+= matrix[t[1]][t[0]]-(int((matrix[t[1]][t[0]]/100)*5)+ int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*2) + int((matrix[t[1]][t[0]]/100)*2) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*1) +int((matrix[t[1]][t[0]]/100)*1))
        else:
            ans += matrix[t[1]][t[0]]-(int((matrix[t[1]][t[0]]/100)*5)+ int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*2) + int((matrix[t[1]][t[0]]/100)*2) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*1) +int((matrix[t[1]][t[0]]/100)*1))
        if (t[1]+2 >= 0 and t[1]+2 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]+2][t[0]]+= int((matrix[t[1]][t[0]]/100)*5)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*5)
        if (t[1] >= 0 and t[1] < n and t[0]-1 >= 0 and t[0]-1 < n):
            matrix[t[1]][t[0]-1]+= int((matrix[t[1]][t[0]]/100)*7)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*7)
        if (t[1] >= 0 and t[1] < n and t[0]+1 >= 0 and t[0]+1 < n):
            matrix[t[1]][t[0]+1]+= int((matrix[t[1]][t[0]]/100)*7)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*7)
        if (t[1] >= 0 and t[1] < n and t[0]+2 >= 0 and t[0]+2 < n):
            matrix[t[1]][t[0]+2]+= int((matrix[t[1]][t[0]]/100)*2)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*2)
        if (t[1] >= 0 and t[1] < n and t[0]-2 >= 0 and t[0]-2 < n):
            matrix[t[1]][t[0]-2]+= int((matrix[t[1]][t[0]]/100)*2)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*2)
        if (t[1]+1 >= 0 and t[1]+1 < n and t[0]+1 >= 0 and t[0]+1 < n):
            matrix[t[1]+1][t[0]+1]+= int((matrix[t[1]][t[0]]/100)*10)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*10)
        if (t[1]+1 >= 0 and t[1]+1 < n and t[0]-1 >= 0 and t[0]-1 < n):
            matrix[t[1]+1][t[0]-1]+= int((matrix[t[1]][t[0]]/100)*10)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*10)
        if (t[1]-1 >= 0 and t[1]-1 < n and t[0]+1 >= 0 and t[0]+1 < n):
            matrix[t[1]-1][t[0]+1]+= int((matrix[t[1]][t[0]]/100)*1)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*1)
        if (t[1]-1 >= 0 and t[1]-1 < n and t[0]-1 >= 0 and t[0]-1 < n):
            matrix[t[1]-1][t[0]-1]+= int((matrix[t[1]][t[0]]/100)*1)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*1)
        matrix[t[1]][t[0]] = 0
    elif(d == 0):
        if (t[1] >= 0 and t[1] < n and t[0]-1 >= 0 and t[0]-1 < n):
            matrix[t[1]][t[0]-1]+= matrix[t[1]][t[0]]-(int((matrix[t[1]][t[0]]/100)*5)+ int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*2) + int((matrix[t[1]][t[0]]/100)*2) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*1) +int((matrix[t[1]][t[0]]/100)*1))
        else:
            ans += matrix[t[1]][t[0]]-(int((matrix[t[1]][t[0]]/100)*5)+ int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*2) + int((matrix[t[1]][t[0]]/100)*2) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*1) +int((matrix[t[1]][t[0]]/100)*1))
        if (t[1] >= 0 and t[1] < n and t[0]-2 >= 0 and t[0]-2 < n):
            matrix[t[1]][t[0]-2]+= int((matrix[t[1]][t[0]]/100)*5)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*5)
        if (t[1]-1 >= 0 and t[1]-1 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]-1][t[0]]+= int((matrix[t[1]][t[0]]/100)*7)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*7)
        if (t[1]+1 >= 0 and t[1]+1 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]+1][t[0]]+= int((matrix[t[1]][t[0]]/100)*7)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*7)
        if (t[1]+2 >= 0 and t[1]+2 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]+2][t[0]]+= int((matrix[t[1]][t[0]]/100)*2)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*2)
        if (t[1]-2 >= 0 and t[1]-2 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]-2][t[0]]+= int((matrix[t[1]][t[0]]/100)*2)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*2)
        if (t[1]-1 >= 0 and t[1]-1 < n and t[0]-1 >= 0 and t[0]-1 < n):
            matrix[t[1]-1][t[0]-1]+= int((matrix[t[1]][t[0]]/100)*10)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*10)
        if (t[1]+1 >= 0 and t[1]+1 < n and t[0]-1 >= 0 and t[0]-1 < n):
            matrix[t[1]+1][t[0]-1]+= int((matrix[t[1]][t[0]]/100)*10)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*10)
        if (t[1]-1 >= 0 and t[1]-1 < n and t[0]+1 >= 0 and t[0]+1 < n):
            matrix[t[1]-1][t[0]+1]+= int((matrix[t[1]][t[0]]/100)*1)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*1)
        if (t[1]+1 >= 0 and t[1]+1 < n and t[0]+1 >= 0 and t[0]+1 < n):
            matrix[t[1]+1][t[0]+1]+= int((matrix[t[1]][t[0]]/100)*1)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*1)
        matrix[t[1]][t[0]] = 0

    elif(d == 2):
        if (t[1] >= 0 and t[1] < n and t[0]+1 >= 0 and t[0]+1 < n):
            matrix[t[1]][t[0]+1]+= matrix[t[1]][t[0]]-(int((matrix[t[1]][t[0]]/100)*5)+ int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*2) + int((matrix[t[1]][t[0]]/100)*2) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*1) +int((matrix[t[1]][t[0]]/100)*1))
        else:
            ans += matrix[t[1]][t[0]]-(int((matrix[t[1]][t[0]]/100)*5)+ int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*2) + int((matrix[t[1]][t[0]]/100)*2) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*1) +int((matrix[t[1]][t[0]]/100)*1))
        if (t[1] >= 0 and t[1] < n and t[0]+2 >= 0 and t[0]+2 < n):
            matrix[t[1]][t[0]+2]+= int((matrix[t[1]][t[0]]/100)*5)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*5)
        if (t[1]-1 >= 0 and t[1]-1 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]-1][t[0]]+= int((matrix[t[1]][t[0]]/100)*7)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*7)
        if (t[1]+1 >= 0 and t[1]+1 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]+1][t[0]]+= int((matrix[t[1]][t[0]]/100)*7)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*7)
        if (t[1]+2 >= 0 and t[1]+2 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]+2][t[0]]+= int((matrix[t[1]][t[0]]/100)*2)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*2)
        if (t[1]-2 >= 0 and t[1]-2 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1]-2][t[0]]+= int((matrix[t[1]][t[0]]/100)*2)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*2)
        if (t[1]-1 >= 0 and t[1]-1 < n and t[0]+1 >= 0 and t[0]+1 < n):
            matrix[t[1]-1][t[0]+1]+= int((matrix[t[1]][t[0]]/100)*10)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*10)
        if (t[1]+1 >= 0 and t[1]+1 < n and t[0]+1 >= 0 and t[0]+1 < n):
            matrix[t[1]+1][t[0]+1]+= int((matrix[t[1]][t[0]]/100)*10)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*10)
        if (t[1]-1 >= 0 and t[1]-1 < n and t[0]-1 >= 0 and t[0]-1 < n):
            matrix[t[1]-1][t[0]-1]+= int((matrix[t[1]][t[0]]/100)*1)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*1)
        if (t[1]+1 >= 0 and t[1]+1 < n and t[0]-1 >= 0 and t[0]-1 < n):
            matrix[t[1]+1][t[0]-1]+= int((matrix[t[1]][t[0]]/100)*1)
        else:
            ans += int((matrix[t[1]][t[0]]/100)*1)
        matrix[t[1]][t[0]] = 0
    elif(d == 3):
        if (t[1] - 1 >= 0 and t[1] - 1 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1] - 1][t[0]] += matrix[t[1]][t[0]]-(int((matrix[t[1]][t[0]]/100)*5)+ int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*2) + int((matrix[t[1]][t[0]]/100)*2) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*1) +int((matrix[t[1]][t[0]]/100)*1))
        else:
            ans += matrix[t[1]][t[0]]-(int((matrix[t[1]][t[0]]/100)*5)+ int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*7) + int((matrix[t[1]][t[0]]/100)*2) + int((matrix[t[1]][t[0]]/100)*2) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*10) +int((matrix[t[1]][t[0]]/100)*1) +int((matrix[t[1]][t[0]]/100)*1))
        if (t[1] - 2 >= 0 and t[1] - 2 < n and t[0] >= 0 and t[0] < n):
            matrix[t[1] - 2][t[0]] += int((matrix[t[1]][t[0]] / 100) * 5)
        else:
            ans += int((matrix[t[1]][t[0]] / 100) * 5)
        if (t[1] >= 0 and t[1] < n and t[0] - 1 >= 0 and t[0] - 1 < n):
            matrix[t[1]][t[0] - 1] += int((matrix[t[1]][t[0]] / 100) * 7)
        else:
            ans += int((matrix[t[1]][t[0]] / 100) * 7)
        if (t[1] >= 0 and t[1] < n and t[0] + 1 >= 0 and t[0] + 1 < n):
            matrix[t[1]][t[0] + 1] += int((matrix[t[1]][t[0]] / 100) * 7)
        else:
            ans += int((matrix[t[1]][t[0]] / 100) * 7)
        if (t[1] >= 0 and t[1] < n and t[0] + 2 >= 0 and t[0] + 2 < n):
            matrix[t[1]][t[0] + 2] += int((matrix[t[1]][t[0]] / 100) * 2)
        else:
            ans += int((matrix[t[1]][t[0]] / 100) * 2)
        if (t[1] >= 0 and t[1] < n and t[0] - 2 >= 0 and t[0] - 2 < n):
            matrix[t[1]][t[0] - 2] += int((matrix[t[1]][t[0]] / 100) * 2)
        else:
            ans += int((matrix[t[1]][t[0]] / 100) * 2)
        if (t[1] + 1 >= 0 and t[1] + 1 < n and t[0] + 1 >= 0 and t[0] + 1 < n):
            matrix[t[1] + 1][t[0] + 1] += int((matrix[t[1]][t[0]] / 100) * 1)
        else:
            ans += int((matrix[t[1]][t[0]] / 100) * 1)
        if (t[1] + 1 >= 0 and t[1] + 1 < n and t[0] - 1 >= 0 and t[0] - 1 < n):
            matrix[t[1] + 1][t[0] - 1] += int((matrix[t[1]][t[0]] / 100) * 1)
        else:
            ans += int((matrix[t[1]][t[0]] / 100) * 1)
        if (t[1] - 1 >= 0 and t[1] - 1 < n and t[0] + 1 >= 0 and t[0] + 1 < n):
            matrix[t[1] - 1][t[0] + 1] += int((matrix[t[1]][t[0]] / 100) * 10)
        else:
            ans += int((matrix[t[1]][t[0]] / 100) * 10)
        if (t[1] - 1 >= 0 and t[1] - 1 < n and t[0] - 1 >= 0 and t[0] - 1 < n):
            matrix[t[1] - 1][t[0] - 1] += int((matrix[t[1]][t[0]] / 100) * 10)
        else:
            ans += int((matrix[t[1]][t[0]] / 100) * 10)
        matrix[t[1]][t[0]] = 0

tornado()
print(ans)