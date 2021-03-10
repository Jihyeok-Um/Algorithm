def main():
    testCase = int(input())
    ring = list(map(int, input().split()))

    for i in range(1, len(ring)):
        a = ring[0]
        b = ring[i]
        reminder = 0
        while(b != 0):
            reminder = a % b
            a = b
            b = reminder
        print("{}/{}".format(int(ring[0]/a),(int(ring[i]/a))))

main()