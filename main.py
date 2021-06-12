# 문자열 내림차순으로 배치하기

def solution(s):
    temp = [i for i in s]
    temp.sort(reverse=True)
    ans = ""
    for i in range(len(temp)):
        ans += temp[i]

    return ans
