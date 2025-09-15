def solution(cookie):
    answer = 0
    original = [0] + [ c for c in cookie ]
    for i in range(1, len(cookie)):
        cookie[i] += cookie[i - 1]
    cookie = [0] + cookie
    
    for m in range(1, len(cookie) - 1):
        l, r = m, m + 1
        while l > 0 and r < len(cookie):
            left = cookie[m] - cookie[l-1]
            right = cookie[r] - cookie[m]
            if left >= right:
                if left == right:
                    answer = max(answer, left)
                r += 1
            else:
                l -= 1
    return answer