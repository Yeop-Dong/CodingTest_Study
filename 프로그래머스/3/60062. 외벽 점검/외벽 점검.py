from itertools import permutations

def solution(n, weak, dist):
    W = len(weak)
    D = len(dist)
    answer = D + 1
    weak = weak + [ w + n for w in weak ]
    
    dist.sort(reverse = True)
    distPD = list(permutations(dist))
    
    for start in range(W):
        for placement in distPD:
            cnt = 1
            right = weak[start] + placement[0]
            for idx in range(start, start+W):
                if right < weak[idx]:
                    cnt += 1
                    if cnt > D or cnt > answer:
                        break
                    right = weak[idx] + placement[cnt - 1]
            answer = min(answer, cnt)
    if answer > D:
        return -1
    return answer
    