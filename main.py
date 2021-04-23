import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
line = int(input())
matrix = []
ans = 100000
for i in range(line):
    matrix.append(list(map(int, input().split())))


def getScore(index, teamA, teamB):
    global ans
    aScore = bScore = 0
    if(index == line):
        for y in range(0, line):
            for x in range(0, line):
                if (x==y):
                    continue
                if (x < len(teamA) and y < len(teamA)):
                    aScore += matrix[teamA[y]][teamA[x]]
                if (x < len(teamB) and y < len(teamB)):
                    bScore += matrix[teamB[y]][teamB[x]]
        ans = min(abs(aScore-bScore),ans)
        return

    getScore(index+1, teamA+[index], teamB)
    getScore(index+1, teamA, teamB+[index])

getScore(0, [], [])
print(ans)