# 자연수 뒤집어 배열로 만들기

def solution(n):
    a = str(n)
    result = []
    for i in a:
        result.append(int(i))

    result.reverse()
    return result
