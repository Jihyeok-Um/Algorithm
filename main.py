def getMollaSum(num):
    temp = num
    sum = 0
    j = 10
    result = 0
    for i in range(temp):
        num -= i
        temp2 = num
        while (num % 1 != num):
            sum += (num % 10)
            num = int(num / 10)
        if (temp == sum + temp2):
            result = temp2
        sum = 0
        num = temp

    print(result)

def main():
    num = int(input())
    getMollaSum(num)

main()