def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start = 0
    end = distance
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        base = 0
        for r in rocks:
            if r - base < mid:
                cnt += 1
            else:
                base = r
        if distance - base < mid:
            cnt += 1
        
        if cnt <= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer