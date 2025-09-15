first = [1, 1, 0, 1, 1]

def check(i):
    if i % 5 == 2: return 0
    if i < 5: return 1
    return check(i // 5)

def solution(n, l, r):
    answer = 0
    for i in range(l-1, r):
        answer += check(i)
    return answer
    