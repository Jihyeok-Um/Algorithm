def fibonaci(num):
    if (num == 0):
        return 0
    if (num == 1):
        d[num] = 1
        return d[num]
    if (d[num] != 0):
        return d[num]
    else:
        d[num] = fibonaci(num-1) + fibonaci(num-2)
        return d[num]

d = [0 for i in range(91)]
num = int(input())
fibonaci(num)
print(d[num])