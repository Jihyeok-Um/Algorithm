while(True):
    try:
        num = int(input())
    except EOFError:
        break
    temp = 1
    count = 1
    while(temp % num != 0):
       temp = (temp * 10) + 1
       count += 1
    print(count)