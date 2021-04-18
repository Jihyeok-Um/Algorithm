array = list(map(int,input().split()))
result = 0
for i in range(0, len(array)):
    array[i] = array[i]*array[i]
    result += array[i]
print(result % 10)