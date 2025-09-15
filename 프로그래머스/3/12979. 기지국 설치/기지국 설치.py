def solution(n, stations, w):
    answer = 0
    reach = 2 * w + 1
    
    start = 1
    for s in stations:
        end = s - w - 1
        if start <= end:
            empty = end - start + 1 
            answer += empty // reach
            if empty % reach > 0:
                answer += 1
        start = s + w + 1
    end = n
    if start <= end:
        empty = end - start + 1
        answer += empty // reach
        if empty % reach > 0:
            answer += 1
    return answer