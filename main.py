import sys
sys.setrecursionlimit(200000)

def getLottoNum(count, array, lotto, i):
    if (i == count):
        if (len(lotto) == 6):
            for i in range(len(lotto)):
                print(lotto[i], end=' ')
            print("")
        return 0

    lotto.append(array[i])
    getLottoNum(count, array, lotto, i+1)
    lotto.remove(lotto[len(lotto)-1])
    getLottoNum(count, array, lotto, i + 1)


def main():
    while(True):
        i = 0
        lotto = []
        array = list(map(int, input().split()))
        if array[0] == 0:
            return 0
        count = array[0]
        array.remove(array[0])
        array.sort()

        getLottoNum(count, array, lotto, i)
        print("")

main()