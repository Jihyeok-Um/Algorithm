array = [False for i in range(123456*2+1)]

def get_prime(max):
    for i in range(2, max+1):
        j = i*i
        while(j <= max):
            array[j] = True
            j += i

def get_prime_count(value):
    count = 0
    for i in range(value+1, (value*2)+1):
        if array[i] == False:
            count += 1
    print(count)

def main():
    get_prime(123456*2)
    while(True):
        num = int(input())
        if num == 0:
            break
        get_prime_count(num)

main()