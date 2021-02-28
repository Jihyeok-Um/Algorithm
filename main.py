Case = int(input())
num_list = list(map(int, input().split()))
print(num_list)
print('{} {}'.format(min(num_list), max(num_list)))

num = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[0], num_list[num - 1])