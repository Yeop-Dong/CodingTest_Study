def solution(s):
    palmax = 0
    n = len(s)
    for i in range(n):
        l = r = i
        while l >= 0 and r < n:
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        if palmax < r - l - 1:
            palmax = r - l - 1
    
    for i in range(n - 1):
        if s[i] == s[i+1]:
            l = i
            r = i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            if palmax < r - l - 1:
                palmax = r - l - 1
    
    return palmax