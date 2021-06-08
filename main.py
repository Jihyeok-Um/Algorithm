def solution(n):
    prime_store = [0 for i in range(1000000)]
    prime_num = 0
    array = [False for i in range(1000000)]

    for i in range(2,n+1):
        if array[i] == False:
            prime_store[prime_num] = i
            prime_num += 1
        j = i*i
        while(j <= n):
            array[j] = True
            j += i

    return prime_num