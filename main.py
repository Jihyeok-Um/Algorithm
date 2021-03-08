def short_time(x,y,w,h):
    shortest = x
    if (w-x < shortest):
        shortest = w-x
    if (y < shortest):
        shortest = y
    if (h-y < shortest):
        shortest = h-y

    print(shortest)

def main():
    num = list(map(int,input().split()))
    short_time(num[0],num[1],num[2],num[3])
main()