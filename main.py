def is_prime(num):
     if num < 2:
        return False
     elif num == 2 or num == 3:
        return True
     j = 2
     while(j*j <= num):
         if num % j == 0:
             j += 1
             return False
         j += 1
     return True


def main():
    count = 0
    num = int(input())
    a = list(map(int, input().split()))
    for i in range(0, len(a)):
        if(is_prime(a[i])):
            count += 1
    print(count)

main()