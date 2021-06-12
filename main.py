def solution(lottos, win_nums):
    count = 0
    zero = 0
    for i in range(len(lottos)):
        if (lottos[i] == 0):
            zero += 1

    for i in range(len(lottos)):
        for j in range(len(lottos)):
            if (lottos[i] == win_nums[j]):
                count += 1

    good = count + zero
    bad = count
    result = []

    if (good == 6):
        result.append(1)
    elif (good == 5):
        result.append(2)
    elif (good == 4):
        result.append(3)
    elif (good == 3):
        result.append(4)
    elif (good == 2):
        result.append(5)
    else:
        result.append(6)

    if (bad == 6):
        result.append(1)
    elif (bad == 5):
        result.append(2)
    elif (bad == 4):
        result.append(3)
    elif (bad == 3):
        result.append(4)
    elif (bad == 2):
        result.append(5)
    else:
        result.append(6)

    return result
