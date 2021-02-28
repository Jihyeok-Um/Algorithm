def get_line_and_count(num):
    count = 0
    line = 0
    num2 = num
    for i in range(1, num2+1):
        if num > i:
            num -= i
            line += 1
        elif num == i:
            num = i-1
            break
        elif num < i:
            num -= 1
            break
    set_fractions(get_is_odd(line), line, num)


def get_is_odd(line):
    if line % 2 != 0:
        return True
    else:
        return False


def set_fractions(is_odd, line, count):
    line = line + 2
    count = count + 1

    big_num = line - count
    small_num = count

    if is_odd:
        print("{}/{}".format(small_num, big_num))
    else:
        print("{}/{}".format(big_num, small_num))


def main():
    num = int(input())
    get_line_and_count(num)


main()
