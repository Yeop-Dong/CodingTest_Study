from itertools import combinations
from collections import defaultdict
def solution(a):
    answer = 0
    A = len(a)
    
    if A < 2:
        return 0
    
    nums = defaultdict(list)
    for i, e in enumerate(a):
        nums[e].append(i)
        
    for n in nums:
        cnt = 0
        lasti = -1
        for i, idx in enumerate(nums[n]):
            if lasti + 1 == idx:
                # chk right
                lasti = idx
                if idx + 1 >= A:
                    break
                if i + 1 < len(nums[n]) and idx + 1 == nums[n][i+1]:
                    continue
                lasti += 1
            else:
                lasti = idx
            cnt += 1
        answer = max(answer, cnt * 2)
        
    return answer