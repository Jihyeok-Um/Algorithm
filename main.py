import sys
from collections import deque
t = int(input())
cog = [0]
turn = []
for i in range(t):
    cog.append(deque(sys.stdin.readline().rstrip()))
k = int(input())
for i in range(k):
    turn.append(list(map(int, input().split())))

def lowCog(cogNum, turn):
    if (cog[cogNum-1][2] != cog[cogNum][6]):
        chain[cogNum-1] = turn*-1
        if (cogNum > 2):
            lowCog(cogNum-1, chain[cogNum-1])
    else:
        return
def highCog(cogNum, turn):
    if (cog[cogNum][2] != cog[cogNum+1][6]):
        chain[cogNum+1] = turn*-1
        if(cogNum < len(cog)-2):
            highCog(cogNum+1, chain[cogNum+1])
    else:
        return

for i in range(k):
    chain = [0 for i in range(len(cog))]
    chain[turn[i][0]] = turn[i][1]
    if (turn[i][0] != 1):
        lowCog(turn[i][0], turn[i][1])
    if (turn[i][0] != len(cog)-1):
        highCog(turn[i][0], turn[i][1])
    for j in range(1, len(cog)):
        cog[j].rotate(chain[j])

count = 0
for i in range(1,len(cog)):
    if (int(cog[i][0]) == 1):
        count += 1
print(count)