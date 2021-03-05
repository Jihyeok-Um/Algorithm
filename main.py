
def main():
    while(True):
        a = list(map(int, input().split()))
        if a[0] == 0 & a[1] == 0:
            break
        if (a[0] % a[1]) == 0:
            print("multiple")
        elif get_gcd(a[0], a[1]) != 1:
            print("factor")
        else:
            print("neither")


def get_gcd(num1, num2):
    while(num2 != 0):
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1

main()