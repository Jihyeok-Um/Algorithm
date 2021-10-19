from itertools import combinations
n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if (matrix[i][j] == 1):
            house.append([i+1,j+1])
        elif (matrix[i][j] == 2):
            chicken.append([i+1,j+1])
chicken = list(combinations(chicken,m))
distance = [[99999 for i in range(len(house))] for i in range(len(chicken))]

for i in range(len(chicken)):
    for j in range(len(chicken[i])):
        for k in range(len(house)):
            dis = abs(chicken[i][j][0]-house[k][0])+abs(chicken[i][j][1]-house[k][1])
            if (dis < distance[i][k]):
                distance[i][k] = dis

for i in range(len(distance)):
    distance[i] = sum(distance[i])
print(min(distance))
