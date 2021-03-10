def main():
    years = list(map(int,input().split()))
    count = 0
    countE = countS = countM = 0

    while(True):
        count += 1
        countE += 1
        countS += 1
        countM += 1
        if countE == 16:
            countE = 1
        if countS == 29:
            countS = 1
        if countM == 20:
            countM = 1
        if (years[0] == countE and years[1] == countS and years[2] == countM):
            print(count)
            break


main()