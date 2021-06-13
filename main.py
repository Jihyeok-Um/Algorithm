# 두 개 뽑아서 더하기

def solution(nums):
    get = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if ((nums[i] + nums[j]) not in get):
                get.append(nums[i] + nums[j])

    get.sort()
    return get
