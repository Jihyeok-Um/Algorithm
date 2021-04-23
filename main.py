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
        if(line / 2 != len(teamA)):
            return
        if(line / 2 != len(teamB)):
            return

        for y in range(0, len(teamA)):
            for x in range(0, len(teamA)):
                if (x==y):
                    continue
                aScore += matrix[teamA[y]][teamA[x]]
                bScore += matrix[teamB[y]][teamB[x]]
        ans = min(abs(aScore-bScore),ans)
        return

    getScore(index+1, teamA+[index], teamB)
    getScore(index+1, teamA, teamB+[index])

getScore(0, [], [])
print(ans)