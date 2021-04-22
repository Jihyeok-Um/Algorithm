import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
line = int(input())
matrix = []
check = [[False for j in range(line)]for i in range(line)]
teamA = teamB = 0
ans = 100000
for i in range(line):
    matrix.append(list(map(int, input().split())))

def getScore(index, addA, teamA, teamB):
    global ans
    if (addA > line/2):
        return

    if (index == line):
        if(addA == line/2):
            ans = min(abs(teamA - teamB),ans)
            print(ans)
            return

    for y in range(0,line):
        for x in range(0,line):
            if (x == y):
                continue
            if (check[y][x]):
                continue

            check[x][y] = check[y][x] = True
            getScore(index+1,addA+1, teamA+matrix[x][y]+matrix[y][x], teamB)
            getScore(index+1,addA, teamA,teamB+matrix[x][y]+matrix[y][x])
            check[x][y] = check[y][x] = False

getScore(0,0,0,0)
print(ans)