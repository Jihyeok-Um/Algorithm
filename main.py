matrix = [list(map(int,list(input()))) for _ in range(n)]

#두 개의 표현은 동일하게 작동한다

for i in range(n):
    temp = input()
    small = []
    for i in range(0,m):
        small.append(int(temp[i]))
    matrix.append(small)

