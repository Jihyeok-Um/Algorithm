def solution(numbers, hand):
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 12]]
    left = [3, 0]
    right = [3, 2]
    answer = ''

    for i in range(len(numbers)):
        if (numbers[i] == 1):
            answer += "L"
            left = [0, 0]
        elif (numbers[i] == 4):
            answer += "L"
            left = [1, 0]
        elif (numbers[i] == 7):
            answer += "L"
            left = [2, 0]
        elif (numbers[i] == 3):
            answer += "R"
            right = [0, 2]
        elif (numbers[i] == 6):
            answer += "R"
            right = [1, 2]
        elif (numbers[i] == 9):
            answer += "R"
            right = [2, 2]
        elif (numbers[i] == 2):
            ld = abs(left[0] - 0) + abs(left[1] - 1)
            rd = abs(right[0] - 0) + abs(right[1] - 1)
            if (ld < rd):
                answer += "L"
                left = [0, 1]
            elif (ld > rd):
                answer += "R"
                right = [0, 1]
            else:
                if (hand == "right"):
                    answer += "R"
                    right = [0, 1]
                else:
                    answer += "L"
                    left = [0, 1]
        elif (numbers[i] == 5):
            ld = abs(left[0] - 1) + abs(left[1] - 1)
            rd = abs(right[0] - 1) + abs(right[1] - 1)
            if (ld < rd):
                answer += "L"
                left = [1, 1]
            elif (ld > rd):
                answer += "R"
                right = [1, 1]
            else:
                if (hand == "right"):
                    answer += "R"
                    right = [1, 1]
                else:
                    answer += "L"
                    left = [1, 1]
        elif (numbers[i] == 8):
            ld = abs(left[0] - 2) + abs(left[1] - 1)
            rd = abs(right[0] - 2) + abs(right[1] - 1)
            if (ld < rd):
                answer += "L"
                left = [2, 1]
            elif (ld > rd):
                answer += "R"
                right = [2, 1]
            else:
                if (hand == "right"):
                    answer += "R"
                    right = [2, 1]
                else:
                    answer += "L"
                    left = [2, 1]
        elif (numbers[i] == 0):
            ld = abs(left[0] - 3) + abs(left[1] - 1)
            rd = abs(right[0] - 3) + abs(right[1] - 1)
            if (ld < rd):
                answer += "L"
                left = [3, 1]
            elif (ld > rd):
                answer += "R"
                right = [3, 1]
            else:
                if (hand == "right"):
                    answer += "R"
                    right = [3, 1]
                else:
                    answer += "L"
                    left = [3, 1]

    return answer