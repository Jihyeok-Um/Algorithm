ans = 0

def bruteforce(numbers, current, i, target):
    global ans
    if (i == len(numbers)):
        if (current == target):
            ans += 1
            return
        else:
            return

    bruteforce(numbers, current + numbers[i], i + 1, target)
    bruteforce(numbers, current - numbers[i], i + 1, target)

def solution(numbers, target):
    global ans
    bruteforce(numbers, 0, 0, target)
    return ans