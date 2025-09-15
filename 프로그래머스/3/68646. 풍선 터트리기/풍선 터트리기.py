def solution(a):
    answer = 0
    
    left = [1000000001]
    right = [1000000001]
    for n in a:
        left.append(min(left[-1], n))
    for n in reversed(a):
        right.append(min(right[-1], n))
    right = list(reversed(right[:-1]))
    
    for i, n in enumerate(a):
        if n < left[i] or n < right[i]:
            answer += 1
    return answer