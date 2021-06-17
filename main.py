def solution(skill, skill_trees):
    count = 0
    for i in range(len(skill_trees)):
        temp = []
        for j in range(len(skill)):
            ans = skill_trees[i].find(skill[j])
            if (ans == -1):
                temp.append(27)
            else:
                temp.append(ans)

        print(temp)
        con = False
        for j in range(len(temp) - 1):
            if (temp[j] > temp[j + 1]):
                con = True
                break
        if (con == True):
            continue
        count += 1
    return count