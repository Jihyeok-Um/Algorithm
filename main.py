def solution(phone_number):
    s = ""
    for i in range(len(phone_number)):
        if (i >= len(phone_number) - 4):
            s += phone_number[i]
        else:
            s += "*"

    return s