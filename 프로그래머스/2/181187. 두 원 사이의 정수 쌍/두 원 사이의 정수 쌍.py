import math
def solution(r1, r2):
    answer = 0
    pow1 = math.pow(r1, 2)
    pow2 = math.pow(r2, 2)
    for x in range(-r2, r2 + 1):
        answer += math.floor(math.sqrt(pow2 - math.pow(x, 2))) * 2 + 1
    for x in range(-r1, r1 + 1):
        minus = math.sqrt(pow1 - math.pow(x, 2))
        if minus == 0: 
            continue
        elif math.floor(minus) == minus:
            answer -= (math.floor(minus) - 1) * 2 + 1
        else:
            answer -= math.floor(minus) * 2 + 1
    return answer