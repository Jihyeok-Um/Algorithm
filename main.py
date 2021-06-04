from collections import deque
s = int(input())
matrix = [[-1 for i in range(s*2)] for i in range(s*2)]
q = deque()
matrix[1][0] = 0
q.append([1,0])

while(max(matrix[s]) == -1):
    temp = q.popleft()
    if (temp[0] >= 1 and temp[0] <= s*2 and matrix[temp[0]][temp[0]] == -1):
        matrix[temp[0]][temp[0]] = matrix[temp[0]][temp[1]] + 1
        q.append([temp[0],temp[0]])
    if (temp[0] >= 1 and temp[0]+temp[1] <= s*2 and matrix[temp[0]+temp[1]][temp[1]] == -1):
        matrix[temp[0]+temp[1]][temp[1]] = matrix[temp[0]][temp[1]] + 1
        q.append([temp[0]+temp[1],temp[1]])
    if (temp[0]-1 >= 1 and temp[0]-1 <= s*2 and matrix[temp[0]-1][temp[1]] == -1):
        matrix[temp[0]-1][temp[1]] = matrix[temp[0]][temp[1]] + 1
        q.append([temp[0]-1,temp[1]])

print(max(matrix[s]))