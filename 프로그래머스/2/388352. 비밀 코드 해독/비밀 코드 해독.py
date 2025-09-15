import itertools

def solution(n, q, ans):
    answer = 0
    nums = [i for i in range(1, n+1)]
    
    combs = list(itertools.combinations(nums, 5))
    
    for c in combs:
        setc = set(c)
        
        cnt = 0
        for i, qi in enumerate(q):
            inter = setc & set(qi)
            if len(inter) != ans[i]:
                break
            cnt += 1
        if cnt == len(q):
            answer += 1
    return answer