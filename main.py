def solution(record):
    ans = []
    uid = {}
    for i in range(len(record)):
        arr = record[i].split(" ")
        if (arr[0] != "Leave"):
            uid[arr[1]] = arr[len(arr) - 1]

    for i in range(len(record)):
        arr = record[i].split(" ")
        if (arr[0] == "Enter"):
            ans.append(f"{uid[arr[1]]}님이 들어왔습니다.")
        elif (arr[0] == "Leave"):
            ans.append(f"{uid[arr[1]]}님이 나갔습니다.")

    return ans