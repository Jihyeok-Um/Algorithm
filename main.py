def get_prime(max, count):
    prime_array = [0 for i in range(max)]
    array = [False for i in range(max+1)]
    prime_num = 0

    for i in range(2, max+1):
        if array[i] == False:
            prime_array[prime_num] = i
            prime_num += 1
        j = i*i
        while(j <= max):
            count += 1
            print(count)
            array[j] = True
            j += i

    prime_array = prime_array[0:prime_num]
    get_partition(prime_array, max, count)

def get_partition(prime_array, max, count):
    small_prime = 0
    big_prime = 0
    difference = max

    for i in range(0, len(prime_array)):
        for j in range(i, len(prime_array)):
            count += 1
            print(count)
            if (prime_array[i] + prime_array[j] == max and prime_array[j] - prime_array[i] < difference):
                small_prime = prime_array[i]
                big_prime = prime_array[j]
                difference = prime_array[j] - prime_array[i]
    print("{} {}".format(small_prime, big_prime))

def main():
    test_case = int(input())

    count = 0
    for i in range(0, test_case):
        num = int(input())
        get_prime(num,count)

main()