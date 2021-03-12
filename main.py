def main():
    num = list(map(int, input().split()))
    nominator = num[0]
    denominator = num[1]


    for i in range(num[1]-1):
        if denominator == 0:
            break
        num[0] = num[0]-1
        num[1] = num[1]-1
        nominator *= (num[0])
        denominator *= (num[1])
        print("{} {}".format(nominator,denominator))

    if denominator == 0:
        print(1)
    else:
        print("{}".format(int(nominator/denominator)))

main()