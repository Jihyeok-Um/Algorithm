def main():
    max = 0
    sum = list(map(int,input().split()))
    card = list(map(int, input().split()))

    for i in range(0, len(card)):
        for j in range(i+1, len(card)):
            for k in range(j+1, len(card)):
                if card[i] + card[j] + card[k] > max and card[i] + card[j] + card[k] <= sum[1]:
                    max = card[i] + card[j] + card[k]
    print(max)

main()