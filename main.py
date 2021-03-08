def main():
    while(True):
        num = list(map(int,input().split()))
        if(num[0] == 0 and num[1] == 0 and num[2] == 0):
            break
        biggest = max(num[0], num[1], num[2])

        if(num[0]*num[0] + num[1]*num[1] + num[2]*num[2] == biggest*biggest*2):
            print("right")
        else:
            print("wrong")

main()