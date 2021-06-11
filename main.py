def solution(s):
    lenCheck = False
    numCheck = False
    num = 0
    if (len(s) == 4 or len(s) == 6):
        lenCheck = True

    for i in range(len(s)):
        for j in range(10):
            if (ord(s[i]) == ord("0") + j):
                num += 1

    if (num == len(s)):
        numCheck = True
    if (numCheck == True and lenCheck == True):
        return True
    else:
        return False
