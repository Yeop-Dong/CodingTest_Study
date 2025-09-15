def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue = queue1 + queue2
    total_sum = sum1 + sum2
    if total_sum % 2 != 0:
        return -1
    total_len = len(queue)
    
    i = 0
    j = len(queue1) - 1
    cnt = 0
    
    while sum1 != sum2 and cnt <= total_len * 2:
        if sum1 > sum2:
            sum1 -= queue[i]
            sum2 += queue[i]
            cnt += 1
            i += 1
            if (i == total_len): i = 0
        elif sum1 < sum2:
            j += 1
            if (j == total_len): j = 0
            sum1 += queue[j]
            sum2 -= queue[j]
            cnt += 1
        
    return cnt if cnt <= total_len * 2 else -1