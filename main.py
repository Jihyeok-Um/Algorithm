temp = int(input())
startNum = 1
endNum = 9
count = 1
result = 0
while (endNum < temp*10):
    if (endNum < temp):
        result += (endNum - startNum + 1) * count
        startNum *= 10
        endNum = (endNum * 10) + 9
        count += 1
    elif (endNum > temp):
        endNum = temp
        result += (endNum - startNum + 1) * count
    else:
        break

print(result)
