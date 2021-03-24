def ddungci(hArray, wArray, nArray):
    for i in range(0, len(hArray)):
        for j in range(0, len(hArray)):
            if (hArray[i] > hArray[j] and wArray[i] > wArray[j]):
                nArray[j] += 1

    for i in nArray:
        print(i, end=' ')

def main():
    num = int(input())
    nArray = []
    hArray = []
    wArray = []
    for i in range(num):
        nArray.append(1)
    for i in range(num):
        h,w = list(map(int, input().split()))
        hArray.append(h)
        wArray.append(w)

    ddungci(hArray, wArray, nArray)

main()