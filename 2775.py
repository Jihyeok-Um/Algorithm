def get_people_count(column, row):
    array = [[0 for _ in range(14)] for _ in range(15)]
    for x in range(0, 14):
        array[0][x] = x + 1

    row -= 1
    for i in range(column):
        for j in range(row+1):
            for k in range(j+1):
                array[i+1][j] += array[i][k]
    return array[i+1][row]

def main():

    t = int(input())
    for i in range(t):
        k = int(input())
        n = int(input())
        print(get_people_count(k, n))

main()