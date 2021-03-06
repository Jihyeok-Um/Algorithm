def get_prime(min, max):
    prime_store = [0 for i in range(1000000)]
    prime_num = 0
    array = [False for i in range(1000000)]

    for i in range(2, max+1):
        if array[i] == False:
            prime_store[prime_num] = i
            prime_num += 1
        j = i*i
        while(j <= max):
            array[j] = True
            j += i

    for i in range(0, len(prime_store)):
        if prime_store[i] == 0:
            break
        elif prime_store[i] < min:
            continue
        else:
            print(prime_store[i])


def main():
    a = list(map(int, input().split()))
    num = a[1]
    get_prime(a[0], a[1])

main()