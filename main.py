def get_count(distance):
    i = 1
    count = 0
    while(distance > 0):
        distance = distance - i
        count += 1
        if distance <= 0:
            break
        distance = distance - i
        count += 1
        i += 1
    return count


def main():
    num = int(input())
    for i in range(1, num+1):
        a = list(map(int, input().split()))
        print(get_count(a[1]-a[0]))

main()