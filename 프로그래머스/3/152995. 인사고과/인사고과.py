from collections import defaultdict
def solution(scores):
    wa, wb = scores[0]
    scores.sort(key = lambda x : (-x[0], x[1]))
    incentives = []
    bmin = 0
    for a, b in scores:
        if bmin < b:
            bmin = b
        if bmin > b:
            if a == wa and b == wb:
                return -1
            continue
        incentives.append([a, b])
    
    incentives.sort(key = lambda x : (-x[0] - x[1]))
    answer = 1
    for a, b in incentives:
        if a + b == wa + wb:
            break
        answer += 1
    return answer