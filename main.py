def count(a,b,v):
    day = 0
    if v > a:
        v = v - a
        day += 1
    elif v == a:
        return 1

    while v != 0:
        if v >= (a-b)*1000000000:
            v = v - (a-b)*1000000000
            day += 1000000000
        elif v >= (a-b)*100000000:
            v = v - (a-b)*100000000
            day += 100000000
        elif v >= (a-b)*10000000:
            v = v - (a-b)*10000000
            day += 10000000
        elif v >= (a-b)*1000000:
            v = v - (a-b)*1000000
            day += 1000000
        elif v >= (a-b)*100000:
            v = v - (a-b)*100000
            day += 100000
        elif v >= (a-b)*10000:
            v = v - (a-b)*10000
            day += 10000
        elif v >= (a-b)*1000:
            v = v - (a-b)*1000
            day += 1000
        elif v >= (a-b)*100:
            v = v - (a-b)*100
            day += 100
        elif v >= (a-b)*10:
            v = v - (a-b)*10
            day += 10
        elif v >= (a-b):
            v = v - (a-b)
            day += 1
        elif v < (a-b):
            v = 0
            day += 1

    return day


def main():
    arr = list(map(int, input().split()))
    print(count(arr[0], arr[1], arr[2]))


main()