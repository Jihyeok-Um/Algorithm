def solution(nums):
    get = []
    for i in range(len(nums)):
        if (len(get) == len(nums) / 2):
            return len(get)

        if (nums[i] not in get):
            get.append(nums[i])

    return len(get)