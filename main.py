from collections import deque


def solution(dirs):
    check = [[[] for i in range(11)] for i in range(11)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    char = [5, 5]
    count = 0
    d = deque()
    d.append(char)
    for i in range(len(dirs)):
        temp = d.popleft()
        if (dirs[i] == "U"):
            if (char[0] + dy[0] >= 0):
                char = [char[0] + dy[0], char[1]]
        elif (dirs[i] == "L"):
            if (char[1] + dx[3] >= 0):
                char = [char[0], char[1] + dx[3]]
        elif (dirs[i] == "D"):
            if (char[0] + dy[2] <= 10):
                char = [char[0] + dy[2], char[1]]
        else:
            if (char[1] + dx[1] <= 10):
                char = [char[0], char[1] + dx[1]]

        if (dirs[i] not in check[char[0]][char[1]] and temp != char):
            check[char[0]][char[1]].append(dirs[i])
            if (dirs[i] == "U"):
                check[temp[0]][temp[1]].append("D")
            elif (dirs[i] == "D"):
                check[temp[0]][temp[1]].append("U")
            elif (dirs[i] == "R"):
                check[temp[0]][temp[1]].append("L")
            elif (dirs[i] == "L"):
                check[temp[0]][temp[1]].append("R")
            count += 1
        d.append(char)

    print(check)
    return count