def solution(new_id):
    ans = ""
    id_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.']

    # 1단계
    new_id = new_id.lower()
    print(new_id)

    # 2단계
    for i in new_id:
        if (i in id_):
            ans += i
    new_id = ans
    ans = ""
    print(new_id)

    # 3단계
    count = 0
    for i in new_id:
        if (i == '.'):
            count += 1
        else:
            if (count >= 1):
                ans += '.'
                count = 0
            ans += i
    new_id = ans
    ans = ""

    print(new_id)

    # 4단계
    for i in range(len(new_id)):
        if (i == 0 and new_id[i] == '.'):
            pass
        else:
            ans += new_id[i]
    new_id = ans
    ans = ""
    print(new_id)

    # 5단계
    if (len(new_id) == 0):
        new_id = "a"
    else:
        pass
    print(new_id)

    # 6단계
    if (len(new_id) >= 16):
        for i in range(15):
            ans += new_id[i]
        new_id = ans
        ans = ""

    for i in range(len(new_id)):
        if (i == len(new_id) - 1 and new_id[i] == '.'):
            pass
        else:
            ans += new_id[i]
    new_id = ans
    print(new_id)

    # 7단계
    if (len(new_id) <= 2):
        ans = new_id[-1]
        while (len(new_id) != 3):
            new_id += ans
        print(new_id)
        return new_id

    print(new_id)
    return new_id